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


class InitOralProcessRequest(AbstractModel):
    """InitOralProcess请求参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 语音段唯一标识，一段语音一个SessionId
        :type SessionId: str
        :param RefText: 被评估语音对应的文本，句子模式下不超过个 20 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式该值传空。
        :type RefText: str
        :param WorkMode: 语音输入模式，0：流式分片，1：非流式一次性评估
        :type WorkMode: int
        :param EvalMode: 评估模式，0：词模式，,1：:句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。
        :type EvalMode: int
        :param ScoreCoeff: 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段
        :type ScoreCoeff: float
        :param SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。
        :type SoeAppId: str
        :param IsLongLifeSession: 长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度，且TransmitOralProcess必须同时为1才可生效。
        :type IsLongLifeSession: int
        :param StorageMode: 音频存储模式，0：不存储，1：存储到公共对象存储，输出结果为该会话最后一个分片TransmitOralProcess 返回结果 AudioUrl 字段。
        :type StorageMode: int
        :param SentenceInfoEnabled: 输出断句中间结果标识，0：不输出，1：输出，通过设置该参数，可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。
        :type SentenceInfoEnabled: int
        :param ServerType: 评估语言，0：英文，1：中文。
        :type ServerType: int
        :param IsAsync: 异步模式标识，0：同步模式，1：异步模式。
        :type IsAsync: int
        :param TextMode: 输入文本模式，0: 普通文本，1: 音素结构文本
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


class InitOralProcessResponse(AbstractModel):
    """InitOralProcess返回参数结构体

    """

    def __init__(self):
        """
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


class PhoneInfo(AbstractModel):
    """单音节评价结果

    """

    def __init__(self):
        """
        :param MemBeginTime: 当前音节语音起始时间点，单位为ms
        :type MemBeginTime: int
        :param MemEndTime: 当前音节语音终止时间点，单位为ms
        :type MemEndTime: int
        :param PronAccuracy: 音节发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配
        :type PronAccuracy: float
        :param DetectedStress: 当前音节是否检测为重音
        :type DetectedStress: bool
        :param Phone: 当前音节
        :type Phone: str
        :param Stress: 当前音节是否应为重音
        :type Stress: bool
        """
        self.MemBeginTime = None
        self.MemEndTime = None
        self.PronAccuracy = None
        self.DetectedStress = None
        self.Phone = None
        self.Stress = None


    def _deserialize(self, params):
        self.MemBeginTime = params.get("MemBeginTime")
        self.MemEndTime = params.get("MemEndTime")
        self.PronAccuracy = params.get("PronAccuracy")
        self.DetectedStress = params.get("DetectedStress")
        self.Phone = params.get("Phone")
        self.Stress = params.get("Stress")


class SentenceInfo(AbstractModel):
    """语音过程中断句的中间结果

    """

    def __init__(self):
        """
        :param SentenceId: 句子序号，在段落、自由说模式下有效，表示断句序号，最后的综合结果的为-1.
        :type SentenceId: int
        :param Words: 详细发音评估结果
        :type Words: list of WordRsp
        :param PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值。当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronAccuracy: float
        :param PronFluency: 发音流利度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronFluency: float
        :param PronCompletion: 发音完整度，取值范围[0, 1]，当为词模式时，取值无意义；当为流式模式且请求中IsEnd未置1时，取值无意义
        :type PronCompletion: float
        """
        self.SentenceId = None
        self.Words = None
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None


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


class TransmitOralProcessRequest(AbstractModel):
    """TransmitOralProcess请求参数结构体

    """

    def __init__(self):
        """
        :param SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
        :type SeqId: int
        :param IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param VoiceFileType: 语音文件类型 	1:raw, 2:wav, 3:mp3(三种格式目前仅支持16k采样率16bit编码单声道，如有不一致可能导致评估不准确或失败)。
        :type VoiceFileType: int
        :param VoiceEncodeType: 语音编码类型	1:pcm。
        :type VoiceEncodeType: int
        :param UserVoiceData: 当前数据包数据, 流式模式下数据包大小可以按需设置，数据包大小必须 >= 4K，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :type UserVoiceData: str
        :param SessionId: 语音段唯一标识，一个完整语音一个SessionId。
        :type SessionId: str
        :param SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。
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


class TransmitOralProcessResponse(AbstractModel):
    """TransmitOralProcess返回参数结构体

    """

    def __init__(self):
        """
        :param PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值。当为流式模式且请求中IsEnd未置1时，取值无意义
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
        self.RequestId = params.get("RequestId")


class TransmitOralProcessWithInitRequest(AbstractModel):
    """TransmitOralProcessWithInit请求参数结构体

    """

    def __init__(self):
        """
        :param SeqId: 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
        :type SeqId: int
        :param IsEnd: 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        :type IsEnd: int
        :param VoiceFileType: 语音文件类型 	1:raw, 2:wav, 3:mp3(三种格式目前仅支持16k采样率16bit编码单声道，如有不一致可能导致评估不准确或失败)。
        :type VoiceFileType: int
        :param VoiceEncodeType: 语音编码类型	1:pcm。
        :type VoiceEncodeType: int
        :param UserVoiceData: 当前数据包数据, 流式模式下数据包大小可以按需设置，数据包大小必须 >= 4K，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64。
        :type UserVoiceData: str
        :param SessionId: 语音段唯一标识，一个完整语音一个SessionId。
        :type SessionId: str
        :param RefText: 被评估语音对应的文本，句子模式下不超过个 20 单词或者中文文字，段落模式不超过 120 单词或者中文文字，中文评估使用 utf-8 编码，自由说模式该值传空。
        :type RefText: str
        :param WorkMode: 语音输入模式，0：流式分片，1：非流式一次性评估
        :type WorkMode: int
        :param EvalMode: 评估模式，0：词模式，,1：:句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。
        :type EvalMode: int
        :param ScoreCoeff: 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段
        :type ScoreCoeff: float
        :param SoeAppId: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。
        :type SoeAppId: str
        :param StorageMode: 音频存储模式，0：不存储，1：存储到公共对象存储，输出结果为该会话最后一个分片TransmitOralProcess 返回结果 AudioUrl 字段。
        :type StorageMode: int
        :param SentenceInfoEnabled: 输出断句中间结果标识，0：不输出，1：输出，通过设置该参数，可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。
        :type SentenceInfoEnabled: int
        :param ServerType: 评估语言，0：英文，1：中文。
        :type ServerType: int
        :param IsAsync: 异步模式标识，0：同步模式，1：异步模式。
        :type IsAsync: int
        :param IsQuery: 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 评估结果。
        :type IsQuery: int
        :param TextMode: 输入文本模式，0: 普通文本，1: 音素结构文本
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


class TransmitOralProcessWithInitResponse(AbstractModel):
    """TransmitOralProcessWithInit返回参数结构体

    """

    def __init__(self):
        """
        :param PronAccuracy: 发音精准度，取值范围[-1, 100]，当取-1时指完全不匹配，当为句子模式时，是所有已识别单词准确度的加权平均值。当为流式模式且请求中IsEnd未置1时，取值无意义
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
        self.RequestId = params.get("RequestId")


class WordRsp(AbstractModel):
    """单词评分细则

    """

    def __init__(self):
        """
        :param MemBeginTime: 当前单词语音起始时间点，单位为ms
        :type MemBeginTime: int
        :param MemEndTime: 当前单词语音终止时间点，单位为ms
        :type MemEndTime: int
        :param PronAccuracy: 单词发音准确度，取值范围[-1, 100]，当取-1时指完全不匹配
        :type PronAccuracy: float
        :param PronFluency: 单词发音流利度，取值范围[0, 1]
        :type PronFluency: float
        :param Word: 当前词
        :type Word: str
        :param MatchTag: 当前词与输入语句的匹配情况，0:匹配单词、1：新增单词、2：缺少单词
        :type MatchTag: int
        :param PhoneInfos: 音节评估详情
        :type PhoneInfos: list of PhoneInfo
        """
        self.MemBeginTime = None
        self.MemEndTime = None
        self.PronAccuracy = None
        self.PronFluency = None
        self.Word = None
        self.MatchTag = None
        self.PhoneInfos = None


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