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


class AudioResult(AbstractModel):
    """音频审核输出参数

    """

    def __init__(self):
        r"""
        :param HitFlag: 该字段用于返回审核内容是否命中审核模型；取值：0（**未命中**）、1（**命中**）。
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Text: 该字段用于返回音频文件经ASR识别后的文本信息。最长可识别**5小时**的音频文件，若超出时长限制，接口将会报错。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Url: 该字段用于返回音频片段存储的链接地址，该地址有效期为1天。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Duration: 该字段用于返回音频文件的时长，单位为秒。
        :type Duration: str
        :param Extra: 该字段用于返回额外附加信息，不同客户或Biztype下返回信息不同。
        :type Extra: str
        :param TextResults: 该字段用于返回音频文件经ASR识别后产生的文本的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
        :type TextResults: list of AudioResultDetailTextResult
        :param MoanResults: 该字段用于返回音频文件呻吟检测的详细审核结果。具体结果内容请参见AudioResultDetailMoanResult数据结构的细节描述。
        :type MoanResults: list of AudioResultDetailMoanResult
        :param LanguageResults: 该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
        :type LanguageResults: list of AudioResultDetailLanguageResult
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param RecognitionResults: 识别类标签结果信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognitionResults: list of RecognitionResult
        """
        self.HitFlag = None
        self.Label = None
        self.Suggestion = None
        self.Score = None
        self.Text = None
        self.Url = None
        self.Duration = None
        self.Extra = None
        self.TextResults = None
        self.MoanResults = None
        self.LanguageResults = None
        self.SubLabel = None
        self.RecognitionResults = None


    def _deserialize(self, params):
        self.HitFlag = params.get("HitFlag")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        self.Text = params.get("Text")
        self.Url = params.get("Url")
        self.Duration = params.get("Duration")
        self.Extra = params.get("Extra")
        if params.get("TextResults") is not None:
            self.TextResults = []
            for item in params.get("TextResults"):
                obj = AudioResultDetailTextResult()
                obj._deserialize(item)
                self.TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self.MoanResults = []
            for item in params.get("MoanResults"):
                obj = AudioResultDetailMoanResult()
                obj._deserialize(item)
                self.MoanResults.append(obj)
        if params.get("LanguageResults") is not None:
            self.LanguageResults = []
            for item in params.get("LanguageResults"):
                obj = AudioResultDetailLanguageResult()
                obj._deserialize(item)
                self.LanguageResults.append(obj)
        self.SubLabel = params.get("SubLabel")
        if params.get("RecognitionResults") is not None:
            self.RecognitionResults = []
            for item in params.get("RecognitionResults"):
                obj = RecognitionResult()
                obj._deserialize(item)
                self.RecognitionResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailLanguageResult(AbstractModel):
    """音频语言种类检测结果

    """

    def __init__(self):
        r"""
        :param Label: 该字段用于返回对应的语言种类信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 该参数用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于当前返回的语种标签；
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param StartTime: 该参数用于返回对应语种标签的片段在音频文件内的开始时间，单位为毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param EndTime: 该参数用于返回对应语种标签的片段在音频文件内的结束时间，单位为毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        :param SubLabelCode: *内测中，敬请期待*
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self.Label = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None
        self.SubLabelCode = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailMoanResult(AbstractModel):
    """音频呻吟审核结果

    """

    def __init__(self):
        r"""
        :param Label: 该字段用于返回检测结果需要检测的内容类型，此处固定为**Moan**（呻吟）以调用呻吟检测功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 该字段用于返回呻吟检测的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于呻吟内容。
        :type Score: int
        :param StartTime: 该字段用于返回对应呻吟标签的片段在音频文件内的开始时间，单位为毫秒。
        :type StartTime: float
        :param EndTime: 该字段用于返回对应呻吟标签的片段在音频文件内的结束时间，单位为毫秒。
        :type EndTime: float
        :param SubLabelCode: *内测中，敬请期待*
        :type SubLabelCode: str
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        """
        self.Label = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None
        self.SubLabelCode = None
        self.SubLabel = None
        self.Suggestion = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubLabelCode = params.get("SubLabelCode")
        self.SubLabel = params.get("SubLabel")
        self.Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailSpeakerResult(AbstractModel):
    """音频说话人声纹识别返回结果

    """

    def __init__(self):
        r"""
        :param Label: 该字段用于返回检测结果需要检测的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 该字段用于返回呻吟检测的置信度，取值范围：0（置信度最低）-100（置信度最高），越高代表音频越有可能属于说话人声纹。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param StartTime: 该字段用于返回对应说话人的片段在音频文件内的开始时间，单位为毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param EndTime: 该字段用于返回对应说话人的片段在音频文件内的结束时间，单位为毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        """
        self.Label = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailTextResult(AbstractModel):
    """音频ASR文本审核结果

    """

    def __init__(self):
        r"""
        :param Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Keywords: 该字段用于返回ASR识别出的文本内容命中的关键词信息，用于标注内容违规的具体原因（如：加我微信）。该参数可能会有多个返回值，代表命中的多个关键词；若返回值为空，Score不为空，则代表识别结果所对应的恶意标签（Label）来自于语义模型判断的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param LibId: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的ID，以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的名称,以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param LibType: 该字段用于返回自定义关键词对应的词库类型，取值为**1**（黑白库）和**2**（自定义关键词库），若未配置自定义关键词库,则默认值为1（黑白库匹配）。
        :type LibType: int
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        """
        self.Label = None
        self.Keywords = None
        self.LibId = None
        self.LibName = None
        self.Score = None
        self.Suggestion = None
        self.LibType = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Keywords = params.get("Keywords")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Score = params.get("Score")
        self.Suggestion = params.get("Suggestion")
        self.LibType = params.get("LibType")
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSegments(AbstractModel):
    """表示声音段信息

    """

    def __init__(self):
        r"""
        :param OffsetTime: 该字段用于返回音频片段的开始时间，单位为秒。对于点播文件，该参数代表对应音频相对于完整音轨的偏移时间，如0（代表不偏移），5（音轨开始后5秒），10（音轨开始后10秒）；对于直播文件，该参数则返回对应音频片段开始时的Unix时间戳，如：1594650717。
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetTime: str
        :param Result: 该字段用于返回音频片段的具体审核结果，详细内容敬请参考AudioResult数据结构的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ams.v20201229.models.AudioResult`
        """
        self.OffsetTime = None
        self.Result = None


    def _deserialize(self, params):
        self.OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self.Result = AudioResult()
            self.Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BucketInfo(AbstractModel):
    """文件桶信息
    参考腾讯云存储相关说明 https://cloud.tencent.com/document/product/436/44352

    """

    def __init__(self):
        r"""
        :param Bucket: 该字段用于标识腾讯云对象存储的存储桶名称,关于文件桶的详细信息敬请参考 [腾讯云存储相关说明](https://cloud.tencent.com/document/product/436/44352)。
        :type Bucket: str
        :param Region: 该字段用于标识腾讯云对象存储的托管机房的分布地区，对象存储 COS 的数据存放在这些地域的存储桶中。
        :type Region: str
        :param Object: 该字段用于标识腾讯云对象存储的对象Key,对象z作为基本单元被存放在存储桶中；用户可以通过腾讯云控制台、API、SDK 等多种方式管理对象。有关对象的详细描述敬请参阅相应 [产品文档](https://cloud.tencent.com/document/product/436/13324)。
        :type Object: str
        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 该字段表示创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要取消的审核任务。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAudioModerationSyncTaskRequest(AbstractModel):
    """CreateAudioModerationSyncTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizType: Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :type BizType: str
        :param DataId: 数据标识，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type DataId: str
        :param FileFormat: 音频文件资源格式，当前支持格式：wav、mp3、m4a，请按照实际文件格式填入。
        :type FileFormat: str
        :param Name: 文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type Name: str
        :param FileContent: 数据Base64编码，短音频同步接口仅传入可音频内容；
支持范围：文件大小不能超过5M，时长不可超过60s；
支持格式：wav (PCM编码)、mp3、m4a (采样率：16kHz~48kHz，位深：16bit 小端，声道数：单声道/双声道，建议格式：16kHz/16bit/单声道)。
        :type FileContent: str
        :param FileUrl: 音频资源访问链接，与FileContent参数必须二选一输入；
支持范围及格式：同FileContent；
        :type FileUrl: str
        """
        self.BizType = None
        self.DataId = None
        self.FileFormat = None
        self.Name = None
        self.FileContent = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        self.FileFormat = params.get("FileFormat")
        self.Name = params.get("Name")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAudioModerationSyncTaskResponse(AbstractModel):
    """CreateAudioModerationSyncTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataId: 请求接口时传入的数据标识
        :type DataId: str
        :param Name: 文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param BizType: Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :type BizType: str
        :param Suggestion: 智能审核服务对于内容违规类型的等级，可选值：
Pass 建议通过；
Reveiw 建议复审；
Block 建议屏蔽；
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 智能审核服务对于内容违规类型的判断，详见返回值列表
如：Label：Porn（色情）；
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param AsrText: 音频文本，备注：这里的文本最大只返回前1000个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrText: str
        :param TextResults: 音频中对话内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type TextResults: list of TextResult
        :param MoanResults: 音频中低俗内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type MoanResults: list of MoanResult
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param LanguageResults: 该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type LanguageResults: list of AudioResultDetailLanguageResult
        :param SpeakerResults: 音频中说话人识别返回结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeakerResults: list of AudioResultDetailSpeakerResult
        :param RecognitionResults: 识别类标签结果信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognitionResults: list of RecognitionResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataId = None
        self.Name = None
        self.BizType = None
        self.Suggestion = None
        self.Label = None
        self.AsrText = None
        self.TextResults = None
        self.MoanResults = None
        self.SubLabel = None
        self.LanguageResults = None
        self.SpeakerResults = None
        self.RecognitionResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Name = params.get("Name")
        self.BizType = params.get("BizType")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.AsrText = params.get("AsrText")
        if params.get("TextResults") is not None:
            self.TextResults = []
            for item in params.get("TextResults"):
                obj = TextResult()
                obj._deserialize(item)
                self.TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self.MoanResults = []
            for item in params.get("MoanResults"):
                obj = MoanResult()
                obj._deserialize(item)
                self.MoanResults.append(obj)
        self.SubLabel = params.get("SubLabel")
        if params.get("LanguageResults") is not None:
            self.LanguageResults = []
            for item in params.get("LanguageResults"):
                obj = AudioResultDetailLanguageResult()
                obj._deserialize(item)
                self.LanguageResults.append(obj)
        if params.get("SpeakerResults") is not None:
            self.SpeakerResults = []
            for item in params.get("SpeakerResults"):
                obj = AudioResultDetailSpeakerResult()
                obj._deserialize(item)
                self.SpeakerResults.append(obj)
        if params.get("RecognitionResults") is not None:
            self.RecognitionResults = []
            for item in params.get("RecognitionResults"):
                obj = RecognitionResult()
                obj._deserialize(item)
                self.RecognitionResults.append(obj)
        self.RequestId = params.get("RequestId")


class CreateAudioModerationTaskRequest(AbstractModel):
    """CreateAudioModerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: 该字段表示输入的音频审核任务信息，具体输入内容请参见TaskInput数据结构的详细描述。<br> 备注：最多同时可创建**10个任务**。
        :type Tasks: list of TaskInput
        :param BizType: 该字段表示策略的具体编号，用于接口调度，在内容安全控制台中可配置。若不传入Biztype参数（留空），则代表采用默认的识别策略；传入则会在审核时根据业务场景采取不同的审核策略。<br>备注：Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。
        :type BizType: str
        :param Type: 该字段表示输入的音频审核类型，取值为：**AUDIO**（点播音频）和 **LIVE_AUDIO**（直播音频），默认值为AUDIO。
        :type Type: str
        :param Seed: 可选参数，该字段表示回调签名的key信息，用于保证数据的安全性。 签名方法为在返回的HTTP头部添加 X-Signature 的字段，值为： seed + body 的 SHA256 编码和Hex字符串，在收到回调数据后，可以根据返回的body，用 **sha256(seed + body)**, 计算出 `X-Signature` 进行验证。<br>具体使用实例可参考 [回调签名示例](https://cloud.tencent.com/document/product/1219/53263)。
        :type Seed: str
        :param CallbackUrl: 可选参数，该字段表示接受审核信息回调的地址，格式为URL链接默认格式。配置成功后，审核过程中产生的违规音频片段将通过此接口发送。回调返回内容格式请参考 [回调签名示例](https://cloud.tencent.com/document/product/1219/53257#.E7.A4.BA.E4.BE.8B2-.E5.9B.9E.E8.B0.83.E7.AD.BE.E5.90.8D.E7.A4.BA.E4.BE.8B)
        :type CallbackUrl: str
        """
        self.Tasks = None
        self.BizType = None
        self.Type = None
        self.Seed = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Seed = params.get("Seed")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAudioModerationTaskResponse(AbstractModel):
    """CreateAudioModerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Results: 该字段用于返回任务创建的结果，具体输出内容请参见TaskResult数据结构的详细描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 该字段表示创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
<br>备注：查询接口单次最大查询量为**20条每次**。
        :type TaskId: str
        :param ShowAllSegments: 该布尔字段表示是否展示全部的音频片段，取值：True(展示全部的音频分片)、False(只展示命中审核规则的音频分片)；默认值为False。
        :type ShowAllSegments: bool
        """
        self.TaskId = None
        self.ShowAllSegments = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ShowAllSegments = params.get("ShowAllSegments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 该字段用于返回创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param DataId: 该字段用于返回调用音频审核接口时在Tasks参数内传入的数据ID参数，方便数据的辨别和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param BizType: 该字段用于返回调用音频审核接口时传入的BizType参数，方便数据的辨别和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param Name: 该字段用于返回调用音频审核接口时传入的TaskInput参数中的任务名称，方便任务的识别与管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: 该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Type: 该字段用于返回调用音频审核接口时输入的音频审核类型，取值为：**AUDIO**（点播音频）和**LIVE_AUDIO**（直播音频），默认值为AUDIO。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Labels: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param InputInfo: 该字段用于返回审核服务的媒体内容信息，主要包括传入文件类型和访问地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.ams.v20201229.models.InputInfo`
        :param AudioText: 该字段用于返回音频文件识别出的对应文本内容，最大支持**前1000个字符**。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioText: str
        :param AudioSegments: 该字段用于返回音频片段的审核结果，主要包括开始时间和音频审核的相应结果。<br>具体输出内容请参见AudioSegments及AudioResult数据结构的详细描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSegments: list of AudioSegments
        :param ErrorType: 当任务状态为Error时，该字段用于返回对应错误的类型；任务状态非Error时，默认返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorType: str
        :param ErrorDescription: 当任务状态为Error时，该字段用于返回对应错误的详细描述，任务状态非Error时默认返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDescription: str
        :param CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param Label: 该字段用于返回检测结果所对应的标签。如果未命中恶意，返回Normal，如果命中恶意，则返回Labels中优先级最高的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.DataId = None
        self.BizType = None
        self.Name = None
        self.Status = None
        self.Type = None
        self.Suggestion = None
        self.Labels = None
        self.InputInfo = None
        self.AudioText = None
        self.AudioSegments = None
        self.ErrorType = None
        self.ErrorDescription = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.Label = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DataId = params.get("DataId")
        self.BizType = params.get("BizType")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("InputInfo") is not None:
            self.InputInfo = InputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.AudioText = params.get("AudioText")
        if params.get("AudioSegments") is not None:
            self.AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self.AudioSegments.append(obj)
        self.ErrorType = params.get("ErrorType")
        self.ErrorDescription = params.get("ErrorDescription")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Label = params.get("Label")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 该参数表示任务列表每页展示的任务条数，**默认值为10**（每页展示10条任务）。
        :type Limit: int
        :param Filter: 该参数表示任务筛选器的输入参数，可根据业务类型、审核文件类型、处理建议及任务状态筛选想要查看的审核任务，具体参数内容请参见TaskFilter数据结构的详细描述。
        :type Filter: :class:`tencentcloud.ams.v20201229.models.TaskFilter`
        :param PageToken: 该参数表示翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
        :type PageToken: str
        :param StartTime: 该参数表示任务列表的开始时间，格式为ISO8601标准的时间戳。**默认值为最近3天**，若传入该参数，则在这一时间到EndTime之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :type StartTime: str
        :param EndTime: 该参数表示任务列表的结束时间，格式为ISO8601标准的时间戳。**默认值为空**，若传入该参数，则在这StartTime到这一时间之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :type EndTime: str
        """
        self.Limit = None
        self.Filter = None
        self.PageToken = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self.Filter = TaskFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.PageToken = params.get("PageToken")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 该字段用于返回当前查询的任务总量，格式为int字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param Data: 该字段用于返回当前页的任务详细数据，具体输出内容请参见TaskData数据结构的详细描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskData
        :param PageToken: 该字段用于返回翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.PageToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TaskData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageToken = params.get("PageToken")
        self.RequestId = params.get("RequestId")


class InputInfo(AbstractModel):
    """输入信息详情

    """

    def __init__(self):
        r"""
        :param Type: 该字段表示文件访问类型，取值为**URL**（资源链接）和**COS** (腾讯云对象存储)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Url: 该字段表示文件访问的链接地址，格式为标准URL格式。<br> 备注：当Type为URL时此字段不为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param BucketInfo: 该字段表示文件访问的腾讯云存储桶信息。<br> 备注：当Type为COS时此字段不为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketInfo: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
        """
        self.Type = None
        self.Url = None
        self.BucketInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self.BucketInfo = BucketInfo()
            self.BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    """媒体类型

    """

    def __init__(self):
        r"""
        :param Codecs: 该字段用于返回传入的媒体文件的编码格式，如wav、mp3、aac、flac、amr、3gp、 m4a、wma、ogg、ape等。
        :type Codecs: str
        :param Duration: 该字段用于返回对传入的流媒体文件进行分片的片段时长，单位为秒。**默认值为15秒**，支持用户自定义配置。
        :type Duration: int
        :param Width: *内测中，敬请期待*
        :type Width: int
        :param Height: *内测中，敬请期待*
        :type Height: int
        :param Thumbnail: *内测中，敬请期待*
        :type Thumbnail: str
        """
        self.Codecs = None
        self.Duration = None
        self.Width = None
        self.Height = None
        self.Thumbnail = None


    def _deserialize(self, params):
        self.Codecs = params.get("Codecs")
        self.Duration = params.get("Duration")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoanResult(AbstractModel):
    """呻吟低俗检测结果

    """

    def __init__(self):
        r"""
        :param Label: 固定取值为Moan（呻吟/娇喘），如音频中无复杂类型「MoanResult」的返回则代表改音频中无呻吟/娇喘相关违规内容；
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Moan 99，则该样本属于呻吟/娇喘的置信度非常高。）
        :type Score: int
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param StartTime: 违规事件开始时间，单位为毫秒（ms）；
        :type StartTime: float
        :param EndTime: 违规事件结束时间，单位为毫秒（ms）；
        :type EndTime: float
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        """
        self.Label = None
        self.Score = None
        self.Suggestion = None
        self.StartTime = None
        self.EndTime = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.Suggestion = params.get("Suggestion")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionResult(AbstractModel):
    """识别类标签结果信息

    """

    def __init__(self):
        r"""
        :param Label: 可能的取值有：Teenager 、Gender
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Tags: 识别标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.Label = None
        self.Tags = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """用于表示数据存储的相关信息

    """

    def __init__(self):
        r"""
        :param Type: 该字段表示文件访问类型，取值为**URL**（资源链接）和**COS** (腾讯云对象存储)；该字段应当与传入的访问类型相对应，可用于强校验并方便系统快速识别访问地址；若不传入此参数，则默认值为URL，此时系统将自动判定访问地址类型。
        :type Type: str
        :param Url: 该字段表示文件访问的链接地址，格式为标准URL格式。<br> 备注：当Type为URL时此字段不为空，该参数与BucketInfo参数须传入其中之一
        :type Url: str
        :param BucketInfo: 该字段表示文件访问的腾讯云存储桶信息。<br> 备注：当Type为COS时此字段不为空，该参数与Url参数须传入其中之一。
        :type BucketInfo: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
        """
        self.Type = None
        self.Url = None
        self.BucketInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self.BucketInfo = BucketInfo()
            self.BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """音频切片识别标签

    """

    def __init__(self):
        r"""
        :param Name: 根据Label字段确定具体名称：
当Label 为Teenager 时 Name可能取值有：Teenager 
当Label 为Gender 时 Name可能取值有：Male 、Female
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Score: 置信分：0～100，数值越大表示置信度越高
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param StartTime: 识别开始偏移时间，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param EndTime: 识别结束偏移时间，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        """
        self.Name = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskData(AbstractModel):
    """任务数据

    """

    def __init__(self):
        r"""
        :param DataId: 该字段用于返回音频审核任务数据所对应的数据ID，方便后续查询和管理审核任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param TaskId: 该字段用于返回音频审核任务所生成的任务ID，用于标识具体审核任务，方便后续查询和管理。
        :type TaskId: str
        :param Status: 该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
        :type Status: str
        :param Name: 该字段用于返回音频审核任务所对应的任务名称，方便后续查询和管理审核任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param BizType: 该字段用于返回调用音频审核接口时传入的BizType参数，方便数据的辨别和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param Type: 该字段用于返回调用音频审核接口时输入的音频审核类型，取值为：**AUDIO**（点播音频）和**LIVE_AUDIO**（直播音频），默认值为AUDIO。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param MediaInfo: 输入信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ams.v20201229.models.MediaInfo`
        :param Labels: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
        :type CreatedAt: str
        :param UpdatedAt: 该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self.DataId = None
        self.TaskId = None
        self.Status = None
        self.Name = None
        self.BizType = None
        self.Type = None
        self.Suggestion = None
        self.MediaInfo = None
        self.Labels = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Name = params.get("Name")
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        if params.get("MediaInfo") is not None:
            self.MediaInfo = MediaInfo()
            self.MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFilter(AbstractModel):
    """任务筛选器

    """

    def __init__(self):
        r"""
        :param BizType: 该字段用于传入任务对应的业务类型供筛选器进行筛选。Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与审核策略，调用前请确认正确的Biztype。Biztype仅为**数字、字母与下划线的组合**，长度为3-32个字符。<br>备注：在不传入该参数时筛选器默认不筛选业务类型。
        :type BizType: str
        :param Type: 该字段用于传入音频审核对应的任务类型供筛选器进行筛选，取值为：**VIDEO**（点播视频审核），**AUDIO**（点播音频审核）， **LIVE_VIDEO**（直播视频审核）, **LIVE_AUDIO**（直播音频审核）。<br>备注：在不传入该参数时筛选器默认不筛选任务类型。
        :type Type: str
        :param Suggestion: 该字段用于传入音频审核对应的建议操作供筛选器进行筛选，取值为：**Block**：建议屏蔽，**Review**：建议人工复审，**Pass**：建议通过。<br>备注：在不传入该参数时筛选器默认不筛选建议操作。
        :type Suggestion: str
        :param TaskStatus: 该字段用于传入审核任务的任务状态供筛选器进行筛选，取值为：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。<br>备注：在不传入该参数时筛选器默认不筛选任务状态。
        :type TaskStatus: str
        """
        self.BizType = None
        self.Type = None
        self.Suggestion = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """音视频任务数据结构

    """

    def __init__(self):
        r"""
        :param DataId: 选填参数，该字段表示您为待检测对象分配的数据ID，传入后可方便您对文件进行标识和管理。<br>取值：由英文字母（大小写均可）、数字及四个特殊符号（_，-，@，#）组成，**长度不超过64个字符**。
        :type DataId: str
        :param Name: 选填参数，该字段表示音频审核任务所对应的任务名称，方便后续查询和管理审核任务。
        :type Name: str
        :param Input: 必填参数，该字段表示审核文件的访问参数，用于获取审核媒体文件，该参数内包括访问类型和访问地址。
        :type Input: :class:`tencentcloud.ams.v20201229.models.StorageInfo`
        """
        self.DataId = None
        self.Name = None
        self.Input = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Name = params.get("Name")
        if params.get("Input") is not None:
            self.Input = StorageInfo()
            self.Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLabel(AbstractModel):
    """用于返回审核任务输出的标签

    """

    def __init__(self):
        r"""
        :param Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 该字段用于返回当前标签对应的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 该字段用于返回当前标签（Label）下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容；*色情 0*，则表明该文本不属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        """
        self.Label = None
        self.Suggestion = None
        self.Score = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """创建任务时的返回结果

    """

    def __init__(self):
        r"""
        :param DataId: 该字段用于返回创建音频审核任务时在TaskInput结构内传入的DataId，用于标识具体审核任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param TaskId: 该字段用于返回音频审核任务所生成的任务ID，用于标识具体审核任务，方便后续查询和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param Code: 该字段用于返回任务创建的状态，如返回OK则代表任务创建成功，其他返回值可参考公共错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Message: **仅在Code的返回值为错误码时生效**，用于返回错误的详情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.DataId = None
        self.TaskId = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextResult(AbstractModel):
    """音频文本内容审核结果

    """

    def __init__(self):
        r"""
        :param Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及其他令人反感、不安全或不适宜的内容类型。

如音频中无复杂类型「TextResults」的返回则代表改音频中无相关违规内容；
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Keywords: 命中的关键词，为空则代表该违规内容出自于模型的判断；
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param LibId: 命中关键词库的库标识；
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 命中关键词库的名字；
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Score: 机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Porn 99，则该样本属于色情的置信度非常高。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param LibType: 自定义词库的类型，自定义词库相关的信息可登录控制台中查看；

1：自定义黑白库；

2：自定义库；
        :type LibType: int
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        """
        self.Label = None
        self.Keywords = None
        self.LibId = None
        self.LibName = None
        self.Score = None
        self.Suggestion = None
        self.LibType = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Keywords = params.get("Keywords")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Score = params.get("Score")
        self.Suggestion = params.get("Suggestion")
        self.LibType = params.get("LibType")
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        