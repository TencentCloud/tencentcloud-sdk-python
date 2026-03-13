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


class BoundingBox(AbstractModel):
    r"""段落文本框位置：x，y代表左上顶点，width和height代表宽高

    """

    def __init__(self):
        r"""
        :param _X: 左上顶点x坐标
        :type X: int
        :param _Y: 左上顶点y坐标
        :type Y: int
        :param _Width: 宽
        :type Width: int
        :param _Height: 高
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""左上顶点x坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""左上顶点y坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""高
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    r"""坐标详细信息

    """

    def __init__(self):
        r"""
        :param _X: X坐标
        :type X: int
        :param _Y: Y坐标
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        r"""X坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Y坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTranslateLLMRequest(AbstractModel):
    r"""ImageTranslateLLM请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>图片数据的Base64字符串，经Base64编码后不超过 9M，分辨率建议600*800以上，支持PNG、JPG、JPEG格式。</p>
        :type Data: str
        :param _Target: <p>目标语言，支持语言列表：</p><ul><li>中文：zh</li><li>繁体（中国台湾）：zh-TW</li><li>繁体（中国香港）：zh-HK</li><li>英文：en</li><li>日语：ja</li><li>韩语：ko</li><li>泰语：th</li><li>越南语：vi</li><li>俄语：ru</li><li>德语：de</li><li>法语：fr</li><li>阿拉伯语：ar</li><li>西班牙语：es</li><li>意大利语：it</li><li>印度尼西亚语：id</li><li>马来西亚语：ms</li><li>葡萄牙语：pt</li><li>土耳其语：tr<br>-</li></ul>
        :type Target: str
        :param _Url: <p>输入图 Url。 使用Url的时候，Data参数需要传入&quot;&quot;。 图片限制：小于 10MB，分辨率建议600*800以上，格式支持 jpg、jpeg、png。</p>
        :type Url: str
        """
        self._Data = None
        self._Target = None
        self._Url = None

    @property
    def Data(self):
        r"""<p>图片数据的Base64字符串，经Base64编码后不超过 9M，分辨率建议600*800以上，支持PNG、JPG、JPEG格式。</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Target(self):
        r"""<p>目标语言，支持语言列表：</p><ul><li>中文：zh</li><li>繁体（中国台湾）：zh-TW</li><li>繁体（中国香港）：zh-HK</li><li>英文：en</li><li>日语：ja</li><li>韩语：ko</li><li>泰语：th</li><li>越南语：vi</li><li>俄语：ru</li><li>德语：de</li><li>法语：fr</li><li>阿拉伯语：ar</li><li>西班牙语：es</li><li>意大利语：it</li><li>印度尼西亚语：id</li><li>马来西亚语：ms</li><li>葡萄牙语：pt</li><li>土耳其语：tr<br>-</li></ul>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Url(self):
        r"""<p>输入图 Url。 使用Url的时候，Data参数需要传入&quot;&quot;。 图片限制：小于 10MB，分辨率建议600*800以上，格式支持 jpg、jpeg、png。</p>
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._Target = params.get("Target")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTranslateLLMResponse(AbstractModel):
    r"""ImageTranslateLLM返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>图片数据的Base64字符串，输出格式为JPG。</p>
        :type Data: str
        :param _Source: <p>原文本主要源语言。</p>
        :type Source: str
        :param _Target: <p>目标翻译语言。</p>
        :type Target: str
        :param _SourceText: <p>图片中的全部原文本。</p>
        :type SourceText: str
        :param _TargetText: <p>图片中全部译文。</p>
        :type TargetText: str
        :param _Angle: <p>逆时针图片角度，取值范围为0-359</p>
        :type Angle: float
        :param _TransDetails: <p>翻译详情信息</p>
        :type TransDetails: list of TransDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Source = None
        self._Target = None
        self._SourceText = None
        self._TargetText = None
        self._Angle = None
        self._TransDetails = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>图片数据的Base64字符串，输出格式为JPG。</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Source(self):
        r"""<p>原文本主要源语言。</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""<p>目标翻译语言。</p>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def SourceText(self):
        r"""<p>图片中的全部原文本。</p>
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""<p>图片中全部译文。</p>
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def Angle(self):
        r"""<p>逆时针图片角度，取值范围为0-359</p>
        :rtype: float
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def TransDetails(self):
        r"""<p>翻译详情信息</p>
        :rtype: list of TransDetail
        """
        return self._TransDetails

    @TransDetails.setter
    def TransDetails(self, TransDetails):
        self._TransDetails = TransDetails

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        self._Angle = params.get("Angle")
        if params.get("TransDetails") is not None:
            self._TransDetails = []
            for item in params.get("TransDetails"):
                obj = TransDetail()
                obj._deserialize(item)
                self._TransDetails.append(obj)
        self._RequestId = params.get("RequestId")


class RotateParagraphRect(AbstractModel):
    r"""段落文本旋转信息

    """

    def __init__(self):
        r"""
        :param _Coord: 段落文本坐标
        :type Coord: list of Coord
        :param _TiltAngle: 旋转角度
        :type TiltAngle: float
        :param _Valid: 段落文本信息是否有效
        :type Valid: bool
        """
        self._Coord = None
        self._TiltAngle = None
        self._Valid = None

    @property
    def Coord(self):
        r"""段落文本坐标
        :rtype: list of Coord
        """
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord

    @property
    def TiltAngle(self):
        r"""旋转角度
        :rtype: float
        """
        return self._TiltAngle

    @TiltAngle.setter
    def TiltAngle(self, TiltAngle):
        self._TiltAngle = TiltAngle

    @property
    def Valid(self):
        r"""段落文本信息是否有效
        :rtype: bool
        """
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid


    def _deserialize(self, params):
        if params.get("Coord") is not None:
            self._Coord = []
            for item in params.get("Coord"):
                obj = Coord()
                obj._deserialize(item)
                self._Coord.append(obj)
        self._TiltAngle = params.get("TiltAngle")
        self._Valid = params.get("Valid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTranslateRequest(AbstractModel):
    r"""TextTranslate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceText: 待翻译的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度需要低于6000字符。
        :type SourceText: str
        :param _Source: 源语言，支持：
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
        :param _Target: 目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：zh-TW（繁体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>zh-TW（繁体中文）：zh（简体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>en（英语）：zh（中文）、zh-TW（繁体中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、zh-TW（繁体中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ar（阿拉伯语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :type Target: str
        :param _ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        :param _UntranslatedText: 用来标记不希望被翻译的文本内容，如句子中的特殊符号、人名、地名等；每次请求只支持配置一个不被翻译的单词；仅支持配置人名、地名等名词，不要配置动词或短语，否则会影响翻译结果。
        :type UntranslatedText: str
        :param _TermRepoIDList: 需要使用的术语库列表，通过 [术语库操作指南](https://cloud.tencent.com/document/product/551/107926) 自行创建术语库获取。
        :type TermRepoIDList: list of str
        :param _SentRepoIDList: 需要使用的例句库列表，通过 [例句库操作指南](https://cloud.tencent.com/document/product/551/107927) 自行创建例句库获取。
        :type SentRepoIDList: list of str
        """
        self._SourceText = None
        self._Source = None
        self._Target = None
        self._ProjectId = None
        self._UntranslatedText = None
        self._TermRepoIDList = None
        self._SentRepoIDList = None

    @property
    def SourceText(self):
        r"""待翻译的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度需要低于6000字符。
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def Source(self):
        r"""源语言，支持：
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
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：zh-TW（繁体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>zh-TW（繁体中文）：zh（简体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>en（英语）：zh（中文）、zh-TW（繁体中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、zh-TW（繁体中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ar（阿拉伯语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def ProjectId(self):
        r"""项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UntranslatedText(self):
        r"""用来标记不希望被翻译的文本内容，如句子中的特殊符号、人名、地名等；每次请求只支持配置一个不被翻译的单词；仅支持配置人名、地名等名词，不要配置动词或短语，否则会影响翻译结果。
        :rtype: str
        """
        return self._UntranslatedText

    @UntranslatedText.setter
    def UntranslatedText(self, UntranslatedText):
        self._UntranslatedText = UntranslatedText

    @property
    def TermRepoIDList(self):
        r"""需要使用的术语库列表，通过 [术语库操作指南](https://cloud.tencent.com/document/product/551/107926) 自行创建术语库获取。
        :rtype: list of str
        """
        return self._TermRepoIDList

    @TermRepoIDList.setter
    def TermRepoIDList(self, TermRepoIDList):
        self._TermRepoIDList = TermRepoIDList

    @property
    def SentRepoIDList(self):
        r"""需要使用的例句库列表，通过 [例句库操作指南](https://cloud.tencent.com/document/product/551/107927) 自行创建例句库获取。
        :rtype: list of str
        """
        return self._SentRepoIDList

    @SentRepoIDList.setter
    def SentRepoIDList(self, SentRepoIDList):
        self._SentRepoIDList = SentRepoIDList


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._ProjectId = params.get("ProjectId")
        self._UntranslatedText = params.get("UntranslatedText")
        self._TermRepoIDList = params.get("TermRepoIDList")
        self._SentRepoIDList = params.get("SentRepoIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTranslateResponse(AbstractModel):
    r"""TextTranslate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetText: 翻译后的文本
        :type TargetText: str
        :param _Source: 源语言，详见入参Source
        :type Source: str
        :param _Target: 目标语言，详见入参Target
        :type Target: str
        :param _UsedAmount: 本次翻译消耗的字符数
        :type UsedAmount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetText = None
        self._Source = None
        self._Target = None
        self._UsedAmount = None
        self._RequestId = None

    @property
    def TargetText(self):
        r"""翻译后的文本
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def Source(self):
        r"""源语言，详见入参Source
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，详见入参Target
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def UsedAmount(self):
        r"""本次翻译消耗的字符数
        :rtype: int
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetText = params.get("TargetText")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._UsedAmount = params.get("UsedAmount")
        self._RequestId = params.get("RequestId")


class TransDetail(AbstractModel):
    r"""大模型图片翻译详情信息

    """

    def __init__(self):
        r"""
        :param _SourceLineText: 当前行的原文本
        :type SourceLineText: str
        :param _TargetLineText: 当前行的译文
        :type TargetLineText: str
        :param _BoundingBox: 段落文本框位置
        :type BoundingBox: :class:`tencentcloud.tmt.v20180321.models.BoundingBox`
        :param _LinesCount: 行数
        :type LinesCount: int
        :param _LineHeight: 行高
        :type LineHeight: int
        :param _SpamCode: 正常段落spam_code字段为0；如果存在spam_code字段且值大于0（1: 命中垃圾检查；2: 命中安全策略；3: 其他。），则命中安全检查被过滤。
        :type SpamCode: int
        :param _RotateParagraphRect: 段落文本旋转信息，只在valid为true时表示坐标有效
        :type RotateParagraphRect: :class:`tencentcloud.tmt.v20180321.models.RotateParagraphRect`
        """
        self._SourceLineText = None
        self._TargetLineText = None
        self._BoundingBox = None
        self._LinesCount = None
        self._LineHeight = None
        self._SpamCode = None
        self._RotateParagraphRect = None

    @property
    def SourceLineText(self):
        r"""当前行的原文本
        :rtype: str
        """
        return self._SourceLineText

    @SourceLineText.setter
    def SourceLineText(self, SourceLineText):
        self._SourceLineText = SourceLineText

    @property
    def TargetLineText(self):
        r"""当前行的译文
        :rtype: str
        """
        return self._TargetLineText

    @TargetLineText.setter
    def TargetLineText(self, TargetLineText):
        self._TargetLineText = TargetLineText

    @property
    def BoundingBox(self):
        r"""段落文本框位置
        :rtype: :class:`tencentcloud.tmt.v20180321.models.BoundingBox`
        """
        return self._BoundingBox

    @BoundingBox.setter
    def BoundingBox(self, BoundingBox):
        self._BoundingBox = BoundingBox

    @property
    def LinesCount(self):
        r"""行数
        :rtype: int
        """
        return self._LinesCount

    @LinesCount.setter
    def LinesCount(self, LinesCount):
        self._LinesCount = LinesCount

    @property
    def LineHeight(self):
        r"""行高
        :rtype: int
        """
        return self._LineHeight

    @LineHeight.setter
    def LineHeight(self, LineHeight):
        self._LineHeight = LineHeight

    @property
    def SpamCode(self):
        r"""正常段落spam_code字段为0；如果存在spam_code字段且值大于0（1: 命中垃圾检查；2: 命中安全策略；3: 其他。），则命中安全检查被过滤。
        :rtype: int
        """
        return self._SpamCode

    @SpamCode.setter
    def SpamCode(self, SpamCode):
        self._SpamCode = SpamCode

    @property
    def RotateParagraphRect(self):
        r"""段落文本旋转信息，只在valid为true时表示坐标有效
        :rtype: :class:`tencentcloud.tmt.v20180321.models.RotateParagraphRect`
        """
        return self._RotateParagraphRect

    @RotateParagraphRect.setter
    def RotateParagraphRect(self, RotateParagraphRect):
        self._RotateParagraphRect = RotateParagraphRect


    def _deserialize(self, params):
        self._SourceLineText = params.get("SourceLineText")
        self._TargetLineText = params.get("TargetLineText")
        if params.get("BoundingBox") is not None:
            self._BoundingBox = BoundingBox()
            self._BoundingBox._deserialize(params.get("BoundingBox"))
        self._LinesCount = params.get("LinesCount")
        self._LineHeight = params.get("LineHeight")
        self._SpamCode = params.get("SpamCode")
        if params.get("RotateParagraphRect") is not None:
            self._RotateParagraphRect = RotateParagraphRect()
            self._RotateParagraphRect._deserialize(params.get("RotateParagraphRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        