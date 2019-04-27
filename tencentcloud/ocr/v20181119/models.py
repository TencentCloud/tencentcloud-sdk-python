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


class Coord(AbstractModel):
    """Coord

    """

    def __init__(self):
        """
        :param X: 横坐标
        :type X: int
        :param Y: 纵坐标
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


class GeneralBasicOCRRequest(AbstractModel):
    """GeneralBasicOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的BASE64值。
支持的图片格式：PNG、JPG、JPEG，暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过3M。图片下载时间不超过3秒。
图片的 ImageUrl、ImageBase64必须提供一个，如果都提供，只使用ImageBase64。
        :type ImageBase64: str
        :param ImageUrl: 图片的URL地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过3M。图片下载时间不超过3秒。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Scene: 保留字段。
        :type Scene: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")


class GeneralBasicOCRResponse(AbstractModel):
    """GeneralBasicOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接
        :type TextDetections: list of TextDetection
        :param Language: 检测到的语言，目前支持的语种范围为：简体中文、繁体中文、英文、日文、韩文。未来将陆续新增对更多语种的支持。
返回结果含义为：zh-中英混合，jap-日文，kor-韩文。
        :type Language: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.RequestId = params.get("RequestId")


class GeneralFastOCRRequest(AbstractModel):
    """GeneralFastOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的BASE64值。
支持的图片格式：PNG、JPG、JPEG，暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过3M。图片下载时间不超过3秒。
图片的 ImageUrl、ImageBase64必须提供一个，如果都提供，只使用ImageBase64。
        :type ImageBase64: str
        :param ImageUrl: 图片的URL地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过3M。图片下载时间不超过3秒。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class GeneralFastOCRResponse(AbstractModel):
    """GeneralFastOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接
        :type TextDetections: list of TextDetection
        :param Language: 检测到的语言，目前支持的语种范围为：简体中文、繁体中文、英文、日文、韩文。未来将陆续新增对更多语种的支持。
返回结果含义为：zh-中英混合，jap-日文，kor-韩文。
        :type Language: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的BASE64值。
支持的图片格式：PNG、JPG、JPEG，暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过6M。图片下载时间不超过3秒。
图片的 ImageUrl、ImageBase64必须提供一个，如果都提供，只使用ImageBase64。
        :type ImageBase64: str
        :param ImageUrl: 图片URL地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过3M。图片下载时间不超过3秒。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param CardSide: FRONT为身份证有照片的一面（正面）
BACK为身份证有国徽的一面（反面）
        :type CardSide: str
        :param Config: 可选字段，根据需要选择是否请求对应字段。
目前包含的字段为：
CropIdCard-身份证照片裁剪，bool类型，
CropPortrait-人像照片裁剪，bool类型，
CopyWarn-复印件告警，bool类型，
ReshootWarn-翻拍告警，bool类型。

SDK设置方式参考：
Config = Json.stringify({"CropIdCard":true,"CropPortrait":true})
API 3.0 Explorer设置方式参考：
Config = {"CropIdCard":true,"CropPortrait":true}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")
        self.Config = params.get("Config")


class IDCardOCRResponse(AbstractModel):
    """IDCardOCR返回参数结构体

    """

    def __init__(self):
        """
        :param Name: 姓名（正面）
        :type Name: str
        :param Sex: 性别（正面）
        :type Sex: str
        :param Nation: 民族（正面）
        :type Nation: str
        :param Birth: 出生日期（正面）
        :type Birth: str
        :param Address: 地址（正面）
        :type Address: str
        :param IdNum: 身份证号（正面）
        :type IdNum: str
        :param Authority: 发证机关（反面）
        :type Authority: str
        :param ValidDate: 证件有效期（反面）
        :type ValidDate: str
        :param AdvancedInfo: 扩展信息，根据请求的可选字段返回对应内容，不请求则不返回，具体输入参考示例3。目前支持的扩展字段为：
IdCard身份证照片，请求CropIdCard时返回；
Portrait人像照片，请求CropPortrait时返回；
WarnInfos告警信息（Code告警码，Msg告警信息），识别出翻拍件或复印件时返回。
        :type AdvancedInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.IdNum = None
        self.Authority = None
        self.ValidDate = None
        self.AdvancedInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdNum = params.get("IdNum")
        self.Authority = params.get("Authority")
        self.ValidDate = params.get("ValidDate")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.RequestId = params.get("RequestId")


class TextDetection(AbstractModel):
    """TextDetection

    """

    def __init__(self):
        """
        :param DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四个顶点坐标表示
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 此字段为扩展字段。
GeneralBasicOcr接口返回段落信息Parag，包含ParagNo。
        :type AdvancedInfo: str
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")