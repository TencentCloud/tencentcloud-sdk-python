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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class TextToVoiceRequest(AbstractModel):
    """TextToVoice请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 合成语音的源文本，按UTF-8编码统一计算。
中文最大支持110个汉字（全角标点符号算一个汉字）；英文最大支持350个字母（半角标点符号算一个字母）。
        :type Text: str
        :param SessionId: 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复。
        :type SessionId: str
        :param ModelType: 模型类型，1-默认模型。
        :type ModelType: int
        :param Volume: 音量大小，范围：[0，10]，分别对应11个等级的音量，默认为0，代表正常音量。没有静音选项。
输入除以上整数之外的其他参数不生效，按默认值处理。
        :type Volume: float
        :param Speed: 语速，范围：[-2，2]，分别对应不同语速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（默认）</li><li>1代表1.2倍</li><li>2代表1.5倍</li>如果需要更细化的语速，可以保留小数点后一位，例如0.5 1.1 1.8等。<br>
        :type Speed: float
        :param ProjectId: 项目id，用户自定义，默认为0。
        :type ProjectId: int
        :param VoiceType: 普通音色<li>0-云小宁，亲和女声(默认)</li><li>1-云小奇，亲和男声</li><li>2-云小晚，成熟男声</li><li>4-云小叶，温暖女声</li><li>5-云小欣，情感女声</li><li>6-云小龙，情感男声</li><li>7-云小曼，客服女声</li><li>1001-智瑜，情感女声</li><li>1002-智聆，通用女声</li><li>1003-智美，客服女声</li><li>1050-WeJack，英文男声</li><li>1051-WeRose，英文女声</li>精品音色<br>精品音色拟真度更高，价格不同于普通音色，查看[购买指南](https://cloud.tencent.com/product/tts/pricing)<br><li>101001-智瑜，情感女声（精品）</li><li>101002-智聆，通用女声（精品）</li><li>101003-智美，客服女声（精品）</li><li>101004-智云，通用男声</li><li>101005-智莉，通用女声</li><li>101006-智言，助手女声</li><li>101007-智娜，客服女声</li><li>101008-智琪，客服女声</li><li>101009-智芸，知性女声</li><li>101010-智华，通用男声</li><li>101011-智燕，新闻女声</li><li>101012-智丹，新闻女声</li><li>101013-智辉，新闻男声</li><li>101014-智宁，新闻男声</li><li>101015-智萌，男童声</li><li>101016-智甜，女童声</li><li>101017-智蓉，情感女声</li><li>101018-智靖，情感男声</li><li>101019-智彤，粤语女声</li><li>101050-WeJack，英文男声（精品）</li><li>101051-WeRose，英文女声（精品）</li><li>102000-贝蕾，客服女声</li><li>102001-贝果，客服女声</li><li>102002-贝紫，粤语女声</li><li>102003-贝雪，新闻女声</li>
        :type VoiceType: int
        :param PrimaryLanguage: 主语言类型：<li>1-中文（默认）</li><li>2-英文</li>
        :type PrimaryLanguage: int
        :param SampleRate: 音频采样率：<li>16000：16k（默认）</li><li>8000：8k</li>
        :type SampleRate: int
        :param Codec: 返回音频格式，可取值：wav（默认），mp3，pcm
        :type Codec: str
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
        self.Codec = None


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
        self.Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TextToVoiceResponse(AbstractModel):
    """TextToVoice返回参数结构体

    """

    def __init__(self):
        """
        :param Audio: base64编码的wav/mp3音频数据
        :type Audio: str
        :param SessionId: 一次请求对应一个SessionId
        :type SessionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Audio = None
        self.SessionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Audio = params.get("Audio")
        self.SessionId = params.get("SessionId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        