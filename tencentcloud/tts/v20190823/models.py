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


class CreateTtsTaskRequest(AbstractModel):
    """CreateTtsTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 合成语音的源文本，按UTF-8编码统一计算，最多支持10万字符
        :type Text: str
        :param _ModelType: 模型类型，1-默认模型。
        :type ModelType: int
        :param _Volume: 音量大小，范围：[0，10]，分别对应11个等级的音量，默认为0，代表正常音量。没有静音选项。
        :type Volume: float
        :param _Speed: 语速，范围：[-2，2]，分别对应不同语速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（默认）</li><li>1代表1.2倍</li><li>2代表1.5倍</li>如果需要更细化的语速，可以保留小数点后 2 位，例如0.5 1.1 1.8等。<br>参数值与实际语速转换，可参考[代码示例](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz)
        :type Speed: float
        :param _ProjectId: 项目id，用户自定义，默认为0。
        :type ProjectId: int
        :param _VoiceType: 音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见[购买指南](https://cloud.tencent.com/document/product/1073/34112)。完整的音色 ID 列表请参见[音色列表](https://cloud.tencent.com/document/product/1073/92668)。
        :type VoiceType: int
        :param _PrimaryLanguage: 主语言类型：<li>1-中文（默认）</li><li>2-英文</li><li>3-日文</li>
        :type PrimaryLanguage: int
        :param _SampleRate: 音频采样率：<li>16000：16k（默认）</li><li>8000：8k</li>
        :type SampleRate: int
        :param _Codec: 返回音频格式，可取值：mp3（默认），wav，pcm
        :type Codec: str
        :param _CallbackUrl: 回调 URL，用户自行搭建的用于接收识别结果的服务URL。如果用户使用轮询方式获取识别结果，则无需提交该参数。[回调说明](https://cloud.tencent.com/document/product/1073/55746)
        :type CallbackUrl: str
        :param _EnableSubtitle: 是否开启时间戳功能，默认为false。
        :type EnableSubtitle: bool
        :param _VoiceoverDialogueSplit: 旁白与对白文本解析，分别合成相应风格（仅适用于旁对白音色10510000、100510000），默认 false
        :type VoiceoverDialogueSplit: bool
        :param _EmotionCategory: 控制合成音频的情感，仅支持多情感音色使用。取值: neutral(中性)、sad(悲伤)、happy(高兴)、angry(生气)、fear(恐惧)、news(新闻)、story(故事)、radio(广播)、poetry(诗歌)、call(客服)、撒娇(sajiao)、厌恶(disgusted)、震惊(amaze)、平静(peaceful)、兴奋(exciting)、傲娇(aojiao)、解说(jieshuo)
        :type EmotionCategory: str
        :param _EmotionIntensity: 控制合成音频情感程度，取值范围为[50,200],默认为100；只有EmotionCategory不为空时生效。
        :type EmotionIntensity: int
        """
        self._Text = None
        self._ModelType = None
        self._Volume = None
        self._Speed = None
        self._ProjectId = None
        self._VoiceType = None
        self._PrimaryLanguage = None
        self._SampleRate = None
        self._Codec = None
        self._CallbackUrl = None
        self._EnableSubtitle = None
        self._VoiceoverDialogueSplit = None
        self._EmotionCategory = None
        self._EmotionIntensity = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Speed(self):
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VoiceType(self):
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def PrimaryLanguage(self):
        return self._PrimaryLanguage

    @PrimaryLanguage.setter
    def PrimaryLanguage(self, PrimaryLanguage):
        self._PrimaryLanguage = PrimaryLanguage

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def EnableSubtitle(self):
        return self._EnableSubtitle

    @EnableSubtitle.setter
    def EnableSubtitle(self, EnableSubtitle):
        self._EnableSubtitle = EnableSubtitle

    @property
    def VoiceoverDialogueSplit(self):
        return self._VoiceoverDialogueSplit

    @VoiceoverDialogueSplit.setter
    def VoiceoverDialogueSplit(self, VoiceoverDialogueSplit):
        self._VoiceoverDialogueSplit = VoiceoverDialogueSplit

    @property
    def EmotionCategory(self):
        return self._EmotionCategory

    @EmotionCategory.setter
    def EmotionCategory(self, EmotionCategory):
        self._EmotionCategory = EmotionCategory

    @property
    def EmotionIntensity(self):
        return self._EmotionIntensity

    @EmotionIntensity.setter
    def EmotionIntensity(self, EmotionIntensity):
        self._EmotionIntensity = EmotionIntensity


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._ModelType = params.get("ModelType")
        self._Volume = params.get("Volume")
        self._Speed = params.get("Speed")
        self._ProjectId = params.get("ProjectId")
        self._VoiceType = params.get("VoiceType")
        self._PrimaryLanguage = params.get("PrimaryLanguage")
        self._SampleRate = params.get("SampleRate")
        self._Codec = params.get("Codec")
        self._CallbackUrl = params.get("CallbackUrl")
        self._EnableSubtitle = params.get("EnableSubtitle")
        self._VoiceoverDialogueSplit = params.get("VoiceoverDialogueSplit")
        self._EmotionCategory = params.get("EmotionCategory")
        self._EmotionIntensity = params.get("EmotionIntensity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTtsTaskRespData(AbstractModel):
    """异步合成请求的返回数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可通过此ID在轮询接口获取合成状态与结果。注意：TaskId数据类型为string
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
        


class CreateTtsTaskResponse(AbstractModel):
    """CreateTtsTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务 id
        :type Data: :class:`tencentcloud.tts.v20190823.models.CreateTtsTaskRespData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateTtsTaskRespData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTtsTaskStatusRequest(AbstractModel):
    """DescribeTtsTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
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
        


class DescribeTtsTaskStatusRespData(AbstractModel):
    """获取异步合成结果的返回参数

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务标识。
        :type TaskId: str
        :param _Status: 任务状态码，0：任务等待，1：任务执行中，2：任务成功，3：任务失败。
        :type Status: int
        :param _StatusStr: 任务状态，waiting：任务等待，doing：任务执行中，success：任务成功，failed：任务失败。
        :type StatusStr: str
        :param _ResultUrl: 合成音频COS地址（链接有效期1天）。
        :type ResultUrl: str
        :param _Subtitles: 时间戳信息，若未开启时间戳，则返回空数组。
        :type Subtitles: list of Subtitle
        :param _ErrorMsg: 失败原因说明。
        :type ErrorMsg: str
        """
        self._TaskId = None
        self._Status = None
        self._StatusStr = None
        self._ResultUrl = None
        self._Subtitles = None
        self._ErrorMsg = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusStr(self):
        return self._StatusStr

    @StatusStr.setter
    def StatusStr(self, StatusStr):
        self._StatusStr = StatusStr

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def Subtitles(self):
        return self._Subtitles

    @Subtitles.setter
    def Subtitles(self, Subtitles):
        self._Subtitles = Subtitles

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._StatusStr = params.get("StatusStr")
        self._ResultUrl = params.get("ResultUrl")
        if params.get("Subtitles") is not None:
            self._Subtitles = []
            for item in params.get("Subtitles"):
                obj = Subtitle()
                obj._deserialize(item)
                self._Subtitles.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTtsTaskStatusResponse(AbstractModel):
    """DescribeTtsTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务状态返回
        :type Data: :class:`tencentcloud.tts.v20190823.models.DescribeTtsTaskStatusRespData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeTtsTaskStatusRespData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class Subtitle(AbstractModel):
    """时间戳信息。

    """

    def __init__(self):
        r"""
        :param _Text: ⽂本信息。
        :type Text: str
        :param _BeginTime: ⽂本对应tts语⾳开始时间戳，单位ms。
        :type BeginTime: int
        :param _EndTime: ⽂本对应tts语⾳结束时间戳，单位ms。
        :type EndTime: int
        :param _BeginIndex: 该字在整句中的开始位置，从0开始。
        :type BeginIndex: int
        :param _EndIndex: 该字在整句中的结束位置，从0开始。
        :type EndIndex: int
        :param _Phoneme: 该字的音素
注意：此字段可能返回 null，表示取不到有效值。
        :type Phoneme: str
        """
        self._Text = None
        self._BeginTime = None
        self._EndTime = None
        self._BeginIndex = None
        self._EndIndex = None
        self._Phoneme = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BeginIndex(self):
        return self._BeginIndex

    @BeginIndex.setter
    def BeginIndex(self, BeginIndex):
        self._BeginIndex = BeginIndex

    @property
    def EndIndex(self):
        return self._EndIndex

    @EndIndex.setter
    def EndIndex(self, EndIndex):
        self._EndIndex = EndIndex

    @property
    def Phoneme(self):
        return self._Phoneme

    @Phoneme.setter
    def Phoneme(self, Phoneme):
        self._Phoneme = Phoneme


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._BeginIndex = params.get("BeginIndex")
        self._EndIndex = params.get("EndIndex")
        self._Phoneme = params.get("Phoneme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceRequest(AbstractModel):
    """TextToVoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 合成语音的源文本，按UTF-8编码统一计算。
中文最大支持150个汉字（全角标点符号算一个汉字）；英文最大支持500个字母（半角标点符号算一个字母）。
        :type Text: str
        :param _SessionId: 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复。
        :type SessionId: str
        :param _Volume: 音量大小，范围[0，10]，对应音量大小。默认为0，代表正常音量，值越大音量越高。
        :type Volume: float
        :param _Speed: 语速，范围：[-2，6]，分别对应不同语速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（默认）</li><li>1代表1.2倍</li><li>2代表1.5倍</li><li>6代表2.5倍</li>如果需要更细化的语速，可以保留小数点后 2 位，例如0.5 1.1 1.8等。<br>参数值与实际语速转换，可参考[代码示例](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz)
        :type Speed: float
        :param _ProjectId: 项目id，用户自定义，默认为0。
        :type ProjectId: int
        :param _ModelType: 模型类型，1-默认模型。
        :type ModelType: int
        :param _VoiceType: 音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见[购买指南](https://cloud.tencent.com/document/product/1073/34112)。完整的音色 ID 列表请参见[音色列表](https://cloud.tencent.com/document/product/1073/92668)。
        :type VoiceType: int
        :param _PrimaryLanguage: 主语言类型：<li>1-中文（默认）</li><li>2-英文</li><li>3-日文</li>
        :type PrimaryLanguage: int
        :param _SampleRate: 音频采样率：
<li>24000：24k（部分音色支持，请参见[音色列表](https://cloud.tencent.com/document/product/1073/92668)）</li>
<li>16000：16k（默认）</li>
<li>8000：8k</li>
        :type SampleRate: int
        :param _Codec: 返回音频格式，可取值：wav（默认），mp3，pcm
        :type Codec: str
        :param _EnableSubtitle: 是否开启时间戳功能，默认为false。
        :type EnableSubtitle: bool
        :param _SegmentRate: 断句敏感阈值，默认值为：0，取值范围：[0,1,2]。该值越大越不容易断句，模型会更倾向于仅按照标点符号断句。此参数建议不要随意调整，可能会影响合成效果。
        :type SegmentRate: int
        :param _EmotionCategory: 控制合成音频的情感，仅支持多情感音色使用。取值: neutral(中性)、sad(悲伤)、happy(高兴)、angry(生气)、fear(恐惧)、news(新闻)、story(故事)、radio(广播)、poetry(诗歌)、call(客服)、撒娇(sajiao)、厌恶(disgusted)、震惊(amaze)、平静(peaceful)、兴奋(exciting)、傲娇(aojiao)、解说(jieshuo)
        :type EmotionCategory: str
        :param _EmotionIntensity: 控制合成音频情感程度，取值范围为[50,200],默认为100；只有EmotionCategory不为空时生效；
        :type EmotionIntensity: int
        """
        self._Text = None
        self._SessionId = None
        self._Volume = None
        self._Speed = None
        self._ProjectId = None
        self._ModelType = None
        self._VoiceType = None
        self._PrimaryLanguage = None
        self._SampleRate = None
        self._Codec = None
        self._EnableSubtitle = None
        self._SegmentRate = None
        self._EmotionCategory = None
        self._EmotionIntensity = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Speed(self):
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def VoiceType(self):
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType

    @property
    def PrimaryLanguage(self):
        return self._PrimaryLanguage

    @PrimaryLanguage.setter
    def PrimaryLanguage(self, PrimaryLanguage):
        self._PrimaryLanguage = PrimaryLanguage

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def EnableSubtitle(self):
        return self._EnableSubtitle

    @EnableSubtitle.setter
    def EnableSubtitle(self, EnableSubtitle):
        self._EnableSubtitle = EnableSubtitle

    @property
    def SegmentRate(self):
        return self._SegmentRate

    @SegmentRate.setter
    def SegmentRate(self, SegmentRate):
        self._SegmentRate = SegmentRate

    @property
    def EmotionCategory(self):
        return self._EmotionCategory

    @EmotionCategory.setter
    def EmotionCategory(self, EmotionCategory):
        self._EmotionCategory = EmotionCategory

    @property
    def EmotionIntensity(self):
        return self._EmotionIntensity

    @EmotionIntensity.setter
    def EmotionIntensity(self, EmotionIntensity):
        self._EmotionIntensity = EmotionIntensity


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._SessionId = params.get("SessionId")
        self._Volume = params.get("Volume")
        self._Speed = params.get("Speed")
        self._ProjectId = params.get("ProjectId")
        self._ModelType = params.get("ModelType")
        self._VoiceType = params.get("VoiceType")
        self._PrimaryLanguage = params.get("PrimaryLanguage")
        self._SampleRate = params.get("SampleRate")
        self._Codec = params.get("Codec")
        self._EnableSubtitle = params.get("EnableSubtitle")
        self._SegmentRate = params.get("SegmentRate")
        self._EmotionCategory = params.get("EmotionCategory")
        self._EmotionIntensity = params.get("EmotionIntensity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceResponse(AbstractModel):
    """TextToVoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Audio: base64编码的wav/mp3音频数据
        :type Audio: str
        :param _SessionId: 一次请求对应一个SessionId
        :type SessionId: str
        :param _Subtitles: 时间戳信息，若未开启时间戳，则返回空数组。
        :type Subtitles: list of Subtitle
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Audio = None
        self._SessionId = None
        self._Subtitles = None
        self._RequestId = None

    @property
    def Audio(self):
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Subtitles(self):
        return self._Subtitles

    @Subtitles.setter
    def Subtitles(self, Subtitles):
        self._Subtitles = Subtitles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Audio = params.get("Audio")
        self._SessionId = params.get("SessionId")
        if params.get("Subtitles") is not None:
            self._Subtitles = []
            for item in params.get("Subtitles"):
                obj = Subtitle()
                obj._deserialize(item)
                self._Subtitles.append(obj)
        self._RequestId = params.get("RequestId")