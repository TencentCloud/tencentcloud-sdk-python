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
        :param HighlightConfigure: 智能精彩集锦任务控制参数。
        :type HighlightConfigure: :class:`tencentcloud.vod.v20180717.models.HighlightsConfigureInfo`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.HighlightConfigure = None
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
        if params.get("HighlightConfigure") is not None:
            self.HighlightConfigure = HighlightsConfigureInfo()
            self.HighlightConfigure._deserialize(params.get("HighlightConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AIRecognitionTemplateItem(AbstractModel):
    """视频内容识别模板详情

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        :param Name: 视频内容识别模板名称。
        :type Name: str
        :param Comment: 视频内容识别模板描述信息。
        :type Comment: str
        :param HeadTailConfigure: 头尾识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadTailConfigure: :class:`tencentcloud.vod.v20180717.models.HeadTailConfigureInfo`
        :param SegmentConfigure: 拆条识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentConfigure: :class:`tencentcloud.vod.v20180717.models.SegmentConfigureInfo`
        :param FaceConfigure: 人脸识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceConfigure: :class:`tencentcloud.vod.v20180717.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本关键词识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 语音全文识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 语音关键词识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.AsrWordsConfigureInfo`
        :param ObjectConfigure: 物体识别控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectConfigure: :class:`tencentcloud.vod.v20180717.models.ObjectConfigureInfo`
        :param ScreenshotInterval: 截图时间间隔，单位：秒。
        :type ScreenshotInterval: float
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.SegmentConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfo()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
        if params.get("SegmentConfigure") is not None:
            self.SegmentConfigure = SegmentConfigureInfo()
            self.SegmentConfigure._deserialize(params.get("SegmentConfigure"))
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfo()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AccelerateAreaInfo(AbstractModel):
    """域名的地区加速信息

    """

    def __init__(self):
        """
        :param Area: 加速地区，可选值：
<li>Chinese Mainland：中国境内（不包含港澳台）。</li>
<li>Outside Chinese Mainland：中国境外。</li>
        :type Area: str
        :param TencentDisableReason: 腾讯禁用原因，可选值：
<li>ForLegalReasons：因法律原因导致关闭加速；</li>
<li>ForOverdueBills：因欠费停服导致关闭加速。</li>
        :type TencentDisableReason: str
        :param TencentEdgeDomain: 加速域名对应的 CNAME 域名。
        :type TencentEdgeDomain: str
        """
        self.Area = None
        self.TencentDisableReason = None
        self.TencentEdgeDomain = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.TencentDisableReason = params.get("TencentDisableReason")
        self.TencentEdgeDomain = params.get("TencentEdgeDomain")


class AdaptiveDynamicStreamingInfoItem(AbstractModel):
    """转自适应码流信息

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流规格。
        :type Definition: int
        :param Package: 打包格式，只能为 HLS。
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
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
        :type WatermarkSet: list of WatermarkInput
        :param SubtitleSet: 字幕列表，元素为字幕 ID，支持多个字幕，最大可支持10个。
        :type SubtitleSet: list of str
        """
        self.Definition = None
        self.WatermarkSet = None
        self.SubtitleSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        self.SubtitleSet = params.get("SubtitleSet")


class AdaptiveDynamicStreamingTemplate(AbstractModel):
    """转自适应码流模板详情

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 转自适应码流模板名称。
        :type Name: str
        :param Comment: 转自适应码流模板描述信息。
        :type Comment: str
        :param Format: 自适应转码格式，取值范围：
<li>HLS。</li>
        :type Format: str
        :param DrmType: DRM 类型，取值范围：
<li>FairPlay；</li>
<li>SimpleAES；</li>
<li>Widevine。</li>
如果取值为空字符串，代表不对视频做 DRM 保护。
        :type DrmType: str
        :param StreamInfos: 自适应转码输入流参数信息，最多输入10路流。
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoResolution: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Format = None
        self.DrmType = None
        self.StreamInfos = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        self.DrmType = params.get("DrmType")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AdaptiveStreamTemplate(AbstractModel):
    """自适应转码流参数模板

    """

    def __init__(self):
        """
        :param Video: 视频参数信息。
        :type Video: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfo`
        :param Audio: 音频参数信息。
        :type Audio: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfo`
        :param RemoveAudio: 是否移除音频流，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type RemoveAudio: int
        :param RemoveVideo: 是否移除视频流，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type RemoveVideo: int
        """
        self.Video = None
        self.Audio = None
        self.RemoveAudio = None
        self.RemoveVideo = None


    def _deserialize(self, params):
        if params.get("Video") is not None:
            self.Video = VideoTemplateInfo()
            self.Video._deserialize(params.get("Video"))
        if params.get("Audio") is not None:
            self.Audio = AudioTemplateInfo()
            self.Audio._deserialize(params.get("Audio"))
        self.RemoveAudio = params.get("RemoveAudio")
        self.RemoveVideo = params.get("RemoveVideo")


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
<li>Highlight：智能精彩集锦</li>
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
        :param HighlightTask: 视频内容分析智能精彩集锦任务的查询结果，当任务类型为 Highlight 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type HighlightTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskHighlightResult`
        """
        self.Type = None
        self.ClassificationTask = None
        self.CoverTask = None
        self.TagTask = None
        self.FrameTagTask = None
        self.HighlightTask = None


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
        if params.get("HighlightTask") is not None:
            self.HighlightTask = AiAnalysisTaskHighlightResult()
            self.HighlightTask._deserialize(params.get("HighlightTask"))


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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskFrameTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskFrameTagOutput()
            self.Output._deserialize(params.get("Output"))


class AiAnalysisTaskHighlightInput(AbstractModel):
    """智能精彩片段任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能精彩片段模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskHighlightOutput(AbstractModel):
    """智能精彩片段结果信息

    """

    def __init__(self):
        """
        :param HighlightSet: 视频智能精彩片段列表。
        :type HighlightSet: list of MediaAiAnalysisHighlightItem
        """
        self.HighlightSet = None


    def _deserialize(self, params):
        if params.get("HighlightSet") is not None:
            self.HighlightSet = []
            for item in params.get("HighlightSet"):
                obj = MediaAiAnalysisHighlightItem()
                obj._deserialize(item)
                self.HighlightSet.append(obj)


class AiAnalysisTaskHighlightResult(AbstractModel):
    """智能精彩片段结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能精彩片段任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskHighlightInput`
        :param Output: 智能精彩片段任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskHighlightOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskHighlightInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskHighlightOutput()
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
<li>Terrorism.Ocr：Ocr 文字鉴恐</li>
<li>Prohibited.Asr：Asr 文字鉴违禁</li>
<li>Prohibited.Ocr：Ocr 文字鉴违禁</li>
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
        :param TerrorismOcrTask: 视频内容审核 Ocr 文字鉴恐任务的查询结果，当任务类型为 Terrorism.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskTerrorismOcrResult`
        :param ProhibitedAsrTask: 视频内容审核 Asr 文字鉴违禁任务的查询结果，当任务类型为 Prohibited.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProhibitedAsrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskProhibitedAsrResult`
        :param ProhibitedOcrTask: 视频内容审核 Ocr 文字鉴违禁任务的查询结果，当任务类型为 Prohibited.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProhibitedOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskProhibitedOcrResult`
        """
        self.Type = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None
        self.TerrorismOcrTask = None
        self.ProhibitedAsrTask = None
        self.ProhibitedOcrTask = None


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
        if params.get("TerrorismOcrTask") is not None:
            self.TerrorismOcrTask = AiReviewTaskTerrorismOcrResult()
            self.TerrorismOcrTask._deserialize(params.get("TerrorismOcrTask"))
        if params.get("ProhibitedAsrTask") is not None:
            self.ProhibitedAsrTask = AiReviewTaskProhibitedAsrResult()
            self.ProhibitedAsrTask._deserialize(params.get("ProhibitedAsrTask"))
        if params.get("ProhibitedOcrTask") is not None:
            self.ProhibitedOcrTask = AiReviewTaskProhibitedOcrResult()
            self.ProhibitedOcrTask._deserialize(params.get("ProhibitedOcrTask"))


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
<li>AsrWordsRecognition：语音关键词识别，</li>
<li>OcrWordsRecognition：文本关键词识别，</li>
<li>AsrFullTextRecognition：语音全文识别，</li>
<li>OcrFullTextRecognition：文本全文识别，</li>
<li>HeadTailRecognition：视频片头片尾识别，</li>
<li>ObjectRecognition：物体识别。</li>
        :type Type: str
        :param HeadTailTask: 视频片头片尾识别结果，当 Type 为
 HeadTailRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadTailTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResult`
        :param SegmentTask: 视频拆条识别结果，当 Type 为
 SegmentRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskSegmentResult`
        :param FaceTask: 人脸识别结果，当 Type 为 
 FaceRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskFaceResult`
        :param AsrWordsTask: 语音关键词识别结果，当 Type 为
 AsrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrWordsTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResult`
        :param AsrFullTextTask: 语音全文识别结果，当 Type 为
 AsrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrFullTextTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResult`
        :param OcrWordsTask: 文本关键词识别结果，当 Type 为
 OcrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrWordsTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResult`
        :param OcrFullTextTask: 文本全文识别结果，当 Type 为
 OcrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrFullTextTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResult`
        :param ObjectTask: 物体识别结果，当 Type 为
 ObjectRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskObjectResult`
        """
        self.Type = None
        self.HeadTailTask = None
        self.SegmentTask = None
        self.FaceTask = None
        self.AsrWordsTask = None
        self.AsrFullTextTask = None
        self.OcrWordsTask = None
        self.OcrFullTextTask = None
        self.ObjectTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("HeadTailTask") is not None:
            self.HeadTailTask = AiRecognitionTaskHeadTailResult()
            self.HeadTailTask._deserialize(params.get("HeadTailTask"))
        if params.get("SegmentTask") is not None:
            self.SegmentTask = AiRecognitionTaskSegmentResult()
            self.SegmentTask._deserialize(params.get("SegmentTask"))
        if params.get("FaceTask") is not None:
            self.FaceTask = AiRecognitionTaskFaceResult()
            self.FaceTask._deserialize(params.get("FaceTask"))
        if params.get("AsrWordsTask") is not None:
            self.AsrWordsTask = AiRecognitionTaskAsrWordsResult()
            self.AsrWordsTask._deserialize(params.get("AsrWordsTask"))
        if params.get("AsrFullTextTask") is not None:
            self.AsrFullTextTask = AiRecognitionTaskAsrFullTextResult()
            self.AsrFullTextTask._deserialize(params.get("AsrFullTextTask"))
        if params.get("OcrWordsTask") is not None:
            self.OcrWordsTask = AiRecognitionTaskOcrWordsResult()
            self.OcrWordsTask._deserialize(params.get("OcrWordsTask"))
        if params.get("OcrFullTextTask") is not None:
            self.OcrFullTextTask = AiRecognitionTaskOcrFullTextResult()
            self.OcrFullTextTask._deserialize(params.get("OcrFullTextTask"))
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
    """语音全文识别结果。

    """

    def __init__(self):
        """
        :param SegmentSet: 语音全文识别片段列表。
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
    """语音关键词识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 语音关键词识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultInput`
        :param Output: 语音关键词识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskAsrWordsResultInput(AbstractModel):
    """语音关键词识别输入。

    """

    def __init__(self):
        """
        :param Definition: 语音关键词识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskAsrWordsResultItem(AbstractModel):
    """语音关键词识别结果。

    """

    def __init__(self):
        """
        :param Word: 语音关键词。
        :type Word: str
        :param SegmentSet: 语音关键词出现的时间片段列表。
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
    """语音关键词识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 语音关键词识别结果集。
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param Definition: 视频智能识别模板 ID 。
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
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
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
    """文本关键识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 文本关键词识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultInput`
        :param Output: 文本关键词识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskOcrWordsResultInput(AbstractModel):
    """文本关键词识别输入。

    """

    def __init__(self):
        """
        :param Definition: 文本关键词识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskOcrWordsResultItem(AbstractModel):
    """文本关键词识别结果。

    """

    def __init__(self):
        """
        :param Word: 文本关键词。
        :type Word: str
        :param SegmentSet: 文本关键出现的片段列表。
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
    """文本关键词识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 文本关键词识别结果集。
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


class AiRecognitionTaskSegmentResult(AbstractModel):
    """视频拆条结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 视频拆条任务输入信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskSegmentResultInput`
        :param Output: 视频拆条任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskSegmentResultOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskSegmentResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskSegmentResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskSegmentResultInput(AbstractModel):
    """视频拆条输入。

    """

    def __init__(self):
        """
        :param Definition: 视频拆条模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskSegmentResultOutput(AbstractModel):
    """视频拆条输出。

    """

    def __init__(self):
        """
        :param SegmentSet: 视频拆条片段列表。
        :type SegmentSet: list of AiRecognitionTaskSegmentSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskSegmentSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskSegmentSegmentItem(AbstractModel):
    """视频拆条片段。

    """

    def __init__(self):
        """
        :param FileId: 文件 ID。仅当处理的是点播文件并且拆条生成的子片段为点播文件时有效。
        :type FileId: str
        :param SegmentUrl: 视频拆条片段 Url。
        :type SegmentUrl: str
        :param Confidence: 拆条片段置信度。取值：0~100。
        :type Confidence: float
        :param StartTimeOffset: 拆条片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 拆条片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param CovImgUrl: 拆条封面图片 Url。
        :type CovImgUrl: str
        :param SpecialInfo: 特殊字段，请忽略。
        :type SpecialInfo: str
        """
        self.FileId = None
        self.SegmentUrl = None
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.CovImgUrl = None
        self.SpecialInfo = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.SegmentUrl = params.get("SegmentUrl")
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.CovImgUrl = params.get("CovImgUrl")
        self.SpecialInfo = params.get("SpecialInfo")


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
        :type Confidence: float
        :param Suggestion: Asr 文字涉政、敏感结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉政、敏感嫌疑的视频片段列表。
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
        :type Confidence: float
        :param Suggestion: 涉政结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 视频鉴政结果标签。内容审核模板[画面鉴政任务控制参数](https://cloud.tencent.com/document/api/266/31773#PoliticalImgReviewTemplateInfo)里 LabelSet 参数与此参数取值范围的对应关系：
violation_photo：
<li>violation_photo：违规图标。</li>
其他（即 politician/entertainment/sport/entrepreneur/scholar/celebrity/military）：
<li>politician：政治人物。</li>
        :type Label: str
        :param SegmentSet: 有涉政嫌疑的视频片段列表。
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
        :type Confidence: float
        :param Suggestion: Asr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉黄嫌疑的视频片段列表。
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
        :type Confidence: float
        :param Suggestion: Ocr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉黄嫌疑的视频片段列表。
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
        :type Confidence: float
        :param Suggestion: 鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 视频鉴黄结果标签，取值范围：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：亲密行为。</li>
        :type Label: str
        :param SegmentSet: 有涉黄嫌疑的视频片段列表。
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


class AiReviewProhibitedAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴违禁任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴违禁模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewProhibitedAsrTaskOutput(AbstractModel):
    """Asr 文字涉违禁信息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉违禁评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Asr 文字涉违禁结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉违禁嫌疑的视频片段列表。
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


class AiReviewProhibitedOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴违禁任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴违禁模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewProhibitedOcrTaskOutput(AbstractModel):
    """Ocr 文字涉违禁信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉违禁评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉违禁结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉违禁嫌疑的视频片段列表。
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


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Asr 文字鉴政任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskInput`
        :param Output: 内容审核 Asr 文字鉴政任务输出。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴政任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴政任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核鉴政任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalTaskInput`
        :param Output: 内容审核鉴政任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Asr 文字鉴黄任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornAsrTaskInput`
        :param Output: 内容审核 Asr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴黄任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核鉴黄任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornTaskInput`
        :param Output: 内容审核鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskProhibitedAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴任违禁务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Asr 文字鉴违禁任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedAsrTaskInput`
        :param Output: 内容审核 Asr 文字鉴违禁任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedAsrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskProhibitedOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴任违禁务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴违禁任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴违禁任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewProhibitedOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskTerrorismOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴恐任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴恐任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴恐任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismOcrTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskTerrorismResult(AbstractModel):
    """内容审核鉴恐任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 内容审核鉴恐任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismTaskInput`
        :param Output: 内容审核鉴恐任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTerrorismOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴恐任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴恐模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewTerrorismOcrTaskOutput(AbstractModel):
    """Ocr 文字涉恐信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉恐评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉恐结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉恐嫌疑的视频片段列表。
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
        :type Confidence: float
        :param Suggestion: 暴恐结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
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
<li>scenario：暴恐画面。</li>
        :type Label: str
        :param SegmentSet: 有暴恐嫌疑的视频片段列表。
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


class AiSampleFaceInfo(AbstractModel):
    """AI 样本管理，人脸信息。

    """

    def __init__(self):
        """
        :param FaceId: 人脸图片 ID。
        :type FaceId: str
        :param Url: 人脸图片地址。
        :type Url: str
        """
        self.FaceId = None
        self.Url = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.Url = params.get("Url")


class AiSampleFaceOperation(AbstractModel):
    """AI 样本管理，人脸数据操作。

    """

    def __init__(self):
        """
        :param Type: 操作类型，可选值：add（添加）、delete（删除）、reset（重置）。重置操作将清空该人物已有人脸数据，并添加 FaceContents 指定人脸数据。
        :type Type: str
        :param FaceIds: 人脸 ID 集合，当 Type为delete 时，该字段必填。
        :type FaceIds: list of str
        :param FaceContents: 人脸图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串集合。
<li>当 Type为add 或 reset 时，该字段必填；</li>
<li>数组长度限制：5 张图片。</li>
注意：图片必须是单人像正面人脸较清晰的照片，像素不低于 200*200。
        :type FaceContents: list of str
        """
        self.Type = None
        self.FaceIds = None
        self.FaceContents = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FaceIds = params.get("FaceIds")
        self.FaceContents = params.get("FaceContents")


class AiSampleFailFaceInfo(AbstractModel):
    """AI 样本管理，处理失败的人脸信息

    """

    def __init__(self):
        """
        :param Index: 对应入参 FaceContents 中错误图片下标，从 0 开始。
        :type Index: int
        :param ErrCode: 错误码，取值：
<li>0：成功；</li>
<li>其他：失败。</li>
        :type ErrCode: int
        :param Message: 错误描述。
        :type Message: str
        """
        self.Index = None
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")


class AiSamplePerson(AbstractModel):
    """AI 样本管理，人物信息。

    """

    def __init__(self):
        """
        :param PersonId: 人物 ID。
        :type PersonId: str
        :param Name: 人物名称。
        :type Name: str
        :param Description: 人物描述。
        :type Description: str
        :param FaceInfoSet: 人脸信息。
        :type FaceInfoSet: list of AiSampleFaceInfo
        :param TagSet: 人物标签。
        :type TagSet: list of str
        :param UsageSet: 应用场景。
        :type UsageSet: list of str
        :param CreateTime: 创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.FaceInfoSet = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = AiSampleFaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AiSampleTagOperation(AbstractModel):
    """AI 样本管理，标签操作。

    """

    def __init__(self):
        """
        :param Type: 操作类型，可选值：add（添加）、delete（删除）、reset（重置）。
        :type Type: str
        :param Tags: 标签，长度限制：128 个字符。
        :type Tags: list of str
        """
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tags = params.get("Tags")


class AiSampleWord(AbstractModel):
    """AI 样本管理，关键词输出信息。

    """

    def __init__(self):
        """
        :param Keyword: 关键词。
        :type Keyword: str
        :param TagSet: 关键词标签。
        :type TagSet: list of str
        :param UsageSet: 关键词应用场景。
        :type UsageSet: list of str
        :param CreateTime: 创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Keyword = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AiSampleWordInfo(AbstractModel):
    """AI 样本管理，关键词输入信息。

    """

    def __init__(self):
        """
        :param Keyword: 关键词，长度限制：20 个字符。
        :type Keyword: str
        :param Tags: 关键词标签
<li>数组长度限制：20 个标签；</li>
<li>单个标签长度限制：128 个字符。</li>
        :type Tags: list of str
        """
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Tags = params.get("Tags")


class AnimatedGraphicTaskInput(AbstractModel):
    """转动图任务类型

    """

    def __init__(self):
        """
        :param Definition: 视频转动图模板 ID
        :type Definition: int
        :param StartTimeOffset: 动图在视频中的起始时间偏移，单位为秒。
<li>不填或填0，表示从视频的起始位置开始；</li>
<li>当数值大于0时（假设为 n），表示从视频的第 n 秒位置开始；</li>
<li>当数值小于0时（假设为 -n），表示从视频结束 n 秒前的位置开始。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的终止时间偏移，单位为秒。
<li>不填或填0，表示持续到视频的末尾终止；</li>
<li>当数值大于0时（假设为 n），表示持续到视频第 n 秒时终止；</li>
<li>当数值小于0时（假设为 -n），表示持续到视频结束 n 秒前终止。</li>
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class AnimatedGraphicsTemplate(AbstractModel):
    """转动图模板详情。

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 转动图模板名称。
        :type Name: str
        :param Comment: 转动图模板描述信息。
        :type Comment: str
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 动图格式。
        :type Format: str
        :param Fps: 帧率。
        :type Fps: int
        :param Quality: 图片质量。
        :type Quality: float
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ApplyUploadRequest(AbstractModel):
    """ApplyUpload请求参数结构体

    """

    def __init__(self):
        """
        :param MediaType: 媒体类型，可选值请参考 [上传能力综述](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type MediaType: str
        :param MediaName: 媒体名称。
        :type MediaName: str
        :param CoverType: 封面类型，可选值请参考 [上传能力综述](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type CoverType: str
        :param Procedure: 媒体后续任务处理操作，即完成媒体上传后，可自动发起任务流操作。参数值为任务流模板名，云点播支持 [创建任务流模板](/document/product/266/33819) 并为模板命名。
        :type Procedure: str
        :param ExpireTime: 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type ExpireTime: str
        :param StorageRegion: 指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :type StorageRegion: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/7812) 接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param SourceContext: 来源上下文，用于透传用户请求信息，[上传完成回调](/document/product/266/7830) 将返回该字段值，最长 250 个字符。
        :type SourceContext: str
        :param SessionContext: 会话上下文，用于透传用户请求信息，当指定 Procedure 参数后，[任务流状态变更回调](/document/product/266/9636) 将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
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
        self.SessionContext = None
        self.ExtInfo = None
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
        self.SessionContext = params.get("SessionContext")
        self.ExtInfo = params.get("ExtInfo")
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
        :type MediaStoragePath: str
        :param CoverStoragePath: 封面存储路径，用于上传接口存储封面的对象键（Key）。
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


class AsrFullTextConfigureInfo(AbstractModel):
    """语音全文识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音全文识别任务开关，可选值：
<li>ON：开启智能语音全文识别任务；</li>
<li>OFF：关闭智能语音全文识别任务。</li>
        :type Switch: str
        :param SubtitleFormat: 生成的字幕文件格式，不填或者填空字符串表示不生成字幕文件，可选值：
<li>vtt：生成 WebVTT 字幕文件。</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")


class AsrFullTextConfigureInfoForUpdate(AbstractModel):
    """语音全文识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音全文识别任务开关，可选值：
<li>ON：开启智能语音全文识别任务；</li>
<li>OFF：关闭智能语音全文识别任务。</li>
        :type Switch: str
        :param SubtitleFormat: 生成的字幕文件格式，填空字符串表示不生成字幕文件，可选值：
<li>vtt：生成 WebVTT 字幕文件。</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")


class AsrWordsConfigureInfo(AbstractModel):
    """语音关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音关键词识别任务开关，可选值：
<li>ON：开启语音关键词识别任务；</li>
<li>OFF：关闭语音关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class AsrWordsConfigureInfoForUpdate(AbstractModel):
    """语音关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音关键词识别任务开关，可选值：
<li>ON：开启语音关键词识别任务；</li>
<li>OFF：关闭语音关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class AttachMediaSubtitlesRequest(AbstractModel):
    """AttachMediaSubtitles请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件唯一标识。
        :type FileId: str
        :param Operation: 操作。取值如下：
<li>Attach：关联字幕。</li>
<li>Detach：解除关联字幕。</li>
        :type Operation: str
        :param AdaptiveDynamicStreamingDefinition: [转自适应码流模板号](https://cloud.tencent.com/document/product/266/34071#zsy)。
        :type AdaptiveDynamicStreamingDefinition: int
        :param SubtitleIds: 字幕的唯一标识。
        :type SubtitleIds: list of str
        """
        self.FileId = None
        self.Operation = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.SubtitleIds = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Operation = params.get("Operation")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        self.SubtitleIds = params.get("SubtitleIds")


class AttachMediaSubtitlesResponse(AbstractModel):
    """AttachMediaSubtitles返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AudioTemplateInfo(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
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
当媒体的封装格式是音频格式时（flac，ogg，mp3，m4a）时，声道数不允许设为立体声。
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
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
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
当媒体的封装格式是音频格式时（flac，ogg，mp3，m4a）时，声道数不允许设为立体声。
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


class AudioTrackItem(AbstractModel):
    """音频轨道上的音频片段信息。

    """

    def __init__(self):
        """
        :param SourceMedia: 音频片段的媒体素材来源，可以是：
<li>点播的媒体文件 ID；</li>
<li>其他媒体文件的下载 URL。</li>
注意：当使用其他媒体文件的下载 URL 作为素材来源，且开启了访问控制（如防盗链）时，需要在 URL 携带访问控制参数（如防盗链签名）。
        :type SourceMedia: str
        :param SourceMediaStartTime: 音频片段取自素材文件的起始时间，单位为秒。0 表示从素材开始位置截取。默认为0。
        :type SourceMediaStartTime: float
        :param Duration: 音频片段的时长，单位为秒。默认和素材本身长度一致，表示截取全部素材。
        :type Duration: float
        :param AudioOperations: 对音频片段进行的操作，如音量调节等。
        :type AudioOperations: list of AudioTransform
        """
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None
        self.AudioOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        if params.get("AudioOperations") is not None:
            self.AudioOperations = []
            for item in params.get("AudioOperations"):
                obj = AudioTransform()
                obj._deserialize(item)
                self.AudioOperations.append(obj)


class AudioTransform(AbstractModel):
    """音频操作

    """

    def __init__(self):
        """
        :param Type: 音频操作类型，取值有：
<li>Volume：音量调节。</li>
        :type Type: str
        :param VolumeParam: 音量调节参数， 当 Type = Volume 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeParam: :class:`tencentcloud.vod.v20180717.models.AudioVolumeParam`
        """
        self.Type = None
        self.VolumeParam = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VolumeParam") is not None:
            self.VolumeParam = AudioVolumeParam()
            self.VolumeParam._deserialize(params.get("VolumeParam"))


class AudioVolumeParam(AbstractModel):
    """音频增益调节参数

    """

    def __init__(self):
        """
        :param Mute: 是否静音，取值范围0或1。
<li>0表示不静音。</li>
<li>1表示静音。</li>
默认是0。
        :type Mute: int
        :param Gain: 音频增益，取值范围0~10。
<li>大于1表示增加音量。</li>
<li>小于1表示降低音量。</li>
<li>0和1：表示不改变。</li>
默认是0。
        :type Gain: float
        """
        self.Mute = None
        self.Gain = None


    def _deserialize(self, params):
        self.Mute = params.get("Mute")
        self.Gain = params.get("Gain")


class Canvas(AbstractModel):
    """画布信息。制作视频时，如果源素材（视频或者图片）不能填满输出的视频窗口，将用设置的画布进行背景绘制。

    """

    def __init__(self):
        """
        :param Color: 背景颜色，取值有：
<li>Black：黑色背景</li>
<li>White：白色背景</li>
默认值：Black。
        :type Color: str
        :param Width: 画布宽度，即输出视频的宽度，取值范围：0~ 4096，单位：px。
默认值：0，表示和第一个视频轨的第一个视频片段的视频宽度一致。
        :type Width: int
        :param Height: 画布高度，即输出视频的高度（或长边），取值范围：0~ 4096，单位：px。
默认值：0，表示和第一个视频轨的第一个视频片段的视频高度一致。
        :type Height: int
        """
        self.Color = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Color = params.get("Color")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class CdnLogInfo(AbstractModel):
    """CDN 日志信息

    """

    def __init__(self):
        """
        :param Date: 日志所属日期， 格式为：yyyy-MM-dd ，如2018-03-01。
        :type Date: str
        :param Name: 日志名称，格式为：日期小时-域名
如 2018120101-test.vod2.mqcloud.com。
        :type Name: str
        :param Url: 日志下载链接，24小时内下载有效。
        :type Url: str
        :param StartTime: 日志起始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type StartTime: str
        :param EndTime: 日志结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type EndTime: str
        """
        self.Date = None
        self.Name = None
        self.Url = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Name = params.get("Name")
        self.Url = params.get("Url")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


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
        :type ErrCode: int
        :param Message: 错误描述。
        :type Message: str
        :param FileId: 输出目标文件的文件 ID。
        :type FileId: str
        :param FileUrl: 输出目标文件的文件地址。
        :type FileUrl: str
        :param FileType: 输出目标文件的文件类型。
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


class ComposeMediaOutput(AbstractModel):
    """输出的媒体文件信息。

    """

    def __init__(self):
        """
        :param FileName: 文件名称，最长 64 个字符。
        :type FileName: str
        :param Description: 描述信息，最长 128 个字符。
        :type Description: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/7812) 接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param ExpireTime: 输出文件的过期时间，超过该时间文件将被删除，默认为永久不过期，格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        :param Container: 封装格式，可选值：mp4、mp3。其中，mp3 为纯音频文件。
        :type Container: str
        :param VideoStream: 输出的视频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoStream: :class:`tencentcloud.vod.v20180717.models.OutputVideoStream`
        :param AudioStream: 输出的音频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioStream: :class:`tencentcloud.vod.v20180717.models.OutputAudioStream`
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
        """
        self.FileName = None
        self.Description = None
        self.ClassId = None
        self.ExpireTime = None
        self.Container = None
        self.VideoStream = None
        self.AudioStream = None
        self.RemoveVideo = None
        self.RemoveAudio = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Description = params.get("Description")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        self.Container = params.get("Container")
        if params.get("VideoStream") is not None:
            self.VideoStream = OutputVideoStream()
            self.VideoStream._deserialize(params.get("VideoStream"))
        if params.get("AudioStream") is not None:
            self.AudioStream = OutputAudioStream()
            self.AudioStream._deserialize(params.get("AudioStream"))
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")


class ComposeMediaRequest(AbstractModel):
    """ComposeMedia请求参数结构体

    """

    def __init__(self):
        """
        :param Tracks: 输入的媒体轨道列表，包括视频、音频、图片等素材组成的多个轨道信息，其中：<li>输入的多个轨道在时间轴上和输出媒体文件的时间轴对齐；</li><li>时间轴上相同时间点的各个轨道的素材进行重叠，视频或者图片按轨道顺序进行图像的叠加，轨道顺序高的素材叠加在上面，音频素材进行混音；</li><li>视频、音频、图片，每一种类型的轨道最多支持10个。</li>
        :type Tracks: list of MediaTrack
        :param Output: 输出的媒体文件信息。
        :type Output: :class:`tencentcloud.vod.v20180717.models.ComposeMediaOutput`
        :param Canvas: 制作视频文件时使用的画布。
        :type Canvas: :class:`tencentcloud.vod.v20180717.models.Canvas`
        :param SessionContext: 标识来源上下文，用于透传用户请求信息，在ComposeMediaComplete回调将返回该字段值，最长 1000个字符。
        :type SessionContext: str
        :param SessionId: 用于任务去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Tracks = None
        self.Output = None
        self.Canvas = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self.Tracks = []
            for item in params.get("Tracks"):
                obj = MediaTrack()
                obj._deserialize(item)
                self.Tracks.append(obj)
        if params.get("Output") is not None:
            self.Output = ComposeMediaOutput()
            self.Output._deserialize(params.get("Output"))
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")


class ComposeMediaResponse(AbstractModel):
    """ComposeMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 制作媒体文件的任务 ID，可以通过该 ID 查询制作任务（任务类型为 MakeMedia）的状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ComposeMediaTask(AbstractModel):
    """制作媒体文件任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 制作媒体文件任务的输入。
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTaskInput`
        :param Output: 制作媒体文件任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTaskOutput`
        :param MetaData: 原始视频的元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.MetaData = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ComposeMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = ComposeMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")


class ComposeMediaTaskInput(AbstractModel):
    """制作媒体文件任务的输入。

    """

    def __init__(self):
        """
        :param Tracks: 输入的媒体轨道列表，包括视频、音频、图片等素材组成的多个轨道信息。
        :type Tracks: list of MediaTrack
        :param Canvas: 制作视频文件时使用的画布。
注意：此字段可能返回 null，表示取不到有效值。
        :type Canvas: :class:`tencentcloud.vod.v20180717.models.Canvas`
        :param Output: 输出的媒体文件信息。
        :type Output: :class:`tencentcloud.vod.v20180717.models.ComposeMediaOutput`
        """
        self.Tracks = None
        self.Canvas = None
        self.Output = None


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self.Tracks = []
            for item in params.get("Tracks"):
                obj = MediaTrack()
                obj._deserialize(item)
                self.Tracks.append(obj)
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        if params.get("Output") is not None:
            self.Output = ComposeMediaOutput()
            self.Output._deserialize(params.get("Output"))


class ComposeMediaTaskOutput(AbstractModel):
    """制作媒体文件任务的输出。

    """

    def __init__(self):
        """
        :param FileType: 文件类型，例如 mp4、mp3 等。
        :type FileType: str
        :param FileId: 媒体文件 ID。
        :type FileId: str
        :param FileUrl: 媒体文件播放地址。
        :type FileUrl: str
        :param MediaName: 文件名称，最长 64 个字符。
        :type MediaName: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/7812) 接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param ExpireTime: 输出文件的过期时间，超过该时间文件将被删除，默认为永久不过期，格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        """
        self.FileType = None
        self.FileId = None
        self.FileUrl = None
        self.MediaName = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.MediaName = params.get("MediaName")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")


class ConcatFileInfo2017(AbstractModel):
    """视频拼接源文件信息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param FileId: 视频拼接源文件的 ID。
        :type FileId: str
        :param FileUrl: 视频拼接源文件的地址。
        :type FileUrl: str
        :param FileType: 视频拼接源文件的格式。
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
        :param EventHandles: 事件句柄，即 [拉取事件通知](/document/product/266/33433) 接口输出参数中的 EventSet. EventHandle 字段。
数组长度限制：16。
        :type EventHandles: list of str
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.EventHandles = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.EventHandles = params.get("EventHandles")
        self.ExtInfo = params.get("ExtInfo")
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


class ContentReviewTemplateItem(AbstractModel):
    """内容审核模板详情

    """

    def __init__(self):
        """
        :param Definition: 内容审核模板唯一标识。
        :type Definition: int
        :param Name: 内容审核模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 内容审核模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param PornConfigure: 鉴黄控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornConfigure: :class:`tencentcloud.vod.v20180717.models.PornConfigureInfo`
        :param TerrorismConfigure: 鉴恐控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismConfigure: :class:`tencentcloud.vod.v20180717.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 鉴政控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalConfigure: :class:`tencentcloud.vod.v20180717.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProhibitedConfigure: :class:`tencentcloud.vod.v20180717.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: 用户自定义内容审核控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefineConfigure: :class:`tencentcloud.vod.v20180717.models.UserDefineConfigureInfo`
        :param ReviewWallSwitch: 审核结果是否进入审核墙（对审核结果进行人工复核）的开关。
<li>ON：是；</li>
<li>OFF：否。</li>
        :type ReviewWallSwitch: str
        :param ScreenshotInterval: 截帧间隔，单位为秒。当不填时，默认截帧间隔为 1 秒，最小值为 0.5 秒。
        :type ScreenshotInterval: float
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.ReviewWallSwitch = None
        self.ScreenshotInterval = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


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
        :param HighlightConfigure: 智能精彩集锦任务控制参数。
        :type HighlightConfigure: :class:`tencentcloud.vod.v20180717.models.HighlightsConfigureInfo`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.HighlightConfigure = None
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
        if params.get("HighlightConfigure") is not None:
            self.HighlightConfigure = HighlightsConfigureInfo()
            self.HighlightConfigure._deserialize(params.get("HighlightConfigure"))
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


class CreateAIRecognitionTemplateRequest(AbstractModel):
    """CreateAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 视频内容识别模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容识别模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param HeadTailConfigure: 视频片头片尾识别控制参数。
        :type HeadTailConfigure: :class:`tencentcloud.vod.v20180717.models.HeadTailConfigureInfo`
        :param SegmentConfigure: 视频拆条识别控制参数。
        :type SegmentConfigure: :class:`tencentcloud.vod.v20180717.models.SegmentConfigureInfo`
        :param FaceConfigure: 人脸识别控制参数。
        :type FaceConfigure: :class:`tencentcloud.vod.v20180717.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文识别控制参数。
        :type OcrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本关键词识别控制参数。
        :type OcrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 语音全文识别控制参数。
        :type AsrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 语音关键词识别控制参数。
        :type AsrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.AsrWordsConfigureInfo`
        :param ObjectConfigure: 物体识别控制参数。
        :type ObjectConfigure: :class:`tencentcloud.vod.v20180717.models.ObjectConfigureInfo`
        :param ScreenshotInterval: 截帧间隔，单位为秒。当不填时，默认截帧间隔为 1 秒，最小值为 0.5 秒。
        :type ScreenshotInterval: float
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.SegmentConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfo()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
        if params.get("SegmentConfigure") is not None:
            self.SegmentConfigure = SegmentConfigureInfo()
            self.SegmentConfigure._deserialize(params.get("SegmentConfigure"))
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfo()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")


class CreateAIRecognitionTemplateResponse(AbstractModel):
    """CreateAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Format: 自适应转码格式，取值范围：
<li>HLS。</li>
        :type Format: str
        :param StreamInfos: 自适应转码输出子流参数信息，最多输出10路子流。
注意：各个子流的帧率必须保持一致；如果不一致，采用第一个子流的帧率作为输出帧率。
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param Name: 模板名称，长度限制：64 个字符。
        :type Name: str
        :param DrmType: DRM方案类型，取值范围：
<li>SimpleAES。</li>
如果取值为空字符串，代表不对视频做 DRM 保护。
        :type DrmType: str
        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
默认为否。
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
默认为否。
        :type DisableHigherVideoResolution: int
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Format = None
        self.StreamInfos = None
        self.Name = None
        self.DrmType = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Name = params.get("Name")
        self.DrmType = params.get("DrmType")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class CreateAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 自适应转码模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAnimatedGraphicsTemplateRequest(AbstractModel):
    """CreateAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。
        :type Fps: int
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 动图格式，取值为 gif 和 webp。默认为 gif。
        :type Format: str
        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。
        :type Quality: float
        :param Name: 转动图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Fps = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Quality = None
        self.Name = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Quality = params.get("Quality")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class CreateAnimatedGraphicsTemplateResponse(AbstractModel):
    """CreateAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
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


class CreateContentReviewTemplateRequest(AbstractModel):
    """CreateContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param ReviewWallSwitch: 智能识别结果是否进入智能识别墙（对识别结果进行人工复核）的开关。
<li>ON：是；</li>
<li>OFF：否。</li>
        :type ReviewWallSwitch: str
        :param Name: 内容智能识别模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 内容智能识别模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param PornConfigure: 令人反感的信息的控制参数。
        :type PornConfigure: :class:`tencentcloud.vod.v20180717.models.PornConfigureInfo`
        :param TerrorismConfigure: 令人不安全的信息的控制参数。
        :type TerrorismConfigure: :class:`tencentcloud.vod.v20180717.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 令人不适宜的控制参数。
        :type PoliticalConfigure: :class:`tencentcloud.vod.v20180717.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
        :type ProhibitedConfigure: :class:`tencentcloud.vod.v20180717.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: 用户自定义内容智能识别控制参数。
        :type UserDefineConfigure: :class:`tencentcloud.vod.v20180717.models.UserDefineConfigureInfo`
        :param ScreenshotInterval: 截帧间隔，单位为秒。当不填时，默认截帧间隔为 1 秒，最小值为 0.5 秒。
        :type ScreenshotInterval: float
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ReviewWallSwitch = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")


class CreateContentReviewTemplateResponse(AbstractModel):
    """CreateContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 内容智能识别模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateImageProcessingTemplateRequest(AbstractModel):
    """CreateImageProcessingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Operations: 图片处理操作数组，操作将以其在数组中的顺序执行。
<li>长度限制：3。</li>
        :type Operations: list of ImageOperation
        :param Name: 图片处理模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Operations = None
        self.Name = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = ImageOperation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class CreateImageProcessingTemplateResponse(AbstractModel):
    """CreateImageProcessingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 图片处理模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
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
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param FileId: 截取雪碧图文件 ID。
        :type FileId: str
        :param Definition: 雪碧图规格，参见[雪碧图截图模板](https://cloud.tencent.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param TotalCount: 雪碧图小图总数量。
        :type TotalCount: int
        :param ImageSpriteUrlSet: 截取雪碧图输出的地址。
        :type ImageSpriteUrlSet: list of str
        :param WebVttUrl: 雪碧图子图位置与时间关系 WebVtt 文件地址。
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


class CreateImageSpriteTemplateRequest(AbstractModel):
    """CreateImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param Name: 雪碧图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.Name = None
        self.Comment = None
        self.FillType = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SubAppId = params.get("SubAppId")


class CreateImageSpriteTemplateResponse(AbstractModel):
    """CreateImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreatePersonSampleRequest(AbstractModel):
    """CreatePersonSample请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 素材名称，长度限制：20 个字符。
        :type Name: str
        :param Usages: 素材应用场景，可选值：
1. Recognition：用于内容识别，等价于 Recognition.Face。
2. Review：用于内容不适宜，等价于 Review.Face。
3. All：包含以上全部，等价于 1+2。
        :type Usages: list of str
        :param Description: 素材描述，长度限制：1024 个字符。
        :type Description: str
        :param FaceContents: 素材图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串，仅支持 jpeg、png 图片格式。数组长度限制：5 张图片。
注意：图片必须是单人像五官较清晰的照片，像素不低于 200*200。
        :type FaceContents: list of str
        :param Tags: 素材标签
<li>数组长度限制：20 个标签；</li>
<li>单个标签长度限制：128 个字符。</li>
        :type Tags: list of str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.Usages = None
        self.Description = None
        self.FaceContents = None
        self.Tags = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usages = params.get("Usages")
        self.Description = params.get("Description")
        self.FaceContents = params.get("FaceContents")
        self.Tags = params.get("Tags")
        self.SubAppId = params.get("SubAppId")


class CreatePersonSampleResponse(AbstractModel):
    """CreatePersonSample返回参数结构体

    """

    def __init__(self):
        """
        :param Person: 素材信息。
        :type Person: :class:`tencentcloud.vod.v20180717.models.AiSamplePerson`
        :param FailFaceInfoSet: 处理失败的五官定位信息。
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateProcedureTemplateRequest(AbstractModel):
    """CreateProcedureTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务流名字（支持中文，不超过20个字）。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
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
        self.Comment = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
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


class CreateSampleSnapshotTemplateRequest(AbstractModel):
    """CreateSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param Name: 采样截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式，取值为 jpg 和 png。默认为 jpg。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.SampleType = None
        self.SampleInterval = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")


class CreateSampleSnapshotTemplateResponse(AbstractModel):
    """CreateSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式，取值可以为 jpg 和 png。默认为 jpg。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")


class CreateSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 时间点截图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSubAppIdRequest(AbstractModel):
    """CreateSubAppId请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 子应用名称，长度限制：40个字符。
        :type Name: str
        :param Description: 子应用简介，长度限制： 300个字符。
        :type Description: str
        """
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")


class CreateSubAppIdResponse(AbstractModel):
    """CreateSubAppId返回参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 新创建的子应用 ID。
        :type SubAppId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.RequestId = params.get("RequestId")


class CreateSuperPlayerConfigRequest(AbstractModel):
    """CreateSuperPlayerConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 播放器配置名称，长度限制：64 个字符。只允许出现 [0-9a-zA-Z] 及 _- 字符（如 test_ABC-123），同一个用户该名称唯一。
        :type Name: str
        :param DrmSwitch: 播放 DRM 保护的自适应码流开关：
<li>ON：开启，表示仅播放 DRM  保护的自适应码流输出；</li>
<li>OFF：关闭，表示播放未加密的自适应码流输出。</li>
默认为 OFF。
        :type DrmSwitch: str
        :param AdaptiveDynamicStreamingDefinition: 允许输出的未加密的自适应码流模板 ID，当 DrmSwitch 为 OFF 时必填。
        :type AdaptiveDynamicStreamingDefinition: int
        :param DrmStreamingsInfo: 允许输出的 DRM 自适应码流模板内容，当 DrmSwitch 为 ON 时必填。
        :type DrmStreamingsInfo: :class:`tencentcloud.vod.v20180717.models.DrmStreamingsInfo`
        :param ImageSpriteDefinition: 允许输出的雪碧图模板 ID。
        :type ImageSpriteDefinition: int
        :param ResolutionNames: 播放器对不于不同分辨率的子流展示名字，不填或者填空数组则使用默认配置：
<li>MinEdgeLength：240，Name：流畅；</li>
<li>MinEdgeLength：480，Name：标清；</li>
<li>MinEdgeLength：720，Name：高清；</li>
<li>MinEdgeLength：1080，Name：全高清；</li>
<li>MinEdgeLength：1440，Name：2K；</li>
<li>MinEdgeLength：2160，Name：4K；</li>
<li>MinEdgeLength：4320，Name：8K。</li>
        :type ResolutionNames: list of ResolutionNameInfo
        :param Domain: 播放时使用的域名。不填或者填 Default，表示使用[默认分发配置](https://cloud.tencent.com/document/product/266/33373)中的域名。
        :type Domain: str
        :param Scheme: 播放时使用的 Scheme。不填或者填 Default，表示使用[默认分发配置](https://cloud.tencent.com/document/product/266/33373)中的 Scheme。其他可选值：
<li>HTTP；</li>
<li>HTTPS。</li>
        :type Scheme: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.DrmSwitch = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.DrmStreamingsInfo = None
        self.ImageSpriteDefinition = None
        self.ResolutionNames = None
        self.Domain = None
        self.Scheme = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DrmSwitch = params.get("DrmSwitch")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        if params.get("DrmStreamingsInfo") is not None:
            self.DrmStreamingsInfo = DrmStreamingsInfo()
            self.DrmStreamingsInfo._deserialize(params.get("DrmStreamingsInfo"))
        self.ImageSpriteDefinition = params.get("ImageSpriteDefinition")
        if params.get("ResolutionNames") is not None:
            self.ResolutionNames = []
            for item in params.get("ResolutionNames"):
                obj = ResolutionNameInfo()
                obj._deserialize(item)
                self.ResolutionNames.append(obj)
        self.Domain = params.get("Domain")
        self.Scheme = params.get("Scheme")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class CreateSuperPlayerConfigResponse(AbstractModel):
    """CreateSuperPlayerConfig返回参数结构体

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
        :param TEHDConfig: 极速高清转码参数。
        :type TEHDConfig: :class:`tencentcloud.vod.v20180717.models.TEHDConfig`
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
        self.TEHDConfig = None
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
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
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
<li>text：文字水印；</li>
<li>svg：SVG 水印。</li>
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
默认值：TopLeft。
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


class CreateWordSamplesRequest(AbstractModel):
    """CreateWordSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Usages: <b>关键词应用场景，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜内容识别；
4. Review.Asr：通过音频识别技术，进行不适宜内容识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜内容识别，等价于 3+4；
7. All：通过光学字符识别技术、音频识别技术，进行内容识别、不适宜内容识别，等价于 1+2+3+4。
        :type Usages: list of str
        :param Words: 关键词，数组长度限制：100。
        :type Words: list of AiSampleWordInfo
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Usages = None
        self.Words = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = AiSampleWordInfo()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SubAppId = params.get("SubAppId")


class CreateWordSamplesResponse(AbstractModel):
    """CreateWordSamples返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DailyPlayStatInfo(AbstractModel):
    """播放统计信息。

    """

    def __init__(self):
        """
        :param Date: 播放媒体文件的日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type Date: str
        :param FileId: 媒体文件ID。
        :type FileId: str
        :param PlayTimes: 播放次数。
        :type PlayTimes: int
        :param Traffic: 播放流量，单位：字节。
        :type Traffic: int
        """
        self.Date = None
        self.FileId = None
        self.PlayTimes = None
        self.Traffic = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.FileId = params.get("FileId")
        self.PlayTimes = params.get("PlayTimes")
        self.Traffic = params.get("Traffic")


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


class DeleteAIRecognitionTemplateRequest(AbstractModel):
    """DeleteAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteAIRecognitionTemplateResponse(AbstractModel):
    """DeleteAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 自适应转码模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAnimatedGraphicsTemplateRequest(AbstractModel):
    """DeleteAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteAnimatedGraphicsTemplateResponse(AbstractModel):
    """DeleteAnimatedGraphicsTemplate返回参数结构体

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


class DeleteContentReviewTemplateRequest(AbstractModel):
    """DeleteContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 内容智能识别模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteContentReviewTemplateResponse(AbstractModel):
    """DeleteContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageProcessingTemplateRequest(AbstractModel):
    """DeleteImageProcessingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 图片处理模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteImageProcessingTemplateResponse(AbstractModel):
    """DeleteImageProcessingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageSpriteTemplateRequest(AbstractModel):
    """DeleteImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteImageSpriteTemplateResponse(AbstractModel):
    """DeleteImageSpriteTemplate返回参数结构体

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


class DeletePersonSampleRequest(AbstractModel):
    """DeletePersonSample请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 素材 ID。
        :type PersonId: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.PersonId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.SubAppId = params.get("SubAppId")


class DeletePersonSampleResponse(AbstractModel):
    """DeletePersonSample返回参数结构体

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


class DeleteSampleSnapshotTemplateRequest(AbstractModel):
    """DeleteSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteSampleSnapshotTemplateResponse(AbstractModel):
    """DeleteSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSuperPlayerConfigRequest(AbstractModel):
    """DeleteSuperPlayerConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 播放器配置名称。
        :type Name: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SubAppId = params.get("SubAppId")


class DeleteSuperPlayerConfigResponse(AbstractModel):
    """DeleteSuperPlayerConfig返回参数结构体

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


class DeleteWordSamplesRequest(AbstractModel):
    """DeleteWordSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Keywords: 关键词，数组长度限制：100 个词。
        :type Keywords: list of str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Keywords = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.SubAppId = params.get("SubAppId")


class DeleteWordSamplesResponse(AbstractModel):
    """DeleteWordSamples返回参数结构体

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
        :param Definitions: 视频内容分析模板唯一标识过滤条件，数组长度最大值：100。
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


class DescribeAIRecognitionTemplatesRequest(AbstractModel):
    """DescribeAIRecognitionTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 视频内容识别模板唯一标识过滤条件，数组长度限制：100。
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


class DescribeAIRecognitionTemplatesResponse(AbstractModel):
    """DescribeAIRecognitionTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AIRecognitionTemplateSet: 视频内容识别模板详情列表。
        :type AIRecognitionTemplateSet: list of AIRecognitionTemplateItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIRecognitionTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIRecognitionTemplateSet") is not None:
            self.AIRecognitionTemplateSet = []
            for item in params.get("AIRecognitionTemplateSet"):
                obj = AIRecognitionTemplateItem()
                obj._deserialize(item)
                self.AIRecognitionTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAdaptiveDynamicStreamingTemplatesRequest(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转自适应码流模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")


class DescribeAdaptiveDynamicStreamingTemplatesResponse(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AdaptiveDynamicStreamingTemplateSet: 转自适应码流模板详情列表。
        :type AdaptiveDynamicStreamingTemplateSet: list of AdaptiveDynamicStreamingTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AdaptiveDynamicStreamingTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AdaptiveDynamicStreamingTemplateSet") is not None:
            self.AdaptiveDynamicStreamingTemplateSet = []
            for item in params.get("AdaptiveDynamicStreamingTemplateSet"):
                obj = AdaptiveDynamicStreamingTemplate()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTemplateSet.append(obj)
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


class DescribeAnimatedGraphicsTemplatesRequest(AbstractModel):
    """DescribeAnimatedGraphicsTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转动图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")


class DescribeAnimatedGraphicsTemplatesResponse(AbstractModel):
    """DescribeAnimatedGraphicsTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AnimatedGraphicsTemplateSet: 转动图模板详情列表。
        :type AnimatedGraphicsTemplateSet: list of AnimatedGraphicsTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AnimatedGraphicsTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AnimatedGraphicsTemplateSet") is not None:
            self.AnimatedGraphicsTemplateSet = []
            for item in params.get("AnimatedGraphicsTemplateSet"):
                obj = AnimatedGraphicsTemplate()
                obj._deserialize(item)
                self.AnimatedGraphicsTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCDNStatDetailsRequest(AbstractModel):
    """DescribeCDNStatDetails请求参数结构体

    """

    def __init__(self):
        """
        :param Metric: 查询指标，取值有：
<li>Traffic：流量，单位为 Byte。</li>
<li>Bandwidth：带宽，单位为 Bps。</li>
        :type Metric: str
        :param StartTime: 起始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param DomainNames: 域名列表。一次最多查询20个域名的数据。默认返回所有域名叠加的用量数据。
        :type DomainNames: list of str
        :param Area: 服务区域，取值有：
<li>Chinese Mainland：中国大陆。 </li>
<li>Asia Pacific Region 1：亚太一区，包括中国香港、中国澳门、新加坡、越南、泰国。 </li>
<li>Asia Pacific Region 2：亚太二区，包括中国台湾、日本、马来西亚、印度尼西亚、韩国。 </li>
<li>Asia Pacific Region 3：亚太三区，包括菲律宾、印度、澳大利亚和亚太其它国家和地区。 </li>
<li>Middle East：中东。 </li>
<li>Europe：欧洲。</li>
<li>North America：北美。</li>
<li>South America：南美。</li>
<li>Africa：非洲。</li>
默认为中国大陆。
        :type Area: str
        :param Districts: 用户所在地区，Area 为 Chinese Mainland 时，取值为以下地区信息，当 Area 为其它值时， 忽略 Districts 参数。
<li>Beijing：北京。</li>
<li>Inner Mongolia：内蒙古。</li>
<li>Shanxi：山西。</li>
<li>Hebei：河北。</li>
<li>Tianjin：天津。</li>
<li>Ningxia：宁夏。</li>
<li>Shaanxi：陕西。</li>
<li>Gansu：甘肃。</li>
<li>Qinghai：青海。</li>
<li>Xinjiang：新疆。</li>
<li>Heilongjiang：黑龙江。</li>
<li>Jilin：吉林。</li>
<li>Liaoning：辽宁。</li>
<li>Fujian：福建。</li>
<li>Jiangsu：江苏。</li>
<li>Anhui：安徽。</li>
<li>Shandong：山东。</li>
<li>Shanghai：上海。</li>
<li>Zhejiang：浙江。</li>
<li>Henan：河南。</li>
<li>Hubei：湖北。</li>
<li>Jiangxi：江西。</li>
<li>Hunan：湖南。</li>
<li>Guizhou：贵州。</li>
<li>Yunnan：云南。</li>
<li>Chongqing：重庆。</li>
<li>Sichuan：四川。</li>
<li>Tibet：西藏。</li>
<li>Guangdong：广东。</li>
<li>Guangxi：广西。</li>
<li>Hainan：海南。</li>
<li>Hong Kong, Macao and Taiwan：港澳台。</li>
<li>Outside Chinese Mainland：海外。</li>
<li>Other：其他 。</li>
        :type Districts: list of str
        :param Isps: 用户所属运营商信息，Area 为 Chinese Mainland 时，取值为以下运营商信息。当 Area 为其它值时忽略 Isps 参数。
<li>China Telecom：中国电信。 </li>
<li>China Unicom：中国联通。 </li>
<li>CERNET：教育网。</li>
<li>Great Wall Broadband Network：长城宽带。</li>
<li>China Mobile：中国移动。</li>
<li>China Mobile Tietong：中国铁通。</li>
<li>ISPs outside Chinese Mainland：海外运营商。</li>
<li>Other ISPs：其他运营商。</li>
        :type Isps: list of str
        :param DataInterval: 每条数据的时间粒度，单位：分钟，取值有：
<li>5：5 分钟粒度，返回指定查询时间内5分钟粒度的明细数据。</li>
<li>1440：天粒度，返回指定查询时间内1天粒度的数据。起始时间和结束时间跨度大于24小时，只支持天粒度的数据。</li>
当 StartTime 和 EndTime 时间跨度大于24小时时，DataInterval 默认为 1440。
        :type DataInterval: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Metric = None
        self.StartTime = None
        self.EndTime = None
        self.DomainNames = None
        self.Area = None
        self.Districts = None
        self.Isps = None
        self.DataInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DomainNames = params.get("DomainNames")
        self.Area = params.get("Area")
        self.Districts = params.get("Districts")
        self.Isps = params.get("Isps")
        self.DataInterval = params.get("DataInterval")
        self.SubAppId = params.get("SubAppId")


class DescribeCDNStatDetailsResponse(AbstractModel):
    """DescribeCDNStatDetails返回参数结构体

    """

    def __init__(self):
        """
        :param DataInterval: 每条数据的时间粒度，单位：分钟。
        :type DataInterval: int
        :param Data: CDN 用量数据。
        :type Data: list of StatDataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInterval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataInterval = params.get("DataInterval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCDNUsageDataRequest(AbstractModel):
    """DescribeCDNUsageData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束日期，需大于开始日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param DataType: CDN 统计数据类型，有效值：
<li>Flux：流量，单位为 byte。</li>
<li>Bandwidth：带宽，单位为 bps。</li>
        :type DataType: str
        :param DataInterval: 用量数据的时间粒度，单位：分钟，取值有：
<li>5：5 分钟粒度，返回指定查询时间内5分钟粒度的明细数据。</li>
<li>60：小时粒度，返回指定查询时间内1小时粒度的数据。</li>
<li>1440：天粒度，返回指定查询时间内1天粒度的数据。</li>
默认值为1440，返回天粒度的数据。
        :type DataInterval: int
        :param DomainNames: 域名列表。一次最多查询20个域名的用量数据。可以指定多个域名，查询这些域名叠加的用量数据。默认返回所有域名叠加的用量数据。
        :type DomainNames: list of str
        :param SubAppId: 点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
当该字段为1时，表示以管理员身份查询所有子应用（含主应用）的用量合计，此时时间粒度只支持天粒度。
        :type SubAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.DataType = None
        self.DataInterval = None
        self.DomainNames = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DataType = params.get("DataType")
        self.DataInterval = params.get("DataInterval")
        self.DomainNames = params.get("DomainNames")
        self.SubAppId = params.get("SubAppId")


class DescribeCDNUsageDataResponse(AbstractModel):
    """DescribeCDNUsageData返回参数结构体

    """

    def __init__(self):
        """
        :param DataInterval: 时间粒度，单位：分钟。
        :type DataInterval: int
        :param Data: CDN 统计数据。
        :type Data: list of StatDataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInterval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataInterval = params.get("DataInterval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCdnLogsRequest(AbstractModel):
    """DescribeCdnLogs请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param StartTime: 获取日志起始时间点，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type StartTime: str
        :param EndTime: 结束时间需大于起始时间；使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type EndTime: str
        :param Limit: 分页拉取的最大返回结果数。默认值：100；最大值：1000。
        :type Limit: int
        :param Offset: 分页拉取的起始偏移量。默认值：0。
        :type Offset: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.DomainName = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SubAppId = params.get("SubAppId")


class DescribeCdnLogsResponse(AbstractModel):
    """DescribeCdnLogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 日志下载链接总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param OverseaCdnLogs: 海外CDN节点的日志下载列表。如果域名没有开启海外加速，忽略该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OverseaCdnLogs: list of CdnLogInfo
        :param DomesticCdnLogs: 国内CDN节点的日志下载列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomesticCdnLogs: list of CdnLogInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OverseaCdnLogs = None
        self.DomesticCdnLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OverseaCdnLogs") is not None:
            self.OverseaCdnLogs = []
            for item in params.get("OverseaCdnLogs"):
                obj = CdnLogInfo()
                obj._deserialize(item)
                self.OverseaCdnLogs.append(obj)
        if params.get("DomesticCdnLogs") is not None:
            self.DomesticCdnLogs = []
            for item in params.get("DomesticCdnLogs"):
                obj = CdnLogInfo()
                obj._deserialize(item)
                self.DomesticCdnLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeContentReviewTemplatesRequest(AbstractModel):
    """DescribeContentReviewTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 内容智能识别模板唯一标识过滤条件，数组长度限制：100。
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


class DescribeContentReviewTemplatesResponse(AbstractModel):
    """DescribeContentReviewTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param ContentReviewTemplateSet: 内容智能识别模板详情列表。
        :type ContentReviewTemplateSet: list of ContentReviewTemplateItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ContentReviewTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ContentReviewTemplateSet") is not None:
            self.ContentReviewTemplateSet = []
            for item in params.get("ContentReviewTemplateSet"):
                obj = ContentReviewTemplateItem()
                obj._deserialize(item)
                self.ContentReviewTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDailyMediaPlayStatRequest(AbstractModel):
    """DescribeDailyMediaPlayStat请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件 ID 。
        :type FileId: str
        :param StartDate: 起始日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。该参数仅日期部分有效。
        :type StartDate: str
        :param EndDate: 结束日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。该参数仅日期部分有效。
        :type EndDate: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.StartDate = None
        self.EndDate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.SubAppId = params.get("SubAppId")


class DescribeDailyMediaPlayStatResponse(AbstractModel):
    """DescribeDailyMediaPlayStat返回参数结构体

    """

    def __init__(self):
        """
        :param DailyPlayStatInfoSet: 播放统计数据。
        :type DailyPlayStatInfoSet: list of DailyPlayStatInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DailyPlayStatInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DailyPlayStatInfoSet") is not None:
            self.DailyPlayStatInfoSet = []
            for item in params.get("DailyPlayStatInfoSet"):
                obj = DailyPlayStatInfo()
                obj._deserialize(item)
                self.DailyPlayStatInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDailyMostPlayedStatRequest(AbstractModel):
    """DescribeDailyMostPlayedStat请求参数结构体

    """

    def __init__(self):
        """
        :param Date: 查询日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。该参数仅日期部分有效。
        :type Date: str
        :param DomainName: 域名。查询该域名播放 Top100 的媒体文件的统计数据。默认查询所有域名的播放统计数据。
        :type DomainName: str
        :param Metric: Top 数据的统计指标，取值有：
<li>Traffic：播放流量，按播放流量统计 Top100 的数据。</li>
<li>PlayTimes：播放次数，按播放次数统计播放 Top100 的数据。</li>
        :type Metric: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Date = None
        self.DomainName = None
        self.Metric = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.DomainName = params.get("DomainName")
        self.Metric = params.get("Metric")
        self.SubAppId = params.get("SubAppId")


class DescribeDailyMostPlayedStatResponse(AbstractModel):
    """DescribeDailyMostPlayedStat返回参数结构体

    """

    def __init__(self):
        """
        :param DailyPlayStatInfoSet: 媒体文件播放统计信息。
        :type DailyPlayStatInfoSet: list of DailyPlayStatInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DailyPlayStatInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DailyPlayStatInfoSet") is not None:
            self.DailyPlayStatInfoSet = []
            for item in params.get("DailyPlayStatInfoSet"):
                obj = DailyPlayStatInfo()
                obj._deserialize(item)
                self.DailyPlayStatInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDailyPlayStatFileListRequest(AbstractModel):
    """DescribeDailyPlayStatFileList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubAppId = params.get("SubAppId")


class DescribeDailyPlayStatFileListResponse(AbstractModel):
    """DescribeDailyPlayStatFileList返回参数结构体

    """

    def __init__(self):
        """
        :param PlayStatFileSet: 播放统计文件列表。
        :type PlayStatFileSet: list of PlayStatFileInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlayStatFileSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayStatFileSet") is not None:
            self.PlayStatFileSet = []
            for item in params.get("PlayStatFileSet"):
                obj = PlayStatFileInfo()
                obj._deserialize(item)
                self.PlayStatFileSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDrmDataKeyRequest(AbstractModel):
    """DescribeDrmDataKey请求参数结构体

    """

    def __init__(self):
        """
        :param EdkList: 加密后的数据密钥列表，最大支持10个。
        :type EdkList: list of str
        """
        self.EdkList = None


    def _deserialize(self, params):
        self.EdkList = params.get("EdkList")


class DescribeDrmDataKeyResponse(AbstractModel):
    """DescribeDrmDataKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyList: 密钥列表，包含加密的数据密钥。
        :type KeyList: list of SimpleAesEdkPair
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyList") is not None:
            self.KeyList = []
            for item in params.get("KeyList"):
                obj = SimpleAesEdkPair()
                obj._deserialize(item)
                self.KeyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEventsStateRequest(AbstractModel):
    """DescribeEventsState请求参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")


class DescribeEventsStateResponse(AbstractModel):
    """DescribeEventsState返回参数结构体

    """

    def __init__(self):
        """
        :param CountOfEventsToPull: 待进行拉取的事件通知数，为近似值，约5秒延迟。
        :type CountOfEventsToPull: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CountOfEventsToPull = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CountOfEventsToPull = params.get("CountOfEventsToPull")
        self.RequestId = params.get("RequestId")


class DescribeImageProcessingTemplatesRequest(AbstractModel):
    """DescribeImageProcessingTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 图片处理模板标识列表。长度限制：100。
        :type Definitions: list of int non-negative
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
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


class DescribeImageProcessingTemplatesResponse(AbstractModel):
    """DescribeImageProcessingTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param ImageProcessingTemplateSet: 图片处理模板详情列表。
        :type ImageProcessingTemplateSet: list of ImageProcessingTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageProcessingTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageProcessingTemplateSet") is not None:
            self.ImageProcessingTemplateSet = []
            for item in params.get("ImageProcessingTemplateSet"):
                obj = ImageProcessingTemplate()
                obj._deserialize(item)
                self.ImageProcessingTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageSpriteTemplatesRequest(AbstractModel):
    """DescribeImageSpriteTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 雪碧图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")


class DescribeImageSpriteTemplatesResponse(AbstractModel):
    """DescribeImageSpriteTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param ImageSpriteTemplateSet: 雪碧图模板详情列表。
        :type ImageSpriteTemplateSet: list of ImageSpriteTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSpriteTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSpriteTemplateSet") is not None:
            self.ImageSpriteTemplateSet = []
            for item in params.get("ImageSpriteTemplateSet"):
                obj = ImageSpriteTemplate()
                obj._deserialize(item)
                self.ImageSpriteTemplateSet.append(obj)
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
<li>adaptiveDynamicStreamingInfo（转自适应码流信息）。</li>
<li>miniProgramReviewInfo（小程序审核信息）。</li>
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
        :type MediaInfoSet: list of MediaInfo
        :param NotExistFileIdSet: 不存在的文件 ID 列表。
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


class DescribeMediaProcessUsageDataRequest(AbstractModel):
    """DescribeMediaProcessUsageData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#52)。
        :type StartTime: str
        :param EndTime: 结束日期，需大于等于起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#52)。
        :type EndTime: str
        :param Type: 查询视频处理任务类型，目前支持的任务类型包括：
<li> Transcoding: 普通转码</li>
<li> Transcoding-TESHD: 极速高清转码</li>
<li> Editing: 视频编辑</li>
<li> AdaptiveBitrateStreaming: 自适应码流</li>
<li> ContentAudit: 内容审核</li>
<li>Transcode: 转码，包含普通转码、极速高清和视频编辑（不推荐使用）</li>
        :type Type: str
        :param SubAppId: 点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")


class DescribeMediaProcessUsageDataResponse(AbstractModel):
    """DescribeMediaProcessUsageData返回参数结构体

    """

    def __init__(self):
        """
        :param MediaProcessDataSet: 视频处理统计数据概览，展示所查询任务的概览以及详细数据。
        :type MediaProcessDataSet: list of TaskStatData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MediaProcessDataSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MediaProcessDataSet") is not None:
            self.MediaProcessDataSet = []
            for item in params.get("MediaProcessDataSet"):
                obj = TaskStatData()
                obj._deserialize(item)
                self.MediaProcessDataSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonSamplesRequest(AbstractModel):
    """DescribePersonSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 拉取的素材类型，可选值：
<li>UserDefine：用户自定义素材库；</li>
<li>Default：系统默认素材库。</li>

默认值：UserDefine，拉取用户自定义素材库素材。
说明：如果是拉取系统默认素材库，只能使用素材名字或者素材 ID + 素材名字的方式进行拉取，且五官图片只返回一张。
        :type Type: str
        :param PersonIds: 素材 ID，数组长度限制：100。
        :type PersonIds: list of str
        :param Names: 素材名称，数组长度限制：20。
        :type Names: list of str
        :param Tags: 素材标签，数组长度限制：20。
        :type Tags: list of str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：100，最大值：100。
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Type = None
        self.PersonIds = None
        self.Names = None
        self.Tags = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PersonIds = params.get("PersonIds")
        self.Names = params.get("Names")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribePersonSamplesResponse(AbstractModel):
    """DescribePersonSamples返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param PersonSet: 人物信息。
        :type PersonSet: list of AiSamplePerson
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = AiSamplePerson()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrepaidProductsRequest(AbstractModel):
    """DescribePrepaidProducts请求参数结构体

    """


class DescribePrepaidProductsResponse(AbstractModel):
    """DescribePrepaidProducts返回参数结构体

    """

    def __init__(self):
        """
        :param ProductInstanceSet: 购买的预付费商品实例列表。
        :type ProductInstanceSet: list of ProductInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProductInstanceSet") is not None:
            self.ProductInstanceSet = []
            for item in params.get("ProductInstanceSet"):
                obj = ProductInstance()
                obj._deserialize(item)
                self.ProductInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProcedureTemplatesRequest(AbstractModel):
    """DescribeProcedureTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Names: 任务流模板名字过滤条件，数组长度限制：100。
        :type Names: list of str
        :param Type: 任务流模板类型过滤条件，可选值：
<li>Preset：系统预置任务流模板；</li>
<li>Custom：用户自定义任务流模板。</li>
        :type Type: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Names = None
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Type = params.get("Type")
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


class DescribeReviewDetailsRequest(AbstractModel):
    """DescribeReviewDetails请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束日期，需大于起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubAppId = params.get("SubAppId")


class DescribeReviewDetailsResponse(AbstractModel):
    """DescribeReviewDetails返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 发起内容智能识别次数。
        :type TotalCount: int
        :param TotalDuration: 内容智能识别总时长。
        :type TotalDuration: int
        :param Data: 内容智能识别时长统计数据，每天一个数据。
        :type Data: list of StatDataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TotalDuration = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TotalDuration = params.get("TotalDuration")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleSnapshotTemplatesRequest(AbstractModel):
    """DescribeSampleSnapshotTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 采样截图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")


class DescribeSampleSnapshotTemplatesResponse(AbstractModel):
    """DescribeSampleSnapshotTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param SampleSnapshotTemplateSet: 采样截图模板详情列表。
        :type SampleSnapshotTemplateSet: list of SampleSnapshotTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SampleSnapshotTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SampleSnapshotTemplateSet") is not None:
            self.SampleSnapshotTemplateSet = []
            for item in params.get("SampleSnapshotTemplateSet"):
                obj = SampleSnapshotTemplate()
                obj._deserialize(item)
                self.SampleSnapshotTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotByTimeOffsetTemplatesRequest(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 指定时间点截图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")


class DescribeSnapshotByTimeOffsetTemplatesResponse(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param SnapshotByTimeOffsetTemplateSet: 指定时间点截图模板详情列表。
        :type SnapshotByTimeOffsetTemplateSet: list of SnapshotByTimeOffsetTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotByTimeOffsetTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotByTimeOffsetTemplateSet") is not None:
            self.SnapshotByTimeOffsetTemplateSet = []
            for item in params.get("SnapshotByTimeOffsetTemplateSet"):
                obj = SnapshotByTimeOffsetTemplate()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStorageDataRequest(AbstractModel):
    """DescribeStorageData请求参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")


class DescribeStorageDataResponse(AbstractModel):
    """DescribeStorageData返回参数结构体

    """

    def __init__(self):
        """
        :param MediaCount: 当前媒体总量。
        :type MediaCount: int
        :param TotalStorage: 当前总存储量，单位是字节。
        :type TotalStorage: int
        :param InfrequentStorage: 当前低频存储量，单位是字节。
        :type InfrequentStorage: int
        :param StandardStorage: 当前标准存储量，单位是字节。
        :type StandardStorage: int
        :param StorageStat: 各计费区域的存储用量。
        :type StorageStat: list of StorageStatData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MediaCount = None
        self.TotalStorage = None
        self.InfrequentStorage = None
        self.StandardStorage = None
        self.StorageStat = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MediaCount = params.get("MediaCount")
        self.TotalStorage = params.get("TotalStorage")
        self.InfrequentStorage = params.get("InfrequentStorage")
        self.StandardStorage = params.get("StandardStorage")
        if params.get("StorageStat") is not None:
            self.StorageStat = []
            for item in params.get("StorageStat"):
                obj = StorageStatData()
                obj._deserialize(item)
                self.StorageStat.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStorageDetailsRequest(AbstractModel):
    """DescribeStorageDetails请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间，格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#52)。
        :type StartTime: str
        :param EndTime: 结束时间，需大于开始日期，格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#52)。
        :type EndTime: str
        :param Interval: 统计时间粒度，有效值：
<li>Minute：以5分钟为粒度。</li>
<li>Day：以天为粒度。</li>
默认按时间跨度决定，小于等于1天以5分钟为粒度，大于1天则以天为粒度。
        :type Interval: str
        :param StorageType: 查询的存储类型，有效值：
<li>TotalStorage：存储总量。</li>
<li>StandardStorage：标准存储。</li>
<li>InfrequentStorage：低频存储。</li>
默认值为 TotalStorage。
        :type StorageType: str
        :param SubAppId: 点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
当该字段为1时，表示以管理员身份查询所有子应用（含主应用）的用量合计。
        :type SubAppId: int
        :param Area: 查询的存储区域，有效值：
<li>Chinese Mainland：中国境内（不包含港澳台）。</li>
<li>Outside Chinese Mainland：中国境外。</li>
默认值为 Chinese Mainland。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.StorageType = None
        self.SubAppId = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.StorageType = params.get("StorageType")
        self.SubAppId = params.get("SubAppId")
        self.Area = params.get("Area")


class DescribeStorageDetailsResponse(AbstractModel):
    """DescribeStorageDetails返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 存储统计数据，每5分钟或每天一条数据。
        :type Data: list of StatDataItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubAppIdsRequest(AbstractModel):
    """DescribeSubAppIds请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 子应用名称。
        :type Name: str
        :param Tags: 标签信息，查询指定标签的子应用列表。
        :type Tags: list of ResourceTag
        :param Offset: 分页拉取的起始偏移量。默认值：0。
        :type Offset: int
        :param Limit: 分页拉取的最大返回结果数。默认值：200；最大值：200。
        :type Limit: int
        """
        self.Name = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubAppIdsResponse(AbstractModel):
    """DescribeSubAppIds返回参数结构体

    """

    def __init__(self):
        """
        :param SubAppIdInfoSet: 子应用信息集合。
        :type SubAppIdInfoSet: list of SubAppIdInfo
        :param TotalCount: 子应用总数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAppIdInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubAppIdInfoSet") is not None:
            self.SubAppIdInfoSet = []
            for item in params.get("SubAppIdInfoSet"):
                obj = SubAppIdInfo()
                obj._deserialize(item)
                self.SubAppIdInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSuperPlayerConfigsRequest(AbstractModel):
    """DescribeSuperPlayerConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param Names: 播放器配置名字过滤条件，数组长度限制：100。
        :type Names: list of str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 播放器配置类型过滤条件，可选值：
<li>Preset：系统预置配置；</li>
<li>Custom：用户自定义配置。</li>
        :type Type: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Names = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SubAppId = params.get("SubAppId")


class DescribeSuperPlayerConfigsResponse(AbstractModel):
    """DescribeSuperPlayerConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param PlayerConfigSet: 播放器配置数组。
        :type PlayerConfigSet: list of PlayerConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PlayerConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PlayerConfigSet") is not None:
            self.PlayerConfigSet = []
            for item in params.get("PlayerConfigSet"):
                obj = PlayerConfig()
                obj._deserialize(item)
                self.PlayerConfigSet.append(obj)
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
<li>SplitMedia：视频拆条任务；</li>
<li>ComposeMedia：制作媒体文件任务；</li>
<li>WechatPublish：微信发布任务；</li>
<li>WechatMiniProgramPublish：微信小程序视频发布任务；</li>
<li>PullUpload：拉取上传媒体文件任务。</li>

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
        :param CreateTime: 任务的创建时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param BeginProcessTime: 任务开始执行的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type BeginProcessTime: str
        :param FinishTime: 任务执行完毕的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
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
        :param ComposeMediaTask: 制作媒体文件任务信息，仅当 TaskType 为 ComposeMedia，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ComposeMediaTask: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTask`
        :param SplitMediaTask: 视频拆条任务信息，仅当 TaskType 为 SplitMedia，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitMediaTask: :class:`tencentcloud.vod.v20180717.models.SplitMediaTask`
        :param WechatMiniProgramPublishTask: 微信小程序发布任务信息，仅当 TaskType 为 WechatMiniProgramPublish，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatMiniProgramPublishTask: :class:`tencentcloud.vod.v20180717.models.WechatMiniProgramPublishTask`
        :param PullUploadTask: 拉取上传媒体文件任务信息，仅当 TaskType 为 PullUpload，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PullUploadTask: :class:`tencentcloud.vod.v20180717.models.PullUploadTask`
        :param TranscodeTask: 视频转码任务信息，仅当 TaskType 为 Transcode，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`tencentcloud.vod.v20180717.models.TranscodeTask2017`
        :param ConcatTask: 视频拼接任务信息，仅当 TaskType 为 Concat，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcatTask: :class:`tencentcloud.vod.v20180717.models.ConcatTask2017`
        :param ClipTask: 视频剪辑任务信息，仅当 TaskType 为 Clip，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClipTask: :class:`tencentcloud.vod.v20180717.models.ClipTask2017`
        :param CreateImageSpriteTask: 截取雪碧图任务信息，仅当 TaskType 为 ImageSprite，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateImageSpriteTask: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTask2017`
        :param SnapshotByTimeOffsetTask: 视频指定时间点截图任务信息，仅当 TaskType 为 SnapshotByTimeOffset，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`
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
        self.ComposeMediaTask = None
        self.SplitMediaTask = None
        self.WechatMiniProgramPublishTask = None
        self.PullUploadTask = None
        self.TranscodeTask = None
        self.ConcatTask = None
        self.ClipTask = None
        self.CreateImageSpriteTask = None
        self.SnapshotByTimeOffsetTask = None
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
        if params.get("ComposeMediaTask") is not None:
            self.ComposeMediaTask = ComposeMediaTask()
            self.ComposeMediaTask._deserialize(params.get("ComposeMediaTask"))
        if params.get("SplitMediaTask") is not None:
            self.SplitMediaTask = SplitMediaTask()
            self.SplitMediaTask._deserialize(params.get("SplitMediaTask"))
        if params.get("WechatMiniProgramPublishTask") is not None:
            self.WechatMiniProgramPublishTask = WechatMiniProgramPublishTask()
            self.WechatMiniProgramPublishTask._deserialize(params.get("WechatMiniProgramPublishTask"))
        if params.get("PullUploadTask") is not None:
            self.PullUploadTask = PullUploadTask()
            self.PullUploadTask._deserialize(params.get("PullUploadTask"))
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = TranscodeTask2017()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("ConcatTask") is not None:
            self.ConcatTask = ConcatTask2017()
            self.ConcatTask._deserialize(params.get("ConcatTask"))
        if params.get("ClipTask") is not None:
            self.ClipTask = ClipTask2017()
            self.ClipTask._deserialize(params.get("ClipTask"))
        if params.get("CreateImageSpriteTask") is not None:
            self.CreateImageSpriteTask = CreateImageSpriteTask2017()
            self.CreateImageSpriteTask._deserialize(params.get("CreateImageSpriteTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
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
        :type TaskSet: list of TaskSimpleInfo
        :param ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 ID。当该字段为空，说明已无更多数据。
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
        :param TEHDType: 极速高清过滤条件，用于过滤普通转码或极速高清转码模板，可选值：
<li>Common：普通转码模板；</li>
<li>TEHD：极速高清模板。</li>
        :type TEHDType: str
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
        self.TEHDType = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.TEHDType = params.get("TEHDType")
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


class DescribeVodDomainsRequest(AbstractModel):
    """DescribeVodDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表。当该字段不填时，则默认列出所有域名信息。本字段字段限制如下：
<li>域名个数度最大为 20。</li>
        :type Domains: list of str
        :param Limit: 分页拉取的最大返回结果数。默认值：20。
        :type Limit: int
        :param Offset: 分页拉取的起始偏移量。默认值：0。
        :type Offset: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Domains = None
        self.Limit = None
        self.Offset = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SubAppId = params.get("SubAppId")


class DescribeVodDomainsResponse(AbstractModel):
    """DescribeVodDomains返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 域名总数量。
        :type TotalCount: int
        :param DomainSet: 域名信息列表。
        :type DomainSet: list of DomainDetailInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DomainSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainSet") is not None:
            self.DomainSet = []
            for item in params.get("DomainSet"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.DomainSet.append(obj)
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
<li>text：文字水印；</li>
<li>svg：SVG 水印。</li>
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


class DescribeWordSamplesRequest(AbstractModel):
    """DescribeWordSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Usages: <b>关键词应用场景过滤条件，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜的内容识别；
4. Review.Asr：通过音频识别技术，进行不适宜的内容识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜的内容识别，等价于 3+4；
可多选，元素间关系为 or，即关键词的应用场景包含该字段集合中任意元素的记录，均符合该条件。
        :type Usages: list of str
        :param Keywords: 关键词过滤条件，数组长度限制：100 个词。
        :type Keywords: list of str
        :param Tags: 标签过滤条件，数组长度限制：20 个词。
        :type Tags: list of str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：100，最大值：100。
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Usages = None
        self.Keywords = None
        self.Tags = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        self.Keywords = params.get("Keywords")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeWordSamplesResponse(AbstractModel):
    """DescribeWordSamples返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param WordSet: 关键词信息。
        :type WordSet: list of AiSampleWord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WordSet") is not None:
            self.WordSet = []
            for item in params.get("WordSet"):
                obj = AiSampleWord()
                obj._deserialize(item)
                self.WordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DomainDetailInfo(AbstractModel):
    """域名信息

    """

    def __init__(self):
        """
        :param Domain: 域名名称。
        :type Domain: str
        :param AccelerateAreaInfos: 加速地区信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccelerateAreaInfos: list of AccelerateAreaInfo
        :param DeployStatus: 部署状态，取值有：
<li>Online：上线；</li>
<li>Deploying：部署中；</li>
<li>Locked: 锁定中，出现该状态时，无法对该域名进行部署变更。</li>
        :type DeployStatus: str
        :param HTTPSConfig: HTTPS 配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type HTTPSConfig: :class:`tencentcloud.vod.v20180717.models.DomainHTTPSConfig`
        :param UrlSignatureAuthPolicy: [Key 防盗链](https://cloud.tencent.com/document/product/266/14047)配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlSignatureAuthPolicy: :class:`tencentcloud.vod.v20180717.models.UrlSignatureAuthPolicy`
        :param RefererAuthPolicy: [Referer 防盗链](https://cloud.tencent.com/document/product/266/14046)配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RefererAuthPolicy: :class:`tencentcloud.vod.v20180717.models.RefererAuthPolicy`
        :param CreateTime: 域名添加到腾讯云点播系统中的时间。
<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>
        :type CreateTime: str
        """
        self.Domain = None
        self.AccelerateAreaInfos = None
        self.DeployStatus = None
        self.HTTPSConfig = None
        self.UrlSignatureAuthPolicy = None
        self.RefererAuthPolicy = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("AccelerateAreaInfos") is not None:
            self.AccelerateAreaInfos = []
            for item in params.get("AccelerateAreaInfos"):
                obj = AccelerateAreaInfo()
                obj._deserialize(item)
                self.AccelerateAreaInfos.append(obj)
        self.DeployStatus = params.get("DeployStatus")
        if params.get("HTTPSConfig") is not None:
            self.HTTPSConfig = DomainHTTPSConfig()
            self.HTTPSConfig._deserialize(params.get("HTTPSConfig"))
        if params.get("UrlSignatureAuthPolicy") is not None:
            self.UrlSignatureAuthPolicy = UrlSignatureAuthPolicy()
            self.UrlSignatureAuthPolicy._deserialize(params.get("UrlSignatureAuthPolicy"))
        if params.get("RefererAuthPolicy") is not None:
            self.RefererAuthPolicy = RefererAuthPolicy()
            self.RefererAuthPolicy._deserialize(params.get("RefererAuthPolicy"))
        self.CreateTime = params.get("CreateTime")


class DomainHTTPSConfig(AbstractModel):
    """域名 HTTPS 配置信息

    """

    def __init__(self):
        """
        :param CertExpireTime: 证书过期时间。
<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>
        :type CertExpireTime: str
        """
        self.CertExpireTime = None


    def _deserialize(self, params):
        self.CertExpireTime = params.get("CertExpireTime")


class DrmStreamingsInfo(AbstractModel):
    """DRM 自适应码流播放信息

    """

    def __init__(self):
        """
        :param SimpleAesDefinition: 保护类型为 SimpleAES 的转自适应码流模板 ID。
        :type SimpleAesDefinition: int
        """
        self.SimpleAesDefinition = None


    def _deserialize(self, params):
        self.SimpleAesDefinition = params.get("SimpleAesDefinition")


class DrmStreamingsInfoForUpdate(AbstractModel):
    """DRM 自适应码流播放信息修改对象

    """

    def __init__(self):
        """
        :param SimpleAesDefinition: 保护类型为 SimpleAES 的转自适应码流模板 ID。
        :type SimpleAesDefinition: int
        """
        self.SimpleAesDefinition = None


    def _deserialize(self, params):
        self.SimpleAesDefinition = params.get("SimpleAesDefinition")


class EditMediaFileInfo(AbstractModel):
    """编辑点播视频文件信息

    """

    def __init__(self):
        """
        :param FileId: 视频的 ID。
        :type FileId: str
        :param StartTimeOffset: 视频剪辑的起始偏移时间偏移，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 视频剪辑的起始结束时间偏移，单位：秒。
        :type EndTimeOffset: float
        """
        self.FileId = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class EditMediaOutputConfig(AbstractModel):
    """编辑视频的结果文件输出。

    """

    def __init__(self):
        """
        :param MediaName: 输出文件名，最长 64 个字符。缺省由系统指定生成文件名。
        :type MediaName: str
        :param Type: 输出文件格式，可选值：mp4、hls。默认是 mp4。
        :type Type: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/7812) 接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param ExpireTime: 输出文件的过期时间，超过该时间文件将被删除，默认为永久不过期，格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        """
        self.MediaName = None
        self.Type = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.MediaName = params.get("MediaName")
        self.Type = params.get("Type")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")


class EditMediaRequest(AbstractModel):
    """EditMedia请求参数结构体

    """

    def __init__(self):
        """
        :param InputType: 输入视频的类型，可以取的值为  File，Stream 两种。
        :type InputType: str
        :param FileInfos: 输入的视频文件信息，当 InputType 为 File 时必填。
        :type FileInfos: list of EditMediaFileInfo
        :param StreamInfos: 输入的流信息，当 InputType 为 Stream 时必填。
        :type StreamInfos: list of EditMediaStreamInfo
        :param Definition: 编辑模板 ID，取值有 10，20，不填代表使用 10 模板。
<li>10：拼接时，以分辨率最高的输入为基准；</li>
<li>20：拼接时，以码率最高的输入为基准；</li>
        :type Definition: int
        :param ProcedureName: [任务流模板](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字，如果要对生成的新视频执行任务流时填写。
        :type ProcedureName: str
        :param OutputConfig: 编辑后生成的文件配置。
        :type OutputConfig: :class:`tencentcloud.vod.v20180717.models.EditMediaOutputConfig`
        :param SessionContext: 标识来源上下文，用于透传用户请求信息，在EditMediaComplete回调和任务流状态变更回调将返回该字段值，最长 1000个字符。
        :type SessionContext: str
        :param TasksPriority: 任务的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param SessionId: 用于任务去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.InputType = None
        self.FileInfos = None
        self.StreamInfos = None
        self.Definition = None
        self.ProcedureName = None
        self.OutputConfig = None
        self.SessionContext = None
        self.TasksPriority = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = EditMediaStreamInfo()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Definition = params.get("Definition")
        self.ProcedureName = params.get("ProcedureName")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = EditMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))
        self.SessionContext = params.get("SessionContext")
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")


class EditMediaResponse(AbstractModel):
    """EditMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 编辑视频的任务 ID，可以通过该 ID 查询编辑任务（任务类型为 EditMedia）的状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EditMediaStreamInfo(AbstractModel):
    """编辑视频流信息

    """

    def __init__(self):
        """
        :param StreamId: 录制的流 ID
        :type StreamId: str
        :param StartTime: 流剪辑的起始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 流剪辑的结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
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
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败：
<li>40000：输入参数不合法，请检查输入参数；</li>
<li>60000：源文件错误（如视频数据损坏），请确认源文件是否正常；</li>
<li>70000：内部服务错误，建议重试。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 视频编辑任务的输入。
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: :class:`tencentcloud.vod.v20180717.models.EditMediaTaskInput`
        :param Output: 视频编辑任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.EditMediaTaskOutput`
        :param ProcedureTaskId: 若发起视频编辑任务时指定了视频处理流程，则该字段为流程任务 ID。
        :type ProcedureTaskId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param MetaData: 原始视频的元信息。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.ProcedureTaskId = None
        self.SessionContext = None
        self.SessionId = None
        self.MetaData = None


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
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))


class EditMediaTaskInput(AbstractModel):
    """编辑视频任务的输入。

    """

    def __init__(self):
        """
        :param InputType: 输入视频的来源类型，可以取的值为 File，Stream 两种。
        :type InputType: str
        :param FileInfoSet: 输入的视频文件信息，当 InputType 为 File 时，该字段有值。
        :type FileInfoSet: list of EditMediaFileInfo
        :param StreamInfoSet: 输入的流信息，当 InputType 为 Stream 时，该字段有值。
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
        :type FileType: str
        :param FileUrl: 媒体文件播放地址。
        :type FileUrl: str
        :param FileId: 媒体文件 ID。
        :type FileId: str
        :param MediaName: 输出文件名，最长 64 个字符。缺省由系统指定生成文件名。
        :type MediaName: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/7812) 接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param ExpireTime: 输出文件的过期时间，超过该时间文件将被删除，默认为永久不过期，格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        """
        self.FileType = None
        self.FileUrl = None
        self.FileId = None
        self.MediaName = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileUrl = params.get("FileUrl")
        self.FileId = params.get("FileId")
        self.MediaName = params.get("MediaName")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")


class EmptyTrackItem(AbstractModel):
    """空的轨道片段，用来进行时间轴的占位。如需要两个音频片段之间有一段时间的静音，可以用 EmptyTrackItem 来进行占位。

    """

    def __init__(self):
        """
        :param Duration: 持续时间，单位为秒。
        :type Duration: float
        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")


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
<li>SplitMediaComplete：视频拆分完成；</li>
<li>WechatPublishComplete：微信发布完成；</li>
<li>ComposeMediaComplete：制作媒体文件完成；</li>
<li>WechatMiniProgramPublishComplete：微信小程序发布完成。</li>
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
        :type PullCompleteEvent: :class:`tencentcloud.vod.v20180717.models.PullUploadTask`
        :param EditMediaCompleteEvent: 视频编辑完成事件，当事件类型为 EditMediaComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type EditMediaCompleteEvent: :class:`tencentcloud.vod.v20180717.models.EditMediaTask`
        :param SplitMediaCompleteEvent: 视频拆条完成事件，当事件类型为 SplitMediaComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SplitMediaCompleteEvent: :class:`tencentcloud.vod.v20180717.models.SplitMediaTask`
        :param ComposeMediaCompleteEvent: 制作媒体文件任务完成事件，当事件类型为 ComposeMediaComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ComposeMediaCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ComposeMediaTask`
        :param ClipCompleteEvent: 视频剪辑完成事件，当事件类型为 ClipComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClipCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ClipTask2017`
        :param TranscodeCompleteEvent: 视频转码完成事件，当事件类型为 TranscodeComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeCompleteEvent: :class:`tencentcloud.vod.v20180717.models.TranscodeTask2017`
        :param CreateImageSpriteCompleteEvent: 视频截取雪碧图完成事件，当事件类型为 CreateImageSpriteComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateImageSpriteCompleteEvent: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTask2017`
        :param ConcatCompleteEvent: 视频拼接完成事件，当事件类型为 ConcatComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcatCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ConcatTask2017`
        :param SnapshotByTimeOffsetCompleteEvent: 视频按时间点截图完成事件，当事件类型为 CreateSnapshotByTimeOffsetComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetCompleteEvent: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`
        :param WechatPublishCompleteEvent: 微信发布完成事件，当事件类型为 WechatPublishComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatPublishCompleteEvent: :class:`tencentcloud.vod.v20180717.models.WechatPublishTask`
        :param WechatMiniProgramPublishCompleteEvent: 微信小程序发布任务完成事件，当事件类型为 WechatMiniProgramPublishComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatMiniProgramPublishCompleteEvent: :class:`tencentcloud.vod.v20180717.models.WechatMiniProgramPublishTask`
        """
        self.EventHandle = None
        self.EventType = None
        self.FileUploadEvent = None
        self.ProcedureStateChangeEvent = None
        self.FileDeleteEvent = None
        self.PullCompleteEvent = None
        self.EditMediaCompleteEvent = None
        self.SplitMediaCompleteEvent = None
        self.ComposeMediaCompleteEvent = None
        self.ClipCompleteEvent = None
        self.TranscodeCompleteEvent = None
        self.CreateImageSpriteCompleteEvent = None
        self.ConcatCompleteEvent = None
        self.SnapshotByTimeOffsetCompleteEvent = None
        self.WechatPublishCompleteEvent = None
        self.WechatMiniProgramPublishCompleteEvent = None


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
            self.PullCompleteEvent = PullUploadTask()
            self.PullCompleteEvent._deserialize(params.get("PullCompleteEvent"))
        if params.get("EditMediaCompleteEvent") is not None:
            self.EditMediaCompleteEvent = EditMediaTask()
            self.EditMediaCompleteEvent._deserialize(params.get("EditMediaCompleteEvent"))
        if params.get("SplitMediaCompleteEvent") is not None:
            self.SplitMediaCompleteEvent = SplitMediaTask()
            self.SplitMediaCompleteEvent._deserialize(params.get("SplitMediaCompleteEvent"))
        if params.get("ComposeMediaCompleteEvent") is not None:
            self.ComposeMediaCompleteEvent = ComposeMediaTask()
            self.ComposeMediaCompleteEvent._deserialize(params.get("ComposeMediaCompleteEvent"))
        if params.get("ClipCompleteEvent") is not None:
            self.ClipCompleteEvent = ClipTask2017()
            self.ClipCompleteEvent._deserialize(params.get("ClipCompleteEvent"))
        if params.get("TranscodeCompleteEvent") is not None:
            self.TranscodeCompleteEvent = TranscodeTask2017()
            self.TranscodeCompleteEvent._deserialize(params.get("TranscodeCompleteEvent"))
        if params.get("CreateImageSpriteCompleteEvent") is not None:
            self.CreateImageSpriteCompleteEvent = CreateImageSpriteTask2017()
            self.CreateImageSpriteCompleteEvent._deserialize(params.get("CreateImageSpriteCompleteEvent"))
        if params.get("ConcatCompleteEvent") is not None:
            self.ConcatCompleteEvent = ConcatTask2017()
            self.ConcatCompleteEvent._deserialize(params.get("ConcatCompleteEvent"))
        if params.get("SnapshotByTimeOffsetCompleteEvent") is not None:
            self.SnapshotByTimeOffsetCompleteEvent = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetCompleteEvent._deserialize(params.get("SnapshotByTimeOffsetCompleteEvent"))
        if params.get("WechatPublishCompleteEvent") is not None:
            self.WechatPublishCompleteEvent = WechatPublishTask()
            self.WechatPublishCompleteEvent._deserialize(params.get("WechatPublishCompleteEvent"))
        if params.get("WechatMiniProgramPublishCompleteEvent") is not None:
            self.WechatMiniProgramPublishCompleteEvent = WechatMiniProgramPublishTask()
            self.WechatMiniProgramPublishCompleteEvent._deserialize(params.get("WechatMiniProgramPublishCompleteEvent"))


class ExecuteFunctionRequest(AbstractModel):
    """ExecuteFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 调用后端接口名称。
        :type FunctionName: str
        :param FunctionArg: 接口参数，具体参数格式调用时与后端协调。
        :type FunctionArg: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FunctionName = None
        self.FunctionArg = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.FunctionArg = params.get("FunctionArg")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")


class ExecuteFunctionResponse(AbstractModel):
    """ExecuteFunction返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 处理结果打包后的字符串，具体与后台一同协调。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class FaceConfigureInfo(AbstractModel):
    """人脸识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 人脸识别任务开关，可选值：
<li>ON：开启智能人脸识别任务；</li>
<li>OFF：关闭智能人脸识别任务。</li>
        :type Switch: str
        :param Score: 人脸识别过滤分数，当识别结果达到该分数以上，返回识别结果。默认 95 分。取值范围：0 - 100。
        :type Score: float
        :param DefaultLibraryLabelSet: 默认人物过滤标签，指定需要返回的默认人物的标签。如果未填或者为空，则全部默认人物结果都返回。标签可选值：
<li>entertainment：娱乐明星；</li>
<li>sport：体育明星；</li>
<li>politician：政治人物。</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: 用户自定义人物过滤标签，指定需要返回的用户自定义人物的标签。如果未填或者为空，则全部自定义人物结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: 人物库选择，可选值：
<li>Default：使用默认人物库；</li>
<li>UserDefine：使用用户自定义人物库。</li>
<li>All：同时使用默认人物库和用户自定义人物库。</li>
默认值：All，使用系统默认人物库及用户自定义人物库。
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")


class FaceConfigureInfoForUpdate(AbstractModel):
    """人脸识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 人脸识别任务开关，可选值：
<li>ON：开启智能人脸识别任务；</li>
<li>OFF：关闭智能人脸识别任务。</li>
        :type Switch: str
        :param Score: 人脸识别过滤分数，当识别结果达到该分数以上，返回识别结果。取值范围：0-100。
        :type Score: float
        :param DefaultLibraryLabelSet: 默认人物过滤标签，指定需要返回的默认人物的标签。如果未填或者为空，则全部默认人物结果都返回。标签可选值：
<li>entertainment：娱乐明星；</li>
<li>sport：体育明星；</li>
<li>politician：政治人物。</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: 用户自定义人物过滤标签，指定需要返回的用户自定义人物的标签。如果未填或者为空，则全部自定义人物结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: 人物库选择，可选值：
<li>Default：使用默认人物库；</li>
<li>UserDefine：使用用户自定义人物库。</li>
<li>All：同时使用默认人物库和用户自定义人物库。</li>
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")


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
        :type ProcedureTaskId: str
        :param MetaData: 元信息。包括大小、时长、视频流信息、音频流信息等。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        """
        self.FileId = None
        self.MediaBasicInfo = None
        self.ProcedureTaskId = None
        self.MetaData = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))


class ForbidMediaDistributionRequest(AbstractModel):
    """ForbidMediaDistribution请求参数结构体

    """

    def __init__(self):
        """
        :param FileIds: 媒体文件列表，每次最多可提交 20 条。
        :type FileIds: list of str
        :param Operation: forbid：禁播，recover：解禁。
        :type Operation: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileIds = None
        self.Operation = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Operation = params.get("Operation")
        self.SubAppId = params.get("SubAppId")


class ForbidMediaDistributionResponse(AbstractModel):
    """ForbidMediaDistribution返回参数结构体

    """

    def __init__(self):
        """
        :param NotExistFileIdSet: 不存在的文件 ID 列表。
        :type NotExistFileIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NotExistFileIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotExistFileIdSet = params.get("NotExistFileIdSet")
        self.RequestId = params.get("RequestId")


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


class HeadTailConfigureInfo(AbstractModel):
    """视频片头片尾识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 视频片头片尾识别任务开关，可选值：
<li>ON：开启智能视频片头片尾识别任务；</li>
<li>OFF：关闭智能视频片头片尾识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class HeadTailConfigureInfoForUpdate(AbstractModel):
    """视频片头片尾识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 视频片头片尾识别任务开关，可选值：
<li>ON：开启智能视频片头片尾识别任务；</li>
<li>OFF：关闭智能视频片头片尾识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class HighlightSegmentItem(AbstractModel):
    """智能精彩集锦片段列表。

    """

    def __init__(self):
        """
        :param Confidence: 置信度。
        :type Confidence: float
        :param StartTimeOffset: 片段起始时间偏移。
        :type StartTimeOffset: float
        :param EndTimeOffset: 片段结束时间偏移。
        :type EndTimeOffset: float
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class HighlightsConfigureInfo(AbstractModel):
    """智能精彩片段任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能精彩片段任务开关，可选值：
<li>ON：开启智能精彩片段任务；</li>
<li>OFF：关闭智能精彩片段任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class HighlightsConfigureInfoForUpdate(AbstractModel):
    """智能精彩片段任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能精彩片段任务开关，可选值：
<li>ON：开启智能精彩片段任务；</li>
<li>OFF：关闭智能精彩片段任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ImageCenterCut(AbstractModel):
    """图片中心裁剪处理。

    """

    def __init__(self):
        """
        :param Type: 图片的裁剪模式，可选 Circle 和 Rectangle。
<li>Circle ： 内切圆裁剪，输出图片半径为 Radius。</li>
<li>Rectangle ： 矩形裁剪，输出图片宽为 Width ， 高为 Height。</li>
        :type Type: str
        :param Width: 输出图片的宽度，单位为像素，当 Type 取值为 Rectangle 时有效。
        :type Width: int
        :param Height: 输出图片的高度，单位为像素，当 Type 取值为 Rectangle 时有效。
        :type Height: int
        :param Radius: 输出图片的半径，单位为像素，当 Type 取值为 Circle 时有效。
        :type Radius: int
        """
        self.Type = None
        self.Width = None
        self.Height = None
        self.Radius = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Radius = params.get("Radius")


class ImageOperation(AbstractModel):
    """单个图片处理操作。

    """

    def __init__(self):
        """
        :param Type: 图片处理类型。可选类型有：
<li>Scale : 图片缩略处理。</li>
<li>CenterCut : 图片裁剪处理。</li>
        :type Type: str
        :param Scale: 图片缩略处理，仅当 Type 为 Scale 时有效。
        :type Scale: :class:`tencentcloud.vod.v20180717.models.ImageScale`
        :param CenterCut: 图片裁剪处理，仅当 Type 为 CenterCut 时有效。
        :type CenterCut: :class:`tencentcloud.vod.v20180717.models.ImageCenterCut`
        """
        self.Type = None
        self.Scale = None
        self.CenterCut = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("Scale") is not None:
            self.Scale = ImageScale()
            self.Scale._deserialize(params.get("Scale"))
        if params.get("CenterCut") is not None:
            self.CenterCut = ImageCenterCut()
            self.CenterCut._deserialize(params.get("CenterCut"))


class ImageProcessingTemplate(AbstractModel):
    """图片处理模板， 最多支持三次操作。例如：裁剪-缩略-裁剪。

    """

    def __init__(self):
        """
        :param Definition: 图片处理模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 图片处理模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Operations: 图片处理操作数组，操作将以数组顺序执行。
<li>长度限制：3。</li>
        :type Operations: list of ImageOperation
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Operations = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = ImageOperation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.CreateTime = params.get("CreateTime")


class ImageScale(AbstractModel):
    """图片缩放处理。

    """

    def __init__(self):
        """
        :param Type: 图片缩放的操作类型。可选模式有：
<li>WidthFirst : 指定图片的宽为 Width ，高度等比缩放。</li>
<li>HeightFirst : 指定图片的高为 Height ，宽度等比缩放。</li>
<li>LongEdgeFirst : 指定图片的长边为 LongEdge ，短边等比缩放。</li>
<li>ShortEdgeFirst : 指定图片的短边为 ShortEdge ，长边等比缩放。</li>
<li>Force : 忽略原图宽高比例，指定图片宽度为 Width，高度为 Height ，强行缩放图片，可能导致目标图片变形。</li>
        :type Type: str
        :param Height: 输出图片的高度，单位为像素。当 Type 取值为 HeightFirst 或 Force 时此字段有效。
        :type Height: int
        :param Width: 输出图片的宽度，单位为像素。当 Type 取值为 WidthFirst 或 Force 时此字段有效。
        :type Width: int
        :param LongEdge: 输出图片的长边长度，单位为像素。当 Type 取值为 LongEdgeFirst 时此字段有效。
        :type LongEdge: int
        :param ShortEdge: 输出图片的短边长度，单位为像素。当 Type 取值为 ShortEdgeFirst 时此字段有效。
        :type ShortEdge: int
        """
        self.Type = None
        self.Height = None
        self.Width = None
        self.LongEdge = None
        self.ShortEdge = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.LongEdge = params.get("LongEdge")
        self.ShortEdge = params.get("ShortEdge")


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


class ImageSpriteTemplate(AbstractModel):
    """雪碧图模板详情

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 雪碧图模板名称。
        :type Name: str
        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采样类型。
        :type SampleType: str
        :param SampleInterval: 采样间隔。
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        :param Comment: 模板描述信息。
        :type Comment: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")


class ImageTransform(AbstractModel):
    """图像旋转、翻转等操作

    """

    def __init__(self):
        """
        :param Type: 类型，取值有：
<li> Rotate：图像旋转。</li>
<li> Flip：图像翻转。</li>
        :type Type: str
        :param RotateAngle: 图像以中心点为原点进行旋转的角度，取值范围0~360。当 Type = Rotate 时有效。
        :type RotateAngle: float
        :param Flip: 图像翻转动作，取值有：
<li>Horizental：水平翻转，即左右镜像。</li>
<li>Vertical：垂直翻转，即上下镜像。</li>
当 Type = Flip 时有效。
        :type Flip: str
        """
        self.Type = None
        self.RotateAngle = None
        self.Flip = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.RotateAngle = params.get("RotateAngle")
        self.Flip = params.get("Flip")


class ImageWatermarkInput(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。取值范围为[8, 4096]。</li>
默认值：10%。
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。取值范围为0或[8, 4096]。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。
        :type Height: str
        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束（默认值）。</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")


class ImageWatermarkInputForUpdate(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。取值范围为[8, 4096]。</li>
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。取值范围为0或[8, 4096]。</li>
        :type Height: str
        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束。</li>
        :type RepeatType: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")


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
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；</li>
0px：表示 Height 按照 Width 对视频宽度的比例缩放。
        :type Height: str
        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束。</li>
        :type RepeatType: str
        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")


class LiveRealTimeClipMediaSegmentInfo(AbstractModel):
    """即时剪辑后媒资的片段信息。

    """

    def __init__(self):
        """
        :param StartTime: 片段的起始时间。格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 片段的结束时间。格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class LiveRealTimeClipRequest(AbstractModel):
    """LiveRealTimeClip请求参数结构体

    """

    def __init__(self):
        """
        :param StreamId: 推流[直播码](https://cloud.tencent.com/document/product/267/5959)。
        :type StreamId: str
        :param StartTime: 流剪辑的开始时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 流剪辑的结束时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param IsPersistence: 是否固化。0 不固化，1 固化。默认不固化。
        :type IsPersistence: int
        :param ExpireTime: 剪辑固化后的视频存储过期时间。格式参照 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。仅 IsPersistence 为 1 时有效，默认剪辑固化的视频永不过期。
        :type ExpireTime: str
        :param Procedure: 剪辑固化后的视频点播任务流处理，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。仅 IsPersistence 为 1 时有效。
        :type Procedure: str
        :param MetaDataRequired: 是否需要返回剪辑后的视频元信息。0 不需要，1 需要。默认不需要。
        :type MetaDataRequired: int
        :param Host: 云点播中添加的用于时移播放的域名，必须在云直播已经[关联录制模板和开通时移服务](https://cloud.tencent.com/document/product/266/52220#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E5.85.B3.E8.81.94.E5.BD.95.E5.88.B6.E6.A8.A1.E6.9D.BF.3Ca-id.3D.22step3.22.3E.3C.2Fa.3E)。**如果本接口的首次调用时间在 2021-01-01T00:00:00Z 之后，则此字段为必选字段。**
        :type Host: str
        :param ExtInfo: 系统保留字段，请勿填写。
        :type ExtInfo: str
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
        self.Host = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsPersistence = params.get("IsPersistence")
        self.ExpireTime = params.get("ExpireTime")
        self.Procedure = params.get("Procedure")
        self.MetaDataRequired = params.get("MetaDataRequired")
        self.Host = params.get("Host")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")


class LiveRealTimeClipResponse(AbstractModel):
    """LiveRealTimeClip返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 剪辑后的视频播放 URL。
        :type Url: str
        :param FileId: 剪辑固化后的视频的媒体文件的唯一标识。
        :type FileId: str
        :param VodTaskId: 剪辑固化后的视频任务流 ID。
        :type VodTaskId: str
        :param MetaData: 剪辑后的视频元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param SegmentSet: <span id="p_segmentset">剪辑后的视频片段信息。</span>
        :type SegmentSet: list of LiveRealTimeClipMediaSegmentInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.FileId = None
        self.VodTaskId = None
        self.MetaData = None
        self.SegmentSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileId = params.get("FileId")
        self.VodTaskId = params.get("VodTaskId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = LiveRealTimeClipMediaSegmentInfo()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.RequestId = params.get("RequestId")


class ManageTaskRequest(AbstractModel):
    """ManageTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 视频处理的任务 ID。
        :type TaskId: str
        :param OperationType: 操作类型，取值范围：
<li>Abort：终止任务。只能终止已发起且状态为等待中（WAITING）的任务。</li>
        :type OperationType: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.TaskId = None
        self.OperationType = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.OperationType = params.get("OperationType")
        self.SubAppId = params.get("SubAppId")


class ManageTaskResponse(AbstractModel):
    """ManageTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MediaAdaptiveDynamicStreamingInfo(AbstractModel):
    """转自适应码流信息

    """

    def __init__(self):
        """
        :param AdaptiveDynamicStreamingSet: 转自适应码流信息数组。
        :type AdaptiveDynamicStreamingSet: list of AdaptiveDynamicStreamingInfoItem
        """
        self.AdaptiveDynamicStreamingSet = None


    def _deserialize(self, params):
        if params.get("AdaptiveDynamicStreamingSet") is not None:
            self.AdaptiveDynamicStreamingSet = []
            for item in params.get("AdaptiveDynamicStreamingSet"):
                obj = AdaptiveDynamicStreamingInfoItem()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingSet.append(obj)


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
        :param CategorySet: 按帧标签名称的分类列表，CategorySet.N 表示第 N+1级分类。
比如 Tag 为“塔楼”时，CategorySet 包含两个元素：CategorySet.0 为“场景”，CategorySet.1为 “建筑”，表示按帧标签为“塔楼”，且第1级分类是“场景”，第2级分类是“建筑”。
        :type CategorySet: list of str
        :param Confidence: 按帧标签的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.CategorySet = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.CategorySet = params.get("CategorySet")
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


class MediaAiAnalysisHighlightItem(AbstractModel):
    """智能精彩片段信息

    """

    def __init__(self):
        """
        :param HighlightUrl: 智能精彩集锦地址。
        :type HighlightUrl: str
        :param CovImgUrl: 智能精彩集锦封面地址。
        :type CovImgUrl: str
        :param Confidence: 智能精彩集锦的可信度，取值范围是 0 到 100。
        :type Confidence: float
        :param Duration: 智能精彩集锦持续时间。
        :type Duration: float
        :param SegmentSet: 智能精彩集锦子片段列表，精彩集锦片段由这些子片段拼接生成。
        :type SegmentSet: list of HighlightSegmentItem
        """
        self.HighlightUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.Duration = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.HighlightUrl = params.get("HighlightUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.Duration = params.get("Duration")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = HighlightSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


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
        :type Url: str
        :param Definition: 转动图模板 ID，参见[转动图参数模板](https://cloud.tencent.com/document/product/266/33481#.3Cspan-id-.3D-.22zdt.22.3E.3C.2Fspan.3E.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Container: 动图格式，如 gif。
        :type Container: str
        :param Height: 动图的高度，单位：px。
        :type Height: int
        :param Width: 动图的宽度，单位：px。
        :type Width: int
        :param Bitrate: 动图码率，单位：bps。
        :type Bitrate: int
        :param Size: 动图大小，单位：字节。
        :type Size: int
        :param Md5: 动图的md5值。
        :type Md5: str
        :param StartTimeOffset: 动图在视频中的起始时间偏移，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的结束时间偏移，单位：秒。
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
        :type Bitrate: int
        :param SamplingRate: 音频流的采样率，单位：hz。
        :type SamplingRate: int
        :param Codec: 音频流的编码格式，例如 aac。
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
        :type Name: str
        :param Description: 媒体文件描述。
        :type Description: str
        :param CreateTime: 媒体文件的创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 媒体文件的最近更新时间（如修改视频属性、发起视频处理等会触发更新媒体文件信息的操作），使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        :param ExpireTime: 媒体文件的过期时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。“9999-12-31T23:59:59Z”表示永不过期。
        :type ExpireTime: str
        :param ClassId: 媒体文件的分类 ID。
        :type ClassId: int
        :param ClassName: 媒体文件的分类名称。
        :type ClassName: str
        :param ClassPath: 媒体文件的分类路径，分类间以“-”分隔，如“新的一级分类 - 新的二级分类”。
        :type ClassPath: str
        :param CoverUrl: 媒体文件的封面图片地址。
        :type CoverUrl: str
        :param Type: 媒体文件的封装格式，例如 mp4、flv 等。
        :type Type: str
        :param MediaUrl: 原始媒体文件的 URL 地址。
        :type MediaUrl: str
        :param SourceInfo: 该媒体文件的来源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceInfo: :class:`tencentcloud.vod.v20180717.models.MediaSourceData`
        :param StorageRegion: 媒体文件存储地区，如 ap-chongqing，参见[地域列表](https://cloud.tencent.com/document/product/266/9760#.E5.B7.B2.E6.94.AF.E6.8C.81.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
        :type StorageRegion: str
        :param TagSet: 媒体文件的标签信息。
        :type TagSet: list of str
        :param Vid: 直播录制文件的唯一标识。
        :type Vid: str
        :param Category: 文件类型：
<li>Video: 视频文件</li>
<li>Audio: 音频文件</li>
<li>Image: 图片文件</li>
        :type Category: str
        :param Status: 文件状态：Normal：正常，Forbidden：封禁。

*注意：此字段暂不支持。
        :type Status: str
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
        self.Category = None
        self.Status = None


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
        self.Category = params.get("Category")
        self.Status = params.get("Status")


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
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
        :type Confidence: float
        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param KeywordSet: 嫌疑关键词列表。
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
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
        :type Confidence: float
        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param KeywordSet: 嫌疑关键词列表。
        :type KeywordSet: list of str
        :param AreaCoordSet: 嫌疑文字出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
        :type AreaCoordSet: list of int
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """内容审核涉政嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉政分数。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鉴政结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Name: 涉政人物、违规图标名字。
        :type Name: str
        :param Label: 嫌疑片段鉴政结果标签。内容审核模板[画面鉴政任务控制参数](https://cloud.tencent.com/document/api/266/31773#PoliticalImgReviewTemplateInfo)里 LabelSet 参数与此参数取值范围的对应关系：
violation_photo：
<li>violation_photo：违规图标。</li>
politician：
<li>nation_politician：国家领导人；</li>
<li>province_politician: 省部级领导人；</li>
<li>bureau_politician：厅局级领导人；</li>
<li>county_politician：县处级领导人；</li>
<li>rural_politician：乡科级领导人；</li>
<li>sensitive_politician：敏感政治人物；</li>
<li>foreign_politician：国外领导人。</li>
entertainment：
<li>sensitive_entertainment：敏感娱乐人物。</li>
sport：
<li>sensitive_sport：敏感体育人物。</li>
entrepreneur：
<li>sensitive_entrepreneur：敏感商业人物。</li>
scholar：
<li>sensitive_scholar：敏感教育学者。</li>
celebrity：
<li>sensitive_celebrity：敏感知名人物；</li>
<li>historical_celebrity：历史知名人物。</li>
military：
<li>sensitive_military：敏感军事人物。</li>
        :type Label: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param AreaCoordSet: 涉政人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
        :type AreaCoordSet: list of int
        :param PicUrlExpireTimeStamp: 该字段已废弃，请使用 PicUrlExpireTime。
        :type PicUrlExpireTimeStamp: int
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type PicUrlExpireTime: str
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
        self.PicUrlExpireTime = None


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
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class MediaContentReviewSegmentItem(AbstractModel):
    """内容审核涉黄/暴恐嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉黄分数。
        :type Confidence: float
        :param Label: 嫌疑片段鉴黄结果标签。
        :type Label: str
        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。
        :type Url: str
        :param PicUrlExpireTimeStamp: 该字段已废弃，请使用 PicUrlExpireTime。
        :type PicUrlExpireTimeStamp: int
        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTimeStamp = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class MediaDeleteItem(AbstractModel):
    """指定删除点播视频时的删除内容

    """

    def __init__(self):
        """
        :param Type: 所指定的删除部分。如果未填写该字段则参数无效。可选值有：
<li>TranscodeFiles（删除转码文件）。</li>
<li>WechatPublishFiles（删除微信发布文件）。</li>
        :type Type: str
        :param Definition: 删除由Type参数指定的种类下的视频模板号，模板定义参见[转码模板](https://cloud.tencent.com/document/product/266/33478#.3Cspan-id-.3D-.22zm.22-.3E.3C.2Fspan.3E.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
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
        :param Definition: 雪碧图规格，参见[雪碧图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Height: 雪碧图小图的高度。
        :type Height: int
        :param Width: 雪碧图小图的宽度。
        :type Width: int
        :param TotalCount: 每一张雪碧图大图里小图的数量。
        :type TotalCount: int
        :param ImageUrlSet: 每一张雪碧图大图的地址。
        :type ImageUrlSet: list of str
        :param WebVttUrl: 雪碧图子图位置与时间关系的 WebVtt 文件地址。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。
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
        :param BasicInfo: 基础信息。包括视频名称、分类、播放地址、封面图片等。
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`
        :param MetaData: 元信息。包括大小、时长、视频流信息、音频流信息等。
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
        :param AdaptiveDynamicStreamingInfo: 转自适应码流信息。包括规格、加密类型、打包格式等相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingInfo: :class:`tencentcloud.vod.v20180717.models.MediaAdaptiveDynamicStreamingInfo`
        :param MiniProgramReviewInfo: 小程序审核信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniProgramReviewInfo: :class:`tencentcloud.vod.v20180717.models.MediaMiniProgramReviewInfo`
        :param SubtitleInfo: 字幕信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubtitleInfo: :class:`tencentcloud.vod.v20180717.models.MediaSubtitleInfo`
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
        self.AdaptiveDynamicStreamingInfo = None
        self.MiniProgramReviewInfo = None
        self.SubtitleInfo = None
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
        if params.get("AdaptiveDynamicStreamingInfo") is not None:
            self.AdaptiveDynamicStreamingInfo = MediaAdaptiveDynamicStreamingInfo()
            self.AdaptiveDynamicStreamingInfo._deserialize(params.get("AdaptiveDynamicStreamingInfo"))
        if params.get("MiniProgramReviewInfo") is not None:
            self.MiniProgramReviewInfo = MediaMiniProgramReviewInfo()
            self.MiniProgramReviewInfo._deserialize(params.get("MiniProgramReviewInfo"))
        if params.get("SubtitleInfo") is not None:
            self.SubtitleInfo = MediaSubtitleInfo()
            self.SubtitleInfo._deserialize(params.get("SubtitleInfo"))
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
        :type Size: int
        :param Container: 容器类型，例如 m4a，mp4 等。
        :type Container: str
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Duration: 视频时长，单位：秒。
        :type Duration: float
        :param Rotate: 视频拍摄时的选择角度，单位：度。
        :type Rotate: int
        :param VideoStreamSet: 视频流信息。
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: 音频流信息。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: 视频时长，单位：秒。
        :type VideoDuration: float
        :param AudioDuration: 音频时长，单位：秒。
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


class MediaMiniProgramReviewElem(AbstractModel):
    """小程序审核概要元信息

    """

    def __init__(self):
        """
        :param Type: 审核类型。 
<li>Porn：画面涉黄，</li>
<li>Porn.Ocr：文字涉黄，</li>
<li>Porn.Asr：声音涉黄，</li>
<li>Terrorism：画面涉暴恐，</li>
<li>Political：画面涉政，</li>
<li>Political.Ocr：文字涉政，</li>
<li>Political.Asr：声音涉政。</li>
        :type Type: str
        :param Suggestion: 审核意见。
<li>pass：确认正常，</li>
<li>block：确认违规，</li>
<li>review：疑似违规。</li>
        :type Suggestion: str
        :param Confidence: 审核结果置信度。取值 0~100。
        :type Confidence: float
        """
        self.Type = None
        self.Suggestion = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")


class MediaMiniProgramReviewInfo(AbstractModel):
    """小程序审核信息

    """

    def __init__(self):
        """
        :param MiniProgramReviewList: 审核信息列表。
        :type MiniProgramReviewList: list of MediaMiniProgramReviewInfoItem
        """
        self.MiniProgramReviewList = None


    def _deserialize(self, params):
        if params.get("MiniProgramReviewList") is not None:
            self.MiniProgramReviewList = []
            for item in params.get("MiniProgramReviewList"):
                obj = MediaMiniProgramReviewInfoItem()
                obj._deserialize(item)
                self.MiniProgramReviewList.append(obj)


class MediaMiniProgramReviewInfoItem(AbstractModel):
    """小程序审核信息单元

    """

    def __init__(self):
        """
        :param Definition: 模板id。小程序视频发布的视频所对应的转码模板ID，为0代表原始视频。
        :type Definition: int
        :param MetaData: 视频元信息。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param Url: 小程序审核视频播放地址。
        :type Url: str
        :param ReviewResult: 小程序视频发布状态：
<li>Pass：成功。</li>
<li>Rejected：未通过。</li>
        :type ReviewResult: str
        :param ReviewSummary: 小程序审核元素。
        :type ReviewSummary: list of MediaMiniProgramReviewElem
        """
        self.Definition = None
        self.MetaData = None
        self.Url = None
        self.ReviewResult = None
        self.ReviewSummary = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.Url = params.get("Url")
        self.ReviewResult = params.get("ReviewResult")
        if params.get("ReviewSummary") is not None:
            self.ReviewSummary = []
            for item in params.get("ReviewSummary"):
                obj = MediaMiniProgramReviewElem()
                obj._deserialize(item)
                self.ReviewSummary.append(obj)


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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频转自适应码流任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AdaptiveDynamicStreamingTaskInput`
        :param Output: 对视频转自适应码流任务的输出。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AdaptiveDynamicStreamingInfoItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 转动图任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AnimatedGraphicTaskInput`
        :param Output: 转动图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaAnimatedGraphicsItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频截图做封面任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.CoverBySnapshotTaskInput`
        :param Output: 对视频截图做封面任务的输出。
        :type Output: :class:`tencentcloud.vod.v20180717.models.CoverBySnapshotTaskOutput`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频截雪碧图任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.ImageSpriteTaskInput`
        :param Output: 对视频截雪碧图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaImageSpriteItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :type TranscodeTaskSet: list of TranscodeTaskInput
        :param AnimatedGraphicTaskSet: 视频转动图任务列表。
        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput
        :param SnapshotByTimeOffsetTaskSet: 对视频按时间点截图任务列表。
        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput
        :param SampleSnapshotTaskSet: 对视频采样截图任务列表。
        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput
        :param ImageSpriteTaskSet: 对视频截雪碧图任务列表。
        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput
        :param CoverBySnapshotTaskSet: 对视频截图做封面任务列表。
        :type CoverBySnapshotTaskSet: list of CoverBySnapshotTaskInput
        :param AdaptiveDynamicStreamingTaskSet: 对视频转自适应码流任务列表。
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频做采样截图任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.SampleSnapshotTaskInput`
        :param Output: 对视频做采样截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaSampleSnapshotItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频按指定时间点截图任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTaskInput`
        :param Output: 对视频按指定时间点截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetItem`
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
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
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 转码任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.TranscodeTaskInput`
        :param Output: 转码任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaTranscodeItem`
        :param Progress: 转码进度，取值范围 [0-100] 。
        :type Progress: int
        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.Progress = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))
        self.Progress = params.get("Progress")


class MediaSampleSnapshotInfo(AbstractModel):
    """点播文件采样截图信息

    """

    def __init__(self):
        """
        :param SampleSnapshotSet: 特定规格的采样截图信息集合，每个元素代表一套相同规格的采样截图。
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
        :param Definition: 采样截图规格 ID，参见[采样截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param SampleType: 采样方式，取值范围：
<li>Percent：根据百分比间隔采样。</li>
<li>Time：根据时间间隔采样。</li>
        :type SampleType: str
        :param Interval: 采样间隔
<li>当 SampleType 为 Percent 时，该值表示多少百分比一张图。</li>
<li>当 SampleType 为 Time 时，该值表示多少时间间隔一张图，单位秒， 第一张图均为视频首帧。</li>
        :type Interval: int
        :param ImageUrlSet: 生成的截图 url 列表。
        :type ImageUrlSet: list of str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
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
        :param Definition: 指定时间点截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param PicInfoSet: 同一规格的截图信息集合，每个元素代表一张截图。
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
        :param TimeOffset: 该张截图对应视频文件中的时间偏移，单位为<font color=red>毫秒</font>。
        :type TimeOffset: float
        :param Url: 该张截图的 URL 地址。
        :type Url: str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
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
        :type SourceType: str
        :param SourceContext: 用户创建文件时透传的字段
        :type SourceContext: str
        """
        self.SourceType = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceContext = params.get("SourceContext")


class MediaSubtitleInfo(AbstractModel):
    """字幕信息。

    """

    def __init__(self):
        """
        :param SubtitleSet: 字幕信息列表。
        :type SubtitleSet: list of MediaSubtitleItem
        """
        self.SubtitleSet = None


    def _deserialize(self, params):
        if params.get("SubtitleSet") is not None:
            self.SubtitleSet = []
            for item in params.get("SubtitleSet"):
                obj = MediaSubtitleItem()
                obj._deserialize(item)
                self.SubtitleSet.append(obj)


class MediaSubtitleInput(AbstractModel):
    """字幕信息输入参数。

    """

    def __init__(self):
        """
        :param Name: 字幕名字，长度限制：64 个字符。
        :type Name: str
        :param Language: 字幕语言。常见的取值如下：
<li>cn：中文</li>
<li>ja：日文</li>
<li>en-US：英文</li>
其他取值参考 [RFC5646](https://tools.ietf.org/html/rfc5646)
        :type Language: str
        :param Format: 字幕格式。取值范围如下：
<li>vtt</li>
        :type Format: str
        :param Content: 字幕内容，进行 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。
        :type Content: str
        :param Id: 字幕的唯一标识。长度不能超过16个字符，可以使用大小写字母、数字、下划线（_）或横杠（-）。不能与媒资文件中现有字幕的唯一标识重复。
        :type Id: str
        """
        self.Name = None
        self.Language = None
        self.Format = None
        self.Content = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Language = params.get("Language")
        self.Format = params.get("Format")
        self.Content = params.get("Content")
        self.Id = params.get("Id")


class MediaSubtitleItem(AbstractModel):
    """字幕信息。

    """

    def __init__(self):
        """
        :param Id: 字幕的唯一标识。
        :type Id: str
        :param Name: 字幕名字。
        :type Name: str
        :param Language: 字幕语言。常见的取值如下：
<li>cn：中文</li>
<li>ja：日文</li>
<li>en-US：英文</li>
其他取值参考 [RFC5646](https://tools.ietf.org/html/rfc5646)
        :type Language: str
        :param Format: 字幕格式。取值范围如下：
<li>vtt</li>
        :type Format: str
        :param Url: 字幕 URL。
        :type Url: str
        """
        self.Id = None
        self.Name = None
        self.Language = None
        self.Format = None
        self.Url = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Language = params.get("Language")
        self.Format = params.get("Format")
        self.Url = params.get("Url")


class MediaTrack(AbstractModel):
    """轨道信息

    """

    def __init__(self):
        """
        :param Type: 轨道类型，取值有：
<ul>
<li>Video ：视频轨道。视频轨道由以下 Item 组成：<ul><li>VideoTrackItem</li><li>MediaTransitionItem</li> <li>EmptyTrackItem</li></ul> </li>
<li>Audio ：音频轨道。音频轨道由以下 Item 组成：<ul><li>AudioTrackItem</li><li>MediaTransitionItem</li><li>EmptyTrackItem</li></ul></li>
<li>Sticker ：贴图轨道。贴图轨道以下 Item 组成：<ul><li> StickerTrackItem</li><li>EmptyTrackItem</li></ul></li>	
</ul>
        :type Type: str
        :param TrackItems: 轨道上的媒体片段列表。
        :type TrackItems: list of MediaTrackItem
        """
        self.Type = None
        self.TrackItems = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TrackItems") is not None:
            self.TrackItems = []
            for item in params.get("TrackItems"):
                obj = MediaTrackItem()
                obj._deserialize(item)
                self.TrackItems.append(obj)


class MediaTrackItem(AbstractModel):
    """媒体轨道的片段信息

    """

    def __init__(self):
        """
        :param Type: 片段类型。取值有：
<li>Video：视频片段。</li>
<li>Audio：音频片段。</li>
<li>Sticker：贴图片段。</li>
<li>Transition：转场。</li>
<li>Empty：空白片段。</li>
        :type Type: str
        :param VideoItem: 视频片段，当 Type = Video 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoItem: :class:`tencentcloud.vod.v20180717.models.VideoTrackItem`
        :param AudioItem: 音频片段，当 Type = Audio 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioItem: :class:`tencentcloud.vod.v20180717.models.AudioTrackItem`
        :param StickerItem: 贴图片段，当 Type = Sticker 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type StickerItem: :class:`tencentcloud.vod.v20180717.models.StickerTrackItem`
        :param TransitionItem: 转场，当 Type = Transition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransitionItem: :class:`tencentcloud.vod.v20180717.models.MediaTransitionItem`
        :param EmptyItem: 空白片段，当 Type = Empty 时有效。空片段用于时间轴的占位。<li>如需要两个音频片段之间有一段时间的静音，可以用 EmptyTrackItem 来进行占位。</li>
<li>使用 EmptyTrackItem 进行占位，来定位某个Item。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type EmptyItem: :class:`tencentcloud.vod.v20180717.models.EmptyTrackItem`
        """
        self.Type = None
        self.VideoItem = None
        self.AudioItem = None
        self.StickerItem = None
        self.TransitionItem = None
        self.EmptyItem = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VideoItem") is not None:
            self.VideoItem = VideoTrackItem()
            self.VideoItem._deserialize(params.get("VideoItem"))
        if params.get("AudioItem") is not None:
            self.AudioItem = AudioTrackItem()
            self.AudioItem._deserialize(params.get("AudioItem"))
        if params.get("StickerItem") is not None:
            self.StickerItem = StickerTrackItem()
            self.StickerItem._deserialize(params.get("StickerItem"))
        if params.get("TransitionItem") is not None:
            self.TransitionItem = MediaTransitionItem()
            self.TransitionItem._deserialize(params.get("TransitionItem"))
        if params.get("EmptyItem") is not None:
            self.EmptyItem = EmptyTrackItem()
            self.EmptyItem._deserialize(params.get("EmptyItem"))


class MediaTranscodeInfo(AbstractModel):
    """点播文件转码信息

    """

    def __init__(self):
        """
        :param TranscodeSet: 各规格的转码信息集合，每个元素代表一个规格的转码结果。
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
        :type Url: str
        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/266/33476)。
        :type Definition: int
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和， 单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Size: 媒体文件总大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
        :type Size: int
        :param Duration: 视频时长，单位：秒。
        :type Duration: float
        :param Container: 容器类型，例如 m4a，mp4 等。
        :type Container: str
        :param Md5: 视频的 md5 值。
        :type Md5: str
        :param AudioStreamSet: 音频流信息。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: 视频流信息。
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


class MediaTransitionItem(AbstractModel):
    """转场信息

    """

    def __init__(self):
        """
        :param Duration: 转场持续时间，单位为秒。进行转场处理的两个媒体片段，第二个片段在轨道上的起始时间会自动进行调整，设置为前面一个片段的结束时间减去转场的持续时间。
        :type Duration: float
        :param Transitions: 转场操作列表。图像转场操作和音频转场操作各自最多支持一个。
        :type Transitions: list of TransitionOpertion
        """
        self.Duration = None
        self.Transitions = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        if params.get("Transitions") is not None:
            self.Transitions = []
            for item in params.get("Transitions"):
                obj = TransitionOpertion()
                obj._deserialize(item)
                self.Transitions.append(obj)


class MediaVideoStreamItem(AbstractModel):
    """点播文件视频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 视频流的码率，单位：bps。
        :type Bitrate: int
        :param Height: 视频流的高度，单位：px。
        :type Height: int
        :param Width: 视频流的宽度，单位：px。
        :type Width: int
        :param Codec: 视频流的编码格式，例如 h264。
        :type Codec: str
        :param Fps: 帧率，单位：hz。
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
        :param HighlightConfigure: 智能精彩集锦任务控制参数。
        :type HighlightConfigure: :class:`tencentcloud.vod.v20180717.models.HighlightsConfigureInfoForUpdate`
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
        self.HighlightConfigure = None
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
        if params.get("HighlightConfigure") is not None:
            self.HighlightConfigure = HighlightsConfigureInfoForUpdate()
            self.HighlightConfigure._deserialize(params.get("HighlightConfigure"))
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


class ModifyAIRecognitionTemplateRequest(AbstractModel):
    """ModifyAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。
        :type Definition: int
        :param Name: 视频内容识别模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容识别模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param HeadTailConfigure: 视频片头片尾识别控制参数。
        :type HeadTailConfigure: :class:`tencentcloud.vod.v20180717.models.HeadTailConfigureInfoForUpdate`
        :param SegmentConfigure: 视频拆条识别控制参数。
        :type SegmentConfigure: :class:`tencentcloud.vod.v20180717.models.SegmentConfigureInfoForUpdate`
        :param FaceConfigure: 人脸识别控制参数。
        :type FaceConfigure: :class:`tencentcloud.vod.v20180717.models.FaceConfigureInfoForUpdate`
        :param OcrFullTextConfigure: 文本全文识别控制参数。
        :type OcrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.OcrFullTextConfigureInfoForUpdate`
        :param OcrWordsConfigure: 文本关键词识别控制参数。
        :type OcrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.OcrWordsConfigureInfoForUpdate`
        :param AsrFullTextConfigure: 语音全文识别控制参数。
        :type AsrFullTextConfigure: :class:`tencentcloud.vod.v20180717.models.AsrFullTextConfigureInfoForUpdate`
        :param AsrWordsConfigure: 语音关键词识别控制参数。
        :type AsrWordsConfigure: :class:`tencentcloud.vod.v20180717.models.AsrWordsConfigureInfoForUpdate`
        :param ObjectConfigure: 物体识别控制参数。
        :type ObjectConfigure: :class:`tencentcloud.vod.v20180717.models.ObjectConfigureInfoForUpdate`
        :param ScreenshotInterval: 截帧间隔，单位为秒，最小值为 0.5 秒。
        :type ScreenshotInterval: float
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.SegmentConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfoForUpdate()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
        if params.get("SegmentConfigure") is not None:
            self.SegmentConfigure = SegmentConfigureInfoForUpdate()
            self.SegmentConfigure._deserialize(params.get("SegmentConfigure"))
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfoForUpdate()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfoForUpdate()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfoForUpdate()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfoForUpdate()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfoForUpdate()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfoForUpdate()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")


class ModifyAIRecognitionTemplateResponse(AbstractModel):
    """ModifyAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 自适应转码模板唯一标识。
        :type Definition: int
        :param Name: 模板名称，长度限制：64 个字符。
        :type Name: str
        :param Format: 自适应转码格式，取值范围：
<li>HLS。</li>
        :type Format: str
        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoBitrate: int
        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
        :type DisableHigherVideoResolution: int
        :param StreamInfos: 自适应转码输入流参数信息，最多输入10路流。
注意：各个流的帧率必须保持一致；如果不一致，采用第一个流的帧率作为输出帧率。
        :type StreamInfos: list of AdaptiveStreamTemplate
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Format = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.StreamInfos = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Format = params.get("Format")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class ModifyAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAnimatedGraphicsTemplateRequest(AbstractModel):
    """ModifyAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param Name: 转动图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 动图格式，取值为 gif 和 webp。
        :type Format: str
        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。
        :type Fps: int
        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。
        :type Quality: float
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class ModifyAnimatedGraphicsTemplateResponse(AbstractModel):
    """ModifyAnimatedGraphicsTemplate返回参数结构体

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


class ModifyContentReviewTemplateRequest(AbstractModel):
    """ModifyContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 内容智能识别模板唯一标识。
        :type Definition: int
        :param Name: 内容智能识别模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 内容智能识别模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param TerrorismConfigure: 令人不安全的信息的控制参数。
        :type TerrorismConfigure: :class:`tencentcloud.vod.v20180717.models.TerrorismConfigureInfoForUpdate`
        :param PornConfigure: 令人反感的信息的控制参数。
        :type PornConfigure: :class:`tencentcloud.vod.v20180717.models.PornConfigureInfoForUpdate`
        :param PoliticalConfigure: 令人不适宜的信息控制参数。
        :type PoliticalConfigure: :class:`tencentcloud.vod.v20180717.models.PoliticalConfigureInfoForUpdate`
        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
        :type ProhibitedConfigure: :class:`tencentcloud.vod.v20180717.models.ProhibitedConfigureInfoForUpdate`
        :param UserDefineConfigure: 用户自定义内容智能识别控制参数。
        :type UserDefineConfigure: :class:`tencentcloud.vod.v20180717.models.UserDefineConfigureInfoForUpdate`
        :param ScreenshotInterval: 截帧间隔，单位为秒，最小值为 0.5 秒。
        :type ScreenshotInterval: float
        :param ReviewWallSwitch: 智能识别结果是否进入智能识别墙（对智能识别结果进行人工识别）的开关。
<li>ON：是；</li>
<li>OFF：否。</li>
        :type ReviewWallSwitch: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.TerrorismConfigure = None
        self.PornConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.ScreenshotInterval = None
        self.ReviewWallSwitch = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfoForUpdate()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfoForUpdate()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfoForUpdate()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfoForUpdate()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfoForUpdate()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.SubAppId = params.get("SubAppId")


class ModifyContentReviewTemplateResponse(AbstractModel):
    """ModifyContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSpriteTemplateRequest(AbstractModel):
    """ModifyImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param Name: 雪碧图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 雪碧图中小图的宽度，取值范围： [128, 4096]，单位：px。
        :type Width: int
        :param Height: 雪碧图中小图的高度，取值范围： [128, 4096]，单位：px。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.FillType = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class ModifyImageSpriteTemplateResponse(AbstractModel):
    """ModifyImageSpriteTemplate返回参数结构体

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
        :param ExpireTime: 媒体文件过期时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。
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
        :param AddSubtitles: 新增一组字幕。单个媒体文件最多 16 个字幕。同一个请求中，AddSubtitles 中指定的字幕 Id 必须与 DeleteSubtitleIds 都不相同。
        :type AddSubtitles: list of MediaSubtitleInput
        :param DeleteSubtitleIds: 待删除字幕的唯一标识。同一个请求中，AddSubtitles 中指定的字幕 Id 必须与 DeleteSubtitleIds 都不相同。
        :type DeleteSubtitleIds: list of str
        :param ClearSubtitles: 取值 1 表示清空媒体文件所有的字幕信息，其他值无意义。
同一个请求里，ClearSubtitles 与 AddSubtitles不能同时出现。
        :type ClearSubtitles: int
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
        self.AddSubtitles = None
        self.DeleteSubtitleIds = None
        self.ClearSubtitles = None
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
        if params.get("AddSubtitles") is not None:
            self.AddSubtitles = []
            for item in params.get("AddSubtitles"):
                obj = MediaSubtitleInput()
                obj._deserialize(item)
                self.AddSubtitles.append(obj)
        self.DeleteSubtitleIds = params.get("DeleteSubtitleIds")
        self.ClearSubtitles = params.get("ClearSubtitles")
        self.SubAppId = params.get("SubAppId")


class ModifyMediaInfoResponse(AbstractModel):
    """ModifyMediaInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CoverUrl: 新的视频封面 URL。
* 注意：仅当请求携带 CoverData 时此返回值有效。 *
        :type CoverUrl: str
        :param AddedSubtitleSet: 新增的字幕信息。
        :type AddedSubtitleSet: list of MediaSubtitleItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CoverUrl = None
        self.AddedSubtitleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        if params.get("AddedSubtitleSet") is not None:
            self.AddedSubtitleSet = []
            for item in params.get("AddedSubtitleSet"):
                obj = MediaSubtitleItem()
                obj._deserialize(item)
                self.AddedSubtitleSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyPersonSampleRequest(AbstractModel):
    """ModifyPersonSample请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 素材 ID。
        :type PersonId: str
        :param Name: 名称，长度限制：128 个字符。
        :type Name: str
        :param Description: 描述，长度限制：1024 个字符。
        :type Description: str
        :param Usages: 素材应用场景，可选值：
1. Recognition：用于内容识别，等价于 Recognition.Face。
2. Review：用于不适宜的内容识别，等价于 Review.Face。
3. All：用于内容识别、不适宜的内容识别，等价于 1+2。
        :type Usages: list of str
        :param FaceOperationInfo: 五官操作信息。
        :type FaceOperationInfo: :class:`tencentcloud.vod.v20180717.models.AiSampleFaceOperation`
        :param TagOperationInfo: 标签操作信息。
        :type TagOperationInfo: :class:`tencentcloud.vod.v20180717.models.AiSampleTagOperation`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.Usages = None
        self.FaceOperationInfo = None
        self.TagOperationInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Usages = params.get("Usages")
        if params.get("FaceOperationInfo") is not None:
            self.FaceOperationInfo = AiSampleFaceOperation()
            self.FaceOperationInfo._deserialize(params.get("FaceOperationInfo"))
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        self.SubAppId = params.get("SubAppId")


class ModifyPersonSampleResponse(AbstractModel):
    """ModifyPersonSample返回参数结构体

    """

    def __init__(self):
        """
        :param Person: 素材信息。
        :type Person: :class:`tencentcloud.vod.v20180717.models.AiSamplePerson`
        :param FailFaceInfoSet: 处理失败的五官信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifySampleSnapshotTemplateRequest(AbstractModel):
    """ModifySampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param Name: 采样截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param Format: 图片格式，取值为 jpg 和 png。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")


class ModifySampleSnapshotTemplateResponse(AbstractModel):
    """ModifySampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板唯一标识。
        :type Definition: int
        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式，取值可以为 jpg 和 png。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.SubAppId = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")
        self.FillType = params.get("FillType")


class ModifySnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubAppIdInfoRequest(AbstractModel):
    """ModifySubAppIdInfo请求参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 子应用 ID。
        :type SubAppId: int
        :param Name: 子应用名称，长度限制：40个字符。
        :type Name: str
        :param Description: 子应用简介，长度限制： 300个字符。
        :type Description: str
        """
        self.SubAppId = None
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")


class ModifySubAppIdInfoResponse(AbstractModel):
    """ModifySubAppIdInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubAppIdStatusRequest(AbstractModel):
    """ModifySubAppIdStatus请求参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 子应用 ID。
        :type SubAppId: int
        :param Status: 子应用状态，取值范围：
<li>On：启用。</li>
<li>Off：停用。</li>
<li>Destroyed：销毁。</li>
当前状态如果是 Destoying ，不能进行启用操作，需要等待销毁完成后才能重新启用。
        :type Status: str
        """
        self.SubAppId = None
        self.Status = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.Status = params.get("Status")


class ModifySubAppIdStatusResponse(AbstractModel):
    """ModifySubAppIdStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySuperPlayerConfigRequest(AbstractModel):
    """ModifySuperPlayerConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 播放器配置名称。
        :type Name: str
        :param DrmSwitch: 播放 DRM 保护的自适应码流开关：
<li>ON：开启，表示仅播放 DRM  保护的自适应码流输出；</li>
<li>OFF：关闭，表示播放未加密的自适应码流输出。</li>
        :type DrmSwitch: str
        :param AdaptiveDynamicStreamingDefinition: 允许输出的未加密的自适应码流模板 ID。
        :type AdaptiveDynamicStreamingDefinition: int
        :param DrmStreamingsInfo: 允许输出的 DRM 自适应码流模板内容。
        :type DrmStreamingsInfo: :class:`tencentcloud.vod.v20180717.models.DrmStreamingsInfoForUpdate`
        :param ImageSpriteDefinition: 允许输出的雪碧图模板 ID。
        :type ImageSpriteDefinition: int
        :param ResolutionNames: 播放器对不于不同分辨率的子流展示名字。
        :type ResolutionNames: list of ResolutionNameInfo
        :param Domain: 播放时使用的域名。填 Default 表示使用[默认分发配置](https://cloud.tencent.com/document/product/266/33373)中的域名。
        :type Domain: str
        :param Scheme: 播放时使用的 Scheme。取值范围：
<li>Default：使用[默认分发配置](https://cloud.tencent.com/document/product/266/33373)中的 Scheme；</li>
<li>HTTP；</li>
<li>HTTPS。</li>
        :type Scheme: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.DrmSwitch = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.DrmStreamingsInfo = None
        self.ImageSpriteDefinition = None
        self.ResolutionNames = None
        self.Domain = None
        self.Scheme = None
        self.Comment = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DrmSwitch = params.get("DrmSwitch")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        if params.get("DrmStreamingsInfo") is not None:
            self.DrmStreamingsInfo = DrmStreamingsInfoForUpdate()
            self.DrmStreamingsInfo._deserialize(params.get("DrmStreamingsInfo"))
        self.ImageSpriteDefinition = params.get("ImageSpriteDefinition")
        if params.get("ResolutionNames") is not None:
            self.ResolutionNames = []
            for item in params.get("ResolutionNames"):
                obj = ResolutionNameInfo()
                obj._deserialize(item)
                self.ResolutionNames.append(obj)
        self.Domain = params.get("Domain")
        self.Scheme = params.get("Scheme")
        self.Comment = params.get("Comment")
        self.SubAppId = params.get("SubAppId")


class ModifySuperPlayerConfigResponse(AbstractModel):
    """ModifySuperPlayerConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param Comment: 模板描述信息，长度限制：256 个字符。
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
        :param TEHDConfig: 极速高清转码参数。
        :type TEHDConfig: :class:`tencentcloud.vod.v20180717.models.TEHDConfigForUpdate`
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
        self.TEHDConfig = None
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
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
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
        :param SvgTemplate: SVG 水印模板，该字段仅对 SVG 水印模板有效。
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
        :type ImageUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class ModifyWordSampleRequest(AbstractModel):
    """ModifyWordSample请求参数结构体

    """

    def __init__(self):
        """
        :param Keyword: 关键词，长度限制：128 个字符。
        :type Keyword: str
        :param Usages: <b>关键词应用场景，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜的内容识别；
4. Review.Asr：通过音频识别技术，进行不适宜的内容识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜的内容识别，等价于 3+4；
7. All：包含以上全部，等价于 1+2+3+4。
        :type Usages: list of str
        :param TagOperationInfo: 标签操作信息。
        :type TagOperationInfo: :class:`tencentcloud.vod.v20180717.models.AiSampleTagOperation`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Keyword = None
        self.Usages = None
        self.TagOperationInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Usages = params.get("Usages")
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        self.SubAppId = params.get("SubAppId")


class ModifyWordSampleResponse(AbstractModel):
    """ModifyWordSample返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MosaicInput(AbstractModel):
    """视频处理任务中的马赛克参数类型

    """

    def __init__(self):
        """
        :param CoordinateOrigin: 原点位置，目前仅支持：
<li>TopLeft：表示坐标原点位于视频图像左上角，马赛克原点为图片或文字的左上角。</li>
默认值：TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 马赛克原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 马赛克原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。
        :type YPos: str
        :param Width: 马赛克的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：10%。
        :type Width: str
        :param Height: 马赛克的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 Height 单位为像素，如 100px 表示 Height 为 100 像素。</li>
默认值：10%。
        :type Height: str
        :param StartTimeOffset: 马赛克的起始时间偏移，单位：秒。不填或填0，表示马赛克从画面出现时开始显现。
<li>不填或填0，表示马赛克从画面开始就出现；</li>
<li>当数值大于0时（假设为 n），表示马赛克从画面开始的第 n 秒出现；</li>
<li>当数值小于0时（假设为 -n），表示马赛克从离画面结束 n 秒前开始出现。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 马赛克的结束时间偏移，单位：秒。
<li>不填或填0，表示马赛克持续到画面结束；</li>
<li>当数值大于0时（假设为 n），表示马赛克持续到第 n 秒时消失；</li>
<li>当数值小于0时（假设为 -n），表示马赛克持续到离画面结束 n 秒前消失。</li>
        :type EndTimeOffset: float
        """
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class ObjectConfigureInfo(AbstractModel):
    """物体识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 物体识别任务开关，可选值：
<li>ON：开启智能物体识别任务；</li>
<li>OFF：关闭智能物体识别任务。</li>
        :type Switch: str
        :param ObjectLibrary: 物体库选择，可选值：
<li>Default：使用默认物体库；</li>
<li>UserDefine：使用用户自定义物体库。</li>
<li>All：同时使用默认物体库和用户自定义物体库。</li>
默认值： All，同时使用默认物体库和用户自定义物体库。
        :type ObjectLibrary: str
        """
        self.Switch = None
        self.ObjectLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ObjectLibrary = params.get("ObjectLibrary")


class ObjectConfigureInfoForUpdate(AbstractModel):
    """物体识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 物体识别任务开关，可选值：
<li>ON：开启智能物体识别任务；</li>
<li>OFF：关闭智能物体识别任务。</li>
        :type Switch: str
        :param ObjectLibrary: 物体库选择，可选值：
<li>Default：使用默认物体库；</li>
<li>UserDefine：使用用户自定义物体库。</li>
<li>All：同时使用默认物体库和用户自定义物体库。</li>
        :type ObjectLibrary: str
        """
        self.Switch = None
        self.ObjectLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ObjectLibrary = params.get("ObjectLibrary")


class OcrFullTextConfigureInfo(AbstractModel):
    """文本全文本识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本全文识别任务开关，可选值：
<li>ON：开启智能文本全文识别任务；</li>
<li>OFF：关闭智能文本全文识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class OcrFullTextConfigureInfoForUpdate(AbstractModel):
    """文本全文本识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本全文识别任务开关，可选值：
<li>ON：开启智能文本全文识别任务；</li>
<li>OFF：关闭智能文本全文识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class OcrWordsConfigureInfo(AbstractModel):
    """文本关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本关键词识别任务开关，可选值：
<li>ON：开启文本关键词识别任务；</li>
<li>OFF：关闭文本关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class OcrWordsConfigureInfoForUpdate(AbstractModel):
    """文本关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本关键词识别任务开关，可选值：
<li>ON：开启文本关键词识别任务；</li>
<li>OFF：关闭文本关键词识别任务。</li>
        :type Switch: str
        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class OutputAudioStream(AbstractModel):
    """输出的音频流信息

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式，可选值：
<li>libfdk_aac：适合 mp4 文件。</li>
默认值：libfdk_aac。
        :type Codec: str
        :param SampleRate: 音频流的采样率，可选值：
<li>16000</li>
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。
默认值：16000。
        :type SampleRate: int
        :param AudioChannel: 音频声道数，可选值：
<li>1：单声道 。</li>
<li>2：双声道</li>
默认值：2。
        :type AudioChannel: int
        """
        self.Codec = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class OutputVideoStream(AbstractModel):
    """输出的视频流信息

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码 </li>
默认值：libx264。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 60]，单位：Hz。
默认值：0，表示和第一个视频轨的第一个视频片段的视频帧率一致。
        :type Fps: int
        """
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")


class ParseStreamingManifestRequest(AbstractModel):
    """ParseStreamingManifest请求参数结构体

    """

    def __init__(self):
        """
        :param MediaManifestContent: 待解析的索引文件内容。
        :type MediaManifestContent: str
        :param ManifestType: 视频索引文件格式。默认 m3u8 格式。
<li>m3u8</li>
<li>mpd</li>
        :type ManifestType: str
        """
        self.MediaManifestContent = None
        self.ManifestType = None


    def _deserialize(self, params):
        self.MediaManifestContent = params.get("MediaManifestContent")
        self.ManifestType = params.get("ManifestType")


class ParseStreamingManifestResponse(AbstractModel):
    """ParseStreamingManifest返回参数结构体

    """

    def __init__(self):
        """
        :param MediaSegmentSet: 分片文件列表。
        :type MediaSegmentSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MediaSegmentSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MediaSegmentSet = params.get("MediaSegmentSet")
        self.RequestId = params.get("RequestId")


class PlayStatFileInfo(AbstractModel):
    """播放统计文件信息

    """

    def __init__(self):
        """
        :param Date: 播放统计数据所属日期，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type Date: str
        :param Url: 播放统计文件的 URL 地址。播放统计文件内容为：
<li> date：播放日期。</li>
<li> file_id：视频文件 ID。</li>
<li> ip_count：去重后的客户端 IP 数。</li>
<li> flux：播放流量，单位：字节。</li>
<li> play_times：总的播放次数。</li>
<li> pc_play_times：PC 端播放次数。</li>
<li> mobile_play_times：移动端播放次数。</li>
<li> iphone_play_times：iPhone 端播放次数。</li>
<li> android_play_times：Android 端播放次数。</li>
<li> host_name	域名。</li>
        :type Url: str
        """
        self.Date = None
        self.Url = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Url = params.get("Url")


class PlayerConfig(AbstractModel):
    """播放器配置详情

    """

    def __init__(self):
        """
        :param Name: 播放器配置名字。
        :type Name: str
        :param Type: 播放器配置类型，取值范围：
<li>Preset：系统预置配置；</li>
<li>Custom：用户自定义配置。</li>
        :type Type: str
        :param DrmSwitch: 播放 DRM 保护的自适应码流开关：
<li>ON：开启，表示仅播放 DRM  保护的自适应码流输出；</li>
<li>OFF：关闭，表示播放未加密的自适应码流输出。</li>
        :type DrmSwitch: str
        :param AdaptiveDynamicStreamingDefinition: 允许输出的未加密的自适应码流模板 ID。
        :type AdaptiveDynamicStreamingDefinition: int
        :param DrmStreamingsInfo: 允许输出的 DRM 自适应码流模板内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type DrmStreamingsInfo: :class:`tencentcloud.vod.v20180717.models.DrmStreamingsInfo`
        :param ImageSpriteDefinition: 允许输出的雪碧图模板 ID。
        :type ImageSpriteDefinition: int
        :param ResolutionNameSet: 播放器对不于不同分辨率的子流展示名字。
        :type ResolutionNameSet: list of ResolutionNameInfo
        :param CreateTime: 播放器配置创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 播放器配置最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        :param Domain: 播放时使用的域名。值为 Default，表示使用[默认分发配置](https://cloud.tencent.com/document/product/266/33373)中的域名。
        :type Domain: str
        :param Scheme: 播放时使用的 Scheme。取值范围：
<li>Default：使用[默认分发配置](https://cloud.tencent.com/document/product/266/33373)中的 Scheme；</li>
<li>HTTP；</li>
<li>HTTPS。</li>
        :type Scheme: str
        :param Comment: 模板描述信息。
        :type Comment: str
        """
        self.Name = None
        self.Type = None
        self.DrmSwitch = None
        self.AdaptiveDynamicStreamingDefinition = None
        self.DrmStreamingsInfo = None
        self.ImageSpriteDefinition = None
        self.ResolutionNameSet = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Domain = None
        self.Scheme = None
        self.Comment = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.DrmSwitch = params.get("DrmSwitch")
        self.AdaptiveDynamicStreamingDefinition = params.get("AdaptiveDynamicStreamingDefinition")
        if params.get("DrmStreamingsInfo") is not None:
            self.DrmStreamingsInfo = DrmStreamingsInfo()
            self.DrmStreamingsInfo._deserialize(params.get("DrmStreamingsInfo"))
        self.ImageSpriteDefinition = params.get("ImageSpriteDefinition")
        if params.get("ResolutionNameSet") is not None:
            self.ResolutionNameSet = []
            for item in params.get("ResolutionNameSet"):
                obj = ResolutionNameInfo()
                obj._deserialize(item)
                self.ResolutionNameSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Domain = params.get("Domain")
        self.Scheme = params.get("Scheme")
        self.Comment = params.get("Comment")


class PoliticalAsrReviewTemplateInfo(AbstractModel):
    """语音鉴政任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音鉴政任务开关，可选值：
<li>ON：开启语音鉴政任务；</li>
<li>OFF：关闭语音鉴政任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音鉴政任务开关，可选值：
<li>ON：开启语音鉴政任务；</li>
<li>OFF：关闭语音鉴政任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalConfigureInfo(AbstractModel):
    """鉴政任务控制参数

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴政控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalImgReviewTemplateInfo`
        :param AsrReviewInfo: 语音鉴政控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本鉴政控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PoliticalConfigureInfoForUpdate(AbstractModel):
    """鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴政控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 语音鉴政控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本鉴政控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PoliticalOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PoliticalImgReviewTemplateInfo(AbstractModel):
    """画面鉴政任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 画面鉴政任务开关，可选值：
<li>ON：开启画面鉴政任务；</li>
<li>OFF：关闭画面鉴政任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴政过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>violation_photo：违规图标；</li>
<li>politician：政治人物；</li>
<li>entertainment：娱乐人物；</li>
<li>sport：体育人物；</li>
<li>entrepreneur：商业人物；</li>
<li>scholar：教育学者；</li>
<li>celebrity：知名人物；</li>
<li>military：军事人物。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 97 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 95 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 画面鉴政任务开关，可选值：
<li>ON：开启画面鉴政任务；</li>
<li>OFF：关闭画面鉴政任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴政过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>violation_photo：违规图标；</li>
<li>politician：政治人物；</li>
<li>entertainment：娱乐人物；</li>
<li>sport：体育人物；</li>
<li>entrepreneur：商业人物；</li>
<li>scholar：教育学者；</li>
<li>celebrity：知名人物；</li>
<li>military：军事人物。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalOcrReviewTemplateInfo(AbstractModel):
    """文本鉴政任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴政任务开关，可选值：
<li>ON：开启文本鉴政任务；</li>
<li>OFF：关闭文本鉴政任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本鉴政任务开关，可选值：
<li>ON：开启文本鉴政任务；</li>
<li>OFF：关闭文本鉴政任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornAsrReviewTemplateInfo(AbstractModel):
    """语音鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音鉴黄任务开关，可选值：
<li>ON：开启语音鉴黄任务；</li>
<li>OFF：关闭语音鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音鉴黄任务开关，可选值：
<li>ON：开启语音鉴黄任务；</li>
<li>OFF：关闭语音鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornConfigureInfo(AbstractModel):
    """鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴黄控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornImgReviewTemplateInfo`
        :param AsrReviewInfo: 语音鉴黄控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本鉴黄控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PornConfigureInfoForUpdate(AbstractModel):
    """鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴黄控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 语音鉴黄控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本鉴黄控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.PornOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PornImgReviewTemplateInfo(AbstractModel):
    """画面鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 画面鉴黄任务开关，可选值：
<li>ON：开启画面鉴黄任务；</li>
<li>OFF：关闭画面鉴黄任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴黄过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：亲密行为；</li>
<li>sexy：性感。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 90 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 0 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 画面鉴黄任务开关，可选值：
<li>ON：开启画面鉴黄任务；</li>
<li>OFF：关闭画面鉴黄任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴黄过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：亲密行为；</li>
<li>sexy：性感。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornOcrReviewTemplateInfo(AbstractModel):
    """文本鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴黄任务开关，可选值：
<li>ON：开启文本鉴黄任务；</li>
<li>OFF：关闭文本鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本鉴黄任务开关，可选值：
<li>ON：开启文本鉴黄任务；</li>
<li>OFF：关闭文本鉴黄任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


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
        :param ErrCode: 已弃用，请使用各个具体任务的 ErrCode。
        :type ErrCode: int
        :param Message: 已弃用，请使用各个具体任务的 Message。
        :type Message: str
        :param FileId: 媒体文件 ID
<li>若流程由 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 发起，该字段表示 [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo) 的 FileId；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426) 发起，该字段表示 [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo) 的 Id。</li>
        :type FileId: str
        :param FileName: 媒体文件名称
<li>若流程由 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 发起，该字段表示 [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo) 的 BasicInfo.Name；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426) 发起，该字段表示 [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo) 的 Name。</li>
        :type FileName: str
        :param FileUrl: 媒体文件地址
<li>若流程由 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 发起，该字段表示 [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo) 的 BasicInfo.MediaUrl；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426) 发起，该字段表示 [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo) 的 Url。</li>
        :type FileUrl: str
        :param MetaData: 原始视频的元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param MediaProcessResultSet: 视频处理任务的执行状态与结果。
        :type MediaProcessResultSet: list of MediaProcessTaskResult
        :param AiContentReviewResultSet: 视频内容审核任务的执行状态与结果。
        :type AiContentReviewResultSet: list of AiContentReviewResult
        :param AiAnalysisResultSet: 视频内容分析任务的执行状态与结果。
        :type AiAnalysisResultSet: list of AiAnalysisResult
        :param AiRecognitionResultSet: 视频内容识别任务的执行状态与结果。
        :type AiRecognitionResultSet: list of AiRecognitionResult
        :param TasksPriority: 任务流的优先级，取值范围为 [-10, 10]。
        :type TasksPriority: int
        :param TasksNotifyMode: 任务流状态变更通知模式。
<li>Finish：只有当任务流全部执行完毕时，才发起一次事件通知；</li>
<li>Change：只要任务流中每个子任务的状态发生变化，都进行事件通知；</li>
<li>None：不接受该任务流回调。</li>
        :type TasksNotifyMode: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
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
        :param Type: 任务流模板类型，取值范围：
<li>Preset：系统预置任务流模板；</li>
<li>Custom：用户自定义任务流模板。</li>
        :type Type: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
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
        :param MiniProgramPublishTask: 微信小程序发布任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniProgramPublishTask: :class:`tencentcloud.vod.v20180717.models.WechatMiniProgramPublishTaskInput`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        """
        self.Name = None
        self.Type = None
        self.Comment = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.MiniProgramPublishTask = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Comment = params.get("Comment")
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
        if params.get("MiniProgramPublishTask") is not None:
            self.MiniProgramPublishTask = WechatMiniProgramPublishTaskInput()
            self.MiniProgramPublishTask._deserialize(params.get("MiniProgramPublishTask"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ProcessMediaByProcedureRequest(AbstractModel):
    """ProcessMediaByProcedure请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件 ID。
        :type FileId: str
        :param ProcedureName: [任务流模板](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字。
        :type ProcedureName: str
        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是-10到10，不填代表0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.ProcedureName = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.ProcedureName = params.get("ProcedureName")
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")


class ProcessMediaByProcedureResponse(AbstractModel):
    """ProcessMediaByProcedure返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaByUrlRequest(AbstractModel):
    """ProcessMediaByUrl请求参数结构体

    """

    def __init__(self):
        """
        :param InputInfo: API 已经<font color='red'>不再维护</font>。推荐使用的替代 API 请参考接口描述。
        :type InputInfo: :class:`tencentcloud.vod.v20180717.models.MediaInputInfo`
        :param OutputInfo: 输出文件 COS 路径信息。
        :type OutputInfo: :class:`tencentcloud.vod.v20180717.models.MediaOutputInfo`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.InputInfo = None
        self.OutputInfo = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
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
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
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
        :param FileId: 媒体文件 ID，即该文件在云点播上的全局唯一标识符，在上传成功后由云点播后台分配。可以在 [视频上传完成事件通知](/document/product/266/7830) 或 [云点播控制台](https://console.cloud.tencent.com/vod/media) 获取该字段。
        :type FileId: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
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
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
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


class ProductInstance(AbstractModel):
    """预付费商品实例

    """

    def __init__(self):
        """
        :param ProductType: 预付费商品实例类型，取值有：
<li>StarterPackage：点播新手包。</li>
<li>MiniProgramPlugin：点播小程序插件。</li>
<li>ResourcePackage：点播资源包。</li>
        :type ProductType: str
        :param StartTime: 资源包实例起始日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type StartTime: str
        :param ExpireTime: 资源包实例过期日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type ExpireTime: str
        :param ProductInstanceId: 资源包实例ID。对应每个资源包，系统会分配相应的资源。续费或者升级资源包时，需要带上这个资源ID。
        :type ProductInstanceId: str
        :param LastConsumeDate: 系统最近一次扣除资源包的日期。使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type LastConsumeDate: str
        :param BindStatus: 资源包绑定 License 状态，取值有：
<li>0：未绑定。</li>
<li>1：已绑定。</li>
        :type BindStatus: int
        :param ProductInstanceResourceSet: 预付费资源包实例中包含的资源包列表。
        :type ProductInstanceResourceSet: list of ProductInstanceRecource
        :param ProductInstanceStatus: 资源包实例的状态，取值有：
<li>Effective：生效，可用于计费抵扣。</li>
<li>Isolated：隔离，不可用于计费抵扣。</li>
        :type ProductInstanceStatus: str
        :param RefundStatus: 资源包实例的可退还状态，取值有：
<li>FullRefund：可全额退款。</li>
<li>Denied：不可退款。</li>
        :type RefundStatus: str
        """
        self.ProductType = None
        self.StartTime = None
        self.ExpireTime = None
        self.ProductInstanceId = None
        self.LastConsumeDate = None
        self.BindStatus = None
        self.ProductInstanceResourceSet = None
        self.ProductInstanceStatus = None
        self.RefundStatus = None


    def _deserialize(self, params):
        self.ProductType = params.get("ProductType")
        self.StartTime = params.get("StartTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ProductInstanceId = params.get("ProductInstanceId")
        self.LastConsumeDate = params.get("LastConsumeDate")
        self.BindStatus = params.get("BindStatus")
        if params.get("ProductInstanceResourceSet") is not None:
            self.ProductInstanceResourceSet = []
            for item in params.get("ProductInstanceResourceSet"):
                obj = ProductInstanceRecource()
                obj._deserialize(item)
                self.ProductInstanceResourceSet.append(obj)
        self.ProductInstanceStatus = params.get("ProductInstanceStatus")
        self.RefundStatus = params.get("RefundStatus")


class ProductInstanceRecource(AbstractModel):
    """资源包中包含的资源。

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型。
<li>Storage：存储资源包。</li>
<li>Traffic：流量资源包。</li>
<li>Transcode：普通转码资源包。</li>
<li>TESHD：极速高清转码资源包。</li>
<li>Review：视频审核转码资源包。</li>
        :type ResourceType: str
        :param Amount: 资源包额度。
<li>视频存储资源包，单位为字节。</li>
<li>视频转码资源包，单位为秒。</li>
<li>视频审核资源包，单位为秒。</li>
<li>视频极速高清资源包，单位为秒。</li>
<li>视频加速资源包，单位为字节。</li>
        :type Amount: int
        :param Left: 资源包余量。
<li>视频存储资源包，单位为字节。</li>
<li>视频转码资源包，单位为秒。</li>
<li>视频审核资源包，单位为秒。</li>
<li>视频极速高清资源包，单位为秒。</li>
<li>视频加速资源包，单位为字节。</li>
        :type Left: int
        """
        self.ResourceType = None
        self.Amount = None
        self.Left = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.Amount = params.get("Amount")
        self.Left = params.get("Left")


class ProhibitedAsrReviewTemplateInfo(AbstractModel):
    """语音违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音违禁任务开关，可选值：
<li>ON：开启语音违禁任务；</li>
<li>OFF：关闭语音违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class ProhibitedAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音违禁任务开关，可选值：
<li>ON：开启语音违禁任务；</li>
<li>OFF：关闭语音违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class ProhibitedConfigureInfo(AbstractModel):
    """违禁任务控制参数

    """

    def __init__(self):
        """
        :param AsrReviewInfo: 语音违禁控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本违禁控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedOcrReviewTemplateInfo`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class ProhibitedConfigureInfoForUpdate(AbstractModel):
    """违禁任务控制参数

    """

    def __init__(self):
        """
        :param AsrReviewInfo: 语音违禁控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本违禁控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.ProhibitedOcrReviewTemplateInfoForUpdate`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class ProhibitedOcrReviewTemplateInfo(AbstractModel):
    """文本违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本违禁任务开关，可选值：
<li>ON：开启文本违禁任务；</li>
<li>OFF：关闭文本违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class ProhibitedOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本违禁任务开关，可选值：
<li>ON：开启文本违禁任务；</li>
<li>OFF：关闭文本违禁任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PullEventsRequest(AbstractModel):
    """PullEvents请求参数结构体

    """

    def __init__(self):
        """
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ExtInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ExtInfo = params.get("ExtInfo")
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


class PullUploadRequest(AbstractModel):
    """PullUpload请求参数结构体

    """

    def __init__(self):
        """
        :param MediaUrl: 要拉取的媒体 URL，暂不支持拉取 Dash 格式（可以支持 HLS）。
支持的扩展名详见[媒体类型](https://cloud.tencent.com/document/product/266/9760#.E5.AA.92.E4.BD.93.E7.B1.BB.E5.9E.8B)。
        :type MediaUrl: str
        :param MediaName: 媒体名称。
        :type MediaName: str
        :param CoverUrl: 要拉取的视频封面 URL。仅支持 gif、jpeg、png 三种图片格式。
        :type CoverUrl: str
        :param Procedure: 媒体后续任务操作，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。
        :type Procedure: str
        :param ExpireTime: 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        :param StorageRegion: 指定上传园区，仅适用于对上传地域有特殊需求的用户：
<li>不填默认上传至您的[默认地域](https://cloud.tencent.com/document/product/266/14059?from=11329#.E5.AD.98.E5.82.A8.E5.9C.B0.E5.9F.9F.E6.AD.A5.E9.AA.A4)。</li>
<li>若指定上传园区，请先确认[上传存储设置](https://cloud.tencent.com/document/product/266/14059?from=11329#.E5.AD.98.E5.82.A8.E5.9C.B0.E5.9F.9F.E6.AD.A5.E9.AA.A4)已经开启相应的存储地域。</li>
        :type StorageRegion: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过[创建分类](https://cloud.tencent.com/document/product/266/7812)接口，创建分类，获得分类 ID。
        :type ClassId: int
        :param SessionContext: 来源上下文，用于透传用户请求信息，当指定 Procedure 任务后，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param ExtInfo: 保留字段，特殊用途时使用。
        :type ExtInfo: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param SourceContext: 来源上下文，用于透传用户请求信息，[上传完成回调](/document/product/266/7830) 将返回该字段值，最长 250 个字符。
        :type SourceContext: str
        """
        self.MediaUrl = None
        self.MediaName = None
        self.CoverUrl = None
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SessionContext = None
        self.SessionId = None
        self.ExtInfo = None
        self.SubAppId = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.MediaUrl = params.get("MediaUrl")
        self.MediaName = params.get("MediaName")
        self.CoverUrl = params.get("CoverUrl")
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.ExtInfo = params.get("ExtInfo")
        self.SubAppId = params.get("SubAppId")
        self.SourceContext = params.get("SourceContext")


class PullUploadResponse(AbstractModel):
    """PullUpload返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 拉取上传视频的任务 ID，可以通过该 ID 查询拉取上传任务的状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PullUploadTask(AbstractModel):
    """视频转拉任务信息

    """

    def __init__(self):
        """
        :param TaskId: 转拉上传任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败：
<li>40000：输入参数不合法，请检查输入参数；</li>
<li>60000：源文件错误（如视频数据损坏），请确认源文件是否正常；</li>
<li>70000：内部服务错误，建议重试。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param FileId: 转拉上传完成后生成的视频 ID。
        :type FileId: str
        :param MediaBasicInfo: 转拉完成后生成的媒体文件基础信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaBasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`
        :param MetaData: 原始视频的元信息。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param FileUrl: 转拉上传完成后生成的播放地址。
        :type FileUrl: str
        :param ProcedureTaskId: 若转拉上传时指定了视频处理流程，则该参数为流程任务 ID。
        :type ProcedureTaskId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.MediaBasicInfo = None
        self.MetaData = None
        self.FileUrl = None
        self.ProcedureTaskId = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.FileUrl = params.get("FileUrl")
        self.ProcedureTaskId = params.get("ProcedureTaskId")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")


class PushUrlCacheRequest(AbstractModel):
    """PushUrlCache请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 预热的 URL 列表，单次最多指定20个 URL。
        :type Urls: list of str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Urls = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.SubAppId = params.get("SubAppId")


class PushUrlCacheResponse(AbstractModel):
    """PushUrlCache返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RefererAuthPolicy(AbstractModel):
    """Referer 防盗链配置

    """

    def __init__(self):
        """
        :param Status: [Referer 防盗链](https://cloud.tencent.com/document/product/266/14046)设置状态，可选值：
<li>Enabled: 启用；</li>
<li>Disabled: 禁用。</li>
        :type Status: str
        :param AuthType: Referer 校验类型，可选值：
<li>Black: 黑名单方式校验；</li>
<li>White:白名单方式校验。</li>
        :type AuthType: str
        :param Referers: 用于校验的 Referer 名单。
        :type Referers: list of str
        :param BlankRefererAllowed: 是否允许空 Referer 访问本域名，可选值：
<li>Yes: 是；</li>
<li>No: 否。</li>
        :type BlankRefererAllowed: str
        """
        self.Status = None
        self.AuthType = None
        self.Referers = None
        self.BlankRefererAllowed = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.AuthType = params.get("AuthType")
        self.Referers = params.get("Referers")
        self.BlankRefererAllowed = params.get("BlankRefererAllowed")


class ResetProcedureTemplateRequest(AbstractModel):
    """ResetProcedureTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务流名字
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
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
        self.Comment = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
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


class ResolutionNameInfo(AbstractModel):
    """播放器子流名字信息

    """

    def __init__(self):
        """
        :param MinEdgeLength: 视频短边长度，单位：像素。
        :type MinEdgeLength: int
        :param Name: 展示名字。
        :type Name: str
        """
        self.MinEdgeLength = None
        self.Name = None


    def _deserialize(self, params):
        self.MinEdgeLength = params.get("MinEdgeLength")
        self.Name = params.get("Name")


class ResourceTag(AbstractModel):
    """标签键值。参考[标签](https://cloud.tencent.com/document/product/651)。

    """

    def __init__(self):
        """
        :param TagKey: 标签键。
        :type TagKey: str
        :param TagValue: 标签值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class SampleSnapshotTaskInput(AbstractModel):
    """对视频做采样截图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
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


class SampleSnapshotTemplate(AbstractModel):
    """采样截图模板详情

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 采样截图模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式。
        :type Format: str
        :param SampleType: 采样截图类型。
        :type SampleType: str
        :param SampleInterval: 采样间隔。
        :type SampleInterval: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.SampleType = None
        self.SampleInterval = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")


class SearchMediaRequest(AbstractModel):
    """SearchMedia请求参数结构体

    """

    def __init__(self):
        """
        :param FileIds: 文件 ID 集合，匹配集合中的任意元素。
<li>数组长度限制：10。</li>
<li>单个 ID 长度限制：40个字符。</li>
        :type FileIds: list of str
        :param Names: 文件名集合，模糊匹配媒体文件的文件名，匹配度越高，排序越优先。
<li>单个文件名长度限制：40个字符。</li>
<li>数组长度限制：10。</li>
        :type Names: list of str
        :param NamePrefixes: 文件名前缀，前缀匹配媒体文件的文件名。
<li>单个文件名前缀长度限制：20个字符。</li>
<li>数组长度限制：10。</li>
        :type NamePrefixes: list of str
        :param Descriptions: 文件描述集合，模糊匹配媒体文件的描述，匹配度越高，排序越优先。
<li>单个描述长度限制：100个字符。</li>
<li>数组长度限制：10。</li>
        :type Descriptions: list of str
        :param ClassIds: 分类 ID 集合，匹配集合指定 ID 的分类及其所有子类。
<li>数组长度限制：10。</li>
        :type ClassIds: list of int
        :param Tags: 标签集合，匹配集合中任意元素。
<li>单个标签长度限制：8个字符。</li>
<li>数组长度限制：10。</li>
        :type Tags: list of str
        :param Categories: 文件类型。匹配集合中的任意元素：
<li>Video: 视频文件</li>
<li>Audio: 音频文件</li>
<li>Image: 图片文件</li>
        :type Categories: list of str
        :param SourceTypes: 媒体文件来源集合，来源取值参见 [SourceType](https://cloud.tencent.com/document/product/266/31773#MediaSourceData)。
<li>数组长度限制：10。</li>
        :type SourceTypes: list of str
        :param StreamIds: 推流 [直播码](https://cloud.tencent.com/document/product/267/5959) 集合。匹配集合中的任意元素。
<li>数组长度限制：10。</li>
        :type StreamIds: list of str
        :param Vids: 直播录制文件的唯一标识。匹配集合中的任意元素。
<li>数组长度限制：10。</li>
        :type Vids: list of str
        :param CreateTime: 匹配创建时间在此时间段内的文件。
<li>包含所指定的头尾时间点。</li>
        :type CreateTime: :class:`tencentcloud.vod.v20180717.models.TimeRange`
        :param Sort: 排序方式。
<li>Sort.Field 可选 CreateTime 。</li>
<li>当 Text、 Names 或 Descriptions 不为空时，Sort.Field 字段无效， 搜索结果将以匹配度排序。</li>
        :type Sort: :class:`tencentcloud.vod.v20180717.models.SortBy`
        :param Offset: <div id="p_offset">分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
<li>取值范围：Offset + Limit 不超过5000。（参见：<a href="#maxResultsDesc">接口返回结果数限制</a>）</li></div>
        :type Offset: int
        :param Limit: <div id="p_limit">分页返回的记录条数，默认值：10。将返回第 Offset 到第 Offset+Limit-1 条。
<li>取值范围：Offset + Limit 不超过5000。（参见：<a href="#maxResultsDesc">接口返回结果数限制</a>）</li></div>
        :type Limit: int
        :param Filters: 指定所有媒体文件需要返回的信息，可同时指定多个信息，N 从 0 开始递增。如果未填写该字段，默认返回所有信息。选项有：
<li>basicInfo（视频基础信息）。</li>
<li>metaData（视频元信息）。</li>
<li>transcodeInfo（视频转码结果信息）。</li>
<li>animatedGraphicsInfo（视频转动图结果信息）。</li>
<li>imageSpriteInfo（视频雪碧图信息）。</li>
<li>snapshotByTimeOffsetInfo（视频指定时间点截图信息）。</li>
<li>sampleSnapshotInfo（采样截图信息）。</li>
<li>keyFrameDescInfo（打点信息）。</li>
<li>adaptiveDynamicStreamingInfo（转自适应码流信息）。</li>
<li>miniProgramReviewInfo（小程序审核信息）。</li>
        :type Filters: list of str
        :param StorageRegions: 媒体文件存储地区，如 ap-chongqing，参见[地域列表](https://cloud.tencent.com/document/product/266/9760#.E5.B7.B2.E6.94.AF.E6.8C.81.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
<li>单个存储地区长度限制：20个字符。</li>
<li>数组长度限制：20。</li>
        :type StorageRegions: list of str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param Text: （不推荐：应使用 Names、NamePrefixes 或 Descriptions 替代）
搜索文本，模糊匹配媒体文件名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：64个字符。
        :type Text: str
        :param SourceType: （不推荐：应使用 SourceTypes 替代）
媒体文件来源，来源取值参见 [SourceType](https://cloud.tencent.com/document/product/266/31773#MediaSourceData)。
        :type SourceType: str
        :param StreamId: （不推荐：应使用 StreamIds 替代）
推流 [直播码](https://cloud.tencent.com/document/product/267/5959)。
        :type StreamId: str
        :param Vid: （不推荐：应使用 Vids 替代）
直播录制文件的唯一标识。
        :type Vid: str
        :param StartTime: （不推荐：应使用 CreateTime 替代）
创建时间的开始时间。
<li>大于等于开始时间。</li>
<li>当 CreateTime.After 也存在时，将优先使用 CreateTime.After。</li>
<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。</li>
        :type StartTime: str
        :param EndTime: （不推荐：应使用 CreateTime 替代）
创建时间的结束时间。
<li>小于结束时间。</li>
<li>当 CreateTime.Before 也存在时，将优先使用 CreateTime.Before。</li>
<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。</li>
        :type EndTime: str
        """
        self.FileIds = None
        self.Names = None
        self.NamePrefixes = None
        self.Descriptions = None
        self.ClassIds = None
        self.Tags = None
        self.Categories = None
        self.SourceTypes = None
        self.StreamIds = None
        self.Vids = None
        self.CreateTime = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.StorageRegions = None
        self.SubAppId = None
        self.Text = None
        self.SourceType = None
        self.StreamId = None
        self.Vid = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Names = params.get("Names")
        self.NamePrefixes = params.get("NamePrefixes")
        self.Descriptions = params.get("Descriptions")
        self.ClassIds = params.get("ClassIds")
        self.Tags = params.get("Tags")
        self.Categories = params.get("Categories")
        self.SourceTypes = params.get("SourceTypes")
        self.StreamIds = params.get("StreamIds")
        self.Vids = params.get("Vids")
        if params.get("CreateTime") is not None:
            self.CreateTime = TimeRange()
            self.CreateTime._deserialize(params.get("CreateTime"))
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Filters = params.get("Filters")
        self.StorageRegions = params.get("StorageRegions")
        self.SubAppId = params.get("SubAppId")
        self.Text = params.get("Text")
        self.SourceType = params.get("SourceType")
        self.StreamId = params.get("StreamId")
        self.Vid = params.get("Vid")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class SearchMediaResponse(AbstractModel):
    """SearchMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索条件的记录总数。
<li>最大值：5000。当命中记录数超过5000时，该字段将返回 5000，而非实际命中总数。</li>
        :type TotalCount: int
        :param MediaInfoSet: 媒体文件信息列表。
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


class SegmentConfigureInfo(AbstractModel):
    """视频拆条任务识别控制参数

    """

    def __init__(self):
        """
        :param Switch: 视频拆条识别任务开关，可选值：
<li>ON：开启智能视频拆条识别任务；</li>
<li>OFF：关闭智能视频拆条识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class SegmentConfigureInfoForUpdate(AbstractModel):
    """视频拆条识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 视频拆条识别任务开关，可选值：
<li>ON：开启智能视频拆条识别任务；</li>
<li>OFF：关闭智能视频拆条识别任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class SimpleAesEdkPair(AbstractModel):
    """简单加密加解密秘钥对。

    """

    def __init__(self):
        """
        :param Edk: 加密后的数据密钥。
        :type Edk: str
        :param Dk: 数据密钥。返回的数据密钥 DK 为 Base64 编码字符串。
        :type Dk: str
        """
        self.Edk = None
        self.Dk = None


    def _deserialize(self, params):
        self.Edk = params.get("Edk")
        self.Dk = params.get("Dk")


class SimpleHlsClipRequest(AbstractModel):
    """SimpleHlsClip请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 需要裁剪的腾讯云点播 HLS 视频 URL。
        :type Url: str
        :param StartTimeOffset: 裁剪的开始偏移时间，单位秒。默认 0，即从视频开头开始裁剪。负数表示距离视频结束多少秒开始裁剪。例如 -10 表示从倒数第 10 秒开始裁剪。
        :type StartTimeOffset: float
        :param EndTimeOffset: 裁剪的结束偏移时间，单位秒。默认 0，即裁剪到视频尾部。负数表示距离视频结束多少秒结束裁剪。例如 -10 表示到倒数第 10 秒结束裁剪。
        :type EndTimeOffset: float
        :param IsPersistence: 是否固化。0 不固化，1 固化。默认不固化。
        :type IsPersistence: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Url = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.IsPersistence = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.IsPersistence = params.get("IsPersistence")
        self.SubAppId = params.get("SubAppId")


class SimpleHlsClipResponse(AbstractModel):
    """SimpleHlsClip返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 裁剪后的视频地址。
        :type Url: str
        :param MetaData: 裁剪后的视频元信息。目前`Size`，`Rotate`，`VideoDuration`，`AudioDuration` 几个字段暂时缺省，没有真实数据。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param FileId: 剪辑固化后的视频的媒体文件的唯一标识。
        :type FileId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.MetaData = None
        self.FileId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.FileId = params.get("FileId")
        self.RequestId = params.get("RequestId")


class SnapshotByTimeOffset2017(AbstractModel):
    """截图输出信息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param TimeOffset: 截图的具体时间点，单位：毫秒。
        :type TimeOffset: int
        :param Url: 截图输出文件地址。
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
        :param Definition: 截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
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
        :param ExtTimeOffsetSet: 截图时间点列表，时间点支持 s、% 两种格式：
<li>当字符串以 s 结尾，表示时间点单位为秒，如 3.5s 表示时间点为第3.5秒；</li>
<li>当字符串以 % 结尾，表示时间点为视频时长的百分比大小，如10%表示时间点为视频前第10%的时间。</li>
        :type ExtTimeOffsetSet: list of str
        :param TimeOffsetSet: 截图时间点列表，单位为<font color=red>毫秒</font>。此参数已不再建议使用，建议您使用 ExtTimeOffsetSet 参数。
        :type TimeOffsetSet: list of float
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.ExtTimeOffsetSet = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ExtTimeOffsetSet = params.get("ExtTimeOffsetSet")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class SnapshotByTimeOffsetTemplate(AbstractModel):
    """指定时间点截图模板详情

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 指定时间点截图模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Format: 图片格式。
        :type Format: str
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>black：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>black：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")


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


class SpecificationDataItem(AbstractModel):
    """指定规格任务统计数据。

    """

    def __init__(self):
        """
        :param Specification: 任务规格。
        :type Specification: str
        :param Data: 统计数据。
        :type Data: list of TaskStatDataItem
        """
        self.Specification = None
        self.Data = None


    def _deserialize(self, params):
        self.Specification = params.get("Specification")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TaskStatDataItem()
                obj._deserialize(item)
                self.Data.append(obj)


class SplitMediaOutputConfig(AbstractModel):
    """视频拆条的结果文件输出。

    """

    def __init__(self):
        """
        :param MediaName: 输出文件名，最长 64 个字符。缺省由系统指定生成文件名。
        :type MediaName: str
        :param Type: 输出文件格式，可选值：mp4、hls。默认是 mp4。
        :type Type: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/7812) 接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param ExpireTime: 输出文件的过期时间，超过该时间文件将被删除，默认为永久不过期，格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        """
        self.MediaName = None
        self.Type = None
        self.ClassId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.MediaName = params.get("MediaName")
        self.Type = params.get("Type")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")


class SplitMediaRequest(AbstractModel):
    """SplitMedia请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 视频的 ID。
        :type FileId: str
        :param Segments: 视频拆条任务信息列表，最多同时支持100个拆条信息。
        :type Segments: list of SplitMediaTaskConfig
        :param SessionContext: 标识来源上下文，用于透传用户请求信息，在 SplitMediaComplete 回调和任务流状态变更回调将返回该字段值，最长 1000个字符。
        :type SessionContext: str
        :param SessionId: 用于任务去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param TasksPriority: 任务的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.Segments = None
        self.SessionContext = None
        self.SessionId = None
        self.TasksPriority = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("Segments") is not None:
            self.Segments = []
            for item in params.get("Segments"):
                obj = SplitMediaTaskConfig()
                obj._deserialize(item)
                self.Segments.append(obj)
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.TasksPriority = params.get("TasksPriority")
        self.SubAppId = params.get("SubAppId")


class SplitMediaResponse(AbstractModel):
    """SplitMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 视频拆条的任务 ID，可以通过该 ID 查询拆条任务（任务类型为 SplitMedia）的状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SplitMediaTask(AbstractModel):
    """视频拆条任务信息，仅当 TaskType 为 SplitMedia，该字段有值。

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/266/50368#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
        :type ErrCodeExt: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param FileInfoSet: 视频拆条任务详细信息列表。
        :type FileInfoSet: list of SplitMediaTaskSegmentInfo
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.FileInfoSet = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = SplitMediaTaskSegmentInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")


class SplitMediaTaskConfig(AbstractModel):
    """视频拆条任务配置信息。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 视频拆条起始的偏移时间，单位：秒。
<li>不填或填0，表示转码后的视频从原始视频的起始位置开始；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频从原始视频的第 n 秒位置开始；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频从原始视频结束 n 秒前的位置开始。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 视频拆条结束的偏移时间，单位：秒。
<li>不填或填0，表示转码后的视频持续到原始视频的末尾终止；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频持续到原始视频第 n 秒时终止；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频持续到原始视频结束 n 秒前终止。</li>
        :type EndTimeOffset: float
        :param ProcedureName: [任务流模板](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字，如果要对生成的新视频执行任务流时填写。
        :type ProcedureName: str
        :param OutputConfig: 视频拆条输出信息。
        :type OutputConfig: :class:`tencentcloud.vod.v20180717.models.SplitMediaOutputConfig`
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.ProcedureName = None
        self.OutputConfig = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.ProcedureName = params.get("ProcedureName")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = SplitMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))


class SplitMediaTaskInput(AbstractModel):
    """视频拆条任务输入信息

    """

    def __init__(self):
        """
        :param FileId: 视频的 ID。
        :type FileId: str
        :param StartTimeOffset: 视频拆条起始的偏移时间，单位：秒。
<li>不填或填0，表示转码后的视频从原始视频的起始位置开始；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频从原始视频的第 n 秒位置开始；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频从原始视频结束 n 秒前的位置开始。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 视频拆条结束的偏移时间，单位：秒。
<li>不填或填0，表示转码后的视频持续到原始视频的末尾终止；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频持续到原始视频第 n 秒时终止；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频持续到原始视频结束 n 秒前终止。</li>
        :type EndTimeOffset: float
        :param ProcedureName: [任务流模板](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字，如果要对生成的新视频执行任务流时填写。
        :type ProcedureName: str
        :param OutputConfig: 视频拆条输出信息。
        :type OutputConfig: :class:`tencentcloud.vod.v20180717.models.SplitMediaOutputConfig`
        """
        self.FileId = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.ProcedureName = None
        self.OutputConfig = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.ProcedureName = params.get("ProcedureName")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = SplitMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))


class SplitMediaTaskSegmentInfo(AbstractModel):
    """视频拆条任务信息。

    """

    def __init__(self):
        """
        :param Input: 视频拆条任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.SplitMediaTaskInput`
        :param Output: 视频拆条任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.TaskOutputMediaInfo`
        :param ProcedureTaskId: 若发起视频拆条任务时指定了视频处理流程，则该字段为流程任务 ID。
        :type ProcedureTaskId: str
        """
        self.Input = None
        self.Output = None
        self.ProcedureTaskId = None


    def _deserialize(self, params):
        if params.get("Input") is not None:
            self.Input = SplitMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = TaskOutputMediaInfo()
            self.Output._deserialize(params.get("Output"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")


class StatDataItem(AbstractModel):
    """统计数据

    """

    def __init__(self):
        """
        :param Time: 数据所在时间区间的开始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。如：当时间粒度为天，2018-12-01T00:00:00+08:00，表示2018年12月1日（含）到2018年12月2日（不含）区间。
<li>表示小时级别数据时，2019-08-22T00:00:00+08:00表示2019-08-22日0点到1点的统计数据。</li>
<li>表示天级别数据时，2019-08-22T00:00:00+08:00表示2019-08-22日的统计数据。</li>
        :type Time: str
        :param Value: 数据大小。
<li>存储空间的数据，单位是字节。</li>
<li>转码时长的数据，单位是秒。</li>
<li>流量数据，单位是字节。</li>
<li>带宽数据，单位是比特每秒。</li>
        :type Value: int
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class StickerTrackItem(AbstractModel):
    """贴图轨上的贴图信息。

    """

    def __init__(self):
        """
        :param SourceMedia: 贴图片段的媒体素材来源，可以是：
<li>点播的媒体文件 ID；</li>
<li>其他媒体文件的下载 URL。</li>
注意：当使用其他媒体文件的下载 URL 作为素材来源，且开启了访问控制（如防盗链）时，需要在 URL 携带访问控制参数（如防盗链签名）。
        :type SourceMedia: str
        :param Duration: 贴图的持续时间，单位为秒。
        :type Duration: float
        :param StartTime: 贴图在轨道上的起始时间，单位为秒。
        :type StartTime: float
        :param CoordinateOrigin: 原点位置，取值有：
<li>Center：坐标原点为中心位置，如画布中心。</li>
默认值：Center。
        :type CoordinateOrigin: str
        :param XPos: 贴图原点距离画布原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示贴图 XPos 为画布宽度指定百分比的位置，如 10% 表示 XPos 为画布宽度的 10%。</li><li>当字符串以 px 结尾，表示贴图 XPos 单位为像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 贴图原点距离画布原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示贴图 YPos 为画布高度指定百分比的位置，如 10% 表示 YPos 为画布高度的 10%。</li>
<li>当字符串以 px 结尾，表示贴图 YPos 单位为像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。
        :type YPos: str
        :param Width: 贴图的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示贴图 Width 为画布宽度的百分比大小，如 10% 表示 Width 为画布宽度的 10%。</li>
<li>当字符串以 px 结尾，表示贴图 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取贴图素材本身的 Width、Height。</li>
<li>当 Width 为空0，Height 非空，则 Width 按比例缩放</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Width: str
        :param Height: 贴图的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示贴图 Height 为画布高度的百分比大小，如 10% 表示 Height 为画布高度的 10%。</li>
<li>当字符串以 px 结尾，表示贴图 Height 单位为像素，如 100px 表示 Hieght 为 100 像素。</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取贴图素材本身的 Width、Height。</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Height: str
        :param ImageOperations: 对贴图进行的操作，如图像旋转等。
        :type ImageOperations: list of ImageTransform
        """
        self.SourceMedia = None
        self.Duration = None
        self.StartTime = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.ImageOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.Duration = params.get("Duration")
        self.StartTime = params.get("StartTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("ImageOperations") is not None:
            self.ImageOperations = []
            for item in params.get("ImageOperations"):
                obj = ImageTransform()
                obj._deserialize(item)
                self.ImageOperations.append(obj)


class StorageStatData(AbstractModel):
    """云点播存储用量的分区统计数据

    """

    def __init__(self):
        """
        :param Area: 点播存储的计费区域，可能值：
<li>Chinese Mainland：中国境内（不包含港澳台）。</li>
<li>Outside Chinese Mainland：中国境外。</li>
        :type Area: str
        :param TotalStorage: 当前总存储量，单位是字节。
        :type TotalStorage: int
        :param InfrequentStorage: 当前低频存储量，单位是字节。
        :type InfrequentStorage: int
        :param StandardStorage: 当前标准存储量，单位是字节。
        :type StandardStorage: int
        """
        self.Area = None
        self.TotalStorage = None
        self.InfrequentStorage = None
        self.StandardStorage = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.TotalStorage = params.get("TotalStorage")
        self.InfrequentStorage = params.get("InfrequentStorage")
        self.StandardStorage = params.get("StandardStorage")


class SubAppIdInfo(AbstractModel):
    """子应用信息。

    """

    def __init__(self):
        """
        :param SubAppId: 子应用 ID。
        :type SubAppId: int
        :param Name: 子应用名称。
        :type Name: str
        :param Description: 子应用简介。
        :type Description: str
        :param CreateTime: 子应用创建时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param Status: 子应用状态，有效值：
<li>On：启用；</li>
<li>Off：停用。</li>
<li>Destroying：销毁中。</li>
<li>Destroyed：销毁完成。</li>
        :type Status: str
        """
        self.SubAppId = None
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")


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
        :param CycleConfig: 水印周期配置，用于配置水印周期性地显示与隐藏。
主要使用场景是：为了视频防遮标，在视频多个地方设置水印，这些水印按固定顺序周期性地显示与隐藏。
例如，设置 A、B、C、D 4 个水印分别位于视频的左上角、右上角、右下角、左下角处，视频开始时，{ A 显示 5 秒 -> B 显示 5 秒 -> C 显示 5 秒 -> D 显示 5 秒 } -> A 显示 5 秒 -> B 显示 5 秒 -> ...，任何时刻只显示一处水印。
花括号 {} 表示由 A、B、C、D 4 个水印组成的大周期，可以看出每个大周期持续 20 秒。
可以看出，A、B、C、D 都是周期性地显示 5 秒、隐藏 15 秒，且四者有固定的显示顺序。
此配置项即用来描述单个水印的周期配置。
        :type CycleConfig: :class:`tencentcloud.vod.v20180717.models.WatermarkCycleConfigForUpdate`
        """
        self.Width = None
        self.Height = None
        self.CycleConfig = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("CycleConfig") is not None:
            self.CycleConfig = WatermarkCycleConfigForUpdate()
            self.CycleConfig._deserialize(params.get("CycleConfig"))


class TEHDConfig(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        """
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不启用极速高清。
        :type Type: str
        :param MaxVideoBitrate: 视频码率上限，当 Type 指定了极速高清类型时有效。
不填或填0表示不设视频码率上限。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")


class TEHDConfigForUpdate(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        """
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不修改。
        :type Type: str
        :param MaxVideoBitrate: 视频码率上限，不填代表不修改。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")


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


class TaskOutputMediaInfo(AbstractModel):
    """视频处理任务的输出媒体文件信息

    """

    def __init__(self):
        """
        :param FileId: 媒体文件 ID。
        :type FileId: str
        :param MediaBasicInfo: 转拉完成后生成的媒体文件基础信息。
        :type MediaBasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`
        """
        self.FileId = None
        self.MediaBasicInfo = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))


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
        :param CreateTime: 任务创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param BeginProcessTime: 任务开始执行时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。若任务尚未开始，该字段为空。
        :type BeginProcessTime: str
        :param FinishTime: 任务结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。若任务尚未完成，该字段为空。
        :type FinishTime: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息。
        :type SessionContext: str
        """
        self.TaskId = None
        self.TaskType = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")


class TaskStatData(AbstractModel):
    """视频处理任务统计数据。

    """

    def __init__(self):
        """
        :param TaskType: 任务类型。
<li> Transcoding: 普通转码</li>
<li> Transcoding-TESHD: 极速高清转码</li>
<li> Editing: 视频编辑</li>
<li> AdaptiveBitrateStreaming: 自适应码流</li>
<li> ContentAudit: 内容审核</li>
<li>Transcode: 转码，包含普通转码、极速高清和视频编辑（不推荐使用）</li>
        :type TaskType: str
        :param Summary: 任务数统计数据概览，用量单位为秒。
        :type Summary: list of TaskStatDataItem
        :param Details: 不同规格任务统计数据详情。
转码规格：
<li>Remuxing: 转封装</li>
<li>Audio: 音频转码</li>
<li>Standard.H264.SD: H.264编码方式标清转码</li>
<li>Standard.H264.HD: H.264编码方式高清转码</li>
<li>Standard.H264.FHD: H.264编码方式全高清转码</li>
<li>Standard.H264.2K: H.264编码方式2K转码</li>
<li>Standard.H264.4K: H.264编码方式4K转码</li>
<li>Standard.H265.SD: H.265编码方式标清转码</li>
<li>Standard.H265.HD: H.265编码方式高清转码</li>
<li>Standard.H265.FHD: H.265编码方式全高清转码</li>
<li>Standard.H265.2K: H.265编码方式2K转码</li>
<li>Standard.H265.4K: H.265编码方式4K转码</li>
<li>TESHD-10.H264.SD: H.264编码方式标清极速高清转码</li>
<li>TESHD-10.H264.HD: H.264编码方式高清极速高清转码</li>
<li>TESHD-10.H264.FHD: H.264编码方式全高清极速高清转码</li>
<li>TESHD-10.H264.2K: H.264编码方式2K极速高清转码</li>
<li>TESHD-10.H264.4K: H.264编码方式4K极速高清转码</li>
<li>TESHD-10.H265.SD: H.265编码方式标清极速高清转码</li>
<li>TESHD-10.H265.HD: H.265编码方式高清极速高清转码</li>
<li>TESHD-10.H265.FHD: H.265编码方式全高清极速高清转码</li>
<li>TESHD-10.H265.2K: H.265编码方式2K极速高清转码</li>
<li>TESHD-10.H265.4K: H.265编码方式4K极速高清转码</li>
<li>Edit.Audio: 音频编辑</li>
<li>Edit.H264.SD: H.264编码方式标清视频编辑</li>
<li>Edit.H264.HD: H.264编码方式高清视频编辑</li>
<li>Edit.H264.FHD: H.264编码方式全高清视频编辑</li>
<li>Edit.H264.2K: H.264编码方式2K视频编辑</li>
<li>Edit.H264.4K: H.264编码方式4K视频编辑</li>
<li>Edit.H265.SD: H.265编码方式标清视频编辑</li>
<li>Edit.H265.HD: H.265编码方式高清视频编辑</li>
<li>Edit.H265.FHD: H.265编码方式全高清视频编辑</li>
<li>Edit.H265.2K: H.265编码方式2K视频编辑</li>
<li>Edit.H265.4K: H.265编码方式4K视频编辑</li>
        :type Details: list of SpecificationDataItem
        """
        self.TaskType = None
        self.Summary = None
        self.Details = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        if params.get("Summary") is not None:
            self.Summary = []
            for item in params.get("Summary"):
                obj = TaskStatDataItem()
                obj._deserialize(item)
                self.Summary.append(obj)
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = SpecificationDataItem()
                obj._deserialize(item)
                self.Details.append(obj)


class TaskStatDataItem(AbstractModel):
    """任务统计数据，包括任务数和用量。

    """

    def __init__(self):
        """
        :param Time: 数据所在时间区间的开始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#52)。如：当时间粒度为天，2018-12-01T00:00:00+08:00，表示2018年12月1日（含）到2018年12月2日（不含）区间。
        :type Time: str
        :param Count: 任务数。
        :type Count: int
        :param Usage: 任务用量。
        :type Usage: int
        """
        self.Time = None
        self.Count = None
        self.Usage = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Count = params.get("Count")
        self.Usage = params.get("Usage")


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


class TerrorismConfigureInfo(AbstractModel):
    """鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴恐任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismImgReviewTemplateInfo`
        :param OcrReviewInfo: 文字鉴恐任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class TerrorismConfigureInfoForUpdate(AbstractModel):
    """鉴恐任务控制参数。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴恐任务控制参数。
        :type ImgReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismImgReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本鉴恐任务控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.TerrorismOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class TerrorismImgReviewTemplateInfo(AbstractModel):
    """画面鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 画面鉴恐任务开关，可选值：
<li>ON：开启画面鉴恐任务；</li>
<li>OFF：关闭画面鉴恐任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴恐过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>guns：武器枪支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥画面；</li>
<li>police：警察部队；</li>
<li>banners：暴恐旗帜；</li>
<li>militant：武装分子；</li>
<li>explosion：爆炸火灾；</li>
<li>terrorists：暴恐人物；</li>
<li>scenario：暴恐画面。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 90 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 80 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TerrorismImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面鉴恐任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 画面鉴恐任务开关，可选值：
<li>ON：开启画面鉴恐任务；</li>
<li>OFF：关闭画面鉴恐任务。</li>
        :type Switch: str
        :param LabelSet: 画面鉴恐过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>guns：武器枪支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥画面；</li>
<li>police：警察部队；</li>
<li>banners：暴恐旗帜；</li>
<li>militant：武装分子；</li>
<li>explosion：爆炸火灾；</li>
<li>terrorists：暴恐人物；</li>
<li>scenario：暴恐画面。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TerrorismOcrReviewTemplateInfo(AbstractModel):
    """文本鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴恐任务开关，可选值：
<li>ON：开启文本鉴恐任务；</li>
<li>OFF：关闭文本鉴恐任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TerrorismOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴恐任务开关，可选值：
<li>ON：开启文本鉴恐任务；</li>
<li>OFF：关闭文本鉴恐任务。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TextWatermarkTemplateInput(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        """
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。
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
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。
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


class TimeRange(AbstractModel):
    """用于描述一个时间段的通用数据类型。

    """

    def __init__(self):
        """
        :param After: <li>大于等于此时间（起始时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。</li>
        :type After: str
        :param Before: <li>小于此时间（结束时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。</li>
        :type Before: str
        """
        self.After = None
        self.Before = None


    def _deserialize(self, params):
        self.After = params.get("After")
        self.Before = params.get("Before")


class TranscodePlayInfo2017(AbstractModel):
    """视频转码播放信息（2017 版）

    """

    def __init__(self):
        """
        :param Url: 播放地址。
        :type Url: str
        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/266/33476)。
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
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param FileId: 被转码文件 ID。
        :type FileId: str
        :param FileName: 被转码文件名称。
        :type FileName: str
        :param Duration: 视频时长，单位：秒。
        :type Duration: int
        :param CoverUrl: 封面地址。
        :type CoverUrl: str
        :param PlayInfoSet: 视频转码后生成的播放信息。
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
        :type WatermarkSet: list of WatermarkInput
        :param MosaicSet: 马赛克列表，最大可支持 10 张。
        :type MosaicSet: list of MosaicInput
        :param StartTimeOffset: 转码后的视频的起始时间偏移，单位：秒。
<li>不填或填0，表示转码后的视频从原始视频的起始位置开始；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频从原始视频的第 n 秒位置开始；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频从原始视频结束 n 秒前的位置开始。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 转码后视频的终止时间偏移，单位：秒。
<li>不填或填0，表示转码后的视频持续到原始视频的末尾终止；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频持续到原始视频第 n 秒时终止；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频持续到原始视频结束 n 秒前终止。</li>
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.WatermarkSet = None
        self.MosaicSet = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("MosaicSet") is not None:
            self.MosaicSet = []
            for item in params.get("MosaicSet"):
                obj = MosaicInput()
                obj._deserialize(item)
                self.MosaicSet.append(obj)
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


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
        :type Name: str
        :param Comment: 模板描述信息。
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
        :param TEHDConfig: 极速高清转码参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TEHDConfig: :class:`tencentcloud.vod.v20180717.models.TEHDConfig`
        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式板。</li>
        :type ContainerType: str
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
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
        self.TEHDConfig = None
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
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class TransitionOpertion(AbstractModel):
    """转场操作

    """

    def __init__(self):
        """
        :param Type: 转场类型，取值有：
<ul>
<li>图像的转场操作，用于两个视频片段图像间的转场处理：
<ul>
<li>ImageFadeInFadeOut：图像淡入淡出。 </li>
<li>BowTieHorizontal：水平蝴蝶结。 </li>
<li>BowTieVertical：垂直蝴蝶结。 </li>
<li>ButterflyWaveScrawler：晃动。 </li>
<li>Cannabisleaf：枫叶。 </li>
<li>Circle：弧形收放。 </li>
<li>CircleCrop：圆环聚拢。 </li>
<li>Circleopen：椭圆聚拢。 </li>
<li>Crosswarp：横向翘曲。 </li>
<li>Cube：立方体。 </li>
<li>DoomScreenTransition：幕布。 </li>
<li>Doorway：门廊。 </li>
<li>Dreamy：波浪。 </li>
<li>DreamyZoom：水平聚拢。 </li>
<li>FilmBurn：火烧云。 </li>
<li>GlitchMemories：抖动。 </li>
<li>Heart：心形。 </li>
<li>InvertedPageCurl：翻页。 </li>
<li>Luma：腐蚀。 </li>
<li>Mosaic：九宫格。 </li>
<li>Pinwheel：风车。 </li>
<li>PolarFunction：椭圆扩散。 </li>
<li>PolkaDotsCurtain：弧形扩散。 </li>
<li>Radial：雷达扫描 </li>
<li>RotateScaleFade：上下收放。 </li>
<li>Squeeze：上下聚拢。 </li>
<li>Swap：放大切换。 </li>
<li>Swirl：螺旋。 </li>
<li>UndulatingBurnOutSwirl：水流蔓延。 </li>
<li>Windowblinds：百叶窗。 </li>
<li>WipeDown：向下收起。 </li>
<li>WipeLeft：向左收起。 </li>
<li>WipeRight：向右收起。 </li>
<li>WipeUp：向上收起。 </li>
<li>ZoomInCircles：水波纹。 </li>
</ul>
</li>
<li>音频的转场操作，用于两个音频片段间的转场处理：
<ul>
<li>AudioFadeInFadeOut：声音淡入淡出。 </li>
</ul>
</li>
</ul>
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")


class UrlSignatureAuthPolicy(AbstractModel):
    """基于签名的 Key 防盗链信息

    """

    def __init__(self):
        """
        :param Status: [Key 防盗链](https://cloud.tencent.com/document/product/266/14047)设置状态，可选值：
<li>Enabled: 启用；</li>
<li>Disabled: 禁用。</li>
        :type Status: str
        :param EncryptedKey: [Key 防盗链](https://cloud.tencent.com/document/product/266/14047)中用于生成签名的密钥。
        :type EncryptedKey: str
        """
        self.Status = None
        self.EncryptedKey = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.EncryptedKey = params.get("EncryptedKey")


class UserDefineAsrTextReviewTemplateInfo(AbstractModel):
    """用户自定义语音审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定语音审核任务开关，可选值：
<li>ON：开启自定义语音审核任务；</li>
<li>OFF：关闭自定义语音审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义语音过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义语音关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineAsrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义语音审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定语音审核任务开关，可选值：
<li>ON：开启自定义语音审核任务；</li>
<li>OFF：关闭自定义语音审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义语音过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义语音关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineConfigureInfo(AbstractModel):
    """用户自定义审核任务控制参数

    """

    def __init__(self):
        """
        :param FaceReviewInfo: 用户自定义人物审核控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineFaceReviewTemplateInfo`
        :param AsrReviewInfo: 用户自定义语音审核控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineAsrTextReviewTemplateInfo`
        :param OcrReviewInfo: 用户自定义文本审核控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineOcrTextReviewTemplateInfo`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfo()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class UserDefineConfigureInfoForUpdate(AbstractModel):
    """用户自定义审核任务控制参数。

    """

    def __init__(self):
        """
        :param FaceReviewInfo: 用户自定义人物审核控制参数。
        :type FaceReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineFaceReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 用户自定义语音审核控制参数。
        :type AsrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineAsrTextReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 用户自定义文本审核控制参数。
        :type OcrReviewInfo: :class:`tencentcloud.vod.v20180717.models.UserDefineOcrTextReviewTemplateInfoForUpdate`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfoForUpdate()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class UserDefineFaceReviewTemplateInfo(AbstractModel):
    """用户自定义人物审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定义人物审核任务开关，可选值：
<li>ON：开启自定义人物审核任务；</li>
<li>OFF：关闭自定义人物审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义人物过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义人物库的时，需要添加对应人物标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 97 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 95 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineFaceReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义人物审核任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 用户自定义人物审核任务开关，可选值：
<li>ON：开启自定义人物审核任务；</li>
<li>OFF：关闭自定义人物审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义人物过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义人物库的时，需要添加对应人物标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineOcrTextReviewTemplateInfo(AbstractModel):
    """用户自定义文本审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定文本审核任务开关，可选值：
<li>ON：开启自定义文本审核任务；</li>
<li>OFF：关闭自定义文本审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义文本过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义文本关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineOcrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义文本审核任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 用户自定文本审核任务开关，可选值：
<li>ON：开启自定义文本审核任务；</li>
<li>OFF：关闭自定义文本审核任务。</li>
        :type Switch: str
        :param LabelSet: 用户自定义文本过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义文本关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class VideoTemplateInfo(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
<li>av1：AOMedia Video 1 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。av1 编码容器目前只支持 mp4 。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 100]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊填充。</li>
默认值：black 。
        :type FillType: str
        :param Vcrf: 视频恒定码率控制因子，取值范围为[1, 51]。
如果指定该参数，将使用 CRF 的码率控制方式做转码（视频码率将不再生效）。
如果没有特殊需求，不建议指定该参数。
        :type Vcrf: int
        :param Gop: 关键帧 I 帧之间的间隔，取值范围：0 和 [1, 100000]，单位：帧数。
当填 0 或不填时，系统将自动设置 gop 长度。
        :type Gop: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.FillType = None
        self.Vcrf = None
        self.Gop = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        self.Gop = params.get("Gop")


class VideoTemplateInfoForUpdate(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
<li>av1：AOMedia Video 1 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。av1 编码容器目前只支持 mp4 。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 100]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
        :type Height: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊填充。</li>
        :type FillType: str
        :param Vcrf: 视频恒定码率控制因子。取值范围为[0, 51]，填0表示禁用该参数。
如果没有特殊需求，不建议指定该参数。
        :type Vcrf: int
        :param Gop: 关键帧 I 帧之间的间隔，取值范围：0 和 [1, 100000]，单位：帧数。
当填 0 或不填时，系统将自动设置 gop 长度。
        :type Gop: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.FillType = None
        self.Vcrf = None
        self.Gop = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        self.Gop = params.get("Gop")


class VideoTrackItem(AbstractModel):
    """视频轨的视频片段信息。

    """

    def __init__(self):
        """
        :param SourceMedia: 视频片段的媒体素材来源，可以是：
<li>点播的媒体文件 ID；</li>
<li>其他媒体文件的下载 URL。</li>
注意：当使用其他媒体文件的下载 URL 作为素材来源，且开启了访问控制（如防盗链）时，需要在 URL 携带访问控制参数（如防盗链签名）。
        :type SourceMedia: str
        :param SourceMediaStartTime: 视频片段取自素材文件的起始时间，单位为秒。默认为0。
        :type SourceMediaStartTime: float
        :param Duration: 视频片段时长，单位为秒。默认取视频素材本身长度，表示截取全部素材。如果源文件是图片，Duration需要大于0。
        :type Duration: float
        :param CoordinateOrigin: 视频原点位置，取值有：
<li>Center：坐标原点为中心位置，如画布中心。</li>
默认值 ：Center。
        :type CoordinateOrigin: str
        :param XPos: 视频片段原点距离画布原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 XPos 为画布宽度指定百分比的位置，如 10% 表示 XPos 为画布口宽度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 XPos 单位为像素，如 100px 表示 XPos 为100像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 视频片段原点距离画布原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 YPos 为画布高度指定百分比的位置，如 10% 表示 YPos 为画布高度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 YPos 单位为像素，如 100px 表示 YPos 为100像素。</li>
默认值：0px。
        :type YPos: str
        :param Width: 视频片段的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Width 为画布宽度的百分比大小，如 10% 表示 Width 为画布宽度的 10%。</li>
<li>当字符串以 px 结尾，表示视频片段 Width 单位为像素，如 100px 表示 Width 为100像素。</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频素材本身的 Width、Height。</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Width: str
        :param Height: 视频片段的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示视频片段 Height 为画布高度的百分比大小，如 10% 表示 Height 为画布高度的 10%；
</li><li>当字符串以 px 结尾，表示视频片段 Height 单位为像素，如 100px 表示 Height 为100像素。</li>
<li>当 Width、Height 均为空，则 Width 和 Height 取视频素材本身的 Width、Height。</li>
<li>当 Width 为空，Height 非空，则 Width 按比例缩放</li>
<li>当 Width 非空，Height 为空，则 Height 按比例缩放。</li>
        :type Height: str
        :param ImageOperations: 对图像进行的操作，如图像旋转等。
        :type ImageOperations: list of ImageTransform
        :param AudioOperations: 对音频进行操作，如静音等。
        :type AudioOperations: list of AudioTransform
        """
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.ImageOperations = None
        self.AudioOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("ImageOperations") is not None:
            self.ImageOperations = []
            for item in params.get("ImageOperations"):
                obj = ImageTransform()
                obj._deserialize(item)
                self.ImageOperations.append(obj)
        if params.get("AudioOperations") is not None:
            self.AudioOperations = []
            for item in params.get("AudioOperations"):
                obj = AudioTransform()
                obj._deserialize(item)
                self.AudioOperations.append(obj)


class WatermarkCycleConfigForUpdate(AbstractModel):
    """水印周期配置。

    """

    def __init__(self):
        """
        :param StartTime: 水印在视频里第一次出现的播放时间点，单位：秒。
        :type StartTime: float
        :param DisplayDuration: 在一个水印周期内，水印显示的持续时间，单位：秒。
        :type DisplayDuration: float
        :param CycleDuration: 一个水印周期的持续时间，单位：秒。
填 0 表示水印只持续一个水印周期（即在整个视频里只显示 DisplayDuration 秒）。
        :type CycleDuration: float
        """
        self.StartTime = None
        self.DisplayDuration = None
        self.CycleDuration = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.DisplayDuration = params.get("DisplayDuration")
        self.CycleDuration = params.get("CycleDuration")


class WatermarkInput(AbstractModel):
    """视频处理任务中的水印参数类型

    """

    def __init__(self):
        """
        :param Definition: 水印模板 ID。
        :type Definition: int
        :param TextContent: 文字内容，长度不超过100个字符。仅当水印类型为文字水印时填写。
文字水印不支持截图打水印。
        :type TextContent: str
        :param SvgContent: SVG 内容。长度不超过 2000000 个字符。仅当水印类型为 SVG 水印时填写。
SVG 水印不支持截图打水印。
        :type SvgContent: str
        :param StartTimeOffset: 水印的起始时间偏移，单位：秒。不填或填0，表示水印从画面出现时开始显现。
<li>不填或填0，表示水印从画面开始就出现；</li>
<li>当数值大于0时（假设为 n），表示水印从画面开始的第 n 秒出现；</li>
<li>当数值小于0时（假设为 -n），表示水印从离画面结束 n 秒前开始出现。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 水印的结束时间偏移，单位：秒。
<li>不填或填0，表示水印持续到画面结束；</li>
<li>当数值大于0时（假设为 n），表示水印持续到第 n 秒时消失；</li>
<li>当数值小于0时（假设为 -n），表示水印持续到离画面结束 n 秒前消失。</li>
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.TextContent = None
        self.SvgContent = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


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
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。
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


class WeChatMiniProgramPublishRequest(AbstractModel):
    """WeChatMiniProgramPublish请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件 ID。
        :type FileId: str
        :param SourceDefinition: 发布视频所对应的转码模板 ID，为0代表原始视频。
        :type SourceDefinition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.SourceDefinition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.SourceDefinition = params.get("SourceDefinition")
        self.SubAppId = params.get("SubAppId")


class WeChatMiniProgramPublishResponse(AbstractModel):
    """WeChatMiniProgramPublish返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class WechatMiniProgramPublishTask(AbstractModel):
    """微信小程序发布任务信息

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
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param FileId: 发布视频文件 ID。
        :type FileId: str
        :param SourceDefinition: 发布视频所对应的转码模板 ID，为 0 代表原始视频。
        :type SourceDefinition: int
        :param PublishResult: 微信小程序视频发布状态，取值：
<li>Pass：发布成功；</li>
<li>Failed：发布失败；</li>
<li>Rejected：审核未通过。</li>
        :type PublishResult: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.SourceDefinition = None
        self.PublishResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.SourceDefinition = params.get("SourceDefinition")
        self.PublishResult = params.get("PublishResult")


class WechatMiniProgramPublishTaskInput(AbstractModel):
    """微信小程序发布任务类型

    """

    def __init__(self):
        """
        :param SourceDefinition: 发布视频所对应的转码模板 ID，为 0 代表原始视频。
        :type SourceDefinition: int
        """
        self.SourceDefinition = None


    def _deserialize(self, params):
        self.SourceDefinition = params.get("SourceDefinition")


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
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param FileId: 发布视频文件 ID。
        :type FileId: str
        :param Definition: 微信发布模板 ID。
        :type Definition: int
        :param SourceDefinition: 发布视频所对应的转码模板 ID，为 0 代表原始视频。
        :type SourceDefinition: int
        :param WechatStatus: 微信发布状态，取值：
<li>FAIL：失败；</li>
<li>SUCCESS：成功；</li>
<li>AUDITNOTPASS：审核未通过；</li>
<li>NOTTRIGGERED：尚未发起微信发布。</li>
        :type WechatStatus: str
        :param WechatVid: 微信 Vid。
        :type WechatVid: str
        :param WechatUrl: 微信地址。
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