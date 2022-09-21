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


class AdvertiseOCRRequest(AbstractModel):
    """AdvertiseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvertiseOCRResponse(AbstractModel):
    """AdvertiseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of AdvertiseTextDetection
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = AdvertiseTextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class AdvertiseTextDetection(AbstractModel):
    """广告文字识别结果

    """

    def __init__(self):
        r"""
        :param DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四个顶点坐标表示
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArithmeticOCRRequest(AbstractModel):
    """ArithmeticOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param SupportHorizontalImage: 用于选择是否支持横屏拍摄。打开则支持横屏拍摄图片角度判断，角度信息在返回参数的angle中，默认值为true
        :type SupportHorizontalImage: bool
        :param RejectNonArithmeticPic: 是否拒绝非速算图，打开则拒绝非速算图(注：非速算图是指风景人物等明显不是速算图片的图片)，默认值为false
        :type RejectNonArithmeticPic: bool
        :param EnableDispRelatedVertical: 是否展开耦合算式中的竖式计算，默认值为false
        :type EnableDispRelatedVertical: bool
        :param EnableDispMidResult: 是否展示竖式算式的中间结果和格式控制字符，默认值为false
        :type EnableDispMidResult: bool
        :param EnablePdfRecognize: 是否开启pdf识别，默认值为true
        :type EnablePdfRecognize: bool
        :param PdfPageIndex: pdf页码，从0开始，默认为0
        :type PdfPageIndex: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.SupportHorizontalImage = None
        self.RejectNonArithmeticPic = None
        self.EnableDispRelatedVertical = None
        self.EnableDispMidResult = None
        self.EnablePdfRecognize = None
        self.PdfPageIndex = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.SupportHorizontalImage = params.get("SupportHorizontalImage")
        self.RejectNonArithmeticPic = params.get("RejectNonArithmeticPic")
        self.EnableDispRelatedVertical = params.get("EnableDispRelatedVertical")
        self.EnableDispMidResult = params.get("EnableDispMidResult")
        self.EnablePdfRecognize = params.get("EnablePdfRecognize")
        self.PdfPageIndex = params.get("PdfPageIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArithmeticOCRResponse(AbstractModel):
    """ArithmeticOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextArithmetic
        :param Angle: 图片横屏的角度(90度或270度)
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextArithmetic()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class BankCardOCRRequest(AbstractModel):
    """BankCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param RetBorderCutImage: 是否返回预处理（精确剪裁对齐）后的银行卡图片数据，默认false。
        :type RetBorderCutImage: bool
        :param RetCardNoImage: 是否返回卡号的切图图片数据，默认false。
        :type RetCardNoImage: bool
        :param EnableCopyCheck: 复印件检测开关，如果输入的图片是银行卡复印件图片则返回告警，默认false。
        :type EnableCopyCheck: bool
        :param EnableReshootCheck: 翻拍检测开关，如果输入的图片是银行卡翻拍图片则返回告警，默认false。
        :type EnableReshootCheck: bool
        :param EnableBorderCheck: 边框遮挡检测开关，如果输入的图片是银行卡边框被遮挡则返回告警，默认false。
        :type EnableBorderCheck: bool
        :param EnableQualityValue: 是否返回图片质量分数（图片质量分数是评价一个图片的模糊程度的标准），默认false。
        :type EnableQualityValue: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetBorderCutImage = None
        self.RetCardNoImage = None
        self.EnableCopyCheck = None
        self.EnableReshootCheck = None
        self.EnableBorderCheck = None
        self.EnableQualityValue = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetBorderCutImage = params.get("RetBorderCutImage")
        self.RetCardNoImage = params.get("RetCardNoImage")
        self.EnableCopyCheck = params.get("EnableCopyCheck")
        self.EnableReshootCheck = params.get("EnableReshootCheck")
        self.EnableBorderCheck = params.get("EnableBorderCheck")
        self.EnableQualityValue = params.get("EnableQualityValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardOCRResponse(AbstractModel):
    """BankCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param CardNo: 卡号
        :type CardNo: str
        :param BankInfo: 银行信息
        :type BankInfo: str
        :param ValidDate: 有效期，格式如：07/2023
        :type ValidDate: str
        :param CardType: 卡类型
        :type CardType: str
        :param CardName: 卡名字
        :type CardName: str
        :param BorderCutImage: 切片图片数据
注意：此字段可能返回 null，表示取不到有效值。
        :type BorderCutImage: str
        :param CardNoImage: 卡号图片数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CardNoImage: str
        :param WarningCode: WarningCode 告警码列表和释义：
-9110:银行卡日期无效; 
-9111:银行卡边框不完整; 
-9112:银行卡图片反光;
-9113:银行卡复印件;
-9114:银行卡翻拍件
（告警码可以同时存在多个）
注意：此字段可能返回 null，表示取不到有效值。
        :type WarningCode: list of int
        :param QualityValue: 图片质量分数，请求EnableQualityValue时返回（取值范围：0-100，分数越低越模糊，建议阈值≥50）。
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityValue: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CardNo = None
        self.BankInfo = None
        self.ValidDate = None
        self.CardType = None
        self.CardName = None
        self.BorderCutImage = None
        self.CardNoImage = None
        self.WarningCode = None
        self.QualityValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CardNo = params.get("CardNo")
        self.BankInfo = params.get("BankInfo")
        self.ValidDate = params.get("ValidDate")
        self.CardType = params.get("CardType")
        self.CardName = params.get("CardName")
        self.BorderCutImage = params.get("BorderCutImage")
        self.CardNoImage = params.get("CardNoImage")
        self.WarningCode = params.get("WarningCode")
        self.QualityValue = params.get("QualityValue")
        self.RequestId = params.get("RequestId")


class BankSlipInfo(AbstractModel):
    """银行回单识别出的字段

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
付款开户行、收款开户行、付款账号、收款账号、回单类型、回单编号、币种、流水号、凭证号码、交易机构、交易金额、手续费、日期等字段信息。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankSlipOCRRequest(AbstractModel):
    """BankSlipOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankSlipOCRResponse(AbstractModel):
    """BankSlipOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param BankSlipInfos: 银行回单识别结果，具体内容请点击左侧链接。
        :type BankSlipInfos: list of BankSlipInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BankSlipInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BankSlipInfos") is not None:
            self.BankSlipInfos = []
            for item in params.get("BankSlipInfos"):
                obj = BankSlipInfo()
                obj._deserialize(item)
                self.BankSlipInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class BizLicenseOCRRequest(AbstractModel):
    """BizLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BizLicenseOCRResponse(AbstractModel):
    """BizLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegNum: 统一社会信用代码（三合一之前为注册号）
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
        :param SetDate: 成立日期
        :type SetDate: str
        :param RecognizeWarnCode: Code 告警码列表和释义：
-20001 非营业执照
-9102 黑白复印件告警
注：告警码可以同时存在多个
        :type RecognizeWarnCode: list of int
        :param RecognizeWarnMsg: 告警码说明：
OCR_WARNING_TPYE_NOT_MATCH 非营业执照
WARN_COPY_CARD 黑白复印件告警
注：告警信息可以同时存在多个
        :type RecognizeWarnMsg: list of str
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
        self.SetDate = None
        self.RecognizeWarnCode = None
        self.RecognizeWarnMsg = None
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
        self.SetDate = params.get("SetDate")
        self.RecognizeWarnCode = params.get("RecognizeWarnCode")
        self.RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self.RequestId = params.get("RequestId")


class BizLicenseVerifyResult(AbstractModel):
    """验真接口

    """

    def __init__(self):
        r"""
        :param RegNum: “0“：一致
“-1”：不一致
        :type RegNum: str
        :param Name: “0“：一致
“-1”：不一致
“”：不验真
        :type Name: str
        :param Address: “0“：一致
“-1”：不一致
“”：不验真
        :type Address: str
        """
        self.RegNum = None
        self.Name = None
        self.Address = None


    def _deserialize(self, params):
        self.RegNum = params.get("RegNum")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusInvoiceInfo(AbstractModel):
    """汽车票字段信息

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、发票号码、日期、票价、始发地、目的地、姓名、时间、发票消费类型、身份证号、省、市、开票日期、乘车地点、检票口、客票类型、车型、座位号、车次。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusInvoiceOCRRequest(AbstractModel):
    """BusInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusInvoiceOCRResponse(AbstractModel):
    """BusInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param BusInvoiceInfos: 汽车票识别结果，具体内容请点击左侧链接。
        :type BusInvoiceInfos: list of BusInvoiceInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BusInvoiceInfos") is not None:
            self.BusInvoiceInfos = []
            for item in params.get("BusInvoiceInfos"):
                obj = BusInvoiceInfo()
                obj._deserialize(item)
                self.BusInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class BusinessCardInfo(AbstractModel):
    """名片识别结果

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称（关键字，可能重复，比如多个手机），能识别的字段名为：
姓名、英文姓名、英文地址、公司、英文公司、职位、英文职位、部门、英文部门、手机、电话、传真、社交帐号、QQ、MSN、微信、微博、邮箱、邮编、网址、公司账号、其他。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        :param ItemCoord: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        self.Name = None
        self.Value = None
        self.ItemCoord = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("ItemCoord") is not None:
            self.ItemCoord = ItemCoord()
            self.ItemCoord._deserialize(params.get("ItemCoord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessCardOCRRequest(AbstractModel):
    """BusinessCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessCardOCRResponse(AbstractModel):
    """BusinessCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessCardInfos: 名片识别结果，具体内容请点击左侧链接。
        :type BusinessCardInfos: list of BusinessCardInfo
        :param RetImageBase64: 返回图像预处理后的图片，图像预处理未开启时返回内容为空。
        :type RetImageBase64: str
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCardInfos = None
        self.RetImageBase64 = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BusinessCardInfos") is not None:
            self.BusinessCardInfos = []
            for item in params.get("BusinessCardInfos"):
                obj = BusinessCardInfo()
                obj._deserialize(item)
                self.BusinessCardInfos.append(obj)
        self.RetImageBase64 = params.get("RetImageBase64")
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class CandWord(AbstractModel):
    """候选字符集(包含候选字Character以及置信度Confidence)

    """

    def __init__(self):
        r"""
        :param CandWords: 候选字符集的单词信息（包括单词Character和单词置信度confidence）
        :type CandWords: list of Words
        """
        self.CandWords = None


    def _deserialize(self, params):
        if params.get("CandWords") is not None:
            self.CandWords = []
            for item in params.get("CandWords"):
                obj = Words()
                obj._deserialize(item)
                self.CandWords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarInvoiceInfo(AbstractModel):
    """购车发票识别结果

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、 机打代码、 发票号码、 发动机号码、 合格证号、 机打号码、 价税合计(小写)、 销货单位名称、 身份证号码/组织机构代码、 购买方名称、 销售方纳税人识别号、 购买方纳税人识别号、主管税务机关、 主管税务机关代码、 开票日期、 不含税价(小写)、 吨位、增值税税率或征收率、 车辆识别代号/车架号码、 增值税税额、 厂牌型号、 省、 市、 发票消费类型、 销售方电话、 销售方账号、 产地、 进口证明书号、 车辆类型、 机器编号、备注、开票人、限乘人数、商检单号、销售方地址、销售方开户银行、价税合计、发票类型。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        :param Rect: 字段在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param Polygon: 字段在原图中的中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self.Name = None
        self.Value = None
        self.Rect = None
        self.Polygon = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        if params.get("Polygon") is not None:
            self.Polygon = Polygon()
            self.Polygon._deserialize(params.get("Polygon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarInvoiceOCRRequest(AbstractModel):
    """CarInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarInvoiceOCRResponse(AbstractModel):
    """CarInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param CarInvoiceInfos: 购车发票识别结果，具体内容请点击左侧链接。
        :type CarInvoiceInfos: list of CarInvoiceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CarInvoiceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CarInvoiceInfos") is not None:
            self.CarInvoiceInfos = []
            for item in params.get("CarInvoiceInfos"):
                obj = CarInvoiceInfo()
                obj._deserialize(item)
                self.CarInvoiceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class CellContent(AbstractModel):
    """单元格识别结果

    """

    def __init__(self):
        r"""
        :param ParagNo: 段落编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ParagNo: int
        :param WordSize: 字体大小
注意：此字段可能返回 null，表示取不到有效值。
        :type WordSize: int
        """
        self.ParagNo = None
        self.WordSize = None


    def _deserialize(self, params):
        self.ParagNo = params.get("ParagNo")
        self.WordSize = params.get("WordSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyDetectInfo(AbstractModel):
    """卡证智能分类结果

    """

    def __init__(self):
        r"""
        :param Name: 分类名称，包括：身份证、护照、名片、银行卡、行驶证、驾驶证、港澳台通行证、户口本、港澳台来往内地通行证、港澳台居住证、不动产证、营业执照
        :type Name: str
        :param Type: 分类类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Rect: 位置坐标
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Type = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyDetectOCRRequest(AbstractModel):
    """ClassifyDetectOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param DiscernType: 可以指定要识别的票证类型,指定后不出现在此列表的票证将不返回类型。不指定时默认返回所有支持类别票证的识别信息。

以下是当前支持的类型：
IDCardFront: 身份证正面识别
IDCardBack: 身份证背面识别
Passport: 护照
BusinessCard: 名片识别
BankCard: 银行卡识别
VehicleLicenseFront: 行驶证主页识别
VehicleLicenseBack: 行驶证副页识别
DriverLicenseFront: 驾驶证主页识别
DriverLicenseBack: 驾驶证副页识别
PermitFront: 港澳台通行证正面
ResidenceBooklet: 户口本资料页
MainlandPermitFront: 港澳台来往内地通行证正面
HmtResidentPermitFront: 港澳台居住证正面
HmtResidentPermitBack: 港澳台居住证背面
EstateCert: 不动产证
BizLicense: 营业执照
        :type DiscernType: list of str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.DiscernType = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.DiscernType = params.get("DiscernType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyDetectOCRResponse(AbstractModel):
    """ClassifyDetectOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClassifyDetectInfos: 智能卡证分类结果。当图片类型不支持分类识别或者识别出的类型不在请求参数DiscernType指定的范围内时，返回结果中的Type字段将为空字符串，Name字段将返回"其它"
        :type ClassifyDetectInfos: list of ClassifyDetectInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClassifyDetectInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassifyDetectInfos") is not None:
            self.ClassifyDetectInfos = []
            for item in params.get("ClassifyDetectInfos"):
                obj = ClassifyDetectInfo()
                obj._deserialize(item)
                self.ClassifyDetectInfos.append(obj)
        self.RequestId = params.get("RequestId")


class Coord(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Detail(AbstractModel):
    """企业四要素核验结果

    """

    def __init__(self):
        r"""
        :param Result: 企业四要素核验结果状态码
        :type Result: int
        :param Desc: 企业四要素核验结果描述
        :type Desc: str
        """
        self.Result = None
        self.Desc = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectedWordCoordPoint(AbstractModel):
    """单字在原图中的坐标，以四个顶点坐标表示，以左上角为起点，顺时针返回。

    """

    def __init__(self):
        r"""
        :param WordCoordinate: 单字在原图中的坐标，以四个顶点坐标表示，以左上角为起点，顺时针返回。
        :type WordCoordinate: list of Coord
        """
        self.WordCoordinate = None


    def _deserialize(self, params):
        if params.get("WordCoordinate") is not None:
            self.WordCoordinate = []
            for item in params.get("WordCoordinate"):
                obj = Coord()
                obj._deserialize(item)
                self.WordCoordinate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectedWords(AbstractModel):
    """识别出来的单字信息包括单字（包括单字Character和单字置信度confidence）

    """

    def __init__(self):
        r"""
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Character: 候选字Character
        :type Character: str
        """
        self.Confidence = None
        self.Character = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Character = params.get("Character")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DriverLicenseOCRRequest(AbstractModel):
    """DriverLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param CardSide: FRONT 为驾驶证主页正面（有红色印章的一面），
BACK 为驾驶证副页正面（有档案编号的一面）。
默认值为：FRONT。
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DriverLicenseOCRResponse(AbstractModel):
    """DriverLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param Nationality: 国籍
        :type Nationality: str
        :param Address: 住址
        :type Address: str
        :param DateOfBirth: 出生日期（YYYY-MM-DD）
        :type DateOfBirth: str
        :param DateOfFirstIssue: 初次领证日期（YYYY-MM-DD）
        :type DateOfFirstIssue: str
        :param Class: 准驾车型
        :type Class: str
        :param StartDate: 有效期开始时间（YYYY-MM-DD）
        :type StartDate: str
        :param EndDate: 有效期截止时间（YYYY-MM-DD）
        :type EndDate: str
        :param CardCode: 证号
        :type CardCode: str
        :param ArchivesCode: 档案编号
        :type ArchivesCode: str
        :param Record: 记录
        :type Record: str
        :param RecognizeWarnCode: Code 告警码列表和释义：
-9102  复印件告警
-9103  翻拍件告警
-9106  ps告警
注：告警码可以同时存在多个
        :type RecognizeWarnCode: list of int
        :param RecognizeWarnMsg: 告警码说明：
WARN_DRIVER_LICENSE_COPY_CARD 复印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
WARN_DRIVER_LICENSE_PS_CARD ps告警
注：告警信息可以同时存在多个
        :type RecognizeWarnMsg: list of str
        :param IssuingAuthority: 发证单位
        :type IssuingAuthority: str
        :param State: 状态（仅电子驾驶证支持返回该字段）
        :type State: str
        :param CumulativeScore: 累积记分（仅电子驾驶证支持返回该字段）
        :type CumulativeScore: str
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
        self.ArchivesCode = None
        self.Record = None
        self.RecognizeWarnCode = None
        self.RecognizeWarnMsg = None
        self.IssuingAuthority = None
        self.State = None
        self.CumulativeScore = None
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
        self.ArchivesCode = params.get("ArchivesCode")
        self.Record = params.get("Record")
        self.RecognizeWarnCode = params.get("RecognizeWarnCode")
        self.RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self.IssuingAuthority = params.get("IssuingAuthority")
        self.State = params.get("State")
        self.CumulativeScore = params.get("CumulativeScore")
        self.RequestId = params.get("RequestId")


class DutyPaidProofInfo(AbstractModel):
    """识别出的字段

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
税号 、纳税人识别号 、纳税人名称 、金额合计大写 、金额合计小写 、填发日期 、税务机关 、填票人。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DutyPaidProofOCRRequest(AbstractModel):
    """DutyPaidProofOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DutyPaidProofOCRResponse(AbstractModel):
    """DutyPaidProofOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param DutyPaidProofInfos: 完税证明识别结果，具体内容请点击左侧链接。
        :type DutyPaidProofInfos: list of DutyPaidProofInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DutyPaidProofInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DutyPaidProofInfos") is not None:
            self.DutyPaidProofInfos = []
            for item in params.get("DutyPaidProofInfos"):
                obj = DutyPaidProofInfo()
                obj._deserialize(item)
                self.DutyPaidProofInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class EduPaperOCRRequest(AbstractModel):
    """EduPaperOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Config: 扩展配置信息。
配置格式：{"option1":value1,"option2":value2}
1. task_type：任务类型【0: 关闭版式分析与处理 1: 开启版式分析处理】可选参数，Int32类型，默认值为1
2. is_structuralization：是否结构化输出【true：返回包体同时返回通用和结构化输出  false：返回包体返回通用输出】 可选参数，Bool类型，默认值为true
3. if_readable_format：是否按照版式整合通用文本/公式输出结果 可选参数，Bool类型，默认值为false
示例：
{"task_type": 1,"is_structuralization": true,"if_readable_format": true}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EduPaperOCRResponse(AbstractModel):
    """EduPaperOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param EduPaperInfos: 检测到的文本信息，具体内容请点击左侧链接。
        :type EduPaperInfos: list of TextEduPaper
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。
        :type Angle: int
        :param QuestionBlockInfos: 结构化方式输出，具体内容请点击左侧链接。
        :type QuestionBlockInfos: list of QuestionBlockObj
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EduPaperInfos = None
        self.Angle = None
        self.QuestionBlockInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EduPaperInfos") is not None:
            self.EduPaperInfos = []
            for item in params.get("EduPaperInfos"):
                obj = TextEduPaper()
                obj._deserialize(item)
                self.EduPaperInfos.append(obj)
        self.Angle = params.get("Angle")
        if params.get("QuestionBlockInfos") is not None:
            self.QuestionBlockInfos = []
            for item in params.get("QuestionBlockInfos"):
                obj = QuestionBlockObj()
                obj._deserialize(item)
                self.QuestionBlockInfos.append(obj)
        self.RequestId = params.get("RequestId")


class EnglishOCRRequest(AbstractModel):
    """EnglishOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param EnableCoordPoint: 单词四点坐标开关，开启可返回图片中单词的四点坐标。
该参数默认值为false。
        :type EnableCoordPoint: bool
        :param EnableCandWord: 候选字开关，开启可返回识别时多个可能的候选字（每个候选字对应其置信度）。
该参数默认值为false。
        :type EnableCandWord: bool
        :param Preprocess: 预处理开关，功能是检测图片倾斜的角度，将原本倾斜的图片矫正。该参数默认值为true。
        :type Preprocess: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.EnableCoordPoint = None
        self.EnableCandWord = None
        self.Preprocess = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.EnableCoordPoint = params.get("EnableCoordPoint")
        self.EnableCandWord = params.get("EnableCandWord")
        self.Preprocess = params.get("Preprocess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnglishOCRResponse(AbstractModel):
    """EnglishOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetectionEn
        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetectionEn()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class EnterpriseLicenseInfo(AbstractModel):
    """企业证照单个字段的内容

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称（关键字），不同证件类型可能不同，证件类型包含企业登记证书、许可证书、企业执照、三证合一类证书；
支持以下字段：统一社会信用代码、法定代表人、公司名称、公司地址、注册资金、企业关型、经营范围、成立日期、有效期、开办资金、经费来源、举办单位等；
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterpriseLicenseOCRRequest(AbstractModel):
    """EnterpriseLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterpriseLicenseOCRResponse(AbstractModel):
    """EnterpriseLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnterpriseLicenseInfos: 企业证照识别结果，具体内容请点击左侧链接。
        :type EnterpriseLicenseInfos: list of EnterpriseLicenseInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnterpriseLicenseInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnterpriseLicenseInfos") is not None:
            self.EnterpriseLicenseInfos = []
            for item in params.get("EnterpriseLicenseInfos"):
                obj = EnterpriseLicenseInfo()
                obj._deserialize(item)
                self.EnterpriseLicenseInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class EstateCertOCRRequest(AbstractModel):
    """EstateCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstateCertOCRResponse(AbstractModel):
    """EstateCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Obligee: 权利人
        :type Obligee: str
        :param Ownership: 共有情况
        :type Ownership: str
        :param Location: 坐落
        :type Location: str
        :param Unit: 不动产单元号
        :type Unit: str
        :param Type: 权利类型
        :type Type: str
        :param Property: 权利性质
        :type Property: str
        :param Usage: 用途
        :type Usage: str
        :param Area: 面积
        :type Area: str
        :param Term: 使用期限
        :type Term: str
        :param Other: 权利其他状况，多行会用换行符\n连接。
        :type Other: str
        :param Angle: 图片旋转角度
        :type Angle: float
        :param Number: 不动产权号
        :type Number: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Obligee = None
        self.Ownership = None
        self.Location = None
        self.Unit = None
        self.Type = None
        self.Property = None
        self.Usage = None
        self.Area = None
        self.Term = None
        self.Other = None
        self.Angle = None
        self.Number = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Obligee = params.get("Obligee")
        self.Ownership = params.get("Ownership")
        self.Location = params.get("Location")
        self.Unit = params.get("Unit")
        self.Type = params.get("Type")
        self.Property = params.get("Property")
        self.Usage = params.get("Usage")
        self.Area = params.get("Area")
        self.Term = params.get("Term")
        self.Other = params.get("Other")
        self.Angle = params.get("Angle")
        self.Number = params.get("Number")
        self.RequestId = params.get("RequestId")


class FinanBillInfo(AbstractModel):
    """金融票据整单识别单个字段的内容

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
【进账单】
日期、出票全称、出票账号、出票开户行、收款人全称、收款人账号、收款开户行、大写金额、小写金额、票据种类、票据张数、票据号码；
【支票】
开户银行、支票种类、凭证号码2、日期、大写金额、小写金额、付款行编号、密码、凭证号码1；
【银行承兑汇票】或【商业承兑汇票】
出票日期、行号1、行号2、出票人全称、出票人账号、付款行全称、收款人全称、收款人账号、收款人开户行、出票金额大写、出票金额小写、汇票到期日、付款行行号、付款行地址。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillOCRRequest(AbstractModel):
    """FinanBillOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillOCRResponse(AbstractModel):
    """FinanBillOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param FinanBillInfos: 金融票据整单识别结果，具体内容请点击左侧链接。
        :type FinanBillInfos: list of FinanBillInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FinanBillInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FinanBillInfos") is not None:
            self.FinanBillInfos = []
            for item in params.get("FinanBillInfos"):
                obj = FinanBillInfo()
                obj._deserialize(item)
                self.FinanBillInfos.append(obj)
        self.RequestId = params.get("RequestId")


class FinanBillSliceInfo(AbstractModel):
    """金融票据切片识别单个字段的内容

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
大写金额、小写金额、账号、票号1、票号2、收款人、大写日期、同城交换号、地址-省份、地址-城市、付款行全称、支票密码、支票用途。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillSliceOCRRequest(AbstractModel):
    """FinanBillSliceOCR请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillSliceOCRResponse(AbstractModel):
    """FinanBillSliceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param FinanBillSliceInfos: 金融票据切片识别结果，具体内容请点击左侧链接。
        :type FinanBillSliceInfos: list of FinanBillSliceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FinanBillSliceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FinanBillSliceInfos") is not None:
            self.FinanBillSliceInfos = []
            for item in params.get("FinanBillSliceInfos"):
                obj = FinanBillSliceInfo()
                obj._deserialize(item)
                self.FinanBillSliceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class FlightInvoiceInfo(AbstractModel):
    """机票行程单识别结果

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
票价、合计金额、填开日期、有效身份证件号码、电子客票号码、验证码、旅客姓名、填开单位、其他税费、燃油附加费、民航发展基金、保险费、销售单位代号、始发地、目的地、航班号、时间、日期、座位等级、承运人、发票消费类型、国内国际标签、印刷序号、客票级别/类别、客票生效日期、有效期截止日期、免费行李。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段 Name 对应的字符串结果。
        :type Value: str
        :param Row: 多个行程的字段所在行号，下标从0开始，非行字段或未能识别行号的该值返回-1。
        :type Row: int
        """
        self.Name = None
        self.Value = None
        self.Row = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Row = params.get("Row")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlightInvoiceOCRRequest(AbstractModel):
    """FlightInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlightInvoiceOCRResponse(AbstractModel):
    """FlightInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlightInvoiceInfos: 机票行程单识别结果，具体内容请点击左侧链接。
        :type FlightInvoiceInfos: list of FlightInvoiceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlightInvoiceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlightInvoiceInfos") is not None:
            self.FlightInvoiceInfos = []
            for item in params.get("FlightInvoiceInfos"):
                obj = FlightInvoiceInfo()
                obj._deserialize(item)
                self.FlightInvoiceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class FormulaOCRRequest(AbstractModel):
    """FormulaOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormulaOCRResponse(AbstractModel):
    """FormulaOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负
        :type Angle: int
        :param FormulaInfos: 检测到的文本信息，具体内容请点击左侧链接。
        :type FormulaInfos: list of TextFormula
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Angle = None
        self.FormulaInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Angle = params.get("Angle")
        if params.get("FormulaInfos") is not None:
            self.FormulaInfos = []
            for item in params.get("FormulaInfos"):
                obj = TextFormula()
                obj._deserialize(item)
                self.FormulaInfos.append(obj)
        self.RequestId = params.get("RequestId")


class GeneralAccurateOCRRequest(AbstractModel):
    """GeneralAccurateOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param IsWords: 是否返回单字信息，默认关
        :type IsWords: bool
        :param EnableDetectSplit: 是否开启原图切图检测功能，开启后可提升“整图面积大，但单字符占比面积小”（例如：试卷）场景下的识别效果，默认关
        :type EnableDetectSplit: bool
        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.IsWords = None
        self.EnableDetectSplit = None
        self.IsPdf = None
        self.PdfPageNumber = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.IsWords = params.get("IsWords")
        self.EnableDetectSplit = params.get("EnableDetectSplit")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralAccurateOCRResponse(AbstractModel):
    """GeneralAccurateOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class GeneralBasicOCRRequest(AbstractModel):
    """GeneralBasicOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片/PDF的 Base64 值。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片/PDF的 Url 地址。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Scene: 保留字段。
        :type Scene: str
        :param LanguageType: 识别语言类型。
支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)，各种语言均支持与英文混合的文字识别。
可选值：
zh：中英混合
zh_rare：支持英文、数字、中文生僻字、繁体字，特殊符号等
auto：自动
mix：混合语种
jap：日语
kor：韩语
spa：西班牙语
fre：法语
ger：德语
por：葡萄牙语
vie：越语
may：马来语
rus：俄语
ita：意大利语
hol：荷兰语
swe：瑞典语
fin：芬兰语
dan：丹麦语
nor：挪威语
hun：匈牙利语
tha：泰语
hi：印地语
ara：阿拉伯语
        :type LanguageType: str
        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param IsWords: 是否返回单字信息，默认关
        :type IsWords: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None
        self.LanguageType = None
        self.IsPdf = None
        self.PdfPageNumber = None
        self.IsWords = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")
        self.LanguageType = params.get("LanguageType")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        self.IsWords = params.get("IsWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralBasicOCRResponse(AbstractModel):
    """GeneralBasicOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param Language: 检测到的语言类型，目前支持的语言类型参考入参LanguageType说明。
        :type Language: str
        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0
        :type PdfPageSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.Angel = None
        self.PdfPageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.Angel = params.get("Angel")
        self.PdfPageSize = params.get("PdfPageSize")
        self.RequestId = params.get("RequestId")


class GeneralEfficientOCRRequest(AbstractModel):
    """GeneralEfficientOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralEfficientOCRResponse(AbstractModel):
    """GeneralEfficientOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class GeneralFastOCRRequest(AbstractModel):
    """GeneralFastOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.IsPdf = None
        self.PdfPageNumber = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralFastOCRResponse(AbstractModel):
    """GeneralFastOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param Language: 检测到的语言，目前支持的语种范围为：简体中文、繁体中文、英文、日文、韩文。未来将陆续新增对更多语种的支持。
返回结果含义为：zh - 中英混合，jap - 日文，kor - 韩文。
        :type Language: str
        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负
        :type Angel: float
        :param PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0
        :type PdfPageSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.Angel = None
        self.PdfPageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.Angel = params.get("Angel")
        self.PdfPageSize = params.get("PdfPageSize")
        self.RequestId = params.get("RequestId")


class GeneralHandwritingOCRRequest(AbstractModel):
    """GeneralHandwritingOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Scene: 场景字段，默认不用填写。
可选值:only_hw  表示只输出手写体识别结果，过滤印刷体。
        :type Scene: str
        :param EnableWordPolygon: 是否开启单字的四点定位坐标输出，默认值为false。
        :type EnableWordPolygon: bool
        :param EnableDetectText: 文本检测开关，默认值为true。
设置为false表示直接进行单行识别，可适用于识别单行手写体签名场景。
        :type EnableDetectText: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None
        self.EnableWordPolygon = None
        self.EnableDetectText = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")
        self.EnableWordPolygon = params.get("EnableWordPolygon")
        self.EnableDetectText = params.get("EnableDetectText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralHandwritingOCRResponse(AbstractModel):
    """GeneralHandwritingOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextGeneralHandwriting
        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextGeneralHandwriting()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class HKIDCardOCRRequest(AbstractModel):
    """HKIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param DetectFake: 是否鉴伪。
        :type DetectFake: bool
        :param ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.DetectFake = None
        self.ReturnHeadImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.DetectFake = params.get("DetectFake")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HKIDCardOCRResponse(AbstractModel):
    """HKIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param CnName: 中文姓名
        :type CnName: str
        :param EnName: 英文姓名
        :type EnName: str
        :param TelexCode: 中文姓名对应电码
        :type TelexCode: str
        :param Sex: 性别 ：“男M”或“女F”
        :type Sex: str
        :param Birthday: 出生日期
        :type Birthday: str
        :param Permanent: 永久性居民身份证。
0：非永久；
1：永久；
-1：未知。
        :type Permanent: int
        :param IdNum: 身份证号码
        :type IdNum: str
        :param Symbol: 证件符号，出生日期下的符号，例如"***AZ"
        :type Symbol: str
        :param FirstIssueDate: 首次签发日期
        :type FirstIssueDate: str
        :param CurrentIssueDate: 最近领用日期
        :type CurrentIssueDate: str
        :param FakeDetectResult: 真假判断。
0：无法判断（图像模糊、不完整、反光、过暗等导致无法判断）；
1：假；
2：真。
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeDetectResult: int
        :param HeadImage: 人像照片Base64后的结果
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadImage: str
        :param WarningCode: 多重告警码，当身份证是翻拍、复印、PS件时返回对应告警码。
-9102：证照复印件告警
-9103：证照翻拍告警
-9104：证照PS告警
-9105：证照防伪告警
        :type WarningCode: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CnName = None
        self.EnName = None
        self.TelexCode = None
        self.Sex = None
        self.Birthday = None
        self.Permanent = None
        self.IdNum = None
        self.Symbol = None
        self.FirstIssueDate = None
        self.CurrentIssueDate = None
        self.FakeDetectResult = None
        self.HeadImage = None
        self.WarningCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CnName = params.get("CnName")
        self.EnName = params.get("EnName")
        self.TelexCode = params.get("TelexCode")
        self.Sex = params.get("Sex")
        self.Birthday = params.get("Birthday")
        self.Permanent = params.get("Permanent")
        self.IdNum = params.get("IdNum")
        self.Symbol = params.get("Symbol")
        self.FirstIssueDate = params.get("FirstIssueDate")
        self.CurrentIssueDate = params.get("CurrentIssueDate")
        self.FakeDetectResult = params.get("FakeDetectResult")
        self.HeadImage = params.get("HeadImage")
        self.WarningCode = params.get("WarningCode")
        self.RequestId = params.get("RequestId")


class HmtResidentPermitOCRRequest(AbstractModel):
    """HmtResidentPermitOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param CardSide: FRONT：有照片的一面（人像面），
BACK：无照片的一面（国徽面），
该参数如果不填或填错，将为您自动判断正反面。
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HmtResidentPermitOCRResponse(AbstractModel):
    """HmtResidentPermitOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 证件姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param Birth: 出生日期
        :type Birth: str
        :param Address: 地址
        :type Address: str
        :param IdCardNo: 身份证号
        :type IdCardNo: str
        :param CardType: 0-正面
1-反面
        :type CardType: int
        :param ValidDate: 证件有效期限
        :type ValidDate: str
        :param Authority: 签发机关
        :type Authority: str
        :param VisaNum: 签发次数
        :type VisaNum: str
        :param PassNo: 通行证号码
        :type PassNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Birth = None
        self.Address = None
        self.IdCardNo = None
        self.CardType = None
        self.ValidDate = None
        self.Authority = None
        self.VisaNum = None
        self.PassNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdCardNo = params.get("IdCardNo")
        self.CardType = params.get("CardType")
        self.ValidDate = params.get("ValidDate")
        self.Authority = params.get("Authority")
        self.VisaNum = params.get("VisaNum")
        self.PassNo = params.get("PassNo")
        self.RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param CardSide: FRONT：身份证有照片的一面（人像面），
BACK：身份证有国徽的一面（国徽面），
该参数如果不填，将为您自动判断身份证正反面。
        :type CardSide: str
        :param Config: 以下可选字段均为bool 类型，默认false：
CropIdCard，身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）
CropPortrait，人像照片裁剪（自动抠取身份证头像区域）
CopyWarn，复印件告警
BorderCheckWarn，边框和框内遮挡告警
ReshootWarn，翻拍告警
DetectPsWarn，PS检测告警
TempIdWarn，临时身份证告警
InvalidDateWarn，身份证有效日期不合法告警
Quality，图片质量分数（评价图片的模糊程度）
MultiCardDetect，是否开启多卡证检测
ReflectWarn，是否开启反光检测

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IDCardOCRResponse(AbstractModel):
    """IDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
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
        :param AdvancedInfo: 扩展信息，不请求则不返回，具体输入参考示例3和示例4。
IdCard，裁剪后身份证照片的base64编码，请求 Config.CropIdCard 时返回；
Portrait，身份证头像照片的base64编码，请求 Config.CropPortrait 时返回；

Quality，图片质量分数，请求 Config.Quality 时返回（取值范围：0 ~ 100，分数越低越模糊，建议阈值≥50）;
BorderCodeValue，身份证边框不完整告警阈值分数，请求 Config.BorderCheckWarn时返回（取值范围：0 ~ 100，分数越低边框遮挡可能性越低，建议阈值≤50）;

WarnInfos，告警信息，Code 告警码列表和释义：
-9100	身份证有效日期不合法告警，
-9101	身份证边框不完整告警，
-9102	身份证复印件告警，
-9103	身份证翻拍告警，
-9105	身份证框内遮挡告警，
-9104	临时身份证告警，
-9106	身份证 PS 告警，
-9107       身份证反光告警。
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


class ImageEnhancementRequest(AbstractModel):
    """ImageEnhancement请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param ReturnImage: 默认为空，ReturnImage的取值以及含义如下：
“preprocess”: 返回预处理后的图片数据
“origin”：返回原图片数据
" ":不返回图片数据
        :type ReturnImage: str
        :param TaskType: 默认值为1，指定图像增强方法：
1：切边增强
2：弯曲矫正
202：黑白模式
204：提亮模式
205：灰度模式
207：省墨模式
208：文字锐化（适合非彩色图片）
301：去摩尔纹
302：去除阴影
        :type TaskType: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnImage = None
        self.TaskType = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnImage = params.get("ReturnImage")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageEnhancementResponse(AbstractModel):
    """ImageEnhancement返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageTag: 图片数据标识：
“origin”：原图
“preprocess”:预处理后的图
        :type ImageTag: str
        :param Image: 图片数据，返回预处理后图像或原图像base64字符
        :type Image: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageTag = None
        self.Image = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageTag = params.get("ImageTag")
        self.Image = params.get("Image")
        self.RequestId = params.get("RequestId")


class InstitutionOCRRequest(AbstractModel):
    """InstitutionOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstitutionOCRResponse(AbstractModel):
    """InstitutionOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegId: 注册号
        :type RegId: str
        :param ValidDate: 有效期
        :type ValidDate: str
        :param Location: 住所
        :type Location: str
        :param Name: 名称
        :type Name: str
        :param LegalPerson: 法定代表人
        :type LegalPerson: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegId = None
        self.ValidDate = None
        self.Location = None
        self.Name = None
        self.LegalPerson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegId = params.get("RegId")
        self.ValidDate = params.get("ValidDate")
        self.Location = params.get("Location")
        self.Name = params.get("Name")
        self.LegalPerson = params.get("LegalPerson")
        self.RequestId = params.get("RequestId")


class InsuranceBillInfo(AbstractModel):
    """保险单据信息

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
【病案首页】
姓名、性别、出生日期、出院诊断、疾病编码、入院病情等。
【费用清单】
医疗参保人员类别、身份证号、入院方式、结账日期、项目、金额等。
【结算单】
名称、单价、数量、金额、医保内、医保外等。
【医疗发票】
姓名、性别、住院时间、收费项目、金额、合计等。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsuranceBillOCRRequest(AbstractModel):
    """InsuranceBillOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsuranceBillOCRResponse(AbstractModel):
    """InsuranceBillOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param InsuranceBillInfos: 保险单据识别结果，具体内容请点击左侧链接。
        :type InsuranceBillInfos: list of InsuranceBillInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InsuranceBillInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InsuranceBillInfos") is not None:
            self.InsuranceBillInfos = []
            for item in params.get("InsuranceBillInfos"):
                obj = InsuranceBillInfo()
                obj._deserialize(item)
                self.InsuranceBillInfos.append(obj)
        self.RequestId = params.get("RequestId")


class InvoiceDetectInfo(AbstractModel):
    """票据检测结果

    """

    def __init__(self):
        r"""
        :param Angle: 识别出的图片在混贴票据图片中的旋转角度。
        :type Angle: float
        :param Type: 识别出的图片所属的票据类型。
-1：未知类型
0：出租车发票
1：定额发票
2：火车票
3：增值税发票
4：客运限额发票
5：机票行程单
6：酒店账单
7：完税证明
8：通用机打发票
9：汽车票
10：轮船票
11：增值税发票（卷票 ）
12：购车发票
13：过路过桥费发票
14：购物小票
        :type Type: int
        :param Rect: 识别出的图片在混贴票据图片中的位置信息。与Angel结合可以得出原图位置，组成RotatedRect((X+0.5\*Width,Y+0.5\*Height), (Width, Height), Angle)，详情可参考OpenCV文档。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param Image: 入参 ReturnImage 为 True 时返回 Base64 编码后的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        """
        self.Angle = None
        self.Type = None
        self.Rect = None
        self.Image = None


    def _deserialize(self, params):
        self.Angle = params.get("Angle")
        self.Type = params.get("Type")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvoiceGeneralInfo(AbstractModel):
    """通用机打发票信息

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段识别（注：下划线表示一个字段）：
发票代码、发票号码、日期、合计金额(小写)、合计金额(大写)、购买方识别号、销售方识别号、校验码、购买方名称、销售方名称、时间、种类、发票消费类型、省、市、是否有公司印章、发票名称、<span style="text-decoration:underline">购买方地址、电话</span>、<span style="text-decoration:underline">销售方地址、电话</span>、购买方开户行及账号、销售方开户行及账号、经办人取票用户、经办人支付信息、经办人商户号、经办人订单号、<span style="text-decoration:underline">货物或应税劳务、服务名称</span>、数量、单价、税率、税额、金额、单位、规格型号、合计税额、合计金额、备注、收款人、复核、开票人、密码区、行业分类
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvoiceGeneralOCRRequest(AbstractModel):
    """InvoiceGeneralOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvoiceGeneralOCRResponse(AbstractModel):
    """InvoiceGeneralOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvoiceGeneralInfos: 通用机打发票识别结果，具体内容请点击左侧链接。
        :type InvoiceGeneralInfos: list of InvoiceGeneralInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceGeneralInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InvoiceGeneralInfos") is not None:
            self.InvoiceGeneralInfos = []
            for item in params.get("InvoiceGeneralInfos"):
                obj = InvoiceGeneralInfo()
                obj._deserialize(item)
                self.InvoiceGeneralInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class ItemCoord(AbstractModel):
    """文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）

    """

    def __init__(self):
        r"""
        :param X: 左上角x
        :type X: int
        :param Y: 左上角y
        :type Y: int
        :param Width: 宽width
        :type Width: int
        :param Height: 高height
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
        


class LicensePlateInfo(AbstractModel):
    """全部车牌信息

    """

    def __init__(self):
        r"""
        :param Number: 识别出的车牌号码。
        :type Number: str
        :param Confidence: 置信度，0 - 100 之间。
        :type Confidence: int
        :param Rect: 文本行在原图片中的像素坐标框。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param Color: 识别出的车牌颜色，目前支持颜色包括 “白”、“黑”、“蓝”、“绿“、“黄”、“黄绿”、“临牌”。
        :type Color: str
        """
        self.Number = None
        self.Confidence = None
        self.Rect = None
        self.Color = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateOCRRequest(AbstractModel):
    """LicensePlateOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateOCRResponse(AbstractModel):
    """LicensePlateOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Number: 识别出的车牌号码。
        :type Number: str
        :param Confidence: 置信度，0 - 100 之间。
        :type Confidence: int
        :param Rect: 文本行在原图片中的像素坐标框。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param Color: 识别出的车牌颜色，目前支持颜色包括 “白”、“黑”、“蓝”、“绿“、“黄”、“黄绿”、“临牌”。
        :type Color: str
        :param LicensePlateInfos: 全部车牌信息。
        :type LicensePlateInfos: list of LicensePlateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Number = None
        self.Confidence = None
        self.Rect = None
        self.Color = None
        self.LicensePlateInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Color = params.get("Color")
        if params.get("LicensePlateInfos") is not None:
            self.LicensePlateInfos = []
            for item in params.get("LicensePlateInfos"):
                obj = LicensePlateInfo()
                obj._deserialize(item)
                self.LicensePlateInfos.append(obj)
        self.RequestId = params.get("RequestId")


class MLIDCardOCRRequest(AbstractModel):
    """MLIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。( 中国地区之外不支持这个字段 )
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param RetImage: 是否返回图片，默认false
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRResponse(AbstractModel):
    """MLIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 身份证号
        :type ID: str
        :param Name: 姓名
        :type Name: str
        :param Address: 地址
        :type Address: str
        :param Sex: 性别
        :type Sex: str
        :param Warn: 告警码
-9103	证照翻拍告警
-9102	证照复印件告警
-9106       证件遮挡告警
-9107       模糊图片告警
        :type Warn: list of int
        :param Image: 证件图片
        :type Image: str
        :param AdvancedInfo: 此字段为扩展字段。
返回字段识别结果的置信度，格式如下
{
  字段名:{
    Confidence:0.9999
  }
}
        :type AdvancedInfo: str
        :param Type: 证件类型
MyKad  身份证
MyPR    永居证
MyTentera   军官证
MyKAS    临时身份证
POLIS  警察证
IKAD   劳工证
MyKid 儿童卡
        :type Type: str
        :param Birthday: 出生日期（目前该字段仅支持IKAD劳工证、MyKad 身份证）
        :type Birthday: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.Address = None
        self.Sex = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.Type = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        self.Sex = params.get("Sex")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.Type = params.get("Type")
        self.Birthday = params.get("Birthday")
        self.RequestId = params.get("RequestId")


class MLIDPassportOCRRequest(AbstractModel):
    """MLIDPassportOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
        :type ImageBase64: str
        :param RetImage: 是否返回图片，默认false
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDPassportOCRResponse(AbstractModel):
    """MLIDPassportOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 护照ID
        :type ID: str
        :param Name: 姓名
        :type Name: str
        :param DateOfBirth: 出生日期
        :type DateOfBirth: str
        :param Sex: 性别（F女，M男）
        :type Sex: str
        :param DateOfExpiration: 有效期
        :type DateOfExpiration: str
        :param IssuingCountry: 发行国
        :type IssuingCountry: str
        :param Nationality: 国家地区代码
        :type Nationality: str
        :param Warn: 告警码
-9103	证照翻拍告警
-9102	证照复印件告警
-9106       证件遮挡告警
        :type Warn: list of int
        :param Image: 证件图片
        :type Image: str
        :param AdvancedInfo: 扩展字段:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param CodeSet: 最下方第一行 MRZ Code 序列
        :type CodeSet: str
        :param CodeCrc: 最下方第二行 MRZ Code 序列
        :type CodeCrc: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.DateOfBirth = None
        self.Sex = None
        self.DateOfExpiration = None
        self.IssuingCountry = None
        self.Nationality = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.CodeSet = None
        self.CodeCrc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.DateOfBirth = params.get("DateOfBirth")
        self.Sex = params.get("Sex")
        self.DateOfExpiration = params.get("DateOfExpiration")
        self.IssuingCountry = params.get("IssuingCountry")
        self.Nationality = params.get("Nationality")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.CodeSet = params.get("CodeSet")
        self.CodeCrc = params.get("CodeCrc")
        self.RequestId = params.get("RequestId")


class MainlandPermitOCRRequest(AbstractModel):
    """MainlandPermitOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param RetProfile: 是否返回头像。默认不返回。
        :type RetProfile: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetProfile = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetProfile = params.get("RetProfile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRResponse(AbstractModel):
    """MainlandPermitOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 中文姓名
        :type Name: str
        :param EnglishName: 英文姓名
        :type EnglishName: str
        :param Sex: 性别
        :type Sex: str
        :param Birthday: 出生日期
        :type Birthday: str
        :param IssueAuthority: 签发机关
        :type IssueAuthority: str
        :param ValidDate: 有效期限
        :type ValidDate: str
        :param Number: 证件号
        :type Number: str
        :param IssueAddress: 签发地点
        :type IssueAddress: str
        :param IssueNumber: 签发次数
        :type IssueNumber: str
        :param Type: 证件类别， 如：台湾居民来往大陆通行证、港澳居民来往内地通行证。
        :type Type: str
        :param Profile: RetProfile为True时返回头像字段， Base64编码
        :type Profile: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.EnglishName = None
        self.Sex = None
        self.Birthday = None
        self.IssueAuthority = None
        self.ValidDate = None
        self.Number = None
        self.IssueAddress = None
        self.IssueNumber = None
        self.Type = None
        self.Profile = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EnglishName = params.get("EnglishName")
        self.Sex = params.get("Sex")
        self.Birthday = params.get("Birthday")
        self.IssueAuthority = params.get("IssueAuthority")
        self.ValidDate = params.get("ValidDate")
        self.Number = params.get("Number")
        self.IssueAddress = params.get("IssueAddress")
        self.IssueNumber = params.get("IssueNumber")
        self.Type = params.get("Type")
        self.Profile = params.get("Profile")
        self.RequestId = params.get("RequestId")


class MedicalInvoiceInfo(AbstractModel):
    """医疗发票识别结果

    """

    def __init__(self):
        r"""
        :param MedicalInvoiceItems: 医疗发票识别结果条目
        :type MedicalInvoiceItems: list of MedicalInvoiceItem
        """
        self.MedicalInvoiceItems = None


    def _deserialize(self, params):
        if params.get("MedicalInvoiceItems") is not None:
            self.MedicalInvoiceItems = []
            for item in params.get("MedicalInvoiceItems"):
                obj = MedicalInvoiceItem()
                obj._deserialize(item)
                self.MedicalInvoiceItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MedicalInvoiceItem(AbstractModel):
    """医疗发票识别结果

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称
<table><tr><td>分类</td><td>name</td></tr><tr><td>票据基本信息</td><td>发票名称</td></tr><tr><td></td><td>票据代码</td></tr><tr><td></td><td>票据号码</td></tr><tr><td></td><td>电子票据代码</td></tr><tr><td></td><td>电子票据号码</td></tr><tr><td></td><td>交款人统一社会信用代码</td></tr><tr><td></td><td>校验码</td></tr><tr><td></td><td>交款人</td></tr><tr><td></td><td>开票日期</td></tr><tr><td></td><td>收款单位</td></tr><tr><td></td><td>复核人</td></tr><tr><td></td><td>收款人</td></tr><tr><td></td><td>业务流水号</td></tr><tr><td></td><td>门诊号</td></tr><tr><td></td><td>就诊日期</td></tr><tr><td></td><td>医疗机构类型</td></tr><tr><td></td><td>医保类型</td></tr><tr><td></td><td>医保编号</td></tr><tr><td></td><td>性别</td></tr><tr><td></td><td>医保统筹基金支付</td></tr><tr><td></td><td>其他支付</td></tr><tr><td></td><td>个人账户支付</td></tr><tr><td></td><td>个人现金支付</td></tr><tr><td></td><td>个人自付</td></tr><tr><td></td><td>个人自费</td></tr><tr><td></td><td>病历号</td></tr><tr><td></td><td>住院号</td></tr><tr><td></td><td>住院科别</td></tr><tr><td></td><td>住院时间</td></tr><tr><td></td><td>预缴金额</td></tr><tr><td></td><td>补缴金额</td></tr><tr><td></td><td>退费金额</td></tr><tr><td></td><td>发票属地</td></tr><tr><td></td><td>发票类型</td></tr><tr><td>总金额</td><td>总金额大写</td></tr><tr><td></td><td>总金额小写</td></tr><tr><td>收费大项</td><td>大项名称</td></tr><tr><td></td><td>大项金额</td></tr><tr><td>收费细项</td><td>项目名称</td></tr><tr><td></td><td>数量</td></tr><tr><td></td><td>单位</td></tr><tr><td></td><td>金额</td></tr><tr><td></td><td>备注</td></tr><tr><td>票据其他信息</td><td>入院时间</td></tr><tr><td></td><td>出院时间</td></tr><tr><td></td><td>住院天数</td></tr><tr><td></td><td>自付二</td></tr><tr><td></td><td>自付一</td></tr><tr><td></td><td>起付金额</td></tr><tr><td></td><td>超封顶金额</td></tr><tr><td></td><td>自费</td></tr><tr><td></td><td>本次医保范围内金额</td></tr><tr><td></td><td>累计医保内范围金额</td></tr><tr><td></td><td>门诊大额支付</td></tr><tr><td></td><td>残军补助支付</td></tr><tr><td></td><td>年度门诊大额累计支付</td></tr><tr><td></td><td>单位补充险[原公疗]支付</td></tr><tr><td></td><td>社会保障卡号</td></tr><tr><td></td><td>姓名</td></tr><tr><td></td><td>交易流水号</td></tr><tr><td></td><td>本次支付后个人账户余额</td></tr><tr><td></td><td>基金支付</td></tr><tr><td></td><td>现金支付</td></tr><tr><td></td><td>复核</td></tr><tr><td></td><td>自负</td></tr><tr><td></td><td>结算方式</td></tr><tr><td></td><td>医保统筹/公医记账</td></tr><tr><td></td><td>其他</td></tr><tr><td></td><td>个人支付金额</td></tr><tr><td></td><td>欠费</td></tr><tr><td></td><td>退休补充支付</td></tr><tr><td></td><td>医院类型</td></tr><tr><td></td><td>退款</td></tr><tr><td></td><td>补收</td></tr><tr><td></td><td>附加支付</td></tr><tr><td></td><td>分类自负</td></tr><tr><td></td><td>其它</td></tr><tr><td></td><td>预交款</td></tr><tr><td></td><td>个人缴费</td></tr></table>
        :type Name: str
        :param Content: 识别出的字段名称对应的值，也就是字段name对应的字符串结果
        :type Content: str
        :param Vertex: 识别出的文本行四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Vertex: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param Coord: 识别出的文本行在旋转纠正之后的图像中的像素坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Content = None
        self.Vertex = None
        self.Coord = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        if params.get("Vertex") is not None:
            self.Vertex = Polygon()
            self.Vertex._deserialize(params.get("Vertex"))
        if params.get("Coord") is not None:
            self.Coord = Rect()
            self.Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceDetectRequest(AbstractModel):
    """MixedInvoiceDetect请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReturnImage: 是否需要返回裁剪后的图片。
        :type ReturnImage: bool
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ReturnImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ReturnImage = params.get("ReturnImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceDetectResponse(AbstractModel):
    """MixedInvoiceDetect返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvoiceDetectInfos: 检测出的票据类型列表，具体内容请点击左侧链接。
        :type InvoiceDetectInfos: list of InvoiceDetectInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceDetectInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InvoiceDetectInfos") is not None:
            self.InvoiceDetectInfos = []
            for item in params.get("InvoiceDetectInfos"):
                obj = InvoiceDetectInfo()
                obj._deserialize(item)
                self.InvoiceDetectInfos.append(obj)
        self.RequestId = params.get("RequestId")


class MixedInvoiceItem(AbstractModel):
    """混贴票据单张发票识别信息

    """

    def __init__(self):
        r"""
        :param Code: 识别结果。
OK：表示识别成功；FailedOperation.UnsupportedInvioce：表示不支持识别；
FailedOperation.UnKnowError：表示识别失败；
其它错误码见各个票据接口的定义。
        :type Code: str
        :param Type: 识别出的图片所属的票据类型。
-1：未知类型
0：出租车发票
1：定额发票
2：火车票
3：增值税发票
5：机票行程单
8：通用机打发票
9：汽车票
10：轮船票
11：增值税发票（卷票）
12：购车发票
13：过路过桥费发票
15：非税发票
16：全电发票
        :type Type: int
        :param Rect: 识别出的图片在混贴票据图片中的位置信息。与Angel结合可以得出原图位置，组成RotatedRect((X+0.5\*Width,Y+0.5\*Height), (Width, Height), Angle)，详情可参考OpenCV文档。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param Angle: 识别出的图片在混贴票据图片中的旋转角度。
        :type Angle: float
        :param SingleInvoiceInfos: 识别到的内容。
        :type SingleInvoiceInfos: list of SingleInvoiceInfo
        """
        self.Code = None
        self.Type = None
        self.Rect = None
        self.Angle = None
        self.SingleInvoiceInfos = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Angle = params.get("Angle")
        if params.get("SingleInvoiceInfos") is not None:
            self.SingleInvoiceInfos = []
            for item in params.get("SingleInvoiceInfos"):
                obj = SingleInvoiceInfo()
                obj._deserialize(item)
                self.SingleInvoiceInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceOCRRequest(AbstractModel):
    """MixedInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Types: 需要识别的票据类型列表，为空或不填表示识别全部类型。
0：出租车发票
1：定额发票
2：火车票
3：增值税发票
5：机票行程单
8：通用机打发票
9：汽车票
10：轮船票
11：增值税发票（卷票 ）
12：购车发票
13：过路过桥费发票
15：非税发票
16：全电发票
        :type Types: list of int
        :param ReturnOther: 是否识别其他类型发票，默认为Yes
Yes：识别其他类型发票
No：不识别其他类型发票
        :type ReturnOther: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Types = None
        self.ReturnOther = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Types = params.get("Types")
        self.ReturnOther = params.get("ReturnOther")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceOCRResponse(AbstractModel):
    """MixedInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param MixedInvoiceItems: 混贴票据识别结果，具体内容请点击左侧链接。
        :type MixedInvoiceItems: list of MixedInvoiceItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MixedInvoiceItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MixedInvoiceItems") is not None:
            self.MixedInvoiceItems = []
            for item in params.get("MixedInvoiceItems"):
                obj = MixedInvoiceItem()
                obj._deserialize(item)
                self.MixedInvoiceItems.append(obj)
        self.RequestId = params.get("RequestId")


class OnlineTaxiItineraryInfo(AbstractModel):
    """网约车行程单识别结果

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、 机打代码、 发票号码、 发动机号码、 合格证号、 机打号码、 价税合计(小写)、 销货单位名称、 身份证号码/组织机构代码、 购买方名称、 销售方纳税人识别号、 购买方纳税人识别号、主管税务机关、 主管税务机关代码、 开票日期、 不含税价(小写)、 吨位、增值税税率或征收率、 车辆识别代号/车架号码、 增值税税额、 厂牌型号、 省、 市、 发票消费类型、 销售方电话、 销售方账号、 产地、 进口证明书号、 车辆类型、 机器编号、备注、开票人、限乘人数、商检单号、销售方地址、销售方开户银行、价税合计、发票类型。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgCodeCertOCRRequest(AbstractModel):
    """OrgCodeCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgCodeCertOCRResponse(AbstractModel):
    """OrgCodeCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param OrgCode: 代码
        :type OrgCode: str
        :param Name: 机构名称
        :type Name: str
        :param Address: 地址
        :type Address: str
        :param ValidDate: 有效期
        :type ValidDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrgCode = None
        self.Name = None
        self.Address = None
        self.ValidDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgCode = params.get("OrgCode")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        self.ValidDate = params.get("ValidDate")
        self.RequestId = params.get("RequestId")


class PassInvoiceInfo(AbstractModel):
    """通行费发票信息

    """

    def __init__(self):
        r"""
        :param NumberPlate: 通行费车牌号
        :type NumberPlate: str
        :param Type: 通行费类型
        :type Type: str
        :param PassDateBegin: 通行日期起
        :type PassDateBegin: str
        :param PassDateEnd: 通行日期止
        :type PassDateEnd: str
        :param TaxClassifyCode: 税收分类编码
        :type TaxClassifyCode: str
        """
        self.NumberPlate = None
        self.Type = None
        self.PassDateBegin = None
        self.PassDateEnd = None
        self.TaxClassifyCode = None


    def _deserialize(self, params):
        self.NumberPlate = params.get("NumberPlate")
        self.Type = params.get("Type")
        self.PassDateBegin = params.get("PassDateBegin")
        self.PassDateEnd = params.get("PassDateEnd")
        self.TaxClassifyCode = params.get("TaxClassifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PassportOCRRequest(AbstractModel):
    """PassportOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param Type: 默认填写CN
支持中国大陆地区护照。
        :type Type: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PassportOCRResponse(AbstractModel):
    """PassportOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Country: 国家码
        :type Country: str
        :param PassportNo: 护照号
        :type PassportNo: str
        :param Sex: 性别
        :type Sex: str
        :param Nationality: 国籍
        :type Nationality: str
        :param BirthDate: 出生日期
        :type BirthDate: str
        :param BirthPlace: 出生地点
        :type BirthPlace: str
        :param IssueDate: 签发日期
        :type IssueDate: str
        :param IssuePlace: 签发地点
        :type IssuePlace: str
        :param ExpiryDate: 有效期
        :type ExpiryDate: str
        :param Signature: 持证人签名
        :type Signature: str
        :param CodeSet: 最下方第一行 MRZ Code 序列
        :type CodeSet: str
        :param CodeCrc: 最下方第二行 MRZ Code 序列
        :type CodeCrc: str
        :param Name: 姓名
        :type Name: str
        :param FamilyName: 姓
        :type FamilyName: str
        :param FirstName: 名
        :type FirstName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Country = None
        self.PassportNo = None
        self.Sex = None
        self.Nationality = None
        self.BirthDate = None
        self.BirthPlace = None
        self.IssueDate = None
        self.IssuePlace = None
        self.ExpiryDate = None
        self.Signature = None
        self.CodeSet = None
        self.CodeCrc = None
        self.Name = None
        self.FamilyName = None
        self.FirstName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Country = params.get("Country")
        self.PassportNo = params.get("PassportNo")
        self.Sex = params.get("Sex")
        self.Nationality = params.get("Nationality")
        self.BirthDate = params.get("BirthDate")
        self.BirthPlace = params.get("BirthPlace")
        self.IssueDate = params.get("IssueDate")
        self.IssuePlace = params.get("IssuePlace")
        self.ExpiryDate = params.get("ExpiryDate")
        self.Signature = params.get("Signature")
        self.CodeSet = params.get("CodeSet")
        self.CodeCrc = params.get("CodeCrc")
        self.Name = params.get("Name")
        self.FamilyName = params.get("FamilyName")
        self.FirstName = params.get("FirstName")
        self.RequestId = params.get("RequestId")


class PermitOCRRequest(AbstractModel):
    """PermitOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermitOCRResponse(AbstractModel):
    """PermitOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 姓名
        :type Name: str
        :param EnglishName: 英文姓名
        :type EnglishName: str
        :param Number: 证件号
        :type Number: str
        :param Sex: 性别
        :type Sex: str
        :param ValidDate: 有效期限
        :type ValidDate: str
        :param IssueAuthority: 签发机关
        :type IssueAuthority: str
        :param IssueAddress: 签发地点
        :type IssueAddress: str
        :param Birthday: 出生日期
        :type Birthday: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.EnglishName = None
        self.Number = None
        self.Sex = None
        self.ValidDate = None
        self.IssueAuthority = None
        self.IssueAddress = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EnglishName = params.get("EnglishName")
        self.Number = params.get("Number")
        self.Sex = params.get("Sex")
        self.ValidDate = params.get("ValidDate")
        self.IssueAuthority = params.get("IssueAuthority")
        self.IssueAddress = params.get("IssueAddress")
        self.Birthday = params.get("Birthday")
        self.RequestId = params.get("RequestId")


class Polygon(AbstractModel):
    """文本的坐标，以四个顶点坐标表示
    注意：此字段可能返回 null，表示取不到有效值

    """

    def __init__(self):
        r"""
        :param LeftTop: 左上顶点坐标
        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param RightTop: 右上顶点坐标
        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param RightBottom: 右下顶点坐标
        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param LeftBottom: 左下顶点坐标
        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        self.LeftTop = None
        self.RightTop = None
        self.RightBottom = None
        self.LeftBottom = None


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self.LeftTop = Coord()
            self.LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self.RightTop = Coord()
            self.RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self.RightBottom = Coord()
            self.RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self.LeftBottom = Coord()
            self.LeftBottom._deserialize(params.get("LeftBottom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductDataRecord(AbstractModel):
    """商品码信息

    """

    def __init__(self):
        r"""
        :param ProductName: 产品名称
        :type ProductName: str
        :param EnName: 产品名称(英文)
        :type EnName: str
        :param BrandName: 品牌名称
        :type BrandName: str
        :param Type: 规格型号
        :type Type: str
        :param Width: 宽度，单位毫米
        :type Width: str
        :param Height: 高度，单位毫米
        :type Height: str
        :param Depth: 深度，单位毫米
        :type Depth: str
        :param KeyWord: 关键字
        :type KeyWord: str
        :param Description: 简短描述
        :type Description: str
        :param ImageLink: 图片链接
        :type ImageLink: list of str
        :param ManufacturerName: 厂家名称
        :type ManufacturerName: str
        :param ManufacturerAddress: 厂家地址
        :type ManufacturerAddress: str
        :param FirmCode: 企业社会信用代码
        :type FirmCode: str
        :param CheckResult: 表示数据查询状态
checkResult	状态说明
1	 经查，该商品条码已在中国物品编码中心注册
2	经查，该厂商识别代码已在中国物品编码中心注册，但编码信息未按规定通报。
3	经查，该厂商识别代码已于xxxxx注销，请关注产品生产日期。
4	经查，该企业以及条码未经条码中心注册，属于违法使用
-1	经查，该商品条码被冒用
-2	经查，该厂商识别代码已在中国物品编码中心注册，但该产品已经下市
S001                未找到该厂商识别代码的注册信息。
S002		该厂商识别代码已经在GS1注册，但编码信息未通报
S003		该商品条码已在GS1通报
S004		该商品条码已注销
S005		数字不正确。GS1前缀（3位国家/地区代码）用于特殊用途。
E001		完整性失败：此GTIN的长度无效。
E002		完整性失败：校验位不正确。
E003		完整性失败：字符串包含字母数字字符。
E004		数字不正确。GS1前缀（3位国家/地区代码）不存在。
E005		数字不正确。GS1前缀（3位国家/地区代码）用于特殊用途。
E006		数字不正确。尚未分配该GS1公司前缀。
E008	        经查，该企业厂商识别代码以及条码尚未通报
        :type CheckResult: str
        :param CategoryCode: UNSPSC分类码
        :type CategoryCode: str
        """
        self.ProductName = None
        self.EnName = None
        self.BrandName = None
        self.Type = None
        self.Width = None
        self.Height = None
        self.Depth = None
        self.KeyWord = None
        self.Description = None
        self.ImageLink = None
        self.ManufacturerName = None
        self.ManufacturerAddress = None
        self.FirmCode = None
        self.CheckResult = None
        self.CategoryCode = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.EnName = params.get("EnName")
        self.BrandName = params.get("BrandName")
        self.Type = params.get("Type")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Depth = params.get("Depth")
        self.KeyWord = params.get("KeyWord")
        self.Description = params.get("Description")
        self.ImageLink = params.get("ImageLink")
        self.ManufacturerName = params.get("ManufacturerName")
        self.ManufacturerAddress = params.get("ManufacturerAddress")
        self.FirmCode = params.get("FirmCode")
        self.CheckResult = params.get("CheckResult")
        self.CategoryCode = params.get("CategoryCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PropOwnerCertOCRRequest(AbstractModel):
    """PropOwnerCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PropOwnerCertOCRResponse(AbstractModel):
    """PropOwnerCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Owner: 房地产权利人
        :type Owner: str
        :param Possession: 共有情况
        :type Possession: str
        :param RegisterTime: 登记时间
        :type RegisterTime: str
        :param Purpose: 规划用途
        :type Purpose: str
        :param Nature: 房屋性质
        :type Nature: str
        :param Location: 房地坐落
        :type Location: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Owner = None
        self.Possession = None
        self.RegisterTime = None
        self.Purpose = None
        self.Nature = None
        self.Location = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Owner = params.get("Owner")
        self.Possession = params.get("Possession")
        self.RegisterTime = params.get("RegisterTime")
        self.Purpose = params.get("Purpose")
        self.Nature = params.get("Nature")
        self.Location = params.get("Location")
        self.RequestId = params.get("RequestId")


class QrcodeImgSize(AbstractModel):
    """图片大小

    """

    def __init__(self):
        r"""
        :param Wide: 宽
        :type Wide: int
        :param High: 高
        :type High: int
        """
        self.Wide = None
        self.High = None


    def _deserialize(self, params):
        self.Wide = params.get("Wide")
        self.High = params.get("High")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QrcodeOCRRequest(AbstractModel):
    """QrcodeOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，支持PNG、JPG、JPEG格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，支持PNG、JPG、JPEG格式。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QrcodeOCRResponse(AbstractModel):
    """QrcodeOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param CodeResults: 二维码/条形码识别结果信息，具体内容请点击左侧链接。
        :type CodeResults: list of QrcodeResultsInfo
        :param ImgSize: 图片大小，具体内容请点击左侧链接。
        :type ImgSize: :class:`tencentcloud.ocr.v20181119.models.QrcodeImgSize`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CodeResults = None
        self.ImgSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CodeResults") is not None:
            self.CodeResults = []
            for item in params.get("CodeResults"):
                obj = QrcodeResultsInfo()
                obj._deserialize(item)
                self.CodeResults.append(obj)
        if params.get("ImgSize") is not None:
            self.ImgSize = QrcodeImgSize()
            self.ImgSize._deserialize(params.get("ImgSize"))
        self.RequestId = params.get("RequestId")


class QrcodePositionObj(AbstractModel):
    """二维码/条形码坐标信息

    """

    def __init__(self):
        r"""
        :param LeftTop: 左上顶点坐标（如果是条形码，X和Y都为-1）
        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param RightTop: 右上顶点坐标（如果是条形码，X和Y都为-1）
        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param RightBottom: 右下顶点坐标（如果是条形码，X和Y都为-1）
        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param LeftBottom: 左下顶点坐标（如果是条形码，X和Y都为-1）
        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        self.LeftTop = None
        self.RightTop = None
        self.RightBottom = None
        self.LeftBottom = None


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self.LeftTop = Coord()
            self.LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self.RightTop = Coord()
            self.RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self.RightBottom = Coord()
            self.RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self.LeftBottom = Coord()
            self.LeftBottom._deserialize(params.get("LeftBottom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QrcodeResultsInfo(AbstractModel):
    """二维码/条形码识别结果信息

    """

    def __init__(self):
        r"""
        :param TypeName: 类型（二维码、条形码）
        :type TypeName: str
        :param Url: 二维码/条形码包含的地址
        :type Url: str
        :param Position: 二维码/条形码坐标（二维码会返回位置坐标，条形码暂不返回位置坐标，因此默认X和Y返回值均为-1）
        :type Position: :class:`tencentcloud.ocr.v20181119.models.QrcodePositionObj`
        """
        self.TypeName = None
        self.Url = None
        self.Position = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.Url = params.get("Url")
        if params.get("Position") is not None:
            self.Position = QrcodePositionObj()
            self.Position._deserialize(params.get("Position"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBarCodeRequest(AbstractModel):
    """QueryBarCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param BarCode: 条形码
        :type BarCode: str
        """
        self.BarCode = None


    def _deserialize(self, params):
        self.BarCode = params.get("BarCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBarCodeResponse(AbstractModel):
    """QueryBarCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param BarCode: 条码
        :type BarCode: str
        :param ProductDataRecords: 条码信息数组
        :type ProductDataRecords: list of ProductDataRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BarCode = None
        self.ProductDataRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BarCode = params.get("BarCode")
        if params.get("ProductDataRecords") is not None:
            self.ProductDataRecords = []
            for item in params.get("ProductDataRecords"):
                obj = ProductDataRecord()
                obj._deserialize(item)
                self.ProductDataRecords.append(obj)
        self.RequestId = params.get("RequestId")


class QuestionBlockObj(AbstractModel):
    """数学试题识别结构化对象

    """

    def __init__(self):
        r"""
        :param QuestionArr: 数学试题识别结构化信息数组
        :type QuestionArr: list of QuestionObj
        :param QuestionBboxCoord: 题目主体区域检测框在图片中的像素坐标
        :type QuestionBboxCoord: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.QuestionArr = None
        self.QuestionBboxCoord = None


    def _deserialize(self, params):
        if params.get("QuestionArr") is not None:
            self.QuestionArr = []
            for item in params.get("QuestionArr"):
                obj = QuestionObj()
                obj._deserialize(item)
                self.QuestionArr.append(obj)
        if params.get("QuestionBboxCoord") is not None:
            self.QuestionBboxCoord = Rect()
            self.QuestionBboxCoord._deserialize(params.get("QuestionBboxCoord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuestionObj(AbstractModel):
    """试题识别结构化信息

    """

    def __init__(self):
        r"""
        :param QuestionTextNo: 题号
        :type QuestionTextNo: str
        :param QuestionTextType: 题型：
1: "选择题"
2: "填空题"
3: "解答题"
        :type QuestionTextType: int
        :param QuestionText: 题干
        :type QuestionText: str
        :param QuestionOptions: 选择题选项，包含1个或多个option
        :type QuestionOptions: str
        :param QuestionSubquestion: 所有子题的question属性
        :type QuestionSubquestion: str
        :param QuestionImageCoords: 示意图检测框在的图片中的像素坐标
        :type QuestionImageCoords: list of Rect
        """
        self.QuestionTextNo = None
        self.QuestionTextType = None
        self.QuestionText = None
        self.QuestionOptions = None
        self.QuestionSubquestion = None
        self.QuestionImageCoords = None


    def _deserialize(self, params):
        self.QuestionTextNo = params.get("QuestionTextNo")
        self.QuestionTextType = params.get("QuestionTextType")
        self.QuestionText = params.get("QuestionText")
        self.QuestionOptions = params.get("QuestionOptions")
        self.QuestionSubquestion = params.get("QuestionSubquestion")
        if params.get("QuestionImageCoords") is not None:
            self.QuestionImageCoords = []
            for item in params.get("QuestionImageCoords"):
                obj = Rect()
                obj._deserialize(item)
                self.QuestionImageCoords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInvoiceOCRRequest(AbstractModel):
    """QuotaInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInvoiceOCRResponse(AbstractModel):
    """QuotaInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvoiceNum: 发票号码
        :type InvoiceNum: str
        :param InvoiceCode: 发票代码
        :type InvoiceCode: str
        :param Rate: 大写金额
        :type Rate: str
        :param RateNum: 小写金额
        :type RateNum: str
        :param InvoiceType: 发票消费类型
        :type InvoiceType: str
        :param Province: 省
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param City: 市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param HasStamp: 是否有公司印章（1有 0无 空为识别不出）
注意：此字段可能返回 null，表示取不到有效值。
        :type HasStamp: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceNum = None
        self.InvoiceCode = None
        self.Rate = None
        self.RateNum = None
        self.InvoiceType = None
        self.Province = None
        self.City = None
        self.HasStamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvoiceNum = params.get("InvoiceNum")
        self.InvoiceCode = params.get("InvoiceCode")
        self.Rate = params.get("Rate")
        self.RateNum = params.get("RateNum")
        self.InvoiceType = params.get("InvoiceType")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.HasStamp = params.get("HasStamp")
        self.RequestId = params.get("RequestId")


class RecognizeContainerOCRRequest(AbstractModel):
    """RecognizeContainerOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeContainerOCRResponse(AbstractModel):
    """RecognizeContainerOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerId: 集装箱箱号
        :type ContainerId: str
        :param ContainerType: 集装箱类型
        :type ContainerType: str
        :param GrossKG: 集装箱总重量，单位：千克（KG）
        :type GrossKG: str
        :param GrossLB: 集装箱总重量，单位：磅（LB）
        :type GrossLB: str
        :param PayloadKG: 集装箱有效承重，单位：千克（KG）
        :type PayloadKG: str
        :param PayloadLB: 集装箱有效承重，单位：磅（LB）
        :type PayloadLB: str
        :param CapacityM3: 集装箱容量，单位：立方米
        :type CapacityM3: str
        :param CapacityFT3: 集装箱容量，单位：立英尺
        :type CapacityFT3: str
        :param Warn: 告警码
-9926	集装箱箱号不完整或者不清晰
-9927	集装箱类型不完整或者不清晰
        :type Warn: list of int
        :param TareKG: 集装箱自身重量，单位：千克（KG）
        :type TareKG: str
        :param TareLB: 集装箱自身重量，单位：磅（LB）
        :type TareLB: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContainerId = None
        self.ContainerType = None
        self.GrossKG = None
        self.GrossLB = None
        self.PayloadKG = None
        self.PayloadLB = None
        self.CapacityM3 = None
        self.CapacityFT3 = None
        self.Warn = None
        self.TareKG = None
        self.TareLB = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ContainerId = params.get("ContainerId")
        self.ContainerType = params.get("ContainerType")
        self.GrossKG = params.get("GrossKG")
        self.GrossLB = params.get("GrossLB")
        self.PayloadKG = params.get("PayloadKG")
        self.PayloadLB = params.get("PayloadLB")
        self.CapacityM3 = params.get("CapacityM3")
        self.CapacityFT3 = params.get("CapacityFT3")
        self.Warn = params.get("Warn")
        self.TareKG = params.get("TareKG")
        self.TareLB = params.get("TareLB")
        self.RequestId = params.get("RequestId")


class RecognizeHealthCodeOCRRequest(AbstractModel):
    """RecognizeHealthCodeOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Type: 需要识别的健康码类型列表，为空或不填表示默认为自动识别。
0:自动识别
        :type Type: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeHealthCodeOCRResponse(AbstractModel):
    """RecognizeHealthCodeOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 持码人姓名，如：王*（允许返回空值）
        :type Name: str
        :param IDNumber: 持码人身份证号，如：11**************01（允许返回空值）
        :type IDNumber: str
        :param Time: 健康码更新时间（允许返回空值）
        :type Time: str
        :param Color: 健康码颜色：绿色、黄色、红色（允许返回空值）
        :type Color: str
        :param TestingInterval: 核酸检测间隔时长（允许返回空值）
        :type TestingInterval: str
        :param TestingResult: 核酸检测结果：阴性、阳性、暂无核酸检测记录（允许返回空值）
        :type TestingResult: str
        :param TestingTime: 核酸检测时间（允许返回空值）
        :type TestingTime: str
        :param Vaccination: 疫苗接种信息，返回接种针数或接种情况（允许返回空值）
        :type Vaccination: str
        :param SpotName: 场所名称（允许返回空值）
        :type SpotName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.IDNumber = None
        self.Time = None
        self.Color = None
        self.TestingInterval = None
        self.TestingResult = None
        self.TestingTime = None
        self.Vaccination = None
        self.SpotName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IDNumber = params.get("IDNumber")
        self.Time = params.get("Time")
        self.Color = params.get("Color")
        self.TestingInterval = params.get("TestingInterval")
        self.TestingResult = params.get("TestingResult")
        self.TestingTime = params.get("TestingTime")
        self.Vaccination = params.get("Vaccination")
        self.SpotName = params.get("SpotName")
        self.RequestId = params.get("RequestId")


class RecognizeIndonesiaIDCardOCRRequest(AbstractModel):
    """RecognizeIndonesiaIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param Scene: 场景参数，默认值为V1
可选值：
V1
V2
        :type Scene: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnHeadImage = None
        self.Scene = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeIndonesiaIDCardOCRResponse(AbstractModel):
    """RecognizeIndonesiaIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param NIK: 证件号码
        :type NIK: str
        :param Nama: 姓名
        :type Nama: str
        :param TempatTglLahir: 出生地/出生时间
        :type TempatTglLahir: str
        :param JenisKelamin: 性别
        :type JenisKelamin: str
        :param GolDarah: 血型
        :type GolDarah: str
        :param Alamat: 地址
        :type Alamat: str
        :param RTRW: 街道
        :type RTRW: str
        :param KelDesa: 村
        :type KelDesa: str
        :param Kecamatan: 地区
        :type Kecamatan: str
        :param Agama: 宗教信仰
        :type Agama: str
        :param StatusPerkawinan: 婚姻状况
        :type StatusPerkawinan: str
        :param Perkerjaan: 职业
        :type Perkerjaan: str
        :param KewargaNegaraan: 国籍
        :type KewargaNegaraan: str
        :param BerlakuHingga: 身份证有效期限
        :type BerlakuHingga: str
        :param IssuedDate: 发证日期
        :type IssuedDate: str
        :param Photo: 人像截图
        :type Photo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NIK = None
        self.Nama = None
        self.TempatTglLahir = None
        self.JenisKelamin = None
        self.GolDarah = None
        self.Alamat = None
        self.RTRW = None
        self.KelDesa = None
        self.Kecamatan = None
        self.Agama = None
        self.StatusPerkawinan = None
        self.Perkerjaan = None
        self.KewargaNegaraan = None
        self.BerlakuHingga = None
        self.IssuedDate = None
        self.Photo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NIK = params.get("NIK")
        self.Nama = params.get("Nama")
        self.TempatTglLahir = params.get("TempatTglLahir")
        self.JenisKelamin = params.get("JenisKelamin")
        self.GolDarah = params.get("GolDarah")
        self.Alamat = params.get("Alamat")
        self.RTRW = params.get("RTRW")
        self.KelDesa = params.get("KelDesa")
        self.Kecamatan = params.get("Kecamatan")
        self.Agama = params.get("Agama")
        self.StatusPerkawinan = params.get("StatusPerkawinan")
        self.Perkerjaan = params.get("Perkerjaan")
        self.KewargaNegaraan = params.get("KewargaNegaraan")
        self.BerlakuHingga = params.get("BerlakuHingga")
        self.IssuedDate = params.get("IssuedDate")
        self.Photo = params.get("Photo")
        self.RequestId = params.get("RequestId")


class RecognizeMedicalInvoiceOCRRequest(AbstractModel):
    """RecognizeMedicalInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的Base64 值。
支持的文件格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载文件经Base64编码后不超过 7M。文件下载时间不超过 3 秒。
输入参数 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的Url 地址。
支持的文件格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载文件经 Base64 编码后不超过 7M。文件下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param ReturnVertex: 是否需要返回识别出的文本行在原图上的四点坐标，默认不返回
        :type ReturnVertex: bool
        :param ReturnCoord: 是否需要返回识别出的文本行在旋转纠正之后的图像中的四点坐标，默认不返回
        :type ReturnCoord: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnVertex = None
        self.ReturnCoord = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnVertex = params.get("ReturnVertex")
        self.ReturnCoord = params.get("ReturnCoord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMedicalInvoiceOCRResponse(AbstractModel):
    """RecognizeMedicalInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param MedicalInvoiceInfos: 识别出的字段信息
        :type MedicalInvoiceInfos: list of MedicalInvoiceInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MedicalInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MedicalInvoiceInfos") is not None:
            self.MedicalInvoiceInfos = []
            for item in params.get("MedicalInvoiceInfos"):
                obj = MedicalInvoiceInfo()
                obj._deserialize(item)
                self.MedicalInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class RecognizeOnlineTaxiItineraryOCRRequest(AbstractModel):
    """RecognizeOnlineTaxiItineraryOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.IsPdf = None
        self.PdfPageNumber = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeOnlineTaxiItineraryOCRResponse(AbstractModel):
    """RecognizeOnlineTaxiItineraryOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param OnlineTaxiItineraryInfos: 网约车行程单识别结果，具体内容请点击左侧链接。
        :type OnlineTaxiItineraryInfos: list of OnlineTaxiItineraryInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OnlineTaxiItineraryInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OnlineTaxiItineraryInfos") is not None:
            self.OnlineTaxiItineraryInfos = []
            for item in params.get("OnlineTaxiItineraryInfos"):
                obj = OnlineTaxiItineraryInfo()
                obj._deserialize(item)
                self.OnlineTaxiItineraryInfos.append(obj)
        self.RequestId = params.get("RequestId")


class RecognizePhilippinesDrivingLicenseOCRRequest(AbstractModel):
    """RecognizePhilippinesDrivingLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ReturnHeadImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesDrivingLicenseOCRResponse(AbstractModel):
    """RecognizePhilippinesDrivingLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param HeadPortrait: 人像照片Base64后的结果
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Name: 姓名
        :type Name: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LastName: 姓氏
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param FirstName: 首姓名
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param MiddleName: 中间姓名
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Nationality: 国籍
        :type Nationality: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Sex: 性别
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Address: 地址
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LicenseNo: 证号
        :type LicenseNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param ExpiresDate: 有效期
        :type ExpiresDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param AgencyCode: 机构代码
        :type AgencyCode: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Birthday: 出生日期
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HeadPortrait = None
        self.Name = None
        self.LastName = None
        self.FirstName = None
        self.MiddleName = None
        self.Nationality = None
        self.Sex = None
        self.Address = None
        self.LicenseNo = None
        self.ExpiresDate = None
        self.AgencyCode = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self.HeadPortrait = TextDetectionResult()
            self.HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("Name") is not None:
            self.Name = TextDetectionResult()
            self.Name._deserialize(params.get("Name"))
        if params.get("LastName") is not None:
            self.LastName = TextDetectionResult()
            self.LastName._deserialize(params.get("LastName"))
        if params.get("FirstName") is not None:
            self.FirstName = TextDetectionResult()
            self.FirstName._deserialize(params.get("FirstName"))
        if params.get("MiddleName") is not None:
            self.MiddleName = TextDetectionResult()
            self.MiddleName._deserialize(params.get("MiddleName"))
        if params.get("Nationality") is not None:
            self.Nationality = TextDetectionResult()
            self.Nationality._deserialize(params.get("Nationality"))
        if params.get("Sex") is not None:
            self.Sex = TextDetectionResult()
            self.Sex._deserialize(params.get("Sex"))
        if params.get("Address") is not None:
            self.Address = TextDetectionResult()
            self.Address._deserialize(params.get("Address"))
        if params.get("LicenseNo") is not None:
            self.LicenseNo = TextDetectionResult()
            self.LicenseNo._deserialize(params.get("LicenseNo"))
        if params.get("ExpiresDate") is not None:
            self.ExpiresDate = TextDetectionResult()
            self.ExpiresDate._deserialize(params.get("ExpiresDate"))
        if params.get("AgencyCode") is not None:
            self.AgencyCode = TextDetectionResult()
            self.AgencyCode._deserialize(params.get("AgencyCode"))
        if params.get("Birthday") is not None:
            self.Birthday = TextDetectionResult()
            self.Birthday._deserialize(params.get("Birthday"))
        self.RequestId = params.get("RequestId")


class RecognizePhilippinesVoteIDOCRRequest(AbstractModel):
    """RecognizePhilippinesVoteIDOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ReturnHeadImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ReturnHeadImage = params.get("ReturnHeadImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesVoteIDOCRResponse(AbstractModel):
    """RecognizePhilippinesVoteIDOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param HeadPortrait: 人像照片Base64后的结果
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param VIN: 菲律宾VoteID的VIN
        :type VIN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param FirstName: 姓名
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param LastName: 姓氏
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Birthday: 出生日期
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param CivilStatus: 婚姻状况
        :type CivilStatus: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Citizenship: 国籍
        :type Citizenship: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param Address: 地址
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param PrecinctNo: 地区
        :type PrecinctNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HeadPortrait = None
        self.VIN = None
        self.FirstName = None
        self.LastName = None
        self.Birthday = None
        self.CivilStatus = None
        self.Citizenship = None
        self.Address = None
        self.PrecinctNo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self.HeadPortrait = TextDetectionResult()
            self.HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("VIN") is not None:
            self.VIN = TextDetectionResult()
            self.VIN._deserialize(params.get("VIN"))
        if params.get("FirstName") is not None:
            self.FirstName = TextDetectionResult()
            self.FirstName._deserialize(params.get("FirstName"))
        if params.get("LastName") is not None:
            self.LastName = TextDetectionResult()
            self.LastName._deserialize(params.get("LastName"))
        if params.get("Birthday") is not None:
            self.Birthday = TextDetectionResult()
            self.Birthday._deserialize(params.get("Birthday"))
        if params.get("CivilStatus") is not None:
            self.CivilStatus = TextDetectionResult()
            self.CivilStatus._deserialize(params.get("CivilStatus"))
        if params.get("Citizenship") is not None:
            self.Citizenship = TextDetectionResult()
            self.Citizenship._deserialize(params.get("Citizenship"))
        if params.get("Address") is not None:
            self.Address = TextDetectionResult()
            self.Address._deserialize(params.get("Address"))
        if params.get("PrecinctNo") is not None:
            self.PrecinctNo = TextDetectionResult()
            self.PrecinctNo._deserialize(params.get("PrecinctNo"))
        self.RequestId = params.get("RequestId")


class RecognizeTableOCRRequest(AbstractModel):
    """RecognizeTableOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片/PDF的 Base64 值。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片/PDF的 Url 地址。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param TableLanguage: 语言，zh：中英文（默认）jap：日文
        :type TableLanguage: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.IsPdf = None
        self.PdfPageNumber = None
        self.TableLanguage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        self.TableLanguage = params.get("TableLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTableOCRResponse(AbstractModel):
    """RecognizeTableOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TableDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TableDetections: list of TableDetectInfo
        :param Data: Base64 编码后的 Excel 数据。
        :type Data: str
        :param PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0
        :type PdfPageSize: int
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，统一以逆时针方向旋转，逆时针为负，角度范围为-360°至0°。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TableDetections = None
        self.Data = None
        self.PdfPageSize = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TableDetections") is not None:
            self.TableDetections = []
            for item in params.get("TableDetections"):
                obj = TableDetectInfo()
                obj._deserialize(item)
                self.TableDetections.append(obj)
        self.Data = params.get("Data")
        self.PdfPageSize = params.get("PdfPageSize")
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class RecognizeThaiIDCardOCRRequest(AbstractModel):
    """RecognizeThaiIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeThaiIDCardOCRResponse(AbstractModel):
    """RecognizeThaiIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 身份证号码
        :type ID: str
        :param ThaiName: 泰文姓名
        :type ThaiName: str
        :param EnFirstName: 英文姓名
        :type EnFirstName: str
        :param Address: 地址
        :type Address: str
        :param Birthday: 出生日期
        :type Birthday: str
        :param IssueDate: 首次领用日期
        :type IssueDate: str
        :param ExpirationDate: 签发日期
        :type ExpirationDate: str
        :param EnLastName: 英文姓名
        :type EnLastName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.ThaiName = None
        self.EnFirstName = None
        self.Address = None
        self.Birthday = None
        self.IssueDate = None
        self.ExpirationDate = None
        self.EnLastName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ThaiName = params.get("ThaiName")
        self.EnFirstName = params.get("EnFirstName")
        self.Address = params.get("Address")
        self.Birthday = params.get("Birthday")
        self.IssueDate = params.get("IssueDate")
        self.ExpirationDate = params.get("ExpirationDate")
        self.EnLastName = params.get("EnLastName")
        self.RequestId = params.get("RequestId")


class RecognizeTravelCardOCRRequest(AbstractModel):
    """RecognizeTravelCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTravelCardOCRResponse(AbstractModel):
    """RecognizeTravelCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Time: 行程卡更新时间，格式为：XXXX.XX.XX XX:XX:XX
        :type Time: str
        :param Color: 行程卡颜色：绿色、黄色、红色
        :type Color: str
        :param ReachedCity: 7天内到达或途经的城市（自2022年7月8日起，通信行程卡查询结果的覆盖时间范围由“14天”调整为“7天”）
        :type ReachedCity: list of str
        :param RiskArea: 7天内到达或途径存在中高风险地区的城市（自2022年6月29日起，通信行程卡取消“星号”标记，改字段将返回空值）
        :type RiskArea: list of str
        :param Telephone: 电话号码
        :type Telephone: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Time = None
        self.Color = None
        self.ReachedCity = None
        self.RiskArea = None
        self.Telephone = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Color = params.get("Color")
        self.ReachedCity = params.get("ReachedCity")
        self.RiskArea = params.get("RiskArea")
        self.Telephone = params.get("Telephone")
        self.RequestId = params.get("RequestId")


class Rect(AbstractModel):
    """矩形坐标

    """

    def __init__(self):
        r"""
        :param X: 左上角x
        :type X: int
        :param Y: 左上角y
        :type Y: int
        :param Width: 宽度
        :type Width: int
        :param Height: 高度
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
        


class ResidenceBookletOCRRequest(AbstractModel):
    """ResidenceBookletOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResidenceBookletOCRResponse(AbstractModel):
    """ResidenceBookletOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param HouseholdNumber: 户号
        :type HouseholdNumber: str
        :param Name: 姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param BirthPlace: 出生地
        :type BirthPlace: str
        :param Nation: 民族
        :type Nation: str
        :param NativePlace: 籍贯
        :type NativePlace: str
        :param BirthDate: 出生日期
        :type BirthDate: str
        :param IdCardNumber: 公民身份证件编号
        :type IdCardNumber: str
        :param EducationDegree: 文化程度
        :type EducationDegree: str
        :param ServicePlace: 服务处所
        :type ServicePlace: str
        :param Household: 户别
        :type Household: str
        :param Address: 住址
        :type Address: str
        :param Signature: 承办人签章文字
        :type Signature: str
        :param IssueDate: 签发日期
        :type IssueDate: str
        :param HomePageNumber: 户主页编号
        :type HomePageNumber: str
        :param HouseholderName: 户主姓名
        :type HouseholderName: str
        :param Relationship: 户主或与户主关系
        :type Relationship: str
        :param OtherAddresses: 本市（县）其他住址
        :type OtherAddresses: str
        :param ReligiousBelief: 宗教信仰
        :type ReligiousBelief: str
        :param Height: 身高
        :type Height: str
        :param BloodType: 血型
        :type BloodType: str
        :param MaritalStatus: 婚姻状况
        :type MaritalStatus: str
        :param VeteranStatus: 兵役状况
        :type VeteranStatus: str
        :param Profession: 职业
        :type Profession: str
        :param MoveToCityInformation: 何时由何地迁来本市(县)
        :type MoveToCityInformation: str
        :param MoveToSiteInformation: 何时由何地迁来本址
        :type MoveToSiteInformation: str
        :param RegistrationDate: 登记日期
        :type RegistrationDate: str
        :param FormerName: 曾用名
        :type FormerName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HouseholdNumber = None
        self.Name = None
        self.Sex = None
        self.BirthPlace = None
        self.Nation = None
        self.NativePlace = None
        self.BirthDate = None
        self.IdCardNumber = None
        self.EducationDegree = None
        self.ServicePlace = None
        self.Household = None
        self.Address = None
        self.Signature = None
        self.IssueDate = None
        self.HomePageNumber = None
        self.HouseholderName = None
        self.Relationship = None
        self.OtherAddresses = None
        self.ReligiousBelief = None
        self.Height = None
        self.BloodType = None
        self.MaritalStatus = None
        self.VeteranStatus = None
        self.Profession = None
        self.MoveToCityInformation = None
        self.MoveToSiteInformation = None
        self.RegistrationDate = None
        self.FormerName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HouseholdNumber = params.get("HouseholdNumber")
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.BirthPlace = params.get("BirthPlace")
        self.Nation = params.get("Nation")
        self.NativePlace = params.get("NativePlace")
        self.BirthDate = params.get("BirthDate")
        self.IdCardNumber = params.get("IdCardNumber")
        self.EducationDegree = params.get("EducationDegree")
        self.ServicePlace = params.get("ServicePlace")
        self.Household = params.get("Household")
        self.Address = params.get("Address")
        self.Signature = params.get("Signature")
        self.IssueDate = params.get("IssueDate")
        self.HomePageNumber = params.get("HomePageNumber")
        self.HouseholderName = params.get("HouseholderName")
        self.Relationship = params.get("Relationship")
        self.OtherAddresses = params.get("OtherAddresses")
        self.ReligiousBelief = params.get("ReligiousBelief")
        self.Height = params.get("Height")
        self.BloodType = params.get("BloodType")
        self.MaritalStatus = params.get("MaritalStatus")
        self.VeteranStatus = params.get("VeteranStatus")
        self.Profession = params.get("Profession")
        self.MoveToCityInformation = params.get("MoveToCityInformation")
        self.MoveToSiteInformation = params.get("MoveToSiteInformation")
        self.RegistrationDate = params.get("RegistrationDate")
        self.FormerName = params.get("FormerName")
        self.RequestId = params.get("RequestId")


class RideHailingDriverLicenseOCRRequest(AbstractModel):
    """RideHailingDriverLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RideHailingDriverLicenseOCRResponse(AbstractModel):
    """RideHailingDriverLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 姓名
        :type Name: str
        :param LicenseNumber: 证号，对应网约车驾驶证字段：证号/从业资格证号/驾驶员证号/身份证号
        :type LicenseNumber: str
        :param StartDate: 有效起始日期
        :type StartDate: str
        :param EndDate: 有效期截止时间，对应网约车驾驶证字段：有效期至/营运期限止
        :type EndDate: str
        :param ReleaseDate: 初始发证日期，对应网约车驾驶证字段：初始领证日期/发证日期
        :type ReleaseDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.LicenseNumber = None
        self.StartDate = None
        self.EndDate = None
        self.ReleaseDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.LicenseNumber = params.get("LicenseNumber")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReleaseDate = params.get("ReleaseDate")
        self.RequestId = params.get("RequestId")


class RideHailingTransportLicenseOCRRequest(AbstractModel):
    """RideHailingTransportLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RideHailingTransportLicenseOCRResponse(AbstractModel):
    """RideHailingTransportLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param OperationLicenseNumber: 交运管许可字号。
        :type OperationLicenseNumber: str
        :param VehicleOwner: 车辆所有人，对应网约车运输证字段：车辆所有人/车主名称/业户名称。
        :type VehicleOwner: str
        :param VehicleNumber: 车牌号码，对应网约车运输证字段：车牌号码/车辆号牌。
        :type VehicleNumber: str
        :param StartDate: 有效起始日期。
        :type StartDate: str
        :param EndDate: 有效期截止时间，对应网约车运输证字段：有效期至/营运期限止。
        :type EndDate: str
        :param ReleaseDate: 初始发证日期，对应网约车运输证字段：初始领证日期/发证日期。
        :type ReleaseDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OperationLicenseNumber = None
        self.VehicleOwner = None
        self.VehicleNumber = None
        self.StartDate = None
        self.EndDate = None
        self.ReleaseDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OperationLicenseNumber = params.get("OperationLicenseNumber")
        self.VehicleOwner = params.get("VehicleOwner")
        self.VehicleNumber = params.get("VehicleNumber")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReleaseDate = params.get("ReleaseDate")
        self.RequestId = params.get("RequestId")


class SealInfo(AbstractModel):
    """印章信息

    """

    def __init__(self):
        r"""
        :param SealBody: 印章主体内容
        :type SealBody: str
        :param Location: 印章坐标
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param OtherTexts: 印章其它文本内容
        :type OtherTexts: list of str
        """
        self.SealBody = None
        self.Location = None
        self.OtherTexts = None


    def _deserialize(self, params):
        self.SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self.Location = Rect()
            self.Location._deserialize(params.get("Location"))
        self.OtherTexts = params.get("OtherTexts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SealOCRRequest(AbstractModel):
    """SealOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SealOCRResponse(AbstractModel):
    """SealOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param SealBody: 印章内容
        :type SealBody: str
        :param Location: 印章坐标
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param OtherTexts: 其它文本内容
        :type OtherTexts: list of str
        :param SealInfos: 全部印章信息
        :type SealInfos: list of SealInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SealBody = None
        self.Location = None
        self.OtherTexts = None
        self.SealInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self.Location = Rect()
            self.Location._deserialize(params.get("Location"))
        self.OtherTexts = params.get("OtherTexts")
        if params.get("SealInfos") is not None:
            self.SealInfos = []
            for item in params.get("SealInfos"):
                obj = SealInfo()
                obj._deserialize(item)
                self.SealInfos.append(obj)
        self.RequestId = params.get("RequestId")


class ShipInvoiceInfo(AbstractModel):
    """轮船票字段信息

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、发票号码、日期、票价、始发地、目的地、姓名、时间、发票消费类型、省、市、币种。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipInvoiceOCRRequest(AbstractModel):
    """ShipInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipInvoiceOCRResponse(AbstractModel):
    """ShipInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param ShipInvoiceInfos: 轮船票识别结果，具体内容请点击左侧链接。
        :type ShipInvoiceInfos: list of ShipInvoiceInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ShipInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ShipInvoiceInfos") is not None:
            self.ShipInvoiceInfos = []
            for item in params.get("ShipInvoiceInfos"):
                obj = ShipInvoiceInfo()
                obj._deserialize(item)
                self.ShipInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class SingleInvoiceInfo(AbstractModel):
    """混贴票据中单张发票的内容

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        :param Row: 字段属于第几行，用于相同字段的排版，如发票明细表格项目，普通字段使用默认值为-1，表示无列排版。
        :type Row: int
        """
        self.Name = None
        self.Value = None
        self.Row = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Row = params.get("Row")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRRequest(AbstractModel):
    """SmartStructuralOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ItemNames: 自定义结构化功能需返回的字段名称，例：
若客户只想返回姓名、性别两个字段的识别结果，则输入
ItemNames=["姓名","性别"]
        :type ItemNames: list of str
        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param ReturnFullText: 是否开启全文字段识别，默认值为false，开启后可返回全文字段识别结果。
        :type ReturnFullText: bool
        """
        self.ImageUrl = None
        self.ImageBase64 = None
        self.ItemNames = None
        self.IsPdf = None
        self.PdfPageNumber = None
        self.ReturnFullText = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.ItemNames = params.get("ItemNames")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        self.ReturnFullText = params.get("ReturnFullText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRResponse(AbstractModel):
    """SmartStructuralOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Angle: 图片旋转角度(角度制)，文本的水平方向
为 0；顺时针为正，逆时针为负
        :type Angle: float
        :param StructuralItems: 识别信息
        :type StructuralItems: list of StructuralItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Angle = None
        self.StructuralItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Angle = params.get("Angle")
        if params.get("StructuralItems") is not None:
            self.StructuralItems = []
            for item in params.get("StructuralItems"):
                obj = StructuralItem()
                obj._deserialize(item)
                self.StructuralItems.append(obj)
        self.RequestId = params.get("RequestId")


class StructuralItem(AbstractModel):
    """智能结构化识别

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)。
        :type Name: str
        :param Value: 识别出的字段名称对应的值。
        :type Value: str
        :param Confidence: 置信度 0 ~100。
        :type Confidence: int
        :param ItemCoord: 文本行在旋转纠正之后的图像中的像素
坐标。
        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        self.Name = None
        self.Value = None
        self.Confidence = None
        self.ItemCoord = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Confidence = params.get("Confidence")
        if params.get("ItemCoord") is not None:
            self.ItemCoord = ItemCoord()
            self.ItemCoord._deserialize(params.get("ItemCoord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableCell(AbstractModel):
    """单元格数据

    """

    def __init__(self):
        r"""
        :param ColTl: 单元格左上角的列索引
        :type ColTl: int
        :param RowTl: 单元格左上角的行索引
        :type RowTl: int
        :param ColBr: 单元格右下角的列索引
        :type ColBr: int
        :param RowBr: 单元格右下角的行索引
        :type RowBr: int
        :param Text: 单元格内识别出的字符串文本，若文本存在多行，以换行符"\n"隔开
        :type Text: str
        :param Type: 单元格类型
        :type Type: str
        :param Confidence: 单元格置信度
        :type Confidence: float
        :param Polygon: 单元格在图像中的四点坐标
        :type Polygon: list of Coord
        :param AdvancedInfo: 此字段为扩展字段
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedInfo: str
        :param Contents: 单元格文本属性
        :type Contents: list of CellContent
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
        self.Contents = None


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
        if params.get("Contents") is not None:
            self.Contents = []
            for item in params.get("Contents"):
                obj = CellContent()
                obj._deserialize(item)
                self.Contents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableDetectInfo(AbstractModel):
    """表格内容检测

    """

    def __init__(self):
        r"""
        :param Cells: 单元格内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Cells: list of TableCell
        :param Titles: 表格标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Titles: list of TableTitle
        :param Type: 图像中的文本块类型，0 为非表格文本，
1 为有线表格，2 为无线表格
（接口暂不支持日文无线表格识别，若传入日文无线表格，返回0）
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param TableCoordPoint: 表格主体四个顶点坐标（依次为左上角，
右上角，右下角，左下角）
注意：此字段可能返回 null，表示取不到有效值。
        :type TableCoordPoint: list of Coord
        """
        self.Cells = None
        self.Titles = None
        self.Type = None
        self.TableCoordPoint = None


    def _deserialize(self, params):
        if params.get("Cells") is not None:
            self.Cells = []
            for item in params.get("Cells"):
                obj = TableCell()
                obj._deserialize(item)
                self.Cells.append(obj)
        if params.get("Titles") is not None:
            self.Titles = []
            for item in params.get("Titles"):
                obj = TableTitle()
                obj._deserialize(item)
                self.Titles.append(obj)
        self.Type = params.get("Type")
        if params.get("TableCoordPoint") is not None:
            self.TableCoordPoint = []
            for item in params.get("TableCoordPoint"):
                obj = Coord()
                obj._deserialize(item)
                self.TableCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableOCRRequest(AbstractModel):
    """TableOCR请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableOCRResponse(AbstractModel):
    """TableOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接
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


class TableTitle(AbstractModel):
    """表格标题

    """

    def __init__(self):
        r"""
        :param Text: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaxiInvoiceOCRRequest(AbstractModel):
    """TaxiInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaxiInvoiceOCRResponse(AbstractModel):
    """TaxiInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvoiceNum: 发票代码
        :type InvoiceNum: str
        :param InvoiceCode: 发票号码
        :type InvoiceCode: str
        :param Date: 日期
        :type Date: str
        :param Fare: 金额
        :type Fare: str
        :param GetOnTime: 上车时间
        :type GetOnTime: str
        :param GetOffTime: 下车时间
        :type GetOffTime: str
        :param Distance: 里程
        :type Distance: str
        :param Location: 发票所在地
        :type Location: str
        :param PlateNumber: 车牌号
        :type PlateNumber: str
        :param InvoiceType: 发票消费类型
        :type InvoiceType: str
        :param Province: 省
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param City: 市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceNum = None
        self.InvoiceCode = None
        self.Date = None
        self.Fare = None
        self.GetOnTime = None
        self.GetOffTime = None
        self.Distance = None
        self.Location = None
        self.PlateNumber = None
        self.InvoiceType = None
        self.Province = None
        self.City = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvoiceNum = params.get("InvoiceNum")
        self.InvoiceCode = params.get("InvoiceCode")
        self.Date = params.get("Date")
        self.Fare = params.get("Fare")
        self.GetOnTime = params.get("GetOnTime")
        self.GetOffTime = params.get("GetOffTime")
        self.Distance = params.get("Distance")
        self.Location = params.get("Location")
        self.PlateNumber = params.get("PlateNumber")
        self.InvoiceType = params.get("InvoiceType")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.RequestId = params.get("RequestId")


class TextArithmetic(AbstractModel):
    """算式识别结果

    """

    def __init__(self):
        r"""
        :param DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param Result: 算式运算结果，true-正确   false-错误或非法参数
        :type Result: bool
        :param Confidence: 保留字段，暂不支持
        :type Confidence: int
        :param Polygon: 原图文本行坐标，以四个顶点坐标表示（保留字段，暂不支持）
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 保留字段，暂不支持
        :type AdvancedInfo: str
        :param ItemCoord: 文本行旋转纠正之后在图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        :param ExpressionType: 算式题型编号：
‘1’: 加减乘除四则
‘2’: 加减乘除已知结果求运算因子
‘3’: 判断大小
‘4’: 约等于估算
‘5’: 带余数除法
‘6’: 分数四则运算
‘7’: 单位换算
‘8’: 竖式加减法
‘9’: 竖式乘除法
‘10’: 脱式计算
‘11’: 解方程
        :type ExpressionType: str
        :param Answer: 错题推荐答案，算式运算结果正确返回为""，算式运算结果错误返回推荐答案 (注：暂不支持多个关系运算符（如1<10<7）、无关系运算符（如frac(1,2)+frac(2,3)）、单位换算（如1元=100角）错题的推荐答案返回)
        :type Answer: str
        """
        self.DetectedText = None
        self.Result = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None
        self.ItemCoord = None
        self.ExpressionType = None
        self.Answer = None


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
        if params.get("ItemCoord") is not None:
            self.ItemCoord = ItemCoord()
            self.ItemCoord._deserialize(params.get("ItemCoord"))
        self.ExpressionType = params.get("ExpressionType")
        self.Answer = params.get("Answer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectRequest(AbstractModel):
    """TextDetect请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectResponse(AbstractModel):
    """TextDetect返回参数结构体

    """

    def __init__(self):
        r"""
        :param HasText: 图片中是否包含文字。
        :type HasText: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HasText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HasText = params.get("HasText")
        self.RequestId = params.get("RequestId")


class TextDetection(AbstractModel):
    """文字识别结果

    """

    def __init__(self):
        r"""
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
        :param ItemPolygon: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type ItemPolygon: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        :param Words: 识别出来的单字信息包括单字（包括单字Character和单字置信度confidence）， 支持识别的接口：GeneralBasicOCR、GeneralAccurateOCR
        :type Words: list of DetectedWords
        :param WordCoordPoint: 单字在原图中的四点坐标， 支持识别的接口：GeneralBasicOCR、GeneralAccurateOCR
        :type WordCoordPoint: list of DetectedWordCoordPoint
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None
        self.ItemPolygon = None
        self.Words = None
        self.WordCoordPoint = None


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
        if params.get("ItemPolygon") is not None:
            self.ItemPolygon = ItemCoord()
            self.ItemPolygon._deserialize(params.get("ItemPolygon"))
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = DetectedWords()
                obj._deserialize(item)
                self.Words.append(obj)
        if params.get("WordCoordPoint") is not None:
            self.WordCoordPoint = []
            for item in params.get("WordCoordPoint"):
                obj = DetectedWordCoordPoint()
                obj._deserialize(item)
                self.WordCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectionEn(AbstractModel):
    """英文识别结果

    """

    def __init__(self):
        r"""
        :param DetectedText: 识别出的文本行内容。
        :type DetectedText: str
        :param Confidence: 置信度 0 ~100。
        :type Confidence: int
        :param Polygon: 文本行在原图中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 此字段为扩展字段。目前EnglishOCR接口返回内容为空。
        :type AdvancedInfo: str
        :param WordCoordPoint: 英文单词在原图中的四点坐标。
        :type WordCoordPoint: list of WordCoordPoint
        :param CandWord: 候选字符集(包含候选字Character以及置信度Confidence)。
        :type CandWord: list of CandWord
        :param Words: 识别出来的单词信息（包括单词Character和单词置信度confidence）
        :type Words: list of Words
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None
        self.WordCoordPoint = None
        self.CandWord = None
        self.Words = None


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
        if params.get("WordCoordPoint") is not None:
            self.WordCoordPoint = []
            for item in params.get("WordCoordPoint"):
                obj = WordCoordPoint()
                obj._deserialize(item)
                self.WordCoordPoint.append(obj)
        if params.get("CandWord") is not None:
            self.CandWord = []
            for item in params.get("CandWord"):
                obj = CandWord()
                obj._deserialize(item)
                self.CandWord.append(obj)
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = Words()
                obj._deserialize(item)
                self.Words.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectionResult(AbstractModel):
    """识别结果

    """

    def __init__(self):
        r"""
        :param Value: 识别出的文本行内容
        :type Value: str
        :param Polygon: 坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        """
        self.Value = None
        self.Polygon = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextEduPaper(AbstractModel):
    """数学试题识别结果

    """

    def __init__(self):
        r"""
        :param Item: 识别出的字段名称（关键字）
        :type Item: str
        :param DetectedText: 识别出的字段名称对应的值，也就是字段Item对应的字符串结果
        :type DetectedText: str
        :param Itemcoord: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type Itemcoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        self.Item = None
        self.DetectedText = None
        self.Itemcoord = None


    def _deserialize(self, params):
        self.Item = params.get("Item")
        self.DetectedText = params.get("DetectedText")
        if params.get("Itemcoord") is not None:
            self.Itemcoord = ItemCoord()
            self.Itemcoord._deserialize(params.get("Itemcoord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextFormula(AbstractModel):
    """数学公式识别结果

    """

    def __init__(self):
        r"""
        :param DetectedText: 识别出的文本行内容
        :type DetectedText: str
        """
        self.DetectedText = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextGeneralHandwriting(AbstractModel):
    """文字识别结果

    """

    def __init__(self):
        r"""
        :param DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 - 100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        :param AdvancedInfo: 此字段为扩展字段。
能返回文本行的段落信息，例如：{\"Parag\":{\"ParagNo\":2}}，
其中ParagNo为段落行，从1开始。
        :type AdvancedInfo: str
        :param WordPolygon: 字的坐标数组，以四个顶点坐标表示
注意：此字段可能返回 null，表示取不到有效值。
        :type WordPolygon: list of Polygon
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None
        self.WordPolygon = None


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
        if params.get("WordPolygon") is not None:
            self.WordPolygon = []
            for item in params.get("WordPolygon"):
                obj = Polygon()
                obj._deserialize(item)
                self.WordPolygon.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTable(AbstractModel):
    """表格识别结果

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextVatInvoice(AbstractModel):
    """增值税发票识别结果

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称（关键字）。支持以下字段的识别：
发票代码、 发票号码、 打印发票代码、 打印发票号码、 开票日期、 购买方识别号、 小写金额、 价税合计(大写)、 销售方识别号、 校验码、 购买方名称、 销售方名称、 税额、 复核、 联次名称、 备注、 联次、 密码区、 开票人、 收款人、 （货物或应税劳务、服务名称）、省、 市、 服务类型、 通行费标志、 是否代开、 是否收购、 合计金额、 是否有公司印章、 发票消费类型、 车船税、 机器编号、 成品油标志、 税率、 合计税额、 （购买方地址、电话）、 （销售方地址、电话）、 单价、 金额、 销售方开户行及账号、 购买方开户行及账号、 规格型号、 发票名称、 单位、 数量、 校验码备选、 校验码后六位备选、发票号码备选、车牌号、类型、通行日期起、通行日期止、发票类型。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Polygon: 字段在原图中的中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self.Name = None
        self.Value = None
        self.Polygon = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Polygon") is not None:
            self.Polygon = Polygon()
            self.Polygon._deserialize(params.get("Polygon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextVehicleBack(AbstractModel):
    """行驶证副页正面的识别结果

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextVehicleFront(AbstractModel):
    """行驶证主页正面的识别结果

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWaybill(AbstractModel):
    """运单识别结果

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoiceInfo(AbstractModel):
    """过路过桥费字段信息

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称（关键字）。支持以下字段的识别：
发票代码、发票号码、日期、金额、入口、出口、时间、发票消费类型、高速标志。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoiceOCRRequest(AbstractModel):
    """TollInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoiceOCRResponse(AbstractModel):
    """TollInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TollInvoiceInfos: 过路过桥费发票识别结果，具体内容请点击左侧链接。
        :type TollInvoiceInfos: list of TollInvoiceInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TollInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TollInvoiceInfos") is not None:
            self.TollInvoiceInfos = []
            for item in params.get("TollInvoiceInfos"):
                obj = TollInvoiceInfo()
                obj._deserialize(item)
                self.TollInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class TrainTicketOCRRequest(AbstractModel):
    """TrainTicketOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainTicketOCRResponse(AbstractModel):
    """TrainTicketOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TicketNum: 编号
        :type TicketNum: str
        :param StartStation: 出发站
        :type StartStation: str
        :param DestinationStation: 到达站
        :type DestinationStation: str
        :param Date: 出发时间
        :type Date: str
        :param TrainNum: 车次
        :type TrainNum: str
        :param Seat: 座位号
        :type Seat: str
        :param Name: 姓名
        :type Name: str
        :param Price: 票价
        :type Price: str
        :param SeatCategory: 席别
        :type SeatCategory: str
        :param ID: 身份证号
        :type ID: str
        :param InvoiceType: 发票消费类型：交通
        :type InvoiceType: str
        :param SerialNumber: 序列号
        :type SerialNumber: str
        :param AdditionalCost: 加收票价
        :type AdditionalCost: str
        :param HandlingFee: 手续费
        :type HandlingFee: str
        :param LegalAmount: 大写金额（票面有大写金额该字段才有值）
        :type LegalAmount: str
        :param TicketStation: 售票站
        :type TicketStation: str
        :param OriginalPrice: 原票价（一般有手续费的才有原始票价字段）
        :type OriginalPrice: str
        :param InvoiceStyle: 发票类型：火车票、火车票补票、火车票退票凭证
        :type InvoiceStyle: str
        :param ReceiptNumber: 收据号码
        :type ReceiptNumber: str
        :param IsReceipt: 仅供报销使用：1为是，0为否
        :type IsReceipt: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TicketNum = None
        self.StartStation = None
        self.DestinationStation = None
        self.Date = None
        self.TrainNum = None
        self.Seat = None
        self.Name = None
        self.Price = None
        self.SeatCategory = None
        self.ID = None
        self.InvoiceType = None
        self.SerialNumber = None
        self.AdditionalCost = None
        self.HandlingFee = None
        self.LegalAmount = None
        self.TicketStation = None
        self.OriginalPrice = None
        self.InvoiceStyle = None
        self.ReceiptNumber = None
        self.IsReceipt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TicketNum = params.get("TicketNum")
        self.StartStation = params.get("StartStation")
        self.DestinationStation = params.get("DestinationStation")
        self.Date = params.get("Date")
        self.TrainNum = params.get("TrainNum")
        self.Seat = params.get("Seat")
        self.Name = params.get("Name")
        self.Price = params.get("Price")
        self.SeatCategory = params.get("SeatCategory")
        self.ID = params.get("ID")
        self.InvoiceType = params.get("InvoiceType")
        self.SerialNumber = params.get("SerialNumber")
        self.AdditionalCost = params.get("AdditionalCost")
        self.HandlingFee = params.get("HandlingFee")
        self.LegalAmount = params.get("LegalAmount")
        self.TicketStation = params.get("TicketStation")
        self.OriginalPrice = params.get("OriginalPrice")
        self.InvoiceStyle = params.get("InvoiceStyle")
        self.ReceiptNumber = params.get("ReceiptNumber")
        self.IsReceipt = params.get("IsReceipt")
        self.RequestId = params.get("RequestId")


class UsedVehicleInvoiceInfo(AbstractModel):
    """二手车销售统一发票信息

    """

    def __init__(self):
        r"""
        :param TaxBureau: 所属税局
        :type TaxBureau: str
        :param Buyer: 买方单位/个人
        :type Buyer: str
        :param BuyerNo: 买方单位代码/身份证号码
        :type BuyerNo: str
        :param BuyerAddress: 买方单位/个人地址
        :type BuyerAddress: str
        :param BuyerTel: 买方单位电话
        :type BuyerTel: str
        :param Seller: 卖方单位/个人
        :type Seller: str
        :param SellerNo: 卖方单位代码/身份证号码
        :type SellerNo: str
        :param SellerAddress: 卖方单位/个人地址
        :type SellerAddress: str
        :param SellerTel: 卖方单位电话
        :type SellerTel: str
        :param VehicleLicenseNo: 车牌照号
        :type VehicleLicenseNo: str
        :param RegisterNo: 登记证号
        :type RegisterNo: str
        :param VehicleIdentifyNo: 车架号/车辆识别代码
        :type VehicleIdentifyNo: str
        :param ManagementOffice: 转入地车辆管理所名称
        :type ManagementOffice: str
        :param VehicleTotalPrice: 车价合计
        :type VehicleTotalPrice: str
        :param Auctioneer: 经营、拍卖单位
        :type Auctioneer: str
        :param AuctioneerAddress: 经营、拍卖单位地址
        :type AuctioneerAddress: str
        :param AuctioneerTaxpayerNum: 经营、拍卖单位纳税人识别号
        :type AuctioneerTaxpayerNum: str
        :param AuctioneerBankAccount: 经营、拍卖单位开户银行、账号
        :type AuctioneerBankAccount: str
        :param AuctioneerTel: 经营、拍卖单位电话
        :type AuctioneerTel: str
        :param Market: 二手车市场
        :type Market: str
        :param MarketTaxpayerNum: 二手车市场纳税人识别号
        :type MarketTaxpayerNum: str
        :param MarketAddress: 二手车市场地址
        :type MarketAddress: str
        :param MarketBankAccount: 二手车市场开户银行账号
        :type MarketBankAccount: str
        :param MarketTel: 二手车市场电话
        :type MarketTel: str
        """
        self.TaxBureau = None
        self.Buyer = None
        self.BuyerNo = None
        self.BuyerAddress = None
        self.BuyerTel = None
        self.Seller = None
        self.SellerNo = None
        self.SellerAddress = None
        self.SellerTel = None
        self.VehicleLicenseNo = None
        self.RegisterNo = None
        self.VehicleIdentifyNo = None
        self.ManagementOffice = None
        self.VehicleTotalPrice = None
        self.Auctioneer = None
        self.AuctioneerAddress = None
        self.AuctioneerTaxpayerNum = None
        self.AuctioneerBankAccount = None
        self.AuctioneerTel = None
        self.Market = None
        self.MarketTaxpayerNum = None
        self.MarketAddress = None
        self.MarketBankAccount = None
        self.MarketTel = None


    def _deserialize(self, params):
        self.TaxBureau = params.get("TaxBureau")
        self.Buyer = params.get("Buyer")
        self.BuyerNo = params.get("BuyerNo")
        self.BuyerAddress = params.get("BuyerAddress")
        self.BuyerTel = params.get("BuyerTel")
        self.Seller = params.get("Seller")
        self.SellerNo = params.get("SellerNo")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerTel = params.get("SellerTel")
        self.VehicleLicenseNo = params.get("VehicleLicenseNo")
        self.RegisterNo = params.get("RegisterNo")
        self.VehicleIdentifyNo = params.get("VehicleIdentifyNo")
        self.ManagementOffice = params.get("ManagementOffice")
        self.VehicleTotalPrice = params.get("VehicleTotalPrice")
        self.Auctioneer = params.get("Auctioneer")
        self.AuctioneerAddress = params.get("AuctioneerAddress")
        self.AuctioneerTaxpayerNum = params.get("AuctioneerTaxpayerNum")
        self.AuctioneerBankAccount = params.get("AuctioneerBankAccount")
        self.AuctioneerTel = params.get("AuctioneerTel")
        self.Market = params.get("Market")
        self.MarketTaxpayerNum = params.get("MarketTaxpayerNum")
        self.MarketAddress = params.get("MarketAddress")
        self.MarketBankAccount = params.get("MarketBankAccount")
        self.MarketTel = params.get("MarketTel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoice(AbstractModel):
    """增值税发票信息

    """

    def __init__(self):
        r"""
        :param Code: 发票代码
        :type Code: str
        :param Number: 发票号码
        :type Number: str
        :param Date: 开票日期
        :type Date: str
        :param BuyerName: 购方抬头
        :type BuyerName: str
        :param BuyerTaxCode: 购方税号
        :type BuyerTaxCode: str
        :param BuyerAddressPhone: 购方地址电话
        :type BuyerAddressPhone: str
        :param BuyerBankAccount: 购方银行账号
        :type BuyerBankAccount: str
        :param SellerName: 销方名称
        :type SellerName: str
        :param SellerTaxCode: 销方税号
        :type SellerTaxCode: str
        :param SellerAddressPhone: 销方地址电话
        :type SellerAddressPhone: str
        :param SellerBankAccount: 销方银行账号
        :type SellerBankAccount: str
        :param Remark: 备注
        :type Remark: str
        :param MachineNo: 机器编码
        :type MachineNo: str
        :param Type: 票种类型
01：增值税专用发票，
02：货运运输业增值税专用发票，
03：机动车销售统一发票，
04：增值税普通发票，
08：增值税电子专用发票（含全电，全电仅新版接口支持），
10：增值税电子普通发票（含全电，全电仅新版接口支持），
11：增值税普通发票（卷式），
14：增值税电子（通行费）发票，
15：二手车销售统一发票，
32：深圳区块链发票
        :type Type: str
        :param CheckCode: 检验码
        :type CheckCode: str
        :param IsAbandoned: 是否作废（红冲）是否作废（红冲）
Y：已作废，N：未作废，H：红冲，HP：部分红冲，HF：全额红冲
        :type IsAbandoned: str
        :param HasSellerList: 是否有销货清单 
Y: 有清单 N：无清单 
卷票无
        :type HasSellerList: str
        :param SellerListTitle: 销货清单标题
        :type SellerListTitle: str
        :param SellerListTax: 销货清单税额
        :type SellerListTax: str
        :param AmountWithoutTax: 不含税金额
        :type AmountWithoutTax: str
        :param TaxAmount: 税额
        :type TaxAmount: str
        :param AmountWithTax: 含税金额
        :type AmountWithTax: str
        :param Items: 项目明细
        :type Items: list of VatInvoiceItem
        :param TaxBureau: 所属税局
        :type TaxBureau: str
        :param TrafficFreeFlag: 通行费标志:Y、是;N、否
        :type TrafficFreeFlag: str
        """
        self.Code = None
        self.Number = None
        self.Date = None
        self.BuyerName = None
        self.BuyerTaxCode = None
        self.BuyerAddressPhone = None
        self.BuyerBankAccount = None
        self.SellerName = None
        self.SellerTaxCode = None
        self.SellerAddressPhone = None
        self.SellerBankAccount = None
        self.Remark = None
        self.MachineNo = None
        self.Type = None
        self.CheckCode = None
        self.IsAbandoned = None
        self.HasSellerList = None
        self.SellerListTitle = None
        self.SellerListTax = None
        self.AmountWithoutTax = None
        self.TaxAmount = None
        self.AmountWithTax = None
        self.Items = None
        self.TaxBureau = None
        self.TrafficFreeFlag = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Number = params.get("Number")
        self.Date = params.get("Date")
        self.BuyerName = params.get("BuyerName")
        self.BuyerTaxCode = params.get("BuyerTaxCode")
        self.BuyerAddressPhone = params.get("BuyerAddressPhone")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.SellerName = params.get("SellerName")
        self.SellerTaxCode = params.get("SellerTaxCode")
        self.SellerAddressPhone = params.get("SellerAddressPhone")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.Remark = params.get("Remark")
        self.MachineNo = params.get("MachineNo")
        self.Type = params.get("Type")
        self.CheckCode = params.get("CheckCode")
        self.IsAbandoned = params.get("IsAbandoned")
        self.HasSellerList = params.get("HasSellerList")
        self.SellerListTitle = params.get("SellerListTitle")
        self.SellerListTax = params.get("SellerListTax")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.TaxAmount = params.get("TaxAmount")
        self.AmountWithTax = params.get("AmountWithTax")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = VatInvoiceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TaxBureau = params.get("TaxBureau")
        self.TrafficFreeFlag = params.get("TrafficFreeFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceGoodsInfo(AbstractModel):
    """发票商品

    """

    def __init__(self):
        r"""
        :param Item: 项目名称
        :type Item: str
        :param Specification: 规格型号
        :type Specification: str
        :param MeasurementDimension: 单位
        :type MeasurementDimension: str
        :param Price: 价格
        :type Price: str
        :param Quantity: 数量
        :type Quantity: str
        :param Amount: 金额
        :type Amount: str
        :param TaxScheme: 税率(如6%、免税)
        :type TaxScheme: str
        :param TaxAmount: 税额
        :type TaxAmount: str
        """
        self.Item = None
        self.Specification = None
        self.MeasurementDimension = None
        self.Price = None
        self.Quantity = None
        self.Amount = None
        self.TaxScheme = None
        self.TaxAmount = None


    def _deserialize(self, params):
        self.Item = params.get("Item")
        self.Specification = params.get("Specification")
        self.MeasurementDimension = params.get("MeasurementDimension")
        self.Price = params.get("Price")
        self.Quantity = params.get("Quantity")
        self.Amount = params.get("Amount")
        self.TaxScheme = params.get("TaxScheme")
        self.TaxAmount = params.get("TaxAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceItem(AbstractModel):
    """增值税发票项目明细

    """

    def __init__(self):
        r"""
        :param LineNo: 行号
        :type LineNo: str
        :param Name: 名称
        :type Name: str
        :param Spec: 规格
        :type Spec: str
        :param Unit: 单位
        :type Unit: str
        :param Quantity: 数量
        :type Quantity: str
        :param UnitPrice: 单价
        :type UnitPrice: str
        :param AmountWithoutTax: 不含税金额
        :type AmountWithoutTax: str
        :param TaxRate: 税率
        :type TaxRate: str
        :param TaxAmount: 税额
        :type TaxAmount: str
        :param TaxClassifyCode: 税收分类编码
        :type TaxClassifyCode: str
        """
        self.LineNo = None
        self.Name = None
        self.Spec = None
        self.Unit = None
        self.Quantity = None
        self.UnitPrice = None
        self.AmountWithoutTax = None
        self.TaxRate = None
        self.TaxAmount = None
        self.TaxClassifyCode = None


    def _deserialize(self, params):
        self.LineNo = params.get("LineNo")
        self.Name = params.get("Name")
        self.Spec = params.get("Spec")
        self.Unit = params.get("Unit")
        self.Quantity = params.get("Quantity")
        self.UnitPrice = params.get("UnitPrice")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.TaxRate = params.get("TaxRate")
        self.TaxAmount = params.get("TaxAmount")
        self.TaxClassifyCode = params.get("TaxClassifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceOCRRequest(AbstractModel):
    """VatInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片/PDF的 Base64 值。
支持的文件格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片/PDF大小：所下载文件经Base64编码后不超过 7M。文件下载时间不超过 3 秒。
输入参数 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片/PDF的 Url 地址。
支持的文件格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片/PDF大小：所下载文件经 Base64 编码后不超过 7M。文件下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.IsPdf = None
        self.PdfPageNumber = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.IsPdf = params.get("IsPdf")
        self.PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceOCRResponse(AbstractModel):
    """VatInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param VatInvoiceInfos: 检测到的文本信息，具体内容请点击左侧链接。
        :type VatInvoiceInfos: list of TextVatInvoice
        :param Items: 明细条目。VatInvoiceInfos中关于明细项的具体条目。
        :type Items: list of VatInvoiceItem
        :param PdfPageSize: 默认值为0。如果图片为PDF时，返回PDF的总页数。
        :type PdfPageSize: int
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VatInvoiceInfos = None
        self.Items = None
        self.PdfPageSize = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VatInvoiceInfos") is not None:
            self.VatInvoiceInfos = []
            for item in params.get("VatInvoiceInfos"):
                obj = TextVatInvoice()
                obj._deserialize(item)
                self.VatInvoiceInfos.append(obj)
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = VatInvoiceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.PdfPageSize = params.get("PdfPageSize")
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class VatInvoiceUserInfo(AbstractModel):
    """发票人员信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param TaxId: 纳税人识别号
        :type TaxId: str
        :param AddrTel: 地 址、电 话
        :type AddrTel: str
        :param FinancialAccount: 开户行及账号
        :type FinancialAccount: str
        """
        self.Name = None
        self.TaxId = None
        self.AddrTel = None
        self.FinancialAccount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TaxId = params.get("TaxId")
        self.AddrTel = params.get("AddrTel")
        self.FinancialAccount = params.get("FinancialAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceVerifyNewRequest(AbstractModel):
    """VatInvoiceVerifyNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoiceNo: 发票号码，8位、20位（全电票）
        :type InvoiceNo: str
        :param InvoiceDate: 开票日期（不支持当天发票查询，支持五年以内开具的发票），格式：“YYYY-MM-DD”，如：2019-12-20。
        :type InvoiceDate: str
        :param InvoiceCode: 发票代码（10或12 位），全电发票为空。查验未成功超过5次后当日无法再查。
        :type InvoiceCode: str
        :param InvoiceKind: 票种类型 01:增值税专用发票， 02:货运运输业增值税专用发 票， 03:机动车销售统一发票， 04:增值税普通发票， 08:增值税电子专用发票(含全电)， 10:增值税电子普通发票(含全电)， 11:增值税普通发票(卷式)， 14:增值税电子(通行费)发 票， 15:二手车销售统一发票， 32:深圳区块链发票(云南区块链因业务调整现已下线)。
        :type InvoiceKind: str
        :param CheckCode: 校验码后 6 位，增值税普通发票、增值税电子普通发票、增值税普通发票(卷式)、增值税电子普通发票(通行费)时必填;
区块链为 5 位
        :type CheckCode: str
        :param Amount: 不含税金额，增值税专用发票、增值税电子专用发票、机动车销售统一发票、二手车销售统一发票、区块链发票时必填; 全电发票为价税合计(含税金额)
        :type Amount: str
        """
        self.InvoiceNo = None
        self.InvoiceDate = None
        self.InvoiceCode = None
        self.InvoiceKind = None
        self.CheckCode = None
        self.Amount = None


    def _deserialize(self, params):
        self.InvoiceNo = params.get("InvoiceNo")
        self.InvoiceDate = params.get("InvoiceDate")
        self.InvoiceCode = params.get("InvoiceCode")
        self.InvoiceKind = params.get("InvoiceKind")
        self.CheckCode = params.get("CheckCode")
        self.Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceVerifyNewResponse(AbstractModel):
    """VatInvoiceVerifyNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param Invoice: 增值税发票信息，详情请点击左侧链接。
        :type Invoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoice`
        :param VehicleInvoiceInfo: 机动车销售统一发票信息
        :type VehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.VehicleInvoiceInfo`
        :param UsedVehicleInvoiceInfo: 二手车销售统一发票信息
        :type UsedVehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.UsedVehicleInvoiceInfo`
        :param PassInvoiceInfoList: 通行费发票信息
        :type PassInvoiceInfoList: list of PassInvoiceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Invoice = None
        self.VehicleInvoiceInfo = None
        self.UsedVehicleInvoiceInfo = None
        self.PassInvoiceInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Invoice") is not None:
            self.Invoice = VatInvoice()
            self.Invoice._deserialize(params.get("Invoice"))
        if params.get("VehicleInvoiceInfo") is not None:
            self.VehicleInvoiceInfo = VehicleInvoiceInfo()
            self.VehicleInvoiceInfo._deserialize(params.get("VehicleInvoiceInfo"))
        if params.get("UsedVehicleInvoiceInfo") is not None:
            self.UsedVehicleInvoiceInfo = UsedVehicleInvoiceInfo()
            self.UsedVehicleInvoiceInfo._deserialize(params.get("UsedVehicleInvoiceInfo"))
        if params.get("PassInvoiceInfoList") is not None:
            self.PassInvoiceInfoList = []
            for item in params.get("PassInvoiceInfoList"):
                obj = PassInvoiceInfo()
                obj._deserialize(item)
                self.PassInvoiceInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class VatInvoiceVerifyRequest(AbstractModel):
    """VatInvoiceVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoiceCode: 发票代码， 一张发票一天只能查询5次。
        :type InvoiceCode: str
        :param InvoiceNo: 发票号码（8位）
        :type InvoiceNo: str
        :param InvoiceDate: 开票日期（不支持当天发票查询，支持五年以内开具的发票），格式：“YYYY-MM-DD”，如：2019-12-20。
        :type InvoiceDate: str
        :param Additional: 根据票种传递对应值，如果报参数错误，请仔细检查每个票种对应的值

增值税专用发票：开具金额（不含税）

增值税普通发票、增值税电子普通发票（含通行费发票）、增值税普通发票（卷票）：校验码后6位

区块链发票：不含税金额/校验码，例如：“285.01/856ab”

机动车销售统一发票：不含税价

货物运输业增值税专用发票：合计金额

二手车销售统一发票：车价合计
        :type Additional: str
        """
        self.InvoiceCode = None
        self.InvoiceNo = None
        self.InvoiceDate = None
        self.Additional = None


    def _deserialize(self, params):
        self.InvoiceCode = params.get("InvoiceCode")
        self.InvoiceNo = params.get("InvoiceNo")
        self.InvoiceDate = params.get("InvoiceDate")
        self.Additional = params.get("Additional")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceVerifyResponse(AbstractModel):
    """VatInvoiceVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param Invoice: 增值税发票信息，详情请点击左侧链接。
        :type Invoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoice`
        :param VehicleInvoiceInfo: 机动车销售统一发票信息
        :type VehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.VehicleInvoiceInfo`
        :param UsedVehicleInvoiceInfo: 二手车销售统一发票信息
        :type UsedVehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.UsedVehicleInvoiceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Invoice = None
        self.VehicleInvoiceInfo = None
        self.UsedVehicleInvoiceInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Invoice") is not None:
            self.Invoice = VatInvoice()
            self.Invoice._deserialize(params.get("Invoice"))
        if params.get("VehicleInvoiceInfo") is not None:
            self.VehicleInvoiceInfo = VehicleInvoiceInfo()
            self.VehicleInvoiceInfo._deserialize(params.get("VehicleInvoiceInfo"))
        if params.get("UsedVehicleInvoiceInfo") is not None:
            self.UsedVehicleInvoiceInfo = UsedVehicleInvoiceInfo()
            self.UsedVehicleInvoiceInfo._deserialize(params.get("UsedVehicleInvoiceInfo"))
        self.RequestId = params.get("RequestId")


class VatRollInvoiceInfo(AbstractModel):
    """增值税发票卷票信息

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、合计金额(小写)、合计金额(大写)、开票日期、发票号码、购买方识别号、销售方识别号、校验码、销售方名称、购买方名称、发票消费类型、省、市、是否有公司印章、单价、金额、数量、服务类型、品名、种类。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatRollInvoiceOCRRequest(AbstractModel):
    """VatRollInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatRollInvoiceOCRResponse(AbstractModel):
    """VatRollInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param VatRollInvoiceInfos: 增值税发票（卷票）识别结果，具体内容请点击左侧链接。
        :type VatRollInvoiceInfos: list of VatRollInvoiceInfo
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VatRollInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VatRollInvoiceInfos") is not None:
            self.VatRollInvoiceInfos = []
            for item in params.get("VatRollInvoiceInfos"):
                obj = VatRollInvoiceInfo()
                obj._deserialize(item)
                self.VatRollInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class VehicleInvoiceInfo(AbstractModel):
    """机动车销售统一发票信息

    """

    def __init__(self):
        r"""
        :param CarType: 车辆类型
        :type CarType: str
        :param PlateModel: 厂牌型号
        :type PlateModel: str
        :param ProduceAddress: 产地
        :type ProduceAddress: str
        :param CertificateNo: 合格证号
        :type CertificateNo: str
        :param ImportNo: 进口证明书号
        :type ImportNo: str
        :param VinNo: LSVCA2NP9HN0xxxxx
        :type VinNo: str
        :param PayTaxesNo: 完税证书号
        :type PayTaxesNo: str
        :param Tonnage: 吨位
        :type Tonnage: str
        :param LimitCount: 限乘人数
        :type LimitCount: str
        :param EngineNo: 发动机号码
        :type EngineNo: str
        :param BizCheckFormNo: 商检单号
        :type BizCheckFormNo: str
        :param TaxtationOrgCode: 主管税务机关代码
        :type TaxtationOrgCode: str
        :param TaxtationOrgName: 主管税务机关名称
        :type TaxtationOrgName: str
        :param MotorTaxRate: 税率
        :type MotorTaxRate: str
        :param MotorBankName: 开户行
        :type MotorBankName: str
        :param MotorBankAccount: 账号
        :type MotorBankAccount: str
        :param SellerAddress: 销售地址
        :type SellerAddress: str
        :param SellerTel: 销售电话
        :type SellerTel: str
        :param BuyerNo: 购方身份证
        :type BuyerNo: str
        """
        self.CarType = None
        self.PlateModel = None
        self.ProduceAddress = None
        self.CertificateNo = None
        self.ImportNo = None
        self.VinNo = None
        self.PayTaxesNo = None
        self.Tonnage = None
        self.LimitCount = None
        self.EngineNo = None
        self.BizCheckFormNo = None
        self.TaxtationOrgCode = None
        self.TaxtationOrgName = None
        self.MotorTaxRate = None
        self.MotorBankName = None
        self.MotorBankAccount = None
        self.SellerAddress = None
        self.SellerTel = None
        self.BuyerNo = None


    def _deserialize(self, params):
        self.CarType = params.get("CarType")
        self.PlateModel = params.get("PlateModel")
        self.ProduceAddress = params.get("ProduceAddress")
        self.CertificateNo = params.get("CertificateNo")
        self.ImportNo = params.get("ImportNo")
        self.VinNo = params.get("VinNo")
        self.PayTaxesNo = params.get("PayTaxesNo")
        self.Tonnage = params.get("Tonnage")
        self.LimitCount = params.get("LimitCount")
        self.EngineNo = params.get("EngineNo")
        self.BizCheckFormNo = params.get("BizCheckFormNo")
        self.TaxtationOrgCode = params.get("TaxtationOrgCode")
        self.TaxtationOrgName = params.get("TaxtationOrgName")
        self.MotorTaxRate = params.get("MotorTaxRate")
        self.MotorBankName = params.get("MotorBankName")
        self.MotorBankAccount = params.get("MotorBankAccount")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerTel = params.get("SellerTel")
        self.BuyerNo = params.get("BuyerNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleLicenseOCRRequest(AbstractModel):
    """VehicleLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param CardSide: FRONT 为行驶证主页正面（有红色印章的一面），
BACK 为行驶证副页正面（有号码号牌的一面），
DOUBLE 为行驶证主页正面和副页正面。
默认值为：FRONT。
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleLicenseOCRResponse(AbstractModel):
    """VehicleLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param FrontInfo: 行驶证主页正面的识别结果，CardSide 为 FRONT。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleFront`
        :param BackInfo: 行驶证副页正面的识别结果，CardSide 为 BACK。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleBack`
        :param RecognizeWarnCode: Code 告警码列表和释义：
-9102 复印件告警
-9103 翻拍件告警
-9106 ps告警
注：告警码可以同时存在多个
        :type RecognizeWarnCode: list of int
        :param RecognizeWarnMsg: 告警码说明：
WARN_DRIVER_LICENSE_COPY_CARD 复印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
WARN_DRIVER_LICENSE_PS_CARD ps告警
注：告警信息可以同时存在多个
        :type RecognizeWarnMsg: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrontInfo = None
        self.BackInfo = None
        self.RecognizeWarnCode = None
        self.RecognizeWarnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FrontInfo") is not None:
            self.FrontInfo = TextVehicleFront()
            self.FrontInfo._deserialize(params.get("FrontInfo"))
        if params.get("BackInfo") is not None:
            self.BackInfo = TextVehicleBack()
            self.BackInfo._deserialize(params.get("BackInfo"))
        self.RecognizeWarnCode = params.get("RecognizeWarnCode")
        self.RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self.RequestId = params.get("RequestId")


class VehicleRegCertInfo(AbstractModel):
    """机动车登记证书识别结果

    """

    def __init__(self):
        r"""
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
【注册登记页】
车辆型号、车辆识别代号/车架号、发动机号、制造厂名称、轴距、轮胎数、总质量、外廓尺寸、轴数、车辆出厂日期、发证日期、使用性质、车辆获得方式、车辆类型、国产/进口、燃料种类、车身颜色、发动机型号、车辆品牌、编号、转向形式、
机动车所有人1、身份证明名称1、号码1、登记机关1、登记日期1
机动车所有人2、身份证明名称2、号码2、登记机关2、登记日期2
机动车所有人3、身份证明名称3、号码3、登记机关3、登记日期3
机动车所有人4、身份证明名称4、号码4、登记机关4、登记日期4
机动车所有人5、身份证明名称5、号码5、登记机关5、登记日期5
机动车所有人6、身份证明名称6、号码6、登记机关6、登记日期6
机动车所有人7、身份证明名称7、号码7、登记机关7、登记日期7
【抵押登记页】
机动车登记证书编号、身份证明名称/号码、抵押权人姓名/名称、抵押登记日期。
        :type Name: str
        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleRegCertOCRRequest(AbstractModel):
    """VehicleRegCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleRegCertOCRResponse(AbstractModel):
    """VehicleRegCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param VehicleRegCertInfos: 机动车登记证书识别结果，具体内容请点击左侧链接。
        :type VehicleRegCertInfos: list of VehicleRegCertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VehicleRegCertInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VehicleRegCertInfos") is not None:
            self.VehicleRegCertInfos = []
            for item in params.get("VehicleRegCertInfos"):
                obj = VehicleRegCertInfo()
                obj._deserialize(item)
                self.VehicleRegCertInfos.append(obj)
        self.RequestId = params.get("RequestId")


class VerifyBasicBizLicenseRequest(AbstractModel):
    """VerifyBasicBizLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageBase64: str
        :param ImageUrl: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageUrl: str
        :param ImageConfig: 用于入参是营业执照图片的场景，表示需要校验的参数：RegNum（注册号或者统一社会信用代码），Name（企业名称），Address（经营地址）。选择后会返回相关参数校验结果。RegNum为必选，Name和Address可选。
格式为{RegNum: true, Name:true/false, Address:true/false}

设置方式参考：
Config = Json.stringify({"Name":true,"Address":true})
API 3.0 Explorer 设置方式参考：
Config = {"Name":true,"Address":true}
        :type ImageConfig: str
        :param RegNum: 用于入参是文本的场景，RegNum表示注册号或者统一社会信用代码。若没有传入营业执照图片，则RegNum为必选项，若图片和RegNum都传入，则只使用RegNum。
        :type RegNum: str
        :param Name: 用于入参是文本的场景，Name表示企业名称。Name为可选项，填写后会返回Name的校验结果。
        :type Name: str
        :param Address: 用于入参是文本的场景，Address表示经营地址。Address为可选项，填写后会返回Address的校验结果。
        :type Address: str
        :param RegCapital: 1表示输出注册资本字段（单位：万元），其他值表示不输出。默认不输出。
        :type RegCapital: int
        :param EstablishTime: true表示展示成立/注册日期
        :type EstablishTime: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ImageConfig = None
        self.RegNum = None
        self.Name = None
        self.Address = None
        self.RegCapital = None
        self.EstablishTime = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageConfig = params.get("ImageConfig")
        self.RegNum = params.get("RegNum")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        self.RegCapital = params.get("RegCapital")
        self.EstablishTime = params.get("EstablishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyBasicBizLicenseResponse(AbstractModel):
    """VerifyBasicBizLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 状态码，成功时返回0
        :type ErrorCode: int
        :param CreditCode: 统一社会信用代码
        :type CreditCode: str
        :param Opfrom: 经营期限自（YYYY-MM-DD）
        :type Opfrom: str
        :param Opto: 经营期限至（YYYY-MM-DD）
        :type Opto: str
        :param Frname: 法人姓名
        :type Frname: str
        :param Entstatus: 经营状态，包括：成立、筹建、存续、在营、开业、在册、正常经营、开业登记中、登记成立、撤销、撤销登记、非正常户、告解、个体暂时吊销、个体转企业、吊销（未注销）、拟注销、已注销、（待）迁入、（待）迁出、停业、歇业、清算等。
        :type Entstatus: str
        :param Zsopscope: 经营业务范围
        :type Zsopscope: str
        :param Reason: 查询的状态信息
        :type Reason: str
        :param Oriregno: 原注册号
        :type Oriregno: str
        :param VerifyRegno: 要核验的工商注册号
        :type VerifyRegno: str
        :param Regno: 工商注册号
        :type Regno: str
        :param VerifyEntname: 要核验的企业名称
        :type VerifyEntname: str
        :param Entname: 企业名称
        :type Entname: str
        :param VerifyDom: 要核验的住址
        :type VerifyDom: str
        :param Dom: 住址
        :type Dom: str
        :param RegNumResult: 验证结果
        :type RegNumResult: :class:`tencentcloud.ocr.v20181119.models.BizLicenseVerifyResult`
        :param RegCapital: 注册资本（单位：万元）,只有输入参数regCapital为1的时候才输出
        :type RegCapital: str
        :param EstablishTime: 成立/注册日期，只有输入参数EstablishTime为true时展示，默认为空
        :type EstablishTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.CreditCode = None
        self.Opfrom = None
        self.Opto = None
        self.Frname = None
        self.Entstatus = None
        self.Zsopscope = None
        self.Reason = None
        self.Oriregno = None
        self.VerifyRegno = None
        self.Regno = None
        self.VerifyEntname = None
        self.Entname = None
        self.VerifyDom = None
        self.Dom = None
        self.RegNumResult = None
        self.RegCapital = None
        self.EstablishTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.CreditCode = params.get("CreditCode")
        self.Opfrom = params.get("Opfrom")
        self.Opto = params.get("Opto")
        self.Frname = params.get("Frname")
        self.Entstatus = params.get("Entstatus")
        self.Zsopscope = params.get("Zsopscope")
        self.Reason = params.get("Reason")
        self.Oriregno = params.get("Oriregno")
        self.VerifyRegno = params.get("VerifyRegno")
        self.Regno = params.get("Regno")
        self.VerifyEntname = params.get("VerifyEntname")
        self.Entname = params.get("Entname")
        self.VerifyDom = params.get("VerifyDom")
        self.Dom = params.get("Dom")
        if params.get("RegNumResult") is not None:
            self.RegNumResult = BizLicenseVerifyResult()
            self.RegNumResult._deserialize(params.get("RegNumResult"))
        self.RegCapital = params.get("RegCapital")
        self.EstablishTime = params.get("EstablishTime")
        self.RequestId = params.get("RequestId")


class VerifyBizLicenseRequest(AbstractModel):
    """VerifyBizLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageBase64: str
        :param ImageUrl: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageUrl: str
        :param ImageConfig: 用于入参是营业执照图片的场景，表示需要校验的参数：RegNum（注册号或者统一社会信用代码），Name（企业名称），Address（经营地址）。选择后会返回相关参数校验结果。RegNum为必选，Name和Address可选。
格式为{RegNum: true, Name:true/false, Address:true/false}

设置方式参考：
Config = Json.stringify({"Name":true,"Address":true})
API 3.0 Explorer 设置方式参考：
Config = {"Name":true,"Address":true}
        :type ImageConfig: str
        :param RegNum: 用于入参是文本的场景，RegNum表示注册号或者统一社会信用代码。若没有传入营业执照图片，则RegNum为必选项，若图片和RegNum都传入，则只使用RegNum。
        :type RegNum: str
        :param Name: 用于入参是文本的场景，Name表示企业名称。Name为可选项，填写后会返回Name的校验结果。
        :type Name: str
        :param Address: 用于入参是文本的场景，Address表示经营地址，填写后会返回Address的校验结果。
        :type Address: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ImageConfig = None
        self.RegNum = None
        self.Name = None
        self.Address = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageConfig = params.get("ImageConfig")
        self.RegNum = params.get("RegNum")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyBizLicenseResponse(AbstractModel):
    """VerifyBizLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 状态码
        :type ErrorCode: int
        :param CreditCode: 统一社会信用代码
        :type CreditCode: str
        :param OrgCode: 组织机构代码
        :type OrgCode: str
        :param OpenFrom: 经营期限自（YYYY-MM-DD）
        :type OpenFrom: str
        :param OpenTo: 经营期限至（YYYY-MM-DD）
        :type OpenTo: str
        :param FrName: 法人姓名
        :type FrName: str
        :param EnterpriseStatus: 经营状态，包括：成立、筹建、存续、在营、开业、在册、正常经营、开业登记中、登记成立、撤销、撤销登记、非正常户、告解、个体暂时吊销、个体转企业、吊销（未注销）、拟注销、已注销、（待）迁入、（待）迁出、停业、歇业、清算等。
        :type EnterpriseStatus: str
        :param OperateScopeAndForm: 经营（业务）范围及方式
        :type OperateScopeAndForm: str
        :param RegCap: 注册资金（单位:万元）
        :type RegCap: str
        :param RegCapCur: 注册币种
        :type RegCapCur: str
        :param RegOrg: 登记机关
        :type RegOrg: str
        :param EsDate: 开业日期（YYYY-MM-DD）
        :type EsDate: str
        :param EnterpriseType: 企业（机构）类型
        :type EnterpriseType: str
        :param CancelDate: 注销日期
        :type CancelDate: str
        :param RevokeDate: 吊销日期
        :type RevokeDate: str
        :param AbuItem: 许可经营项目
        :type AbuItem: str
        :param CbuItem: 一般经营项目
        :type CbuItem: str
        :param ApprDate: 核准时间
        :type ApprDate: str
        :param Province: 省（返回空值）
        :type Province: str
        :param City: 地级市（返回空值）
        :type City: str
        :param County: 区\县（返回空值）
        :type County: str
        :param AreaCode: 住所所在行政区划代码（返回空值）
        :type AreaCode: str
        :param IndustryPhyCode: 行业门类代码（返回空值）
        :type IndustryPhyCode: str
        :param IndustryPhyName: 行业门类名称（返回空值）
        :type IndustryPhyName: str
        :param IndustryCode: 国民经济行业代码（返回空值）
        :type IndustryCode: str
        :param IndustryName: 国民经济行业名称（返回空值）
        :type IndustryName: str
        :param OperateScope: 经营（业务）范围
        :type OperateScope: str
        :param VerifyRegNo: 要核验的工商注册号
        :type VerifyRegNo: str
        :param RegNo: 工商注册号
        :type RegNo: str
        :param VerifyEnterpriseName: 要核验的企业名称
        :type VerifyEnterpriseName: str
        :param EnterpriseName: 企业名称
        :type EnterpriseName: str
        :param VerifyAddress: 要核验的注册地址
        :type VerifyAddress: str
        :param Address: 注册地址
        :type Address: str
        :param RegNumResult: 验证结果
        :type RegNumResult: :class:`tencentcloud.ocr.v20181119.models.BizLicenseVerifyResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.CreditCode = None
        self.OrgCode = None
        self.OpenFrom = None
        self.OpenTo = None
        self.FrName = None
        self.EnterpriseStatus = None
        self.OperateScopeAndForm = None
        self.RegCap = None
        self.RegCapCur = None
        self.RegOrg = None
        self.EsDate = None
        self.EnterpriseType = None
        self.CancelDate = None
        self.RevokeDate = None
        self.AbuItem = None
        self.CbuItem = None
        self.ApprDate = None
        self.Province = None
        self.City = None
        self.County = None
        self.AreaCode = None
        self.IndustryPhyCode = None
        self.IndustryPhyName = None
        self.IndustryCode = None
        self.IndustryName = None
        self.OperateScope = None
        self.VerifyRegNo = None
        self.RegNo = None
        self.VerifyEnterpriseName = None
        self.EnterpriseName = None
        self.VerifyAddress = None
        self.Address = None
        self.RegNumResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.CreditCode = params.get("CreditCode")
        self.OrgCode = params.get("OrgCode")
        self.OpenFrom = params.get("OpenFrom")
        self.OpenTo = params.get("OpenTo")
        self.FrName = params.get("FrName")
        self.EnterpriseStatus = params.get("EnterpriseStatus")
        self.OperateScopeAndForm = params.get("OperateScopeAndForm")
        self.RegCap = params.get("RegCap")
        self.RegCapCur = params.get("RegCapCur")
        self.RegOrg = params.get("RegOrg")
        self.EsDate = params.get("EsDate")
        self.EnterpriseType = params.get("EnterpriseType")
        self.CancelDate = params.get("CancelDate")
        self.RevokeDate = params.get("RevokeDate")
        self.AbuItem = params.get("AbuItem")
        self.CbuItem = params.get("CbuItem")
        self.ApprDate = params.get("ApprDate")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.County = params.get("County")
        self.AreaCode = params.get("AreaCode")
        self.IndustryPhyCode = params.get("IndustryPhyCode")
        self.IndustryPhyName = params.get("IndustryPhyName")
        self.IndustryCode = params.get("IndustryCode")
        self.IndustryName = params.get("IndustryName")
        self.OperateScope = params.get("OperateScope")
        self.VerifyRegNo = params.get("VerifyRegNo")
        self.RegNo = params.get("RegNo")
        self.VerifyEnterpriseName = params.get("VerifyEnterpriseName")
        self.EnterpriseName = params.get("EnterpriseName")
        self.VerifyAddress = params.get("VerifyAddress")
        self.Address = params.get("Address")
        if params.get("RegNumResult") is not None:
            self.RegNumResult = BizLicenseVerifyResult()
            self.RegNumResult._deserialize(params.get("RegNumResult"))
        self.RequestId = params.get("RequestId")


class VerifyEnterpriseFourFactorsRequest(AbstractModel):
    """VerifyEnterpriseFourFactors请求参数结构体

    """

    def __init__(self):
        r"""
        :param RealName: 姓名
        :type RealName: str
        :param IdCard: 证件号码（公司注册证件号）
        :type IdCard: str
        :param EnterpriseName: 企业全称
        :type EnterpriseName: str
        :param EnterpriseMark: 企业标识（注册号，统一社会信用代码）
        :type EnterpriseMark: str
        """
        self.RealName = None
        self.IdCard = None
        self.EnterpriseName = None
        self.EnterpriseMark = None


    def _deserialize(self, params):
        self.RealName = params.get("RealName")
        self.IdCard = params.get("IdCard")
        self.EnterpriseName = params.get("EnterpriseName")
        self.EnterpriseMark = params.get("EnterpriseMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyEnterpriseFourFactorsResponse(AbstractModel):
    """VerifyEnterpriseFourFactors返回参数结构体

    """

    def __init__(self):
        r"""
        :param State: 核验一致性（1:一致，2:不一致，3:查询无记录）
        :type State: int
        :param Detail: 核验结果明细，7：企业法人/负责人，6：企业股东，5：企
业管理人员，-21：企业名称与企业标识不符，-22：姓名不一致，-23：证件号码不一致，-24：企业名称不一致，-25：企业标识不一致
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.ocr.v20181119.models.Detail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        if params.get("Detail") is not None:
            self.Detail = Detail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class VerifyOfdVatInvoiceOCRRequest(AbstractModel):
    """VerifyOfdVatInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param OfdFileUrl: OFD文件的 Url 地址。
        :type OfdFileUrl: str
        :param OfdFileBase64: OFD文件的 Base64 值。
OfdFileUrl 和 OfdFileBase64 必传其一，若两者都传，只解析OfdFileBase64。
        :type OfdFileBase64: str
        """
        self.OfdFileUrl = None
        self.OfdFileBase64 = None


    def _deserialize(self, params):
        self.OfdFileUrl = params.get("OfdFileUrl")
        self.OfdFileBase64 = params.get("OfdFileBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyOfdVatInvoiceOCRResponse(AbstractModel):
    """VerifyOfdVatInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 发票类型
026:增值税电子普通发票
028:增值税电子专用发票
        :type Type: str
        :param InvoiceCode: 发票代码
        :type InvoiceCode: str
        :param InvoiceNumber: 发票号码
        :type InvoiceNumber: str
        :param IssueDate: 开票日期
        :type IssueDate: str
        :param InvoiceCheckCode: 验证码
        :type InvoiceCheckCode: str
        :param MachineNumber: 机器编号
        :type MachineNumber: str
        :param TaxControlCode: 密码区
        :type TaxControlCode: str
        :param Buyer: 购买方
        :type Buyer: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceUserInfo`
        :param Seller: 销售方
        :type Seller: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceUserInfo`
        :param TaxInclusiveTotalAmount: 价税合计
        :type TaxInclusiveTotalAmount: str
        :param InvoiceClerk: 开票人
        :type InvoiceClerk: str
        :param Payee: 收款人
        :type Payee: str
        :param Checker: 复核人
        :type Checker: str
        :param TaxTotalAmount: 税额
        :type TaxTotalAmount: str
        :param TaxExclusiveTotalAmount: 不含税金额
        :type TaxExclusiveTotalAmount: str
        :param Note: 备注
        :type Note: str
        :param GoodsInfos: 货物或服务清单
        :type GoodsInfos: list of VatInvoiceGoodsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Type = None
        self.InvoiceCode = None
        self.InvoiceNumber = None
        self.IssueDate = None
        self.InvoiceCheckCode = None
        self.MachineNumber = None
        self.TaxControlCode = None
        self.Buyer = None
        self.Seller = None
        self.TaxInclusiveTotalAmount = None
        self.InvoiceClerk = None
        self.Payee = None
        self.Checker = None
        self.TaxTotalAmount = None
        self.TaxExclusiveTotalAmount = None
        self.Note = None
        self.GoodsInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InvoiceCode = params.get("InvoiceCode")
        self.InvoiceNumber = params.get("InvoiceNumber")
        self.IssueDate = params.get("IssueDate")
        self.InvoiceCheckCode = params.get("InvoiceCheckCode")
        self.MachineNumber = params.get("MachineNumber")
        self.TaxControlCode = params.get("TaxControlCode")
        if params.get("Buyer") is not None:
            self.Buyer = VatInvoiceUserInfo()
            self.Buyer._deserialize(params.get("Buyer"))
        if params.get("Seller") is not None:
            self.Seller = VatInvoiceUserInfo()
            self.Seller._deserialize(params.get("Seller"))
        self.TaxInclusiveTotalAmount = params.get("TaxInclusiveTotalAmount")
        self.InvoiceClerk = params.get("InvoiceClerk")
        self.Payee = params.get("Payee")
        self.Checker = params.get("Checker")
        self.TaxTotalAmount = params.get("TaxTotalAmount")
        self.TaxExclusiveTotalAmount = params.get("TaxExclusiveTotalAmount")
        self.Note = params.get("Note")
        if params.get("GoodsInfos") is not None:
            self.GoodsInfos = []
            for item in params.get("GoodsInfos"):
                obj = VatInvoiceGoodsInfo()
                obj._deserialize(item)
                self.GoodsInfos.append(obj)
        self.RequestId = params.get("RequestId")


class VinOCRRequest(AbstractModel):
    """VinOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VinOCRResponse(AbstractModel):
    """VinOCR返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param EnablePreDetect: 预检测开关，当待识别运单占整个输入图像的比例较小时，建议打开预检测开关。默认值为false。
        :type EnablePreDetect: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.EnablePreDetect = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.EnablePreDetect = params.get("EnablePreDetect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaybillOCRResponse(AbstractModel):
    """WaybillOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
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
        r"""
        :param Text: 识别出的文本行内容
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordCoordPoint(AbstractModel):
    """英文OCR识别出的单词在原图中的四点坐标数组

    """

    def __init__(self):
        r"""
        :param WordCoordinate: 英文OCR识别出的每个单词在原图中的四点坐标。
        :type WordCoordinate: list of Coord
        """
        self.WordCoordinate = None


    def _deserialize(self, params):
        if params.get("WordCoordinate") is not None:
            self.WordCoordinate = []
            for item in params.get("WordCoordinate"):
                obj = Coord()
                obj._deserialize(item)
                self.WordCoordinate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Words(AbstractModel):
    """识别出来的单词信息包括单词（包括单词Character和单词置信度confidence）

    """

    def __init__(self):
        r"""
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Character: 候选字Character
        :type Character: str
        """
        self.Confidence = None
        self.Character = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Character = params.get("Character")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        