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


class ChangeClothesRequest(AbstractModel):
    r"""ChangeClothes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelUrl: 模特图片 Url。
图片限制：单边分辨率小于3000，且大于512，转成 Base64 字符串后小于 8MB。
输入要求：
1、建议上传正面模特图片，至少完整露出应穿着输入指定服装的身体部位（全身、上半身或下半身），无大角度身体偏转或异常姿势。
2、建议上传3:4比例的图片，生成效果更佳。
3、建议模特图片中的原始服装和更换后的服装类别一致，或原始服装在身体上的覆盖范围小于等于更换后的服装（例如需要给模特换上短裤，则原始模特图片中也建议穿短裤，不建议穿长裤），否则会影响人像生成效果。

        :type ModelUrl: str
        :param _ClothesUrl: 服装图片 Url。
图片限制：单边分辨率小于3000，大于512，转成 Base64 字符串后小于 8MB。
输入要求：
建议上传服装完整的正面平铺图片，仅包含1个服装主体，服装类型支持上衣、下装、连衣裙，三选一。算法将根据输入的图片，结合服装图片给模特换装。
        :type ClothesUrl: str
        :param _ClothesType: 服装类型，需要和服装图片保持一致。
取值：
Upper-body：上衣
Lower-body：下装
Dress：连衣裙
        :type ClothesType: str
        :param _LogoAdd: 为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _RspImgType: 返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。
生成图分辨率较大时建议选择 url，使用 base64 可能因图片过大导致返回失败。
        :type RspImgType: str
        """
        self._ModelUrl = None
        self._ClothesUrl = None
        self._ClothesType = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def ModelUrl(self):
        r"""模特图片 Url。
图片限制：单边分辨率小于3000，且大于512，转成 Base64 字符串后小于 8MB。
输入要求：
1、建议上传正面模特图片，至少完整露出应穿着输入指定服装的身体部位（全身、上半身或下半身），无大角度身体偏转或异常姿势。
2、建议上传3:4比例的图片，生成效果更佳。
3、建议模特图片中的原始服装和更换后的服装类别一致，或原始服装在身体上的覆盖范围小于等于更换后的服装（例如需要给模特换上短裤，则原始模特图片中也建议穿短裤，不建议穿长裤），否则会影响人像生成效果。

        :rtype: str
        """
        return self._ModelUrl

    @ModelUrl.setter
    def ModelUrl(self, ModelUrl):
        self._ModelUrl = ModelUrl

    @property
    def ClothesUrl(self):
        r"""服装图片 Url。
图片限制：单边分辨率小于3000，大于512，转成 Base64 字符串后小于 8MB。
输入要求：
建议上传服装完整的正面平铺图片，仅包含1个服装主体，服装类型支持上衣、下装、连衣裙，三选一。算法将根据输入的图片，结合服装图片给模特换装。
        :rtype: str
        """
        return self._ClothesUrl

    @ClothesUrl.setter
    def ClothesUrl(self, ClothesUrl):
        self._ClothesUrl = ClothesUrl

    @property
    def ClothesType(self):
        r"""服装类型，需要和服装图片保持一致。
取值：
Upper-body：上衣
Lower-body：下装
Dress：连衣裙
        :rtype: str
        """
        return self._ClothesType

    @ClothesType.setter
    def ClothesType(self, ClothesType):
        self._ClothesType = ClothesType

    @property
    def LogoAdd(self):
        r"""为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        r"""返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。
生成图分辨率较大时建议选择 url，使用 base64 可能因图片过大导致返回失败。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._ModelUrl = params.get("ModelUrl")
        self._ClothesUrl = params.get("ClothesUrl")
        self._ClothesType = params.get("ClothesType")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeClothesResponse(AbstractModel):
    r"""ChangeClothes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 根据入参 RspImgType 填入不同，返回不同的内容。
如果传入 base64 则返回生成图 Base64 编码。
如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""根据入参 RspImgType 填入不同，返回不同的内容。
如果传入 base64 则返回生成图 Base64 编码。
如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class FaceInfo(AbstractModel):
    r"""融合信息

    """

    def __init__(self):
        r"""
        :param _ImageUrls: 用户图 URL 列表
        :type ImageUrls: list of str
        :param _TemplateFaceRect: 模板图人脸坐标。
        :type TemplateFaceRect: :class:`tencentcloud.aiart.v20221229.models.Rect`
        """
        self._ImageUrls = None
        self._TemplateFaceRect = None

    @property
    def ImageUrls(self):
        r"""用户图 URL 列表
        :rtype: list of str
        """
        return self._ImageUrls

    @ImageUrls.setter
    def ImageUrls(self, ImageUrls):
        self._ImageUrls = ImageUrls

    @property
    def TemplateFaceRect(self):
        r"""模板图人脸坐标。
        :rtype: :class:`tencentcloud.aiart.v20221229.models.Rect`
        """
        return self._TemplateFaceRect

    @TemplateFaceRect.setter
    def TemplateFaceRect(self, TemplateFaceRect):
        self._TemplateFaceRect = TemplateFaceRect


    def _deserialize(self, params):
        self._ImageUrls = params.get("ImageUrls")
        if params.get("TemplateFaceRect") is not None:
            self._TemplateFaceRect = Rect()
            self._TemplateFaceRect._deserialize(params.get("TemplateFaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""训练图像质量过滤开关配置。
    支持开启或关闭对训练图像分辨率下限、脸部区域大小、脸部遮挡、脸部角度的过滤，默认开启以上过滤。
    如果训练图像内包含多人脸或无人脸、和 Base 人像不为同一人也将被过滤，不可关闭该过滤条件。
    建议：关闭以上过滤可能导致写真生成效果受损，建议使用单人、正脸、脸部清晰、无遮挡、无夸张表情、脸部区域占比较大的图像进行训练。

    """

    def __init__(self):
        r"""
        :param _Resolution: 过滤不满足分辨率下限的训练图像，默认开启过滤
开启后将过滤横边<512或竖边<720的图片，横、竖边上限均为2000，不支持调整

1：开启过滤
0：关闭过滤
        :type Resolution: int
        :param _Size: 过滤脸部区域过小的训练图像，默认开启过滤

1：开启过滤
0：关闭过滤
        :type Size: int
        :param _Occlusion: 过滤脸部存在明显遮挡、偏转角度过大等质量较差的训练图像，默认开启过滤

1：开启过滤
0：关闭过滤
        :type Occlusion: int
        """
        self._Resolution = None
        self._Size = None
        self._Occlusion = None

    @property
    def Resolution(self):
        r"""过滤不满足分辨率下限的训练图像，默认开启过滤
开启后将过滤横边<512或竖边<720的图片，横、竖边上限均为2000，不支持调整

1：开启过滤
0：关闭过滤
        :rtype: int
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Size(self):
        r"""过滤脸部区域过小的训练图像，默认开启过滤

1：开启过滤
0：关闭过滤
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Occlusion(self):
        r"""过滤脸部存在明显遮挡、偏转角度过大等质量较差的训练图像，默认开启过滤

1：开启过滤
0：关闭过滤
        :rtype: int
        """
        return self._Occlusion

    @Occlusion.setter
    def Occlusion(self, Occlusion):
        self._Occlusion = Occlusion


    def _deserialize(self, params):
        self._Resolution = params.get("Resolution")
        self._Size = params.get("Size")
        self._Occlusion = params.get("Occlusion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateAvatarRequest(AbstractModel):
    r"""GenerateAvatar请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: <p>图像类型，默认为人像。<br>human：人像头像，仅支持人像图片输入，建议避免上传无人、多人、人像过小的图片。<br>pet：萌宠贴纸，仅支持动物图片输入，建议避免上传无动物、多动物、动物过小的图片。</p>
        :type Type: str
        :param _Style: <p>头像风格，仅在人像模式下生效。<br>若使用人像模式，请在  <a href="https://cloud.tencent.com/document/product/1668/107741">百变头像风格列表</a> 中选择期望的风格，传入风格编号，不传默认使用 flower 风格。<br>若使用萌宠贴纸模式，无需选择风格，该参数不生效。</p>
        :type Style: str
        :param _InputImage: <p>输入图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputImage: str
        :param _InputUrl: <p>输入图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputUrl: str
        :param _Filter: <p>输入人像图的质量检测开关，默认开启，仅在人像模式下生效。<br>1：开启<br>0：关闭<br>建议开启检测，可提升生成效果，关闭检测可能因输入图像质量较差导致生成效果受损。<br>开启后，将增强对输入图像的质量要求，如果输入图像单边分辨率&lt;500、图像中人脸占比较小、存在多人、没有检测到人脸、人脸不完整、人脸遮挡等，将被拦截。<br>关闭后，将降低对输入图像的质量要求，如果图像中没有检测到人脸或人脸占比过小等，将被拦截。</p>
        :type Filter: int
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _RspImgType: <p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。</p>
        :type RspImgType: str
        """
        self._Type = None
        self._Style = None
        self._InputImage = None
        self._InputUrl = None
        self._Filter = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def Type(self):
        r"""<p>图像类型，默认为人像。<br>human：人像头像，仅支持人像图片输入，建议避免上传无人、多人、人像过小的图片。<br>pet：萌宠贴纸，仅支持动物图片输入，建议避免上传无动物、多动物、动物过小的图片。</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Style(self):
        r"""<p>头像风格，仅在人像模式下生效。<br>若使用人像模式，请在  <a href="https://cloud.tencent.com/document/product/1668/107741">百变头像风格列表</a> 中选择期望的风格，传入风格编号，不传默认使用 flower 风格。<br>若使用萌宠贴纸模式，无需选择风格，该参数不生效。</p>
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def InputImage(self):
        r"""<p>输入图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        r"""<p>输入图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def Filter(self):
        r"""<p>输入人像图的质量检测开关，默认开启，仅在人像模式下生效。<br>1：开启<br>0：关闭<br>建议开启检测，可提升生成效果，关闭检测可能因输入图像质量较差导致生成效果受损。<br>开启后，将增强对输入图像的质量要求，如果输入图像单边分辨率&lt;500、图像中人脸占比较小、存在多人、没有检测到人脸、人脸不完整、人脸遮挡等，将被拦截。<br>关闭后，将降低对输入图像的质量要求，如果图像中没有检测到人脸或人脸占比过小等，将被拦截。</p>
        :rtype: int
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Style = params.get("Style")
        self._InputImage = params.get("InputImage")
        self._InputUrl = params.get("InputUrl")
        self._Filter = params.get("Filter")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateAvatarResponse(AbstractModel):
    r"""GenerateAvatar返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class Image(AbstractModel):
    r"""图片

    """

    def __init__(self):
        r"""
        :param _Base64: 图片Base64
        :type Base64: str
        :param _Url: 图片Url
        :type Url: str
        """
        self._Base64 = None
        self._Url = None

    @property
    def Base64(self):
        r"""图片Base64
        :rtype: str
        """
        return self._Base64

    @Base64.setter
    def Base64(self, Base64):
        self._Base64 = Base64

    @property
    def Url(self):
        r"""图片Url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Base64 = params.get("Base64")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInpaintingRemovalRequest(AbstractModel):
    r"""ImageInpaintingRemoval请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InputImage: <p>输入图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputImage: str
        :param _InputUrl: <p>输入图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputUrl: str
        :param _Mask: <p>消除区域 Mask 图 Base64 数据。<br>Mask 为单通道灰度图，待消除部分呈白色区域，原图保持部分呈黑色区域。<br>Mask 的 Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：Mask 分辨率需要和输入原图保持一致，转成 Base64 字符串后小于 6MB。</p>
        :type Mask: str
        :param _MaskUrl: <p>消除区域 Mask 图 Url。<br>Mask 为单通道灰度图，待消除部分呈白色区域，原图保持部分呈黑色区域。<br>Mask 的 Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：Mask 分辨率需要和输入原图保持一致，转成 Base64 字符串后小于 6MB。</p>
        :type MaskUrl: str
        :param _RspImgType: <p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :type RspImgType: str
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        self._InputImage = None
        self._InputUrl = None
        self._Mask = None
        self._MaskUrl = None
        self._RspImgType = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def InputImage(self):
        r"""<p>输入图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        r"""<p>输入图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def Mask(self):
        r"""<p>消除区域 Mask 图 Base64 数据。<br>Mask 为单通道灰度图，待消除部分呈白色区域，原图保持部分呈黑色区域。<br>Mask 的 Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：Mask 分辨率需要和输入原图保持一致，转成 Base64 字符串后小于 6MB。</p>
        :rtype: str
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def MaskUrl(self):
        r"""<p>消除区域 Mask 图 Url。<br>Mask 为单通道灰度图，待消除部分呈白色区域，原图保持部分呈黑色区域。<br>Mask 的 Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：Mask 分辨率需要和输入原图保持一致，转成 Base64 字符串后小于 6MB。</p>
        :rtype: str
        """
        return self._MaskUrl

    @MaskUrl.setter
    def MaskUrl(self, MaskUrl):
        self._MaskUrl = MaskUrl

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._InputImage = params.get("InputImage")
        self._InputUrl = params.get("InputUrl")
        self._Mask = params.get("Mask")
        self._MaskUrl = params.get("MaskUrl")
        self._RspImgType = params.get("RspImgType")
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
        


class ImageInpaintingRemovalResponse(AbstractModel):
    r"""ImageInpaintingRemoval返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。 如果传入 base64 则返回生成图 Base64 编码。 如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。 如果传入 base64 则返回生成图 Base64 编码。 如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class ImageOutpaintingRequest(AbstractModel):
    r"""ImageOutpainting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ratio: <p>扩展后的比例（宽:高），需要不等于原图比例。<br>支持：1:1、4:3、3:4、16:9、9:16</p>
        :type Ratio: str
        :param _InputImage: <p>输入图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputImage: str
        :param _InputUrl: <p>输入图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputUrl: str
        :param _RspImgType: <p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :type RspImgType: str
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        self._Ratio = None
        self._InputImage = None
        self._InputUrl = None
        self._RspImgType = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Ratio(self):
        r"""<p>扩展后的比例（宽:高），需要不等于原图比例。<br>支持：1:1、4:3、3:4、16:9、9:16</p>
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio

    @property
    def InputImage(self):
        r"""<p>输入图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        r"""<p>输入图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Ratio = params.get("Ratio")
        self._InputImage = params.get("InputImage")
        self._InputUrl = params.get("InputUrl")
        self._RspImgType = params.get("RspImgType")
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
        


class ImageOutpaintingResponse(AbstractModel):
    r"""ImageOutpainting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class ImageToImageRequest(AbstractModel):
    r"""ImageToImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InputImage: <p>输入图 Base64 数据。<br>算法将根据输入的图片，结合文本描述智能生成与之相关的图像。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px且大于50px，转成 Base64 字符串后小于 8MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputImage: str
        :param _InputUrl: <p>输入图 Url。<br>算法将根据输入的图片，结合文本描述智能生成与之相关的图像。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px且大于50px，转成 Base64 字符串后小于 8MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputUrl: str
        :param _Prompt: <p>文本描述。<br>用于在输入图的基础上引导生成图效果，增加生成结果中出现描述内容的可能。<br>推荐使用中文。最多支持256个 utf-8 字符。</p>
        :type Prompt: str
        :param _NegativePrompt: <p>反向文本描述。<br>用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。<br>推荐使用中文。最多可传256个 utf-8 字符。</p>
        :type NegativePrompt: str
        :param _Styles: <p>绘画风格。<br>请在  <a href="https://cloud.tencent.com/document/product/1668/86250">图像风格化风格列表</a> 中选择期望的风格，传入风格编号。<br>推荐使用且只使用一种风格。不传默认使用201（日系动漫风格）。</p>
        :type Styles: list of str
        :param _ResultConfig: <p>生成图结果的配置，包括输出图片分辨率和尺寸等。<br>支持生成以下分辨率的图片：origin（与输入图分辨率一致，长边最高为2000，超出将做等比例缩小）、768:768（1:1）、768:1024（3:4）、1024:768（4:3）。<br>不传默认使用origin。<br>单位为 px。</p>
        :type ResultConfig: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _Strength: <p>生成自由度。<br>Strength 值越小，生成图和原图越接近，取值范围(0, 1]，不传使用模型内置的默认值。<br>推荐的取值范围为0.6 - 0.8。</p>
        :type Strength: float
        :param _RspImgType: <p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。</p>
        :type RspImgType: str
        :param _EnhanceImage: <p>画质增强开关，默认关闭。<br>1：开启<br>0：关闭<br>开启后将增强图像的画质清晰度，生成耗时有所增加。</p>
        :type EnhanceImage: int
        :param _RestoreFace: <p>细节优化的面部数量上限，支持0 ~ 6，默认为0。<br>若上传大于0的值，将以此为上限对每张图片中面积占比较小的面部进行细节修复，生成耗时根据实际优化的面部个数有所增加。</p>
        :type RestoreFace: int
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
        self._RspImgType = None
        self._EnhanceImage = None
        self._RestoreFace = None

    @property
    def InputImage(self):
        r"""<p>输入图 Base64 数据。<br>算法将根据输入的图片，结合文本描述智能生成与之相关的图像。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px且大于50px，转成 Base64 字符串后小于 8MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        r"""<p>输入图 Url。<br>算法将根据输入的图片，结合文本描述智能生成与之相关的图像。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px且大于50px，转成 Base64 字符串后小于 8MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def Prompt(self):
        r"""<p>文本描述。<br>用于在输入图的基础上引导生成图效果，增加生成结果中出现描述内容的可能。<br>推荐使用中文。最多支持256个 utf-8 字符。</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        r"""<p>反向文本描述。<br>用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。<br>推荐使用中文。最多可传256个 utf-8 字符。</p>
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Styles(self):
        r"""<p>绘画风格。<br>请在  <a href="https://cloud.tencent.com/document/product/1668/86250">图像风格化风格列表</a> 中选择期望的风格，传入风格编号。<br>推荐使用且只使用一种风格。不传默认使用201（日系动漫风格）。</p>
        :rtype: list of str
        """
        return self._Styles

    @Styles.setter
    def Styles(self, Styles):
        self._Styles = Styles

    @property
    def ResultConfig(self):
        r"""<p>生成图结果的配置，包括输出图片分辨率和尺寸等。<br>支持生成以下分辨率的图片：origin（与输入图分辨率一致，长边最高为2000，超出将做等比例缩小）、768:768（1:1）、768:1024（3:4）、1024:768（4:3）。<br>不传默认使用origin。<br>单位为 px。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        """
        return self._ResultConfig

    @ResultConfig.setter
    def ResultConfig(self, ResultConfig):
        self._ResultConfig = ResultConfig

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Strength(self):
        r"""<p>生成自由度。<br>Strength 值越小，生成图和原图越接近，取值范围(0, 1]，不传使用模型内置的默认值。<br>推荐的取值范围为0.6 - 0.8。</p>
        :rtype: float
        """
        return self._Strength

    @Strength.setter
    def Strength(self, Strength):
        self._Strength = Strength

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def EnhanceImage(self):
        r"""<p>画质增强开关，默认关闭。<br>1：开启<br>0：关闭<br>开启后将增强图像的画质清晰度，生成耗时有所增加。</p>
        :rtype: int
        """
        return self._EnhanceImage

    @EnhanceImage.setter
    def EnhanceImage(self, EnhanceImage):
        self._EnhanceImage = EnhanceImage

    @property
    def RestoreFace(self):
        r"""<p>细节优化的面部数量上限，支持0 ~ 6，默认为0。<br>若上传大于0的值，将以此为上限对每张图片中面积占比较小的面部进行细节修复，生成耗时根据实际优化的面部个数有所增加。</p>
        :rtype: int
        """
        return self._RestoreFace

    @RestoreFace.setter
    def RestoreFace(self, RestoreFace):
        self._RestoreFace = RestoreFace


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
        self._RspImgType = params.get("RspImgType")
        self._EnhanceImage = params.get("EnhanceImage")
        self._RestoreFace = params.get("RestoreFace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToImageResponse(AbstractModel):
    r"""ImageToImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class LogoParam(AbstractModel):
    r"""logo参数

    """

    def __init__(self):
        r"""
        :param _LogoUrl: 水印 Url
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoUrl: str
        :param _LogoImage: 水印 Base64，Url 和 Base64 二选一传入，如果都提供以 Url 为准
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoImage: str
        :param _LogoRect: 水印图片位于生成结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoRect: :class:`tencentcloud.aiart.v20221229.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        r"""水印 Url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        r"""水印 Base64，Url 和 Base64 二选一传入，如果都提供以 Url 为准
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        r"""水印图片位于生成结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoRect`
        """
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
    r"""输入框

    """

    def __init__(self):
        r"""
        :param _X: <p>左上角X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param _Y: <p>左上角Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        :param _Width: <p>方框宽度<br>单位为 px</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: <p>方框高度<br>单位为 px</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""<p>左上角X坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""<p>左上角Y坐标</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""<p>方框宽度<br>单位为 px</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""<p>方框高度<br>单位为 px</p>
注意：此字段可能返回 null，表示取不到有效值。
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
        


class QueryDrawPortraitJobRequest(AbstractModel):
    r"""QueryDrawPortraitJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 查询生成写真图片任务 ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""查询生成写真图片任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDrawPortraitJobResponse(AbstractModel):
    r"""QueryDrawPortraitJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 任务状态码。
INIT: 初始化、WAIT：等待中、RUN：运行中、FAIL：处理失败、DONE：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 任务状态信息。
        :type JobStatusMsg: str
        :param _JobErrorCode: 任务错误码。
        :type JobErrorCode: str
        :param _JobErrorMsg: 任务错误信息。
        :type JobErrorMsg: str
        :param _ResultUrls: 结果 URL 数组。
URL 有效期1小时，请及时保存。
        :type ResultUrls: list of str
        :param _ResultDetails: 结果描述数组。
        :type ResultDetails: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultUrls = None
        self._ResultDetails = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        r"""任务状态码。
INIT: 初始化、WAIT：等待中、RUN：运行中、FAIL：处理失败、DONE：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        r"""任务状态信息。
        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        r"""任务错误码。
        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        r"""任务错误信息。
        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultUrls(self):
        r"""结果 URL 数组。
URL 有效期1小时，请及时保存。
        :rtype: list of str
        """
        return self._ResultUrls

    @ResultUrls.setter
    def ResultUrls(self, ResultUrls):
        self._ResultUrls = ResultUrls

    @property
    def ResultDetails(self):
        r"""结果描述数组。
        :rtype: list of str
        """
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

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
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultUrls = params.get("ResultUrls")
        self._ResultDetails = params.get("ResultDetails")
        self._RequestId = params.get("RequestId")


class QueryGlamPicJobRequest(AbstractModel):
    r"""QueryGlamPicJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryGlamPicJobResponse(AbstractModel):
    r"""QueryGlamPicJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 当前任务状态：排队中、处理中、处理失败或者处理完成。

        :type JobStatusMsg: str
        :param _JobErrorCode: 任务处理失败错误码。

        :type JobErrorCode: str
        :param _JobErrorMsg: 任务处理失败错误信息。

        :type JobErrorMsg: str
        :param _ResultImage: 生成图 URL 列表，有效期1小时，请及时保存。

        :type ResultImage: list of str
        :param _ResultDetails: 结果 detail 数组，Success 代表成功。

        :type ResultDetails: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultImage = None
        self._ResultDetails = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        r"""当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        r"""当前任务状态：排队中、处理中、处理失败或者处理完成。

        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        r"""任务处理失败错误码。

        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        r"""任务处理失败错误信息。

        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultImage(self):
        r"""生成图 URL 列表，有效期1小时，请及时保存。

        :rtype: list of str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultDetails(self):
        r"""结果 detail 数组，Success 代表成功。

        :rtype: list of str
        """
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

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
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultImage = params.get("ResultImage")
        self._ResultDetails = params.get("ResultDetails")
        self._RequestId = params.get("RequestId")


class QueryMemeJobRequest(AbstractModel):
    r"""QueryMemeJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 查询表情动图生成任务 ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""查询表情动图生成任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemeJobResponse(AbstractModel):
    r"""QueryMemeJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 当前任务状态：排队中、处理中、处理失败或者处理完成。
        :type JobStatusMsg: str
        :param _JobErrorCode: 任务处理失败错误码。

        :type JobErrorCode: str
        :param _JobErrorMsg: 任务处理失败错误信息。

        :type JobErrorMsg: str
        :param _ResultImage: 生成图 URL，有效期1小时，请及时保存。
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultImage = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        r"""当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        r"""当前任务状态：排队中、处理中、处理失败或者处理完成。
        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        r"""任务处理失败错误码。

        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        r"""任务处理失败错误信息。

        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultImage(self):
        r"""生成图 URL，有效期1小时，请及时保存。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class QueryTextToImageJobRequest(AbstractModel):
    r"""QueryTextToImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTextToImageJobResponse(AbstractModel):
    r"""QueryTextToImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 当前任务状态：排队中、处理中、处理失败或者处理完成。

        :type JobStatusMsg: str
        :param _JobErrorCode: 任务处理失败错误码。

        :type JobErrorCode: str
        :param _JobErrorMsg: 任务处理失败错误信息。

        :type JobErrorMsg: str
        :param _ResultImage: 生成图 URL 列表，有效期1小时，请及时保存。

        :type ResultImage: list of str
        :param _ResultDetails: 结果 detail 数组，Success 代表成功。

        :type ResultDetails: list of str
        :param _RevisedPrompt: 对应 SubmitTextToImageProJob 接口中 Revise 参数。开启扩写时，返回扩写后的 prompt 文本。 如果关闭扩写，将直接返回原始输入的 prompt。
        :type RevisedPrompt: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultImage = None
        self._ResultDetails = None
        self._RevisedPrompt = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        r"""当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        r"""当前任务状态：排队中、处理中、处理失败或者处理完成。

        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        r"""任务处理失败错误码。

        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        r"""任务处理失败错误信息。

        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultImage(self):
        r"""生成图 URL 列表，有效期1小时，请及时保存。

        :rtype: list of str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultDetails(self):
        r"""结果 detail 数组，Success 代表成功。

        :rtype: list of str
        """
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

    @property
    def RevisedPrompt(self):
        r"""对应 SubmitTextToImageProJob 接口中 Revise 参数。开启扩写时，返回扩写后的 prompt 文本。 如果关闭扩写，将直接返回原始输入的 prompt。
        :rtype: list of str
        """
        return self._RevisedPrompt

    @RevisedPrompt.setter
    def RevisedPrompt(self, RevisedPrompt):
        self._RevisedPrompt = RevisedPrompt

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
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultImage = params.get("ResultImage")
        self._ResultDetails = params.get("ResultDetails")
        self._RevisedPrompt = params.get("RevisedPrompt")
        self._RequestId = params.get("RequestId")


class QueryTextToImageProJobRequest(AbstractModel):
    r"""QueryTextToImageProJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTextToImageProJobResponse(AbstractModel):
    r"""QueryTextToImageProJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 当前任务状态：排队中、处理中、处理失败或者处理完成。

        :type JobStatusMsg: str
        :param _JobErrorCode: 任务处理失败错误码。

        :type JobErrorCode: str
        :param _JobErrorMsg: 任务处理失败错误信息。

        :type JobErrorMsg: str
        :param _ResultImage: 生成图 URL 列表，有效期1小时，请及时保存。

        :type ResultImage: list of str
        :param _ResultDetails: 结果 detail 数组，Success 代表成功。

        :type ResultDetails: list of str
        :param _RevisedPrompt: 对应 SubmitTextToImageProJob 接口中 Revise 参数。开启扩写时，返回扩写后的 prompt 文本。 如果关闭扩写，将直接返回原始输入的 prompt。
        :type RevisedPrompt: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultImage = None
        self._ResultDetails = None
        self._RevisedPrompt = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        r"""当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        r"""当前任务状态：排队中、处理中、处理失败或者处理完成。

        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        r"""任务处理失败错误码。

        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        r"""任务处理失败错误信息。

        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultImage(self):
        r"""生成图 URL 列表，有效期1小时，请及时保存。

        :rtype: list of str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultDetails(self):
        r"""结果 detail 数组，Success 代表成功。

        :rtype: list of str
        """
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

    @property
    def RevisedPrompt(self):
        r"""对应 SubmitTextToImageProJob 接口中 Revise 参数。开启扩写时，返回扩写后的 prompt 文本。 如果关闭扩写，将直接返回原始输入的 prompt。
        :rtype: list of str
        """
        return self._RevisedPrompt

    @RevisedPrompt.setter
    def RevisedPrompt(self, RevisedPrompt):
        self._RevisedPrompt = RevisedPrompt

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
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultImage = params.get("ResultImage")
        self._ResultDetails = params.get("ResultDetails")
        self._RevisedPrompt = params.get("RevisedPrompt")
        self._RequestId = params.get("RequestId")


class QueryTrainPortraitModelJobRequest(AbstractModel):
    r"""QueryTrainPortraitModelJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 写真模型 ID。

        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        r"""写真模型 ID。

        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTrainPortraitModelJobResponse(AbstractModel):
    r"""QueryTrainPortraitModelJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 任务状态码。
INIT: 初始化、WAIT：等待中、RUN：运行中、FAIL：处理失败、DONE：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 任务状态信息。
        :type JobStatusMsg: str
        :param _JobErrorCode: 任务错误码。
        :type JobErrorCode: str
        :param _JobErrorMsg: 任务错误信息。
        :type JobErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        r"""任务状态码。
INIT: 初始化、WAIT：等待中、RUN：运行中、FAIL：处理失败、DONE：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        r"""任务状态信息。
        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        r"""任务错误码。
        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        r"""任务错误信息。
        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

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
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._RequestId = params.get("RequestId")


class Rect(AbstractModel):
    r"""人脸框坐标

    """

    def __init__(self):
        r"""
        :param _X: <p>人脸框左上角横坐标。</p>
        :type X: int
        :param _Y: <p>人脸框左上角纵坐标。</p>
        :type Y: int
        :param _Width: <p>人脸框宽度。<br>单位：px</p>
        :type Width: int
        :param _Height: <p>人脸框高度。<br>单位：px</p>
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""<p>人脸框左上角横坐标。</p>
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""<p>人脸框左上角纵坐标。</p>
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""<p>人脸框宽度。<br>单位：px</p>
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""<p>人脸框高度。<br>单位：px</p>
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
        


class RefineImageRequest(AbstractModel):
    r"""RefineImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InputUrl: 输入图 Url。
Base64 和 Url 必须提供一个，如果都提供以 Url 为准。
图片限制：转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。
        :type InputUrl: str
        :param _InputImage: 输入图 Base64 数据。
Base64 和 Url 必须提供一个，如果都提供以 Url 为准。
图片限制：转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。
        :type InputImage: str
        :param _RspImgType: 返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。 示例值：url
        :type RspImgType: str
        """
        self._InputUrl = None
        self._InputImage = None
        self._RspImgType = None

    @property
    def InputUrl(self):
        r"""输入图 Url。
Base64 和 Url 必须提供一个，如果都提供以 Url 为准。
图片限制：转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def InputImage(self):
        r"""输入图 Base64 数据。
Base64 和 Url 必须提供一个，如果都提供以 Url 为准。
图片限制：转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def RspImgType(self):
        r"""返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。 示例值：url
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._InputUrl = params.get("InputUrl")
        self._InputImage = params.get("InputImage")
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefineImageResponse(AbstractModel):
    r"""RefineImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 根据入参 RspImgType 填入不同，返回不同的内容。
如果传入 base64 则返回生成图 Base64 编码。
如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""根据入参 RspImgType 填入不同，返回不同的内容。
如果传入 base64 则返回生成图 Base64 编码。
如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class ReplaceBackgroundRequest(AbstractModel):
    r"""ReplaceBackground请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductUrl: <p>商品原图 Url。<br>图片限制：单边分辨率小于4000px，长宽比在2:5 ~ 5:2之间，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type ProductUrl: str
        :param _Prompt: <p>对新背景的文本描述。<br>最多支持256个 utf-8 字符，支持中、英文。<br>如果 Prompt = &quot;BackgroundTemplate&quot; 代表启用背景模板，需要在参数 BackgroundTemplate 中指定一个背景名称。</p>
        :type Prompt: str
        :param _NegativePrompt: <p>反向提示词。<br>最多支持256个 utf-8 字符，支持中、英文。</p>
        :type NegativePrompt: str
        :param _Product: <p>商品图中的商品主体名称。<br>最多支持50个 utf-8 字符，支持中、英文。<br>建议说明商品主体，否则影响生成效果。</p>
        :type Product: str
        :param _BackgroundTemplate: <p>背景模板。<br>仅当 Prompt = &quot;BackgroundTemplate&quot; 时生效，可支持的模板详见 <a href="https://cloud.tencent.com/document/product/1668/115391">商品背景模板列表</a> ，请传入字段“背景名称”中的值。</p>
        :type BackgroundTemplate: str
        :param _MaskUrl: <p>商品 Mask 图 Url，要求背景透明，保留商品主体。<br>如果不传，将自动使用内置的商品分割算法得到 Mask。<br>支持自定义上传 Mask，如果该参数不为空，则以实际上传的数据为准。<br>图片限制：Mask 图必须和商品原图分辨率一致，转成 Base64 字符串后小于 6MB，格式仅支持 png。</p>
        :type MaskUrl: str
        :param _Resolution: <p>替换背景后生成的商品图分辨率。<br>支持生成单边分辨率大于500px且小于4000px、长宽比在2:5 ~ 5:2之间的图片，不传默认生成1280:1280。<br>建议图片比例为1:1、9:16、16:9，生成效果更佳，使用其他比例的生成效果可能不如建议比例。</p>
        :type Resolution: str
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _RspImgType: <p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。<br>生成图分辨率较大时建议选择 url，使用 base64 可能因图片过大导致返回失败。</p>
        :type RspImgType: str
        """
        self._ProductUrl = None
        self._Prompt = None
        self._NegativePrompt = None
        self._Product = None
        self._BackgroundTemplate = None
        self._MaskUrl = None
        self._Resolution = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def ProductUrl(self):
        r"""<p>商品原图 Url。<br>图片限制：单边分辨率小于4000px，长宽比在2:5 ~ 5:2之间，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._ProductUrl

    @ProductUrl.setter
    def ProductUrl(self, ProductUrl):
        self._ProductUrl = ProductUrl

    @property
    def Prompt(self):
        r"""<p>对新背景的文本描述。<br>最多支持256个 utf-8 字符，支持中、英文。<br>如果 Prompt = &quot;BackgroundTemplate&quot; 代表启用背景模板，需要在参数 BackgroundTemplate 中指定一个背景名称。</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        r"""<p>反向提示词。<br>最多支持256个 utf-8 字符，支持中、英文。</p>
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Product(self):
        r"""<p>商品图中的商品主体名称。<br>最多支持50个 utf-8 字符，支持中、英文。<br>建议说明商品主体，否则影响生成效果。</p>
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def BackgroundTemplate(self):
        r"""<p>背景模板。<br>仅当 Prompt = &quot;BackgroundTemplate&quot; 时生效，可支持的模板详见 <a href="https://cloud.tencent.com/document/product/1668/115391">商品背景模板列表</a> ，请传入字段“背景名称”中的值。</p>
        :rtype: str
        """
        return self._BackgroundTemplate

    @BackgroundTemplate.setter
    def BackgroundTemplate(self, BackgroundTemplate):
        self._BackgroundTemplate = BackgroundTemplate

    @property
    def MaskUrl(self):
        r"""<p>商品 Mask 图 Url，要求背景透明，保留商品主体。<br>如果不传，将自动使用内置的商品分割算法得到 Mask。<br>支持自定义上传 Mask，如果该参数不为空，则以实际上传的数据为准。<br>图片限制：Mask 图必须和商品原图分辨率一致，转成 Base64 字符串后小于 6MB，格式仅支持 png。</p>
        :rtype: str
        """
        return self._MaskUrl

    @MaskUrl.setter
    def MaskUrl(self, MaskUrl):
        self._MaskUrl = MaskUrl

    @property
    def Resolution(self):
        r"""<p>替换背景后生成的商品图分辨率。<br>支持生成单边分辨率大于500px且小于4000px、长宽比在2:5 ~ 5:2之间的图片，不传默认生成1280:1280。<br>建议图片比例为1:1、9:16、16:9，生成效果更佳，使用其他比例的生成效果可能不如建议比例。</p>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。<br>生成图分辨率较大时建议选择 url，使用 base64 可能因图片过大导致返回失败。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._ProductUrl = params.get("ProductUrl")
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Product = params.get("Product")
        self._BackgroundTemplate = params.get("BackgroundTemplate")
        self._MaskUrl = params.get("MaskUrl")
        self._Resolution = params.get("Resolution")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceBackgroundResponse(AbstractModel):
    r"""ReplaceBackground返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _MaskImage: <p>如果 MaskUrl 未传，则返回使用内置商品分割算法得到的 Mask 结果。</p>
        :type MaskImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._MaskImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def MaskImage(self):
        r"""<p>如果 MaskUrl 未传，则返回使用内置商品分割算法得到的 Mask 结果。</p>
        :rtype: str
        """
        return self._MaskImage

    @MaskImage.setter
    def MaskImage(self, MaskImage):
        self._MaskImage = MaskImage

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
        self._ResultImage = params.get("ResultImage")
        self._MaskImage = params.get("MaskImage")
        self._RequestId = params.get("RequestId")


class ResultConfig(AbstractModel):
    r"""返回结果配置

    """

    def __init__(self):
        r"""
        :param _Resolution: 生成图分辨率

图像风格化（图生图）支持生成以下分辨率的图片：origin（与输入图分辨率一致，长边最高为2000，超出将做等比例缩小）、768:768（1:1）、768:1024（3:4）、1024:768（4:3），不传默认使用origin，如果指定生成的长宽比与输入图长宽比差异过大可能导致图片内容被裁剪。
注意：此字段可能返回 null，表示取不到有效值。
        :type Resolution: str
        """
        self._Resolution = None

    @property
    def Resolution(self):
        r"""生成图分辨率

图像风格化（图生图）支持生成以下分辨率的图片：origin（与输入图分辨率一致，长边最高为2000，超出将做等比例缩小）、768:768（1:1）、768:1024（3:4）、1024:768（4:3），不传默认使用origin，如果指定生成的长宽比与输入图长宽比差异过大可能导致图片内容被裁剪。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class SketchToImageRequest(AbstractModel):
    r"""SketchToImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>用于线稿生图的文本描述。<br>最多支持200个 utf-8 字符。<br>建议格式：线稿中的主体对象+画面场景+配色/材质/元素/风格等</p>
        :type Prompt: str
        :param _InputImage: <p>线稿图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以Url 为准。<br>图片限制：黑白线稿图片，单边分辨率小于5000px且大于128px（分辨率过小会导致效果受损），转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputImage: str
        :param _InputUrl: <p>线稿图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以Url 为准。<br>图片限制：黑白线稿图片，单边分辨率小于5000px且大于128px（分辨率过小会导致效果受损），转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputUrl: str
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _RspImgType: <p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。生成图分辨率较大时建议选择 url，使用 base64 可能因图片过大导致返回失败。</p>
        :type RspImgType: str
        """
        self._Prompt = None
        self._InputImage = None
        self._InputUrl = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def Prompt(self):
        r"""<p>用于线稿生图的文本描述。<br>最多支持200个 utf-8 字符。<br>建议格式：线稿中的主体对象+画面场景+配色/材质/元素/风格等</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def InputImage(self):
        r"""<p>线稿图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以Url 为准。<br>图片限制：黑白线稿图片，单边分辨率小于5000px且大于128px（分辨率过小会导致效果受损），转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        r"""<p>线稿图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以Url 为准。<br>图片限制：黑白线稿图片，单边分辨率小于5000px且大于128px（分辨率过小会导致效果受损），转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。生成图分辨率较大时建议选择 url，使用 base64 可能因图片过大导致返回失败。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._InputImage = params.get("InputImage")
        self._InputUrl = params.get("InputUrl")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SketchToImageResponse(AbstractModel):
    r"""SketchToImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class SubmitDrawPortraitJobRequest(AbstractModel):
    r"""SubmitDrawPortraitJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: <p>写真模型 ID。</p>
        :type ModelId: str
        :param _StyleId: <p>写真风格模板。<br>请在<a href="https://cloud.tencent.com/document/product/1668/105740"> AI 写真风格列表</a> 中选择期望的风格，传入风格编号。</p>
        :type StyleId: str
        :param _ImageNum: <p>本次生成的图片数量，取值范围[1,4]</p>
        :type ImageNum: int
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br> 0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _Definition: <p>清晰度，单位为 px。<br>支持以下选项：<br>sd：基础版，分辨率512:640<br>hd：高清畅享版，分辨率1024:1280<br>hdpro：高清优享版，分辨率1024:1280（推荐）<br>uhd：超清版，分辨率2048:2560<br>不填默认为sd。</p>
        :type Definition: str
        """
        self._ModelId = None
        self._StyleId = None
        self._ImageNum = None
        self._LogoAdd = None
        self._LogoParam = None
        self._Definition = None

    @property
    def ModelId(self):
        r"""<p>写真模型 ID。</p>
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def StyleId(self):
        r"""<p>写真风格模板。<br>请在<a href="https://cloud.tencent.com/document/product/1668/105740"> AI 写真风格列表</a> 中选择期望的风格，传入风格编号。</p>
        :rtype: str
        """
        return self._StyleId

    @StyleId.setter
    def StyleId(self, StyleId):
        self._StyleId = StyleId

    @property
    def ImageNum(self):
        r"""<p>本次生成的图片数量，取值范围[1,4]</p>
        :rtype: int
        """
        return self._ImageNum

    @ImageNum.setter
    def ImageNum(self, ImageNum):
        self._ImageNum = ImageNum

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br> 0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Definition(self):
        r"""<p>清晰度，单位为 px。<br>支持以下选项：<br>sd：基础版，分辨率512:640<br>hd：高清畅享版，分辨率1024:1280<br>hdpro：高清优享版，分辨率1024:1280（推荐）<br>uhd：超清版，分辨率2048:2560<br>不填默认为sd。</p>
        :rtype: str
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._StyleId = params.get("StyleId")
        self._ImageNum = params.get("ImageNum")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitDrawPortraitJobResponse(AbstractModel):
    r"""SubmitDrawPortraitJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>提交生成写真图片任务 ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>提交生成写真图片任务 ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitGlamPicJobRequest(AbstractModel):
    r"""SubmitGlamPicJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateUrl: <p>美照模板图 URL。<br>图片限制：模板图中最多出现5张人脸，单边分辨率大于300px，转成 Base64 字符串后小于 10MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type TemplateUrl: str
        :param _FaceInfos: <p>用户图 URL 列表，以及模板图中需要替换成用户的人脸框信息。<br>一张美照中可包含1 ~ 5个用户形象。每个用户需上传1 ~ 6张照片，仅支持单人照。<br>模板图中的人脸数量需要大于等于用户个数。如果不传每个用户在模板图中的人脸框位置，默认按照模板图人脸框从大到小的顺序进行替换。如需自定义顺序，需要依次上传每个用户在模板图中的人脸框位置。<br>图片限制：每张图片转成 Base64 字符串后小于 10MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。建议使用单人、正脸、脸部区域占比较大、脸部清晰无遮挡、无大角度偏转、无夸张表情的用户图。<br>示例值：[{&quot;ImageUrls&quot;: [&quot;https://cos.ap-guangzhou.myqcloud.com/image.jpg&quot;]}]</p>
        :type FaceInfos: list of FaceInfo
        :param _Num: <p>美照生成数量。<br>支持1 ~ 4张，默认生成4张。</p>
        :type Num: int
        :param _Style: <p>美照生成风格。<br>仅对单人美照生效，单人可支持选择不同风格。需按照美照生成数量，在数组中逐一填入每张美照的风格名称。如果不传，默认取不重复的随机风格顺序。<br>多人美照只支持 balanced 一种风格，该参数不生效。<br>可选风格：<ul><li>real：面部相似度更高。</li><li>balanced：平衡面部真实感和美观度。</li><li>textured：脸部皮肤更具真实感。</li><li>beautiful：脸部美观度更高。</li></ul></p>
        :type Style: list of str
        :param _Similarity: <p>相似度系数，越高越像用户图。<br>取值范围[0, 1]，默认为0.6。</p>
        :type Similarity: float
        :param _Clarity: <p>超分选项，默认不做超分，可选开启。<br>x2：2倍超分<br>x4：4倍超分</p>
        :type Clarity: str
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        self._TemplateUrl = None
        self._FaceInfos = None
        self._Num = None
        self._Style = None
        self._Similarity = None
        self._Clarity = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def TemplateUrl(self):
        r"""<p>美照模板图 URL。<br>图片限制：模板图中最多出现5张人脸，单边分辨率大于300px，转成 Base64 字符串后小于 10MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._TemplateUrl

    @TemplateUrl.setter
    def TemplateUrl(self, TemplateUrl):
        self._TemplateUrl = TemplateUrl

    @property
    def FaceInfos(self):
        r"""<p>用户图 URL 列表，以及模板图中需要替换成用户的人脸框信息。<br>一张美照中可包含1 ~ 5个用户形象。每个用户需上传1 ~ 6张照片，仅支持单人照。<br>模板图中的人脸数量需要大于等于用户个数。如果不传每个用户在模板图中的人脸框位置，默认按照模板图人脸框从大到小的顺序进行替换。如需自定义顺序，需要依次上传每个用户在模板图中的人脸框位置。<br>图片限制：每张图片转成 Base64 字符串后小于 10MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。建议使用单人、正脸、脸部区域占比较大、脸部清晰无遮挡、无大角度偏转、无夸张表情的用户图。<br>示例值：[{&quot;ImageUrls&quot;: [&quot;https://cos.ap-guangzhou.myqcloud.com/image.jpg&quot;]}]</p>
        :rtype: list of FaceInfo
        """
        return self._FaceInfos

    @FaceInfos.setter
    def FaceInfos(self, FaceInfos):
        self._FaceInfos = FaceInfos

    @property
    def Num(self):
        r"""<p>美照生成数量。<br>支持1 ~ 4张，默认生成4张。</p>
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Style(self):
        r"""<p>美照生成风格。<br>仅对单人美照生效，单人可支持选择不同风格。需按照美照生成数量，在数组中逐一填入每张美照的风格名称。如果不传，默认取不重复的随机风格顺序。<br>多人美照只支持 balanced 一种风格，该参数不生效。<br>可选风格：<ul><li>real：面部相似度更高。</li><li>balanced：平衡面部真实感和美观度。</li><li>textured：脸部皮肤更具真实感。</li><li>beautiful：脸部美观度更高。</li></ul></p>
        :rtype: list of str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Similarity(self):
        r"""<p>相似度系数，越高越像用户图。<br>取值范围[0, 1]，默认为0.6。</p>
        :rtype: float
        """
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def Clarity(self):
        r"""<p>超分选项，默认不做超分，可选开启。<br>x2：2倍超分<br>x4：4倍超分</p>
        :rtype: str
        """
        return self._Clarity

    @Clarity.setter
    def Clarity(self, Clarity):
        self._Clarity = Clarity

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._TemplateUrl = params.get("TemplateUrl")
        if params.get("FaceInfos") is not None:
            self._FaceInfos = []
            for item in params.get("FaceInfos"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfos.append(obj)
        self._Num = params.get("Num")
        self._Style = params.get("Style")
        self._Similarity = params.get("Similarity")
        self._Clarity = params.get("Clarity")
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
        


class SubmitGlamPicJobResponse(AbstractModel):
    r"""SubmitGlamPicJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitMemeJobRequest(AbstractModel):
    r"""SubmitMemeJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Pose: <p>表情模板。<br>请在 <a href="https://cloud.tencent.com/document/product/1668/115327">表情动图模板列表</a>  中选择期望的模板，传入 Pose 名称。</p>
        :type Pose: str
        :param _InputImage: <p>人像参考图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputImage: str
        :param _InputUrl: <p>人像参考图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :type InputUrl: str
        :param _Resolution: <p>生成分辨率，单位为 px。<br>真人类型支持256、512，默认为256，<br>卡通类型仅支持512。</p>
        :type Resolution: int
        :param _Text: <p>自定义文案。<br>仅对真人类型的 Pose 生效，将在生成的表情动图中显示指定的文字。如果传入的字符串长度大于10，只截取前10个显示。<br>如果不传，默认使用自带的文案。<br>如果 text = &quot;&quot; 空字符串，代表不在表情动图中添加文案。</p>
        :type Text: str
        :param _Haircut: <p>头发遮罩开关。<br>true：裁剪过长的头发。<br>false：不裁剪过长的头发。<br>仅对卡通类型的 Pose 生效，默认为 false。</p>
        :type Haircut: bool
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        self._Pose = None
        self._InputImage = None
        self._InputUrl = None
        self._Resolution = None
        self._Text = None
        self._Haircut = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Pose(self):
        r"""<p>表情模板。<br>请在 <a href="https://cloud.tencent.com/document/product/1668/115327">表情动图模板列表</a>  中选择期望的模板，传入 Pose 名称。</p>
        :rtype: str
        """
        return self._Pose

    @Pose.setter
    def Pose(self, Pose):
        self._Pose = Pose

    @property
    def InputImage(self):
        r"""<p>人像参考图 Base64 数据。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        r"""<p>人像参考图 Url。<br>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。<br>图片限制：单边分辨率小于5000px，转成 Base64 字符串后小于 6MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。</p>
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def Resolution(self):
        r"""<p>生成分辨率，单位为 px。<br>真人类型支持256、512，默认为256，<br>卡通类型仅支持512。</p>
        :rtype: int
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Text(self):
        r"""<p>自定义文案。<br>仅对真人类型的 Pose 生效，将在生成的表情动图中显示指定的文字。如果传入的字符串长度大于10，只截取前10个显示。<br>如果不传，默认使用自带的文案。<br>如果 text = &quot;&quot; 空字符串，代表不在表情动图中添加文案。</p>
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Haircut(self):
        r"""<p>头发遮罩开关。<br>true：裁剪过长的头发。<br>false：不裁剪过长的头发。<br>仅对卡通类型的 Pose 生效，默认为 false。</p>
        :rtype: bool
        """
        return self._Haircut

    @Haircut.setter
    def Haircut(self, Haircut):
        self._Haircut = Haircut

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。<br>示例值：{&quot;LogoUrl&quot;: &quot;https://cos.ap-guangzhou.myqcloud.com/logo.jpg&quot;, &quot;LogoRect&quot;: {&quot;X&quot;: 10, &quot;Y&quot;: 10, &quot;Width&quot;: 20, &quot;Height&quot;: 20}}</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Pose = params.get("Pose")
        self._InputImage = params.get("InputImage")
        self._InputUrl = params.get("InputUrl")
        self._Resolution = params.get("Resolution")
        self._Text = params.get("Text")
        self._Haircut = params.get("Haircut")
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
        


class SubmitMemeJobResponse(AbstractModel):
    r"""SubmitMemeJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务id</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务id</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitTextToImageJobRequest(AbstractModel):
    r"""SubmitTextToImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>文本描述。<br>算法将根据输入的文本智能生成与之相关的图像。<br>不能为空，推荐使用中文。最多可传8192个 utf-8 字符。</p>
        :type Prompt: str
        :param _Images: <p>参考图，最多三张图。  - Base64 或 Url 。</p><ul><li>单张图片限制：输入图分辨率单边最小50px，最大5000px；图片base64后大小小于6M ；格式支持 jpg、jpeg、png、bmp、tiff、webp。</li></ul>
        :type Images: list of str
        :param _Resolution: <p>生成图分辨率<br>单位为 px。<br>格式：&quot;${宽}:${高}&quot;，说明：分辨率的设置和输入是否有参考图（image_urls/images参数）有关：<br>一、文生图（无参考图）<br>默认分辨率：1024:1024；<br>尺寸约束：宽、高均在 [512, 2048] 像素范围内，宽高乘积 ≤ 1024:1024 像素。<br>二、图生图（有参考图）<br>尺寸约束：宽、高均在 [512, 2048] 像素范围内，宽高乘积 ≤ 1024:1024 像素。</p><p>传入尺寸时（输出自适应，不严格遵循传入尺寸）：<br>输入图分辨率分桶与传入尺寸分桶一致时：按输入图长宽比，缩放至接近 1024:1024 面积输出；<br>输入图分辨率分桶与传入尺寸分桶不一致时：从 尺寸列表 中选取最接近传入尺寸的尺寸输出<br>尺寸列表：2048:512、1984:512、1920:512、1856:512、1792:512、<br>1728:512、1664:512、1600:512、1536:512、1472:576、<br>1408:640、1344:704、1280:768、1216:832、1152:896、<br>1088:960、1024:1024、960:1088、896:1152、832:1216、<br>768:1280、704:1344、640:1408、576:1472、512:1536、<br>512:1600、512:1664、512:1728、512:1792、512:1856、<br>512:1920、512:1984、512:2048、768:1024、720:1280、<br>1024:768、1280:720<br>不传入尺寸时：将传入默认值1024:1024。</p>
        :type Resolution: str
        :param _Seed: <p>随机种子，默认随机。<br>不传：随机种子生成。<br>正数：固定种子生成。<br>扩写开启时固定种子不生效，将保持随机。<br>取值范围：1 - 4294967295</p>
        :type Seed: int
        :param _LogoAdd: <p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _Revise: <p>是否开启prompt改写，为空时默认开启，改写预计会增加20s左右耗时。<br>0：关闭改写<br>1：开启改写<br>建议默认开启，如果关闭改写，需要调用方自己接改写，否则对生图效果有较大影响，改写方法可以参考：<a href="https://github.com/Tencent-Hunyuan/HunyuanImage-3.0/tree/main/PE">改写</a><br>示例值：1</p>
        :type Revise: int
        """
        self._Prompt = None
        self._Images = None
        self._Resolution = None
        self._Seed = None
        self._LogoAdd = None
        self._LogoParam = None
        self._Revise = None

    @property
    def Prompt(self):
        r"""<p>文本描述。<br>算法将根据输入的文本智能生成与之相关的图像。<br>不能为空，推荐使用中文。最多可传8192个 utf-8 字符。</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Images(self):
        r"""<p>参考图，最多三张图。  - Base64 或 Url 。</p><ul><li>单张图片限制：输入图分辨率单边最小50px，最大5000px；图片base64后大小小于6M ；格式支持 jpg、jpeg、png、bmp、tiff、webp。</li></ul>
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Resolution(self):
        r"""<p>生成图分辨率<br>单位为 px。<br>格式：&quot;${宽}:${高}&quot;，说明：分辨率的设置和输入是否有参考图（image_urls/images参数）有关：<br>一、文生图（无参考图）<br>默认分辨率：1024:1024；<br>尺寸约束：宽、高均在 [512, 2048] 像素范围内，宽高乘积 ≤ 1024:1024 像素。<br>二、图生图（有参考图）<br>尺寸约束：宽、高均在 [512, 2048] 像素范围内，宽高乘积 ≤ 1024:1024 像素。</p><p>传入尺寸时（输出自适应，不严格遵循传入尺寸）：<br>输入图分辨率分桶与传入尺寸分桶一致时：按输入图长宽比，缩放至接近 1024:1024 面积输出；<br>输入图分辨率分桶与传入尺寸分桶不一致时：从 尺寸列表 中选取最接近传入尺寸的尺寸输出<br>尺寸列表：2048:512、1984:512、1920:512、1856:512、1792:512、<br>1728:512、1664:512、1600:512、1536:512、1472:576、<br>1408:640、1344:704、1280:768、1216:832、1152:896、<br>1088:960、1024:1024、960:1088、896:1152、832:1216、<br>768:1280、704:1344、640:1408、576:1472、512:1536、<br>512:1600、512:1664、512:1728、512:1792、512:1856、<br>512:1920、512:1984、512:2048、768:1024、720:1280、<br>1024:768、1280:720<br>不传入尺寸时：将传入默认值1024:1024。</p>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Seed(self):
        r"""<p>随机种子，默认随机。<br>不传：随机种子生成。<br>正数：固定种子生成。<br>扩写开启时固定种子不生效，将保持随机。<br>取值范围：1 - 4294967295</p>
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Revise(self):
        r"""<p>是否开启prompt改写，为空时默认开启，改写预计会增加20s左右耗时。<br>0：关闭改写<br>1：开启改写<br>建议默认开启，如果关闭改写，需要调用方自己接改写，否则对生图效果有较大影响，改写方法可以参考：<a href="https://github.com/Tencent-Hunyuan/HunyuanImage-3.0/tree/main/PE">改写</a><br>示例值：1</p>
        :rtype: int
        """
        return self._Revise

    @Revise.setter
    def Revise(self, Revise):
        self._Revise = Revise


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Images = params.get("Images")
        self._Resolution = params.get("Resolution")
        self._Seed = params.get("Seed")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._Revise = params.get("Revise")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTextToImageJobResponse(AbstractModel):
    r"""SubmitTextToImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务 ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务 ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitTextToImageProJobRequest(AbstractModel):
    r"""SubmitTextToImageProJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本描述。 
算法将根据输入的文本智能生成与之相关的图像。 
不能为空，推荐使用中文。最多可传100个 utf-8 字符。
        :type Prompt: str
        :param _Style: 绘画风格。
请在 [文生图（高级版）风格列表](https://cloud.tencent.com/document/product/1668/104567) 中选择期望的风格，传入风格编号。
不传默认不指定风格。
        :type Style: str
        :param _Resolution: 生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3），不传默认使用1024:1024。
        :type Resolution: str
        :param _LogoAdd: 为生成结果图添加显式水印标识的开关，默认为1。  
1：添加。  
0：不添加。  
其他数值：默认按1处理。  
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _Engine: 文生图模型，默认使用engine1。
取值：
engine1
engine2
        :type Engine: str
        :param _Revise: prompt 扩写开关。1为开启，0为关闭，不传默认开启。
开启扩写后，将自动扩写原始输入的 prompt 并使用扩写后的 prompt 生成图片，返回生成图片结果时将一并返回扩写后的 prompt 文本。
如果关闭扩写，将直接使用原始输入的 prompt 生成图片。
建议开启，在多数场景下可提升生成图片效果、丰富生成图片细节。
        :type Revise: int
        """
        self._Prompt = None
        self._Style = None
        self._Resolution = None
        self._LogoAdd = None
        self._Engine = None
        self._Revise = None

    @property
    def Prompt(self):
        r"""文本描述。 
算法将根据输入的文本智能生成与之相关的图像。 
不能为空，推荐使用中文。最多可传100个 utf-8 字符。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Style(self):
        r"""绘画风格。
请在 [文生图（高级版）风格列表](https://cloud.tencent.com/document/product/1668/104567) 中选择期望的风格，传入风格编号。
不传默认不指定风格。
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Resolution(self):
        r"""生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3），不传默认使用1024:1024。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        r"""为生成结果图添加显式水印标识的开关，默认为1。  
1：添加。  
0：不添加。  
其他数值：默认按1处理。  
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def Engine(self):
        r"""文生图模型，默认使用engine1。
取值：
engine1
engine2
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Revise(self):
        r"""prompt 扩写开关。1为开启，0为关闭，不传默认开启。
开启扩写后，将自动扩写原始输入的 prompt 并使用扩写后的 prompt 生成图片，返回生成图片结果时将一并返回扩写后的 prompt 文本。
如果关闭扩写，将直接使用原始输入的 prompt 生成图片。
建议开启，在多数场景下可提升生成图片效果、丰富生成图片细节。
        :rtype: int
        """
        return self._Revise

    @Revise.setter
    def Revise(self, Revise):
        self._Revise = Revise


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Style = params.get("Style")
        self._Resolution = params.get("Resolution")
        self._LogoAdd = params.get("LogoAdd")
        self._Engine = params.get("Engine")
        self._Revise = params.get("Revise")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTextToImageProJobResponse(AbstractModel):
    r"""SubmitTextToImageProJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitTrainPortraitModelJobRequest(AbstractModel):
    r"""SubmitTrainPortraitModelJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 在上传写真训练图片时指定的写真模型 ID。 
每个 AI 写真模型自训练完成起1年内有效，有效期内可使用模型生成图片，期满后需要重新训练模型。

        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        r"""在上传写真训练图片时指定的写真模型 ID。 
每个 AI 写真模型自训练完成起1年内有效，有效期内可使用模型生成图片，期满后需要重新训练模型。

        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTrainPortraitModelJobResponse(AbstractModel):
    r"""SubmitTrainPortraitModelJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class TextToImageLiteRequest(AbstractModel):
    r"""TextToImageLite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>文本描述。将根据输入的文本智能生成与之相关的图像。<br>不能为空，推荐使用中文。最多可传1024个 utf-8 字符。</p>
        :type Prompt: str
        :param _NegativePrompt: <p>反向提示词。 减少生成结果中出现描述内容。<br>推荐使用中文。最多可传1024个 utf-8 字符。</p>
        :type NegativePrompt: str
        :param _Resolution: <p>生成图分辨率，默认1024:1024。<br>支持的图像宽高比例: 1:1，3:4，4:3，9:16，16:9。<br>支持的长边分辨率: 160，200，225，258，512，520，608，768，1024，1080，1280，1600，1620，1920，2048，2400，2560，2592，3440，3840，4096。<br>单位为px。</p>
        :type Resolution: str
        :param _Seed: <p>随机种子，默认随机。<br>0：随机种子生成。<br>不传：随机种子生成。<br>正数：固定种子生成。</p>
        :type Seed: int
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _RspImgType: <p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :type RspImgType: str
        """
        self._Prompt = None
        self._NegativePrompt = None
        self._Resolution = None
        self._Seed = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def Prompt(self):
        r"""<p>文本描述。将根据输入的文本智能生成与之相关的图像。<br>不能为空，推荐使用中文。最多可传1024个 utf-8 字符。</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        r"""<p>反向提示词。 减少生成结果中出现描述内容。<br>推荐使用中文。最多可传1024个 utf-8 字符。</p>
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Resolution(self):
        r"""<p>生成图分辨率，默认1024:1024。<br>支持的图像宽高比例: 1:1，3:4，4:3，9:16，16:9。<br>支持的长边分辨率: 160，200，225，258，512，520，608，768，1024，1080，1280，1600，1620，1920，2048，2400，2560，2592，3440，3840，4096。<br>单位为px。</p>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Seed(self):
        r"""<p>随机种子，默认随机。<br>0：随机种子生成。<br>不传：随机种子生成。<br>正数：固定种子生成。</p>
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Resolution = params.get("Resolution")
        self._Seed = params.get("Seed")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageLiteResponse(AbstractModel):
    r"""TextToImageLite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _Seed: <p>Seed</p>
        :type Seed: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._Seed = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def Seed(self):
        r"""<p>Seed</p>
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

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
        self._ResultImage = params.get("ResultImage")
        self._Seed = params.get("Seed")
        self._RequestId = params.get("RequestId")


class TextToImageRapidRequest(AbstractModel):
    r"""TextToImageRapid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>文本描述。<br>算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。<br>不能为空，推荐使用中文。最多可传256个 utf-8 字符。</p>
        :type Prompt: str
        :param _Resolution: <p>生成图分辨率，默认1024:1024。<br>支持的图像宽高比例: 1:1，3:4，4:3，9:16，16:9。<br>支持的长边分辨率: 160，200，225，258，512，520，608，768，1024，1080，1280，1600，1620，1920，2048，2400，2560，2592，3440，3840，4096。<br>单位为 px。</p>
        :type Resolution: str
        :param _Seed: <p>随机种子，默认随机。<br>0：随机种子生成。<br>不传：随机种子生成。<br>正数：固定种子生成。</p>
        :type Seed: int
        :param _Image: <p>参考图。</p><ul><li>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。</li><li>当传入Image参数时，Style和Resolution参数不生效，输出图分辨率将保持Image传入图分辨率。</li><li>图片限制：单边分辨率大于128px且小于2048px；图片小于6M；格式支持 jpg、jpeg、png、bmp、tiff、webp。</li></ul>
        :type Image: :class:`tencentcloud.aiart.v20221229.models.Image`
        :param _Style: <p>生成的图片风格，参考值：</p><p>1：宫崎骏风格；<br>2：新海诚风格；<br>3：去旅行风格；<br>4：水彩风格；<br>5：像素风格；<br>6：童话世界风格；<br>7：奇趣卡通风格；<br>8：赛博朋克风格；<br>9：极简风格；<br>10：复古风格；<br>11：暗黑系风格；<br>12：波普风风格；<br>13：糖果色风格；<br>14：胶片电影风格；<br>15：素描风格；<br>16：水墨画风格；<br>17：油画风格；<br>18：粉笔风格；<br>19：粘土风格；<br>20：毛毡风格；<br>21：刺绣风格；<br>22：彩铅风格；<br>23：莫奈风格；<br>24：毕加索风格；<br>25：穆夏风格；<br>26：古风二次元风格；<br>27：都市二次元风格；<br>28：悬疑风格；<br>29：校园风格；<br>30：都市异能风格。</p>
        :type Style: str
        :param _LogoAdd: <p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _RspImgType: <p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :type RspImgType: str
        """
        self._Prompt = None
        self._Resolution = None
        self._Seed = None
        self._Image = None
        self._Style = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def Prompt(self):
        r"""<p>文本描述。<br>算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。<br>不能为空，推荐使用中文。最多可传256个 utf-8 字符。</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Resolution(self):
        r"""<p>生成图分辨率，默认1024:1024。<br>支持的图像宽高比例: 1:1，3:4，4:3，9:16，16:9。<br>支持的长边分辨率: 160，200，225，258，512，520，608，768，1024，1080，1280，1600，1620，1920，2048，2400，2560，2592，3440，3840，4096。<br>单位为 px。</p>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Seed(self):
        r"""<p>随机种子，默认随机。<br>0：随机种子生成。<br>不传：随机种子生成。<br>正数：固定种子生成。</p>
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def Image(self):
        r"""<p>参考图。</p><ul><li>Base64 和 Url 必须提供一个，如果都提供以 Url 为准。</li><li>当传入Image参数时，Style和Resolution参数不生效，输出图分辨率将保持Image传入图分辨率。</li><li>图片限制：单边分辨率大于128px且小于2048px；图片小于6M；格式支持 jpg、jpeg、png、bmp、tiff、webp。</li></ul>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Style(self):
        r"""<p>生成的图片风格，参考值：</p><p>1：宫崎骏风格；<br>2：新海诚风格；<br>3：去旅行风格；<br>4：水彩风格；<br>5：像素风格；<br>6：童话世界风格；<br>7：奇趣卡通风格；<br>8：赛博朋克风格；<br>9：极简风格；<br>10：复古风格；<br>11：暗黑系风格；<br>12：波普风风格；<br>13：糖果色风格；<br>14：胶片电影风格；<br>15：素描风格；<br>16：水墨画风格；<br>17：油画风格；<br>18：粉笔风格；<br>19：粘土风格；<br>20：毛毡风格；<br>21：刺绣风格；<br>22：彩铅风格；<br>23：莫奈风格；<br>24：毕加索风格；<br>25：穆夏风格；<br>26：古风二次元风格；<br>27：都市二次元风格；<br>28：悬疑风格；<br>29：校园风格；<br>30：都市异能风格。</p>
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        r"""<p>返回图像方式（base64 或 url），二选一，默认为 base64。url 有效期为1小时。</p>
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Resolution = params.get("Resolution")
        self._Seed = params.get("Seed")
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        self._Style = params.get("Style")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageRapidResponse(AbstractModel):
    r"""TextToImageRapid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: <p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :type ResultImage: str
        :param _Seed: <p>Seed</p>
        :type Seed: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._Seed = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""<p>根据入参 RspImgType 填入不同，返回不同的内容。<br>如果传入 base64 则返回生成图 Base64 编码。<br>如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。</p>
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def Seed(self):
        r"""<p>Seed</p>
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

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
        self._ResultImage = params.get("ResultImage")
        self._Seed = params.get("Seed")
        self._RequestId = params.get("RequestId")


class UploadTrainPortraitImagesRequest(AbstractModel):
    r"""UploadTrainPortraitImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: <p>写真模型 ID。由英文大小写字母、数字及下划线组成。<br>用于唯一标识一个写真模型，一个写真模型只能用于一个人物的写真图片生成。</p>
        :type ModelId: str
        :param _BaseUrl: <p>写真模型训练用的基础图像 URL，用于固定写真模型可生成的人物。<br>图片数量：1张。<br>图片内容：单人，脸部清晰。<br>图片限制：单边分辨率小于2000px，转成 Base64 字符串后小于 5MB。</p>
        :type BaseUrl: str
        :param _Urls: <p>写真模型训练用的图像 URL 列表，仅常规训练模式需要上传。<br>图片数量：19 - 24 张。<br>图片内容：单人，脸部清晰，和基础图像中的人物为同一人。<br>图片限制：单边分辨率小于2000px，转成 Base64 字符串后小于 5MB。</p>
        :type Urls: list of str
        :param _Filter: <p>训练图像质量过滤开关配置。<br>支持开启或关闭对训练图像分辨率下限、脸部区域大小、脸部遮挡的过滤，默认开启以上过滤。<br>如果训练图像内包含多人脸或无人脸、和 Base 人像不为同一人也将被过滤，不可关闭该过滤条件。<br>建议：关闭以上过滤可能导致写真生成效果受损，建议使用单人、正脸、脸部区域占比较大、脸部清晰无遮挡、无大角度偏转、无夸张表情的图像进行训练。<br>示例值：{&quot;Resolution&quot;:1,&quot;Size&quot;:1,&quot;Occlusion&quot;:1}</p>
        :type Filter: :class:`tencentcloud.aiart.v20221229.models.Filter`
        :param _TrainMode: <p>训练模式。<br>默认使用常规训练模式。如果使用快速训练模式和免训练模式，只需要在 BaseUrl 中传入1张图片，Urls.N 中无需传入图片。<br>0：常规训练模式，上传多张图片用于模型训练，完成训练后可生成写真图片。<br>1：快速训练模式，仅需上传1张图片用于模型训练，训练速度更快，完成训练后可生成写真图片。<br>2：免训练模式，仅需上传1张图片，跳过模型训练环节，直接生成写真图片。</p>
        :type TrainMode: int
        """
        self._ModelId = None
        self._BaseUrl = None
        self._Urls = None
        self._Filter = None
        self._TrainMode = None

    @property
    def ModelId(self):
        r"""<p>写真模型 ID。由英文大小写字母、数字及下划线组成。<br>用于唯一标识一个写真模型，一个写真模型只能用于一个人物的写真图片生成。</p>
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def BaseUrl(self):
        r"""<p>写真模型训练用的基础图像 URL，用于固定写真模型可生成的人物。<br>图片数量：1张。<br>图片内容：单人，脸部清晰。<br>图片限制：单边分辨率小于2000px，转成 Base64 字符串后小于 5MB。</p>
        :rtype: str
        """
        return self._BaseUrl

    @BaseUrl.setter
    def BaseUrl(self, BaseUrl):
        self._BaseUrl = BaseUrl

    @property
    def Urls(self):
        r"""<p>写真模型训练用的图像 URL 列表，仅常规训练模式需要上传。<br>图片数量：19 - 24 张。<br>图片内容：单人，脸部清晰，和基础图像中的人物为同一人。<br>图片限制：单边分辨率小于2000px，转成 Base64 字符串后小于 5MB。</p>
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def Filter(self):
        r"""<p>训练图像质量过滤开关配置。<br>支持开启或关闭对训练图像分辨率下限、脸部区域大小、脸部遮挡的过滤，默认开启以上过滤。<br>如果训练图像内包含多人脸或无人脸、和 Base 人像不为同一人也将被过滤，不可关闭该过滤条件。<br>建议：关闭以上过滤可能导致写真生成效果受损，建议使用单人、正脸、脸部区域占比较大、脸部清晰无遮挡、无大角度偏转、无夸张表情的图像进行训练。<br>示例值：{&quot;Resolution&quot;:1,&quot;Size&quot;:1,&quot;Occlusion&quot;:1}</p>
        :rtype: :class:`tencentcloud.aiart.v20221229.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def TrainMode(self):
        r"""<p>训练模式。<br>默认使用常规训练模式。如果使用快速训练模式和免训练模式，只需要在 BaseUrl 中传入1张图片，Urls.N 中无需传入图片。<br>0：常规训练模式，上传多张图片用于模型训练，完成训练后可生成写真图片。<br>1：快速训练模式，仅需上传1张图片用于模型训练，训练速度更快，完成训练后可生成写真图片。<br>2：免训练模式，仅需上传1张图片，跳过模型训练环节，直接生成写真图片。</p>
        :rtype: int
        """
        return self._TrainMode

    @TrainMode.setter
    def TrainMode(self, TrainMode):
        self._TrainMode = TrainMode


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._BaseUrl = params.get("BaseUrl")
        self._Urls = params.get("Urls")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._TrainMode = params.get("TrainMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadTrainPortraitImagesResponse(AbstractModel):
    r"""UploadTrainPortraitImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultDetails: <p>用于提示对应上传的Urls训练图片是否符合要求，如果未通过需要重新上传。如果基础图像不符合要求会直接通过ErrorCode提示。如果您选择了快速模式，该参数返回为空数组。</p>
        :type ResultDetails: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultDetails = None
        self._RequestId = None

    @property
    def ResultDetails(self):
        r"""<p>用于提示对应上传的Urls训练图片是否符合要求，如果未通过需要重新上传。如果基础图像不符合要求会直接通过ErrorCode提示。如果您选择了快速模式，该参数返回为空数组。</p>
        :rtype: list of str
        """
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

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
        self._ResultDetails = params.get("ResultDetails")
        self._RequestId = params.get("RequestId")