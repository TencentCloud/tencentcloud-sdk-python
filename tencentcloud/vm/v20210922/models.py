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
    """音频输出参数

    """

    def __init__(self):
        r"""
        :param _HitFlag: 该字段用于返回审核内容是否命中审核模型；取值：0（**未命中**）、1（**命中**）。
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Text: 该字段用于返回音频文件经ASR识别后的文本信息。最长可识别**5小时**的音频文件，若超出时长限制，接口将会报错。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Url: 该字段用于返回音频片段存储的链接地址，该地址有效期为1天。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Duration: 该字段用于返回音频文件的时长，单位为毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _Extra: 该字段用于返回输入参数中的额外附加信息（Extra），如未配置则默认返回值为空。<br>备注：不同客户或Biztype下返回信息不同，如需配置该字段请提交工单咨询或联系售后专员处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _TextResults: 该字段用于返回音频文件经ASR识别后产生的文本的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextResults: list of AudioResultDetailTextResult
        :param _MoanResults: 该字段用于返回音频文件呻吟检测的详细审核结果。具体结果内容请参见AudioResultDetailMoanResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type MoanResults: list of AudioResultDetailMoanResult
        :param _LanguageResults: 该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type LanguageResults: list of AudioResultDetailLanguageResult
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _RecognitionResults: 识别类标签结果信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognitionResults: list of RecognitionResult
        """
        self._HitFlag = None
        self._Label = None
        self._Suggestion = None
        self._Score = None
        self._Text = None
        self._Url = None
        self._Duration = None
        self._Extra = None
        self._TextResults = None
        self._MoanResults = None
        self._LanguageResults = None
        self._SubLabel = None
        self._RecognitionResults = None

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

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
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def TextResults(self):
        return self._TextResults

    @TextResults.setter
    def TextResults(self, TextResults):
        self._TextResults = TextResults

    @property
    def MoanResults(self):
        return self._MoanResults

    @MoanResults.setter
    def MoanResults(self, MoanResults):
        self._MoanResults = MoanResults

    @property
    def LanguageResults(self):
        return self._LanguageResults

    @LanguageResults.setter
    def LanguageResults(self, LanguageResults):
        self._LanguageResults = LanguageResults

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def RecognitionResults(self):
        return self._RecognitionResults

    @RecognitionResults.setter
    def RecognitionResults(self, RecognitionResults):
        self._RecognitionResults = RecognitionResults


    def _deserialize(self, params):
        self._HitFlag = params.get("HitFlag")
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Score = params.get("Score")
        self._Text = params.get("Text")
        self._Url = params.get("Url")
        self._Duration = params.get("Duration")
        self._Extra = params.get("Extra")
        if params.get("TextResults") is not None:
            self._TextResults = []
            for item in params.get("TextResults"):
                obj = AudioResultDetailTextResult()
                obj._deserialize(item)
                self._TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self._MoanResults = []
            for item in params.get("MoanResults"):
                obj = AudioResultDetailMoanResult()
                obj._deserialize(item)
                self._MoanResults.append(obj)
        if params.get("LanguageResults") is not None:
            self._LanguageResults = []
            for item in params.get("LanguageResults"):
                obj = AudioResultDetailLanguageResult()
                obj._deserialize(item)
                self._LanguageResults.append(obj)
        self._SubLabel = params.get("SubLabel")
        if params.get("RecognitionResults") is not None:
            self._RecognitionResults = []
            for item in params.get("RecognitionResults"):
                obj = RecognitionResult()
                obj._deserialize(item)
                self._RecognitionResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailLanguageResult(AbstractModel):
    """音频小语种检测结果

    """

    def __init__(self):
        r"""
        :param _Label: 语种
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        :param _SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self._Label = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None
        self._SubLabelCode = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubLabelCode(self):
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        self._SubLabelCode = SubLabelCode


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailMoanResult(AbstractModel):
    """音频呻吟审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回检测结果需要检测的内容类型，此处固定为**Moan**（呻吟）以调用呻吟检测功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Score: 该字段用于返回呻吟检测的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于呻吟内容。
        :type Score: int
        :param _StartTime: 该字段用于返回对应呻吟标签的片段在音频文件内的开始时间，单位为毫秒。
        :type StartTime: float
        :param _EndTime: 该字段用于返回对应呻吟标签的片段在音频文件内的结束时间，单位为毫秒。
        :type EndTime: float
        :param _SubLabelCode: *内测中，敬请期待*
        :type SubLabelCode: str
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
        :type SubLabel: str
        :param _Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        """
        self._Label = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None
        self._SubLabelCode = None
        self._SubLabel = None
        self._Suggestion = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubLabelCode(self):
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        self._SubLabelCode = SubLabelCode

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SubLabelCode = params.get("SubLabelCode")
        self._SubLabel = params.get("SubLabel")
        self._Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailTextResult(AbstractModel):
    """音频ASR文本审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Keywords: 该字段用于返回ASR识别出的文本内容命中的关键词信息，用于标注内容违规的具体原因（如：加我微信）。该参数可能会有多个返回值，代表命中的多个关键词；若返回值为空，Score不为空，则代表识别结果所对应的恶意标签（Label）来自于语义模型判断的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _LibId: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的ID，以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param _LibName: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的名称,以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _LibType: 该字段用于返回自定义关键词对应的词库类型，取值为**1**（黑白库）和**2**（自定义关键词库），若未配置自定义关键词库,则默认值为1（黑白库匹配）。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibType: int
        :param _Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        """
        self._Label = None
        self._Keywords = None
        self._LibId = None
        self._LibName = None
        self._Score = None
        self._LibType = None
        self._Suggestion = None
        self._SubLabel = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def LibType(self):
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Keywords = params.get("Keywords")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Score = params.get("Score")
        self._LibType = params.get("LibType")
        self._Suggestion = params.get("Suggestion")
        self._SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSegments(AbstractModel):
    """声音段信息

    """

    def __init__(self):
        r"""
        :param _OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetTime: str
        :param _Result: 结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.vm.v20210922.models.AudioResult`
        """
        self._OffsetTime = None
        self._Result = None

    @property
    def OffsetTime(self):
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self._Result = AudioResult()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BucketInfo(AbstractModel):
    """文件桶信息
    参考腾讯云存储相关说明 https://cloud.tencent.com/document/product/436/44352

    """

    def __init__(self):
        r"""
        :param _Bucket: 腾讯云对象存储，存储桶名称
        :type Bucket: str
        :param _Region: 地域
        :type Region: str
        :param _Object: 对象Key
        :type Object: str
        """
        self._Bucket = None
        self._Region = None
        self._Object = None

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateVideoModerationTaskRequest(AbstractModel):
    """CreateVideoModerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 该字段表示策略的具体编号，用于接口调度，在[内容安全控制台](https://console.cloud.tencent.com/cms/clouds/manage)中可配置。若不传入Biztype参数（留空），则代表采用默认的识别策略；传入则会在审核时根据业务场景采取不同的审核策略。
备注：Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。
        :type BizType: str
        :param _Type: 任务类型：可选VIDEO（点播视频），LIVE_VIDEO（直播视频）
        :type Type: str
        :param _Tasks: 输入的任务信息，最多可以同时创建10个任务
        :type Tasks: list of TaskInput
        :param _Seed: 验证签名参数，具体可以参考[验签说明](https://cloud.tencent.com/document/product/1265/104001#42dd87d2-580f-46cf-a953-639a787d1eda)。
        :type Seed: str
        :param _CallbackUrl: 接收审核信息回调地址。如果设置了该字段，在审核过程中发现违规音频片段和画面截帧结果将发送至该接口。更多详情请参阅[回调配置说明](https://cloud.tencent.com/document/product/1265/104001)。
        :type CallbackUrl: str
        :param _Priority: 审核排队优先级。当您有多个视频审核任务排队时，可以根据这个参数控制排队优先级。用于处理插队等逻辑。默认该参数为0
        :type Priority: int
        :param _User: 该字段表示待检测对象对应的用户相关信息，若填入则可甄别相应违规风险用户
        :type User: :class:`tencentcloud.vm.v20210922.models.User`
        """
        self._BizType = None
        self._Type = None
        self._Tasks = None
        self._Seed = None
        self._CallbackUrl = None
        self._Priority = None
        self._User = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Seed(self):
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._Type = params.get("Type")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Seed = params.get("Seed")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Priority = params.get("Priority")
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoModerationTaskResponse(AbstractModel):
    """CreateVideoModerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 任务创建结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，创建任务后返回的TaskId字段
        :type TaskId: str
        :param _ShowAllSegments: 是否展示所有分片，默认只展示命中规则的分片
        :type ShowAllSegments: bool
        """
        self._TaskId = None
        self._ShowAllSegments = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ShowAllSegments(self):
        return self._ShowAllSegments

    @ShowAllSegments.setter
    def ShowAllSegments(self, ShowAllSegments):
        self._ShowAllSegments = ShowAllSegments


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ShowAllSegments = params.get("ShowAllSegments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 该字段用于返回创建视频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _DataId: 该字段用于返回调用视频审核接口时传入的数据ID参数，方便数据的辨别和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _BizType: 该字段用于返回调用视频审核接口时传入的BizType参数，方便数据的辨别和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param _Name: 该字段用于返回调用视频审核接口时传入的TaskInput参数中的任务名称，方便任务的识别与管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: 该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Type: 该字段用于返回调用视频审核接口时输入的视频审核类型，取值为：**VIDEO**（点播视频）和**LIVE_VIDEO**（直播视频），默认值为VIDEO。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Labels: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param _MediaInfo: 该字段用于返回输入媒体文件的详细信息，包括编解码格式、分片时长等信息。详细内容敬请参考MediaInfo数据结构的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.vm.v20210922.models.MediaInfo`
        :param _InputInfo: 该字段用于返回审核服务的媒体内容信息，主要包括传入文件类型和访问地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.vm.v20210922.models.InputInfo`
        :param _CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _TryInSeconds: 在秒后重试
注意：此字段可能返回 null，表示取不到有效值。
        :type TryInSeconds: int
        :param _ImageSegments: 该字段用于返回视频中截帧审核的结果，详细返回内容敬请参考ImageSegments数据结构的描述。<br>备注：数据有效期为24小时，如需要延长存储时间，请在已配置的COS储存桶中设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSegments: list of ImageSegments
        :param _AudioSegments: 该字段用于返回视频中音频审核的结果，详细返回内容敬请参考AudioSegments数据结构的描述。<br>备注：数据有效期为24小时，如需要延长存储时间，请在已配置的COS储存桶中设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSegments: list of AudioSegments
        :param _ErrorType: 当任务状态为Error时，返回对应错误的类型，取值：
**DECODE_ERROR**: 解码失败。（输入资源中可能包含无法解码的视频）
**URL_ERROR**：下载地址验证失败。
**TIMEOUT_ERROR**：处理超时。
**CALLBACK_ERRORR**：回调错误。
**MODERATION_ERROR**：审核失败。
**URL_NOT_SUPPORTED**：源文件太大或没有图片音频帧
任务状态非Error时默认返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorType: str
        :param _ErrorDescription: 当任务状态为Error时，该字段用于返回对应错误的详细描述，任务状态非Error时默认返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDescription: str
        :param _Label: 该字段用于返回检测结果所对应的标签。如果未命中恶意，返回Normal，如果命中恶意，则返回Labels中优先级最高的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _AudioText: 该字段用于返回音频文件识别出的对应文本内容，最大支持**前1000个字符**。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioText: str
        :param _Asrs: 该字段用于返回音频文件识别出的对应文本内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Asrs: list of RcbAsr
        :param _SegmentCosUrlList: 该字段用于返回检测结果明细数据相关的cos url	
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentCosUrlList: :class:`tencentcloud.vm.v20210922.models.SegmentCosUrlList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._DataId = None
        self._BizType = None
        self._Name = None
        self._Status = None
        self._Type = None
        self._Suggestion = None
        self._Labels = None
        self._MediaInfo = None
        self._InputInfo = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._TryInSeconds = None
        self._ImageSegments = None
        self._AudioSegments = None
        self._ErrorType = None
        self._ErrorDescription = None
        self._Label = None
        self._AudioText = None
        self._Asrs = None
        self._SegmentCosUrlList = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def MediaInfo(self):
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

    @property
    def InputInfo(self):
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def TryInSeconds(self):
        return self._TryInSeconds

    @TryInSeconds.setter
    def TryInSeconds(self, TryInSeconds):
        self._TryInSeconds = TryInSeconds

    @property
    def ImageSegments(self):
        return self._ImageSegments

    @ImageSegments.setter
    def ImageSegments(self, ImageSegments):
        self._ImageSegments = ImageSegments

    @property
    def AudioSegments(self):
        return self._AudioSegments

    @AudioSegments.setter
    def AudioSegments(self, AudioSegments):
        self._AudioSegments = AudioSegments

    @property
    def ErrorType(self):
        return self._ErrorType

    @ErrorType.setter
    def ErrorType(self, ErrorType):
        self._ErrorType = ErrorType

    @property
    def ErrorDescription(self):
        return self._ErrorDescription

    @ErrorDescription.setter
    def ErrorDescription(self, ErrorDescription):
        self._ErrorDescription = ErrorDescription

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def AudioText(self):
        return self._AudioText

    @AudioText.setter
    def AudioText(self, AudioText):
        self._AudioText = AudioText

    @property
    def Asrs(self):
        return self._Asrs

    @Asrs.setter
    def Asrs(self, Asrs):
        self._Asrs = Asrs

    @property
    def SegmentCosUrlList(self):
        return self._SegmentCosUrlList

    @SegmentCosUrlList.setter
    def SegmentCosUrlList(self, SegmentCosUrlList):
        self._SegmentCosUrlList = SegmentCosUrlList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DataId = params.get("DataId")
        self._BizType = params.get("BizType")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Suggestion = params.get("Suggestion")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("MediaInfo") is not None:
            self._MediaInfo = MediaInfo()
            self._MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("InputInfo") is not None:
            self._InputInfo = InputInfo()
            self._InputInfo._deserialize(params.get("InputInfo"))
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._TryInSeconds = params.get("TryInSeconds")
        if params.get("ImageSegments") is not None:
            self._ImageSegments = []
            for item in params.get("ImageSegments"):
                obj = ImageSegments()
                obj._deserialize(item)
                self._ImageSegments.append(obj)
        if params.get("AudioSegments") is not None:
            self._AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self._AudioSegments.append(obj)
        self._ErrorType = params.get("ErrorType")
        self._ErrorDescription = params.get("ErrorDescription")
        self._Label = params.get("Label")
        self._AudioText = params.get("AudioText")
        if params.get("Asrs") is not None:
            self._Asrs = []
            for item in params.get("Asrs"):
                obj = RcbAsr()
                obj._deserialize(item)
                self._Asrs.append(obj)
        if params.get("SegmentCosUrlList") is not None:
            self._SegmentCosUrlList = SegmentCosUrlList()
            self._SegmentCosUrlList._deserialize(params.get("SegmentCosUrlList"))
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 该参数表示任务列表每页展示的任务条数，**默认值为10**（每页展示10条任务）。
        :type Limit: int
        :param _Filter: 该参数表示任务筛选器的输入参数，可根据业务类型、审核文件类型、处理建议及任务状态筛选想要查看的审核任务，具体参数内容请参见TaskFilter数据结构的详细描述。
        :type Filter: :class:`tencentcloud.vm.v20210922.models.TaskFilter`
        :param _PageToken: 该参数表示翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
        :type PageToken: str
        :param _StartTime: 该参数表示任务列表的开始时间，格式为ISO8601标准的时间戳。**默认值为最近3天**，若传入该参数，则在这一时间到EndTime之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :type StartTime: str
        :param _EndTime: 该参数表示任务列表的结束时间，格式为ISO8601标准的时间戳。**默认值为空**，若传入该参数，则在这StartTime到这一时间之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :type EndTime: str
        """
        self._Limit = None
        self._Filter = None
        self._PageToken = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def PageToken(self):
        return self._PageToken

    @PageToken.setter
    def PageToken(self, PageToken):
        self._PageToken = PageToken

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self._Filter = TaskFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._PageToken = params.get("PageToken")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 该字段用于返回当前查询的任务总量，格式为int字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param _Data: 该字段用于返回当前页的任务详细数据，具体输出内容请参见TaskData数据结构的详细描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskData
        :param _PageToken: 该字段用于返回翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._PageToken = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def PageToken(self):
        return self._PageToken

    @PageToken.setter
    def PageToken(self, PageToken):
        self._PageToken = PageToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._PageToken = params.get("PageToken")
        self._RequestId = params.get("RequestId")


class ImageResult(AbstractModel):
    """Result结果详情

    """

    def __init__(self):
        r"""
        :param _HitFlag: 违规标志
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Label: 命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Results: 画面截帧图片结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of ImageResultResult
        :param _Url: 图片URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Extra: 附加字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        """
        self._HitFlag = None
        self._Label = None
        self._Suggestion = None
        self._Score = None
        self._Results = None
        self._Url = None
        self._Extra = None

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

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
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._HitFlag = params.get("HitFlag")
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Score = params.get("Score")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ImageResultResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._Url = params.get("Url")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultResult(AbstractModel):
    """图片输出结果的子结果

    """

    def __init__(self):
        r"""
        :param _Scene: 场景
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Scene: str
        :param _HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param _Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _SubLabel: 子标签
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _Score: 分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Names: 人物名称列表，如未识别，则为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Names: list of str
        :param _Text: 图片OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Details: 其他详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of ImageResultsResultDetail
        """
        self._Scene = None
        self._HitFlag = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Names = None
        self._Text = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

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
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._HitFlag = params.get("HitFlag")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        self._Names = params.get("Names")
        self._Text = params.get("Text")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ImageResultsResultDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetail(AbstractModel):
    """具体场景下的图片识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Text: OCR识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Location: 位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: :class:`tencentcloud.vm.v20210922.models.ImageResultsResultDetailLocation`
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _LibId: 库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param _LibName: 库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _Keywords: 命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _Suggestion: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self._Name = None
        self._Text = None
        self._Location = None
        self._Label = None
        self._LibId = None
        self._LibName = None
        self._Keywords = None
        self._Suggestion = None
        self._Score = None
        self._SubLabelCode = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def SubLabelCode(self):
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        self._SubLabelCode = SubLabelCode


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Text = params.get("Text")
        if params.get("Location") is not None:
            self._Location = ImageResultsResultDetailLocation()
            self._Location._deserialize(params.get("Location"))
        self._Label = params.get("Label")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Keywords = params.get("Keywords")
        self._Suggestion = params.get("Suggestion")
        self._Score = params.get("Score")
        self._SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetailLocation(AbstractModel):
    """图片详情位置信息

    """

    def __init__(self):
        r"""
        :param _X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param _Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        :param _Width: 宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Rotate: 旋转角度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: float
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._Rotate = None

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

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Rotate = params.get("Rotate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSegments(AbstractModel):
    """图片段信息

    """

    def __init__(self):
        r"""
        :param _OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
        :type OffsetTime: str
        :param _Result: 画面截帧结果详情
        :type Result: :class:`tencentcloud.vm.v20210922.models.ImageResult`
        """
        self._OffsetTime = None
        self._Result = None

    @property
    def OffsetTime(self):
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self._Result = ImageResult()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """输入信息详情

    """

    def __init__(self):
        r"""
        :param _Type: 传入的类型可选：URL，COS
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Url: Url地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _BucketInfo: 桶信息。当输入当时COS时，该字段不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketInfo: str
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        return self._BucketInfo

    @BucketInfo.setter
    def BucketInfo(self, BucketInfo):
        self._BucketInfo = BucketInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._BucketInfo = params.get("BucketInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    """媒体类型

    """

    def __init__(self):
        r"""
        :param _Codecs: 编码格式
        :type Codecs: str
        :param _Duration: 流检测时分片时长
注意：此字段可能返回 0，表示取不到有效值。
        :type Duration: int
        :param _Width: 宽，单位为像素
        :type Width: int
        :param _Height: 高，单位为像素
        :type Height: int
        :param _Thumbnail: 封面
        :type Thumbnail: str
        """
        self._Codecs = None
        self._Duration = None
        self._Width = None
        self._Height = None
        self._Thumbnail = None

    @property
    def Codecs(self):
        return self._Codecs

    @Codecs.setter
    def Codecs(self, Codecs):
        self._Codecs = Codecs

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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

    @property
    def Thumbnail(self):
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail


    def _deserialize(self, params):
        self._Codecs = params.get("Codecs")
        self._Duration = params.get("Duration")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RcbAsr(AbstractModel):
    """审核切片asr文本信息

    """

    def __init__(self):
        r"""
        :param _Text: 该字段用于返回音频文件识别出的对应文本内容，最大支持**前1000个字符**。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        """
        self._Text = None
        self._CreatedAt = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionResult(AbstractModel):
    """识别类标签结果信息

    """

    def __init__(self):
        r"""
        :param _Label: 可能的取值有：Teenager 、Gender
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Tags: 识别标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._Label = None
        self._Tags = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Label = params.get("Label")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentCosUrlList(AbstractModel):
    """明细数据相关的cos url

    """

    def __init__(self):
        r"""
        :param _ImageAllUrl: 全量图片片段的cos url
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageAllUrl: str
        :param _AudioAllUrl: 全量音频片段的cos url
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioAllUrl: str
        :param _ImageBlockUrl: 违规图片片段的cos url
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageBlockUrl: str
        :param _AudioBlockUrl: 违规音频片段的cos url
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioBlockUrl: str
        :param _AsrUrl: 全量音频识别文本的cos url
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrUrl: str
        """
        self._ImageAllUrl = None
        self._AudioAllUrl = None
        self._ImageBlockUrl = None
        self._AudioBlockUrl = None
        self._AsrUrl = None

    @property
    def ImageAllUrl(self):
        return self._ImageAllUrl

    @ImageAllUrl.setter
    def ImageAllUrl(self, ImageAllUrl):
        self._ImageAllUrl = ImageAllUrl

    @property
    def AudioAllUrl(self):
        return self._AudioAllUrl

    @AudioAllUrl.setter
    def AudioAllUrl(self, AudioAllUrl):
        self._AudioAllUrl = AudioAllUrl

    @property
    def ImageBlockUrl(self):
        return self._ImageBlockUrl

    @ImageBlockUrl.setter
    def ImageBlockUrl(self, ImageBlockUrl):
        self._ImageBlockUrl = ImageBlockUrl

    @property
    def AudioBlockUrl(self):
        return self._AudioBlockUrl

    @AudioBlockUrl.setter
    def AudioBlockUrl(self, AudioBlockUrl):
        self._AudioBlockUrl = AudioBlockUrl

    @property
    def AsrUrl(self):
        return self._AsrUrl

    @AsrUrl.setter
    def AsrUrl(self, AsrUrl):
        self._AsrUrl = AsrUrl


    def _deserialize(self, params):
        self._ImageAllUrl = params.get("ImageAllUrl")
        self._AudioAllUrl = params.get("AudioAllUrl")
        self._ImageBlockUrl = params.get("ImageBlockUrl")
        self._AudioBlockUrl = params.get("AudioBlockUrl")
        self._AsrUrl = params.get("AsrUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """数据存储信息

    """

    def __init__(self):
        r"""
        :param _Type: 类型 可选：
URL 资源链接类型
COS 腾讯云对象存储类型
        :type Type: str
        :param _Url: 资源链接
        :type Url: str
        :param _BucketInfo: 腾讯云存储桶信息
        :type BucketInfo: :class:`tencentcloud.vm.v20210922.models.BucketInfo`
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        return self._BucketInfo

    @BucketInfo.setter
    def BucketInfo(self, BucketInfo):
        self._BucketInfo = BucketInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self._BucketInfo = BucketInfo()
            self._BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """音频切片识别标签

    """

    def __init__(self):
        r"""
        :param _Name: 根据Label字段确定具体名称：
当Label 为Teenager 时 Name可能取值有：Teenager 
当Label 为Gender 时 Name可能取值有：Male 、Female
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Score: 置信分：0～100，数值越大表示置信度越高
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _StartTime: 识别开始偏移时间，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param _EndTime: 识别结束偏移时间，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        """
        self._Name = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskData(AbstractModel):
    """任务数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _DataId: 输入的数据ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _BizType: 业务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param _Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: 状态，可选：PENDING，RUNNING，ERROR，FINISH，CANCELLED
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Suggestion: 处理建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Labels: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param _MediaInfo: 媒体信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.vm.v20210922.models.MediaInfo`
        :param _InputInfo: 输入信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.vm.v20210922.models.InputInfo`
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self._TaskId = None
        self._DataId = None
        self._BizType = None
        self._Name = None
        self._Status = None
        self._Type = None
        self._Suggestion = None
        self._Labels = None
        self._MediaInfo = None
        self._InputInfo = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def MediaInfo(self):
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

    @property
    def InputInfo(self):
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._DataId = params.get("DataId")
        self._BizType = params.get("BizType")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Suggestion = params.get("Suggestion")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("MediaInfo") is not None:
            self._MediaInfo = MediaInfo()
            self._MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("InputInfo") is not None:
            self._InputInfo = InputInfo()
            self._InputInfo._deserialize(params.get("InputInfo"))
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFilter(AbstractModel):
    """Cos TaskFilter

    """

    def __init__(self):
        r"""
        :param _BizType: 任务业务类型
        :type BizType: str
        :param _Type: 任务类型，可选：VIDEO，AUDIO， LIVE_VIDEO, LIVE_AUDIO
        :type Type: str
        :param _Suggestion: 建议，可选：Pass, Review,Block
        :type Suggestion: str
        :param _TaskStatus: 状态，可选：PENDING，RUNNING，ERROR，FINISH，CANCELLED
        :type TaskStatus: str
        """
        self._BizType = None
        self._Type = None
        self._Suggestion = None
        self._TaskStatus = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._Type = params.get("Type")
        self._Suggestion = params.get("Suggestion")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """音视频任务结构

    """

    def __init__(self):
        r"""
        :param _DataId: 数据ID
        :type DataId: str
        :param _Name: 任务名
        :type Name: str
        :param _Input: 任务输入
        :type Input: :class:`tencentcloud.vm.v20210922.models.StorageInfo`
        """
        self._DataId = None
        self._Name = None
        self._Input = None

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._Name = params.get("Name")
        if params.get("Input") is not None:
            self._Input = StorageInfo()
            self._Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLabel(AbstractModel):
    """任务输出标签

    """

    def __init__(self):
        r"""
        :param _Label: 命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Score: 得分，分数是 0 ～ 100
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _SubLabel: 命中的二级标签
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        """
        self._Label = None
        self._Suggestion = None
        self._Score = None
        self._SubLabel = None

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
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Score = params.get("Score")
        self._SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """创建任务时的返回结果

    """

    def __init__(self):
        r"""
        :param _DataId: 请求时传入的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param _TaskId: TaskId，任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Code: 错误码。如果code为OK，则表示创建成功，其他则参考公共错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Message: 如果错误，该字段表示错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._DataId = None
        self._TaskId = None
        self._Code = None
        self._Message = None

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._TaskId = params.get("TaskId")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 业务用户ID 如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param _AccountType: 该字段表示业务用户ID对应的账号类型，取值：1-微信uin，2-QQ号，3-微信群uin，4-qq群号，5-微信openid，6-QQopenid，7-其它string。
该字段与账号ID参数（UserId）配合使用可确定唯一账号。
        :type AccountType: str
        :param _Nickname: 用户昵称
        :type Nickname: str
        :param _Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param _Age: 年龄 默认0 未知
        :type Age: int
        :param _Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param _Phone: 手机号
        :type Phone: str
        :param _Desc: 用户简介，长度不超过5000字
        :type Desc: str
        :param _HeadUrl: 用户头像图片链接
        :type HeadUrl: str
        :param _RoomId: 群聊场景房间ID
        :type RoomId: str
        :param _GroupId: 群聊场景群ID
        :type GroupId: str
        :param _GroupSize: 群聊场景群用户数
        :type GroupSize: int
        :param _ReceiverId: 消息接收者ID
        :type ReceiverId: str
        :param _SendTime: 消息生成时间，毫秒
        :type SendTime: str
        """
        self._UserId = None
        self._AccountType = None
        self._Nickname = None
        self._Gender = None
        self._Age = None
        self._Level = None
        self._Phone = None
        self._Desc = None
        self._HeadUrl = None
        self._RoomId = None
        self._GroupId = None
        self._GroupSize = None
        self._ReceiverId = None
        self._SendTime = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def HeadUrl(self):
        return self._HeadUrl

    @HeadUrl.setter
    def HeadUrl(self, HeadUrl):
        self._HeadUrl = HeadUrl

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupSize(self):
        return self._GroupSize

    @GroupSize.setter
    def GroupSize(self, GroupSize):
        self._GroupSize = GroupSize

    @property
    def ReceiverId(self):
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def SendTime(self):
        return self._SendTime

    @SendTime.setter
    def SendTime(self, SendTime):
        self._SendTime = SendTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._AccountType = params.get("AccountType")
        self._Nickname = params.get("Nickname")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Level = params.get("Level")
        self._Phone = params.get("Phone")
        self._Desc = params.get("Desc")
        self._HeadUrl = params.get("HeadUrl")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._GroupSize = params.get("GroupSize")
        self._ReceiverId = params.get("ReceiverId")
        self._SendTime = params.get("SendTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        