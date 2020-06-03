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
        :param ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
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
        :param ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
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
        :param Target: 翻译目标语言类型，支持的语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param AudioFormat: pcm : 146   speex : 16779154   mp3 : 83886080
        :type AudioFormat: int
        :param Seq: 语音分片的序号，从0开始
        :type Seq: int
        :param IsEnd: 是否最后一片语音分片，0-否，1-是
        :type IsEnd: int
        :param Data: 语音分片内容进行 Base64 编码后的字符串。音频内容需包含有效并可识别的文本信息。
        :type Data: str
        :param ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        :param Mode: 识别模式，该参数已废弃
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
        :param SourceText: 识别出的原文
        :type SourceText: str
        :param TargetText: 翻译出的译文
        :type TargetText: str
        :param Seq: 第几个语音分片
        :type Seq: int
        :param Source: 原语言
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


class TextTranslateBatchRequest(AbstractModel):
    """TextTranslateBatch请求参数结构体

    """

    def __init__(self):
        """
        :param Source: 源语言，支持： 
auto：自动识别（识别为一种语言）
zh：简体中文
zh-TW：繁体中文
en：英语
ja：日语
ko：韩语
fr：法语
es：西班牙语
it：意大利语
de：德语
tr：土耳其语
ru：俄语
pt：葡萄牙语
vi：越南语
id：印尼语
th：泰语
ms：马来西亚语
ar：阿拉伯语
hi：印地语
        :type Source: str
        :param Target: 目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）</li>
<li>zh-TW（繁体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）</li>
<li>en（英语）：zh（中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、en（英语）</li>
<li>ar（阿拉伯语）：en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :type Target: str
        :param ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        :param SourceTextList: 待翻译的文本列表，批量接口可以以数组方式在一次请求中填写多个待翻译文本。文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度总和需要低于2000。
        :type SourceTextList: list of str
        """
        self.Source = None
        self.Target = None
        self.ProjectId = None
        self.SourceTextList = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.ProjectId = params.get("ProjectId")
        self.SourceTextList = params.get("SourceTextList")


class TextTranslateBatchResponse(AbstractModel):
    """TextTranslateBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Source: 源语言，详见入参Target
        :type Source: str
        :param Target: 目标语言，详见入参Target
        :type Target: str
        :param TargetTextList: 翻译后的文本列表
        :type TargetTextList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Source = None
        self.Target = None
        self.TargetTextList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.TargetTextList = params.get("TargetTextList")
        self.RequestId = params.get("RequestId")


class TextTranslateRequest(AbstractModel):
    """TextTranslate请求参数结构体

    """

    def __init__(self):
        """
        :param SourceText: 待翻译的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度需要低于2000。
        :type SourceText: str
        :param Source: 源语言，支持：
auto：自动识别（识别为一种语言）
zh：简体中文
zh-TW：繁体中文
en：英语
ja：日语
ko：韩语
fr：法语
es：西班牙语
it：意大利语
de：德语
tr：土耳其语
ru：俄语
pt：葡萄牙语
vi：越南语
id：印尼语
th：泰语
ms：马来西亚语
ar：阿拉伯语
hi：印地语
        :type Source: str
        :param Target: 目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）</li>
<li>zh-TW（繁体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）</li>
<li>en（英语）：zh（中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、en（英语）</li>
<li>ar（阿拉伯语）：en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :type Target: str
        :param ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        :param UntranslatedText: 用来标记不希望被翻译的文本内容，如句子中的特殊符号、人名、地名等；每次请求只支持配置一个不被翻译的单词；仅支持配置人名、地名等名词，不要配置动词或短语，否则会影响翻译结果。
        :type UntranslatedText: str
        """
        self.SourceText = None
        self.Source = None
        self.Target = None
        self.ProjectId = None
        self.UntranslatedText = None


    def _deserialize(self, params):
        self.SourceText = params.get("SourceText")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.ProjectId = params.get("ProjectId")
        self.UntranslatedText = params.get("UntranslatedText")


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