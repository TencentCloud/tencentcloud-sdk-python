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
        :param Text: 合成语音的源文本，按UTF-8编码统一计算，最多支持10万字符
        :type Text: str
        :param ModelType: 模型类型，1-默认模型。
        :type ModelType: int
        :param Volume: 音量大小，范围：[0，10]，分别对应11个等级的音量，默认为0，代表正常音量。没有静音选项。
        :type Volume: float
        :param Speed: 语速，范围：[-2，2]，分别对应不同语速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（默认）</li><li>1代表1.2倍</li><li>2代表1.5倍</li>如果需要更细化的语速，可以保留小数点后 2 位，例如0.5 1.1 1.8等。<br>参数值与实际语速转换，可参考[代码示例](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz)
        :type Speed: float
        :param ProjectId: 项目id，用户自定义，默认为0。
        :type ProjectId: int
        :param VoiceType: 音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见[购买指南](https://cloud.tencent.com/document/product/1073/34112)。完整的音色 ID 列表请参见[音色列表](https://cloud.tencent.com/document/product/1073/92668)。
        :type VoiceType: int
        :param PrimaryLanguage: 主语言类型：<li>1-中文（默认）</li><li>2-英文</li>
        :type PrimaryLanguage: int
        :param SampleRate: 音频采样率：<li>16000：16k（默认）</li><li>8000：8k</li>
        :type SampleRate: int
        :param Codec: 返回音频格式，可取值：mp3（默认），wav，pcm
        :type Codec: str
        :param CallbackUrl: 回调 URL，用户自行搭建的用于接收识别结果的服务URL。如果用户使用轮询方式获取识别结果，则无需提交该参数。[回调说明](https://cloud.tencent.com/document/product/1073/55746)
        :type CallbackUrl: str
        :param VoiceoverDialogueSplit: 旁白与对白文本解析，分别合成相应风格（仅适用于旁对白音色），默认 false
        :type VoiceoverDialogueSplit: bool
        """
        self.Text = None
        self.ModelType = None
        self.Volume = None
        self.Speed = None
        self.ProjectId = None
        self.VoiceType = None
        self.PrimaryLanguage = None
        self.SampleRate = None
        self.Codec = None
        self.CallbackUrl = None
        self.VoiceoverDialogueSplit = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.ModelType = params.get("ModelType")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.ProjectId = params.get("ProjectId")
        self.VoiceType = params.get("VoiceType")
        self.PrimaryLanguage = params.get("PrimaryLanguage")
        self.SampleRate = params.get("SampleRate")
        self.Codec = params.get("Codec")
        self.CallbackUrl = params.get("CallbackUrl")
        self.VoiceoverDialogueSplit = params.get("VoiceoverDialogueSplit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTtsTaskRespData(AbstractModel):
    """异步合成请求的返回数据

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID，可通过此ID在轮询接口获取合成状态与结果。注意：TaskId数据类型为string
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
        


class CreateTtsTaskResponse(AbstractModel):
    """CreateTtsTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 任务 id
        :type Data: :class:`tencentcloud.tts.v20190823.models.CreateTtsTaskRespData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CreateTtsTaskRespData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTtsTaskStatusRequest(AbstractModel):
    """DescribeTtsTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
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
        


class DescribeTtsTaskStatusRespData(AbstractModel):
    """获取异步合成结果的返回参数

    """

    def __init__(self):
        r"""
        :param TaskId: 任务标识。
        :type TaskId: str
        :param Status: 任务状态码，0：任务等待，1：任务执行中，2：任务成功，3：任务失败。
        :type Status: int
        :param StatusStr: 任务状态，waiting：任务等待，doing：任务执行中，success：任务成功，failed：任务失败。
        :type StatusStr: str
        :param ResultUrl: 合成音频COS地址（链接有效期1天）。
        :type ResultUrl: str
        :param ErrorMsg: 失败原因说明。
        :type ErrorMsg: str
        """
        self.TaskId = None
        self.Status = None
        self.StatusStr = None
        self.ResultUrl = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.StatusStr = params.get("StatusStr")
        self.ResultUrl = params.get("ResultUrl")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTtsTaskStatusResponse(AbstractModel):
    """DescribeTtsTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 任务状态返回
        :type Data: :class:`tencentcloud.tts.v20190823.models.DescribeTtsTaskStatusRespData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeTtsTaskStatusRespData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class Subtitle(AbstractModel):
    """时间戳信息。

    """

    def __init__(self):
        r"""
        :param Text: ⽂本信息。
        :type Text: str
        :param BeginTime: ⽂本对应tts语⾳开始时间戳，单位ms。
        :type BeginTime: int
        :param EndTime: ⽂本对应tts语⾳结束时间戳，单位ms。
        :type EndTime: int
        :param BeginIndex: 该字在整句中的开始位置，从0开始。
        :type BeginIndex: int
        :param EndIndex: 该字在整句中的结束位置，从0开始。
        :type EndIndex: int
        :param Phoneme: 该字的音素
注意：此字段可能返回 null，表示取不到有效值。
        :type Phoneme: str
        """
        self.Text = None
        self.BeginTime = None
        self.EndTime = None
        self.BeginIndex = None
        self.EndIndex = None
        self.Phoneme = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.BeginIndex = params.get("BeginIndex")
        self.EndIndex = params.get("EndIndex")
        self.Phoneme = params.get("Phoneme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceRequest(AbstractModel):
    """TextToVoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 合成语音的源文本，按UTF-8编码统一计算。
中文最大支持150个汉字（全角标点符号算一个汉字）；英文最大支持500个字母（半角标点符号算一个字母）。
        :type Text: str
        :param SessionId: 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复。
        :type SessionId: str
        :param Volume: 音量大小，范围：[0，10]，分别对应11个等级的音量，默认为0，代表正常音量。没有静音选项。
        :type Volume: float
        :param Speed: 语速，范围：[-2，6]，分别对应不同语速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（默认）</li><li>1代表1.2倍</li><li>2代表1.5倍</li><li>6代表2.5倍</li>如果需要更细化的语速，可以保留小数点后 2 位，例如0.5 1.1 1.8等。<br>参数值与实际语速转换，可参考[代码示例](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz)
        :type Speed: float
        :param ProjectId: 项目id，用户自定义，默认为0。
        :type ProjectId: int
        :param ModelType: 模型类型，1-默认模型。
        :type ModelType: int
        :param VoiceType: 音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见[购买指南](https://cloud.tencent.com/document/product/1073/34112)。完整的音色 ID 列表请参见[音色列表](https://cloud.tencent.com/document/product/1073/92668)。
        :type VoiceType: int
        :param PrimaryLanguage: 主语言类型：<li>1-中文（默认）</li><li>2-英文</li>
        :type PrimaryLanguage: int
        :param SampleRate: 音频采样率：<li>16000：16k（默认）</li><li>8000：8k</li>
        :type SampleRate: int
        :param Codec: 返回音频格式，可取值：wav（默认），mp3，pcm
        :type Codec: str
        :param EnableSubtitle: 是否开启时间戳功能，默认为false。
        :type EnableSubtitle: bool
        :param SegmentRate: 断句敏感阈值，默认值为：0，取值范围：[0,1,2]。该值越大越不容易断句，模型会更倾向于仅按照标点符号断句。此参数建议不要随意调整，可能会影响合成效果。
        :type SegmentRate: int
        :param EmotionCategory: 控制合成音频的情感，仅支持多情感音色使用。取值: neutral(中性)、sad(悲伤)、happy(高兴)、angry(生气)、fear(恐惧)、news(新闻)、story(故事)、radio(广播)、poetry(诗歌)、call(客服)、撒娇(sajiao)、厌恶(disgusted)、震惊(amaze)、平静(peaceful)、兴奋(exciting)
        :type EmotionCategory: str
        :param EmotionIntensity: 控制合成音频情感程度，取值范围为[50,200],默认为100；只有EmotionCategory不为空时生效；
        :type EmotionIntensity: int
        """
        self.Text = None
        self.SessionId = None
        self.Volume = None
        self.Speed = None
        self.ProjectId = None
        self.ModelType = None
        self.VoiceType = None
        self.PrimaryLanguage = None
        self.SampleRate = None
        self.Codec = None
        self.EnableSubtitle = None
        self.SegmentRate = None
        self.EmotionCategory = None
        self.EmotionIntensity = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.SessionId = params.get("SessionId")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.ProjectId = params.get("ProjectId")
        self.ModelType = params.get("ModelType")
        self.VoiceType = params.get("VoiceType")
        self.PrimaryLanguage = params.get("PrimaryLanguage")
        self.SampleRate = params.get("SampleRate")
        self.Codec = params.get("Codec")
        self.EnableSubtitle = params.get("EnableSubtitle")
        self.SegmentRate = params.get("SegmentRate")
        self.EmotionCategory = params.get("EmotionCategory")
        self.EmotionIntensity = params.get("EmotionIntensity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToVoiceResponse(AbstractModel):
    """TextToVoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Audio: base64编码的wav/mp3音频数据
        :type Audio: str
        :param SessionId: 一次请求对应一个SessionId
        :type SessionId: str
        :param Subtitles: 时间戳信息，若未开启时间戳，则返回空数组。
        :type Subtitles: list of Subtitle
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Audio = None
        self.SessionId = None
        self.Subtitles = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Audio = params.get("Audio")
        self.SessionId = params.get("SessionId")
        if params.get("Subtitles") is not None:
            self.Subtitles = []
            for item in params.get("Subtitles"):
                obj = Subtitle()
                obj._deserialize(item)
                self.Subtitles.append(obj)
        self.RequestId = params.get("RequestId")