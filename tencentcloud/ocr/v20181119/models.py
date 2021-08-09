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
        """
        :param ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。\n        :type TextDetections: list of AdvertiseTextDetection\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param DetectedText: 识别出的文本行内容\n        :type DetectedText: str\n        :param Confidence: 置信度 0 ~100\n        :type Confidence: int\n        :param Polygon: 文本行坐标，以四个顶点坐标表示\n        :type Polygon: list of Coord\n        :param AdvancedInfo: 此字段为扩展字段。
GeneralBasicOcr接口返回段落信息Parag，包含ParagNo。\n        :type AdvancedInfo: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param SupportHorizontalImage: 用于选择是否支持横屏拍摄。打开则支持横屏拍摄图片角度判断，角度信息在返回参数的angle中，默认值为true\n        :type SupportHorizontalImage: bool\n        :param RejectNonArithmeticPic: 是否拒绝非速算图，打开则拒绝非速算图(注：非速算图是指风景人物等明显不是速算图片的图片)，默认值为false\n        :type RejectNonArithmeticPic: bool\n        :param EnableDispRelatedVertical: 是否展开耦合算式中的竖式计算，默认值为false\n        :type EnableDispRelatedVertical: bool\n        :param EnableDispMidResult: 是否展示竖式算式的中间结果和格式控制字符，默认值为false\n        :type EnableDispMidResult: bool\n        :param EnablePdfRecognize: 是否开启pdf识别，默认值为true\n        :type EnablePdfRecognize: bool\n        :param PdfPageIndex: pdf页码，从0开始，默认为0\n        :type PdfPageIndex: int\n        """
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
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。\n        :type TextDetections: list of TextArithmetic\n        :param Angle: 图片横屏的角度(90度或270度)\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        :param RetBorderCutImage: 是否返回预处理（精确剪裁对齐）后的银行卡图片数据，默认false。\n        :type RetBorderCutImage: bool\n        :param RetCardNoImage: 是否返回卡号的切图图片数据，默认false。\n        :type RetCardNoImage: bool\n        :param EnableCopyCheck: 复印件检测开关，如果输入的图片是银行卡复印件图片则返回告警，默认false。\n        :type EnableCopyCheck: bool\n        :param EnableReshootCheck: 翻拍检测开关，如果输入的图片是银行卡翻拍图片则返回告警，默认false。\n        :type EnableReshootCheck: bool\n        :param EnableBorderCheck: 边框遮挡检测开关，如果输入的图片是银行卡边框被遮挡则返回告警，默认false。\n        :type EnableBorderCheck: bool\n        :param EnableQualityValue: 是否返回图片质量分数（图片质量分数是评价一个图片的模糊程度的标准），默认false。\n        :type EnableQualityValue: bool\n        """
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
        """
        :param CardNo: 卡号\n        :type CardNo: str\n        :param BankInfo: 银行信息\n        :type BankInfo: str\n        :param ValidDate: 有效期，格式如：07/2023\n        :type ValidDate: str\n        :param CardType: 卡类型\n        :type CardType: str\n        :param CardName: 卡名字\n        :type CardName: str\n        :param BorderCutImage: 切片图片数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type BorderCutImage: str\n        :param CardNoImage: 卡号图片数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type CardNoImage: str\n        :param WarningCode: WarningCode 告警码列表和释义：
-9110:银行卡日期无效; 
-9111:银行卡边框不完整; 
-9112:银行卡图片反光;
-9113:银行卡复印件;
-9114:银行卡翻拍件
（告警码可以同时存在多个）
注意：此字段可能返回 null，表示取不到有效值。\n        :type WarningCode: list of int\n        :param QualityValue: 图片质量分数，请求EnableQualityValue时返回（取值范围：0-100，分数越低越模糊，建议阈值≥50）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type QualityValue: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
付款开户行、收款开户行、付款账号、收款账号、回单类型、回单编号、币种、流水号、凭证号码、交易机构、交易金额、手续费、日期等字段信息。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        """
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
        """
        :param BankSlipInfos: 银行回单识别结果，具体内容请点击左侧链接。\n        :type BankSlipInfos: list of BankSlipInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param RegNum: 统一社会信用代码（三合一之前为注册号）\n        :type RegNum: str\n        :param Name: 公司名称\n        :type Name: str\n        :param Capital: 注册资本\n        :type Capital: str\n        :param Person: 法定代表人\n        :type Person: str\n        :param Address: 地址\n        :type Address: str\n        :param Business: 经营范围\n        :type Business: str\n        :param Type: 主体类型\n        :type Type: str\n        :param Period: 营业期限\n        :type Period: str\n        :param ComposingForm: 组成形式\n        :type ComposingForm: str\n        :param SetDate: 成立日期\n        :type SetDate: str\n        :param RecognizeWarnCode: Code 告警码列表和释义：
-20001 非营业执照
注：告警码可以同时存在多个\n        :type RecognizeWarnCode: list of int\n        :param RecognizeWarnMsg: 告警码说明：
OCR_WARNING_TPYE_NOT_MATCH 非营业执照
注：告警信息可以同时存在多个\n        :type RecognizeWarnMsg: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegNum: “0“：一致
“-1”：此号未查询到结果\n        :type RegNum: str\n        :param Name: “0“：一致
“-1”：不一致
“”：不验真\n        :type Name: str\n        :param Address: “0“：一致
“-1”：不一致
“”：不验真\n        :type Address: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、发票号码、日期、票价、始发地、目的地、姓名、时间、发票消费类型、身份证号、省、市。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param BusInvoiceInfos: 汽车票识别结果，具体内容请点击左侧链接。\n        :type BusInvoiceInfos: list of BusInvoiceInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称（关键字，可能重复，比如多个手机），能识别的字段名为：
姓名、英文姓名、英文地址、公司、英文公司、职位、英文职位、部门、英文部门、手机、电话、传真、社交帐号、QQ、MSN、微信、微博、邮箱、邮编、网址、公司账号、其他。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。\n        :type Value: str\n        :param ItemCoord: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）\n        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param Config: 可选字段，根据需要选择是否请求对应字段。
目前支持的字段为：
RetImageType-“PROPROCESS” 图像预处理，string 类型。
图像预处理功能为，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。

SDK 设置方式参考：
Config = Json.stringify({"RetImageType":"PROPROCESS"})
API 3.0 Explorer 设置方式参考：
Config = {"RetImageType":"PROPROCESS"}\n        :type Config: str\n        """
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
        """
        :param BusinessCardInfos: 名片识别结果，具体内容请点击左侧链接。\n        :type BusinessCardInfos: list of BusinessCardInfo\n        :param RetImageBase64: 返回图像预处理后的图片，图像预处理未开启时返回内容为空。\n        :type RetImageBase64: str\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param CandWords: 候选字符集的单词信息（包括单词Character和单词置信度confidence）\n        :type CandWords: list of Words\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、 机打代码、 发票号码、 发动机号码、 合格证号、 机打号码、 价税合计(小写)、 销货单位名称、 身份证号码/组织机构代码、 购买方名称、 销售方纳税人识别号、 购买方纳税人识别号、主管税务机关、 主管税务机关代码、 开票日期、 不含税价(小写)、 吨位、增值税税率或征收率、 车辆识别代号/车架号码、 增值税税额、 厂牌型号、 省、 市、 发票消费类型、 销售方电话、 销售方账号、 产地、 进口证明书号、 车辆类型、 机器编号、备注、开票人、限乘人数、商检单号、销售方地址、销售方开户银行、价税合计、发票类型。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。\n        :type Value: str\n        :param Rect: 字段在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        :param Polygon: 字段在原图中的中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param CarInvoiceInfos: 购车发票识别结果，具体内容请点击左侧链接。\n        :type CarInvoiceInfos: list of CarInvoiceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ParagNo: 段落编号
注意：此字段可能返回 null，表示取不到有效值。\n        :type ParagNo: int\n        :param WordSize: 字体大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type WordSize: int\n        """
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
        """
        :param Name: 分类名称，包括：身份证、护照、名片、银行卡、行驶证、驾驶证、港澳台通行证、户口本、港澳台来往内地通行证、港澳台居住证、不动产证、营业执照\n        :type Name: str\n        :param Type: 分类类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Rect: 位置坐标\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param DiscernType: 可以指定要识别的票证类型,指定后不出现在此列表的票证将不返回类型。不指定时默认返回所有支持类别票证的识别信息。

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
BizLicense: 营业执照\n        :type DiscernType: list of str\n        """
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
        """
        :param ClassifyDetectInfos: 智能卡证分类结果。当图片类型不支持分类识别或者识别出的类型不在请求参数DiscernType指定的范围内时，返回结果中的Type字段将为空字符串，Name字段将返回"其它"\n        :type ClassifyDetectInfos: list of ClassifyDetectInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param X: 横坐标\n        :type X: int\n        :param Y: 纵坐标\n        :type Y: int\n        """
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
        """
        :param Result: 企业四要素核验结果状态码\n        :type Result: int\n        :param Desc: 企业四要素核验结果描述\n        :type Desc: str\n        """
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
        """
        :param WordCoordinate: 单字在原图中的坐标，以四个顶点坐标表示，以左上角为起点，顺时针返回。\n        :type WordCoordinate: list of Coord\n        """
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
        """
        :param Confidence: 置信度 0 ~100\n        :type Confidence: int\n        :param Character: 候选字Character\n        :type Character: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        :param CardSide: FRONT 为驾驶证主页正面（有红色印章的一面），
BACK 为驾驶证副页正面（有档案编号的一面）。
默认值为：FRONT。\n        :type CardSide: str\n        """
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
        """
        :param Name: 姓名\n        :type Name: str\n        :param Sex: 性别\n        :type Sex: str\n        :param Nationality: 国籍\n        :type Nationality: str\n        :param Address: 住址\n        :type Address: str\n        :param DateOfBirth: 出生日期（YYYY-MM-DD）\n        :type DateOfBirth: str\n        :param DateOfFirstIssue: 初次领证日期（YYYY-MM-DD）\n        :type DateOfFirstIssue: str\n        :param Class: 准驾车型\n        :type Class: str\n        :param StartDate: 有效期开始时间（YYYY-MM-DD）\n        :type StartDate: str\n        :param EndDate: 有效期截止时间（YYYY-MM-DD）\n        :type EndDate: str\n        :param CardCode: 证号\n        :type CardCode: str\n        :param ArchivesCode: 档案编号\n        :type ArchivesCode: str\n        :param Record: 记录\n        :type Record: str\n        :param RecognizeWarnCode: Code 告警码列表和释义：
-9102  复印件告警
-9103  翻拍件告警
-9106  ps告警
注：告警码可以同时存在多个\n        :type RecognizeWarnCode: list of int\n        :param RecognizeWarnMsg: 告警码说明：
WARN_DRIVER_LICENSE_COPY_CARD 复印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
WARN_DRIVER_LICENSE_PS_CARD ps告警
注：告警信息可以同时存在多个\n        :type RecognizeWarnMsg: list of str\n        :param IssuingAuthority: 发证单位\n        :type IssuingAuthority: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class DutyPaidProofInfo(AbstractModel):
    """识别出的字段

    """

    def __init__(self):
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
税号 、纳税人识别号 、纳税人名称 、金额合计大写 、金额合计小写 、填发日期 、税务机关 、填票人。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param DutyPaidProofInfos: 完税证明识别结果，具体内容请点击左侧链接。\n        :type DutyPaidProofInfos: list of DutyPaidProofInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param Config: 扩展配置信息。
配置格式：{"option1":value1,"option2":value2}
1. task_type：任务类型【0: 关闭版式分析与处理 1: 开启版式分析处理】可选参数，Int32类型，默认值为1
2. is_structuralization：是否结构化输出【true：返回包体同时返回通用和结构化输出  false：返回包体返回通用输出】 可选参数，Bool类型，默认值为true
3. if_readable_format：是否按照版式整合通用文本/公式输出结果 可选参数，Bool类型，默认值为false
示例：
{"task_type": 1,"is_structuralization": true,"if_readable_format": true}\n        :type Config: str\n        """
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
        """
        :param EduPaperInfos: 检测到的文本信息，具体内容请点击左侧链接。\n        :type EduPaperInfos: list of TextEduPaper\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。\n        :type Angle: int\n        :param QuestionBlockInfos: 结构化方式输出，具体内容请点击左侧链接。\n        :type QuestionBlockInfos: list of QuestionBlockObj\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param EnableCoordPoint: 单词四点坐标开关，开启可返回图片中单词的四点坐标。
该参数默认值为false。\n        :type EnableCoordPoint: bool\n        :param EnableCandWord: 候选字开关，开启可返回识别时多个可能的候选字（每个候选字对应其置信度）。
该参数默认值为false。\n        :type EnableCandWord: bool\n        :param Preprocess: 预处理开关，功能是检测图片倾斜的角度，将原本倾斜的图片矫正。该参数默认值为true。\n        :type Preprocess: bool\n        """
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
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。\n        :type TextDetections: list of TextDetectionEn\n        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>\n        :type Angel: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称（关键字），不同证件类型可能不同，证件类型包含企业登记证书、许可证书、企业执照、三证合一类证书；
支持以下字段：统一社会信用代码、法定代表人、公司名称、公司地址、注册资金、企业关型、经营范围、成立日期、有效期、开办资金、经费来源、举办单位等；\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param EnterpriseLicenseInfos: 企业证照识别结果，具体内容请点击左侧链接。\n        :type EnterpriseLicenseInfos: list of EnterpriseLicenseInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param Obligee: 权利人\n        :type Obligee: str\n        :param Ownership: 共有情况\n        :type Ownership: str\n        :param Location: 坐落\n        :type Location: str\n        :param Unit: 不动产单元号\n        :type Unit: str\n        :param Type: 权利类型\n        :type Type: str\n        :param Property: 权利性质\n        :type Property: str\n        :param Usage: 用途\n        :type Usage: str\n        :param Area: 面积\n        :type Area: str\n        :param Term: 使用期限\n        :type Term: str\n        :param Other: 权利其他状况，多行会用换行符\n连接。\n        :type Other: str\n        :param Angle: 图片旋转角度\n        :type Angle: float\n        :param Number: 不动产权号\n        :type Number: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
【进账单】
日期、出票全称、出票账号、出票开户行、收款人全称、收款人账号、收款开户行、大写金额、小写金额、票据种类、票据张数、票据号码；
【支票】
开户银行、支票种类、凭证号码2、日期、大写金额、小写金额、付款行编号、密码、凭证号码1；
【银行承兑汇票】或【商业承兑汇票】
出票日期、行号1、行号2、出票人全称、出票人账号、付款行全称、收款人全称、收款人账号、收款人开户行、出票金额大写、出票金额小写、汇票到期日、付款行行号、付款行地址。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param FinanBillInfos: 金融票据整单识别结果，具体内容请点击左侧链接。\n        :type FinanBillInfos: list of FinanBillInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
大写金额、小写金额、账号、票号1、票号2、收款人、大写日期、同城交换号、地址-省份、地址-城市、付款行全称、支票密码、支票用途。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param FinanBillSliceInfos: 金融票据切片识别结果，具体内容请点击左侧链接。\n        :type FinanBillSliceInfos: list of FinanBillSliceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
票价、合计金额、填开日期、有效身份证件号码、电子客票号码、验证码、旅客姓名、填开单位、其他税费、燃油附加费、民航发展基金、保险费、销售单位代号、始发地、目的地、航班号、时间、日期、座位等级、承运人、发票消费类型、国内国际标签、印刷序号、客票级别/类别、客票生效日期、有效期截止日期、免费行李。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段 Name 对应的字符串结果。\n        :type Value: str\n        :param Row: 多个行程的字段所在行号，下标从0开始，非行字段或未能识别行号的该值返回-1。\n        :type Row: int\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param FlightInvoiceInfos: 机票行程单识别结果，具体内容请点击左侧链接。\n        :type FlightInvoiceInfos: list of FlightInvoiceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负\n        :type Angle: int\n        :param FormulaInfos: 检测到的文本信息，具体内容请点击左侧链接。\n        :type FormulaInfos: list of TextFormula\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param IsWords: 是否返回单字信息，默认关\n        :type IsWords: bool\n        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.IsWords = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.IsWords = params.get("IsWords")
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
        """
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。\n        :type TextDetections: list of TextDetection\n        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>\n        :type Angel: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片/PDF的 Base64 值。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片/PDF的 Url 地址。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param Scene: 保留字段。\n        :type Scene: str\n        :param LanguageType: 识别语言类型。
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
ara：阿拉伯语\n        :type LanguageType: str\n        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。\n        :type IsPdf: bool\n        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。\n        :type PdfPageNumber: int\n        :param IsWords: 是否返回单字信息，默认关\n        :type IsWords: bool\n        """
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
        """
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。\n        :type TextDetections: list of TextDetection\n        :param Language: 检测到的语言类型，目前支持的语言类型参考入参LanguageType说明。\n        :type Language: str\n        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>\n        :type Angel: float\n        :param PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0\n        :type PdfPageSize: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。\n        :type TextDetections: list of TextDetection\n        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>\n        :type Angel: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。\n        :type IsPdf: bool\n        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。\n        :type PdfPageNumber: int\n        """
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
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。\n        :type TextDetections: list of TextDetection\n        :param Language: 检测到的语言，目前支持的语种范围为：简体中文、繁体中文、英文、日文、韩文。未来将陆续新增对更多语种的支持。
返回结果含义为：zh - 中英混合，jap - 日文，kor - 韩文。\n        :type Language: str\n        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负\n        :type Angel: float\n        :param PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0\n        :type PdfPageSize: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param Scene: 场景字段，默认不用填写。
可选值:only_hw  表示只输出手写体识别结果，过滤印刷体。\n        :type Scene: str\n        :param EnableWordPolygon: 是否开启单字的四点定位坐标输出，默认值为false。\n        :type EnableWordPolygon: bool\n        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None
        self.EnableWordPolygon = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")
        self.EnableWordPolygon = params.get("EnableWordPolygon")
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
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。\n        :type TextDetections: list of TextGeneralHandwriting\n        :param Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>\n        :type Angel: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param DetectFake: 是否鉴伪。\n        :type DetectFake: bool\n        :param ReturnHeadImage: 是否返回人像照片。\n        :type ReturnHeadImage: bool\n        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param CnName: 中文姓名\n        :type CnName: str\n        :param EnName: 英文姓名\n        :type EnName: str\n        :param TelexCode: 中文姓名对应电码\n        :type TelexCode: str\n        :param Sex: 性别 ：“男M”或“女F”\n        :type Sex: str\n        :param Birthday: 出生日期\n        :type Birthday: str\n        :param Permanent: 永久性居民身份证。
0：非永久；
1：永久；
-1：未知。\n        :type Permanent: int\n        :param IdNum: 身份证号码\n        :type IdNum: str\n        :param Symbol: 证件符号，出生日期下的符号，例如"***AZ"\n        :type Symbol: str\n        :param FirstIssueDate: 首次签发日期\n        :type FirstIssueDate: str\n        :param CurrentIssueDate: 最近领用日期\n        :type CurrentIssueDate: str\n        :param FakeDetectResult: 真假判断。
0：无法判断（图像模糊、不完整、反光、过暗等导致无法判断）；
1：假；
2：真。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FakeDetectResult: int\n        :param HeadImage: 人像照片Base64后的结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeadImage: str\n        :param WarningCode: 多重告警码，当身份证是翻拍、复印、PS件时返回对应告警码。
-9102：证照复印件告警
-9103：证照翻拍告警
-9104：证照PS告警
-9105：证照防伪告警\n        :type WarningCode: list of int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param CardSide: FRONT：有照片的一面（人像面），
BACK：无照片的一面（国徽面），
该参数如果不填或填错，将为您自动判断正反面。\n        :type CardSide: str\n        """
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
        """
        :param Name: 证件姓名\n        :type Name: str\n        :param Sex: 性别\n        :type Sex: str\n        :param Birth: 出生日期\n        :type Birth: str\n        :param Address: 地址\n        :type Address: str\n        :param IdCardNo: 身份证号\n        :type IdCardNo: str\n        :param CardType: 0-正面
1-反面\n        :type CardType: int\n        :param ValidDate: 证件有效期限\n        :type ValidDate: str\n        :param Authority: 签发机关\n        :type Authority: str\n        :param VisaNum: 签发次数\n        :type VisaNum: str\n        :param PassNo: 通行证号码\n        :type PassNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        :param CardSide: FRONT：身份证有照片的一面（人像面），
BACK：身份证有国徽的一面（国徽面），
该参数如果不填，将为您自动判断身份证正反面。\n        :type CardSide: str\n        :param Config: 以下可选字段均为bool 类型，默认false：
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
Config = {"CropIdCard":true,"CropPortrait":true}\n        :type Config: str\n        """
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
        """
        :param Name: 姓名（人像面）\n        :type Name: str\n        :param Sex: 性别（人像面）\n        :type Sex: str\n        :param Nation: 民族（人像面）\n        :type Nation: str\n        :param Birth: 出生日期（人像面）\n        :type Birth: str\n        :param Address: 地址（人像面）\n        :type Address: str\n        :param IdNum: 身份证号（人像面）\n        :type IdNum: str\n        :param Authority: 发证机关（国徽面）\n        :type Authority: str\n        :param ValidDate: 证件有效期（国徽面）\n        :type ValidDate: str\n        :param AdvancedInfo: 扩展信息，不请求则不返回，具体输入参考示例3和示例4。
IdCard，裁剪后身份证照片的base64编码，请求 Config.CropIdCard 时返回；
Portrait，身份证头像照片的base64编码，请求 Config.CropPortrait 时返回；

Quality，图片质量分数，请求 Config.Quality 时返回（取值范围：0~100，分数越低越模糊，建议阈值≥50）;
BorderCodeValue，身份证边框不完整告警阈值分数，请求 Config.BorderCheckWarn时返回（取值范围：0~100，分数越低边框遮挡可能性越低，建议阈值≥50）;

WarnInfos，告警信息，Code 告警码列表和释义：
-9100	身份证有效日期不合法告警，
-9101	身份证边框不完整告警，
-9102	身份证复印件告警，
-9103	身份证翻拍告警，
-9105	身份证框内遮挡告警，
-9104	临时身份证告警，
-9106	身份证 PS 告警，
-9107       身份证反光告警。\n        :type AdvancedInfo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class InstitutionOCRRequest(AbstractModel):
    """InstitutionOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param RegId: 注册号\n        :type RegId: str\n        :param ValidDate: 有效期\n        :type ValidDate: str\n        :param Location: 住所\n        :type Location: str\n        :param Name: 名称\n        :type Name: str\n        :param LegalPerson: 法定代表人\n        :type LegalPerson: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
【病案首页】
姓名、性别、出生日期、出院诊断、疾病编码、入院病情等。
【费用清单】
医疗参保人员类别、身份证号、入院方式、结账日期、项目、金额等。
【结算单】
名称、单价、数量、金额、医保内、医保外等。
【医疗发票】
姓名、性别、住院时间、收费项目、金额、合计等。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param InsuranceBillInfos: 保险单据识别结果，具体内容请点击左侧链接。\n        :type InsuranceBillInfos: list of InsuranceBillInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Angle: 识别出的图片在混贴票据图片中的旋转角度。\n        :type Angle: float\n        :param Type: 识别出的图片所属的票据类型。
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
14：购物小票\n        :type Type: int\n        :param Rect: 识别出的图片在混贴票据图片中的位置信息。与Angel结合可以得出原图位置，组成RotatedRect((X+0.5\*Width,Y+0.5\*Height), (Width, Height), Angle)，详情可参考OpenCV文档。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        :param Image: 入参 ReturnImage 为 True 时返回 Base64 编码后的图片。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Image: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、发票号码、日期、合计金额(小写)、合计金额(大写)、购买方识别号、销售方识别号、校验码、购买方名称、销售方名称、时间、种类、发票消费类型、省、市、是否有公司印章。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param InvoiceGeneralInfos: 通用机打发票识别结果，具体内容请点击左侧链接。\n        :type InvoiceGeneralInfos: list of InvoiceGeneralInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param X: 左上角x\n        :type X: int\n        :param Y: 左上角y\n        :type Y: int\n        :param Width: 宽width\n        :type Width: int\n        :param Height: 高height\n        :type Height: int\n        """
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
        


class LicensePlateOCRRequest(AbstractModel):
    """LicensePlateOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param Number: 识别出的车牌号码。\n        :type Number: str\n        :param Confidence: 置信度，0 - 100 之间。\n        :type Confidence: int\n        :param Rect: 文本行在原图片中的像素坐标框。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Number = None
        self.Confidence = None
        self.Rect = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.RequestId = params.get("RequestId")


class MLIDCardOCRRequest(AbstractModel):
    """MLIDCardOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。( 中国地区之外不支持这个字段 )
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param RetImage: 是否返回图片，默认false\n        :type RetImage: bool\n        """
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
        """
        :param ID: 身份证号\n        :type ID: str\n        :param Name: 姓名\n        :type Name: str\n        :param Address: 地址\n        :type Address: str\n        :param Sex: 性别\n        :type Sex: str\n        :param Warn: 告警码
-9103	证照翻拍告警
-9102	证照复印件告警
-9106       证件遮挡告警\n        :type Warn: list of int\n        :param Image: 证件图片\n        :type Image: str\n        :param AdvancedInfo: 扩展字段：
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}\n        :type AdvancedInfo: str\n        :param Type: 证件类型
MyKad  身份证
MyPR    永居证
MyTentera   军官证
MyKAS    临时身份证
POLIS  警察证
IKAD   劳工证
MyKid 儿童卡\n        :type Type: str\n        :param Birthday: 出生日期（目前该字段仅支持IKAD劳工证）\n        :type Birthday: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n        :type ImageBase64: str\n        :param RetImage: 是否返回图片，默认false\n        :type RetImage: bool\n        """
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
        """
        :param ID: 护照ID\n        :type ID: str\n        :param Name: 姓名\n        :type Name: str\n        :param DateOfBirth: 出生日期\n        :type DateOfBirth: str\n        :param Sex: 性别（F女，M男）\n        :type Sex: str\n        :param DateOfExpiration: 有效期\n        :type DateOfExpiration: str\n        :param IssuingCountry: 发行国\n        :type IssuingCountry: str\n        :param Nationality: 国籍\n        :type Nationality: str\n        :param Warn: 告警码
-9103	证照翻拍告警
-9102	证照复印件告警
-9106       证件遮挡告警\n        :type Warn: list of int\n        :param Image: 证件图片\n        :type Image: str\n        :param AdvancedInfo: 扩展字段:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}\n        :type AdvancedInfo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class MainlandPermitOCRRequest(AbstractModel):
    """MainlandPermitOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param RetProfile: 是否返回头像。默认不返回。\n        :type RetProfile: bool\n        """
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
        """
        :param Name: 中文姓名\n        :type Name: str\n        :param EnglishName: 英文姓名\n        :type EnglishName: str\n        :param Sex: 性别\n        :type Sex: str\n        :param Birthday: 出生日期\n        :type Birthday: str\n        :param IssueAuthority: 签发机关\n        :type IssueAuthority: str\n        :param ValidDate: 有效期限\n        :type ValidDate: str\n        :param Number: 证件号\n        :type Number: str\n        :param IssueAddress: 签发地点\n        :type IssueAddress: str\n        :param IssueNumber: 签发次数\n        :type IssueNumber: str\n        :param Type: 证件类别， 如：台湾居民来往大陆通行证、港澳居民来往内地通行证。\n        :type Type: str\n        :param Profile: RetProfile为True时返回头像字段， Base64编码\n        :type Profile: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class MixedInvoiceDetectRequest(AbstractModel):
    """MixedInvoiceDetect请求参数结构体

    """

    def __init__(self):
        """
        :param ReturnImage: 是否需要返回裁剪后的图片。\n        :type ReturnImage: bool\n        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param InvoiceDetectInfos: 检测出的票据类型列表，具体内容请点击左侧链接。\n        :type InvoiceDetectInfos: list of InvoiceDetectInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Code: 识别结果。
OK：表示识别成功；FailedOperation.UnsupportedInvioce：表示不支持识别；
FailedOperation.UnKnowError：表示识别失败；
其它错误码见各个票据接口的定义。\n        :type Code: str\n        :param Type: 识别出的图片所属的票据类型。
-1：未知类型
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
13：过路过桥费发票\n        :type Type: int\n        :param Rect: 识别出的图片在混贴票据图片中的位置信息。与Angel结合可以得出原图位置，组成RotatedRect((X+0.5\*Width,Y+0.5\*Height), (Width, Height), Angle)，详情可参考OpenCV文档。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        :param Angle: 识别出的图片在混贴票据图片中的旋转角度。\n        :type Angle: float\n        :param SingleInvoiceInfos: 识别到的内容。\n        :type SingleInvoiceInfos: list of SingleInvoiceInfo\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param Types: 需要识别的票据类型列表，为空或不填表示识别全部类型。
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
13：过路过桥费发票\n        :type Types: list of int\n        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Types = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Types = params.get("Types")
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
        """
        :param MixedInvoiceItems: 混贴票据识别结果，具体内容请点击左侧链接。\n        :type MixedInvoiceItems: list of MixedInvoiceItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class OrgCodeCertOCRRequest(AbstractModel):
    """OrgCodeCertOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param OrgCode: 代码\n        :type OrgCode: str\n        :param Name: 机构名称\n        :type Name: str\n        :param Address: 地址\n        :type Address: str\n        :param ValidDate: 有效期\n        :type ValidDate: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class PassportOCRRequest(AbstractModel):
    """PassportOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        :param Type: 默认填写CN
支持中国大陆地区护照。\n        :type Type: str\n        """
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
        """
        :param Country: 国家码\n        :type Country: str\n        :param PassportNo: 护照号\n        :type PassportNo: str\n        :param Sex: 性别\n        :type Sex: str\n        :param Nationality: 国籍\n        :type Nationality: str\n        :param BirthDate: 出生日期\n        :type BirthDate: str\n        :param BirthPlace: 出生地点\n        :type BirthPlace: str\n        :param IssueDate: 签发日期\n        :type IssueDate: str\n        :param IssuePlace: 签发地点\n        :type IssuePlace: str\n        :param ExpiryDate: 有效期\n        :type ExpiryDate: str\n        :param Signature: 持证人签名\n        :type Signature: str\n        :param CodeSet: 最下方第一行 MRZ Code 序列\n        :type CodeSet: str\n        :param CodeCrc: 最下方第二行 MRZ Code 序列\n        :type CodeCrc: str\n        :param Name: 姓名\n        :type Name: str\n        :param FamilyName: 姓\n        :type FamilyName: str\n        :param FirstName: 名\n        :type FirstName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param Name: 姓名\n        :type Name: str\n        :param EnglishName: 英文姓名\n        :type EnglishName: str\n        :param Number: 证件号\n        :type Number: str\n        :param Sex: 性别\n        :type Sex: str\n        :param ValidDate: 有效期限\n        :type ValidDate: str\n        :param IssueAuthority: 签发机关\n        :type IssueAuthority: str\n        :param IssueAddress: 签发地点\n        :type IssueAddress: str\n        :param Birthday: 出生日期\n        :type Birthday: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param LeftTop: 左上顶点坐标\n        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        :param RightTop: 右上顶点坐标\n        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        :param RightBottom: 右下顶点坐标\n        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        :param LeftBottom: 左下顶点坐标\n        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        """
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
        """
        :param ProductName: 产品名称\n        :type ProductName: str\n        :param EnName: 产品名称(英文)\n        :type EnName: str\n        :param BrandName: 品牌名称\n        :type BrandName: str\n        :param Type: 规格型号\n        :type Type: str\n        :param Width: 宽度，单位毫米\n        :type Width: str\n        :param Height: 高度，单位毫米\n        :type Height: str\n        :param Depth: 深度，单位毫米\n        :type Depth: str\n        :param KeyWord: 关键字\n        :type KeyWord: str\n        :param Description: 简短描述\n        :type Description: str\n        :param ImageLink: 图片链接\n        :type ImageLink: list of str\n        :param ManufacturerName: 厂家名称\n        :type ManufacturerName: str\n        :param ManufacturerAddress: 厂家地址\n        :type ManufacturerAddress: str\n        :param FirmCode: 企业社会信用代码\n        :type FirmCode: str\n        :param CheckResult: 表示数据查询状态
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
E008	        经查，该企业厂商识别代码以及条码尚未通报\n        :type CheckResult: str\n        :param CategoryCode: UNSPSC分类码\n        :type CategoryCode: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param Owner: 房地产权利人\n        :type Owner: str\n        :param Possession: 共有情况\n        :type Possession: str\n        :param RegisterTime: 登记时间\n        :type RegisterTime: str\n        :param Purpose: 规划用途\n        :type Purpose: str\n        :param Nature: 房屋性质\n        :type Nature: str\n        :param Location: 房地坐落\n        :type Location: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Wide: 宽\n        :type Wide: int\n        :param High: 高\n        :type High: int\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，支持PNG、JPG、JPEG格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，支持PNG、JPG、JPEG格式。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        """
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
        """
        :param CodeResults: 二维码/条形码识别结果信息，具体内容请点击左侧链接。\n        :type CodeResults: list of QrcodeResultsInfo\n        :param ImgSize: 图片大小，具体内容请点击左侧链接。\n        :type ImgSize: :class:`tencentcloud.ocr.v20181119.models.QrcodeImgSize`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param LeftTop: 左上顶点坐标（如果是条形码，X和Y都为-1）\n        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        :param RightTop: 右上顶点坐标（如果是条形码，X和Y都为-1）\n        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        :param RightBottom: 右下顶点坐标（如果是条形码，X和Y都为-1）\n        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        :param LeftBottom: 左下顶点坐标（如果是条形码，X和Y都为-1）\n        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`\n        """
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
        """
        :param TypeName: 类型（二维码、条形码）\n        :type TypeName: str\n        :param Url: 二维码/条形码包含的地址\n        :type Url: str\n        :param Position: 二维码/条形码坐标（二维码会返回位置坐标，条形码暂不返回位置坐标，因此默认X和Y返回值均为-1）\n        :type Position: :class:`tencentcloud.ocr.v20181119.models.QrcodePositionObj`\n        """
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
        """
        :param BarCode: 条形码\n        :type BarCode: str\n        """
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
        """
        :param BarCode: 条码\n        :type BarCode: str\n        :param ProductDataRecords: 条码信息数组\n        :type ProductDataRecords: list of ProductDataRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param QuestionArr: 数学试题识别结构化信息数组\n        :type QuestionArr: list of QuestionObj\n        :param QuestionBboxCoord: 题目主体区域检测框在图片中的像素坐标\n        :type QuestionBboxCoord: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param QuestionTextNo: 题号\n        :type QuestionTextNo: str\n        :param QuestionTextType: 题型：
1: "选择题"
2: "填空题"
3: "解答题"\n        :type QuestionTextType: int\n        :param QuestionText: 题干\n        :type QuestionText: str\n        :param QuestionOptions: 选择题选项，包含1个或多个option\n        :type QuestionOptions: str\n        :param QuestionSubquestion: 所有子题的question属性\n        :type QuestionSubquestion: str\n        :param QuestionImageCoords: 示意图检测框在的图片中的像素坐标\n        :type QuestionImageCoords: list of Rect\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param InvoiceNum: 发票号码\n        :type InvoiceNum: str\n        :param InvoiceCode: 发票代码\n        :type InvoiceCode: str\n        :param Rate: 大写金额\n        :type Rate: str\n        :param RateNum: 小写金额\n        :type RateNum: str\n        :param InvoiceType: 发票消费类型\n        :type InvoiceType: str\n        :param Province: 省
注意：此字段可能返回 null，表示取不到有效值。\n        :type Province: str\n        :param City: 市
注意：此字段可能返回 null，表示取不到有效值。\n        :type City: str\n        :param HasStamp: 是否有公司印章（1有 0无 空为识别不出）
注意：此字段可能返回 null，表示取不到有效值。\n        :type HasStamp: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class RecognizeTableOCRRequest(AbstractModel):
    """RecognizeTableOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片/PDF的 Base64 值。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片/PDF的 Url 地址。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。\n        :type IsPdf: bool\n        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。\n        :type PdfPageNumber: int\n        :param TableLanguage: 语言，zh：中英文（默认）jap：日文\n        :type TableLanguage: str\n        """
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
        """
        :param TableDetections: 检测到的文本信息，具体内容请点击左侧链接。\n        :type TableDetections: list of TableDetectInfo\n        :param Data: Base64 编码后的 Excel 数据。\n        :type Data: str\n        :param PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0\n        :type PdfPageSize: int\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，统一以逆时针方向旋转，逆时针为负，角度范围为-360°至0°。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        """
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
        """
        :param ID: 身份证号码\n        :type ID: str\n        :param ThaiName: 泰文姓名\n        :type ThaiName: str\n        :param EnFirstName: 英文姓名\n        :type EnFirstName: str\n        :param Address: 地址\n        :type Address: str\n        :param Birthday: 出生日期\n        :type Birthday: str\n        :param IssueDate: 首次领用日期\n        :type IssueDate: str\n        :param ExpirationDate: 签发日期\n        :type ExpirationDate: str\n        :param EnLastName: 英文姓名\n        :type EnLastName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class Rect(AbstractModel):
    """矩形坐标

    """

    def __init__(self):
        """
        :param X: 左上角x\n        :type X: int\n        :param Y: 左上角y\n        :type Y: int\n        :param Width: 宽度\n        :type Width: int\n        :param Height: 高度\n        :type Height: int\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param HouseholdNumber: 户号\n        :type HouseholdNumber: str\n        :param Name: 姓名\n        :type Name: str\n        :param Sex: 性别\n        :type Sex: str\n        :param BirthPlace: 出生地\n        :type BirthPlace: str\n        :param Nation: 民族\n        :type Nation: str\n        :param NativePlace: 籍贯\n        :type NativePlace: str\n        :param BirthDate: 出生日期\n        :type BirthDate: str\n        :param IdCardNumber: 公民身份证件编号\n        :type IdCardNumber: str\n        :param EducationDegree: 文化程度\n        :type EducationDegree: str\n        :param ServicePlace: 服务处所\n        :type ServicePlace: str\n        :param Household: 户别\n        :type Household: str\n        :param Address: 住址\n        :type Address: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class RideHailingDriverLicenseOCRRequest(AbstractModel):
    """RideHailingDriverLicenseOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        """
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
        """
        :param Name: 姓名\n        :type Name: str\n        :param LicenseNumber: 证号，对应网约车驾驶证字段：证号/从业资格证号/驾驶员证号/身份证号\n        :type LicenseNumber: str\n        :param StartDate: 有效起始日期\n        :type StartDate: str\n        :param EndDate: 有效期截止时间，对应网约车驾驶证字段：有效期至/营运期限止\n        :type EndDate: str\n        :param ReleaseDate: 初始发证日期，对应网约车驾驶证字段：初始领证日期/发证日期\n        :type ReleaseDate: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        """
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
        """
        :param OperationLicenseNumber: 交运管许可字号。\n        :type OperationLicenseNumber: str\n        :param VehicleOwner: 车辆所有人，对应网约车运输证字段：车辆所有人/车主名称/业户名称。\n        :type VehicleOwner: str\n        :param VehicleNumber: 车牌号码，对应网约车运输证字段：车牌号码/车辆号牌。\n        :type VehicleNumber: str\n        :param StartDate: 有效起始日期。\n        :type StartDate: str\n        :param EndDate: 有效期截止时间，对应网约车运输证字段：有效期至/营运期限止。\n        :type EndDate: str\n        :param ReleaseDate: 初始发证日期，对应网约车运输证字段：初始领证日期/发证日期。\n        :type ReleaseDate: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class SealOCRRequest(AbstractModel):
    """SealOCR请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        """
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
        """
        :param SealBody: 印章内容\n        :type SealBody: str\n        :param Location: 印章坐标\n        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        :param OtherTexts: 其它文本内容\n        :type OtherTexts: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SealBody = None
        self.Location = None
        self.OtherTexts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self.Location = Rect()
            self.Location._deserialize(params.get("Location"))
        self.OtherTexts = params.get("OtherTexts")
        self.RequestId = params.get("RequestId")


class ShipInvoiceInfo(AbstractModel):
    """轮船票字段信息

    """

    def __init__(self):
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、发票号码、日期、票价、始发地、目的地、姓名、时间、发票消费类型、省、市、币种。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param ShipInvoiceInfos: 轮船票识别结果，具体内容请点击左侧链接。\n        :type ShipInvoiceInfos: list of ShipInvoiceInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。\n        :type Value: str\n        """
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
        


class TableCell(AbstractModel):
    """单元格数据

    """

    def __init__(self):
        """
        :param ColTl: 单元格左上角的列索引\n        :type ColTl: int\n        :param RowTl: 单元格左上角的行索引\n        :type RowTl: int\n        :param ColBr: 单元格右下角的列索引\n        :type ColBr: int\n        :param RowBr: 单元格右下角的行索引\n        :type RowBr: int\n        :param Text: 单元格内识别出的字符串文本，若文本存在多行，以换行符"\n"隔开\n        :type Text: str\n        :param Type: 单元格类型\n        :type Type: str\n        :param Confidence: 单元格置信度\n        :type Confidence: float\n        :param Polygon: 单元格在图像中的四点坐标\n        :type Polygon: list of Coord\n        :param AdvancedInfo: 此字段为扩展字段
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdvancedInfo: str\n        :param Contents: 单元格文本属性\n        :type Contents: list of CellContent\n        """
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
        """
        :param Cells: 单元格内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cells: list of TableCell\n        :param Titles: 表格标题
注意：此字段可能返回 null，表示取不到有效值。\n        :type Titles: list of TableTitle\n        :param Type: 图像中的文本块类型，0 为非表格文本，
1 为有线表格，2 为无线表格
（接口暂不支持日文无线表格识别，若传入日文无线表格，返回0）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param TableCoordPoint: 表格主体四个顶点坐标（依次为左上角，
右上角，右下角，左下角）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableCoordPoint: list of Coord\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接\n        :type TextDetections: list of TextTable\n        :param Data: Base64 编码后的 Excel 数据。\n        :type Data: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Text: 表格名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param InvoiceNum: 发票代码\n        :type InvoiceNum: str\n        :param InvoiceCode: 发票号码\n        :type InvoiceCode: str\n        :param Date: 日期\n        :type Date: str\n        :param Fare: 金额\n        :type Fare: str\n        :param GetOnTime: 上车时间\n        :type GetOnTime: str\n        :param GetOffTime: 下车时间\n        :type GetOffTime: str\n        :param Distance: 里程\n        :type Distance: str\n        :param Location: 发票所在地\n        :type Location: str\n        :param PlateNumber: 车牌号\n        :type PlateNumber: str\n        :param InvoiceType: 发票消费类型\n        :type InvoiceType: str\n        :param Province: 省
注意：此字段可能返回 null，表示取不到有效值。\n        :type Province: str\n        :param City: 市
注意：此字段可能返回 null，表示取不到有效值。\n        :type City: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param DetectedText: 识别出的文本行内容\n        :type DetectedText: str\n        :param Result: 算式运算结果，true-正确   false-错误或非法参数\n        :type Result: bool\n        :param Confidence: 保留字段，暂不支持\n        :type Confidence: int\n        :param Polygon: 原图文本行坐标，以四个顶点坐标表示（保留字段，暂不支持）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Polygon: list of Coord\n        :param AdvancedInfo: 保留字段，暂不支持\n        :type AdvancedInfo: str\n        :param ItemCoord: 文本行旋转纠正之后在图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）\n        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`\n        :param ExpressionType: 算式题型编号：
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
‘11’: 解方程\n        :type ExpressionType: str\n        :param Answer: 错题推荐答案，算式运算结果正确返回为""，算式运算结果错误返回推荐答案 (注：暂不支持多个关系运算符（如1<10<7）、无关系运算符（如frac(1,2)+frac(2,3)）、单位换算（如1元=100角）错题的推荐答案返回)\n        :type Answer: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param HasText: 图片中是否包含文字。\n        :type HasText: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.HasText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HasText = params.get("HasText")
        self.RequestId = params.get("RequestId")


class TextDetection(AbstractModel):
    """文字识别结果

    """

    def __init__(self):
        """
        :param DetectedText: 识别出的文本行内容\n        :type DetectedText: str\n        :param Confidence: 置信度 0 ~100\n        :type Confidence: int\n        :param Polygon: 文本行坐标，以四个顶点坐标表示
注意：此字段可能返回 null，表示取不到有效值。\n        :type Polygon: list of Coord\n        :param AdvancedInfo: 此字段为扩展字段。
GeneralBasicOcr接口返回段落信息Parag，包含ParagNo。\n        :type AdvancedInfo: str\n        :param ItemPolygon: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）\n        :type ItemPolygon: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`\n        :param Words: 识别出来的单字信息包括单字（包括单字Character和单字置信度confidence）， 支持识别的接口：GeneralBasicOCR、GeneralAccurateOCR\n        :type Words: list of DetectedWords\n        :param WordCoordPoint: 单字在原图中的四点坐标， 支持识别的接口：GeneralBasicOCR、GeneralAccurateOCR\n        :type WordCoordPoint: list of DetectedWordCoordPoint\n        """
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
        """
        :param DetectedText: 识别出的文本行内容。\n        :type DetectedText: str\n        :param Confidence: 置信度 0 ~100。\n        :type Confidence: int\n        :param Polygon: 文本行在原图中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Polygon: list of Coord\n        :param AdvancedInfo: 此字段为扩展字段。目前EnglishOCR接口返回内容为空。\n        :type AdvancedInfo: str\n        :param WordCoordPoint: 英文单词在原图中的四点坐标。\n        :type WordCoordPoint: list of WordCoordPoint\n        :param CandWord: 候选字符集(包含候选字Character以及置信度Confidence)。\n        :type CandWord: list of CandWord\n        :param Words: 识别出来的单词信息（包括单词Character和单词置信度confidence）\n        :type Words: list of Words\n        """
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
        


class TextEduPaper(AbstractModel):
    """数学试题识别结果

    """

    def __init__(self):
        """
        :param Item: 识别出的字段名称（关键字）\n        :type Item: str\n        :param DetectedText: 识别出的字段名称对应的值，也就是字段Item对应的字符串结果\n        :type DetectedText: str\n        :param Itemcoord: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）\n        :type Itemcoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`\n        """
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
        """
        :param DetectedText: 识别出的文本行内容\n        :type DetectedText: str\n        """
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
        """
        :param DetectedText: 识别出的文本行内容\n        :type DetectedText: str\n        :param Confidence: 置信度 0 - 100\n        :type Confidence: int\n        :param Polygon: 文本行坐标，以四个顶点坐标表示\n        :type Polygon: list of Coord\n        :param AdvancedInfo: 此字段为扩展字段。
能返回文本行的段落信息，例如：{\"Parag\":{\"ParagNo\":2}}，
其中ParagNo为段落行，从1开始。\n        :type AdvancedInfo: str\n        :param WordPolygon: 字的坐标数组，以四个顶点坐标表示
注意：此字段可能返回 null，表示取不到有效值。\n        :type WordPolygon: list of Polygon\n        """
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
        """
        :param ColTl: 单元格左上角的列索引\n        :type ColTl: int\n        :param RowTl: 单元格左上角的行索引\n        :type RowTl: int\n        :param ColBr: 单元格右下角的列索引\n        :type ColBr: int\n        :param RowBr: 单元格右下角的行索引\n        :type RowBr: int\n        :param Text: 单元格文字\n        :type Text: str\n        :param Type: 单元格类型，包含body（表格主体）、header（表头）、footer（表尾）三种\n        :type Type: str\n        :param Confidence: 置信度 0 ~100\n        :type Confidence: int\n        :param Polygon: 文本行坐标，以四个顶点坐标表示\n        :type Polygon: list of Coord\n        :param AdvancedInfo: 此字段为扩展字段\n        :type AdvancedInfo: str\n        """
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
        """
        :param Name: 识别出的字段名称（关键字）。支持以下字段的识别：
发票代码、 发票号码、 打印发票代码、 打印发票号码、 开票日期、 购买方识别号、 小写金额、 价税合计(大写)、 销售方识别号、 校验码、 购买方名称、 销售方名称、 税额、 复核、 联次名称、 备注、 联次、 密码区、 开票人、 收款人、 （货物或应税劳务、服务名称）、省、 市、 服务类型、 通行费标志、 是否代开、 是否收购、 合计金额、 是否有公司印章、 发票消费类型、 车船税、 机器编号、 成品油标志、 税率、 合计税额、 （购买方地址、电话）、 （销售方地址、电话）、 单价、 金额、 销售方开户行及账号、 购买方开户行及账号、 规格型号、 发票名称、 单位、 数量、 校验码备选、 校验码后六位备选、发票号码备选、车牌号、类型、通行日期起、通行日期止、发票类型。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Polygon: 字段在原图中的中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`\n        """
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
        """
        :param PlateNo: 号牌号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlateNo: str\n        :param FileNo: 档案编号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileNo: str\n        :param AllowNum: 核定人数
注意：此字段可能返回 null，表示取不到有效值。\n        :type AllowNum: str\n        :param TotalMass: 总质量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalMass: str\n        :param CurbWeight: 整备质量
注意：此字段可能返回 null，表示取不到有效值。\n        :type CurbWeight: str\n        :param LoadQuality: 核定载质量
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadQuality: str\n        :param ExternalSize: 外廓尺寸
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalSize: str\n        :param Marks: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Marks: str\n        :param Record: 检验记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type Record: str\n        :param TotalQuasiMass: 准牵引总质量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalQuasiMass: str\n        """
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
        """
        :param PlateNo: 号牌号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlateNo: str\n        :param VehicleType: 车辆类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type VehicleType: str\n        :param Owner: 所有人
注意：此字段可能返回 null，表示取不到有效值。\n        :type Owner: str\n        :param Address: 住址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Address: str\n        :param UseCharacter: 使用性质
注意：此字段可能返回 null，表示取不到有效值。\n        :type UseCharacter: str\n        :param Model: 品牌型号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Model: str\n        :param Vin: 车辆识别代号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vin: str\n        :param EngineNo: 发动机号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type EngineNo: str\n        :param RegisterDate: 注册日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegisterDate: str\n        :param IssueDate: 发证日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type IssueDate: str\n        :param Seal: 印章
注意：此字段可能返回 null，表示取不到有效值。\n        :type Seal: str\n        """
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
        """
        :param RecName: 收件人姓名\n        :type RecName: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`\n        :param RecNum: 收件人手机号\n        :type RecNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`\n        :param RecAddr: 收件人地址\n        :type RecAddr: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`\n        :param SenderName: 寄件人姓名\n        :type SenderName: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`\n        :param SenderNum: 寄件人手机号\n        :type SenderNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`\n        :param SenderAddr: 寄件人地址\n        :type SenderAddr: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`\n        :param WaybillNum: 运单号\n        :type WaybillNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`\n        """
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
        """
        :param Name: 识别出的字段名称（关键字）。支持以下字段的识别：
发票代码、发票号码、日期、金额、入口、出口、时间、发票消费类型、高速标志。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param TollInvoiceInfos: 过路过桥费发票识别结果，具体内容请点击左侧链接。\n        :type TollInvoiceInfos: list of TollInvoiceInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param TicketNum: 编号\n        :type TicketNum: str\n        :param StartStation: 出发站\n        :type StartStation: str\n        :param DestinationStation: 到达站\n        :type DestinationStation: str\n        :param Date: 出发时间\n        :type Date: str\n        :param TrainNum: 车次\n        :type TrainNum: str\n        :param Seat: 座位号\n        :type Seat: str\n        :param Name: 姓名\n        :type Name: str\n        :param Price: 票价\n        :type Price: str\n        :param SeatCategory: 席别\n        :type SeatCategory: str\n        :param ID: 身份证号\n        :type ID: str\n        :param InvoiceType: 发票消费类型：交通\n        :type InvoiceType: str\n        :param SerialNumber: 序列号\n        :type SerialNumber: str\n        :param AdditionalCost: 加收票价\n        :type AdditionalCost: str\n        :param HandlingFee: 手续费\n        :type HandlingFee: str\n        :param LegalAmount: 大写金额（票面有大写金额该字段才有值）\n        :type LegalAmount: str\n        :param TicketStation: 售票站\n        :type TicketStation: str\n        :param OriginalPrice: 原票价（一般有手续费的才有原始票价字段）\n        :type OriginalPrice: str\n        :param InvoiceStyle: 发票类型：火车票、火车票补票、火车票退票凭证\n        :type InvoiceStyle: str\n        :param ReceiptNumber: 收据号码\n        :type ReceiptNumber: str\n        :param IsReceipt: 仅供报销使用：1为是，0为否\n        :type IsReceipt: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TaxBureau: 所属税局\n        :type TaxBureau: str\n        :param Buyer: 买方单位/个人\n        :type Buyer: str\n        :param BuyerNo: 买方单位代码/身份证号码\n        :type BuyerNo: str\n        :param BuyerAddress: 买方单位/个人地址\n        :type BuyerAddress: str\n        :param BuyerTel: 买方单位电话\n        :type BuyerTel: str\n        :param Seller: 卖方单位/个人\n        :type Seller: str\n        :param SellerNo: 卖方单位代码/身份证号码\n        :type SellerNo: str\n        :param SellerAddress: 卖方单位/个人地址\n        :type SellerAddress: str\n        :param SellerTel: 卖方单位电话\n        :type SellerTel: str\n        :param VehicleLicenseNo: 车牌照号\n        :type VehicleLicenseNo: str\n        :param RegisterNo: 登记证号\n        :type RegisterNo: str\n        :param VehicleIdentifyNo: 车架号/车辆识别代码\n        :type VehicleIdentifyNo: str\n        :param ManagementOffice: 转入地车辆管理所名称\n        :type ManagementOffice: str\n        :param VehicleTotalPrice: 车价合计\n        :type VehicleTotalPrice: str\n        :param Auctioneer: 经营、拍卖单位\n        :type Auctioneer: str\n        :param AuctioneerAddress: 经营、拍卖单位地址\n        :type AuctioneerAddress: str\n        :param AuctioneerTaxpayerNum: 经营、拍卖单位纳税人识别号\n        :type AuctioneerTaxpayerNum: str\n        :param AuctioneerBankAccount: 经营、拍卖单位开户银行、账号\n        :type AuctioneerBankAccount: str\n        :param AuctioneerTel: 经营、拍卖单位电话\n        :type AuctioneerTel: str\n        :param Market: 二手车市场\n        :type Market: str\n        :param MarketTaxpayerNum: 二手车市场纳税人识别号\n        :type MarketTaxpayerNum: str\n        :param MarketAddress: 二手车市场地址\n        :type MarketAddress: str\n        :param MarketBankAccount: 二手车市场开户银行账号\n        :type MarketBankAccount: str\n        :param MarketTel: 二手车市场电话\n        :type MarketTel: str\n        """
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
        """
        :param Code: 发票代码\n        :type Code: str\n        :param Number: 发票号码\n        :type Number: str\n        :param Date: 开票日期\n        :type Date: str\n        :param BuyerName: 购方抬头\n        :type BuyerName: str\n        :param BuyerTaxCode: 购方税号\n        :type BuyerTaxCode: str\n        :param BuyerAddressPhone: 购方地址电话\n        :type BuyerAddressPhone: str\n        :param BuyerBankAccount: 购方银行账号\n        :type BuyerBankAccount: str\n        :param SellerName: 销方名称\n        :type SellerName: str\n        :param SellerTaxCode: 销方税号\n        :type SellerTaxCode: str\n        :param SellerAddressPhone: 销方地址电话\n        :type SellerAddressPhone: str\n        :param SellerBankAccount: 销方银行账号\n        :type SellerBankAccount: str\n        :param Remark: 备注\n        :type Remark: str\n        :param MachineNo: 机器编码\n        :type MachineNo: str\n        :param Type: 发票类型
01：专用发票 
02：货运发票
03：机动车发票 
04：普通发票 
10：电子发票 
11：卷式发票 
14：通行费发票 
15：二手车发票\n        :type Type: str\n        :param CheckCode: 检验码\n        :type CheckCode: str\n        :param IsAbandoned: 是否作废（红冲）是否作废（红冲）
Y: 已作废 N：未作废 H：红冲\n        :type IsAbandoned: str\n        :param HasSellerList: 是否有销货清单 
Y: 有清单 N：无清单 
卷票无\n        :type HasSellerList: str\n        :param SellerListTitle: 销货清单标题\n        :type SellerListTitle: str\n        :param SellerListTax: 销货清单税额\n        :type SellerListTax: str\n        :param AmountWithoutTax: 不含税金额\n        :type AmountWithoutTax: str\n        :param TaxAmount: 税额\n        :type TaxAmount: str\n        :param AmountWithTax: 含税金额\n        :type AmountWithTax: str\n        :param Items: 项目明细\n        :type Items: list of VatInvoiceItem\n        """
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
        """
        :param Item: 项目名称\n        :type Item: str\n        :param Specification: 规格型号\n        :type Specification: str\n        :param MeasurementDimension: 单位\n        :type MeasurementDimension: str\n        :param Price: 价格\n        :type Price: str\n        :param Quantity: 数量\n        :type Quantity: str\n        :param Amount: 金额\n        :type Amount: str\n        :param TaxScheme: 税率(如6%、免税)\n        :type TaxScheme: str\n        :param TaxAmount: 税额\n        :type TaxAmount: str\n        """
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
        """
        :param LineNo: 行号\n        :type LineNo: str\n        :param Name: 名称\n        :type Name: str\n        :param Spec: 规格\n        :type Spec: str\n        :param Unit: 单位\n        :type Unit: str\n        :param Quantity: 数量\n        :type Quantity: str\n        :param UnitPrice: 单价\n        :type UnitPrice: str\n        :param AmountWithoutTax: 不含税金额\n        :type AmountWithoutTax: str\n        :param TaxRate: 税率\n        :type TaxRate: str\n        :param TaxAmount: 税额\n        :type TaxAmount: str\n        """
        self.LineNo = None
        self.Name = None
        self.Spec = None
        self.Unit = None
        self.Quantity = None
        self.UnitPrice = None
        self.AmountWithoutTax = None
        self.TaxRate = None
        self.TaxAmount = None


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
        """
        :param ImageBase64: 图片/PDF的 Base64 值。
支持的文件格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片/PDF大小：所下载文件经Base64编码后不超过 7M。文件下载时间不超过 3 秒。
输入参数 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片/PDF的 Url 地址。
支持的文件格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片/PDF大小：所下载文件经 Base64 编码后不超过 7M。文件下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。\n        :type IsPdf: bool\n        :param PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。\n        :type PdfPageNumber: int\n        """
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
        """
        :param VatInvoiceInfos: 检测到的文本信息，具体内容请点击左侧链接。\n        :type VatInvoiceInfos: list of TextVatInvoice\n        :param Items: 明细条目。VatInvoiceInfos中关于明细项的具体条目。\n        :type Items: list of VatInvoiceItem\n        :param PdfPageSize: 默认值为0。如果图片为PDF时，返回PDF的总页数。\n        :type PdfPageSize: int\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 名称\n        :type Name: str\n        :param TaxId: 纳税人识别号\n        :type TaxId: str\n        :param AddrTel: 地 址、电 话\n        :type AddrTel: str\n        :param FinancialAccount: 开户行及账号\n        :type FinancialAccount: str\n        """
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
        


class VatInvoiceVerifyRequest(AbstractModel):
    """VatInvoiceVerify请求参数结构体

    """

    def __init__(self):
        """
        :param InvoiceCode: 发票代码， 一张发票一天只能查询5次。\n        :type InvoiceCode: str\n        :param InvoiceNo: 发票号码（8位）。\n        :type InvoiceNo: str\n        :param InvoiceDate: 开票日期（不支持当天发票查询，只支持一年以内），如：2019-12-20。\n        :type InvoiceDate: str\n        :param Additional: 金额/发票校验码后6位（根据票种传递对应值，如果报参数错误，请仔细检查每个票种对应的值）
增值税专用发票：开具金额（不含税）
增值税普通发票、增值税电子普通发票（含通行费发票）、增值税普通发票（卷票）：校验码后6位
机动车销售统一发票：不含税价
货物运输业增值税专用发票：合计金额
二手车销售统一发票：车价合计\n        :type Additional: str\n        """
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
        """
        :param Invoice: 增值税发票信息，详情请点击左侧链接。\n        :type Invoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoice`\n        :param VehicleInvoiceInfo: 机动车销售统一发票信息\n        :type VehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.VehicleInvoiceInfo`\n        :param UsedVehicleInvoiceInfo: 二手车销售统一发票信息\n        :type UsedVehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.UsedVehicleInvoiceInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、合计金额(小写)、合计金额(大写)、开票日期、发票号码、购买方识别号、销售方识别号、校验码、销售方名称、购买方名称、发票消费类型、省、市、是否有公司印章、服务类型、品名、种类。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。\n        :type Value: str\n        :param Rect: 文本行在旋转纠正之后的图像中的像素坐标。\n        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param VatRollInvoiceInfos: 增值税发票（卷票）识别结果，具体内容请点击左侧链接。\n        :type VatRollInvoiceInfos: list of VatRollInvoiceInfo\n        :param Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。\n        :type Angle: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param CarType: 车辆类型\n        :type CarType: str\n        :param PlateModel: 厂牌型号\n        :type PlateModel: str\n        :param ProduceAddress: 产地\n        :type ProduceAddress: str\n        :param CertificateNo: 合格证号\n        :type CertificateNo: str\n        :param ImportNo: 进口证明书号\n        :type ImportNo: str\n        :param VinNo: LSVCA2NP9HN0xxxxx\n        :type VinNo: str\n        :param PayTaxesNo: 完税证书号\n        :type PayTaxesNo: str\n        :param Tonnage: 吨位\n        :type Tonnage: str\n        :param LimitCount: 限乘人数\n        :type LimitCount: str\n        :param EngineNo: 发动机号码\n        :type EngineNo: str\n        :param BizCheckFormNo: 商检单号\n        :type BizCheckFormNo: str\n        :param TaxtationOrgCode: 主管税务机关代码\n        :type TaxtationOrgCode: str\n        :param TaxtationOrgName: 主管税务机关名称\n        :type TaxtationOrgName: str\n        :param MotorTaxRate: 税率\n        :type MotorTaxRate: str\n        :param MotorBankName: 开户行\n        :type MotorBankName: str\n        :param MotorBankAccount: 账号\n        :type MotorBankAccount: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。\n        :type ImageUrl: str\n        :param CardSide: FRONT 为行驶证主页正面（有红色印章的一面），
BACK 为行驶证副页正面（有号码号牌的一面）。
默认值为：FRONT。\n        :type CardSide: str\n        """
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
        """
        :param FrontInfo: 行驶证主页正面的识别结果，CardSide 为 FRONT。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleFront`\n        :param BackInfo: 行驶证副页正面的识别结果，CardSide 为 BACK。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleBack`\n        :param RecognizeWarnCode: Code 告警码列表和释义：
-9102 复印件告警
-9103 翻拍件告警
-9106 ps告警
注：告警码可以同时存在多个\n        :type RecognizeWarnCode: list of int\n        :param RecognizeWarnMsg: 告警码说明：
WARN_DRIVER_LICENSE_COPY_CARD 复印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
WARN_DRIVER_LICENSE_PS_CARD ps告警
注：告警信息可以同时存在多个\n        :type RecognizeWarnMsg: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
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
机动车登记证书编号、身份证明名称/号码、抵押权人姓名/名称、抵押登记日期。\n        :type Name: str\n        :param Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。\n        :type Value: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param VehicleRegCertInfos: 机动车登记证书识别结果，具体内容请点击左侧链接。\n        :type VehicleRegCertInfos: list of VehicleRegCertInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n        :type ImageBase64: str\n        :param ImageUrl: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n        :type ImageUrl: str\n        :param ImageConfig: 用于入参是营业执照图片的场景，表示需要校验的参数：RegNum（注册号或者统一社会信用代码），Name（企业名称），Address（经营地址）。选择后会返回相关参数校验结果。RegNum为必选，Name和Address可选。
格式为{RegNum: true, Name:true/false, Address:true/false}

设置方式参考：
Config = Json.stringify({"Name":true,"Address":true})
API 3.0 Explorer 设置方式参考：
Config = {"Name":true,"Address":true}\n        :type ImageConfig: str\n        :param RegNum: 用于入参是文本的场景，RegNum表示注册号或者统一社会信用代码。若没有传入营业执照图片，则RegNum为必选项，若图片和RegNum都传入，则只使用RegNum。\n        :type RegNum: str\n        :param Name: 用于入参是文本的场景，Name表示企业名称。Name为可选项，填写后会返回Name的校验结果。\n        :type Name: str\n        :param Address: 用于入参是文本的场景，Address表示经营地址。Address为可选项，填写后会返回Address的校验结果。\n        :type Address: str\n        :param RegCapital: 1表示输出注册资本字段（单位：万元），其他值表示不输出。默认不输出。\n        :type RegCapital: int\n        :param EstablishTime: true表示展示成立/注册日期\n        :type EstablishTime: bool\n        """
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
        """
        :param ErrorCode: 状态码，成功时返回0\n        :type ErrorCode: int\n        :param CreditCode: 统一社会信用代码\n        :type CreditCode: str\n        :param Opfrom: 经营期限自（YYYY-MM-DD）\n        :type Opfrom: str\n        :param Opto: 经营期限至（YYYY-MM-DD）\n        :type Opto: str\n        :param Frname: 法人姓名\n        :type Frname: str\n        :param Entstatus: 经营状态，包括：成立、筹建、存续、在营、开业、在册、正常经营、开业登记中、登记成立、撤销、撤销登记、非正常户、告解、个体暂时吊销、个体转企业、吊销（未注销）、拟注销、已注销、（待）迁入、（待）迁出、停业、歇业、清算等。\n        :type Entstatus: str\n        :param Zsopscope: 经营业务范围\n        :type Zsopscope: str\n        :param Reason: 查询的状态信息\n        :type Reason: str\n        :param Oriregno: 原注册号\n        :type Oriregno: str\n        :param VerifyRegno: 要核验的工商注册号\n        :type VerifyRegno: str\n        :param Regno: 工商注册号\n        :type Regno: str\n        :param VerifyEntname: 要核验的企业名称\n        :type VerifyEntname: str\n        :param Entname: 企业名称\n        :type Entname: str\n        :param VerifyDom: 要核验的住址\n        :type VerifyDom: str\n        :param Dom: 住址\n        :type Dom: str\n        :param RegNumResult: 验证结果\n        :type RegNumResult: :class:`tencentcloud.ocr.v20181119.models.BizLicenseVerifyResult`\n        :param RegCapital: 注册资本（单位：万元）,只有输入参数regCapital为1的时候才输出\n        :type RegCapital: str\n        :param EstablishTime: 成立/注册日期，只有输入参数EstablishTime为true时展示，默认为空\n        :type EstablishTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n        :type ImageBase64: str\n        :param ImageUrl: 用于入参是营业执照图片的场景，ImageBase64和ImageUrl必须提供一个，如果都提供，只使用 ImageUrl。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n        :type ImageUrl: str\n        :param ImageConfig: 用于入参是营业执照图片的场景，表示需要校验的参数：RegNum（注册号或者统一社会信用代码），Name（企业名称），Address（经营地址）。选择后会返回相关参数校验结果。RegNum为必选，Name和Address可选。
格式为{RegNum: true, Name:true/false, Address:true/false}

设置方式参考：
Config = Json.stringify({"Name":true,"Address":true})
API 3.0 Explorer 设置方式参考：
Config = {"Name":true,"Address":true}\n        :type ImageConfig: str\n        :param RegNum: 用于入参是文本的场景，RegNum表示注册号或者统一社会信用代码。若没有传入营业执照图片，则RegNum为必选项，若图片和RegNum都传入，则只使用RegNum。\n        :type RegNum: str\n        :param Name: 用于入参是文本的场景，Name表示企业名称。Name为可选项，填写后会返回Name的校验结果。\n        :type Name: str\n        :param Address: 用于入参是文本的场景，Address表示经营地址，填写后会返回Address的校验结果。\n        :type Address: str\n        """
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
        """
        :param ErrorCode: 状态码\n        :type ErrorCode: int\n        :param CreditCode: 统一社会信用代码\n        :type CreditCode: str\n        :param OrgCode: 组织机构代码\n        :type OrgCode: str\n        :param OpenFrom: 经营期限自（YYYY-MM-DD）\n        :type OpenFrom: str\n        :param OpenTo: 经营期限至（YYYY-MM-DD）\n        :type OpenTo: str\n        :param FrName: 法人姓名\n        :type FrName: str\n        :param EnterpriseStatus: 经营状态，包括：成立、筹建、存续、在营、开业、在册、正常经营、开业登记中、登记成立、撤销、撤销登记、非正常户、告解、个体暂时吊销、个体转企业、吊销（未注销）、拟注销、已注销、（待）迁入、（待）迁出、停业、歇业、清算等。\n        :type EnterpriseStatus: str\n        :param OperateScopeAndForm: 经营（业务）范围及方式\n        :type OperateScopeAndForm: str\n        :param RegCap: 注册资金（单位:万元）\n        :type RegCap: str\n        :param RegCapCur: 注册币种\n        :type RegCapCur: str\n        :param RegOrg: 登记机关\n        :type RegOrg: str\n        :param EsDate: 开业日期（YYYY-MM-DD）\n        :type EsDate: str\n        :param EnterpriseType: 企业（机构）类型\n        :type EnterpriseType: str\n        :param CancelDate: 注销日期\n        :type CancelDate: str\n        :param RevokeDate: 吊销日期\n        :type RevokeDate: str\n        :param AbuItem: 许可经营项目\n        :type AbuItem: str\n        :param CbuItem: 一般经营项目\n        :type CbuItem: str\n        :param ApprDate: 核准时间\n        :type ApprDate: str\n        :param Province: 省\n        :type Province: str\n        :param City: 地级市\n        :type City: str\n        :param County: 区\县\n        :type County: str\n        :param AreaCode: 住所所在行政区划代码\n        :type AreaCode: str\n        :param IndustryPhyCode: 行业门类代码\n        :type IndustryPhyCode: str\n        :param IndustryPhyName: 行业门类名称\n        :type IndustryPhyName: str\n        :param IndustryCode: 国民经济行业代码\n        :type IndustryCode: str\n        :param IndustryName: 国民经济行业名称\n        :type IndustryName: str\n        :param OperateScope: 经营（业务）范围\n        :type OperateScope: str\n        :param VerifyRegNo: 要核验的工商注册号\n        :type VerifyRegNo: str\n        :param RegNo: 工商注册号\n        :type RegNo: str\n        :param VerifyEnterpriseName: 要核验的企业名称\n        :type VerifyEnterpriseName: str\n        :param EnterpriseName: 企业名称\n        :type EnterpriseName: str\n        :param VerifyAddress: 要核验的注册地址\n        :type VerifyAddress: str\n        :param Address: 注册地址\n        :type Address: str\n        :param RegNumResult: 验证结果\n        :type RegNumResult: :class:`tencentcloud.ocr.v20181119.models.BizLicenseVerifyResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RealName: 姓名\n        :type RealName: str\n        :param IdCard: 证件号码（公司注册证件号）\n        :type IdCard: str\n        :param EnterpriseName: 企业全称\n        :type EnterpriseName: str\n        :param EnterpriseMark: 企业标识（注册号，统一社会信用代码）\n        :type EnterpriseMark: str\n        """
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
        """
        :param State: 核验一致性（1:一致，2:不一致）\n        :type State: int\n        :param Detail: 返回不一致时，返回明细，-22：姓名不一致，-23：证件号码不一致，-24：企业名称不一致，-25：企业标识不一致
注意：此字段可能返回 null，表示取不到有效值。\n        :type Detail: :class:`tencentcloud.ocr.v20181119.models.Detail`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param OfdFileUrl: OFD文件的 Url 地址。\n        :type OfdFileUrl: str\n        :param OfdFileBase64: OFD文件的 Base64 值。
OfdFileUrl 和 OfdFileBase64 必传其一，若两者都传，只解析OfdFileBase64。\n        :type OfdFileBase64: str\n        """
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
        """
        :param Type: 发票类型
026:增值税电子普通发票
028:增值税电子专用发票\n        :type Type: str\n        :param InvoiceCode: 发票代码\n        :type InvoiceCode: str\n        :param InvoiceNumber: 发票号码\n        :type InvoiceNumber: str\n        :param IssueDate: 开票日期\n        :type IssueDate: str\n        :param InvoiceCheckCode: 验证码\n        :type InvoiceCheckCode: str\n        :param MachineNumber: 机器编号\n        :type MachineNumber: str\n        :param TaxControlCode: 密码区\n        :type TaxControlCode: str\n        :param Buyer: 购买方\n        :type Buyer: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceUserInfo`\n        :param Seller: 销售方\n        :type Seller: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceUserInfo`\n        :param TaxInclusiveTotalAmount: 价税合计\n        :type TaxInclusiveTotalAmount: str\n        :param InvoiceClerk: 开票人\n        :type InvoiceClerk: str\n        :param Payee: 收款人\n        :type Payee: str\n        :param Checker: 复核人\n        :type Checker: str\n        :param TaxTotalAmount: 税额\n        :type TaxTotalAmount: str\n        :param TaxExclusiveTotalAmount: 不含税金额\n        :type TaxExclusiveTotalAmount: str\n        :param Note: 备注\n        :type Note: str\n        :param GoodsInfos: 货物或服务清单\n        :type GoodsInfos: list of VatInvoiceGoodsInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        """
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
        """
        :param Vin: 检测到的车辆 VIN 码。\n        :type Vin: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。\n        :type ImageBase64: str\n        :param ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。\n        :type ImageUrl: str\n        :param EnablePreDetect: 预检测开关，当待识别运单占整个输入图像的比例较小时，建议打开预检测开关。默认值为false。\n        :type EnablePreDetect: bool\n        """
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
        """
        :param TextDetections: 检测到的文本信息，具体内容请点击左侧链接。\n        :type TextDetections: :class:`tencentcloud.ocr.v20181119.models.TextWaybill`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Text: 识别出的文本行内容\n        :type Text: str\n        """
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
        """
        :param WordCoordinate: 英文OCR识别出的每个单词在原图中的四点坐标。\n        :type WordCoordinate: list of Coord\n        """
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
        """
        :param Confidence: 置信度 0 ~100\n        :type Confidence: int\n        :param Character: 候选字Character\n        :type Character: str\n        """
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
        