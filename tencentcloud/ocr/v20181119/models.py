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


class ArithmeticOCRRequest(AbstractModel):
    """ArithmeticOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class ArithmeticOCRResponse(AbstractModel):
    """ArithmeticOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextArithmetic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextArithmetic()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class BankCardOCRRequest(AbstractModel):
    """BankCardOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class BankCardOCRResponse(AbstractModel):
    """BankCardOCR返回参数结构体

    """

    def __init__(self):
        """
        :param CardNo: 卡号
        :type CardNo: str
        :param BankInfo: 银行信息
        :type BankInfo: str
        :param ValidDate: 有效期
        :type ValidDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CardNo = None
        self.BankInfo = None
        self.ValidDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CardNo = params.get("CardNo")
        self.BankInfo = params.get("BankInfo")
        self.ValidDate = params.get("ValidDate")
        self.RequestId = params.get("RequestId")


class BizLicenseOCRRequest(AbstractModel):
    """BizLicenseOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class BizLicenseOCRResponse(AbstractModel):
    """BizLicenseOCR返回参数结构体

    """

    def __init__(self):
        """
        :param RegNum: 注册号
        :type RegNum: str
        :param Name: 公司名称
        :type Name: str
        :param Capital: 注册资本
        :type Capital: str
        :param Person: 法定代表人
        :type Person: str
        :param Address: 地址
        :type Address: str
        :param Business: 经营范围
        :type Business: str
        :param Type: 主体类型
        :type Type: str
        :param Period: 营业期限
        :type Period: str
        :param ComposingForm: 组成形式
        :type ComposingForm: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegNum = None
        self.Name = None
        self.Capital = None
        self.Person = None
        self.Address = None
        self.Business = None
        self.Type = None
        self.Period = None
        self.ComposingForm = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegNum = params.get("RegNum")
        self.Name = params.get("Name")
        self.Capital = params.get("Capital")
        self.Person = params.get("Person")
        self.Address = params.get("Address")
        self.Business = params.get("Business")
        self.Type = params.get("Type")
        self.Period = params.get("Period")
        self.ComposingForm = params.get("ComposingForm")
        self.RequestId = params.get("RequestId")


class BusinessCardInfo(AbstractModel):
    """名片识别结果

    """

    def __init__(self):
        """
        :param Name: 识别出的字段名称（关键字，可能重复，比如多个手机），能识别的字段名为：
姓名、英文姓名、英文地址、公司、英文公司、职位、英文职位、部门、英文部门、手机、电话、传真、社交帐号、QQ、MSN、微信、微博、邮箱、邮编、网址、公司账号、其他。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class BusinessCardOCRRequest(AbstractModel):
    """BusinessCardOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Config: 可选字段，根据需要选择是否请求对应字段。
目前支持的字段为：
RetImageType-“PROPROCESS” 图像预处理，string 类型。
图像预处理功能为，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。

SDK 设置方式参考：
Config = Json.stringify({"RetImageType":"PROPROCESS"})
API 3.0 Explorer 设置方式参考：
Config = {"RetImageType":"PROPROCESS"}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")


class BusinessCardOCRResponse(AbstractModel):
    """BusinessCardOCR返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessCardInfos: 名片识别内容。
        :type BusinessCardInfos: list of BusinessCardInfo
        :param RetImageBase64: 返回图像预处理后的图片，图像预处理未开启时返回内容为空。
        :type RetImageBase64: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCardInfos = None
        self.RetImageBase64 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BusinessCardInfos") is not None:
            self.BusinessCardInfos = []
            for item in params.get("BusinessCardInfos"):
                obj = BusinessCardInfo()
                obj._deserialize(item)
                self.BusinessCardInfos.append(obj)
        self.RetImageBase64 = params.get("RetImageBase64")
        self.RequestId = params.get("RequestId")


class Coord(AbstractModel):
    """坐标

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


class DriverLicenseOCRRequest(AbstractModel):
    """DriverLicenseOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class DriverLicenseOCRResponse(AbstractModel):
    """DriverLicenseOCR返回参数结构体

    """

    def __init__(self):
        """
        :param Name: 姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param Nationality: 国籍
        :type Nationality: str
        :param Address: 住址
        :type Address: str
        :param DateOfBirth: 出生日期
        :type DateOfBirth: str
        :param DateOfFirstIssue: 初次领证日期
        :type DateOfFirstIssue: str
        :param Class: 准驾车型
        :type Class: str
        :param StartDate: 有效期开始时间
        :type StartDate: str
        :param EndDate: 有效期截止时间
        :type EndDate: str
        :param CardCode: 证号
        :type CardCode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Nationality = None
        self.Address = None
        self.DateOfBirth = None
        self.DateOfFirstIssue = None
        self.Class = None
        self.StartDate = None
        self.EndDate = None
        self.CardCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Nationality = params.get("Nationality")
        self.Address = params.get("Address")
        self.DateOfBirth = params.get("DateOfBirth")
        self.DateOfFirstIssue = params.get("DateOfFirstIssue")
        self.Class = params.get("Class")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.CardCode = params.get("CardCode")
        self.RequestId = params.get("RequestId")


class EnglishOCRRequest(AbstractModel):
    """EnglishOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class EnglishOCRResponse(AbstractModel):
    """EnglishOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetectionEn
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetectionEn()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class GeneralAccurateOCRRequest(AbstractModel):
    """GeneralAccurateOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class GeneralAccurateOCRResponse(AbstractModel):
    """GeneralAccurateOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class GeneralBasicOCRRequest(AbstractModel):
    """GeneralBasicOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Scene: 保留字段。
        :type Scene: str
        :param LanguageType: 识别语言类型。
支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)。
可选值：
zh\auto\jap\kor\
spa\fre\ger\por\
vie\may\rus\ita\
hol\swe\fin\dan\
nor\hun\tha
可选值分别表示：
中英文混合、自动识别、日语、韩语、
西班牙语、法语、德语、葡萄牙语、
越南语、马来语、俄语、意大利语、
荷兰语、瑞典语、芬兰语、丹麦语、
挪威语、匈牙利语、泰语。
        :type LanguageType: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None
        self.LanguageType = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")
        self.LanguageType = params.get("LanguageType")


class GeneralBasicOCRResponse(AbstractModel):
    """GeneralBasicOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param Language: 检测到的语言类型，目前支持的语言类型参考入参LanguageType说明。
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
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
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
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param Language: 检测到的语言，目前支持的语种范围为：简体中文、繁体中文、英文、日文、韩文。未来将陆续新增对更多语种的支持。
返回结果含义为：zh - 中英混合，jap - 日文，kor - 韩文。
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


class GeneralHandwritingOCRRequest(AbstractModel):
    """GeneralHandwritingOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class GeneralHandwritingOCRResponse(AbstractModel):
    """GeneralHandwritingOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextGeneralHandwriting
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextGeneralHandwriting()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param CardSide: FRONT 为身份证有照片的一面（人像面），
BACK 为身份证有国徽的一面（国徽面）。
        :type CardSide: str
        :param Config: 可选字段，根据需要选择是否请求对应字段。
目前包含的字段为：
CropIdCard，身份证照片裁剪，bool 类型，
CropPortrait，人像照片裁剪，bool 类型，
CopyWarn，复印件告警，bool 类型，
BorderCheckWarn，遮挡告警，bool 类型，
ReshootWarn，翻拍告警，bool 类型。

SDK 设置方式参考：
Config = Json.stringify({"CropIdCard":true,"CropPortrait":true})
API 3.0 Explorer 设置方式参考：
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
        :param Name: 姓名（人像面）
        :type Name: str
        :param Sex: 性别（人像面）
        :type Sex: str
        :param Nation: 民族（人像面）
        :type Nation: str
        :param Birth: 出生日期（人像面）
        :type Birth: str
        :param Address: 地址（人像面）
        :type Address: str
        :param IdNum: 身份证号（人像面）
        :type IdNum: str
        :param Authority: 发证机关（国徽面）
        :type Authority: str
        :param ValidDate: 证件有效期（国徽面）
        :type ValidDate: str
        :param AdvancedInfo: 扩展信息，根据请求的可选字段返回对应内容，不请求则不返回，具体输入参考示例3。目前支持的扩展字段为：
IdCard，身份证照片，请求 CropIdCard 时返回；
Portrait，人像照片，请求 CropPortrait 时返回；
WarnInfos，告警信息（Code - 告警码，Msg - 告警信息内容），识别出翻拍件或复印件时返回。

Code 告警码列表和释义：
-9103	身份证翻拍告警，
-9102	身份证复印件告警，
-9105	身份证框内遮挡告警。
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


class LicensePlateOCRRequest(AbstractModel):
    """LicensePlateOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class LicensePlateOCRResponse(AbstractModel):
    """LicensePlateOCR返回参数结构体

    """

    def __init__(self):
        """
        :param Number: 识别出的车牌号码。
        :type Number: str
        :param Confidence: 置信度，0 - 100 之间。
        :type Confidence: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Number = None
        self.Confidence = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Confidence = params.get("Confidence")
        self.RequestId = params.get("RequestId")


class TableOCRRequest(AbstractModel):
    """TableOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class TableOCRResponse(AbstractModel):
    """TableOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextTable
        :param Data: Base64 编码后的 Excel 数据。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextTable()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TextArithmetic(AbstractModel):
    """算式识别结果

    """

    def __init__(self):
        """
        :param DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param Result: 结果
        :type Result: bool
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四个顶点坐标表示
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 此字段为扩展字段。
        :type AdvancedInfo: str
        """
        self.DetectedText = None
        self.Result = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")


class TextDetection(AbstractModel):
    """文字识别结果

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


class TextDetectionEn(AbstractModel):
    """英文识别结果

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
        :param AdvancedInfo: 此字段为扩展字段。目前EnglishOCR接口返回内容为空。
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


class TextGeneralHandwriting(AbstractModel):
    """文字识别结果

    """

    def __init__(self):
        """
        :param DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 - 100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        :param AdvancedInfo: 此字段为扩展字段
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


class TextTable(AbstractModel):
    """表格识别结果

    """

    def __init__(self):
        """
        :param ColTl: 单元格左上角的列索引
        :type ColTl: int
        :param RowTl: 单元格左上角的行索引
        :type RowTl: int
        :param ColBr: 单元格右下角的列索引
        :type ColBr: int
        :param RowBr: 单元格右下角的行索引
        :type RowBr: int
        :param Text: 单元格文字
        :type Text: str
        :param Type: 单元格类型，包含body（表格主体）、header（表头）、footer（表尾）三种
        :type Type: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        :param AdvancedInfo: 此字段为扩展字段
        :type AdvancedInfo: str
        """
        self.ColTl = None
        self.RowTl = None
        self.ColBr = None
        self.RowBr = None
        self.Text = None
        self.Type = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.ColTl = params.get("ColTl")
        self.RowTl = params.get("RowTl")
        self.ColBr = params.get("ColBr")
        self.RowBr = params.get("RowBr")
        self.Text = params.get("Text")
        self.Type = params.get("Type")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")


class TextVatInvoice(AbstractModel):
    """增值税发票识别结果

    """

    def __init__(self):
        """
        :param Name: 识别出的字段名称（关键字）。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class TextVehicleBack(AbstractModel):
    """TextVehicleBack

    """

    def __init__(self):
        """
        :param PlateNo: 号牌号码
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateNo: str
        :param FileNo: 档案编号
注意：此字段可能返回 null，表示取不到有效值。
        :type FileNo: str
        :param AllowNum: 核定人数
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowNum: str
        :param TotalMass: 总质量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalMass: str
        :param CurbWeight: 整备质量
注意：此字段可能返回 null，表示取不到有效值。
        :type CurbWeight: str
        :param LoadQuality: 核定载质量
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadQuality: str
        :param ExternalSize: 外廓尺寸
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalSize: str
        :param Marks: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Marks: str
        :param Record: 检验记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Record: str
        :param TotalQuasiMass: 准牵引总质量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalQuasiMass: str
        """
        self.PlateNo = None
        self.FileNo = None
        self.AllowNum = None
        self.TotalMass = None
        self.CurbWeight = None
        self.LoadQuality = None
        self.ExternalSize = None
        self.Marks = None
        self.Record = None
        self.TotalQuasiMass = None


    def _deserialize(self, params):
        self.PlateNo = params.get("PlateNo")
        self.FileNo = params.get("FileNo")
        self.AllowNum = params.get("AllowNum")
        self.TotalMass = params.get("TotalMass")
        self.CurbWeight = params.get("CurbWeight")
        self.LoadQuality = params.get("LoadQuality")
        self.ExternalSize = params.get("ExternalSize")
        self.Marks = params.get("Marks")
        self.Record = params.get("Record")
        self.TotalQuasiMass = params.get("TotalQuasiMass")


class TextVehicleFront(AbstractModel):
    """TextVehicleFront

    """

    def __init__(self):
        """
        :param PlateNo: 号牌号码
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateNo: str
        :param VehicleType: 车辆类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VehicleType: str
        :param Owner: 所有人
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param Address: 住址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param UseCharacter: 使用性质
注意：此字段可能返回 null，表示取不到有效值。
        :type UseCharacter: str
        :param Model: 品牌型号
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param Vin: 车辆识别代号
注意：此字段可能返回 null，表示取不到有效值。
        :type Vin: str
        :param EngineNo: 发动机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineNo: str
        :param RegisterDate: 注册日期
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisterDate: str
        :param IssueDate: 发证日期
注意：此字段可能返回 null，表示取不到有效值。
        :type IssueDate: str
        :param Seal: 印章
注意：此字段可能返回 null，表示取不到有效值。
        :type Seal: str
        """
        self.PlateNo = None
        self.VehicleType = None
        self.Owner = None
        self.Address = None
        self.UseCharacter = None
        self.Model = None
        self.Vin = None
        self.EngineNo = None
        self.RegisterDate = None
        self.IssueDate = None
        self.Seal = None


    def _deserialize(self, params):
        self.PlateNo = params.get("PlateNo")
        self.VehicleType = params.get("VehicleType")
        self.Owner = params.get("Owner")
        self.Address = params.get("Address")
        self.UseCharacter = params.get("UseCharacter")
        self.Model = params.get("Model")
        self.Vin = params.get("Vin")
        self.EngineNo = params.get("EngineNo")
        self.RegisterDate = params.get("RegisterDate")
        self.IssueDate = params.get("IssueDate")
        self.Seal = params.get("Seal")


class TextWaybill(AbstractModel):
    """运单识别结果

    """

    def __init__(self):
        """
        :param RecName: 收件人姓名
        :type RecName: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param RecNum: 收件人手机号
        :type RecNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param RecAddr: 收件人地址
        :type RecAddr: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param SenderName: 寄件人姓名
        :type SenderName: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param SenderNum: 寄件人手机号
        :type SenderNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param SenderAddr: 寄件人地址
        :type SenderAddr: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param WaybillNum: 运单号
        :type WaybillNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        """
        self.RecName = None
        self.RecNum = None
        self.RecAddr = None
        self.SenderName = None
        self.SenderNum = None
        self.SenderAddr = None
        self.WaybillNum = None


    def _deserialize(self, params):
        if params.get("RecName") is not None:
            self.RecName = WaybillObj()
            self.RecName._deserialize(params.get("RecName"))
        if params.get("RecNum") is not None:
            self.RecNum = WaybillObj()
            self.RecNum._deserialize(params.get("RecNum"))
        if params.get("RecAddr") is not None:
            self.RecAddr = WaybillObj()
            self.RecAddr._deserialize(params.get("RecAddr"))
        if params.get("SenderName") is not None:
            self.SenderName = WaybillObj()
            self.SenderName._deserialize(params.get("SenderName"))
        if params.get("SenderNum") is not None:
            self.SenderNum = WaybillObj()
            self.SenderNum._deserialize(params.get("SenderNum"))
        if params.get("SenderAddr") is not None:
            self.SenderAddr = WaybillObj()
            self.SenderAddr._deserialize(params.get("SenderAddr"))
        if params.get("WaybillNum") is not None:
            self.WaybillNum = WaybillObj()
            self.WaybillNum._deserialize(params.get("WaybillNum"))


class VatInvoiceOCRRequest(AbstractModel):
    """VatInvoiceOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class VatInvoiceOCRResponse(AbstractModel):
    """VatInvoiceOCR返回参数结构体

    """

    def __init__(self):
        """
        :param VatInvoiceInfos: 检测到的文本信息，具体内容请点击左侧链接。
        :type VatInvoiceInfos: list of TextVatInvoice
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VatInvoiceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VatInvoiceInfos") is not None:
            self.VatInvoiceInfos = []
            for item in params.get("VatInvoiceInfos"):
                obj = TextVatInvoice()
                obj._deserialize(item)
                self.VatInvoiceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class VehicleLicenseOCRRequest(AbstractModel):
    """VehicleLicenseOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param CardSide: FRONT 为行驶证主页正面（有红色印章的一面），
BACK 为行驶证副页正面（有号码号牌的一面）。
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")


class VehicleLicenseOCRResponse(AbstractModel):
    """VehicleLicenseOCR返回参数结构体

    """

    def __init__(self):
        """
        :param FrontInfo: 行驶证主页正面的识别结果，CardSide 为 FRONT。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleFront`
        :param BackInfo: 行驶证副页正面的识别结果，CardSide 为 BACK。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleBack`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrontInfo = None
        self.BackInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FrontInfo") is not None:
            self.FrontInfo = TextVehicleFront()
            self.FrontInfo._deserialize(params.get("FrontInfo"))
        if params.get("BackInfo") is not None:
            self.BackInfo = TextVehicleBack()
            self.BackInfo._deserialize(params.get("BackInfo"))
        self.RequestId = params.get("RequestId")


class VinOCRRequest(AbstractModel):
    """VinOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class VinOCRResponse(AbstractModel):
    """VinOCR返回参数结构体

    """

    def __init__(self):
        """
        :param Vin: 检测到的车辆 VIN 码。
        :type Vin: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Vin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Vin = params.get("Vin")
        self.RequestId = params.get("RequestId")


class WaybillOCRRequest(AbstractModel):
    """WaybillOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class WaybillOCRResponse(AbstractModel):
    """WaybillOCR返回参数结构体

    """

    def __init__(self):
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextDetections: :class:`tencentcloud.ocr.v20181119.models.TextWaybill`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = TextWaybill()
            self.TextDetections._deserialize(params.get("TextDetections"))
        self.RequestId = params.get("RequestId")


class WaybillObj(AbstractModel):
    """运单识别对象

    """

    def __init__(self):
        """
        :param Text: 识别出的文本行内容
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")