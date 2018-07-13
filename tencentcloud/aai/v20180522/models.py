# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class SentenceRecognitionRequest(AbstractModel):
    """SentenceRecognition请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 腾讯云项目 ID，可填 0，总长度不超过 1024 字节。
        :type ProjectId: int
        :param SubServiceType: 子服务类型。0：离线语音识别。1：实时流式识别，2，一句话识别。
        :type SubServiceType: int
        :param EngSerViceType: 引擎类型。8k：电话 8k 通用模型；16k：16k 通用模型。
        :type EngSerViceType: str
        :param SourceType: 语音数据来源。0：语音 URL；1：语音数据（post body）。
        :type SourceType: int
        :param VoiceFormat: 识别音频的音频格式（支持mp3,wav）。
        :type VoiceFormat: str
        :param UsrAudioKey: 用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。
        :type UsrAudioKey: str
        :param Url: 语音 URL，公网可下载。当 SourceType 值为 0 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。
        :type Url: str
        :param Data: 语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码。音频数据要小于900k。
        :type Data: str
        :param DataLen: 数据长度，当 SourceType 值为1时必须填写，为0可不写。
        :type DataLen: int
        """
        self.ProjectId = None
        self.SubServiceType = None
        self.EngSerViceType = None
        self.SourceType = None
        self.VoiceFormat = None
        self.UsrAudioKey = None
        self.Url = None
        self.Data = None
        self.DataLen = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SubServiceType = params.get("SubServiceType")
        self.EngSerViceType = params.get("EngSerViceType")
        self.SourceType = params.get("SourceType")
        self.VoiceFormat = params.get("VoiceFormat")
        self.UsrAudioKey = params.get("UsrAudioKey")
        self.Url = params.get("Url")
        self.Data = params.get("Data")
        self.DataLen = params.get("DataLen")


class SentenceRecognitionResponse(AbstractModel):
    """SentenceRecognition返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 识别结果。
        :type Result: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class TextToVoiceRequest(AbstractModel):
    """TextToVoice请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 合成语音的源文本
        :type Text: str
        :param SessionId: 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复
        :type SessionId: str
        :param ModelType: 模型类型，1-默认模型
        :type ModelType: int
        :param Volume: 音量大小，暂仅支持默认值1
        :type Volume: float
        :param Speed: 语速，暂仅支持默认值1
        :type Speed: float
        :param ProjectId: 用户自定义项目id，默认为0
        :type ProjectId: int
        :param VoiceType: 音色，1-默认音色
        :type VoiceType: int
        :param PrimaryLanguage: 主语言类型<li>1-中文(包括粤语)，最大300字符</li><li>2-英文，最大支持600字符</li>
        :type PrimaryLanguage: int
        :param SampleRate: 音频采样率：暂仅支持16k
        :type SampleRate: int
        """
        self.Text = None
        self.SessionId = None
        self.ModelType = None
        self.Volume = None
        self.Speed = None
        self.ProjectId = None
        self.VoiceType = None
        self.PrimaryLanguage = None
        self.SampleRate = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.SessionId = params.get("SessionId")
        self.ModelType = params.get("ModelType")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.ProjectId = params.get("ProjectId")
        self.VoiceType = params.get("VoiceType")
        self.PrimaryLanguage = params.get("PrimaryLanguage")
        self.SampleRate = params.get("SampleRate")


class TextToVoiceResponse(AbstractModel):
    """TextToVoice返回参数结构体

    """

    def __init__(self):
        """
        :param Audio: base编码的wav音频
        :type Audio: str
        :param SessionId: 一次请求对应一个SessionId
        :type SessionId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Audio = None
        self.SessionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Audio = params.get("Audio")
        self.SessionId = params.get("SessionId")
        self.RequestId = params.get("RequestId")