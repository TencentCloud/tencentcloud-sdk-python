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
        :param SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param RefText: 被评估语音对应的文本，仅支持中文和英文。
句子模式下不超过个 30 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式RefText可以不填。
关于RefText的文本键入要求，请参考[评测模式介绍](https://cloud.tencent.com/document/product/884/56131)。
如需要在评测模式下使用自定义注音（支持中英文），可以通过设置「TextMode」参数实现，设置方式请参考[音素标注](https://cloud.tencent.com/document/product/884/33698)。
        :type RefText: str
        :param WorkMode: 语音输入模式
0：流式分片
1：非流式一次性评估
推荐使用流式分片传输。
        :type WorkMode: int
        :param EvalMode: 评测模式
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
        :param ScoreCoeff: 评价苛刻指数。取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数。
1.0：适用于最小年龄段用户，一般对应儿童应用场景；
4.0：适用于最高年龄段用户，一般对应成人严格打分场景。
        :type ScoreCoeff: float
        :param SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。
        :type SoeAppId: str
        :param IsLongLifeSession: 长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度，且TransmitOralProcess必须同时为1才可生效。
        :type IsLongLifeSession: int
        :param StorageMode: 音频存储模式，此参数已废弃，无需设置，设置与否都默认为0不存储；
注：有存储需求的用户建议自行存储至腾讯云COS[对象存储](https://cloud.tencent.com/product/cos)使用。
        :type StorageMode: int
        :param SentenceInfoEnabled: 输出断句中间结果标识
0：不输出
1：输出，通过设置该参数
可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。
        :type SentenceInfoEnabled: int
        :param ServerType: 评估语言
0：英文
1：中文
ServerType不填默认为0
        :type ServerType: int
        :param IsAsync: 异步模式标识
0：同步模式
1：异步模式（一般情况不建议使用异步模式）
可选值参考[服务模式](https://cloud.tencent.com/document/product/884/33697)。
        :type IsAsync: int
        :param TextMode: 输入文本模式
0: 普通文本
1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本
2：音素注册模式（提工单注册需要使用音素的单词）。
        :type TextMode: int
        """
        self.SessionId = None
        self.RefText = None
        self.WorkMode = None
        self.EvalMode = None
        self.ScoreCoeff = None
        self.SoeAppId = None
        self.IsLongLifeSession = None
        self.StorageMode = None
        self.SentenceInfoEnabled = None
        self.ServerType = None
        self.IsAsync = None
        self.TextMode = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.RefText = params.get("RefText")
        self.WorkMode = params.get("WorkMode")
        self.EvalMode = params.get("EvalMode")
        self.ScoreCoeff = params.get("ScoreCoeff")
        self.SoeAppId = params.get("SoeAppId")
        self.IsLongLifeSession = params.get("IsLongLifeSession")
        self.StorageMode = params.get("StorageMode")
        self.SentenceInfoEnabled = params.get("SentenceInfoEnabled")
        self.ServerType = params.get("ServerType")
        self.IsAsync = params.get("IsAsync")
        self.TextMode = params.get("TextMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitOralProcessResponse(AbstractModel):
    """InitOralProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: 语音段唯一标识，一个完整语音一个SessionId
        :type SessionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.RequestId = params.get("RequestId")


class Keyword(AbstractModel):
    """评测关键词

    """

    def __init__(self):
        r"""
        :param RefText: 被评估语音对应的文本，句子模式下不超过个 20 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式RefText可以不填。如需要在单词模式和句子模式下使用自定义音素，可以通过设置 TextMode 使用[音素标注](https://cloud.tencent.com/document/product/884/33698)。
        :type RefText: str
        :param EvalMode: 评估模式，0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。
        :type EvalMode: int
        :param ScoreCoeff: 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段
        :type ScoreCoeff: float
        :param ServerType: 评估语言，0：英文，1：中文。
ServerType不填默认传0
        :type ServerType: int
        :param TextMode: 输入文本模式，0: 普通文本，1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本。
        :type TextMode: int
        """
        self.RefText = None
        self.EvalMode = None
        self.ScoreCoeff = None
        self.ServerType = None
        self.TextMode = None


    def _deserialize(self, params):
        self.RefText = params.get("RefText")
        self.EvalMode = params.get("EvalMode")
        self.ScoreCoeff = params.get("ScoreCoeff")
        self.ServerType = params.get("ServerType")
        self.TextMode = params.get("TextMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordEvaluateRequest(AbstractModel):
    """KeywordEvaluate请求参数结构体

    """

    def __init__(self):
        r"""
        :param SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
注意：序号上限为3000，不能超过上限。
        :type SeqId: int
        :param IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param VoiceFileType: 语音文件类型
1: raw
2: wav
3: mp3
4: speex
语音文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败。
        :type VoiceFileType: int
        :param VoiceEncodeType: 语音编码类型
1:pcm
        :type VoiceEncodeType: int
        :param UserVoiceData: 当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为1k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :type UserVoiceData: str
        :param SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param Keywords: 关键词列表
        :type Keywords: list of Keyword
        :param SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。
        :type SoeAppId: str
        :param IsQuery: 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 评估结果。
        :type IsQuery: int
        """
        self.SeqId = None
        self.IsEnd = None
        self.VoiceFileType = None
        self.VoiceEncodeType = None
        self.UserVoiceData = None
        self.SessionId = None
        self.Keywords = None
        self.SoeAppId = None
        self.IsQuery = None


    def _deserialize(self, params):
        self.SeqId = params.get("SeqId")
        self.IsEnd = params.get("IsEnd")
        self.VoiceFileType = params.get("VoiceFileType")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.UserVoiceData = params.get("UserVoiceData")
        self.SessionId = params.get("SessionId")
        if params.get("Keywords") is not None:
            self.Keywords = []
            for item in params.get("Keywords"):
                obj = Keyword()
                obj._deserialize(item)
                self.Keywords.append(obj)
        self.SoeAppId = params.get("SoeAppId")
        self.IsQuery = params.get("IsQuery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordEvaluateResponse(AbstractModel):
    """KeywordEvaluate返回参数结构体

    """

    def __init__(self):
        r"""
        :param KeywordScores: 关键词得分
        :type KeywordScores: list of KeywordScore
        :param SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeywordScores = None
        self.SessionId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeywordScores") is not None:
            self.KeywordScores = []
            for item in params.get("KeywordScores"):
                obj = KeywordScore()
                obj._deserialize(item)
                self.KeywordScores.append(obj)
        self.SessionId = params.get("SessionId")
        self.RequestId = params.get("RequestId")


class KeywordScore(AbstractModel):
    """关键词得分

    """

    def __init__(self):
        r"""
        :param Keyword: 关键词
        :type Keyword: str
        :param PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。当为流式模式且请求中IsEnd未置1时，取值无意义。
        :type PronAccuracy: float
        :param PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronFluency: float
        :param PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronCompletion: float
        :param Words: 详细发音评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Words: list of WordRsp
        :param SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracy）× 完整度（PronCompletion）×（2 - 完整度（PronCompletion）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        """
        self.Keyword = None
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None
        self.Words = None
        self.SuggestedScore = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SuggestedScore = params.get("SuggestedScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneInfo(AbstractModel):
    """单音节评价结果

    """

    def __init__(self):
        r"""
        :param MemBeginTime: 当前音节语音起始时间点，单位为ms
        :type MemBeginTime: int
        :param MemEndTime: 当前音节语音终止时间点，单位为ms
        :type MemEndTime: int
        :param PronAccuracy: 音节发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配
        :type PronAccuracy: float
        :param DetectedStress: 当前音节是否检测为重音
        :type DetectedStress: bool
        :param Phone: 当前音节，当前评测识别的音素
        :type Phone: str
        :param Stress: 当前音节是否应为重音
        :type Stress: bool
        :param ReferencePhone: 参考音素，在单词诊断模式下，代表标准音素
        :type ReferencePhone: str
        :param MatchTag: 当前词与输入语句的匹配情况，0：匹配单词、1：新增单词、2：缺少单词、3：错读的词、4：未录入单词。
        :type MatchTag: int
        :param ReferenceLetter: 参考字符，在单词诊断模式下，代表音素对应的原始文本
        :type ReferenceLetter: str
        """
        self.MemBeginTime = None
        self.MemEndTime = None
        self.PronAccuracy = None
        self.DetectedStress = None
        self.Phone = None
        self.Stress = None
        self.ReferencePhone = None
        self.MatchTag = None
        self.ReferenceLetter = None


    def _deserialize(self, params):
        self.MemBeginTime = params.get("MemBeginTime")
        self.MemEndTime = params.get("MemEndTime")
        self.PronAccuracy = params.get("PronAccuracy")
        self.DetectedStress = params.get("DetectedStress")
        self.Phone = params.get("Phone")
        self.Stress = params.get("Stress")
        self.ReferencePhone = params.get("ReferencePhone")
        self.MatchTag = params.get("MatchTag")
        self.ReferenceLetter = params.get("ReferenceLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceInfo(AbstractModel):
    """语音过程中断句的中间结果

    """

    def __init__(self):
        r"""
        :param SentenceId: 句子序号，在段落、自由说模式下有效，表示断句序号，最后的综合结果的为-1.
        :type SentenceId: int
        :param Words: 详细发音评估结果
        :type Words: list of WordRsp
        :param PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。
        :type PronAccuracy: float
        :param PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronFluency: float
        :param PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronCompletion: float
        :param SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracyfloat）* 完整度（PronCompletionfloat）*（2 - 完整度（PronCompletionfloat）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        """
        self.SentenceId = None
        self.Words = None
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None
        self.SuggestedScore = None


    def _deserialize(self, params):
        self.SentenceId = params.get("SentenceId")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self.Words.append(obj)
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.PronCompletion = params.get("PronCompletion")
        self.SuggestedScore = params.get("SuggestedScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitOralProcessRequest(AbstractModel):
    """TransmitOralProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
注意：序号上限为3000，不能超过上限。
        :type SeqId: int
        :param IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param VoiceFileType: 语音文件类型
1: raw
2: wav
3: mp3
4: speex
语音文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败。
        :type VoiceFileType: int
        :param VoiceEncodeType: 语音编码类型
1:pcm
        :type VoiceEncodeType: int
        :param UserVoiceData: 当前数据包数据, 流式模式下数据包大小可以按需设置，在网络稳定时，分片大小建议设置0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :type UserVoiceData: str
        :param SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。
        :type SoeAppId: str
        :param IsLongLifeSession: 长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度。当InitOralProcess接口调用时此项为1时，此项必填1才可生效。
        :type IsLongLifeSession: int
        :param IsQuery: 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 的评估结果。
        :type IsQuery: int
        """
        self.SeqId = None
        self.IsEnd = None
        self.VoiceFileType = None
        self.VoiceEncodeType = None
        self.UserVoiceData = None
        self.SessionId = None
        self.SoeAppId = None
        self.IsLongLifeSession = None
        self.IsQuery = None


    def _deserialize(self, params):
        self.SeqId = params.get("SeqId")
        self.IsEnd = params.get("IsEnd")
        self.VoiceFileType = params.get("VoiceFileType")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.UserVoiceData = params.get("UserVoiceData")
        self.SessionId = params.get("SessionId")
        self.SoeAppId = params.get("SoeAppId")
        self.IsLongLifeSession = params.get("IsLongLifeSession")
        self.IsQuery = params.get("IsQuery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitOralProcessResponse(AbstractModel):
    """TransmitOralProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。当为流式模式且请求中IsEnd未置1时，取值无意义。
        :type PronAccuracy: float
        :param PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronFluency: float
        :param PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronCompletion: float
        :param Words: 详细发音评估结果
        :type Words: list of WordRsp
        :param SessionId: 语音段唯一标识，一段语音一个SessionId
        :type SessionId: str
        :param AudioUrl: 保存语音音频文件下载地址
        :type AudioUrl: str
        :param SentenceInfoSet: 断句中间结果，中间结果是局部最优而非全局最优的结果，所以中间结果有可能和最终整体结果对应部分不一致；中间结果的输出便于客户端UI更新；待用户发音完全结束后，系统会给出一个综合所有句子的整体结果。
        :type SentenceInfoSet: list of SentenceInfo
        :param Status: 评估 session 状态，“Evaluating"：评估中、"Failed"：评估失败、"Finished"：评估完成
        :type Status: str
        :param SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracy）× 完整度（PronCompletion）×（2 - 完整度（PronCompletion）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None
        self.Words = None
        self.SessionId = None
        self.AudioUrl = None
        self.SentenceInfoSet = None
        self.Status = None
        self.SuggestedScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SessionId = params.get("SessionId")
        self.AudioUrl = params.get("AudioUrl")
        if params.get("SentenceInfoSet") is not None:
            self.SentenceInfoSet = []
            for item in params.get("SentenceInfoSet"):
                obj = SentenceInfo()
                obj._deserialize(item)
                self.SentenceInfoSet.append(obj)
        self.Status = params.get("Status")
        self.SuggestedScore = params.get("SuggestedScore")
        self.RequestId = params.get("RequestId")


class TransmitOralProcessWithInitRequest(AbstractModel):
    """TransmitOralProcessWithInit请求参数结构体

    """

    def __init__(self):
        r"""
        :param SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
注意：序号上限为3000，不能超过上限。
        :type SeqId: int
        :param IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param VoiceFileType: 语音文件类型
1: raw
2: wav
3: mp3
4: speex
语音文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败。
        :type VoiceFileType: int
        :param VoiceEncodeType: 语音编码类型
1:pcm
        :type VoiceEncodeType: int
        :param UserVoiceData: 当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为1k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :type UserVoiceData: str
        :param SessionId: 语音段唯一标识，一段完整语音使用一个SessionId，不同语音段的评测需要使用不同的SessionId。一般使用uuid(通用唯一识别码)来作为它的值，要尽量保证SessionId的唯一性。
        :type SessionId: str
        :param RefText: 被评估语音对应的文本，仅支持中文和英文。
句子模式下不超过个 30 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式RefText可以不填。
关于RefText的文本键入要求，请参考[评测模式介绍](https://cloud.tencent.com/document/product/884/56131)。
如需要在评测模式下使用自定义注音（支持中英文），可以通过设置「TextMode」参数实现，设置方式请参考[音素标注](https://cloud.tencent.com/document/product/884/33698)。
        :type RefText: str
        :param WorkMode: 语音输入模式
0：流式分片
1：非流式一次性评估
推荐使用流式分片传输。
        :type WorkMode: int
        :param EvalMode: 评测模式
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
        :param ScoreCoeff: 评价苛刻指数。取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数。
1.0：适用于最小年龄段用户，一般对应儿童应用场景；
4.0：适用于最高年龄段用户，一般对应成人严格打分场景。
        :type ScoreCoeff: float
        :param SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。如果没有新建SoeAppId，请勿填入该参数，否则会报欠费错误。
        :type SoeAppId: str
        :param StorageMode: 音频存储模式，此参数已废弃，无需设置，设置与否都默认为0不存储；
注：有存储需求的用户建议自行存储至腾讯云COS[对象存储](https://cloud.tencent.com/product/cos)使用。
        :type StorageMode: int
        :param SentenceInfoEnabled: 输出断句中间结果标识
0：不输出
1：输出，通过设置该参数
可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。
        :type SentenceInfoEnabled: int
        :param ServerType: 评估语言
0：英文
1：中文
ServerType不填默认为0
        :type ServerType: int
        :param IsAsync: 异步模式标识
0：同步模式
1：异步模式（一般情况不建议使用异步模式）
可选值参考[服务模式](https://cloud.tencent.com/document/product/884/33697)。
        :type IsAsync: int
        :param IsQuery: 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 评估结果。
        :type IsQuery: int
        :param TextMode: 输入文本模式
0: 普通文本
1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本
2：音素注册模式（提工单注册需要使用音素的单词）。
        :type TextMode: int
        """
        self.SeqId = None
        self.IsEnd = None
        self.VoiceFileType = None
        self.VoiceEncodeType = None
        self.UserVoiceData = None
        self.SessionId = None
        self.RefText = None
        self.WorkMode = None
        self.EvalMode = None
        self.ScoreCoeff = None
        self.SoeAppId = None
        self.StorageMode = None
        self.SentenceInfoEnabled = None
        self.ServerType = None
        self.IsAsync = None
        self.IsQuery = None
        self.TextMode = None


    def _deserialize(self, params):
        self.SeqId = params.get("SeqId")
        self.IsEnd = params.get("IsEnd")
        self.VoiceFileType = params.get("VoiceFileType")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.UserVoiceData = params.get("UserVoiceData")
        self.SessionId = params.get("SessionId")
        self.RefText = params.get("RefText")
        self.WorkMode = params.get("WorkMode")
        self.EvalMode = params.get("EvalMode")
        self.ScoreCoeff = params.get("ScoreCoeff")
        self.SoeAppId = params.get("SoeAppId")
        self.StorageMode = params.get("StorageMode")
        self.SentenceInfoEnabled = params.get("SentenceInfoEnabled")
        self.ServerType = params.get("ServerType")
        self.IsAsync = params.get("IsAsync")
        self.IsQuery = params.get("IsQuery")
        self.TextMode = params.get("TextMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransmitOralProcessWithInitResponse(AbstractModel):
    """TransmitOralProcessWithInit返回参数结构体

    """

    def __init__(self):
        r"""
        :param PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值，在reftext中但未识别出来的词不计入分数中。当为流式模式且请求中IsEnd未置1时，取值无意义。
        :type PronAccuracy: float
        :param PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronFluency: float
        :param PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronCompletion: float
        :param Words: 详细发音评估结果
        :type Words: list of WordRsp
        :param SessionId: 语音段唯一标识，一段语音一个SessionId
        :type SessionId: str
        :param AudioUrl: 保存语音音频文件下载地址
        :type AudioUrl: str
        :param SentenceInfoSet: 断句中间结果，中间结果是局部最优而非全局最优的结果，所以中间结果有可能和最终整体结果对应部分不一致；中间结果的输出便于客户端UI更新；待用户发音完全结束后，系统会给出一个综合所有句子的整体结果。
        :type SentenceInfoSet: list of SentenceInfo
        :param Status: 评估 session 状态，“Evaluating"：评估中、"Failed"：评估失败、"Finished"：评估完成
        :type Status: str
        :param SuggestedScore: 建议评分，取值范围[0,100]，评分方式为建议评分 = 准确度（PronAccuracy）× 完整度（PronCompletion）×（2 - 完整度（PronCompletion）），如若评分策略不符合请参考Words数组中的详细分数自定义评分逻辑。
        :type SuggestedScore: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None
        self.Words = None
        self.SessionId = None
        self.AudioUrl = None
        self.SentenceInfoSet = None
        self.Status = None
        self.SuggestedScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SessionId = params.get("SessionId")
        self.AudioUrl = params.get("AudioUrl")
        if params.get("SentenceInfoSet") is not None:
            self.SentenceInfoSet = []
            for item in params.get("SentenceInfoSet"):
                obj = SentenceInfo()
                obj._deserialize(item)
                self.SentenceInfoSet.append(obj)
        self.Status = params.get("Status")
        self.SuggestedScore = params.get("SuggestedScore")
        self.RequestId = params.get("RequestId")


class WordRsp(AbstractModel):
    """单词评分细则

    """

    def __init__(self):
        r"""
        :param MemBeginTime: 当前单词语音起始时间点，单位为ms，该字段段落模式下无意义。
        :type MemBeginTime: int
        :param MemEndTime: 当前单词语音终止时间点，单位为ms，该字段段落模式下无意义。
        :type MemEndTime: int
        :param PronAccuracy: 单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配
        :type PronAccuracy: float
        :param PronFluency: 单词发音流利度，取值范围[0, 1]
        :type PronFluency: float
        :param Word: 当前词
        :type Word: str
        :param MatchTag: 当前词与输入语句的匹配情况，0：匹配单词、1：新增单词、2：缺少单词、3：错读的词、4：未录入单词。
        :type MatchTag: int
        :param PhoneInfos: 音节评估详情
        :type PhoneInfos: list of PhoneInfo
        :param ReferenceWord: 参考词，目前为保留字段。
        :type ReferenceWord: str
        """
        self.MemBeginTime = None
        self.MemEndTime = None
        self.PronAccuracy = None
        self.PronFluency = None
        self.Word = None
        self.MatchTag = None
        self.PhoneInfos = None
        self.ReferenceWord = None


    def _deserialize(self, params):
        self.MemBeginTime = params.get("MemBeginTime")
        self.MemEndTime = params.get("MemEndTime")
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.Word = params.get("Word")
        self.MatchTag = params.get("MatchTag")
        if params.get("PhoneInfos") is not None:
            self.PhoneInfos = []
            for item in params.get("PhoneInfos"):
                obj = PhoneInfo()
                obj._deserialize(item)
                self.PhoneInfos.append(obj)
        self.ReferenceWord = params.get("ReferenceWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        