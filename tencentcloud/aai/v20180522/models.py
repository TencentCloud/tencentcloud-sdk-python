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


class ChatRequest(AbstractModel):
    r"""Chat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 聊天输入文本
        :type Text: str
        :param _ProjectId: 腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :type ProjectId: int
        :param _User: json格式，比如 {"id":"test","gender":"male"}。记录当前与机器人交互的用户id，非必须但强烈建议传入，否则多轮聊天功能会受影响
        :type User: str
        """
        self._Text = None
        self._ProjectId = None
        self._User = None

    @property
    def Text(self):
        r"""聊天输入文本
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def ProjectId(self):
        r"""腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def User(self):
        r"""json格式，比如 {"id":"test","gender":"male"}。记录当前与机器人交互的用户id，非必须但强烈建议传入，否则多轮聊天功能会受影响
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._ProjectId = params.get("ProjectId")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatResponse(AbstractModel):
    r"""Chat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Answer: 聊天输出文本
        :type Answer: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Answer = None
        self._RequestId = None

    @property
    def Answer(self):
        r"""聊天输出文本
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Answer = params.get("Answer")
        self._RequestId = params.get("RequestId")


class SentenceRecognitionRequest(AbstractModel):
    r"""SentenceRecognition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :type ProjectId: int
        :param _SubServiceType: 子服务类型。2，一句话识别。
        :type SubServiceType: int
        :param _EngSerViceType: 引擎类型。8k：电话 8k 通用模型；16k：16k 通用模型。只支持单声道音频识别。
        :type EngSerViceType: str
        :param _SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
        :type SourceType: int
        :param _VoiceFormat: 识别音频的音频格式（支持mp3,wav）。
        :type VoiceFormat: str
        :param _UsrAudioKey: 用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。
        :type UsrAudioKey: str
        :param _Url: 语音 URL，公网可下载。当 SourceType 值为 0 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。
        :type Url: str
        :param _Data: 语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于600kB。
        :type Data: str
        :param _DataLen: 数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。
        :type DataLen: int
        """
        self._ProjectId = None
        self._SubServiceType = None
        self._EngSerViceType = None
        self._SourceType = None
        self._VoiceFormat = None
        self._UsrAudioKey = None
        self._Url = None
        self._Data = None
        self._DataLen = None

    @property
    def ProjectId(self):
        r"""腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubServiceType(self):
        r"""子服务类型。2，一句话识别。
        :rtype: int
        """
        return self._SubServiceType

    @SubServiceType.setter
    def SubServiceType(self, SubServiceType):
        self._SubServiceType = SubServiceType

    @property
    def EngSerViceType(self):
        r"""引擎类型。8k：电话 8k 通用模型；16k：16k 通用模型。只支持单声道音频识别。
        :rtype: str
        """
        return self._EngSerViceType

    @EngSerViceType.setter
    def EngSerViceType(self, EngSerViceType):
        self._EngSerViceType = EngSerViceType

    @property
    def SourceType(self):
        r"""语音数据来源。0：语音 URL；1：语音数据（post body）。
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def VoiceFormat(self):
        r"""识别音频的音频格式（支持mp3,wav）。
        :rtype: str
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def UsrAudioKey(self):
        r"""用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。
        :rtype: str
        """
        return self._UsrAudioKey

    @UsrAudioKey.setter
    def UsrAudioKey(self, UsrAudioKey):
        self._UsrAudioKey = UsrAudioKey

    @property
    def Url(self):
        r"""语音 URL，公网可下载。当 SourceType 值为 0 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Data(self):
        r"""语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于600kB。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DataLen(self):
        r"""数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。
        :rtype: int
        """
        return self._DataLen

    @DataLen.setter
    def DataLen(self, DataLen):
        self._DataLen = DataLen


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SubServiceType = params.get("SubServiceType")
        self._EngSerViceType = params.get("EngSerViceType")
        self._SourceType = params.get("SourceType")
        self._VoiceFormat = params.get("VoiceFormat")
        self._UsrAudioKey = params.get("UsrAudioKey")
        self._Url = params.get("Url")
        self._Data = params.get("Data")
        self._DataLen = params.get("DataLen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceRecognitionResponse(AbstractModel):
    r"""SentenceRecognition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 识别结果。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""识别结果。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class SimultaneousInterpretingRequest(AbstractModel):
    r"""SimultaneousInterpreting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :type ProjectId: int
        :param _SubServiceType: 子服务类型。0：离线语音识别。1：实时流式识别，2，一句话识别。3：同传。
        :type SubServiceType: int
        :param _RecEngineModelType: 识别引擎类型。8k_zh： 8k 中文会场模型；16k_zh：16k 中文会场模型，8k_en： 8k 英文会场模型；16k_en：16k 英文会场模型。当前仅支持16K。
        :type RecEngineModelType: str
        :param _Data: 语音数据，要base64编码。
        :type Data: str
        :param _DataLen: 数据长度。
        :type DataLen: int
        :param _VoiceId: 声音id，标识一句话。
        :type VoiceId: str
        :param _IsEnd: 是否是一句话的结束。
        :type IsEnd: int
        :param _VoiceFormat: 声音编码的格式1:pcm，4:speex，6:silk，默认为1。
        :type VoiceFormat: int
        :param _OpenTranslate: 是否需要翻译结果，1表示需要翻译，0是不需要。
        :type OpenTranslate: int
        :param _SourceLanguage: 如果需要翻译，表示源语言类型，可取值：zh，en。
        :type SourceLanguage: str
        :param _TargetLanguage: 如果需要翻译，表示目标语言类型，可取值：zh，en。
        :type TargetLanguage: str
        :param _Seq: 表明当前语音分片的索引，从0开始
        :type Seq: int
        """
        self._ProjectId = None
        self._SubServiceType = None
        self._RecEngineModelType = None
        self._Data = None
        self._DataLen = None
        self._VoiceId = None
        self._IsEnd = None
        self._VoiceFormat = None
        self._OpenTranslate = None
        self._SourceLanguage = None
        self._TargetLanguage = None
        self._Seq = None

    @property
    def ProjectId(self):
        r"""腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubServiceType(self):
        r"""子服务类型。0：离线语音识别。1：实时流式识别，2，一句话识别。3：同传。
        :rtype: int
        """
        return self._SubServiceType

    @SubServiceType.setter
    def SubServiceType(self, SubServiceType):
        self._SubServiceType = SubServiceType

    @property
    def RecEngineModelType(self):
        r"""识别引擎类型。8k_zh： 8k 中文会场模型；16k_zh：16k 中文会场模型，8k_en： 8k 英文会场模型；16k_en：16k 英文会场模型。当前仅支持16K。
        :rtype: str
        """
        return self._RecEngineModelType

    @RecEngineModelType.setter
    def RecEngineModelType(self, RecEngineModelType):
        self._RecEngineModelType = RecEngineModelType

    @property
    def Data(self):
        r"""语音数据，要base64编码。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DataLen(self):
        r"""数据长度。
        :rtype: int
        """
        return self._DataLen

    @DataLen.setter
    def DataLen(self, DataLen):
        self._DataLen = DataLen

    @property
    def VoiceId(self):
        r"""声音id，标识一句话。
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def IsEnd(self):
        r"""是否是一句话的结束。
        :rtype: int
        """
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def VoiceFormat(self):
        r"""声音编码的格式1:pcm，4:speex，6:silk，默认为1。
        :rtype: int
        """
        return self._VoiceFormat

    @VoiceFormat.setter
    def VoiceFormat(self, VoiceFormat):
        self._VoiceFormat = VoiceFormat

    @property
    def OpenTranslate(self):
        r"""是否需要翻译结果，1表示需要翻译，0是不需要。
        :rtype: int
        """
        return self._OpenTranslate

    @OpenTranslate.setter
    def OpenTranslate(self, OpenTranslate):
        self._OpenTranslate = OpenTranslate

    @property
    def SourceLanguage(self):
        r"""如果需要翻译，表示源语言类型，可取值：zh，en。
        :rtype: str
        """
        return self._SourceLanguage

    @SourceLanguage.setter
    def SourceLanguage(self, SourceLanguage):
        self._SourceLanguage = SourceLanguage

    @property
    def TargetLanguage(self):
        r"""如果需要翻译，表示目标语言类型，可取值：zh，en。
        :rtype: str
        """
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def Seq(self):
        r"""表明当前语音分片的索引，从0开始
        :rtype: int
        """
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SubServiceType = params.get("SubServiceType")
        self._RecEngineModelType = params.get("RecEngineModelType")
        self._Data = params.get("Data")
        self._DataLen = params.get("DataLen")
        self._VoiceId = params.get("VoiceId")
        self._IsEnd = params.get("IsEnd")
        self._VoiceFormat = params.get("VoiceFormat")
        self._OpenTranslate = params.get("OpenTranslate")
        self._SourceLanguage = params.get("SourceLanguage")
        self._TargetLanguage = params.get("TargetLanguage")
        self._Seq = params.get("Seq")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimultaneousInterpretingResponse(AbstractModel):
    r"""SimultaneousInterpreting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AsrText: 语音识别的结果
        :type AsrText: str
        :param _NmtText: 机器翻译的结果
        :type NmtText: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AsrText = None
        self._NmtText = None
        self._RequestId = None

    @property
    def AsrText(self):
        r"""语音识别的结果
        :rtype: str
        """
        return self._AsrText

    @AsrText.setter
    def AsrText(self, AsrText):
        self._AsrText = AsrText

    @property
    def NmtText(self):
        r"""机器翻译的结果
        :rtype: str
        """
        return self._NmtText

    @NmtText.setter
    def NmtText(self, NmtText):
        self._NmtText = NmtText

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsrText = params.get("AsrText")
        self._NmtText = params.get("NmtText")
        self._RequestId = params.get("RequestId")


class TextToVoiceRequest(AbstractModel):
    r"""TextToVoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 合成语音的源文本，按UTF-8编码统一计算。
中文最大支持100个汉字（全角标点符号算一个汉字）；英文最大支持400个字母（半角标点符号算一个字母）。包含空格等字符时需要url encode再传输。
        :type Text: str
        :param _SessionId: 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复。
        :type SessionId: str
        :param _ModelType: 模型类型，1-默认模型。
        :type ModelType: int
        :param _Volume: 音量大小，范围：[0，10]，分别对应11个等级的音量，默认为0，代表正常音量。没有静音选项。
输入除以上整数之外的其他参数不生效，按默认值处理。
        :type Volume: float
        :param _Speed: 语速，范围：[-2，2]，分别对应不同语速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（默认）</li><li>1代表1.2倍</li><li>2代表1.5倍</li>输入除以上整数之外的其他参数不生效，按默认值处理。
        :type Speed: float
        :param _ProjectId: 项目id，用户自定义，默认为0。
        :type ProjectId: int
        :param _VoiceType: 音色<li>0-亲和女声(默认)</li><li>1-亲和男声</li><li>2-成熟男声</li><li>3-活力男声</li><li>4-温暖女声</li><li>5-情感女声</li><li>6-情感男声</li>
        :type VoiceType: int
        :param _PrimaryLanguage: 主语言类型：<li>1-中文（默认）</li><li>2-英文</li>
        :type PrimaryLanguage: int
        :param _SampleRate: 音频采样率：<li>16000：16k（默认）</li><li>8000：8k</li>
        :type SampleRate: int
        :param _Codec: 返回音频格式，可取值：wav（默认），mp3
        :type Codec: str
        """
        self._Text = None
        self._SessionId = None
        self._ModelType = None
        self._Volume = None
        self._Speed = None
        self._ProjectId = None
        self._VoiceType = None
        self._PrimaryLanguage = None
        self._SampleRate = None
        self._Codec = None

    @property
    def Text(self):
        r"""合成语音的源文本，按UTF-8编码统一计算。
中文最大支持100个汉字（全角标点符号算一个汉字）；英文最大支持400个字母（半角标点符号算一个字母）。包含空格等字符时需要url encode再传输。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def SessionId(self):
        r"""一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ModelType(self):
        r"""模型类型，1-默认模型。
        :rtype: int
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def Volume(self):
        r"""音量大小，范围：[0，10]，分别对应11个等级的音量，默认为0，代表正常音量。没有静音选项。
输入除以上整数之外的其他参数不生效，按默认值处理。
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Speed(self):
        r"""语速，范围：[-2，2]，分别对应不同语速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（默认）</li><li>1代表1.2倍</li><li>2代表1.5倍</li>输入除以上整数之外的其他参数不生效，按默认值处理。
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def ProjectId(self):
        r"""项目id，用户自定义，默认为0。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VoiceType(self):
        r"""音色<li>0-亲和女声(默认)</li><li>1-亲和男声</li><li>2-成熟男声</li><li>3-活力男声</li><li>4-温暖女声</li><li>5-情感女声</li><li>6-情感男声</li>
        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def PrimaryLanguage(self):
        r"""主语言类型：<li>1-中文（默认）</li><li>2-英文</li>
        :rtype: int
        """
        return self._PrimaryLanguage

    @PrimaryLanguage.setter
    def PrimaryLanguage(self, PrimaryLanguage):
        self._PrimaryLanguage = PrimaryLanguage

    @property
    def SampleRate(self):
        r"""音频采样率：<li>16000：16k（默认）</li><li>8000：8k</li>
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Codec(self):
        r"""返回音频格式，可取值：wav（默认），mp3
        :rtype: str
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._SessionId = params.get("SessionId")
        self._ModelType = params.get("ModelType")
        self._Volume = params.get("Volume")
        self._Speed = params.get("Speed")
        self._ProjectId = params.get("ProjectId")
        self._VoiceType = params.get("VoiceType")
        self._PrimaryLanguage = params.get("PrimaryLanguage")
        self._SampleRate = params.get("SampleRate")
        self._Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceResponse(AbstractModel):
    r"""TextToVoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Audio: base64编码的wav/mp3音频数据
        :type Audio: str
        :param _SessionId: 一次请求对应一个SessionId
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Audio = None
        self._SessionId = None
        self._RequestId = None

    @property
    def Audio(self):
        r"""base64编码的wav/mp3音频数据
        :rtype: str
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def SessionId(self):
        r"""一次请求对应一个SessionId
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Audio = params.get("Audio")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")