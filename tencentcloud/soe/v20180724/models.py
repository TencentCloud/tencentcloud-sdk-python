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


class InitOralProcessRequest(AbstractModel):
    """InitOralProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param _RefText: 被评估语音对应的文本，仅支持中文和英文。
句子模式下不超过个 30 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式RefText可以不填。
关于RefText的文本键入要求，请参考[评测模式介绍](https://cloud.tencent.com/document/product/884/56131)。
如需要在评测模式下使用自定义注音（支持中英文），可以通过设置「TextMode」参数实现，设置方式请参考[音素标注](https://cloud.tencent.com/document/product/884/33698)。
        :type RefText: str
        :param _WorkMode: 语音输入模式
0：流式分片
1：非流式一次性评估
推荐使用流式分片传输。
        :type WorkMode: int
        :param _EvalMode: 评测模式
0：单词/单字模式（中文评测模式下为单字模式）
1：句子模式
2：段落模式
3：自由说模式
4：单词音素纠错模式
5：情景评测模式
6：句子多分支评测模式
7：单词实时评测模式
8：拼音评测模式
关于每种评测模式的详细介绍，以及适用场景，请参考[评测模式介绍](https://cloud.tencent.com/document/product/884/56131)。
        :type EvalMode: int
        :param _ScoreCoeff: 评价苛刻指数。取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数。
1.0：适用于最小年龄段用户，一般对应儿童应用场景；
4.0：适用于最高年龄段用户，一般对应成人严格打分场景。苛刻度影响范围参考：[苛刻度影响范围](https://cloud.tencent.com/document/product/884/78824#.E8.8B.9B.E5.88.BB.E5.BA.A6)
        :type ScoreCoeff: float
        :param _SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。使用指南：[业务应用](https://cloud.tencent.com/document/product/884/78824#.E4.B8.9A.E5.8A.A1.E5.BA.94.E7.94.A8)
        :type SoeAppId: str
        :param _IsLongLifeSession: 长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度，且TransmitOralProcess必须同时为1才可生效。
        :type IsLongLifeSession: int
        :param _StorageMode: 音频存储模式，此参数已废弃，无需设置，设置与否都默认为0不存储；
注：有存储需求的用户建议自行存储至腾讯云COS[对象存储](https://cloud.tencent.com/product/cos)使用。
        :type StorageMode: int
        :param _SentenceInfoEnabled: 输出断句中间结果标识
0：不输出
1：输出，通过设置该参数
可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。
        :type SentenceInfoEnabled: int
        :param _ServerType: 评估语言
0：英文（默认）
1：中文
        :type ServerType: int
        :param _IsAsync: 异步模式标识
0：同步模式
1：异步模式（一般情况不建议使用异步模式）
可选值参考[服务模式](https://cloud.tencent.com/document/product/884/33697)。
        :type IsAsync: int
        :param _TextMode: 输入文本模式
0: 普通文本
1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本
        :type TextMode: int
        :param _Keyword: 主题词和关键词
        :type Keyword: str
        """
        self._SessionId = None
        self._RefText = None
        self._WorkMode = None
        self._EvalMode = None
        self._ScoreCoeff = None
        self._SoeAppId = None
        self._IsLongLifeSession = None
        self._StorageMode = None
        self._SentenceInfoEnabled = None
        self._ServerType = None
        self._IsAsync = None
        self._TextMode = None
        self._Keyword = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RefText(self):
        return self._RefText

    @RefText.setter
    def RefText(self, RefText):
        self._RefText = RefText

    @property
    def WorkMode(self):
        return self._WorkMode

    @WorkMode.setter
    def WorkMode(self, WorkMode):
        self._WorkMode = WorkMode

    @property
    def EvalMode(self):
        return self._EvalMode

    @EvalMode.setter
    def EvalMode(self, EvalMode):
        self._EvalMode = EvalMode

    @property
    def ScoreCoeff(self):
        return self._ScoreCoeff

    @ScoreCoeff.setter
    def ScoreCoeff(self, ScoreCoeff):
        self._ScoreCoeff = ScoreCoeff

    @property
    def SoeAppId(self):
        return self._SoeAppId

    @SoeAppId.setter
    def SoeAppId(self, SoeAppId):
        self._SoeAppId = SoeAppId

    @property
    def IsLongLifeSession(self):
        return self._IsLongLifeSession

    @IsLongLifeSession.setter
    def IsLongLifeSession(self, IsLongLifeSession):
        self._IsLongLifeSession = IsLongLifeSession

    @property
    def StorageMode(self):
        return self._StorageMode

    @StorageMode.setter
    def StorageMode(self, StorageMode):
        self._StorageMode = StorageMode

    @property
    def SentenceInfoEnabled(self):
        return self._SentenceInfoEnabled

    @SentenceInfoEnabled.setter
    def SentenceInfoEnabled(self, SentenceInfoEnabled):
        self._SentenceInfoEnabled = SentenceInfoEnabled

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def IsAsync(self):
        return self._IsAsync

    @IsAsync.setter
    def IsAsync(self, IsAsync):
        self._IsAsync = IsAsync

    @property
    def TextMode(self):
        return self._TextMode

    @TextMode.setter
    def TextMode(self, TextMode):
        self._TextMode = TextMode

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RefText = params.get("RefText")
        self._WorkMode = params.get("WorkMode")
        self._EvalMode = params.get("EvalMode")
        self._ScoreCoeff = params.get("ScoreCoeff")
        self._SoeAppId = params.get("SoeAppId")
        self._IsLongLifeSession = params.get("IsLongLifeSession")
        self._StorageMode = params.get("StorageMode")
        self._SentenceInfoEnabled = params.get("SentenceInfoEnabled")
        self._ServerType = params.get("ServerType")
        self._IsAsync = params.get("IsAsync")
        self._TextMode = params.get("TextMode")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitOralProcessResponse(AbstractModel):
    """InitOralProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 语音段唯一标识，一个完整语音一个SessionId
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class Keyword(AbstractModel):
    """评测关键词

    """

    def __init__(self):
        r"""
        :param _RefText: 被评估语音对应的文本，句子模式下不超过 20个单词或者中文文字，段落模式不超过 120个单词或者中文文字，中文文字需使用 utf-8 编码，自由说模式RefText可以不填。如需要在单词模式和句子模式下使用自定义音素，可以通过设置 TextMode 使用[音素标注](https://cloud.tencent.com/document/product/884/33698)。
        :type RefText: str
        :param _EvalMode: 评估模式，0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。
        :type EvalMode: int
        :param _ScoreCoeff: 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段
        :type ScoreCoeff: float
        :param _ServerType: 评估语言，0：英文，1：中文。
ServerType不填默认为0
        :type ServerType: int
        :param _TextMode: 输入文本模式，0: 普通文本，1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本。
        :type TextMode: int
        """
        self._RefText = None
        self._EvalMode = None
        self._ScoreCoeff = None
        self._ServerType = None
        self._TextMode = None

    @property
    def RefText(self):
        return self._RefText

    @RefText.setter
    def RefText(self, RefText):
        self._RefText = RefText

    @property
    def EvalMode(self):
        return self._EvalMode

    @EvalMode.setter
    def EvalMode(self, EvalMode):
        self._EvalMode = EvalMode

    @property
    def ScoreCoeff(self):
        return self._ScoreCoeff

    @ScoreCoeff.setter
    def ScoreCoeff(self, ScoreCoeff):
        self._ScoreCoeff = ScoreCoeff

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def TextMode(self):
        return self._TextMode

    @TextMode.setter
    def TextMode(self, TextMode):
        self._TextMode = TextMode


    def _deserialize(self, params):
        self._RefText = params.get("RefText")
        self._EvalMode = params.get("EvalMode")
        self._ScoreCoeff = params.get("ScoreCoeff")
        self._ServerType = params.get("ServerType")
        self._TextMode = params.get("TextMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordEvaluateRequest(AbstractModel):
    """KeywordEvaluate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，非流式模式时无意义。
注意：序号上限为3000，不能超过上限。
        :type SeqId: int
        :param _IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param _VoiceFileType: 语音文件类型
1: raw/pcm
2: wav
3: mp3
4: speex
[音频上传格式](https://cloud.tencent.com/document/product/884/56132)
        :type VoiceFileType: int
        :param _VoiceEncodeType: 语音编码类型
1:pcm
        :type VoiceEncodeType: int
        :param _UserVoiceData: 当前语音数据, 编码格式要求为BASE64且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数）。格式要求参考[音频上传格式](https://cloud.tencent.com/document/product/884/56132)
流式模式下需要将语音数据进行分片处理，参考：[分片大小设置](https://cloud.tencent.com/document/product/884/78985#.E5.88.86.E7.89.87.E5.A4.A7.E5.B0.8F.E8.AE.BE.E7.BD.AE.E4.B8.BA.E5.A4.9A.E5.A4.A7.E6.AF.94.E8.BE.83.E5.90.88.E9.80.82.3F)
如何进行流式分片参考：[流式评测](https://cloud.tencent.com/document/product/884/78824#.E6.B5.81.E5.BC.8F.E8.AF.84.E6.B5.8B)
        :type UserVoiceData: str
        :param _SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param _Keywords: 关键词列表
        :type Keywords: list of Keyword
        :param _SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。使用指南：[业务应用](https://cloud.tencent.com/document/product/884/78824#.E4.B8.9A.E5.8A.A1.E5.BA.94.E7.94.A8)
        :type SoeAppId: str
        :param _IsQuery: 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 评估结果。
        :type IsQuery: int
        """
        self._SeqId = None
        self._IsEnd = None
        self._VoiceFileType = None
        self._VoiceEncodeType = None
        self._UserVoiceData = None
        self._SessionId = None
        self._Keywords = None
        self._SoeAppId = None
        self._IsQuery = None

    @property
    def SeqId(self):
        return self._SeqId

    @SeqId.setter
    def SeqId(self, SeqId):
        self._SeqId = SeqId

    @property
    def IsEnd(self):
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def VoiceFileType(self):
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType

    @property
    def VoiceEncodeType(self):
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def UserVoiceData(self):
        return self._UserVoiceData

    @UserVoiceData.setter
    def UserVoiceData(self, UserVoiceData):
        self._UserVoiceData = UserVoiceData

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def SoeAppId(self):
        return self._SoeAppId

    @SoeAppId.setter
    def SoeAppId(self, SoeAppId):
        self._SoeAppId = SoeAppId

    @property
    def IsQuery(self):
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery


    def _deserialize(self, params):
        self._SeqId = params.get("SeqId")
        self._IsEnd = params.get("IsEnd")
        self._VoiceFileType = params.get("VoiceFileType")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._UserVoiceData = params.get("UserVoiceData")
        self._SessionId = params.get("SessionId")
        if params.get("Keywords") is not None:
            self._Keywords = []
            for item in params.get("Keywords"):
                obj = Keyword()
                obj._deserialize(item)
                self._Keywords.append(obj)
        self._SoeAppId = params.get("SoeAppId")
        self._IsQuery = params.get("IsQuery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordEvaluateResponse(AbstractModel):
    """KeywordEvaluate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeywordScores: 关键词得分
        :type KeywordScores: list of KeywordScore
        :param _SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeywordScores = None
        self._SessionId = None
        self._RequestId = None

    @property
    def KeywordScores(self):
        return self._KeywordScores

    @KeywordScores.setter
    def KeywordScores(self, KeywordScores):
        self._KeywordScores = KeywordScores

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeywordScores") is not None:
            self._KeywordScores = []
            for item in params.get("KeywordScores"):
                obj = KeywordScore()
                obj._deserialize(item)
                self._KeywordScores.append(obj)
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class KeywordScore(AbstractModel):
    """关键词得分

    """

    def __init__(self):
        r"""
        :param _Keyword: 关键词
        :type Keyword: str
        :param _PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。当为流式模式且请求中IsEnd未置1时，取值无意义。
        :type PronAccuracy: float
        :param _PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronFluency: float
        :param _PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronCompletion: float
        :param _Words: 详细发音评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Words: list of WordRsp
        :param _SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracy）× 完整度（PronCompletion）×（2 - 完整度（PronCompletion）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        """
        self._Keyword = None
        self._PronAccuracy = None
        self._PronFluency = None
        self._PronCompletion = None
        self._Words = None
        self._SuggestedScore = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PronAccuracy(self):
        return self._PronAccuracy

    @PronAccuracy.setter
    def PronAccuracy(self, PronAccuracy):
        self._PronAccuracy = PronAccuracy

    @property
    def PronFluency(self):
        return self._PronFluency

    @PronFluency.setter
    def PronFluency(self, PronFluency):
        self._PronFluency = PronFluency

    @property
    def PronCompletion(self):
        return self._PronCompletion

    @PronCompletion.setter
    def PronCompletion(self, PronCompletion):
        self._PronCompletion = PronCompletion

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def SuggestedScore(self):
        return self._SuggestedScore

    @SuggestedScore.setter
    def SuggestedScore(self, SuggestedScore):
        self._SuggestedScore = SuggestedScore


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._PronAccuracy = params.get("PronAccuracy")
        self._PronFluency = params.get("PronFluency")
        self._PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self._Words.append(obj)
        self._SuggestedScore = params.get("SuggestedScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneInfo(AbstractModel):
    """单音节评价结果

    """

    def __init__(self):
        r"""
        :param _MemBeginTime: 当前音节语音起始时间点，单位为ms
        :type MemBeginTime: int
        :param _MemEndTime: 当前音节语音终止时间点，单位为ms
        :type MemEndTime: int
        :param _PronAccuracy: 音节发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配
        :type PronAccuracy: float
        :param _DetectedStress: 当前音节是否检测为重音
        :type DetectedStress: bool
        :param _Phone: 当前音节，当前评测识别的音素
        :type Phone: str
        :param _Stress: 当前音节是否应为重音
        :type Stress: bool
        :param _ReferencePhone: 参考音素，在单词诊断模式下，代表标准音素
        :type ReferencePhone: str
        :param _MatchTag: 当前词与输入语句的匹配情况，0：匹配单词、1：新增单词、2：缺少单词、3：错读的词、4：未录入单词。
        :type MatchTag: int
        :param _ReferenceLetter: 参考字符，在单词诊断模式下，代表音素对应的原始文本
        :type ReferenceLetter: str
        """
        self._MemBeginTime = None
        self._MemEndTime = None
        self._PronAccuracy = None
        self._DetectedStress = None
        self._Phone = None
        self._Stress = None
        self._ReferencePhone = None
        self._MatchTag = None
        self._ReferenceLetter = None

    @property
    def MemBeginTime(self):
        return self._MemBeginTime

    @MemBeginTime.setter
    def MemBeginTime(self, MemBeginTime):
        self._MemBeginTime = MemBeginTime

    @property
    def MemEndTime(self):
        return self._MemEndTime

    @MemEndTime.setter
    def MemEndTime(self, MemEndTime):
        self._MemEndTime = MemEndTime

    @property
    def PronAccuracy(self):
        return self._PronAccuracy

    @PronAccuracy.setter
    def PronAccuracy(self, PronAccuracy):
        self._PronAccuracy = PronAccuracy

    @property
    def DetectedStress(self):
        return self._DetectedStress

    @DetectedStress.setter
    def DetectedStress(self, DetectedStress):
        self._DetectedStress = DetectedStress

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Stress(self):
        return self._Stress

    @Stress.setter
    def Stress(self, Stress):
        self._Stress = Stress

    @property
    def ReferencePhone(self):
        return self._ReferencePhone

    @ReferencePhone.setter
    def ReferencePhone(self, ReferencePhone):
        self._ReferencePhone = ReferencePhone

    @property
    def MatchTag(self):
        return self._MatchTag

    @MatchTag.setter
    def MatchTag(self, MatchTag):
        self._MatchTag = MatchTag

    @property
    def ReferenceLetter(self):
        return self._ReferenceLetter

    @ReferenceLetter.setter
    def ReferenceLetter(self, ReferenceLetter):
        self._ReferenceLetter = ReferenceLetter


    def _deserialize(self, params):
        self._MemBeginTime = params.get("MemBeginTime")
        self._MemEndTime = params.get("MemEndTime")
        self._PronAccuracy = params.get("PronAccuracy")
        self._DetectedStress = params.get("DetectedStress")
        self._Phone = params.get("Phone")
        self._Stress = params.get("Stress")
        self._ReferencePhone = params.get("ReferencePhone")
        self._MatchTag = params.get("MatchTag")
        self._ReferenceLetter = params.get("ReferenceLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceInfo(AbstractModel):
    """语音过程中断句的中间结果

    """

    def __init__(self):
        r"""
        :param _SentenceId: 句子序号，在段落、自由说模式下有效，表示断句序号，最后的综合结果的为-1.
        :type SentenceId: int
        :param _Words: 详细发音评估结果
        :type Words: list of WordRsp
        :param _PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。
        :type PronAccuracy: float
        :param _PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronFluency: float
        :param _PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronCompletion: float
        :param _SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracyfloat）* 完整度（PronCompletionfloat）*（2 - 完整度（PronCompletionfloat）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        :param _RefTextId: 匹配候选文本的序号，在句子多分支、情景对 话、段落模式下表示匹配到的文本序号
注意：此字段可能返回 null，表示取不到有效值。
        :type RefTextId: int
        :param _KeyWordHits: 主题词命中标志，0表示没命中，1表示命中
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordHits: list of float
        :param _UnKeyWordHits: 负向主题词命中标志，0表示没命中，1表示命中
注意：此字段可能返回 null，表示取不到有效值。
        :type UnKeyWordHits: list of float
        """
        self._SentenceId = None
        self._Words = None
        self._PronAccuracy = None
        self._PronFluency = None
        self._PronCompletion = None
        self._SuggestedScore = None
        self._RefTextId = None
        self._KeyWordHits = None
        self._UnKeyWordHits = None

    @property
    def SentenceId(self):
        return self._SentenceId

    @SentenceId.setter
    def SentenceId(self, SentenceId):
        self._SentenceId = SentenceId

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def PronAccuracy(self):
        return self._PronAccuracy

    @PronAccuracy.setter
    def PronAccuracy(self, PronAccuracy):
        self._PronAccuracy = PronAccuracy

    @property
    def PronFluency(self):
        return self._PronFluency

    @PronFluency.setter
    def PronFluency(self, PronFluency):
        self._PronFluency = PronFluency

    @property
    def PronCompletion(self):
        return self._PronCompletion

    @PronCompletion.setter
    def PronCompletion(self, PronCompletion):
        self._PronCompletion = PronCompletion

    @property
    def SuggestedScore(self):
        return self._SuggestedScore

    @SuggestedScore.setter
    def SuggestedScore(self, SuggestedScore):
        self._SuggestedScore = SuggestedScore

    @property
    def RefTextId(self):
        return self._RefTextId

    @RefTextId.setter
    def RefTextId(self, RefTextId):
        self._RefTextId = RefTextId

    @property
    def KeyWordHits(self):
        return self._KeyWordHits

    @KeyWordHits.setter
    def KeyWordHits(self, KeyWordHits):
        self._KeyWordHits = KeyWordHits

    @property
    def UnKeyWordHits(self):
        return self._UnKeyWordHits

    @UnKeyWordHits.setter
    def UnKeyWordHits(self, UnKeyWordHits):
        self._UnKeyWordHits = UnKeyWordHits


    def _deserialize(self, params):
        self._SentenceId = params.get("SentenceId")
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self._Words.append(obj)
        self._PronAccuracy = params.get("PronAccuracy")
        self._PronFluency = params.get("PronFluency")
        self._PronCompletion = params.get("PronCompletion")
        self._SuggestedScore = params.get("SuggestedScore")
        self._RefTextId = params.get("RefTextId")
        self._KeyWordHits = params.get("KeyWordHits")
        self._UnKeyWordHits = params.get("UnKeyWordHits")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tone(AbstractModel):
    """中文声调检测结果

    """

    def __init__(self):
        r"""
        :param _Valid: 检测结果是否有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Valid: bool
        :param _RefTone: 文本标准声调，数值范围[-1,1,2,3,4]
注意：此字段可能返回 null，表示取不到有效值。
        :type RefTone: int
        :param _HypothesisTone: 实际发音声调，数值范围[-1,1,2,3,4]
注意：此字段可能返回 null，表示取不到有效值。
        :type HypothesisTone: int
        """
        self._Valid = None
        self._RefTone = None
        self._HypothesisTone = None

    @property
    def Valid(self):
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid

    @property
    def RefTone(self):
        return self._RefTone

    @RefTone.setter
    def RefTone(self, RefTone):
        self._RefTone = RefTone

    @property
    def HypothesisTone(self):
        return self._HypothesisTone

    @HypothesisTone.setter
    def HypothesisTone(self, HypothesisTone):
        self._HypothesisTone = HypothesisTone


    def _deserialize(self, params):
        self._Valid = params.get("Valid")
        self._RefTone = params.get("RefTone")
        self._HypothesisTone = params.get("HypothesisTone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitOralProcessRequest(AbstractModel):
    """TransmitOralProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
注意：序号上限为3000，不能超过上限。
        :type SeqId: int
        :param _IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param _VoiceFileType: 1: raw/pcm
2: wav
3: mp3
4: speex
[音频上传格式](https://cloud.tencent.com/document/product/884/56132)
        :type VoiceFileType: int
        :param _VoiceEncodeType: 语音编码类型
1:pcm
        :type VoiceEncodeType: int
        :param _UserVoiceData: 当前语音数据, 编码格式要求为BASE64且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数）。格式要求参考[音频上传格式](https://cloud.tencent.com/document/product/884/56132)
流式模式下需要将语音数据进行分片处理，参考：[分片大小设置](https://cloud.tencent.com/document/product/884/78985#.E5.88.86.E7.89.87.E5.A4.A7.E5.B0.8F.E8.AE.BE.E7.BD.AE.E4.B8.BA.E5.A4.9A.E5.A4.A7.E6.AF.94.E8.BE.83.E5.90.88.E9.80.82.3F)
如何进行流式分片参考：[流式评测](https://cloud.tencent.com/document/product/884/78824#.E6.B5.81.E5.BC.8F.E8.AF.84.E6.B5.8B)
        :type UserVoiceData: str
        :param _SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param _SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。使用指南：[业务应用](https://cloud.tencent.com/document/product/884/78824#.E4.B8.9A.E5.8A.A1.E5.BA.94.E7.94.A8)
        :type SoeAppId: str
        :param _IsLongLifeSession: 长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度。当InitOralProcess接口调用时此项为1时，此项必填1才可生效。
        :type IsLongLifeSession: int
        :param _IsQuery: 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 的评估结果。
        :type IsQuery: int
        """
        self._SeqId = None
        self._IsEnd = None
        self._VoiceFileType = None
        self._VoiceEncodeType = None
        self._UserVoiceData = None
        self._SessionId = None
        self._SoeAppId = None
        self._IsLongLifeSession = None
        self._IsQuery = None

    @property
    def SeqId(self):
        return self._SeqId

    @SeqId.setter
    def SeqId(self, SeqId):
        self._SeqId = SeqId

    @property
    def IsEnd(self):
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def VoiceFileType(self):
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType

    @property
    def VoiceEncodeType(self):
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def UserVoiceData(self):
        return self._UserVoiceData

    @UserVoiceData.setter
    def UserVoiceData(self, UserVoiceData):
        self._UserVoiceData = UserVoiceData

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SoeAppId(self):
        return self._SoeAppId

    @SoeAppId.setter
    def SoeAppId(self, SoeAppId):
        self._SoeAppId = SoeAppId

    @property
    def IsLongLifeSession(self):
        return self._IsLongLifeSession

    @IsLongLifeSession.setter
    def IsLongLifeSession(self, IsLongLifeSession):
        self._IsLongLifeSession = IsLongLifeSession

    @property
    def IsQuery(self):
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery


    def _deserialize(self, params):
        self._SeqId = params.get("SeqId")
        self._IsEnd = params.get("IsEnd")
        self._VoiceFileType = params.get("VoiceFileType")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._UserVoiceData = params.get("UserVoiceData")
        self._SessionId = params.get("SessionId")
        self._SoeAppId = params.get("SoeAppId")
        self._IsLongLifeSession = params.get("IsLongLifeSession")
        self._IsQuery = params.get("IsQuery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitOralProcessResponse(AbstractModel):
    """TransmitOralProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。当为流式模式且请求中IsEnd未置1时，取值无意义。
        :type PronAccuracy: float
        :param _PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义。取值无意义时，值为-1
        :type PronFluency: float
        :param _PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式或自由说模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义。取值无意义时，值为-1
        :type PronCompletion: float
        :param _Words: 详细发音评估结果
        :type Words: list of WordRsp
        :param _SessionId: 语音段唯一标识，一段语音一个SessionId
        :type SessionId: str
        :param _AudioUrl: 已废弃，不再保存语音音频文件下载地址
        :type AudioUrl: str
        :param _SentenceInfoSet: 断句中间结果，中间结果是局部最优而非全局最优的结果，所以中间结果有可能和最终整体结果对应部分不一致；中间结果的输出便于客户端UI更新；待用户发音完全结束后，系统会给出一个综合所有句子的整体结果。
        :type SentenceInfoSet: list of SentenceInfo
        :param _Status: 评估 session 状态，“Evaluating"：评估中、"Failed"：评估失败、"Finished"：评估完成
        :type Status: str
        :param _SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracy）× 完整度（PronCompletion）×（2 - 完整度（PronCompletion）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        :param _RefTextId: 匹配候选文本的序号，在句子多分支、情景对 话、段落模式下表示匹配到的文本序号
注意：此字段可能返回 null，表示取不到有效值。
        :type RefTextId: int
        :param _KeyWordHits: 主题词命中标志，0表示没命中，1表示命中
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordHits: list of float
        :param _UnKeyWordHits: 负向主题词命中标志，0表示没命中，1表示命中
注意：此字段可能返回 null，表示取不到有效值。
        :type UnKeyWordHits: list of float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PronAccuracy = None
        self._PronFluency = None
        self._PronCompletion = None
        self._Words = None
        self._SessionId = None
        self._AudioUrl = None
        self._SentenceInfoSet = None
        self._Status = None
        self._SuggestedScore = None
        self._RefTextId = None
        self._KeyWordHits = None
        self._UnKeyWordHits = None
        self._RequestId = None

    @property
    def PronAccuracy(self):
        return self._PronAccuracy

    @PronAccuracy.setter
    def PronAccuracy(self, PronAccuracy):
        self._PronAccuracy = PronAccuracy

    @property
    def PronFluency(self):
        return self._PronFluency

    @PronFluency.setter
    def PronFluency(self, PronFluency):
        self._PronFluency = PronFluency

    @property
    def PronCompletion(self):
        return self._PronCompletion

    @PronCompletion.setter
    def PronCompletion(self, PronCompletion):
        self._PronCompletion = PronCompletion

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AudioUrl(self):
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def SentenceInfoSet(self):
        return self._SentenceInfoSet

    @SentenceInfoSet.setter
    def SentenceInfoSet(self, SentenceInfoSet):
        self._SentenceInfoSet = SentenceInfoSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuggestedScore(self):
        return self._SuggestedScore

    @SuggestedScore.setter
    def SuggestedScore(self, SuggestedScore):
        self._SuggestedScore = SuggestedScore

    @property
    def RefTextId(self):
        return self._RefTextId

    @RefTextId.setter
    def RefTextId(self, RefTextId):
        self._RefTextId = RefTextId

    @property
    def KeyWordHits(self):
        return self._KeyWordHits

    @KeyWordHits.setter
    def KeyWordHits(self, KeyWordHits):
        self._KeyWordHits = KeyWordHits

    @property
    def UnKeyWordHits(self):
        return self._UnKeyWordHits

    @UnKeyWordHits.setter
    def UnKeyWordHits(self, UnKeyWordHits):
        self._UnKeyWordHits = UnKeyWordHits

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PronAccuracy = params.get("PronAccuracy")
        self._PronFluency = params.get("PronFluency")
        self._PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self._Words.append(obj)
        self._SessionId = params.get("SessionId")
        self._AudioUrl = params.get("AudioUrl")
        if params.get("SentenceInfoSet") is not None:
            self._SentenceInfoSet = []
            for item in params.get("SentenceInfoSet"):
                obj = SentenceInfo()
                obj._deserialize(item)
                self._SentenceInfoSet.append(obj)
        self._Status = params.get("Status")
        self._SuggestedScore = params.get("SuggestedScore")
        self._RefTextId = params.get("RefTextId")
        self._KeyWordHits = params.get("KeyWordHits")
        self._UnKeyWordHits = params.get("UnKeyWordHits")
        self._RequestId = params.get("RequestId")


class TransmitOralProcessWithInitRequest(AbstractModel):
    """TransmitOralProcessWithInit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
注意：序号上限为3000，不能超过上限。
        :type SeqId: int
        :param _IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param _VoiceFileType: 语音文件类型
1: raw/pcm
2: wav
3: mp3
4: speex
语音文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败。
[音频上传格式](https://cloud.tencent.com/document/product/884/56132)
        :type VoiceFileType: int
        :param _VoiceEncodeType: 语音编码类型
1:pcm
        :type VoiceEncodeType: int
        :param _UserVoiceData: 当前语音数据, 编码格式要求为BASE64且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数）。格式要求参考[音频上传格式](https://cloud.tencent.com/document/product/884/56132)
流式模式下需要将语音数据进行分片处理，参考：[分片大小设置](https://cloud.tencent.com/document/product/884/78985#.E5.88.86.E7.89.87.E5.A4.A7.E5.B0.8F.E8.AE.BE.E7.BD.AE.E4.B8.BA.E5.A4.9A.E5.A4.A7.E6.AF.94.E8.BE.83.E5.90.88.E9.80.82.3F)
如何进行流式分片参考：[流式测试](https://cloud.tencent.com/document/product/884/78824#.E6.B5.81.E5.BC.8F.E8.AF.84.E6.B5.8B)
        :type UserVoiceData: str
        :param _SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param _RefText: 被评估语音对应的文本，仅支持中文和英文。
句子模式下不超过个 30 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式RefText可以不填。
关于RefText的文本键入要求，请参考[评测模式介绍](https://cloud.tencent.com/document/product/884/56131)。
如需要在评测模式下使用自定义注音（支持中英文），可以通过设置「TextMode」参数实现，设置方式请参考[音素标注](https://cloud.tencent.com/document/product/884/33698)。
        :type RefText: str
        :param _WorkMode: 语音输入模式
0：流式分片
1：非流式一次性评估
推荐使用流式分片传输。
        :type WorkMode: int
        :param _EvalMode: 评测模式
0：单词/单字模式（中文评测模式下为单字模式）
1：句子模式
2：段落模式
3：自由说模式
4：单词音素纠错模式
5：情景评测模式
6：句子多分支评测模式
7：单词实时评测模式
8：拼音评测模式
关于每种评测模式的详细介绍，以及适用场景，请参考[评测模式介绍](https://cloud.tencent.com/document/product/884/56131)。
        :type EvalMode: int
        :param _ScoreCoeff: 评价苛刻指数。取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数。
1.0：适用于最小年龄段用户，一般对应儿童应用场景；
4.0：适用于最高年龄段用户，一般对应成人严格打分场景。
苛刻度影响范围参考：[苛刻度影响范围](https://cloud.tencent.com/document/product/884/78824#.E8.8B.9B.E5.88.BB.E5.BA.A6)
        :type ScoreCoeff: float
        :param _SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。使用指南：[业务应用](https://cloud.tencent.com/document/product/884/78824#.E4.B8.9A.E5.8A.A1.E5.BA.94.E7.94.A8)
        :type SoeAppId: str
        :param _StorageMode: 音频存储模式，此参数已废弃，无需设置，设置与否都默认为0不存储；
注：有存储需求的用户建议自行存储至腾讯云COS[对象存储](https://cloud.tencent.com/product/cos)使用。
        :type StorageMode: int
        :param _SentenceInfoEnabled: 输出断句中间结果标识
0：不输出（默认）
1：输出，通过设置该参数
可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcessWithInit请求返回结果 SentenceInfoSet 字段。
        :type SentenceInfoEnabled: int
        :param _ServerType: 评估语言
0：英文（默认）
1：中文
        :type ServerType: int
        :param _IsAsync: 异步模式标识
0：同步模式（默认）
1：异步模式（一般情况不建议使用异步模式，如需使用参考：[异步轮询](https://cloud.tencent.com/document/product/884/78824#.E7.BB.93.E6.9E.9C.E6.9F.A5.E8.AF.A2)）
可选值参考[服务模式](https://cloud.tencent.com/document/product/884/33697)。
        :type IsAsync: int
        :param _IsQuery: 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 评估结果。
        :type IsQuery: int
        :param _TextMode: 输入文本模式
0: 普通文本（默认）
1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本
        :type TextMode: int
        :param _Keyword: 主题词和关键词
        :type Keyword: str
        """
        self._SeqId = None
        self._IsEnd = None
        self._VoiceFileType = None
        self._VoiceEncodeType = None
        self._UserVoiceData = None
        self._SessionId = None
        self._RefText = None
        self._WorkMode = None
        self._EvalMode = None
        self._ScoreCoeff = None
        self._SoeAppId = None
        self._StorageMode = None
        self._SentenceInfoEnabled = None
        self._ServerType = None
        self._IsAsync = None
        self._IsQuery = None
        self._TextMode = None
        self._Keyword = None

    @property
    def SeqId(self):
        return self._SeqId

    @SeqId.setter
    def SeqId(self, SeqId):
        self._SeqId = SeqId

    @property
    def IsEnd(self):
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def VoiceFileType(self):
        return self._VoiceFileType

    @VoiceFileType.setter
    def VoiceFileType(self, VoiceFileType):
        self._VoiceFileType = VoiceFileType

    @property
    def VoiceEncodeType(self):
        return self._VoiceEncodeType

    @VoiceEncodeType.setter
    def VoiceEncodeType(self, VoiceEncodeType):
        self._VoiceEncodeType = VoiceEncodeType

    @property
    def UserVoiceData(self):
        return self._UserVoiceData

    @UserVoiceData.setter
    def UserVoiceData(self, UserVoiceData):
        self._UserVoiceData = UserVoiceData

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RefText(self):
        return self._RefText

    @RefText.setter
    def RefText(self, RefText):
        self._RefText = RefText

    @property
    def WorkMode(self):
        return self._WorkMode

    @WorkMode.setter
    def WorkMode(self, WorkMode):
        self._WorkMode = WorkMode

    @property
    def EvalMode(self):
        return self._EvalMode

    @EvalMode.setter
    def EvalMode(self, EvalMode):
        self._EvalMode = EvalMode

    @property
    def ScoreCoeff(self):
        return self._ScoreCoeff

    @ScoreCoeff.setter
    def ScoreCoeff(self, ScoreCoeff):
        self._ScoreCoeff = ScoreCoeff

    @property
    def SoeAppId(self):
        return self._SoeAppId

    @SoeAppId.setter
    def SoeAppId(self, SoeAppId):
        self._SoeAppId = SoeAppId

    @property
    def StorageMode(self):
        return self._StorageMode

    @StorageMode.setter
    def StorageMode(self, StorageMode):
        self._StorageMode = StorageMode

    @property
    def SentenceInfoEnabled(self):
        return self._SentenceInfoEnabled

    @SentenceInfoEnabled.setter
    def SentenceInfoEnabled(self, SentenceInfoEnabled):
        self._SentenceInfoEnabled = SentenceInfoEnabled

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def IsAsync(self):
        return self._IsAsync

    @IsAsync.setter
    def IsAsync(self, IsAsync):
        self._IsAsync = IsAsync

    @property
    def IsQuery(self):
        return self._IsQuery

    @IsQuery.setter
    def IsQuery(self, IsQuery):
        self._IsQuery = IsQuery

    @property
    def TextMode(self):
        return self._TextMode

    @TextMode.setter
    def TextMode(self, TextMode):
        self._TextMode = TextMode

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._SeqId = params.get("SeqId")
        self._IsEnd = params.get("IsEnd")
        self._VoiceFileType = params.get("VoiceFileType")
        self._VoiceEncodeType = params.get("VoiceEncodeType")
        self._UserVoiceData = params.get("UserVoiceData")
        self._SessionId = params.get("SessionId")
        self._RefText = params.get("RefText")
        self._WorkMode = params.get("WorkMode")
        self._EvalMode = params.get("EvalMode")
        self._ScoreCoeff = params.get("ScoreCoeff")
        self._SoeAppId = params.get("SoeAppId")
        self._StorageMode = params.get("StorageMode")
        self._SentenceInfoEnabled = params.get("SentenceInfoEnabled")
        self._ServerType = params.get("ServerType")
        self._IsAsync = params.get("IsAsync")
        self._IsQuery = params.get("IsQuery")
        self._TextMode = params.get("TextMode")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitOralProcessWithInitResponse(AbstractModel):
    """TransmitOralProcessWithInit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。当为流式模式且请求中IsEnd未置1时，取值无意义。
        :type PronAccuracy: float
        :param _PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义。取值无意义时，值为-1
        :type PronFluency: float
        :param _PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式或自由说模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义。取值无意义时，值为-1
        :type PronCompletion: float
        :param _Words: 详细发音评估结果
        :type Words: list of WordRsp
        :param _SessionId: 语音段唯一标识，一段语音一个SessionId
        :type SessionId: str
        :param _AudioUrl: 已废弃，不再保存语音音频文件下载地址
        :type AudioUrl: str
        :param _SentenceInfoSet: 断句中间结果，中间结果是局部最优而非全局最优的结果，所以中间结果有可能和最终整体结果对应部分不一致；中间结果的输出便于客户端UI更新；待用户发音完全结束后，系统会给出一个综合所有句子的整体结果。
        :type SentenceInfoSet: list of SentenceInfo
        :param _Status: 评估 session 状态，“Evaluating"：评估中、"Failed"：评估失败、"Finished"：评估完成
        :type Status: str
        :param _SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracy）× 完整度（PronCompletion）×（2 - 完整度（PronCompletion）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        :param _RefTextId: 匹配候选文本的序号，在句子多分支、情景对 话、段落模式下表示匹配到的文本序号
注意：此字段可能返回 null，表示取不到有效值。
        :type RefTextId: int
        :param _KeyWordHits: 主题词命中标志，0表示没命中，1表示命中
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyWordHits: list of float
        :param _UnKeyWordHits: 负向主题词命中标志，0表示没命中，1表示命中
注意：此字段可能返回 null，表示取不到有效值。
        :type UnKeyWordHits: list of float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PronAccuracy = None
        self._PronFluency = None
        self._PronCompletion = None
        self._Words = None
        self._SessionId = None
        self._AudioUrl = None
        self._SentenceInfoSet = None
        self._Status = None
        self._SuggestedScore = None
        self._RefTextId = None
        self._KeyWordHits = None
        self._UnKeyWordHits = None
        self._RequestId = None

    @property
    def PronAccuracy(self):
        return self._PronAccuracy

    @PronAccuracy.setter
    def PronAccuracy(self, PronAccuracy):
        self._PronAccuracy = PronAccuracy

    @property
    def PronFluency(self):
        return self._PronFluency

    @PronFluency.setter
    def PronFluency(self, PronFluency):
        self._PronFluency = PronFluency

    @property
    def PronCompletion(self):
        return self._PronCompletion

    @PronCompletion.setter
    def PronCompletion(self, PronCompletion):
        self._PronCompletion = PronCompletion

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AudioUrl(self):
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def SentenceInfoSet(self):
        return self._SentenceInfoSet

    @SentenceInfoSet.setter
    def SentenceInfoSet(self, SentenceInfoSet):
        self._SentenceInfoSet = SentenceInfoSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuggestedScore(self):
        return self._SuggestedScore

    @SuggestedScore.setter
    def SuggestedScore(self, SuggestedScore):
        self._SuggestedScore = SuggestedScore

    @property
    def RefTextId(self):
        return self._RefTextId

    @RefTextId.setter
    def RefTextId(self, RefTextId):
        self._RefTextId = RefTextId

    @property
    def KeyWordHits(self):
        return self._KeyWordHits

    @KeyWordHits.setter
    def KeyWordHits(self, KeyWordHits):
        self._KeyWordHits = KeyWordHits

    @property
    def UnKeyWordHits(self):
        return self._UnKeyWordHits

    @UnKeyWordHits.setter
    def UnKeyWordHits(self, UnKeyWordHits):
        self._UnKeyWordHits = UnKeyWordHits

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PronAccuracy = params.get("PronAccuracy")
        self._PronFluency = params.get("PronFluency")
        self._PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self._Words.append(obj)
        self._SessionId = params.get("SessionId")
        self._AudioUrl = params.get("AudioUrl")
        if params.get("SentenceInfoSet") is not None:
            self._SentenceInfoSet = []
            for item in params.get("SentenceInfoSet"):
                obj = SentenceInfo()
                obj._deserialize(item)
                self._SentenceInfoSet.append(obj)
        self._Status = params.get("Status")
        self._SuggestedScore = params.get("SuggestedScore")
        self._RefTextId = params.get("RefTextId")
        self._KeyWordHits = params.get("KeyWordHits")
        self._UnKeyWordHits = params.get("UnKeyWordHits")
        self._RequestId = params.get("RequestId")


class WordRsp(AbstractModel):
    """单词评分细则

    """

    def __init__(self):
        r"""
        :param _MemBeginTime: 当前单词语音起始时间点，单位为ms，该字段段落模式下无意义。
        :type MemBeginTime: int
        :param _MemEndTime: 当前单词语音终止时间点，单位为ms，该字段段落模式下无意义。
        :type MemEndTime: int
        :param _PronAccuracy: 单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配
        :type PronAccuracy: float
        :param _PronFluency: 单词发音流利度，取值范围[0, 1]
        :type PronFluency: float
        :param _Word: 当前词
        :type Word: str
        :param _MatchTag: 当前词与输入语句的匹配情况，0：匹配单词、1：新增单词、2：缺少单词、3：错读的词、4：未录入单词。
        :type MatchTag: int
        :param _PhoneInfos: 音节评估详情
        :type PhoneInfos: list of PhoneInfo
        :param _ReferenceWord: 参考词，目前为保留字段。
        :type ReferenceWord: str
        :param _KeywordTag: 主题词命中标志，0表示没命中，1表示命中
注意：此字段可能返回 null，表示取不到有效值。
        :type KeywordTag: int
        :param _Tone: 声调检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Tone: :class:`tencentcloud.soe.v20180724.models.Tone`
        """
        self._MemBeginTime = None
        self._MemEndTime = None
        self._PronAccuracy = None
        self._PronFluency = None
        self._Word = None
        self._MatchTag = None
        self._PhoneInfos = None
        self._ReferenceWord = None
        self._KeywordTag = None
        self._Tone = None

    @property
    def MemBeginTime(self):
        return self._MemBeginTime

    @MemBeginTime.setter
    def MemBeginTime(self, MemBeginTime):
        self._MemBeginTime = MemBeginTime

    @property
    def MemEndTime(self):
        return self._MemEndTime

    @MemEndTime.setter
    def MemEndTime(self, MemEndTime):
        self._MemEndTime = MemEndTime

    @property
    def PronAccuracy(self):
        return self._PronAccuracy

    @PronAccuracy.setter
    def PronAccuracy(self, PronAccuracy):
        self._PronAccuracy = PronAccuracy

    @property
    def PronFluency(self):
        return self._PronFluency

    @PronFluency.setter
    def PronFluency(self, PronFluency):
        self._PronFluency = PronFluency

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def MatchTag(self):
        return self._MatchTag

    @MatchTag.setter
    def MatchTag(self, MatchTag):
        self._MatchTag = MatchTag

    @property
    def PhoneInfos(self):
        return self._PhoneInfos

    @PhoneInfos.setter
    def PhoneInfos(self, PhoneInfos):
        self._PhoneInfos = PhoneInfos

    @property
    def ReferenceWord(self):
        return self._ReferenceWord

    @ReferenceWord.setter
    def ReferenceWord(self, ReferenceWord):
        self._ReferenceWord = ReferenceWord

    @property
    def KeywordTag(self):
        return self._KeywordTag

    @KeywordTag.setter
    def KeywordTag(self, KeywordTag):
        self._KeywordTag = KeywordTag

    @property
    def Tone(self):
        return self._Tone

    @Tone.setter
    def Tone(self, Tone):
        self._Tone = Tone


    def _deserialize(self, params):
        self._MemBeginTime = params.get("MemBeginTime")
        self._MemEndTime = params.get("MemEndTime")
        self._PronAccuracy = params.get("PronAccuracy")
        self._PronFluency = params.get("PronFluency")
        self._Word = params.get("Word")
        self._MatchTag = params.get("MatchTag")
        if params.get("PhoneInfos") is not None:
            self._PhoneInfos = []
            for item in params.get("PhoneInfos"):
                obj = PhoneInfo()
                obj._deserialize(item)
                self._PhoneInfos.append(obj)
        self._ReferenceWord = params.get("ReferenceWord")
        self._KeywordTag = params.get("KeywordTag")
        if params.get("Tone") is not None:
            self._Tone = Tone()
            self._Tone._deserialize(params.get("Tone"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        