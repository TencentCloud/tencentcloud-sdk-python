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


class AudioResult(AbstractModel):
    r"""音频审核输出参数

    """

    def __init__(self):
        r"""
        :param _HitFlag: 该字段用于返回审核内容是否命中审核模型；取值：0（**未命中**）、1（**命中**）。
        :type HitFlag: int
        :param _Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        :param _Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
        :type Score: int
        :param _Text: 该字段用于返回音频文件经ASR识别后的文本信息。最长可识别**5小时**的音频文件，若超出时长限制，接口将会报错。
        :type Text: str
        :param _Url: 该字段用于返回审核结果的访问链接（URL）。<br>备注：链接默认有效期为12小时。如果您需要更长时效的链接，请使用[COS预签名](https://cloud.tencent.com/document/product/1265/104001)功能更新签名时效。
        :type Url: str
        :param _Duration: 该字段用于返回音频文件的时长，单位为毫秒。
        :type Duration: str
        :param _Extra: 该字段用于返回额外附加信息，不同客户或Biztype下返回信息不同。
        :type Extra: str
        :param _TextResults: 该字段用于返回音频文件经ASR识别后产生的文本的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
        :type TextResults: list of AudioResultDetailTextResult
        :param _MoanResults: 该字段用于返回音频文件呻吟检测的详细审核结果。具体结果内容请参见AudioResultDetailMoanResult数据结构的细节描述。
        :type MoanResults: list of AudioResultDetailMoanResult
        :param _LanguageResults: 该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
        :type LanguageResults: list of AudioResultDetailLanguageResult
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
        :type SubLabel: str
        :param _RecognitionResults: 识别类标签结果信息列表
        :type RecognitionResults: list of RecognitionResult
        :param _SpeakerResults: 说话人结果
        :type SpeakerResults: list of SpeakerResults
        :param _LabelResults: 歌曲识别结果
        :type LabelResults: list of LabelResults
        :param _TravelResults: 出行结果
        :type TravelResults: list of TravelResults
        :param _SubTag: 三级标签
        :type SubTag: str
        :param _SubTagCode: 三级标签码
        :type SubTagCode: str
        :param _HitType: 审核检测类型
        :type HitType: str
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
        self._SpeakerResults = None
        self._LabelResults = None
        self._TravelResults = None
        self._SubTag = None
        self._SubTagCode = None
        self._HitType = None

    @property
    def HitFlag(self):
        r"""该字段用于返回审核内容是否命中审核模型；取值：0（**未命中**）、1（**命中**）。
        :rtype: int
        """
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Label(self):
        r"""该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        r"""该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        r"""该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Text(self):
        r"""该字段用于返回音频文件经ASR识别后的文本信息。最长可识别**5小时**的音频文件，若超出时长限制，接口将会报错。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Url(self):
        r"""该字段用于返回审核结果的访问链接（URL）。<br>备注：链接默认有效期为12小时。如果您需要更长时效的链接，请使用[COS预签名](https://cloud.tencent.com/document/product/1265/104001)功能更新签名时效。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Duration(self):
        r"""该字段用于返回音频文件的时长，单位为毫秒。
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Extra(self):
        r"""该字段用于返回额外附加信息，不同客户或Biztype下返回信息不同。
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def TextResults(self):
        r"""该字段用于返回音频文件经ASR识别后产生的文本的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
        :rtype: list of AudioResultDetailTextResult
        """
        return self._TextResults

    @TextResults.setter
    def TextResults(self, TextResults):
        self._TextResults = TextResults

    @property
    def MoanResults(self):
        r"""该字段用于返回音频文件呻吟检测的详细审核结果。具体结果内容请参见AudioResultDetailMoanResult数据结构的细节描述。
        :rtype: list of AudioResultDetailMoanResult
        """
        return self._MoanResults

    @MoanResults.setter
    def MoanResults(self, MoanResults):
        self._MoanResults = MoanResults

    @property
    def LanguageResults(self):
        r"""该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
        :rtype: list of AudioResultDetailLanguageResult
        """
        return self._LanguageResults

    @LanguageResults.setter
    def LanguageResults(self, LanguageResults):
        self._LanguageResults = LanguageResults

    @property
    def SubLabel(self):
        r"""该字段用于返回当前标签（Lable）下的二级标签。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def RecognitionResults(self):
        r"""识别类标签结果信息列表
        :rtype: list of RecognitionResult
        """
        return self._RecognitionResults

    @RecognitionResults.setter
    def RecognitionResults(self, RecognitionResults):
        self._RecognitionResults = RecognitionResults

    @property
    def SpeakerResults(self):
        r"""说话人结果
        :rtype: list of SpeakerResults
        """
        return self._SpeakerResults

    @SpeakerResults.setter
    def SpeakerResults(self, SpeakerResults):
        self._SpeakerResults = SpeakerResults

    @property
    def LabelResults(self):
        r"""歌曲识别结果
        :rtype: list of LabelResults
        """
        return self._LabelResults

    @LabelResults.setter
    def LabelResults(self, LabelResults):
        self._LabelResults = LabelResults

    @property
    def TravelResults(self):
        r"""出行结果
        :rtype: list of TravelResults
        """
        return self._TravelResults

    @TravelResults.setter
    def TravelResults(self, TravelResults):
        self._TravelResults = TravelResults

    @property
    def SubTag(self):
        r"""三级标签
        :rtype: str
        """
        return self._SubTag

    @SubTag.setter
    def SubTag(self, SubTag):
        self._SubTag = SubTag

    @property
    def SubTagCode(self):
        r"""三级标签码
        :rtype: str
        """
        return self._SubTagCode

    @SubTagCode.setter
    def SubTagCode(self, SubTagCode):
        self._SubTagCode = SubTagCode

    @property
    def HitType(self):
        r"""审核检测类型
        :rtype: str
        """
        return self._HitType

    @HitType.setter
    def HitType(self, HitType):
        self._HitType = HitType


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
        if params.get("SpeakerResults") is not None:
            self._SpeakerResults = []
            for item in params.get("SpeakerResults"):
                obj = SpeakerResults()
                obj._deserialize(item)
                self._SpeakerResults.append(obj)
        if params.get("LabelResults") is not None:
            self._LabelResults = []
            for item in params.get("LabelResults"):
                obj = LabelResults()
                obj._deserialize(item)
                self._LabelResults.append(obj)
        if params.get("TravelResults") is not None:
            self._TravelResults = []
            for item in params.get("TravelResults"):
                obj = TravelResults()
                obj._deserialize(item)
                self._TravelResults.append(obj)
        self._SubTag = params.get("SubTag")
        self._SubTagCode = params.get("SubTagCode")
        self._HitType = params.get("HitType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailLanguageResult(AbstractModel):
    r"""音频语言种类检测结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回对应的语言种类信息。
        :type Label: str
        :param _Score: 该参数用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于当前返回的语种标签；
        :type Score: int
        :param _StartTime: 该参数用于返回对应语种标签的片段在音频文件内的开始时间，单位为秒。
        :type StartTime: float
        :param _EndTime: 该参数用于返回对应语种标签的片段在音频文件内的结束时间，单位为秒。
        :type EndTime: float
        :param _SubLabelCode: *内测中，敬请期待*
        :type SubLabelCode: str
        """
        self._Label = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None
        self._SubLabelCode = None

    @property
    def Label(self):
        r"""该字段用于返回对应的语言种类信息。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        r"""该参数用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于当前返回的语种标签；
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""该参数用于返回对应语种标签的片段在音频文件内的开始时间，单位为秒。
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""该参数用于返回对应语种标签的片段在音频文件内的结束时间，单位为秒。
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubLabelCode(self):
        r"""*内测中，敬请期待*
        :rtype: str
        """
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
    r"""音频呻吟审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回检测结果需要检测的内容类型，此处固定为**Moan**（呻吟）以调用呻吟检测功能。
        :type Label: str
        :param _Score: 该字段用于返回呻吟检测的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于呻吟内容。
        :type Score: int
        :param _StartTime: 该字段用于返回对应呻吟标签的片段在音频文件内的开始时间，单位为秒。
        :type StartTime: float
        :param _EndTime: 该字段用于返回对应呻吟标签的片段在音频文件内的结束时间，单位为秒。
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
        r"""该字段用于返回检测结果需要检测的内容类型，此处固定为**Moan**（呻吟）以调用呻吟检测功能。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        r"""该字段用于返回呻吟检测的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于呻吟内容。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""该字段用于返回对应呻吟标签的片段在音频文件内的开始时间，单位为秒。
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""该字段用于返回对应呻吟标签的片段在音频文件内的结束时间，单位为秒。
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubLabelCode(self):
        warnings.warn("parameter `SubLabelCode` is deprecated", DeprecationWarning) 

        r"""*内测中，敬请期待*
        :rtype: str
        """
        return self._SubLabelCode

    @SubLabelCode.setter
    def SubLabelCode(self, SubLabelCode):
        warnings.warn("parameter `SubLabelCode` is deprecated", DeprecationWarning) 

        self._SubLabelCode = SubLabelCode

    @property
    def SubLabel(self):
        r"""该字段用于返回当前标签（Lable）下的二级标签。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Suggestion(self):
        r"""该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :rtype: str
        """
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
        


class AudioResultDetailSpeakerResult(AbstractModel):
    r"""音频说话人声纹识别返回结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回检测结果需要检测的内容类型。
        :type Label: str
        :param _Score: 该字段用于返回呻吟检测的置信度，取值范围：0（置信度最低）-100（置信度最高），越高代表音频越有可能属于说话人声纹。
        :type Score: int
        :param _StartTime: 该字段用于返回对应说话人的片段在音频文件内的开始时间，单位为秒。
        :type StartTime: float
        :param _EndTime: 该字段用于返回对应说话人的片段在音频文件内的结束时间，单位为秒。
        :type EndTime: float
        """
        self._Label = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Label(self):
        r"""该字段用于返回检测结果需要检测的内容类型。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        r"""该字段用于返回呻吟检测的置信度，取值范围：0（置信度最低）-100（置信度最高），越高代表音频越有可能属于说话人声纹。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""该字段用于返回对应说话人的片段在音频文件内的开始时间，单位为秒。
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""该字段用于返回对应说话人的片段在音频文件内的结束时间，单位为秒。
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Label = params.get("Label")
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
        


class AudioResultDetailTextResult(AbstractModel):
    r"""音频ASR文本审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _Keywords: 该字段用于返回ASR识别出的文本内容命中的关键词信息，用于标注内容违规的具体原因（如：加我微信）。该参数可能会有多个返回值，代表命中的多个关键词；若返回值为空，Score不为空，则代表识别结果所对应的恶意标签（Label）来自于语义模型判断的返回值。
        :type Keywords: list of str
        :param _LibId: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的ID，以方便自定义库管理和配置。
        :type LibId: str
        :param _LibName: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的名称,以方便自定义库管理和配置。
        :type LibName: str
        :param _Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
        :type Score: int
        :param _Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        :param _LibType: 该字段用于返回自定义关键词对应的词库类型，取值为**1**（黑白库）和**2**（自定义关键词库），若未配置自定义关键词库,则默认值为1（黑白库匹配）。
        :type LibType: int
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
        :type SubLabel: str
        :param _HitInfos: 该字段用于命中的关键词信息
        :type HitInfos: list of HitInfo
        """
        self._Label = None
        self._Keywords = None
        self._LibId = None
        self._LibName = None
        self._Score = None
        self._Suggestion = None
        self._LibType = None
        self._SubLabel = None
        self._HitInfos = None

    @property
    def Label(self):
        r"""该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Keywords(self):
        r"""该字段用于返回ASR识别出的文本内容命中的关键词信息，用于标注内容违规的具体原因（如：加我微信）。该参数可能会有多个返回值，代表命中的多个关键词；若返回值为空，Score不为空，则代表识别结果所对应的恶意标签（Label）来自于语义模型判断的返回值。
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def LibId(self):
        r"""该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的ID，以方便自定义库管理和配置。
        :rtype: str
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        r"""该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的名称,以方便自定义库管理和配置。
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Score(self):
        r"""该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Suggestion(self):
        r"""该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def LibType(self):
        r"""该字段用于返回自定义关键词对应的词库类型，取值为**1**（黑白库）和**2**（自定义关键词库），若未配置自定义关键词库,则默认值为1（黑白库匹配）。
        :rtype: int
        """
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType

    @property
    def SubLabel(self):
        r"""该字段用于返回当前标签（Lable）下的二级标签。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def HitInfos(self):
        r"""该字段用于命中的关键词信息
        :rtype: list of HitInfo
        """
        return self._HitInfos

    @HitInfos.setter
    def HitInfos(self, HitInfos):
        self._HitInfos = HitInfos


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Keywords = params.get("Keywords")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Score = params.get("Score")
        self._Suggestion = params.get("Suggestion")
        self._LibType = params.get("LibType")
        self._SubLabel = params.get("SubLabel")
        if params.get("HitInfos") is not None:
            self._HitInfos = []
            for item in params.get("HitInfos"):
                obj = HitInfo()
                obj._deserialize(item)
                self._HitInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSegments(AbstractModel):
    r"""表示该段声音的信息

    """

    def __init__(self):
        r"""
        :param _OffsetTime: 该字段用于返回音频片段的开始时间，单位为秒。对于点播文件，该参数代表对应音频相对于完整音轨的偏移时间，如0（代表不偏移），5（音轨开始后5秒），10（音轨开始后10秒）；对于直播文件，该参数则返回对应音频片段开始时的Unix时间戳，如：1594650717。
        :type OffsetTime: str
        :param _Result: 该字段用于返回音频片段的具体审核结果，详细内容敬请参考AudioResult数据结构的描述。
        :type Result: :class:`tencentcloud.ams.v20201229.models.AudioResult`
        :param _CreatedAt: 入库时间
        :type CreatedAt: str
        """
        self._OffsetTime = None
        self._Result = None
        self._CreatedAt = None

    @property
    def OffsetTime(self):
        r"""该字段用于返回音频片段的开始时间，单位为秒。对于点播文件，该参数代表对应音频相对于完整音轨的偏移时间，如0（代表不偏移），5（音轨开始后5秒），10（音轨开始后10秒）；对于直播文件，该参数则返回对应音频片段开始时的Unix时间戳，如：1594650717。
        :rtype: str
        """
        return self._OffsetTime

    @OffsetTime.setter
    def OffsetTime(self, OffsetTime):
        self._OffsetTime = OffsetTime

    @property
    def Result(self):
        r"""该字段用于返回音频片段的具体审核结果，详细内容敬请参考AudioResult数据结构的描述。
        :rtype: :class:`tencentcloud.ams.v20201229.models.AudioResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def CreatedAt(self):
        r"""入库时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self._Result = AudioResult()
            self._Result._deserialize(params.get("Result"))
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BucketInfo(AbstractModel):
    r"""文件桶信息
    参考腾讯云存储相关说明 https://cloud.tencent.com/document/product/436/44352

    """

    def __init__(self):
        r"""
        :param _Bucket: 该字段用于标识腾讯云对象存储的存储桶名称,关于文件桶的详细信息敬请参考 [腾讯云存储相关说明](https://cloud.tencent.com/document/product/436/44352)。
        :type Bucket: str
        :param _Region: 该字段用于标识腾讯云对象存储的托管机房的分布地区，对象存储 COS 的数据存放在这些地域的存储桶中。
        :type Region: str
        :param _Object: 该字段用于标识腾讯云对象存储的对象Key,对象作为基本单元被存放在存储桶中；用户可以通过腾讯云控制台、API、SDK 等多种方式管理对象。有关对象的详细描述敬请参阅相应 [产品文档](https://cloud.tencent.com/document/product/436/13324)。
        :type Object: str
        """
        self._Bucket = None
        self._Region = None
        self._Object = None

    @property
    def Bucket(self):
        r"""该字段用于标识腾讯云对象存储的存储桶名称,关于文件桶的详细信息敬请参考 [腾讯云存储相关说明](https://cloud.tencent.com/document/product/436/44352)。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""该字段用于标识腾讯云对象存储的托管机房的分布地区，对象存储 COS 的数据存放在这些地域的存储桶中。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Object(self):
        r"""该字段用于标识腾讯云对象存储的对象Key,对象作为基本单元被存放在存储桶中；用户可以通过腾讯云控制台、API、SDK 等多种方式管理对象。有关对象的详细描述敬请参阅相应 [产品文档](https://cloud.tencent.com/document/product/436/13324)。
        :rtype: str
        """
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
    r"""CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 该字段表示创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要取消的审核任务。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""该字段表示创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要取消的审核任务。
        :rtype: str
        """
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
    r"""CancelTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateAudioModerationSyncTaskRequest(AbstractModel):
    r"""CreateAudioModerationSyncTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :type BizType: str
        :param _DataId: 数据标识，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type DataId: str
        :param _FileFormat: 音频文件资源格式，当前支持格式：wav、mp3、m4a，请按照实际文件格式填入。
        :type FileFormat: str
        :param _Name: 文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type Name: str
        :param _FileContent: 数据Base64编码，短音频同步接口仅传入可音频内容；
支持范围：文件大小不能超过5M，时长不可超过60s；
支持格式：wav (PCM编码)、mp3、m4a (采样率：16kHz~48kHz，位深：16bit 小端，声道数：单声道/双声道，建议格式：16kHz/16bit/单声道)。
        :type FileContent: str
        :param _FileUrl: 音频资源访问链接，与FileContent参数必须二选一输入；
支持范围及格式：同FileContent；
        :type FileUrl: str
        """
        self._BizType = None
        self._DataId = None
        self._FileFormat = None
        self._Name = None
        self._FileContent = None
        self._FileUrl = None

    @property
    def BizType(self):
        r"""Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DataId(self):
        r"""数据标识，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def FileFormat(self):
        r"""音频文件资源格式，当前支持格式：wav、mp3、m4a，请按照实际文件格式填入。
        :rtype: str
        """
        return self._FileFormat

    @FileFormat.setter
    def FileFormat(self, FileFormat):
        self._FileFormat = FileFormat

    @property
    def Name(self):
        r"""文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FileContent(self):
        r"""数据Base64编码，短音频同步接口仅传入可音频内容；
支持范围：文件大小不能超过5M，时长不可超过60s；
支持格式：wav (PCM编码)、mp3、m4a (采样率：16kHz~48kHz，位深：16bit 小端，声道数：单声道/双声道，建议格式：16kHz/16bit/单声道)。
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileUrl(self):
        r"""音频资源访问链接，与FileContent参数必须二选一输入；
支持范围及格式：同FileContent；
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._DataId = params.get("DataId")
        self._FileFormat = params.get("FileFormat")
        self._Name = params.get("Name")
        self._FileContent = params.get("FileContent")
        self._FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAudioModerationSyncTaskResponse(AbstractModel):
    r"""CreateAudioModerationSyncTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataId: 请求接口时传入的数据标识
        :type DataId: str
        :param _Name: 文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _BizType: Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :type BizType: str
        :param _Suggestion: 智能审核服务对于内容违规类型的等级，可选值：
Pass 建议通过；
Reveiw 建议复审；
Block 建议屏蔽；
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Label: 智能审核服务对于内容违规类型的判断，详见返回值列表
如：Label：Porn（色情）；
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _AsrText: 音频文本，备注：这里的文本最大只返回前1000个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrText: str
        :param _TextResults: 音频中对话内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type TextResults: list of TextResult
        :param _MoanResults: 音频中低俗内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type MoanResults: list of MoanResult
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _LanguageResults: 该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type LanguageResults: list of AudioResultDetailLanguageResult
        :param _SpeakerResults: 音频中说话人识别返回结果；
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeakerResults: list of AudioResultDetailSpeakerResult
        :param _RecognitionResults: 识别类标签结果信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognitionResults: list of RecognitionResult
        :param _Duration: 识别音频时长，单位为毫秒；
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _HitFlag: 是否命中(0:否, 1: 是)
        :type HitFlag: int
        :param _Score: 得分
        :type Score: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataId = None
        self._Name = None
        self._BizType = None
        self._Suggestion = None
        self._Label = None
        self._AsrText = None
        self._TextResults = None
        self._MoanResults = None
        self._SubLabel = None
        self._LanguageResults = None
        self._SpeakerResults = None
        self._RecognitionResults = None
        self._Duration = None
        self._HitFlag = None
        self._Score = None
        self._RequestId = None

    @property
    def DataId(self):
        r"""请求接口时传入的数据标识
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Name(self):
        r"""文件名称，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BizType(self):
        r"""Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。Biztype仅为数字、字母与下划线的组合，长度为3-32个字符；调用时不传入Biztype代表采用默认的识别策略。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Suggestion(self):
        r"""智能审核服务对于内容违规类型的等级，可选值：
Pass 建议通过；
Reveiw 建议复审；
Block 建议屏蔽；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        r"""智能审核服务对于内容违规类型的判断，详见返回值列表
如：Label：Porn（色情）；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def AsrText(self):
        r"""音频文本，备注：这里的文本最大只返回前1000个字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AsrText

    @AsrText.setter
    def AsrText(self, AsrText):
        self._AsrText = AsrText

    @property
    def TextResults(self):
        r"""音频中对话内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TextResult
        """
        return self._TextResults

    @TextResults.setter
    def TextResults(self, TextResults):
        self._TextResults = TextResults

    @property
    def MoanResults(self):
        r"""音频中低俗内容审核结果；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MoanResult
        """
        return self._MoanResults

    @MoanResults.setter
    def MoanResults(self, MoanResults):
        self._MoanResults = MoanResults

    @property
    def SubLabel(self):
        r"""该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def LanguageResults(self):
        r"""该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioResultDetailLanguageResult
        """
        return self._LanguageResults

    @LanguageResults.setter
    def LanguageResults(self, LanguageResults):
        self._LanguageResults = LanguageResults

    @property
    def SpeakerResults(self):
        r"""音频中说话人识别返回结果；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioResultDetailSpeakerResult
        """
        return self._SpeakerResults

    @SpeakerResults.setter
    def SpeakerResults(self, SpeakerResults):
        self._SpeakerResults = SpeakerResults

    @property
    def RecognitionResults(self):
        r"""识别类标签结果信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RecognitionResult
        """
        return self._RecognitionResults

    @RecognitionResults.setter
    def RecognitionResults(self, RecognitionResults):
        self._RecognitionResults = RecognitionResults

    @property
    def Duration(self):
        r"""识别音频时长，单位为毫秒；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def HitFlag(self):
        r"""是否命中(0:否, 1: 是)
        :rtype: int
        """
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Score(self):
        r"""得分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

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
        self._DataId = params.get("DataId")
        self._Name = params.get("Name")
        self._BizType = params.get("BizType")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._AsrText = params.get("AsrText")
        if params.get("TextResults") is not None:
            self._TextResults = []
            for item in params.get("TextResults"):
                obj = TextResult()
                obj._deserialize(item)
                self._TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self._MoanResults = []
            for item in params.get("MoanResults"):
                obj = MoanResult()
                obj._deserialize(item)
                self._MoanResults.append(obj)
        self._SubLabel = params.get("SubLabel")
        if params.get("LanguageResults") is not None:
            self._LanguageResults = []
            for item in params.get("LanguageResults"):
                obj = AudioResultDetailLanguageResult()
                obj._deserialize(item)
                self._LanguageResults.append(obj)
        if params.get("SpeakerResults") is not None:
            self._SpeakerResults = []
            for item in params.get("SpeakerResults"):
                obj = AudioResultDetailSpeakerResult()
                obj._deserialize(item)
                self._SpeakerResults.append(obj)
        if params.get("RecognitionResults") is not None:
            self._RecognitionResults = []
            for item in params.get("RecognitionResults"):
                obj = RecognitionResult()
                obj._deserialize(item)
                self._RecognitionResults.append(obj)
        self._Duration = params.get("Duration")
        self._HitFlag = params.get("HitFlag")
        self._Score = params.get("Score")
        self._RequestId = params.get("RequestId")


class CreateAudioModerationTaskRequest(AbstractModel):
    r"""CreateAudioModerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 该字段表示输入的音频审核任务信息，具体输入内容请参见TaskInput数据结构的详细描述。<br> 备注：最多同时可创建**10个任务**。
        :type Tasks: list of TaskInput
        :param _BizType: 该字段表示使用的策略的具体编号，该字段需要先在[内容安全控制台](https://console.cloud.tencent.com/cms/clouds/manage)中配置。
备注：不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。
        :type BizType: str
        :param _Type: 该字段表示输入的音频审核类型，取值含：**AUDIO**（点播音频）、**LIVE_AUDIO**（直播音频）、**AUDIO_AIGC**（AI生成识别）三种，默认值为AUDIO。
        :type Type: str
        :param _Seed: 可选参数，该字段表示回调签名的key信息，用于保证数据的安全性。 签名方法为在返回的HTTP头部添加 X-Signature 的字段，值为： seed + body 的 SHA256 编码和Hex字符串，在收到回调数据后，可以根据返回的body，用 **sha256(seed + body)**, 计算出 `X-Signature` 进行验证。<br>具体使用实例可参考 [回调签名示例](https://cloud.tencent.com/document/product/1219/104000#42dd87d2-580f-46cf-a953-639a787d1eda)。
        :type Seed: str
        :param _CallbackUrl: 接收审核信息回调地址。如果设置了该字段，在审核过程中发现违规音频片段结果将发送至该接口。更多详情请参阅[回调配置说明](https://cloud.tencent.com/document/product/1219/104000)。
        :type CallbackUrl: str
        :param _User: 该字段表示待检测对象对应的用户相关信息，若填入则可甄别相应违规风险用户
        :type User: :class:`tencentcloud.ams.v20201229.models.User`
        """
        self._Tasks = None
        self._BizType = None
        self._Type = None
        self._Seed = None
        self._CallbackUrl = None
        self._User = None

    @property
    def Tasks(self):
        r"""该字段表示输入的音频审核任务信息，具体输入内容请参见TaskInput数据结构的详细描述。<br> 备注：最多同时可创建**10个任务**。
        :rtype: list of TaskInput
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def BizType(self):
        r"""该字段表示使用的策略的具体编号，该字段需要先在[内容安全控制台](https://console.cloud.tencent.com/cms/clouds/manage)中配置。
备注：不同Biztype关联不同的业务场景与识别能力策略，调用前请确认正确的Biztype。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Type(self):
        r"""该字段表示输入的音频审核类型，取值含：**AUDIO**（点播音频）、**LIVE_AUDIO**（直播音频）、**AUDIO_AIGC**（AI生成识别）三种，默认值为AUDIO。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Seed(self):
        r"""可选参数，该字段表示回调签名的key信息，用于保证数据的安全性。 签名方法为在返回的HTTP头部添加 X-Signature 的字段，值为： seed + body 的 SHA256 编码和Hex字符串，在收到回调数据后，可以根据返回的body，用 **sha256(seed + body)**, 计算出 `X-Signature` 进行验证。<br>具体使用实例可参考 [回调签名示例](https://cloud.tencent.com/document/product/1219/104000#42dd87d2-580f-46cf-a953-639a787d1eda)。
        :rtype: str
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def CallbackUrl(self):
        r"""接收审核信息回调地址。如果设置了该字段，在审核过程中发现违规音频片段结果将发送至该接口。更多详情请参阅[回调配置说明](https://cloud.tencent.com/document/product/1219/104000)。
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def User(self):
        r"""该字段表示待检测对象对应的用户相关信息，若填入则可甄别相应违规风险用户
        :rtype: :class:`tencentcloud.ams.v20201229.models.User`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._BizType = params.get("BizType")
        self._Type = params.get("Type")
        self._Seed = params.get("Seed")
        self._CallbackUrl = params.get("CallbackUrl")
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
        


class CreateAudioModerationTaskResponse(AbstractModel):
    r"""CreateAudioModerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 该字段用于返回任务创建的结果，具体输出内容请参见TaskResult数据结构的详细描述。
        :type Results: list of TaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        r"""该字段用于返回任务创建的结果，具体输出内容请参见TaskResult数据结构的详细描述。
        :rtype: list of TaskResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

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
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    r"""DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 该字段表示创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
<br>备注：查询接口单次最大查询量为**20条每次**。
        :type TaskId: str
        :param _ShowAllSegments: 该布尔字段表示是否展示全部的音频片段，取值：True(展示全部的音频分片)、False(只展示命中审核规则的音频分片)；默认值为False。
        :type ShowAllSegments: bool
        """
        self._TaskId = None
        self._ShowAllSegments = None

    @property
    def TaskId(self):
        r"""该字段表示创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
<br>备注：查询接口单次最大查询量为**20条每次**。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ShowAllSegments(self):
        r"""该布尔字段表示是否展示全部的音频片段，取值：True(展示全部的音频分片)、False(只展示命中审核规则的音频分片)；默认值为False。
        :rtype: bool
        """
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
    r"""DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 该字段用于返回创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
        :type TaskId: str
        :param _DataId: 该字段用于返回调用音频审核接口时在Tasks参数内传入的数据ID参数，方便数据的辨别和管理。
        :type DataId: str
        :param _BizType: 该字段用于返回调用音频审核接口时传入的BizType参数，方便数据的辨别和管理。
        :type BizType: str
        :param _Name: 该字段用于返回调用音频审核接口时传入的TaskInput参数中的任务名称，方便任务的识别与管理。
        :type Name: str
        :param _Status: 该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
        :type Status: str
        :param _Type: 该字段用于返回调用音频审核接口时输入的音频审核类型，取值为：**AUDIO**（点播音频）和**LIVE_AUDIO**（直播音频），默认值为AUDIO。
        :type Type: str
        :param _Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        :param _Labels: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :type Labels: list of TaskLabel
        :param _InputInfo: 该字段用于返回审核服务的媒体内容信息，主要包括传入文件类型和访问地址。
        :type InputInfo: :class:`tencentcloud.ams.v20201229.models.InputInfo`
        :param _AudioText: 该字段用于返回音频文件识别出的对应文本内容，最大支持**前1000个字符**。
        :type AudioText: str
        :param _AudioSegments: 该字段用于返回音频片段的审核结果，主要包括开始时间和音频审核的相应结果。<br>具体输出内容请参见AudioSegments及AudioResult数据结构的详细描述。
        :type AudioSegments: list of AudioSegments
        :param _ErrorType: 当任务状态为Error时，该字段用于返回对应错误的类型；任务状态非Error时，默认返回为空。
        :type ErrorType: str
        :param _ErrorDescription: 当任务状态为Error时，该字段用于返回对应错误的详细描述，任务状态非Error时默认返回为空。
        :type ErrorDescription: str
        :param _CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
        :type CreatedAt: str
        :param _UpdatedAt: 该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
        :type UpdatedAt: str
        :param _Label: 该字段用于返回检测结果所对应的标签。如果未命中恶意，返回Normal，如果命中恶意，则返回Labels中优先级最高的标签
        :type Label: str
        :param _MediaInfo: 媒体信息
        :type MediaInfo: :class:`tencentcloud.ams.v20201229.models.MediaInfo`
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
        self._InputInfo = None
        self._AudioText = None
        self._AudioSegments = None
        self._ErrorType = None
        self._ErrorDescription = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Label = None
        self._MediaInfo = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""该字段用于返回创建音频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DataId(self):
        r"""该字段用于返回调用音频审核接口时在Tasks参数内传入的数据ID参数，方便数据的辨别和管理。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        r"""该字段用于返回调用音频审核接口时传入的BizType参数，方便数据的辨别和管理。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Name(self):
        r"""该字段用于返回调用音频审核接口时传入的TaskInput参数中的任务名称，方便任务的识别与管理。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""该字段用于返回调用音频审核接口时输入的音频审核类型，取值为：**AUDIO**（点播音频）和**LIVE_AUDIO**（直播音频），默认值为AUDIO。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        r"""该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Labels(self):
        r"""该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :rtype: list of TaskLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def InputInfo(self):
        r"""该字段用于返回审核服务的媒体内容信息，主要包括传入文件类型和访问地址。
        :rtype: :class:`tencentcloud.ams.v20201229.models.InputInfo`
        """
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo

    @property
    def AudioText(self):
        r"""该字段用于返回音频文件识别出的对应文本内容，最大支持**前1000个字符**。
        :rtype: str
        """
        return self._AudioText

    @AudioText.setter
    def AudioText(self, AudioText):
        self._AudioText = AudioText

    @property
    def AudioSegments(self):
        r"""该字段用于返回音频片段的审核结果，主要包括开始时间和音频审核的相应结果。<br>具体输出内容请参见AudioSegments及AudioResult数据结构的详细描述。
        :rtype: list of AudioSegments
        """
        return self._AudioSegments

    @AudioSegments.setter
    def AudioSegments(self, AudioSegments):
        self._AudioSegments = AudioSegments

    @property
    def ErrorType(self):
        r"""当任务状态为Error时，该字段用于返回对应错误的类型；任务状态非Error时，默认返回为空。
        :rtype: str
        """
        return self._ErrorType

    @ErrorType.setter
    def ErrorType(self, ErrorType):
        self._ErrorType = ErrorType

    @property
    def ErrorDescription(self):
        r"""当任务状态为Error时，该字段用于返回对应错误的详细描述，任务状态非Error时默认返回为空。
        :rtype: str
        """
        return self._ErrorDescription

    @ErrorDescription.setter
    def ErrorDescription(self, ErrorDescription):
        self._ErrorDescription = ErrorDescription

    @property
    def CreatedAt(self):
        r"""该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Label(self):
        r"""该字段用于返回检测结果所对应的标签。如果未命中恶意，返回Normal，如果命中恶意，则返回Labels中优先级最高的标签
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def MediaInfo(self):
        r"""媒体信息
        :rtype: :class:`tencentcloud.ams.v20201229.models.MediaInfo`
        """
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

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
        if params.get("InputInfo") is not None:
            self._InputInfo = InputInfo()
            self._InputInfo._deserialize(params.get("InputInfo"))
        self._AudioText = params.get("AudioText")
        if params.get("AudioSegments") is not None:
            self._AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self._AudioSegments.append(obj)
        self._ErrorType = params.get("ErrorType")
        self._ErrorDescription = params.get("ErrorDescription")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Label = params.get("Label")
        if params.get("MediaInfo") is not None:
            self._MediaInfo = MediaInfo()
            self._MediaInfo._deserialize(params.get("MediaInfo"))
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    r"""DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 该参数表示任务列表每页展示的任务条数，**默认值为10**（每页展示10条任务）。
        :type Limit: int
        :param _Filter: 该参数表示任务筛选器的输入参数，可根据业务类型、审核文件类型、处理建议及任务状态筛选想要查看的审核任务，具体参数内容请参见TaskFilter数据结构的详细描述。
        :type Filter: :class:`tencentcloud.ams.v20201229.models.TaskFilter`
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
        r"""该参数表示任务列表每页展示的任务条数，**默认值为10**（每页展示10条任务）。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        r"""该参数表示任务筛选器的输入参数，可根据业务类型、审核文件类型、处理建议及任务状态筛选想要查看的审核任务，具体参数内容请参见TaskFilter数据结构的详细描述。
        :rtype: :class:`tencentcloud.ams.v20201229.models.TaskFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def PageToken(self):
        r"""该参数表示翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
        :rtype: str
        """
        return self._PageToken

    @PageToken.setter
    def PageToken(self, PageToken):
        self._PageToken = PageToken

    @property
    def StartTime(self):
        r"""该参数表示任务列表的开始时间，格式为ISO8601标准的时间戳。**默认值为最近3天**，若传入该参数，则在这一时间到EndTime之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""该参数表示任务列表的结束时间，格式为ISO8601标准的时间戳。**默认值为空**，若传入该参数，则在这StartTime到这一时间之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :rtype: str
        """
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
    r"""DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 该字段用于返回当前查询的任务总量，格式为int字符串。
        :type Total: str
        :param _Data: 该字段用于返回当前页的任务详细数据，具体输出内容请参见TaskData数据结构的详细描述。
        :type Data: list of TaskData
        :param _PageToken: 该字段用于返回翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
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
        r"""该字段用于返回当前查询的任务总量，格式为int字符串。
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""该字段用于返回当前页的任务详细数据，具体输出内容请参见TaskData数据结构的详细描述。
        :rtype: list of TaskData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def PageToken(self):
        r"""该字段用于返回翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
        :rtype: str
        """
        return self._PageToken

    @PageToken.setter
    def PageToken(self, PageToken):
        self._PageToken = PageToken

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._PageToken = params.get("PageToken")
        self._RequestId = params.get("RequestId")


class HitInfo(AbstractModel):
    r"""关键词命中位置信息

    """

    def __init__(self):
        r"""
        :param _Type: 标识模型命中还是关键词命中
        :type Type: str
        :param _Keyword: 命中关键词
        :type Keyword: str
        :param _LibName: 自定义词库名称
        :type LibName: str
        :param _Positions: 	位置信息
        :type Positions: list of Position
        """
        self._Type = None
        self._Keyword = None
        self._LibName = None
        self._Positions = None

    @property
    def Type(self):
        r"""标识模型命中还是关键词命中
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Keyword(self):
        r"""命中关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def LibName(self):
        r"""自定义词库名称
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Positions(self):
        r"""	位置信息
        :rtype: list of Position
        """
        return self._Positions

    @Positions.setter
    def Positions(self, Positions):
        self._Positions = Positions


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Keyword = params.get("Keyword")
        self._LibName = params.get("LibName")
        if params.get("Positions") is not None:
            self._Positions = []
            for item in params.get("Positions"):
                obj = Position()
                obj._deserialize(item)
                self._Positions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    r"""输入信息详情

    """

    def __init__(self):
        r"""
        :param _Type: 该字段表示文件访问类型，取值为**URL**（资源链接）和**COS** (腾讯云对象存储)。
        :type Type: str
        :param _Url: 该字段表示文件访问的链接地址，格式为标准URL格式。<br> 备注：当Type为URL时此字段不为空。
        :type Url: str
        :param _BucketInfo: 该字段表示文件访问的腾讯云存储桶信息。<br> 备注：当Type为COS时此字段不为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketInfo: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        r"""该字段表示文件访问类型，取值为**URL**（资源链接）和**COS** (腾讯云对象存储)。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""该字段表示文件访问的链接地址，格式为标准URL格式。<br> 备注：当Type为URL时此字段不为空。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        r"""该字段表示文件访问的腾讯云存储桶信息。<br> 备注：当Type为COS时此字段不为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
        """
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
        


class LabelResults(AbstractModel):
    r"""歌曲识别结果

    """

    def __init__(self):
        r"""
        :param _Scene: 场景
        :type Scene: str
        :param _Suggestion: 建议值
        :type Suggestion: int
        :param _Label: 标签
        :type Label: str
        :param _Name: 名称：歌曲名，语种名，说话人名 等
        :type Name: str
        :param _Score: 得分
        :type Score: int
        :param _StartTime: 开始时间
        :type StartTime: float
        :param _EndTime: 结束时间
        :type EndTime: float
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._Name = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Scene(self):
        r"""场景
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        r"""建议值
        :rtype: int
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        r"""标签
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Name(self):
        r"""名称：歌曲名，语种名，说话人名 等
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        r"""得分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
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
        


class MediaInfo(AbstractModel):
    r"""媒体类型

    """

    def __init__(self):
        r"""
        :param _Codecs: 该字段用于返回传入的媒体文件的编码格式，如wav、mp3、aac、flac、amr、3gp、 m4a、wma、ogg、ape等。
        :type Codecs: str
        :param _Duration: 该字段用于返回对传入的流媒体文件进行分片的片段时长，单位为毫秒。**默认值为15秒**，支持用户自定义配置。
        :type Duration: int
        :param _Width: *内测中，敬请期待*
        :type Width: int
        :param _Height: *内测中，敬请期待*
        :type Height: int
        :param _Thumbnail: *内测中，敬请期待*
        :type Thumbnail: str
        """
        self._Codecs = None
        self._Duration = None
        self._Width = None
        self._Height = None
        self._Thumbnail = None

    @property
    def Codecs(self):
        r"""该字段用于返回传入的媒体文件的编码格式，如wav、mp3、aac、flac、amr、3gp、 m4a、wma、ogg、ape等。
        :rtype: str
        """
        return self._Codecs

    @Codecs.setter
    def Codecs(self, Codecs):
        self._Codecs = Codecs

    @property
    def Duration(self):
        r"""该字段用于返回对传入的流媒体文件进行分片的片段时长，单位为毫秒。**默认值为15秒**，支持用户自定义配置。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Width(self):
        r"""*内测中，敬请期待*
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""*内测中，敬请期待*
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Thumbnail(self):
        r"""*内测中，敬请期待*
        :rtype: str
        """
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
        


class MoanResult(AbstractModel):
    r"""呻吟低俗检测结果

    """

    def __init__(self):
        r"""
        :param _Label: 固定取值为Moan（呻吟/娇喘），如音频中无复杂类型「MoanResult」的返回则代表该音频中无呻吟/娇喘相关违规内容；
        :type Label: str
        :param _Score: 机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Moan 99，则该样本属于呻吟/娇喘的置信度非常高。）
        :type Score: int
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _StartTime: 违规事件开始时间，单位为秒（s）；
        :type StartTime: float
        :param _EndTime: 违规事件结束时间，单位为秒（s）；
        :type EndTime: float
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
        :type SubLabel: str
        """
        self._Label = None
        self._Score = None
        self._Suggestion = None
        self._StartTime = None
        self._EndTime = None
        self._SubLabel = None

    @property
    def Label(self):
        r"""固定取值为Moan（呻吟/娇喘），如音频中无复杂类型「MoanResult」的返回则代表该音频中无呻吟/娇喘相关违规内容；
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        r"""机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Moan 99，则该样本属于呻吟/娇喘的置信度非常高。）
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Suggestion(self):
        r"""建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def StartTime(self):
        r"""违规事件开始时间，单位为秒（s）；
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""违规事件结束时间，单位为秒（s）；
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubLabel(self):
        r"""该字段用于返回当前标签（Lable）下的二级标签。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Score = params.get("Score")
        self._Suggestion = params.get("Suggestion")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Position(AbstractModel):
    r"""标识命中的违规关键词位置信息

    """

    def __init__(self):
        r"""
        :param _Start: 关键词起始位置
        :type Start: int
        :param _End: 关键词结束位置
        :type End: int
        """
        self._Start = None
        self._End = None

    @property
    def Start(self):
        r"""关键词起始位置
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        r"""关键词结束位置
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionResult(AbstractModel):
    r"""识别类标签结果信息

    """

    def __init__(self):
        r"""
        :param _Label: 可能的取值有：Teenager 、Gender
        :type Label: str
        :param _Tags: 识别标签列表
        :type Tags: list of Tag
        """
        self._Label = None
        self._Tags = None

    @property
    def Label(self):
        r"""可能的取值有：Teenager 、Gender
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Tags(self):
        r"""识别标签列表
        :rtype: list of Tag
        """
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
        


class SpeakerResults(AbstractModel):
    r"""说话人结果

    """

    def __init__(self):
        r"""
        :param _Label: 标签
        :type Label: str
        :param _Score: 得分
        :type Score: int
        :param _StartTime: 开始时间
        :type StartTime: float
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._Label = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Label(self):
        r"""标签
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Score(self):
        r"""得分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Label = params.get("Label")
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
        


class StorageInfo(AbstractModel):
    r"""用于表示数据存储的相关信息

    """

    def __init__(self):
        r"""
        :param _Type: 该字段表示文件访问类型，取值为**URL**（资源链接）和**COS** (腾讯云对象存储)；该字段应当与传入的访问类型相对应，可用于强校验并方便系统快速识别访问地址；若不传入此参数，则默认值为URL，此时系统将自动判定访问地址类型。
        :type Type: str
        :param _Url: 该字段表示文件访问的链接地址，格式为标准URL格式。<br> 备注：当Type为URL时此字段不为空，该参数与BucketInfo参数须传入其中之一
        :type Url: str
        :param _BucketInfo: 该字段表示文件访问的腾讯云存储桶信息。<br> 备注：当Type为COS时此字段不为空，该参数与Url参数须传入其中之一。
        :type BucketInfo: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
        """
        self._Type = None
        self._Url = None
        self._BucketInfo = None

    @property
    def Type(self):
        r"""该字段表示文件访问类型，取值为**URL**（资源链接）和**COS** (腾讯云对象存储)；该字段应当与传入的访问类型相对应，可用于强校验并方便系统快速识别访问地址；若不传入此参数，则默认值为URL，此时系统将自动判定访问地址类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""该字段表示文件访问的链接地址，格式为标准URL格式。<br> 备注：当Type为URL时此字段不为空，该参数与BucketInfo参数须传入其中之一
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BucketInfo(self):
        r"""该字段表示文件访问的腾讯云存储桶信息。<br> 备注：当Type为COS时此字段不为空，该参数与Url参数须传入其中之一。
        :rtype: :class:`tencentcloud.ams.v20201229.models.BucketInfo`
        """
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
    r"""音频切片识别标签

    """

    def __init__(self):
        r"""
        :param _Name: 根据Label字段确定具体名称：
当Label 为Teenager 时 Name可能取值有：Teenager 
当Label 为Gender 时 Name可能取值有：Male 、Female
        :type Name: str
        :param _Score: 置信分：0～100，数值越大表示置信度越高
        :type Score: int
        :param _StartTime: 识别开始偏移时间，单位：毫秒
        :type StartTime: float
        :param _EndTime: 识别结束偏移时间，单位：毫秒
        :type EndTime: float
        """
        self._Name = None
        self._Score = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Name(self):
        r"""根据Label字段确定具体名称：
当Label 为Teenager 时 Name可能取值有：Teenager 
当Label 为Gender 时 Name可能取值有：Male 、Female
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        r"""置信分：0～100，数值越大表示置信度越高
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def StartTime(self):
        r"""识别开始偏移时间，单位：毫秒
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""识别结束偏移时间，单位：毫秒
        :rtype: float
        """
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
    r"""任务数据

    """

    def __init__(self):
        r"""
        :param _DataId: 该字段用于返回音频审核任务数据所对应的数据ID，方便后续查询和管理审核任务。
        :type DataId: str
        :param _TaskId: 该字段用于返回音频审核任务所生成的任务ID，用于标识具体审核任务，方便后续查询和管理。
        :type TaskId: str
        :param _Status: 该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
        :type Status: str
        :param _Name: 该字段用于返回音频审核任务所对应的任务名称，方便后续查询和管理审核任务。
        :type Name: str
        :param _BizType: 该字段用于返回调用音频审核接口时传入的BizType参数，方便数据的辨别和管理。
        :type BizType: str
        :param _Type: 该字段用于返回调用音频审核接口时输入的音频审核类型，取值为：**AUDIO**（点播音频）和**LIVE_AUDIO**（直播音频），默认值为AUDIO。
        :type Type: str
        :param _Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        :param _MediaInfo: 输入信息
        :type MediaInfo: :class:`tencentcloud.ams.v20201229.models.MediaInfo`
        :param _Labels: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :type Labels: list of TaskLabel
        :param _CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
        :type CreatedAt: str
        :param _UpdatedAt: 该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
        :type UpdatedAt: str
        :param _InputInfo: 任务信息
        :type InputInfo: :class:`tencentcloud.ams.v20201229.models.InputInfo`
        """
        self._DataId = None
        self._TaskId = None
        self._Status = None
        self._Name = None
        self._BizType = None
        self._Type = None
        self._Suggestion = None
        self._MediaInfo = None
        self._Labels = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._InputInfo = None

    @property
    def DataId(self):
        r"""该字段用于返回音频审核任务数据所对应的数据ID，方便后续查询和管理审核任务。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def TaskId(self):
        r"""该字段用于返回音频审核任务所生成的任务ID，用于标识具体审核任务，方便后续查询和管理。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Name(self):
        r"""该字段用于返回音频审核任务所对应的任务名称，方便后续查询和管理审核任务。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BizType(self):
        r"""该字段用于返回调用音频审核接口时传入的BizType参数，方便数据的辨别和管理。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Type(self):
        r"""该字段用于返回调用音频审核接口时输入的音频审核类型，取值为：**AUDIO**（点播音频）和**LIVE_AUDIO**（直播音频），默认值为AUDIO。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        r"""该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def MediaInfo(self):
        r"""输入信息
        :rtype: :class:`tencentcloud.ams.v20201229.models.MediaInfo`
        """
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

    @property
    def Labels(self):
        r"""该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :rtype: list of TaskLabel
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def CreatedAt(self):
        r"""该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def InputInfo(self):
        r"""任务信息
        :rtype: :class:`tencentcloud.ams.v20201229.models.InputInfo`
        """
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        self._BizType = params.get("BizType")
        self._Type = params.get("Type")
        self._Suggestion = params.get("Suggestion")
        if params.get("MediaInfo") is not None:
            self._MediaInfo = MediaInfo()
            self._MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("InputInfo") is not None:
            self._InputInfo = InputInfo()
            self._InputInfo._deserialize(params.get("InputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFilter(AbstractModel):
    r"""任务筛选器

    """

    def __init__(self):
        r"""
        :param _BizType: 该字段用于传入任务对应的业务类型供筛选器进行筛选。Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与审核策略，调用前请确认正确的Biztype。Biztype仅为**数字、字母与下划线的组合**，长度为3-32个字符。<br>备注：在不传入该参数时筛选器默认不筛选业务类型。
        :type BizType: str
        :param _Type: 该字段用于传入音频审核对应的任务类型供筛选器进行筛选，取值为：**VIDEO**（点播视频审核），**AUDIO**（点播音频审核）， **LIVE_VIDEO**（直播视频审核）, **LIVE_AUDIO**（直播音频审核）。<br>备注：在不传入该参数时筛选器默认不筛选任务类型。
        :type Type: str
        :param _Suggestion: 该字段用于传入音频审核对应的建议操作供筛选器进行筛选，取值为：**Block**：建议屏蔽，**Review**：建议人工复审，**Pass**：建议通过。<br>备注：在不传入该参数时筛选器默认不筛选建议操作。
        :type Suggestion: str
        :param _TaskStatus: 该字段用于传入审核任务的任务状态供筛选器进行筛选，取值为：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。<br>备注：在不传入该参数时筛选器默认不筛选任务状态。
        :type TaskStatus: str
        """
        self._BizType = None
        self._Type = None
        self._Suggestion = None
        self._TaskStatus = None

    @property
    def BizType(self):
        r"""该字段用于传入任务对应的业务类型供筛选器进行筛选。Biztype为策略的具体的编号，用于接口调度，在内容安全控制台中可配置。不同Biztype关联不同的业务场景与审核策略，调用前请确认正确的Biztype。Biztype仅为**数字、字母与下划线的组合**，长度为3-32个字符。<br>备注：在不传入该参数时筛选器默认不筛选业务类型。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Type(self):
        r"""该字段用于传入音频审核对应的任务类型供筛选器进行筛选，取值为：**VIDEO**（点播视频审核），**AUDIO**（点播音频审核）， **LIVE_VIDEO**（直播视频审核）, **LIVE_AUDIO**（直播音频审核）。<br>备注：在不传入该参数时筛选器默认不筛选任务类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Suggestion(self):
        r"""该字段用于传入音频审核对应的建议操作供筛选器进行筛选，取值为：**Block**：建议屏蔽，**Review**：建议人工复审，**Pass**：建议通过。<br>备注：在不传入该参数时筛选器默认不筛选建议操作。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def TaskStatus(self):
        r"""该字段用于传入审核任务的任务状态供筛选器进行筛选，取值为：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。<br>备注：在不传入该参数时筛选器默认不筛选任务状态。
        :rtype: str
        """
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
    r"""音视频任务数据结构

    """

    def __init__(self):
        r"""
        :param _DataId: 选填参数，该字段表示您为待检测对象分配的数据ID，传入后可方便您对文件进行标识和管理。<br>取值：由英文字母（大小写均可）、数字及四个特殊符号（_，-，@，#）组成，**长度不超过64个字符**。
        :type DataId: str
        :param _Name: 选填参数，该字段表示音频审核任务所对应的任务名称，方便后续查询和管理审核任务。
        :type Name: str
        :param _Input: 必填参数，该字段表示审核文件的访问参数，用于获取审核媒体文件，该参数内包括访问类型和访问地址。
        :type Input: :class:`tencentcloud.ams.v20201229.models.StorageInfo`
        """
        self._DataId = None
        self._Name = None
        self._Input = None

    @property
    def DataId(self):
        r"""选填参数，该字段表示您为待检测对象分配的数据ID，传入后可方便您对文件进行标识和管理。<br>取值：由英文字母（大小写均可）、数字及四个特殊符号（_，-，@，#）组成，**长度不超过64个字符**。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Name(self):
        r"""选填参数，该字段表示音频审核任务所对应的任务名称，方便后续查询和管理审核任务。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Input(self):
        r"""必填参数，该字段表示审核文件的访问参数，用于获取审核媒体文件，该参数内包括访问类型和访问地址。
        :rtype: :class:`tencentcloud.ams.v20201229.models.StorageInfo`
        """
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
    r"""用于返回审核任务输出的标签

    """

    def __init__(self):
        r"""
        :param _Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _Suggestion: 该字段用于返回当前标签对应的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        :param _Score: 该字段用于返回当前标签（Label）下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容；*色情 0*，则表明该文本不属于色情内容。
        :type Score: int
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
        :type SubLabel: str
        """
        self._Label = None
        self._Suggestion = None
        self._Score = None
        self._SubLabel = None

    @property
    def Label(self):
        r"""该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        r"""该字段用于返回当前标签对应的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Score(self):
        r"""该字段用于返回当前标签（Label）下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容；*色情 0*，则表明该文本不属于色情内容。
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def SubLabel(self):
        r"""该字段用于返回当前标签（Lable）下的二级标签。
        :rtype: str
        """
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
    r"""创建任务时的返回结果

    """

    def __init__(self):
        r"""
        :param _DataId: 该字段用于返回创建音频审核任务时在TaskInput结构内传入的DataId，用于标识具体审核任务。
        :type DataId: str
        :param _TaskId: 该字段用于返回音频审核任务所生成的任务ID，用于标识具体审核任务，方便后续查询和管理。
        :type TaskId: str
        :param _Code: 该字段用于返回任务创建的状态，如返回OK则代表任务创建成功，其他返回值可参考公共错误码。
        :type Code: str
        :param _Message: **仅在Code的返回值为错误码时生效**，用于返回错误的详情内容。
        :type Message: str
        """
        self._DataId = None
        self._TaskId = None
        self._Code = None
        self._Message = None

    @property
    def DataId(self):
        r"""该字段用于返回创建音频审核任务时在TaskInput结构内传入的DataId，用于标识具体审核任务。
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def TaskId(self):
        r"""该字段用于返回音频审核任务所生成的任务ID，用于标识具体审核任务，方便后续查询和管理。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Code(self):
        r"""该字段用于返回任务创建的状态，如返回OK则代表任务创建成功，其他返回值可参考公共错误码。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""**仅在Code的返回值为错误码时生效**，用于返回错误的详情内容。
        :rtype: str
        """
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
        


class TextResult(AbstractModel):
    r"""音频文本内容审核结果

    """

    def __init__(self):
        r"""
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告。
以及其他令人反感、不安全或不适宜的内容类型。

如音频中无复杂类型「TextResults」的返回则代表该音频中无相关违规内容；
        :type Label: str
        :param _Keywords: 命中的关键词，为空则代表该违规内容出自于模型的判断；
        :type Keywords: list of str
        :param _LibId: 命中关键词库的库标识；
        :type LibId: str
        :param _LibName: 命中关键词库的名字；
        :type LibName: str
        :param _Score: 机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Porn 99，则该样本属于色情的置信度非常高。）
        :type Score: int
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _LibType: 自定义词库的类型，自定义词库相关的信息可登录控制台中查看；
1：自定义黑白库；
2：公库；
        :type LibType: int
        :param _SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
        :type SubLabel: str
        :param _HitInfos: 该字段用于返回违规文本命中信息
        :type HitInfos: list of HitInfo
        """
        self._Label = None
        self._Keywords = None
        self._LibId = None
        self._LibName = None
        self._Score = None
        self._Suggestion = None
        self._LibType = None
        self._SubLabel = None
        self._HitInfos = None

    @property
    def Label(self):
        r"""恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告。
以及其他令人反感、不安全或不适宜的内容类型。

如音频中无复杂类型「TextResults」的返回则代表该音频中无相关违规内容；
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Keywords(self):
        r"""命中的关键词，为空则代表该违规内容出自于模型的判断；
        :rtype: list of str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def LibId(self):
        r"""命中关键词库的库标识；
        :rtype: str
        """
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        r"""命中关键词库的名字；
        :rtype: str
        """
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Score(self):
        r"""机器判断当前分类的置信度，取值范围：0~100。分数越高，表示越有可能属于当前分类。
（如：Porn 99，则该样本属于色情的置信度非常高。）
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Suggestion(self):
        r"""建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def LibType(self):
        r"""自定义词库的类型，自定义词库相关的信息可登录控制台中查看；
1：自定义黑白库；
2：公库；
        :rtype: int
        """
        return self._LibType

    @LibType.setter
    def LibType(self, LibType):
        self._LibType = LibType

    @property
    def SubLabel(self):
        r"""该字段用于返回当前标签（Lable）下的二级标签。
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def HitInfos(self):
        r"""该字段用于返回违规文本命中信息
        :rtype: list of HitInfo
        """
        return self._HitInfos

    @HitInfos.setter
    def HitInfos(self, HitInfos):
        self._HitInfos = HitInfos


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Keywords = params.get("Keywords")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Score = params.get("Score")
        self._Suggestion = params.get("Suggestion")
        self._LibType = params.get("LibType")
        self._SubLabel = params.get("SubLabel")
        if params.get("HitInfos") is not None:
            self._HitInfos = []
            for item in params.get("HitInfos"):
                obj = HitInfo()
                obj._deserialize(item)
                self._HitInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TravelResults(AbstractModel):
    r"""出行结果

    """

    def __init__(self):
        r"""
        :param _Label: 一级标签
        :type Label: str
        :param _SubLabel: 二级标签
        :type SubLabel: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: str
        :param _AudioRole: 出行音频角色
        :type AudioRole: str
        :param _AudioText: 出行语音文本
        :type AudioText: str
        :param _StartTime: 开始时间
        :type StartTime: float
        :param _EndTime: 结束时间
        :type EndTime: float
        """
        self._Label = None
        self._SubLabel = None
        self._RiskLevel = None
        self._AudioRole = None
        self._AudioText = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Label(self):
        r"""一级标签
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        r"""二级标签
        :rtype: str
        """
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def AudioRole(self):
        r"""出行音频角色
        :rtype: str
        """
        return self._AudioRole

    @AudioRole.setter
    def AudioRole(self, AudioRole):
        self._AudioRole = AudioRole

    @property
    def AudioText(self):
        r"""出行语音文本
        :rtype: str
        """
        return self._AudioText

    @AudioText.setter
    def AudioText(self, AudioText):
        self._AudioText = AudioText

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: float
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: float
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._RiskLevel = params.get("RiskLevel")
        self._AudioRole = params.get("AudioRole")
        self._AudioText = params.get("AudioText")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    r"""User结果

    """

    def __init__(self):
        r"""
        :param _Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param _Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param _Age: 年龄 默认0 未知
        :type Age: int
        :param _UserId: 业务用户ID 如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param _Phone: 手机号
        :type Phone: str
        :param _AccountType: 业务用户ID类型 "1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :type AccountType: str
        :param _Nickname: 用户昵称
        :type Nickname: str
        :param _HeadUrl: 用户头像图片链接
        :type HeadUrl: str
        :param _Desc: 用户简介，长度不超过5000字
        :type Desc: str
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
        self._Level = None
        self._Gender = None
        self._Age = None
        self._UserId = None
        self._Phone = None
        self._AccountType = None
        self._Nickname = None
        self._HeadUrl = None
        self._Desc = None
        self._RoomId = None
        self._GroupId = None
        self._GroupSize = None
        self._ReceiverId = None
        self._SendTime = None

    @property
    def Level(self):
        r"""用户等级，默认0 未知 1 低 2 中 3 高
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Gender(self):
        r"""性别 默认0 未知 1 男性 2 女性
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        r"""年龄 默认0 未知
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def UserId(self):
        r"""业务用户ID 如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Phone(self):
        r"""手机号
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def AccountType(self):
        r"""业务用户ID类型 "1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Nickname(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def HeadUrl(self):
        r"""用户头像图片链接
        :rtype: str
        """
        return self._HeadUrl

    @HeadUrl.setter
    def HeadUrl(self, HeadUrl):
        self._HeadUrl = HeadUrl

    @property
    def Desc(self):
        r"""用户简介，长度不超过5000字
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def RoomId(self):
        r"""群聊场景房间ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        r"""群聊场景群ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupSize(self):
        r"""群聊场景群用户数
        :rtype: int
        """
        return self._GroupSize

    @GroupSize.setter
    def GroupSize(self, GroupSize):
        self._GroupSize = GroupSize

    @property
    def ReceiverId(self):
        r"""消息接收者ID
        :rtype: str
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def SendTime(self):
        r"""消息生成时间，毫秒
        :rtype: str
        """
        return self._SendTime

    @SendTime.setter
    def SendTime(self, SendTime):
        self._SendTime = SendTime


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._UserId = params.get("UserId")
        self._Phone = params.get("Phone")
        self._AccountType = params.get("AccountType")
        self._Nickname = params.get("Nickname")
        self._HeadUrl = params.get("HeadUrl")
        self._Desc = params.get("Desc")
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
        