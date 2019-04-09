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


class ImageRecord(AbstractModel):
    """图片翻译结果

    """

    def __init__(self):
        """
        :param Value: 图片翻译结果
        :type Value: list of ItemValue
        """
        self.Value = None


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = ItemValue()
                obj._deserialize(item)
                self.Value.append(obj)


class ImageTranslateRequest(AbstractModel):
    """ImageTranslate请求参数结构体

    """

    def __init__(self):
        """
        :param SessionUuid: 唯一id，返回时原样返回
        :type SessionUuid: str
        :param Scene: doc:文档扫描
        :type Scene: str
        :param Data: 图片数据的Base64字符串，图片大小上限为4M，建议对源图片进行一定程度压缩
        :type Data: str
        :param Source: 源语言，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Source: str
        :param Target: 目标语言，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param ProjectId: 项目id
        :type ProjectId: int
        """
        self.SessionUuid = None
        self.Scene = None
        self.Data = None
        self.Source = None
        self.Target = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.Scene = params.get("Scene")
        self.Data = params.get("Data")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.ProjectId = params.get("ProjectId")


class ImageTranslateResponse(AbstractModel):
    """ImageTranslate返回参数结构体

    """

    def __init__(self):
        """
        :param SessionUuid: 请求的SessionUuid返回
        :type SessionUuid: str
        :param Source: 源语言
        :type Source: str
        :param Target: 目标语言
        :type Target: str
        :param ImageRecord: 图片翻译结果，翻译结果按识别的文本每一行独立翻译，后续会推出按段落划分并翻译的版本
        :type ImageRecord: :class:`tencentcloud.tmt.v20180321.models.ImageRecord`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionUuid = None
        self.Source = None
        self.Target = None
        self.ImageRecord = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        if params.get("ImageRecord") is not None:
            self.ImageRecord = ImageRecord()
            self.ImageRecord._deserialize(params.get("ImageRecord"))
        self.RequestId = params.get("RequestId")


class ItemValue(AbstractModel):
    """翻译结果

    """

    def __init__(self):
        """
        :param SourceText: 识别出的源文
        :type SourceText: str
        :param TargetText: 翻译后的译文
        :type TargetText: str
        :param X: X坐标
        :type X: int
        :param Y: Y坐标
        :type Y: int
        :param W: 宽度
        :type W: int
        :param H: 高度
        :type H: int
        """
        self.SourceText = None
        self.TargetText = None
        self.X = None
        self.Y = None
        self.W = None
        self.H = None


    def _deserialize(self, params):
        self.SourceText = params.get("SourceText")
        self.TargetText = params.get("TargetText")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.W = params.get("W")
        self.H = params.get("H")


class LanguageDetectRequest(AbstractModel):
    """LanguageDetect请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待识别的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败。单次请求的文本长度需要低于2000。
        :type Text: str
        :param ProjectId: 项目id
        :type ProjectId: int
        """
        self.Text = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.ProjectId = params.get("ProjectId")


class LanguageDetectResponse(AbstractModel):
    """LanguageDetect返回参数结构体

    """

    def __init__(self):
        """
        :param Lang: 识别出的语言种类，参考语言列表
<li> zh : 中文 </li> <li> en : 英文 </li><li> jp : 日语 </li> <li> kr : 韩语 </li><li> de : 德语 </li><li> fr : 法语 </li><li> es : 西班牙文 </li> <li> it : 意大利文 </li><li> tr : 土耳其文 </li><li> ru : 俄文 </li><li> pt : 葡萄牙文 </li><li> vi : 越南文 </li><li> id : 印度尼西亚文 </li><li> ms : 马来西亚文 </li><li> th : 泰文 </li>
        :type Lang: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Lang = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.RequestId = params.get("RequestId")


class SpeechTranslateRequest(AbstractModel):
    """SpeechTranslate请求参数结构体

    """

    def __init__(self):
        """
        :param SessionUuid: 一段完整的语音对应一个SessionUuid
        :type SessionUuid: str
        :param Source: 音频中的语言类型，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Source: str
        :param Target: 翻译目标语⾔言类型 ，支持的语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param AudioFormat: pcm : 146   amr : 33554432   mp3 : 83886080
        :type AudioFormat: int
        :param Seq: 语音分片的序号，从0开始
        :type Seq: int
        :param IsEnd: 是否最后一片语音分片，0-否，1-是
        :type IsEnd: int
        :param Data: 语音分片内容的base64字符串，音频内容应含有效并可识别的文本
        :type Data: str
        :param ProjectId: 项目id，用户可自定义
        :type ProjectId: int
        :param Mode: 识别模式，不填则由调用放进行vad(静音检测)，填bvad则由服务放进行vad，前者适合段语音翻译（收到所有语音分片后翻译），后者适合长语音翻译（在完成一个断句识别后就会返回部分结果）
        :type Mode: str
        """
        self.SessionUuid = None
        self.Source = None
        self.Target = None
        self.AudioFormat = None
        self.Seq = None
        self.IsEnd = None
        self.Data = None
        self.ProjectId = None
        self.Mode = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.AudioFormat = params.get("AudioFormat")
        self.Seq = params.get("Seq")
        self.IsEnd = params.get("IsEnd")
        self.Data = params.get("Data")
        self.ProjectId = params.get("ProjectId")
        self.Mode = params.get("Mode")


class SpeechTranslateResponse(AbstractModel):
    """SpeechTranslate返回参数结构体

    """

    def __init__(self):
        """
        :param SessionUuid: 请求的SessionUuid直接返回
        :type SessionUuid: str
        :param RecognizeStatus: 语音识别状态 1-进行中 0-完成
        :type RecognizeStatus: int
        :param SourceText: 识别出的源文
        :type SourceText: str
        :param TargetText: 翻译出的译文
        :type TargetText: str
        :param Seq: 第几个语音分片
        :type Seq: int
        :param Source: 源语言
        :type Source: str
        :param Target: 目标语言
        :type Target: str
        :param VadSeq: 当请求的Mode参数填写bvad是，启动VadSeq。此时Seq会被设置为后台vad（静音检测）后的新序号，而VadSeq代表客户端原始Seq值
        :type VadSeq: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionUuid = None
        self.RecognizeStatus = None
        self.SourceText = None
        self.TargetText = None
        self.Seq = None
        self.Source = None
        self.Target = None
        self.VadSeq = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.RecognizeStatus = params.get("RecognizeStatus")
        self.SourceText = params.get("SourceText")
        self.TargetText = params.get("TargetText")
        self.Seq = params.get("Seq")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.VadSeq = params.get("VadSeq")
        self.RequestId = params.get("RequestId")


class TextTranslateRequest(AbstractModel):
    """TextTranslate请求参数结构体

    """

    def __init__(self):
        """
        :param SourceText: 待翻译的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本会翻译失败。单次请求的文本长度需要低于2000。
        :type SourceText: str
        :param Source: 源语言，参照Target支持语言列表
        :type Source: str
        :param Target: 目标语言，参照支持语言列表
<li> zh : 中文 </li> <li> en : 英文 </li><li> jp : 日语 </li> <li> kr : 韩语 </li><li> de : 德语 </li><li> fr : 法语 </li><li> es : 西班牙文 </li> <li> it : 意大利文 </li><li> tr : 土耳其文 </li><li> ru : 俄文 </li><li> pt : 葡萄牙文 </li><li> vi : 越南文 </li><li> id : 印度尼西亚文 </li><li> ms : 马来西亚文 </li><li> th : 泰文 </li><li> auto : 自动识别源语言，只能用于source字段 </li>
        :type Target: str
        :param ProjectId: 项目id
        :type ProjectId: int
        """
        self.SourceText = None
        self.Source = None
        self.Target = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.SourceText = params.get("SourceText")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.ProjectId = params.get("ProjectId")


class TextTranslateResponse(AbstractModel):
    """TextTranslate返回参数结构体

    """

    def __init__(self):
        """
        :param TargetText: 翻译后的文本
        :type TargetText: str
        :param Source: 源语言，详见入参Target
        :type Source: str
        :param Target: 目标语言，详见入参Target
        :type Target: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TargetText = None
        self.Source = None
        self.Target = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetText = params.get("TargetText")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.RequestId = params.get("RequestId")