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


class PostAudioRequest(AbstractModel):
    """PostAudio请求参数结构体

    """

    def __init__(self):
        """
        :param BotId: 机器人标识
        :type BotId: str
        :param EngineModelType: 语音识别引擎类型,{8k_0、16k_0、16k_en}
        :type EngineModelType: str
        :param AsrVoiceFormat: 输入音频文件编码格式。1：wav(pcm)；4：speex(sp)；6：silk
        :type AsrVoiceFormat: int
        :param VoiceId: asr请求Id。长度为16位的字符串，同一句话VoiceId保持一致
        :type VoiceId: str
        :param Seq: 语音分片序列号。同一句话必须从0开始，依次递增
        :type Seq: int
        :param IsEnd: 是否为尾包。传递最后一个语音分片时为true，其他为false
        :type IsEnd: bool
        :param WaveData: 待识别音频字节流
        :type WaveData: str
        :param UserId: 子账户id，每个终端对应一个
        :type UserId: str
        :param BotVersion: 机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotVersion: str
        :param ResultTextFormat: 识别返回文本编码格式	0：UTF-8（默认）；1：GB2312；2：GBK；3：BIG5
        :type ResultTextFormat: int
        :param SessionAttributes: 透传字段，传递给后台
        :type SessionAttributes: str
        :param NeedTts: 是否将机器人回答合成音频并返回url
        :type NeedTts: bool
        :param Volume: 音量大小，范围：[0，10]。默认值为0，代表正常音量
        :type Volume: int
        :param Speed: 语速，范围：[-2，2]。0代表1.0倍
        :type Speed: int
        :param VoiceType: 音色,{0：女声,1:男声}
        :type VoiceType: int
        :param SampleRate: 返回音频的采样率{8k,16k}。默认16k
        :type SampleRate: str
        :param BotEnv: 机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotEnv: str
        :param TtsVoiceFormat: TTS合成音频格式，{0：wav}。该字段在当前版本仅支持取值为0。
        :type TtsVoiceFormat: int
        """
        self.BotId = None
        self.EngineModelType = None
        self.AsrVoiceFormat = None
        self.VoiceId = None
        self.Seq = None
        self.IsEnd = None
        self.WaveData = None
        self.UserId = None
        self.BotVersion = None
        self.ResultTextFormat = None
        self.SessionAttributes = None
        self.NeedTts = None
        self.Volume = None
        self.Speed = None
        self.VoiceType = None
        self.SampleRate = None
        self.BotEnv = None
        self.TtsVoiceFormat = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.EngineModelType = params.get("EngineModelType")
        self.AsrVoiceFormat = params.get("AsrVoiceFormat")
        self.VoiceId = params.get("VoiceId")
        self.Seq = params.get("Seq")
        self.IsEnd = params.get("IsEnd")
        self.WaveData = params.get("WaveData")
        self.UserId = params.get("UserId")
        self.BotVersion = params.get("BotVersion")
        self.ResultTextFormat = params.get("ResultTextFormat")
        self.SessionAttributes = params.get("SessionAttributes")
        self.NeedTts = params.get("NeedTts")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.VoiceType = params.get("VoiceType")
        self.SampleRate = params.get("SampleRate")
        self.BotEnv = params.get("BotEnv")
        self.TtsVoiceFormat = params.get("TtsVoiceFormat")


class PostAudioResponse(AbstractModel):
    """PostAudio返回参数结构体

    """

    def __init__(self):
        """
        :param DialogStatus: 当前会话状态。取值:"start"/"continue"/"complete"
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 匹配到的机器人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 匹配到的意图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param ResponseText: 机器人应答文本
        :type ResponseText: str
        :param SlotInfoList: 语义解析的槽位结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param SessionAttributes: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param Question: 用户说法。该说法是用户原生说法或ASR识别结果，未经过语义优化
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param WaveUrl: tts合成pcm音频存储链接。仅当请求参数NeedTts=true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param WaveData: tts合成pcm音频
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.ResponseText = None
        self.SlotInfoList = None
        self.SessionAttributes = None
        self.Question = None
        self.WaveUrl = None
        self.WaveData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        self.ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.SessionAttributes = params.get("SessionAttributes")
        self.Question = params.get("Question")
        self.WaveUrl = params.get("WaveUrl")
        self.WaveData = params.get("WaveData")
        self.RequestId = params.get("RequestId")


class PostTextRequest(AbstractModel):
    """PostText请求参数结构体

    """

    def __init__(self):
        """
        :param BotId: 机器人标识
        :type BotId: str
        :param InputText: 请求的文本
        :type InputText: str
        :param UserId: 子账户id，每个终端对应一个
        :type UserId: str
        :param BotVersion: 机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotVersion: str
        :param SessionAttributes: 透传字段，传递给后台
        :type SessionAttributes: str
        :param NeedTts: 是否将机器人回答合成音频并返回url
        :type NeedTts: bool
        :param Volume: 音量大小，范围：[0，10]。默认值为0，代表正常音量
        :type Volume: int
        :param Speed: 语速，范围：[-2，2]。0代表1.0倍
        :type Speed: int
        :param VoiceType: 音色,{0：女声,1:男声}
        :type VoiceType: int
        :param SampleRate: 返回音频的采样率{8k,16k}。默认16k
        :type SampleRate: str
        :param BotEnv: 机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotEnv: str
        :param TtsVoiceFormat: TTS合成音频格式，{0：wav}。该字段在当前版本仅支持取值为0。
        :type TtsVoiceFormat: int
        """
        self.BotId = None
        self.InputText = None
        self.UserId = None
        self.BotVersion = None
        self.SessionAttributes = None
        self.NeedTts = None
        self.Volume = None
        self.Speed = None
        self.VoiceType = None
        self.SampleRate = None
        self.BotEnv = None
        self.TtsVoiceFormat = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.InputText = params.get("InputText")
        self.UserId = params.get("UserId")
        self.BotVersion = params.get("BotVersion")
        self.SessionAttributes = params.get("SessionAttributes")
        self.NeedTts = params.get("NeedTts")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.VoiceType = params.get("VoiceType")
        self.SampleRate = params.get("SampleRate")
        self.BotEnv = params.get("BotEnv")
        self.TtsVoiceFormat = params.get("TtsVoiceFormat")


class PostTextResponse(AbstractModel):
    """PostText返回参数结构体

    """

    def __init__(self):
        """
        :param DialogStatus: 当前会话状态。取值:"start"/"continue"/"complete"
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 匹配到的机器人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 匹配到的意图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param ResponseText: 机器人回答
        :type ResponseText: str
        :param SlotInfoList: 语义解析的槽位结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param SessionAttributes: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param Question: 用户说法。该说法是用户原生说法或ASR识别结果，未经过语义优化
        :type Question: str
        :param WaveUrl: tts合成pcm音频存储链接。仅当请求参数NeedTts=true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param WaveData: tts合成的pcm音频。二进制数组经过base64编码(暂时不返回)
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.ResponseText = None
        self.SlotInfoList = None
        self.SessionAttributes = None
        self.Question = None
        self.WaveUrl = None
        self.WaveData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        self.ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.SessionAttributes = params.get("SessionAttributes")
        self.Question = params.get("Question")
        self.WaveUrl = params.get("WaveUrl")
        self.WaveData = params.get("WaveData")
        self.RequestId = params.get("RequestId")


class ResetRequest(AbstractModel):
    """Reset请求参数结构体

    """

    def __init__(self):
        """
        :param BotId: 机器人标识
        :type BotId: str
        :param UserId: 子账户id，每个终端对应一个
        :type UserId: str
        :param BotVersion: 机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotVersion: str
        :param BotEnv: 机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotEnv: str
        """
        self.BotId = None
        self.UserId = None
        self.BotVersion = None
        self.BotEnv = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.UserId = params.get("UserId")
        self.BotVersion = params.get("BotVersion")
        self.BotEnv = params.get("BotEnv")


class ResetResponse(AbstractModel):
    """Reset返回参数结构体

    """

    def __init__(self):
        """
        :param DialogStatus: 当前会话状态。取值:"start"/"continue"/"complete"
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 匹配到的机器人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 匹配到的意图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param ResponseText: 机器人回答
        :type ResponseText: str
        :param SlotInfoList: 语义解析的槽位结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param SessionAttributes: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param Question: 用户说法。该说法是用户原生说法或ASR识别结果，未经过语义优化
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param WaveUrl: tts合成pcm音频存储链接。仅当请求参数NeedTts=true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param WaveData: tts合成的pcm音频。二进制数组经过base64编码(暂时不返回)
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.ResponseText = None
        self.SlotInfoList = None
        self.SessionAttributes = None
        self.Question = None
        self.WaveUrl = None
        self.WaveData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        self.ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.SessionAttributes = params.get("SessionAttributes")
        self.Question = params.get("Question")
        self.WaveUrl = params.get("WaveUrl")
        self.WaveData = params.get("WaveData")
        self.RequestId = params.get("RequestId")


class SlotInfo(AbstractModel):
    """槽位信息

    """

    def __init__(self):
        """
        :param SlotName: 槽位名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotName: str
        :param SlotValue: 槽位值
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotValue: str
        """
        self.SlotName = None
        self.SlotValue = None


    def _deserialize(self, params):
        self.SlotName = params.get("SlotName")
        self.SlotValue = params.get("SlotValue")