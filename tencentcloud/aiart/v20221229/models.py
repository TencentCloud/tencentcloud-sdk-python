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


class ImageToImageRequest(AbstractModel):
    """ImageToImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InputImage: 输入图 Base64 数据。
算法将根据输入的图片，结合文本描述智能生成与之相关的图像。
Base64 和 Url 必须提供一个，如果都提供以 Base64 为准。
图片限制：单边分辨率小于2000，转成 Base64 字符串后小于 5MB。
        :type InputImage: str
        :param _InputUrl: 输入图 Url。
算法将根据输入的图片，结合文本描述智能生成与之相关的图像。
Base64 和 Url 必须提供一个，如果都提供以 Base64 为准。
图片限制：单边分辨率小于2000，转成 Base64 字符串后小于 5MB。
        :type InputUrl: str
        :param _Prompt: 文本描述。
用于在输入图的基础上引导生成图效果，建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。推荐使用中文。最多支持512个 utf-8 字符。
注意：如果不输入任何文本描述，可能导致较差的效果，建议根据期望的效果输入相应的文本描述。
        :type Prompt: str
        :param _NegativePrompt: 反向文本描述。
用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。
推荐使用中文。最多可传512个 utf-8 字符。
        :type NegativePrompt: str
        :param _Styles: 绘画风格。
请在  [智能图生图风格列表](https://cloud.tencent.com/document/product/1668/86250) 中选择期望的风格，传入风格编号。
推荐使用且只使用一种风格。不传默认使用201（日系动漫风格）。
如果想要探索风格列表之外的风格，也可以尝试在 Prompt 中输入其他的风格描述。
        :type Styles: list of str
        :param _ResultConfig: 生成图结果的配置，包括输出图片分辨率和尺寸等。
        :type ResultConfig: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        :param _LogoAdd: 为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _Strength: 生成自由度。
Strength 值越小，生成图和原图越接近。取值范围0~1，不传默认为0.65。
        :type Strength: float
        """
        self._InputImage = None
        self._InputUrl = None
        self._Prompt = None
        self._NegativePrompt = None
        self._Styles = None
        self._ResultConfig = None
        self._LogoAdd = None
        self._LogoParam = None
        self._Strength = None

    @property
    def InputImage(self):
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def Prompt(self):
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Styles(self):
        return self._Styles

    @Styles.setter
    def Styles(self, Styles):
        self._Styles = Styles

    @property
    def ResultConfig(self):
        return self._ResultConfig

    @ResultConfig.setter
    def ResultConfig(self, ResultConfig):
        self._ResultConfig = ResultConfig

    @property
    def LogoAdd(self):
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Strength(self):
        return self._Strength

    @Strength.setter
    def Strength(self, Strength):
        self._Strength = Strength


    def _deserialize(self, params):
        self._InputImage = params.get("InputImage")
        self._InputUrl = params.get("InputUrl")
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Styles = params.get("Styles")
        if params.get("ResultConfig") is not None:
            self._ResultConfig = ResultConfig()
            self._ResultConfig._deserialize(params.get("ResultConfig"))
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._Strength = params.get("Strength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToImageResponse(AbstractModel):
    """ImageToImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 返回的生成图 Base64 编码。
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class LogoParam(AbstractModel):
    """logo参数

    """

    def __init__(self):
        r"""
        :param _LogoUrl: 水印url
        :type LogoUrl: str
        :param _LogoImage: 水印base64，url和base64二选一传入
        :type LogoImage: str
        :param _LogoRect: 水印图片位于融合结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
        :type LogoRect: :class:`tencentcloud.aiart.v20221229.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect


    def _deserialize(self, params):
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        if params.get("LogoRect") is not None:
            self._LogoRect = LogoRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoRect(AbstractModel):
    """输入框

    """

    def __init__(self):
        r"""
        :param _X: 左上角X坐标
        :type X: int
        :param _Y: 左上角Y坐标
        :type Y: int
        :param _Width: 方框宽度
        :type Width: int
        :param _Height: 方框高度
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
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
        


class ResultConfig(AbstractModel):
    """返回结果配置

    """

    def __init__(self):
        r"""
        :param _Resolution: 生成图分辨率
支持生成以下不同分辨率的图片，对应1:1方图、3:4竖图、4:3横图三种尺寸规格。
取值：
● 768:768
● 768:1024
● 1024:768
        :type Resolution: str
        """
        self._Resolution = None

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution


    def _deserialize(self, params):
        self._Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageRequest(AbstractModel):
    """TextToImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本描述。
算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。
不能为空，推荐使用中文。最多可传512个 utf-8 字符。
        :type Prompt: str
        :param _NegativePrompt: 反向文本描述。
用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。
推荐使用中文。最多可传512个 utf-8 字符。
        :type NegativePrompt: str
        :param _Styles: 绘画风格。
请在 [智能文生图风格列表](https://cloud.tencent.com/document/product/1668/86249) 中选择期望的风格，传入风格编号。
推荐使用且只使用一种风格。不传默认使用201（日系动漫风格）。
如果想要探索风格列表之外的风格，也可以尝试在 Prompt 中输入其他的风格描述。
        :type Styles: list of str
        :param _ResultConfig: 生成图结果的配置，包括输出图片分辨率和尺寸等。
        :type ResultConfig: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        :param _LogoAdd: 为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        self._Prompt = None
        self._NegativePrompt = None
        self._Styles = None
        self._ResultConfig = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Styles(self):
        return self._Styles

    @Styles.setter
    def Styles(self, Styles):
        self._Styles = Styles

    @property
    def ResultConfig(self):
        return self._ResultConfig

    @ResultConfig.setter
    def ResultConfig(self, ResultConfig):
        self._ResultConfig = ResultConfig

    @property
    def LogoAdd(self):
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Styles = params.get("Styles")
        if params.get("ResultConfig") is not None:
            self._ResultConfig = ResultConfig()
            self._ResultConfig._deserialize(params.get("ResultConfig"))
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageResponse(AbstractModel):
    """TextToImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 返回的生成图 Base64 编码。
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")