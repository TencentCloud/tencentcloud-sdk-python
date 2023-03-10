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
        :param InputImage: 输入图 Base64 数据。
算法将根据输入的图片，结合文本描述智能生成与之相关的图像。
Base64 和 Url 必须提供一个，如果都提供以 Base64 为准。
图片限制：单边分辨率小于2000，转成 Base64 字符串后小于 5MB。
        :type InputImage: str
        :param InputUrl: 输入图 Url。
算法将根据输入的图片，结合文本描述智能生成与之相关的图像。
Base64 和 Url 必须提供一个，如果都提供以 Base64 为准。
图片限制：单边分辨率小于2000，转成 Base64 字符串后小于 5MB。
        :type InputUrl: str
        :param Prompt: 文本描述。
用于在输入图的基础上引导生成图效果，建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。推荐使用中文。最多支持512个 utf-8 字符。
注意：如果不输入任何文本描述，可能导致较差的效果，建议根据期望的效果输入相应的文本描述。
        :type Prompt: str
        :param NegativePrompt: 反向文本描述。
用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。
推荐使用中文。最多可传512个 utf-8 字符。
        :type NegativePrompt: str
        :param Styles: 绘画风格。
请在  [智能图生图风格列表](https://cloud.tencent.com/document/product/1668/86250) 中选择期望的风格，传入风格编号。
推荐使用且只使用一种风格。不传默认使用201（日系动漫风格）。
如果想要探索风格列表之外的风格，也可以尝试在 Prompt 中输入其他的风格描述。
        :type Styles: list of str
        :param ResultConfig: 生成图结果的配置，包括输出图片分辨率和尺寸等。
        :type ResultConfig: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        :param LogoAdd: 为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param Strength: 生成自由度。
Strength 值越小，生成图和原图越接近。取值范围0~1，不传默认为0.6。
        :type Strength: float
        """
        self.InputImage = None
        self.InputUrl = None
        self.Prompt = None
        self.NegativePrompt = None
        self.Styles = None
        self.ResultConfig = None
        self.LogoAdd = None
        self.LogoParam = None
        self.Strength = None


    def _deserialize(self, params):
        self.InputImage = params.get("InputImage")
        self.InputUrl = params.get("InputUrl")
        self.Prompt = params.get("Prompt")
        self.NegativePrompt = params.get("NegativePrompt")
        self.Styles = params.get("Styles")
        if params.get("ResultConfig") is not None:
            self.ResultConfig = ResultConfig()
            self.ResultConfig._deserialize(params.get("ResultConfig"))
        self.LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self.LogoParam = LogoParam()
            self.LogoParam._deserialize(params.get("LogoParam"))
        self.Strength = params.get("Strength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToImageResponse(AbstractModel):
    """ImageToImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultImage: 返回的生成图 Base64 编码。
        :type ResultImage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.RequestId = params.get("RequestId")


class LogoParam(AbstractModel):
    """logo参数

    """

    def __init__(self):
        r"""
        :param LogoUrl: 水印url
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoUrl: str
        :param LogoImage: 水印base64，url和base64二选一传入
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoImage: str
        :param LogoRect: 水印图片位于融合结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoRect: :class:`tencentcloud.aiart.v20221229.models.LogoRect`
        """
        self.LogoUrl = None
        self.LogoImage = None
        self.LogoRect = None


    def _deserialize(self, params):
        self.LogoUrl = params.get("LogoUrl")
        self.LogoImage = params.get("LogoImage")
        if params.get("LogoRect") is not None:
            self.LogoRect = LogoRect()
            self.LogoRect._deserialize(params.get("LogoRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoRect(AbstractModel):
    """输入框

    """

    def __init__(self):
        r"""
        :param X: 左上角X坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param Y: 左上角Y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        :param Width: 方框宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 方框高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultConfig(AbstractModel):
    """返回结果配置

    """

    def __init__(self):
        r"""
        :param Resolution: 生成图分辨率
支持生成以下不同分辨率的图片，对应1:1方图、3:4竖图、4:3横图三种尺寸规格，不传默认为"768:768"
取值：
● 768:768
● 768:1024
● 1024:768
注意：此字段可能返回 null，表示取不到有效值。
        :type Resolution: str
        """
        self.Resolution = None


    def _deserialize(self, params):
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageRequest(AbstractModel):
    """TextToImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Prompt: 文本描述。
算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。
不能为空，推荐使用中文。最多可传512个 utf-8 字符。
        :type Prompt: str
        :param NegativePrompt: 反向文本描述。
用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。
推荐使用中文。最多可传512个 utf-8 字符。
        :type NegativePrompt: str
        :param Styles: 绘画风格。
请在 [智能文生图风格列表](https://cloud.tencent.com/document/product/1668/86249) 中选择期望的风格，传入风格编号。
推荐使用且只使用一种风格。不传默认使用201（日系动漫风格）。
如果想要探索风格列表之外的风格，也可以尝试在 Prompt 中输入其他的风格描述。
        :type Styles: list of str
        :param ResultConfig: 生成图结果的配置，包括输出图片分辨率和尺寸等。
        :type ResultConfig: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        :param LogoAdd: 为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        self.Prompt = None
        self.NegativePrompt = None
        self.Styles = None
        self.ResultConfig = None
        self.LogoAdd = None
        self.LogoParam = None


    def _deserialize(self, params):
        self.Prompt = params.get("Prompt")
        self.NegativePrompt = params.get("NegativePrompt")
        self.Styles = params.get("Styles")
        if params.get("ResultConfig") is not None:
            self.ResultConfig = ResultConfig()
            self.ResultConfig._deserialize(params.get("ResultConfig"))
        self.LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self.LogoParam = LogoParam()
            self.LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageResponse(AbstractModel):
    """TextToImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultImage: 返回的生成图 Base64 编码。
        :type ResultImage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.RequestId = params.get("RequestId")