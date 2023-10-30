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
        :param _ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvertiseOCRResponse(AbstractModel):
    """AdvertiseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of AdvertiseTextDetection
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = AdvertiseTextDetection()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._RequestId = params.get("RequestId")


class AdvertiseTextDetection(AbstractModel):
    """广告文字识别结果

    """

    def __init__(self):
        r"""
        :param _DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param _Confidence: 置信度 0 ~100
        :type Confidence: int
        :param _Polygon: 文本行坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        :param _AdvancedInfo: 此字段为扩展字段。
GeneralBasicOcr接口返回段落信息Parag，包含ParagNo。
        :type AdvancedInfo: str
        """
        self._DetectedText = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AirTransport(AbstractModel):
    """机票行程单

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Number: 电子客票号码
        :type Number: str
        :param _CheckCode: 校验码
        :type CheckCode: str
        :param _SerialNumber: 印刷序号
        :type SerialNumber: str
        :param _Date: 开票日期
        :type Date: str
        :param _AgentCode: 销售单位代号
        :type AgentCode: str
        :param _AgentCodeFirst: 销售单位代号第一行
        :type AgentCodeFirst: str
        :param _AgentCodeSecond: 销售单位代号第二行
        :type AgentCodeSecond: str
        :param _UserName: 姓名
        :type UserName: str
        :param _UserID: 身份证号
        :type UserID: str
        :param _Issuer: 填开单位
        :type Issuer: str
        :param _Fare: 票价
        :type Fare: str
        :param _Tax: 合计税额
        :type Tax: str
        :param _FuelSurcharge: 燃油附加费
        :type FuelSurcharge: str
        :param _AirDevelopmentFund: 民航发展基金
        :type AirDevelopmentFund: str
        :param _Insurance: 保险费
        :type Insurance: str
        :param _Total: 合计金额（小写）
        :type Total: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _DomesticInternationalTag: 国内国际标签
        :type DomesticInternationalTag: str
        :param _DateStart: 客票生效日期
        :type DateStart: str
        :param _DateEnd: 有效截至日期
        :type DateEnd: str
        :param _Endorsement: 签注
        :type Endorsement: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _FlightItems: 条目
        :type FlightItems: list of FlightItem
        """
        self._Title = None
        self._Number = None
        self._CheckCode = None
        self._SerialNumber = None
        self._Date = None
        self._AgentCode = None
        self._AgentCodeFirst = None
        self._AgentCodeSecond = None
        self._UserName = None
        self._UserID = None
        self._Issuer = None
        self._Fare = None
        self._Tax = None
        self._FuelSurcharge = None
        self._AirDevelopmentFund = None
        self._Insurance = None
        self._Total = None
        self._Kind = None
        self._DomesticInternationalTag = None
        self._DateStart = None
        self._DateEnd = None
        self._Endorsement = None
        self._QRCodeMark = None
        self._FlightItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AgentCode(self):
        return self._AgentCode

    @AgentCode.setter
    def AgentCode(self, AgentCode):
        self._AgentCode = AgentCode

    @property
    def AgentCodeFirst(self):
        return self._AgentCodeFirst

    @AgentCodeFirst.setter
    def AgentCodeFirst(self, AgentCodeFirst):
        self._AgentCodeFirst = AgentCodeFirst

    @property
    def AgentCodeSecond(self):
        return self._AgentCodeSecond

    @AgentCodeSecond.setter
    def AgentCodeSecond(self, AgentCodeSecond):
        self._AgentCodeSecond = AgentCodeSecond

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Fare(self):
        return self._Fare

    @Fare.setter
    def Fare(self, Fare):
        self._Fare = Fare

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def FuelSurcharge(self):
        return self._FuelSurcharge

    @FuelSurcharge.setter
    def FuelSurcharge(self, FuelSurcharge):
        self._FuelSurcharge = FuelSurcharge

    @property
    def AirDevelopmentFund(self):
        return self._AirDevelopmentFund

    @AirDevelopmentFund.setter
    def AirDevelopmentFund(self, AirDevelopmentFund):
        self._AirDevelopmentFund = AirDevelopmentFund

    @property
    def Insurance(self):
        return self._Insurance

    @Insurance.setter
    def Insurance(self, Insurance):
        self._Insurance = Insurance

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def DomesticInternationalTag(self):
        return self._DomesticInternationalTag

    @DomesticInternationalTag.setter
    def DomesticInternationalTag(self, DomesticInternationalTag):
        self._DomesticInternationalTag = DomesticInternationalTag

    @property
    def DateStart(self):
        return self._DateStart

    @DateStart.setter
    def DateStart(self, DateStart):
        self._DateStart = DateStart

    @property
    def DateEnd(self):
        return self._DateEnd

    @DateEnd.setter
    def DateEnd(self, DateEnd):
        self._DateEnd = DateEnd

    @property
    def Endorsement(self):
        return self._Endorsement

    @Endorsement.setter
    def Endorsement(self, Endorsement):
        self._Endorsement = Endorsement

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def FlightItems(self):
        return self._FlightItems

    @FlightItems.setter
    def FlightItems(self, FlightItems):
        self._FlightItems = FlightItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._CheckCode = params.get("CheckCode")
        self._SerialNumber = params.get("SerialNumber")
        self._Date = params.get("Date")
        self._AgentCode = params.get("AgentCode")
        self._AgentCodeFirst = params.get("AgentCodeFirst")
        self._AgentCodeSecond = params.get("AgentCodeSecond")
        self._UserName = params.get("UserName")
        self._UserID = params.get("UserID")
        self._Issuer = params.get("Issuer")
        self._Fare = params.get("Fare")
        self._Tax = params.get("Tax")
        self._FuelSurcharge = params.get("FuelSurcharge")
        self._AirDevelopmentFund = params.get("AirDevelopmentFund")
        self._Insurance = params.get("Insurance")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._DomesticInternationalTag = params.get("DomesticInternationalTag")
        self._DateStart = params.get("DateStart")
        self._DateEnd = params.get("DateEnd")
        self._Endorsement = params.get("Endorsement")
        self._QRCodeMark = params.get("QRCodeMark")
        if params.get("FlightItems") is not None:
            self._FlightItems = []
            for item in params.get("FlightItems"):
                obj = FlightItem()
                obj._deserialize(item)
                self._FlightItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArithmeticOCRRequest(AbstractModel):
    """ArithmeticOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _SupportHorizontalImage: 用于选择是否支持横屏拍摄。打开则支持横屏拍摄图片角度判断，角度信息在返回参数的angle中，默认值为true
        :type SupportHorizontalImage: bool
        :param _RejectNonArithmeticPic: 是否拒绝非速算图，打开则拒绝非速算图(注：非速算图是指风景人物等明显不是速算图片的图片)，默认值为false
        :type RejectNonArithmeticPic: bool
        :param _EnableDispRelatedVertical: 是否展开耦合算式中的竖式计算，默认值为false
        :type EnableDispRelatedVertical: bool
        :param _EnableDispMidResult: 是否展示竖式算式的中间结果和格式控制字符，默认值为false
        :type EnableDispMidResult: bool
        :param _EnablePdfRecognize: 是否开启pdf识别，默认值为true
        :type EnablePdfRecognize: bool
        :param _PdfPageIndex: pdf页码，从0开始，默认为0
        :type PdfPageIndex: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._SupportHorizontalImage = None
        self._RejectNonArithmeticPic = None
        self._EnableDispRelatedVertical = None
        self._EnableDispMidResult = None
        self._EnablePdfRecognize = None
        self._PdfPageIndex = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def SupportHorizontalImage(self):
        return self._SupportHorizontalImage

    @SupportHorizontalImage.setter
    def SupportHorizontalImage(self, SupportHorizontalImage):
        self._SupportHorizontalImage = SupportHorizontalImage

    @property
    def RejectNonArithmeticPic(self):
        return self._RejectNonArithmeticPic

    @RejectNonArithmeticPic.setter
    def RejectNonArithmeticPic(self, RejectNonArithmeticPic):
        self._RejectNonArithmeticPic = RejectNonArithmeticPic

    @property
    def EnableDispRelatedVertical(self):
        return self._EnableDispRelatedVertical

    @EnableDispRelatedVertical.setter
    def EnableDispRelatedVertical(self, EnableDispRelatedVertical):
        self._EnableDispRelatedVertical = EnableDispRelatedVertical

    @property
    def EnableDispMidResult(self):
        return self._EnableDispMidResult

    @EnableDispMidResult.setter
    def EnableDispMidResult(self, EnableDispMidResult):
        self._EnableDispMidResult = EnableDispMidResult

    @property
    def EnablePdfRecognize(self):
        return self._EnablePdfRecognize

    @EnablePdfRecognize.setter
    def EnablePdfRecognize(self, EnablePdfRecognize):
        self._EnablePdfRecognize = EnablePdfRecognize

    @property
    def PdfPageIndex(self):
        return self._PdfPageIndex

    @PdfPageIndex.setter
    def PdfPageIndex(self, PdfPageIndex):
        self._PdfPageIndex = PdfPageIndex


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._SupportHorizontalImage = params.get("SupportHorizontalImage")
        self._RejectNonArithmeticPic = params.get("RejectNonArithmeticPic")
        self._EnableDispRelatedVertical = params.get("EnableDispRelatedVertical")
        self._EnableDispMidResult = params.get("EnableDispMidResult")
        self._EnablePdfRecognize = params.get("EnablePdfRecognize")
        self._PdfPageIndex = params.get("PdfPageIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArithmeticOCRResponse(AbstractModel):
    """ArithmeticOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextArithmetic
        :param _Angle: 图片横屏的角度(90度或270度)
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Angle = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextArithmetic()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class BankCardOCRRequest(AbstractModel):
    """BankCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param _RetBorderCutImage: 是否返回预处理（精确剪裁对齐）后的银行卡图片数据，默认false。
        :type RetBorderCutImage: bool
        :param _RetCardNoImage: 是否返回卡号的切图图片数据，默认false。
        :type RetCardNoImage: bool
        :param _EnableCopyCheck: 复印件检测开关，如果输入的图片是银行卡复印件图片则返回告警，默认false。
        :type EnableCopyCheck: bool
        :param _EnableReshootCheck: 翻拍检测开关，如果输入的图片是银行卡翻拍图片则返回告警，默认false。
        :type EnableReshootCheck: bool
        :param _EnableBorderCheck: 边框遮挡检测开关，如果输入的图片是银行卡边框被遮挡则返回告警，默认false。
        :type EnableBorderCheck: bool
        :param _EnableQualityValue: 是否返回图片质量分数（图片质量分数是评价一个图片的模糊程度的标准），默认false。
        :type EnableQualityValue: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._RetBorderCutImage = None
        self._RetCardNoImage = None
        self._EnableCopyCheck = None
        self._EnableReshootCheck = None
        self._EnableBorderCheck = None
        self._EnableQualityValue = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RetBorderCutImage(self):
        return self._RetBorderCutImage

    @RetBorderCutImage.setter
    def RetBorderCutImage(self, RetBorderCutImage):
        self._RetBorderCutImage = RetBorderCutImage

    @property
    def RetCardNoImage(self):
        return self._RetCardNoImage

    @RetCardNoImage.setter
    def RetCardNoImage(self, RetCardNoImage):
        self._RetCardNoImage = RetCardNoImage

    @property
    def EnableCopyCheck(self):
        return self._EnableCopyCheck

    @EnableCopyCheck.setter
    def EnableCopyCheck(self, EnableCopyCheck):
        self._EnableCopyCheck = EnableCopyCheck

    @property
    def EnableReshootCheck(self):
        return self._EnableReshootCheck

    @EnableReshootCheck.setter
    def EnableReshootCheck(self, EnableReshootCheck):
        self._EnableReshootCheck = EnableReshootCheck

    @property
    def EnableBorderCheck(self):
        return self._EnableBorderCheck

    @EnableBorderCheck.setter
    def EnableBorderCheck(self, EnableBorderCheck):
        self._EnableBorderCheck = EnableBorderCheck

    @property
    def EnableQualityValue(self):
        return self._EnableQualityValue

    @EnableQualityValue.setter
    def EnableQualityValue(self, EnableQualityValue):
        self._EnableQualityValue = EnableQualityValue


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._RetBorderCutImage = params.get("RetBorderCutImage")
        self._RetCardNoImage = params.get("RetCardNoImage")
        self._EnableCopyCheck = params.get("EnableCopyCheck")
        self._EnableReshootCheck = params.get("EnableReshootCheck")
        self._EnableBorderCheck = params.get("EnableBorderCheck")
        self._EnableQualityValue = params.get("EnableQualityValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardOCRResponse(AbstractModel):
    """BankCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CardNo: 卡号
        :type CardNo: str
        :param _BankInfo: 银行信息
        :type BankInfo: str
        :param _ValidDate: 有效期，格式如：07/2023
        :type ValidDate: str
        :param _CardType: 卡类型
        :type CardType: str
        :param _CardName: 卡名字
        :type CardName: str
        :param _BorderCutImage: 切片图片数据
注意：此字段可能返回 null，表示取不到有效值。
        :type BorderCutImage: str
        :param _CardNoImage: 卡号图片数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CardNoImage: str
        :param _WarningCode: WarningCode 告警码列表和释义：
-9110:银行卡日期无效; 
-9111:银行卡边框不完整; 
-9112:银行卡图片反光;
-9113:银行卡复印件;
-9114:银行卡翻拍件
（告警码可以同时存在多个）
注意：此字段可能返回 null，表示取不到有效值。
        :type WarningCode: list of int
        :param _QualityValue: 图片质量分数，请求EnableQualityValue时返回（取值范围：0-100，分数越低越模糊，建议阈值≥50）。
注意：此字段可能返回 null，表示取不到有效值。
        :type QualityValue: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CardNo = None
        self._BankInfo = None
        self._ValidDate = None
        self._CardType = None
        self._CardName = None
        self._BorderCutImage = None
        self._CardNoImage = None
        self._WarningCode = None
        self._QualityValue = None
        self._RequestId = None

    @property
    def CardNo(self):
        return self._CardNo

    @CardNo.setter
    def CardNo(self, CardNo):
        self._CardNo = CardNo

    @property
    def BankInfo(self):
        return self._BankInfo

    @BankInfo.setter
    def BankInfo(self, BankInfo):
        self._BankInfo = BankInfo

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def CardType(self):
        return self._CardType

    @CardType.setter
    def CardType(self, CardType):
        self._CardType = CardType

    @property
    def CardName(self):
        return self._CardName

    @CardName.setter
    def CardName(self, CardName):
        self._CardName = CardName

    @property
    def BorderCutImage(self):
        return self._BorderCutImage

    @BorderCutImage.setter
    def BorderCutImage(self, BorderCutImage):
        self._BorderCutImage = BorderCutImage

    @property
    def CardNoImage(self):
        return self._CardNoImage

    @CardNoImage.setter
    def CardNoImage(self, CardNoImage):
        self._CardNoImage = CardNoImage

    @property
    def WarningCode(self):
        return self._WarningCode

    @WarningCode.setter
    def WarningCode(self, WarningCode):
        self._WarningCode = WarningCode

    @property
    def QualityValue(self):
        return self._QualityValue

    @QualityValue.setter
    def QualityValue(self, QualityValue):
        self._QualityValue = QualityValue

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CardNo = params.get("CardNo")
        self._BankInfo = params.get("BankInfo")
        self._ValidDate = params.get("ValidDate")
        self._CardType = params.get("CardType")
        self._CardName = params.get("CardName")
        self._BorderCutImage = params.get("BorderCutImage")
        self._CardNoImage = params.get("CardNoImage")
        self._WarningCode = params.get("WarningCode")
        self._QualityValue = params.get("QualityValue")
        self._RequestId = params.get("RequestId")


class BankSlipInfo(AbstractModel):
    """银行回单识别出的字段

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
付款开户行、收款开户行、付款账号、收款账号、回单类型、回单编号、币种、流水号、凭证号码、交易机构、交易金额、手续费、日期等字段信息。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Value = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankSlipOCRRequest(AbstractModel):
    """BankSlipOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankSlipOCRResponse(AbstractModel):
    """BankSlipOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BankSlipInfos: 银行回单识别结果，具体内容请点击左侧链接。
        :type BankSlipInfos: list of BankSlipInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BankSlipInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def BankSlipInfos(self):
        return self._BankSlipInfos

    @BankSlipInfos.setter
    def BankSlipInfos(self, BankSlipInfos):
        self._BankSlipInfos = BankSlipInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BankSlipInfos") is not None:
            self._BankSlipInfos = []
            for item in params.get("BankSlipInfos"):
                obj = BankSlipInfo()
                obj._deserialize(item)
                self._BankSlipInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class BizLicenseOCRRequest(AbstractModel):
    """BizLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _EnableCopyWarn: 是否返回黑白复印件告警码，默认为false
        :type EnableCopyWarn: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._EnableCopyWarn = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def EnableCopyWarn(self):
        return self._EnableCopyWarn

    @EnableCopyWarn.setter
    def EnableCopyWarn(self, EnableCopyWarn):
        self._EnableCopyWarn = EnableCopyWarn


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._EnableCopyWarn = params.get("EnableCopyWarn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BizLicenseOCRResponse(AbstractModel):
    """BizLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegNum: 统一社会信用代码（三合一之前为注册号）
        :type RegNum: str
        :param _Name: 公司名称
        :type Name: str
        :param _Capital: 注册资本
        :type Capital: str
        :param _Person: 法定代表人
        :type Person: str
        :param _Address: 地址
        :type Address: str
        :param _Business: 经营范围
        :type Business: str
        :param _Type: 主体类型
        :type Type: str
        :param _Period: 营业期限
        :type Period: str
        :param _ComposingForm: 组成形式
        :type ComposingForm: str
        :param _SetDate: 成立日期
        :type SetDate: str
        :param _RecognizeWarnCode: Code 告警码列表和释义：
-9102 黑白复印件告警
-9104 翻拍件告警
        :type RecognizeWarnCode: list of int
        :param _RecognizeWarnMsg: 告警码说明：
WARN_COPY_CARD 黑白复印件告警
WARN_RESHOOT_SCREENED_CARD 翻拍件告警
        :type RecognizeWarnMsg: list of str
        :param _IsDuplication: 是否为副本。1为是，-1为不是。
        :type IsDuplication: int
        :param _RegistrationDate: 登记日期
        :type RegistrationDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegNum = None
        self._Name = None
        self._Capital = None
        self._Person = None
        self._Address = None
        self._Business = None
        self._Type = None
        self._Period = None
        self._ComposingForm = None
        self._SetDate = None
        self._RecognizeWarnCode = None
        self._RecognizeWarnMsg = None
        self._IsDuplication = None
        self._RegistrationDate = None
        self._RequestId = None

    @property
    def RegNum(self):
        return self._RegNum

    @RegNum.setter
    def RegNum(self, RegNum):
        self._RegNum = RegNum

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Capital(self):
        return self._Capital

    @Capital.setter
    def Capital(self, Capital):
        self._Capital = Capital

    @property
    def Person(self):
        return self._Person

    @Person.setter
    def Person(self, Person):
        self._Person = Person

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ComposingForm(self):
        return self._ComposingForm

    @ComposingForm.setter
    def ComposingForm(self, ComposingForm):
        self._ComposingForm = ComposingForm

    @property
    def SetDate(self):
        return self._SetDate

    @SetDate.setter
    def SetDate(self, SetDate):
        self._SetDate = SetDate

    @property
    def RecognizeWarnCode(self):
        return self._RecognizeWarnCode

    @RecognizeWarnCode.setter
    def RecognizeWarnCode(self, RecognizeWarnCode):
        self._RecognizeWarnCode = RecognizeWarnCode

    @property
    def RecognizeWarnMsg(self):
        return self._RecognizeWarnMsg

    @RecognizeWarnMsg.setter
    def RecognizeWarnMsg(self, RecognizeWarnMsg):
        self._RecognizeWarnMsg = RecognizeWarnMsg

    @property
    def IsDuplication(self):
        return self._IsDuplication

    @IsDuplication.setter
    def IsDuplication(self, IsDuplication):
        self._IsDuplication = IsDuplication

    @property
    def RegistrationDate(self):
        return self._RegistrationDate

    @RegistrationDate.setter
    def RegistrationDate(self, RegistrationDate):
        self._RegistrationDate = RegistrationDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegNum = params.get("RegNum")
        self._Name = params.get("Name")
        self._Capital = params.get("Capital")
        self._Person = params.get("Person")
        self._Address = params.get("Address")
        self._Business = params.get("Business")
        self._Type = params.get("Type")
        self._Period = params.get("Period")
        self._ComposingForm = params.get("ComposingForm")
        self._SetDate = params.get("SetDate")
        self._RecognizeWarnCode = params.get("RecognizeWarnCode")
        self._RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self._IsDuplication = params.get("IsDuplication")
        self._RegistrationDate = params.get("RegistrationDate")
        self._RequestId = params.get("RequestId")


class BusInvoice(AbstractModel):
    """汽车票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _Number: 发票号码
        :type Number: str
        :param _Code: 发票代码
        :type Code: str
        :param _Date: 开票日期
        :type Date: str
        :param _TimeGetOn: 乘车时间
        :type TimeGetOn: str
        :param _DateGetOn: 乘车日期
        :type DateGetOn: str
        :param _StationGetOn: 出发车站
        :type StationGetOn: str
        :param _StationGetOff: 到达车站
        :type StationGetOff: str
        :param _Total: 票价
        :type Total: str
        :param _UserName: 姓名
        :type UserName: str
        :param _Kind: 消费类型
        :type Kind: str
        :param _UserID: 身份证号
        :type UserID: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _PlaceGetOn: 乘车地点
        :type PlaceGetOn: str
        :param _GateNumber: 检票口
        :type GateNumber: str
        :param _TicketType: 客票类型
        :type TicketType: str
        :param _VehicleType: 车型
        :type VehicleType: str
        :param _SeatNumber: 座位号
        :type SeatNumber: str
        :param _TrainNumber: 车次
        :type TrainNumber: str
        """
        self._Title = None
        self._QRCodeMark = None
        self._Number = None
        self._Code = None
        self._Date = None
        self._TimeGetOn = None
        self._DateGetOn = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Total = None
        self._UserName = None
        self._Kind = None
        self._UserID = None
        self._Province = None
        self._City = None
        self._PlaceGetOn = None
        self._GateNumber = None
        self._TicketType = None
        self._VehicleType = None
        self._SeatNumber = None
        self._TrainNumber = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def DateGetOn(self):
        return self._DateGetOn

    @DateGetOn.setter
    def DateGetOn(self, DateGetOn):
        self._DateGetOn = DateGetOn

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def PlaceGetOn(self):
        return self._PlaceGetOn

    @PlaceGetOn.setter
    def PlaceGetOn(self, PlaceGetOn):
        self._PlaceGetOn = PlaceGetOn

    @property
    def GateNumber(self):
        return self._GateNumber

    @GateNumber.setter
    def GateNumber(self, GateNumber):
        self._GateNumber = GateNumber

    @property
    def TicketType(self):
        return self._TicketType

    @TicketType.setter
    def TicketType(self, TicketType):
        self._TicketType = TicketType

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def SeatNumber(self):
        return self._SeatNumber

    @SeatNumber.setter
    def SeatNumber(self, SeatNumber):
        self._SeatNumber = SeatNumber

    @property
    def TrainNumber(self):
        return self._TrainNumber

    @TrainNumber.setter
    def TrainNumber(self, TrainNumber):
        self._TrainNumber = TrainNumber


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Number = params.get("Number")
        self._Code = params.get("Code")
        self._Date = params.get("Date")
        self._TimeGetOn = params.get("TimeGetOn")
        self._DateGetOn = params.get("DateGetOn")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Total = params.get("Total")
        self._UserName = params.get("UserName")
        self._Kind = params.get("Kind")
        self._UserID = params.get("UserID")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._PlaceGetOn = params.get("PlaceGetOn")
        self._GateNumber = params.get("GateNumber")
        self._TicketType = params.get("TicketType")
        self._VehicleType = params.get("VehicleType")
        self._SeatNumber = params.get("SeatNumber")
        self._TrainNumber = params.get("TrainNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusInvoiceInfo(AbstractModel):
    """汽车票字段信息

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、发票号码、日期、票价、始发地、目的地、姓名、时间、发票消费类型、身份证号、省、市、开票日期、乘车地点、检票口、客票类型、车型、座位号、车次。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Value = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusInvoiceOCRRequest(AbstractModel):
    """BusInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusInvoiceOCRResponse(AbstractModel):
    """BusInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusInvoiceInfos: 汽车票识别结果，具体内容请点击左侧链接。
        :type BusInvoiceInfos: list of BusInvoiceInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusInvoiceInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def BusInvoiceInfos(self):
        return self._BusInvoiceInfos

    @BusInvoiceInfos.setter
    def BusInvoiceInfos(self, BusInvoiceInfos):
        self._BusInvoiceInfos = BusInvoiceInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BusInvoiceInfos") is not None:
            self._BusInvoiceInfos = []
            for item in params.get("BusInvoiceInfos"):
                obj = BusInvoiceInfo()
                obj._deserialize(item)
                self._BusInvoiceInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class BusinessCardInfo(AbstractModel):
    """名片识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称（关键字，可能重复，比如多个手机），能识别的字段名为：
姓名、英文姓名、英文地址、公司、英文公司、职位、英文职位、部门、英文部门、手机、电话、传真、社交帐号、QQ、MSN、微信、微博、邮箱、邮编、网址、公司账号、其他。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        :param _ItemCoord: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        self._Name = None
        self._Value = None
        self._ItemCoord = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ItemCoord(self):
        return self._ItemCoord

    @ItemCoord.setter
    def ItemCoord(self, ItemCoord):
        self._ItemCoord = ItemCoord


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("ItemCoord") is not None:
            self._ItemCoord = ItemCoord()
            self._ItemCoord._deserialize(params.get("ItemCoord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessCardOCRRequest(AbstractModel):
    """BusinessCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Config: 可选字段，根据需要选择是否请求对应字段。
目前支持的字段为：
RetImageType-“PROPROCESS” 图像预处理，string 类型。
图像预处理功能为，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。

SDK 设置方式参考：
Config = Json.stringify({"RetImageType":"PROPROCESS"})
API 3.0 Explorer 设置方式参考：
Config = {"RetImageType":"PROPROCESS"}
        :type Config: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Config = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BusinessCardOCRResponse(AbstractModel):
    """BusinessCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessCardInfos: 名片识别结果，具体内容请点击左侧链接。
        :type BusinessCardInfos: list of BusinessCardInfo
        :param _RetImageBase64: 返回图像预处理后的图片，图像预处理未开启时返回内容为空。
        :type RetImageBase64: str
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessCardInfos = None
        self._RetImageBase64 = None
        self._Angle = None
        self._RequestId = None

    @property
    def BusinessCardInfos(self):
        return self._BusinessCardInfos

    @BusinessCardInfos.setter
    def BusinessCardInfos(self, BusinessCardInfos):
        self._BusinessCardInfos = BusinessCardInfos

    @property
    def RetImageBase64(self):
        return self._RetImageBase64

    @RetImageBase64.setter
    def RetImageBase64(self, RetImageBase64):
        self._RetImageBase64 = RetImageBase64

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BusinessCardInfos") is not None:
            self._BusinessCardInfos = []
            for item in params.get("BusinessCardInfos"):
                obj = BusinessCardInfo()
                obj._deserialize(item)
                self._BusinessCardInfos.append(obj)
        self._RetImageBase64 = params.get("RetImageBase64")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class CandWord(AbstractModel):
    """候选字符集(包含候选字Character以及置信度Confidence)

    """

    def __init__(self):
        r"""
        :param _CandWords: 候选字符集的单词信息（包括单词Character和单词置信度confidence）
        :type CandWords: list of Words
        """
        self._CandWords = None

    @property
    def CandWords(self):
        return self._CandWords

    @CandWords.setter
    def CandWords(self, CandWords):
        self._CandWords = CandWords


    def _deserialize(self, params):
        if params.get("CandWords") is not None:
            self._CandWords = []
            for item in params.get("CandWords"):
                obj = Words()
                obj._deserialize(item)
                self._CandWords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarInvoiceInfo(AbstractModel):
    """购车发票识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、 机打代码、 发票号码、 发动机号码、 合格证号、 机打号码、 价税合计(小写)、 销货单位名称、 身份证号码/组织机构代码、 购买方名称、 销售方纳税人识别号、 购买方纳税人识别号、主管税务机关、 主管税务机关代码、 开票日期、 不含税价(小写)、 吨位、增值税税率或征收率、 车辆识别代号/车架号码、 增值税税额、 厂牌型号、 省、 市、 发票消费类型、 销售方电话、 销售方账号、 产地、 进口证明书号、 车辆类型、 机器编号、备注、开票人、限乘人数、商检单号、销售方地址、销售方开户银行、价税合计、发票类型。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        :param _Rect: 字段在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _Polygon: 字段在原图中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self._Name = None
        self._Value = None
        self._Rect = None
        self._Polygon = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        if params.get("Polygon") is not None:
            self._Polygon = Polygon()
            self._Polygon._deserialize(params.get("Polygon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarInvoiceOCRRequest(AbstractModel):
    """CarInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarInvoiceOCRResponse(AbstractModel):
    """CarInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CarInvoiceInfos: 购车发票识别结果，具体内容请点击左侧链接。
        :type CarInvoiceInfos: list of CarInvoiceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CarInvoiceInfos = None
        self._RequestId = None

    @property
    def CarInvoiceInfos(self):
        return self._CarInvoiceInfos

    @CarInvoiceInfos.setter
    def CarInvoiceInfos(self, CarInvoiceInfos):
        self._CarInvoiceInfos = CarInvoiceInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CarInvoiceInfos") is not None:
            self._CarInvoiceInfos = []
            for item in params.get("CarInvoiceInfos"):
                obj = CarInvoiceInfo()
                obj._deserialize(item)
                self._CarInvoiceInfos.append(obj)
        self._RequestId = params.get("RequestId")


class CellContent(AbstractModel):
    """单元格识别结果

    """

    def __init__(self):
        r"""
        :param _ParagNo: 段落编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ParagNo: int
        :param _WordSize: 字体大小
注意：此字段可能返回 null，表示取不到有效值。
        :type WordSize: int
        """
        self._ParagNo = None
        self._WordSize = None

    @property
    def ParagNo(self):
        return self._ParagNo

    @ParagNo.setter
    def ParagNo(self, ParagNo):
        self._ParagNo = ParagNo

    @property
    def WordSize(self):
        return self._WordSize

    @WordSize.setter
    def WordSize(self, WordSize):
        self._WordSize = WordSize


    def _deserialize(self, params):
        self._ParagNo = params.get("ParagNo")
        self._WordSize = params.get("WordSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyDetectInfo(AbstractModel):
    """卡证智能分类结果

    """

    def __init__(self):
        r"""
        :param _Name: 分类名称，包括：身份证、护照、名片、银行卡、行驶证、驾驶证、港澳台通行证、户口本、港澳台来往内地通行证、港澳台居住证、不动产证、营业执照
        :type Name: str
        :param _Type: 分类类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Rect: 位置坐标
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Type = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyDetectOCRRequest(AbstractModel):
    """ClassifyDetectOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _DiscernType: 可以指定要识别的票证类型,指定后不出现在此列表的票证将不返回类型。不指定时默认返回所有支持类别票证的识别信息。

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
        self._ImageBase64 = None
        self._ImageUrl = None
        self._DiscernType = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def DiscernType(self):
        return self._DiscernType

    @DiscernType.setter
    def DiscernType(self, DiscernType):
        self._DiscernType = DiscernType


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._DiscernType = params.get("DiscernType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyDetectOCRResponse(AbstractModel):
    """ClassifyDetectOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClassifyDetectInfos: 智能卡证分类结果。当图片类型不支持分类识别或者识别出的类型不在请求参数DiscernType指定的范围内时，返回结果中的Type字段将为空字符串，Name字段将返回"其它"
        :type ClassifyDetectInfos: list of ClassifyDetectInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClassifyDetectInfos = None
        self._RequestId = None

    @property
    def ClassifyDetectInfos(self):
        return self._ClassifyDetectInfos

    @ClassifyDetectInfos.setter
    def ClassifyDetectInfos(self, ClassifyDetectInfos):
        self._ClassifyDetectInfos = ClassifyDetectInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClassifyDetectInfos") is not None:
            self._ClassifyDetectInfos = []
            for item in params.get("ClassifyDetectInfos"):
                obj = ClassifyDetectInfo()
                obj._deserialize(item)
                self._ClassifyDetectInfos.append(obj)
        self._RequestId = params.get("RequestId")


class Coord(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param _X: 横坐标
        :type X: int
        :param _Y: 纵坐标
        :type Y: int
        """
        self._X = None
        self._Y = None

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
        


class CreateAIFormTaskRequest(AbstractModel):
    """CreateAIFormTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileList: 多个文件的URL列表
        :type FileList: list of SmartFormFileUrl
        :param _FirstNotes: 备注信息1
        :type FirstNotes: str
        :param _SecondNotes: 备注信息2
        :type SecondNotes: str
        :param _FileType: 文件类型
        :type FileType: int
        """
        self._FileList = None
        self._FirstNotes = None
        self._SecondNotes = None
        self._FileType = None

    @property
    def FileList(self):
        return self._FileList

    @FileList.setter
    def FileList(self, FileList):
        self._FileList = FileList

    @property
    def FirstNotes(self):
        return self._FirstNotes

    @FirstNotes.setter
    def FirstNotes(self, FirstNotes):
        self._FirstNotes = FirstNotes

    @property
    def SecondNotes(self):
        return self._SecondNotes

    @SecondNotes.setter
    def SecondNotes(self, SecondNotes):
        self._SecondNotes = SecondNotes

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        if params.get("FileList") is not None:
            self._FileList = []
            for item in params.get("FileList"):
                obj = SmartFormFileUrl()
                obj._deserialize(item)
                self._FileList.append(obj)
        self._FirstNotes = params.get("FirstNotes")
        self._SecondNotes = params.get("SecondNotes")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIFormTaskResponse(AbstractModel):
    """CreateAIFormTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 本次识别任务的唯一身份ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _OperateUrl: 本次识别任务的操作URL，有效期自生成之时起共24小时
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._OperateUrl = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def OperateUrl(self):
        return self._OperateUrl

    @OperateUrl.setter
    def OperateUrl(self, OperateUrl):
        self._OperateUrl = OperateUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._OperateUrl = params.get("OperateUrl")
        self._RequestId = params.get("RequestId")


class DetectedWordCoordPoint(AbstractModel):
    """单字在原图中的坐标，以四个顶点坐标表示，以左上角为起点，顺时针返回。

    """

    def __init__(self):
        r"""
        :param _WordCoordinate: 单字在原图中的坐标，以四个顶点坐标表示，以左上角为起点，顺时针返回。
        :type WordCoordinate: list of Coord
        """
        self._WordCoordinate = None

    @property
    def WordCoordinate(self):
        return self._WordCoordinate

    @WordCoordinate.setter
    def WordCoordinate(self, WordCoordinate):
        self._WordCoordinate = WordCoordinate


    def _deserialize(self, params):
        if params.get("WordCoordinate") is not None:
            self._WordCoordinate = []
            for item in params.get("WordCoordinate"):
                obj = Coord()
                obj._deserialize(item)
                self._WordCoordinate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectedWords(AbstractModel):
    """识别出来的单字信息包括单字（包括单字Character和单字置信度confidence）

    """

    def __init__(self):
        r"""
        :param _Confidence: 置信度 0 ~100
        :type Confidence: int
        :param _Character: 候选字Character
        :type Character: str
        """
        self._Confidence = None
        self._Character = None

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Character(self):
        return self._Character

    @Character.setter
    def Character(self, Character):
        self._Character = Character


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Character = params.get("Character")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DriverLicenseOCRRequest(AbstractModel):
    """DriverLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param _CardSide: FRONT 为驾驶证主页正面（有红色印章的一面），
BACK 为驾驶证副页正面（有档案编号的一面）。
DOUBLE 支持自动识别驾驶证正副页单面，和正副双面同框识别
默认值为：FRONT。
        :type CardSide: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CardSide = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CardSide(self):
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DriverLicenseOCRResponse(AbstractModel):
    """DriverLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 驾驶证正页姓名
        :type Name: str
        :param _Sex: 性别
        :type Sex: str
        :param _Nationality: 国籍
        :type Nationality: str
        :param _Address: 住址
        :type Address: str
        :param _DateOfBirth: 出生日期（YYYY-MM-DD）
        :type DateOfBirth: str
        :param _DateOfFirstIssue: 初次领证日期（YYYY-MM-DD）
        :type DateOfFirstIssue: str
        :param _Class: 准驾车型
        :type Class: str
        :param _StartDate: 有效期开始时间（YYYY-MM-DD）
        :type StartDate: str
        :param _EndDate: 有效期截止时间（新版驾驶证返回 YYYY-MM-DD，
老版驾驶证返回有效期限 X年）
        :type EndDate: str
        :param _CardCode: 驾驶证正页证号
        :type CardCode: str
        :param _ArchivesCode: 档案编号
        :type ArchivesCode: str
        :param _Record: 记录
        :type Record: str
        :param _RecognizeWarnCode: Code 告警码列表和释义：
-9102  复印件告警
-9103  翻拍件告警
注：告警码可以同时存在多个
        :type RecognizeWarnCode: list of int
        :param _RecognizeWarnMsg: 告警码说明：
WARN_DRIVER_LICENSE_COPY_CARD 复印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
注：告警信息可以同时存在多个
        :type RecognizeWarnMsg: list of str
        :param _IssuingAuthority: 发证单位
        :type IssuingAuthority: str
        :param _State: 状态（仅电子驾驶证支持返回该字段）
        :type State: str
        :param _CumulativeScore: 累积记分（仅电子驾驶证支持返回该字段）
        :type CumulativeScore: str
        :param _CurrentTime: 当前时间（仅电子驾驶证支持返回该字段）
        :type CurrentTime: str
        :param _GenerateTime: 生成时间（仅电子驾驶证支持返回该字段）
        :type GenerateTime: str
        :param _BackPageName: 驾驶证副页姓名
        :type BackPageName: str
        :param _BackPageCardCode: 驾驶证副页证号
        :type BackPageCardCode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Sex = None
        self._Nationality = None
        self._Address = None
        self._DateOfBirth = None
        self._DateOfFirstIssue = None
        self._Class = None
        self._StartDate = None
        self._EndDate = None
        self._CardCode = None
        self._ArchivesCode = None
        self._Record = None
        self._RecognizeWarnCode = None
        self._RecognizeWarnMsg = None
        self._IssuingAuthority = None
        self._State = None
        self._CumulativeScore = None
        self._CurrentTime = None
        self._GenerateTime = None
        self._BackPageName = None
        self._BackPageCardCode = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def DateOfBirth(self):
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

    @property
    def DateOfFirstIssue(self):
        return self._DateOfFirstIssue

    @DateOfFirstIssue.setter
    def DateOfFirstIssue(self, DateOfFirstIssue):
        self._DateOfFirstIssue = DateOfFirstIssue

    @property
    def Class(self):
        return self._Class

    @Class.setter
    def Class(self, Class):
        self._Class = Class

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def CardCode(self):
        return self._CardCode

    @CardCode.setter
    def CardCode(self, CardCode):
        self._CardCode = CardCode

    @property
    def ArchivesCode(self):
        return self._ArchivesCode

    @ArchivesCode.setter
    def ArchivesCode(self, ArchivesCode):
        self._ArchivesCode = ArchivesCode

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def RecognizeWarnCode(self):
        return self._RecognizeWarnCode

    @RecognizeWarnCode.setter
    def RecognizeWarnCode(self, RecognizeWarnCode):
        self._RecognizeWarnCode = RecognizeWarnCode

    @property
    def RecognizeWarnMsg(self):
        return self._RecognizeWarnMsg

    @RecognizeWarnMsg.setter
    def RecognizeWarnMsg(self, RecognizeWarnMsg):
        self._RecognizeWarnMsg = RecognizeWarnMsg

    @property
    def IssuingAuthority(self):
        return self._IssuingAuthority

    @IssuingAuthority.setter
    def IssuingAuthority(self, IssuingAuthority):
        self._IssuingAuthority = IssuingAuthority

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CumulativeScore(self):
        return self._CumulativeScore

    @CumulativeScore.setter
    def CumulativeScore(self, CumulativeScore):
        self._CumulativeScore = CumulativeScore

    @property
    def CurrentTime(self):
        return self._CurrentTime

    @CurrentTime.setter
    def CurrentTime(self, CurrentTime):
        self._CurrentTime = CurrentTime

    @property
    def GenerateTime(self):
        return self._GenerateTime

    @GenerateTime.setter
    def GenerateTime(self, GenerateTime):
        self._GenerateTime = GenerateTime

    @property
    def BackPageName(self):
        return self._BackPageName

    @BackPageName.setter
    def BackPageName(self, BackPageName):
        self._BackPageName = BackPageName

    @property
    def BackPageCardCode(self):
        return self._BackPageCardCode

    @BackPageCardCode.setter
    def BackPageCardCode(self, BackPageCardCode):
        self._BackPageCardCode = BackPageCardCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Nationality = params.get("Nationality")
        self._Address = params.get("Address")
        self._DateOfBirth = params.get("DateOfBirth")
        self._DateOfFirstIssue = params.get("DateOfFirstIssue")
        self._Class = params.get("Class")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._CardCode = params.get("CardCode")
        self._ArchivesCode = params.get("ArchivesCode")
        self._Record = params.get("Record")
        self._RecognizeWarnCode = params.get("RecognizeWarnCode")
        self._RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self._IssuingAuthority = params.get("IssuingAuthority")
        self._State = params.get("State")
        self._CumulativeScore = params.get("CumulativeScore")
        self._CurrentTime = params.get("CurrentTime")
        self._GenerateTime = params.get("GenerateTime")
        self._BackPageName = params.get("BackPageName")
        self._BackPageCardCode = params.get("BackPageCardCode")
        self._RequestId = params.get("RequestId")


class DutyPaidProofInfo(AbstractModel):
    """识别出的字段

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
税号 、纳税人识别号 、纳税人名称 、金额合计大写 、金额合计小写 、填发日期 、税务机关 、填票人。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Value = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DutyPaidProofOCRRequest(AbstractModel):
    """DutyPaidProofOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DutyPaidProofOCRResponse(AbstractModel):
    """DutyPaidProofOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DutyPaidProofInfos: 完税证明识别结果，具体内容请点击左侧链接。
        :type DutyPaidProofInfos: list of DutyPaidProofInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DutyPaidProofInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def DutyPaidProofInfos(self):
        return self._DutyPaidProofInfos

    @DutyPaidProofInfos.setter
    def DutyPaidProofInfos(self, DutyPaidProofInfos):
        self._DutyPaidProofInfos = DutyPaidProofInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DutyPaidProofInfos") is not None:
            self._DutyPaidProofInfos = []
            for item in params.get("DutyPaidProofInfos"):
                obj = DutyPaidProofInfo()
                obj._deserialize(item)
                self._DutyPaidProofInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class EduPaperOCRRequest(AbstractModel):
    """EduPaperOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Config: 扩展配置信息。
配置格式：{"option1":value1,"option2":value2}
1. task_type：任务类型【0: 关闭版式分析与处理 1: 开启版式分析处理】可选参数，Int32类型，默认值为1
2. is_structuralization：是否结构化输出【true：返回包体同时返回通用和结构化输出  false：返回包体返回通用输出】 可选参数，Bool类型，默认值为true
3. if_readable_format：是否按照版式整合通用文本/公式输出结果 可选参数，Bool类型，默认值为false
示例：
{"task_type": 1,"is_structuralization": true,"if_readable_format": true}
        :type Config: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Config = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EduPaperOCRResponse(AbstractModel):
    """EduPaperOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EduPaperInfos: 检测到的文本信息，具体内容请点击左侧链接。
        :type EduPaperInfos: list of TextEduPaper
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。
        :type Angle: int
        :param _QuestionBlockInfos: 结构化方式输出，具体内容请点击左侧链接。
        :type QuestionBlockInfos: list of QuestionBlockObj
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EduPaperInfos = None
        self._Angle = None
        self._QuestionBlockInfos = None
        self._RequestId = None

    @property
    def EduPaperInfos(self):
        return self._EduPaperInfos

    @EduPaperInfos.setter
    def EduPaperInfos(self, EduPaperInfos):
        self._EduPaperInfos = EduPaperInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def QuestionBlockInfos(self):
        return self._QuestionBlockInfos

    @QuestionBlockInfos.setter
    def QuestionBlockInfos(self, QuestionBlockInfos):
        self._QuestionBlockInfos = QuestionBlockInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EduPaperInfos") is not None:
            self._EduPaperInfos = []
            for item in params.get("EduPaperInfos"):
                obj = TextEduPaper()
                obj._deserialize(item)
                self._EduPaperInfos.append(obj)
        self._Angle = params.get("Angle")
        if params.get("QuestionBlockInfos") is not None:
            self._QuestionBlockInfos = []
            for item in params.get("QuestionBlockInfos"):
                obj = QuestionBlockObj()
                obj._deserialize(item)
                self._QuestionBlockInfos.append(obj)
        self._RequestId = params.get("RequestId")


class EnglishOCRRequest(AbstractModel):
    """EnglishOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。像素须介于20-10000px之间。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。

        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。像素须介于20-10000px之间。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _EnableCoordPoint: 单词四点坐标开关，开启可返回图片中单词的四点坐标。
该参数默认值为false。
        :type EnableCoordPoint: bool
        :param _EnableCandWord: 候选字开关，开启可返回识别时多个可能的候选字（每个候选字对应其置信度）。
该参数默认值为false。
        :type EnableCandWord: bool
        :param _Preprocess: 预处理开关，功能是检测图片倾斜的角度，将原本倾斜的图片矫正。该参数默认值为true。
        :type Preprocess: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._EnableCoordPoint = None
        self._EnableCandWord = None
        self._Preprocess = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def EnableCoordPoint(self):
        return self._EnableCoordPoint

    @EnableCoordPoint.setter
    def EnableCoordPoint(self, EnableCoordPoint):
        self._EnableCoordPoint = EnableCoordPoint

    @property
    def EnableCandWord(self):
        return self._EnableCandWord

    @EnableCandWord.setter
    def EnableCandWord(self, EnableCandWord):
        self._EnableCandWord = EnableCandWord

    @property
    def Preprocess(self):
        return self._Preprocess

    @Preprocess.setter
    def Preprocess(self, Preprocess):
        self._Preprocess = Preprocess


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._EnableCoordPoint = params.get("EnableCoordPoint")
        self._EnableCandWord = params.get("EnableCandWord")
        self._Preprocess = params.get("Preprocess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnglishOCRResponse(AbstractModel):
    """EnglishOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetectionEn
        :param _Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Angel = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Angel(self):
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        self._Angel = Angel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetectionEn()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Angel = params.get("Angel")
        self._RequestId = params.get("RequestId")


class EnterpriseLicenseInfo(AbstractModel):
    """企业证照单个字段的内容

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称（关键字），不同证件类型可能不同，证件类型包含企业登记证书、许可证书、企业执照、三证合一类证书；
支持以下字段：统一社会信用代码、法定代表人、公司名称、公司地址、注册资金、企业类型、经营范围、成立日期、有效期、开办资金、经费来源、举办单位等；
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterpriseLicenseOCRRequest(AbstractModel):
    """EnterpriseLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterpriseLicenseOCRResponse(AbstractModel):
    """EnterpriseLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnterpriseLicenseInfos: 企业证照识别结果，具体内容请点击左侧链接。
        :type EnterpriseLicenseInfos: list of EnterpriseLicenseInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnterpriseLicenseInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def EnterpriseLicenseInfos(self):
        return self._EnterpriseLicenseInfos

    @EnterpriseLicenseInfos.setter
    def EnterpriseLicenseInfos(self, EnterpriseLicenseInfos):
        self._EnterpriseLicenseInfos = EnterpriseLicenseInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnterpriseLicenseInfos") is not None:
            self._EnterpriseLicenseInfos = []
            for item in params.get("EnterpriseLicenseInfos"):
                obj = EnterpriseLicenseInfo()
                obj._deserialize(item)
                self._EnterpriseLicenseInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class EstateCertOCRRequest(AbstractModel):
    """EstateCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EstateCertOCRResponse(AbstractModel):
    """EstateCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Obligee: 权利人
        :type Obligee: str
        :param _Ownership: 共有情况
        :type Ownership: str
        :param _Location: 坐落
        :type Location: str
        :param _Unit: 不动产单元号
        :type Unit: str
        :param _Type: 权利类型
        :type Type: str
        :param _Property: 权利性质
        :type Property: str
        :param _Usage: 用途
        :type Usage: str
        :param _Area: 面积
        :type Area: str
        :param _Term: 使用期限
        :type Term: str
        :param _Other: 权利其他状况，多行会用换行符\n连接。
        :type Other: str
        :param _Angle: 图片旋转角度
        :type Angle: float
        :param _Number: 不动产权号
        :type Number: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Obligee = None
        self._Ownership = None
        self._Location = None
        self._Unit = None
        self._Type = None
        self._Property = None
        self._Usage = None
        self._Area = None
        self._Term = None
        self._Other = None
        self._Angle = None
        self._Number = None
        self._RequestId = None

    @property
    def Obligee(self):
        return self._Obligee

    @Obligee.setter
    def Obligee(self, Obligee):
        self._Obligee = Obligee

    @property
    def Ownership(self):
        return self._Ownership

    @Ownership.setter
    def Ownership(self, Ownership):
        self._Ownership = Ownership

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Property(self):
        return self._Property

    @Property.setter
    def Property(self, Property):
        self._Property = Property

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Term(self):
        return self._Term

    @Term.setter
    def Term(self, Term):
        self._Term = Term

    @property
    def Other(self):
        return self._Other

    @Other.setter
    def Other(self, Other):
        self._Other = Other

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Obligee = params.get("Obligee")
        self._Ownership = params.get("Ownership")
        self._Location = params.get("Location")
        self._Unit = params.get("Unit")
        self._Type = params.get("Type")
        self._Property = params.get("Property")
        self._Usage = params.get("Usage")
        self._Area = params.get("Area")
        self._Term = params.get("Term")
        self._Other = params.get("Other")
        self._Angle = params.get("Angle")
        self._Number = params.get("Number")
        self._RequestId = params.get("RequestId")


class FinanBillInfo(AbstractModel):
    """金融票据整单识别单个字段的内容

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
【进账单】
日期、出票全称、出票账号、出票开户行、收款人全称、收款人账号、收款开户行、大写金额、小写金额、票据种类、票据张数、票据号码；
【支票】
开户银行、支票种类、凭证号码2、日期、大写金额、小写金额、付款行编号、密码、凭证号码1；
【银行承兑汇票】或【商业承兑汇票】
出票日期、行号1、行号2、出票人全称、出票人账号、付款行全称、收款人全称、收款人账号、收款人开户行、出票金额大写、出票金额小写、汇票到期日、付款行行号、付款行地址。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillOCRRequest(AbstractModel):
    """FinanBillOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillOCRResponse(AbstractModel):
    """FinanBillOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FinanBillInfos: 金融票据整单识别结果，具体内容请点击左侧链接。
        :type FinanBillInfos: list of FinanBillInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FinanBillInfos = None
        self._RequestId = None

    @property
    def FinanBillInfos(self):
        return self._FinanBillInfos

    @FinanBillInfos.setter
    def FinanBillInfos(self, FinanBillInfos):
        self._FinanBillInfos = FinanBillInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FinanBillInfos") is not None:
            self._FinanBillInfos = []
            for item in params.get("FinanBillInfos"):
                obj = FinanBillInfo()
                obj._deserialize(item)
                self._FinanBillInfos.append(obj)
        self._RequestId = params.get("RequestId")


class FinanBillSliceInfo(AbstractModel):
    """金融票据切片识别单个字段的内容

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
大写金额、小写金额、账号、票号1、票号2、收款人、大写日期、同城交换号、地址-省份、地址-城市、付款行全称、支票密码、支票用途。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillSliceOCRRequest(AbstractModel):
    """FinanBillSliceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanBillSliceOCRResponse(AbstractModel):
    """FinanBillSliceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FinanBillSliceInfos: 金融票据切片识别结果，具体内容请点击左侧链接。
        :type FinanBillSliceInfos: list of FinanBillSliceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FinanBillSliceInfos = None
        self._RequestId = None

    @property
    def FinanBillSliceInfos(self):
        return self._FinanBillSliceInfos

    @FinanBillSliceInfos.setter
    def FinanBillSliceInfos(self, FinanBillSliceInfos):
        self._FinanBillSliceInfos = FinanBillSliceInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FinanBillSliceInfos") is not None:
            self._FinanBillSliceInfos = []
            for item in params.get("FinanBillSliceInfos"):
                obj = FinanBillSliceInfo()
                obj._deserialize(item)
                self._FinanBillSliceInfos.append(obj)
        self._RequestId = params.get("RequestId")


class FlightInvoiceInfo(AbstractModel):
    """机票行程单识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
票价、合计金额、填开日期、有效身份证件号码、电子客票号码、验证码、旅客姓名、填开单位、其他税费、燃油附加费、民航发展基金、保险费、销售单位代号、始发地、目的地、航班号、时间、日期、座位等级、承运人、发票消费类型、国内国际标签、印刷序号、客票级别/类别、客票生效日期、有效期截止日期、免费行李。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段 Name 对应的字符串结果。
        :type Value: str
        :param _Row: 多个行程的字段所在行号，下标从0开始，非行字段或未能识别行号的该值返回-1。
        :type Row: int
        """
        self._Name = None
        self._Value = None
        self._Row = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Row(self):
        return self._Row

    @Row.setter
    def Row(self, Row):
        self._Row = Row


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Row = params.get("Row")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlightInvoiceOCRRequest(AbstractModel):
    """FlightInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlightInvoiceOCRResponse(AbstractModel):
    """FlightInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlightInvoiceInfos: 机票行程单识别结果，具体内容请点击左侧链接。
        :type FlightInvoiceInfos: list of FlightInvoiceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlightInvoiceInfos = None
        self._RequestId = None

    @property
    def FlightInvoiceInfos(self):
        return self._FlightInvoiceInfos

    @FlightInvoiceInfos.setter
    def FlightInvoiceInfos(self, FlightInvoiceInfos):
        self._FlightInvoiceInfos = FlightInvoiceInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FlightInvoiceInfos") is not None:
            self._FlightInvoiceInfos = []
            for item in params.get("FlightInvoiceInfos"):
                obj = FlightInvoiceInfo()
                obj._deserialize(item)
                self._FlightInvoiceInfos.append(obj)
        self._RequestId = params.get("RequestId")


class FlightItem(AbstractModel):
    """机票行程卡条目

    """

    def __init__(self):
        r"""
        :param _TerminalGetOn: 出发航站楼
        :type TerminalGetOn: str
        :param _TerminalGetOff: 到达航站楼
        :type TerminalGetOff: str
        :param _Carrier: 承运人
        :type Carrier: str
        :param _FlightNumber: 航班号
        :type FlightNumber: str
        :param _Seat: 座位等级
        :type Seat: str
        :param _DateGetOn: 乘机日期
        :type DateGetOn: str
        :param _TimeGetOn: 乘机时间
        :type TimeGetOn: str
        :param _StationGetOn: 出发站
        :type StationGetOn: str
        :param _StationGetOff: 到达站
        :type StationGetOff: str
        :param _Allow: 免费行李
        :type Allow: str
        :param _FareBasis: 客票级别/客票类别
        :type FareBasis: str
        """
        self._TerminalGetOn = None
        self._TerminalGetOff = None
        self._Carrier = None
        self._FlightNumber = None
        self._Seat = None
        self._DateGetOn = None
        self._TimeGetOn = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Allow = None
        self._FareBasis = None

    @property
    def TerminalGetOn(self):
        return self._TerminalGetOn

    @TerminalGetOn.setter
    def TerminalGetOn(self, TerminalGetOn):
        self._TerminalGetOn = TerminalGetOn

    @property
    def TerminalGetOff(self):
        return self._TerminalGetOff

    @TerminalGetOff.setter
    def TerminalGetOff(self, TerminalGetOff):
        self._TerminalGetOff = TerminalGetOff

    @property
    def Carrier(self):
        return self._Carrier

    @Carrier.setter
    def Carrier(self, Carrier):
        self._Carrier = Carrier

    @property
    def FlightNumber(self):
        return self._FlightNumber

    @FlightNumber.setter
    def FlightNumber(self, FlightNumber):
        self._FlightNumber = FlightNumber

    @property
    def Seat(self):
        return self._Seat

    @Seat.setter
    def Seat(self, Seat):
        self._Seat = Seat

    @property
    def DateGetOn(self):
        return self._DateGetOn

    @DateGetOn.setter
    def DateGetOn(self, DateGetOn):
        self._DateGetOn = DateGetOn

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Allow(self):
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def FareBasis(self):
        return self._FareBasis

    @FareBasis.setter
    def FareBasis(self, FareBasis):
        self._FareBasis = FareBasis


    def _deserialize(self, params):
        self._TerminalGetOn = params.get("TerminalGetOn")
        self._TerminalGetOff = params.get("TerminalGetOff")
        self._Carrier = params.get("Carrier")
        self._FlightNumber = params.get("FlightNumber")
        self._Seat = params.get("Seat")
        self._DateGetOn = params.get("DateGetOn")
        self._TimeGetOn = params.get("TimeGetOn")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Allow = params.get("Allow")
        self._FareBasis = params.get("FareBasis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormulaOCRRequest(AbstractModel):
    """FormulaOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormulaOCRResponse(AbstractModel):
    """FormulaOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负
        :type Angle: int
        :param _FormulaInfos: 检测到的文本信息，具体内容请点击左侧链接。
        :type FormulaInfos: list of TextFormula
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Angle = None
        self._FormulaInfos = None
        self._RequestId = None

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def FormulaInfos(self):
        return self._FormulaInfos

    @FormulaInfos.setter
    def FormulaInfos(self, FormulaInfos):
        self._FormulaInfos = FormulaInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Angle = params.get("Angle")
        if params.get("FormulaInfos") is not None:
            self._FormulaInfos = []
            for item in params.get("FormulaInfos"):
                obj = TextFormula()
                obj._deserialize(item)
                self._FormulaInfos.append(obj)
        self._RequestId = params.get("RequestId")


class GeneralAccurateOCRRequest(AbstractModel):
    """GeneralAccurateOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsWords: 是否返回单字信息，默认关
        :type IsWords: bool
        :param _EnableDetectSplit: 是否开启原图切图检测功能，开启后可提升“整图面积大，但单字符占比面积小”（例如：试卷）场景下的识别效果，默认关
        :type EnableDetectSplit: bool
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param _EnableDetectText: 文本检测开关，默认为true。设置为false可直接进行单行识别，适用于仅包含正向单行文本的图片场景。
        :type EnableDetectText: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsWords = None
        self._EnableDetectSplit = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._EnableDetectText = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsWords(self):
        return self._IsWords

    @IsWords.setter
    def IsWords(self, IsWords):
        self._IsWords = IsWords

    @property
    def EnableDetectSplit(self):
        return self._EnableDetectSplit

    @EnableDetectSplit.setter
    def EnableDetectSplit(self, EnableDetectSplit):
        self._EnableDetectSplit = EnableDetectSplit

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def EnableDetectText(self):
        return self._EnableDetectText

    @EnableDetectText.setter
    def EnableDetectText(self, EnableDetectText):
        self._EnableDetectText = EnableDetectText


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsWords = params.get("IsWords")
        self._EnableDetectSplit = params.get("EnableDetectSplit")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._EnableDetectText = params.get("EnableDetectText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralAccurateOCRResponse(AbstractModel):
    """GeneralAccurateOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param _Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Angel = None
        self._Angle = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Angel(self):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        self._Angel = Angel

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Angel = params.get("Angel")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class GeneralBasicOCRRequest(AbstractModel):
    """GeneralBasicOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片/PDF的 Base64 值。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片/PDF的 Url 地址。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Scene: 保留字段。
        :type Scene: str
        :param _LanguageType: 识别语言类型。
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
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param _IsWords: 是否返回单字信息，默认关
        :type IsWords: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Scene = None
        self._LanguageType = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._IsWords = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LanguageType(self):
        return self._LanguageType

    @LanguageType.setter
    def LanguageType(self, LanguageType):
        self._LanguageType = LanguageType

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def IsWords(self):
        return self._IsWords

    @IsWords.setter
    def IsWords(self, IsWords):
        self._IsWords = IsWords


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Scene = params.get("Scene")
        self._LanguageType = params.get("LanguageType")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._IsWords = params.get("IsWords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralBasicOCRResponse(AbstractModel):
    """GeneralBasicOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param _Language: 检测到的语言类型，目前支持的语言类型参考入参LanguageType说明。
        :type Language: str
        :param _Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param _PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0
        :type PdfPageSize: int
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Language = None
        self._Angel = None
        self._PdfPageSize = None
        self._Angle = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Angel(self):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        warnings.warn("parameter `Angel` is deprecated", DeprecationWarning) 

        self._Angel = Angel

    @property
    def PdfPageSize(self):
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Language = params.get("Language")
        self._Angel = params.get("Angel")
        self._PdfPageSize = params.get("PdfPageSize")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class GeneralEfficientOCRRequest(AbstractModel):
    """GeneralEfficientOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
要求图片经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralEfficientOCRResponse(AbstractModel):
    """GeneralEfficientOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，包括文本行内容、置信度、文本行坐标以及文本行旋转纠正后的坐标，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param _Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Angel = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Angel(self):
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        self._Angel = Angel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Angel = params.get("Angel")
        self._RequestId = params.get("RequestId")


class GeneralFastOCRRequest(AbstractModel):
    """GeneralFastOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralFastOCRResponse(AbstractModel):
    """GeneralFastOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextDetection
        :param _Language: 检测到的语言，目前支持的语种范围为：简体中文、繁体中文、英文、日文、韩文。未来将陆续新增对更多语种的支持。
返回结果含义为：zh - 中英混合，jap - 日文，kor - 韩文。
        :type Language: str
        :param _Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负
        :type Angel: float
        :param _PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0
        :type PdfPageSize: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Language = None
        self._Angel = None
        self._PdfPageSize = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Angel(self):
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        self._Angel = Angel

    @property
    def PdfPageSize(self):
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Language = params.get("Language")
        self._Angel = params.get("Angel")
        self._PdfPageSize = params.get("PdfPageSize")
        self._RequestId = params.get("RequestId")


class GeneralHandwritingOCRRequest(AbstractModel):
    """GeneralHandwritingOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Scene: 场景字段，默认不用填写。
可选值:only_hw  表示只输出手写体识别结果，过滤印刷体。
        :type Scene: str
        :param _EnableWordPolygon: 是否开启单字的四点定位坐标输出，默认值为false。
        :type EnableWordPolygon: bool
        :param _EnableDetectText: 文本检测开关，默认值为true。
设置为false表示直接进行单行识别，可适用于识别单行手写体签名场景。
        :type EnableDetectText: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Scene = None
        self._EnableWordPolygon = None
        self._EnableDetectText = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def EnableWordPolygon(self):
        return self._EnableWordPolygon

    @EnableWordPolygon.setter
    def EnableWordPolygon(self, EnableWordPolygon):
        self._EnableWordPolygon = EnableWordPolygon

    @property
    def EnableDetectText(self):
        return self._EnableDetectText

    @EnableDetectText.setter
    def EnableDetectText(self, EnableDetectText):
        self._EnableDetectText = EnableDetectText


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Scene = params.get("Scene")
        self._EnableWordPolygon = params.get("EnableWordPolygon")
        self._EnableDetectText = params.get("EnableDetectText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralHandwritingOCRResponse(AbstractModel):
    """GeneralHandwritingOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: list of TextGeneralHandwriting
        :param _Angel: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angel: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Angel = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Angel(self):
        return self._Angel

    @Angel.setter
    def Angel(self, Angel):
        self._Angel = Angel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextGeneralHandwriting()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Angel = params.get("Angel")
        self._RequestId = params.get("RequestId")


class GeneralMachineItem(AbstractModel):
    """通用机打发票条目

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
        :type Name: str
        :param _Specification: 规格型号
        :type Specification: str
        :param _Unit: 单位
        :type Unit: str
        :param _Quantity: 数量
        :type Quantity: str
        :param _Price: 单价
        :type Price: str
        :param _Total: 金额
        :type Total: str
        :param _TaxRate: 税率
        :type TaxRate: str
        :param _Tax: 税额
        :type Tax: str
        """
        self._Name = None
        self._Specification = None
        self._Unit = None
        self._Quantity = None
        self._Price = None
        self._Total = None
        self._TaxRate = None
        self._Tax = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Specification = params.get("Specification")
        self._Unit = params.get("Unit")
        self._Quantity = params.get("Quantity")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        self._TaxRate = params.get("TaxRate")
        self._Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskStateRequest(AbstractModel):
    """GetTaskState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 智慧表单任务唯一身份ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskStateResponse(AbstractModel):
    """GetTaskState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskState: 1:任务识别完成，还未提交
2:任务已手动关闭
3:任务已提交
4:任务识别中
5:超时：任务超过了可操作的24H时限
6:任务识别失败
        :type TaskState: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskState = None
        self._RequestId = None

    @property
    def TaskState(self):
        return self._TaskState

    @TaskState.setter
    def TaskState(self, TaskState):
        self._TaskState = TaskState

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskState = params.get("TaskState")
        self._RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """组在图中的序号

    """

    def __init__(self):
        r"""
        :param _Groups: 每一行的元素
        :type Groups: list of LineInfo
        """
        self._Groups = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = LineInfo()
                obj._deserialize(item)
                self._Groups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HKIDCardOCRRequest(AbstractModel):
    """HKIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DetectFake: 是否鉴伪。
        :type DetectFake: bool
        :param _ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._DetectFake = None
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def DetectFake(self):
        return self._DetectFake

    @DetectFake.setter
    def DetectFake(self, DetectFake):
        self._DetectFake = DetectFake

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._DetectFake = params.get("DetectFake")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HKIDCardOCRResponse(AbstractModel):
    """HKIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CnName: 中文姓名
        :type CnName: str
        :param _EnName: 英文姓名
        :type EnName: str
        :param _TelexCode: 中文姓名对应电码
        :type TelexCode: str
        :param _Sex: 性别 ：“男M”或“女F”
        :type Sex: str
        :param _Birthday: 出生日期
        :type Birthday: str
        :param _Permanent: 永久性居民身份证。
0：非永久；
1：永久；
-1：未知。
        :type Permanent: int
        :param _IdNum: 身份证号码
        :type IdNum: str
        :param _Symbol: 证件符号，出生日期下的符号，例如"***AZ"
        :type Symbol: str
        :param _FirstIssueDate: 首次签发日期
        :type FirstIssueDate: str
        :param _CurrentIssueDate: 最近领用日期
        :type CurrentIssueDate: str
        :param _FakeDetectResult: 真假判断。
0：无法判断（图像模糊、不完整、反光、过暗等导致无法判断）；
1：假；
2：真。
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeDetectResult: int
        :param _HeadImage: 人像照片Base64后的结果
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadImage: str
        :param _WarningCode: 多重告警码，当身份证是翻拍、复印件时返回对应告警码。
-9102：证照复印件告警
-9103：证照翻拍告警
        :type WarningCode: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CnName = None
        self._EnName = None
        self._TelexCode = None
        self._Sex = None
        self._Birthday = None
        self._Permanent = None
        self._IdNum = None
        self._Symbol = None
        self._FirstIssueDate = None
        self._CurrentIssueDate = None
        self._FakeDetectResult = None
        self._HeadImage = None
        self._WarningCode = None
        self._RequestId = None

    @property
    def CnName(self):
        return self._CnName

    @CnName.setter
    def CnName(self, CnName):
        self._CnName = CnName

    @property
    def EnName(self):
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def TelexCode(self):
        return self._TelexCode

    @TelexCode.setter
    def TelexCode(self, TelexCode):
        self._TelexCode = TelexCode

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def Permanent(self):
        return self._Permanent

    @Permanent.setter
    def Permanent(self, Permanent):
        self._Permanent = Permanent

    @property
    def IdNum(self):
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Symbol(self):
        return self._Symbol

    @Symbol.setter
    def Symbol(self, Symbol):
        self._Symbol = Symbol

    @property
    def FirstIssueDate(self):
        return self._FirstIssueDate

    @FirstIssueDate.setter
    def FirstIssueDate(self, FirstIssueDate):
        self._FirstIssueDate = FirstIssueDate

    @property
    def CurrentIssueDate(self):
        return self._CurrentIssueDate

    @CurrentIssueDate.setter
    def CurrentIssueDate(self, CurrentIssueDate):
        self._CurrentIssueDate = CurrentIssueDate

    @property
    def FakeDetectResult(self):
        return self._FakeDetectResult

    @FakeDetectResult.setter
    def FakeDetectResult(self, FakeDetectResult):
        self._FakeDetectResult = FakeDetectResult

    @property
    def HeadImage(self):
        return self._HeadImage

    @HeadImage.setter
    def HeadImage(self, HeadImage):
        self._HeadImage = HeadImage

    @property
    def WarningCode(self):
        return self._WarningCode

    @WarningCode.setter
    def WarningCode(self, WarningCode):
        self._WarningCode = WarningCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CnName = params.get("CnName")
        self._EnName = params.get("EnName")
        self._TelexCode = params.get("TelexCode")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._Permanent = params.get("Permanent")
        self._IdNum = params.get("IdNum")
        self._Symbol = params.get("Symbol")
        self._FirstIssueDate = params.get("FirstIssueDate")
        self._CurrentIssueDate = params.get("CurrentIssueDate")
        self._FakeDetectResult = params.get("FakeDetectResult")
        self._HeadImage = params.get("HeadImage")
        self._WarningCode = params.get("WarningCode")
        self._RequestId = params.get("RequestId")


class HmtResidentPermitOCRRequest(AbstractModel):
    """HmtResidentPermitOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _CardSide: FRONT：有照片的一面（人像面），
BACK：无照片的一面（国徽面），
该参数如果不填或填错，将为您自动判断正反面。
        :type CardSide: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CardSide = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CardSide(self):
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HmtResidentPermitOCRResponse(AbstractModel):
    """HmtResidentPermitOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 证件姓名
        :type Name: str
        :param _Sex: 性别
        :type Sex: str
        :param _Birth: 出生日期
        :type Birth: str
        :param _Address: 地址
        :type Address: str
        :param _IdCardNo: 身份证号
        :type IdCardNo: str
        :param _CardType: 0-正面
1-反面
        :type CardType: int
        :param _ValidDate: 证件有效期限
        :type ValidDate: str
        :param _Authority: 签发机关
        :type Authority: str
        :param _VisaNum: 签发次数
        :type VisaNum: str
        :param _PassNo: 通行证号码
        :type PassNo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Sex = None
        self._Birth = None
        self._Address = None
        self._IdCardNo = None
        self._CardType = None
        self._ValidDate = None
        self._Authority = None
        self._VisaNum = None
        self._PassNo = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birth(self):
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IdCardNo(self):
        return self._IdCardNo

    @IdCardNo.setter
    def IdCardNo(self, IdCardNo):
        self._IdCardNo = IdCardNo

    @property
    def CardType(self):
        return self._CardType

    @CardType.setter
    def CardType(self, CardType):
        self._CardType = CardType

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def Authority(self):
        return self._Authority

    @Authority.setter
    def Authority(self, Authority):
        self._Authority = Authority

    @property
    def VisaNum(self):
        return self._VisaNum

    @VisaNum.setter
    def VisaNum(self, VisaNum):
        self._VisaNum = VisaNum

    @property
    def PassNo(self):
        return self._PassNo

    @PassNo.setter
    def PassNo(self, PassNo):
        self._PassNo = PassNo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Birth = params.get("Birth")
        self._Address = params.get("Address")
        self._IdCardNo = params.get("IdCardNo")
        self._CardType = params.get("CardType")
        self._ValidDate = params.get("ValidDate")
        self._Authority = params.get("Authority")
        self._VisaNum = params.get("VisaNum")
        self._PassNo = params.get("PassNo")
        self._RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param _CardSide: FRONT：身份证有照片的一面（人像面），
BACK：身份证有国徽的一面（国徽面），
该参数如果不填，将为您自动判断身份证正反面。
        :type CardSide: str
        :param _Config: 以下可选字段均为bool 类型，默认false：
CropIdCard，身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）
CropPortrait，人像照片裁剪（自动抠取身份证头像区域）
CopyWarn，复印件告警
BorderCheckWarn，边框和框内遮挡告警
ReshootWarn，翻拍告警
DetectPsWarn，疑似存在PS痕迹告警
TempIdWarn，临时身份证告警
InvalidDateWarn，身份证有效日期不合法告警
Quality，图片质量分数（评价图片的模糊程度）
MultiCardDetect，是否开启正反面同框识别（仅支持二代身份证正反页同框识别或临时身份证正反页同框识别）
ReflectWarn，是否开启反光检测

SDK 设置方式参考：
Config = Json.stringify({"CropIdCard":true,"CropPortrait":true})
API 3.0 Explorer 设置方式参考：
Config = {"CropIdCard":true,"CropPortrait":true}
        :type Config: str
        :param _EnableRecognitionRectify: 默认值为true，打开识别结果纠正开关。开关开启后，身份证号、出生日期、性别，三个字段会进行矫正补齐，统一结果输出；若关闭此开关，以上三个字段不会进行矫正补齐，保持原始识别结果输出，若原图出现篡改情况，这三个字段的识别结果可能会不统一。
        :type EnableRecognitionRectify: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CardSide = None
        self._Config = None
        self._EnableRecognitionRectify = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CardSide(self):
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def EnableRecognitionRectify(self):
        return self._EnableRecognitionRectify

    @EnableRecognitionRectify.setter
    def EnableRecognitionRectify(self, EnableRecognitionRectify):
        self._EnableRecognitionRectify = EnableRecognitionRectify


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CardSide = params.get("CardSide")
        self._Config = params.get("Config")
        self._EnableRecognitionRectify = params.get("EnableRecognitionRectify")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IDCardOCRResponse(AbstractModel):
    """IDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 姓名（人像面）
        :type Name: str
        :param _Sex: 性别（人像面）
        :type Sex: str
        :param _Nation: 民族（人像面）
        :type Nation: str
        :param _Birth: 出生日期（人像面）
        :type Birth: str
        :param _Address: 地址（人像面）
        :type Address: str
        :param _IdNum: 身份证号（人像面）
        :type IdNum: str
        :param _Authority: 发证机关（国徽面）
        :type Authority: str
        :param _ValidDate: 证件有效期（国徽面）
        :type ValidDate: str
        :param _AdvancedInfo: 扩展信息，不请求则不返回，具体输入参考示例3和示例4。
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
-9106	身份证疑似存在PS痕迹告警，
-9107       身份证反光告警。
        :type AdvancedInfo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Sex = None
        self._Nation = None
        self._Birth = None
        self._Address = None
        self._IdNum = None
        self._Authority = None
        self._ValidDate = None
        self._AdvancedInfo = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def Birth(self):
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IdNum(self):
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Authority(self):
        return self._Authority

    @Authority.setter
    def Authority(self, Authority):
        self._Authority = Authority

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Nation = params.get("Nation")
        self._Birth = params.get("Birth")
        self._Address = params.get("Address")
        self._IdNum = params.get("IdNum")
        self._Authority = params.get("Authority")
        self._ValidDate = params.get("ValidDate")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._RequestId = params.get("RequestId")


class ImageEnhancementRequest(AbstractModel):
    """ImageEnhancement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ReturnImage: 默认为空，ReturnImage的取值以及含义如下：
“preprocess”: 返回预处理后的图片数据
“origin”：返回原图片数据
" ":不返回图片数据
        :type ReturnImage: str
        :param _TaskType: 默认值为1，指定图像增强方法：
1：切边增强
2：弯曲矫正
202：黑白模式
204：提亮模式
205：灰度模式
207：省墨模式
208：文字锐化（适合非彩色图片）
300:自动增强（自动从301～304选择任务类型）
301：去摩尔纹
302：去除阴影
303：去除模糊 
304：去除过曝
        :type TaskType: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnImage = None
        self._TaskType = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnImage(self):
        return self._ReturnImage

    @ReturnImage.setter
    def ReturnImage(self, ReturnImage):
        self._ReturnImage = ReturnImage

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnImage = params.get("ReturnImage")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageEnhancementResponse(AbstractModel):
    """ImageEnhancement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageTag: 图片数据标识：
“origin”：原图
“preprocess”:预处理后的图
        :type ImageTag: str
        :param _Image: 图片数据，返回预处理后图像或原图像base64字符
        :type Image: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageTag = None
        self._Image = None
        self._RequestId = None

    @property
    def ImageTag(self):
        return self._ImageTag

    @ImageTag.setter
    def ImageTag(self, ImageTag):
        self._ImageTag = ImageTag

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageTag = params.get("ImageTag")
        self._Image = params.get("Image")
        self._RequestId = params.get("RequestId")


class InstitutionOCRRequest(AbstractModel):
    """InstitutionOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstitutionOCRResponse(AbstractModel):
    """InstitutionOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegId: 注册号
        :type RegId: str
        :param _ValidDate: 有效期
        :type ValidDate: str
        :param _Location: 住所
        :type Location: str
        :param _Name: 名称
        :type Name: str
        :param _LegalPerson: 法定代表人
        :type LegalPerson: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegId = None
        self._ValidDate = None
        self._Location = None
        self._Name = None
        self._LegalPerson = None
        self._RequestId = None

    @property
    def RegId(self):
        return self._RegId

    @RegId.setter
    def RegId(self, RegId):
        self._RegId = RegId

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LegalPerson(self):
        return self._LegalPerson

    @LegalPerson.setter
    def LegalPerson(self, LegalPerson):
        self._LegalPerson = LegalPerson

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegId = params.get("RegId")
        self._ValidDate = params.get("ValidDate")
        self._Location = params.get("Location")
        self._Name = params.get("Name")
        self._LegalPerson = params.get("LegalPerson")
        self._RequestId = params.get("RequestId")


class InsuranceBillInfo(AbstractModel):
    """保险单据信息

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
【病案首页】
姓名、性别、出生日期、出院诊断、疾病编码、入院病情等。
【费用清单】
医疗参保人员类别、身份证号、入院方式、结账日期、项目、金额等。
【结算单】
名称、单价、数量、金额、医保内、医保外等。
【医疗发票】
姓名、性别、住院时间、收费项目、金额、合计等。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsuranceBillOCRRequest(AbstractModel):
    """InsuranceBillOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsuranceBillOCRResponse(AbstractModel):
    """InsuranceBillOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InsuranceBillInfos: 保险单据识别结果，具体内容请点击左侧链接。
        :type InsuranceBillInfos: list of InsuranceBillInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InsuranceBillInfos = None
        self._RequestId = None

    @property
    def InsuranceBillInfos(self):
        return self._InsuranceBillInfos

    @InsuranceBillInfos.setter
    def InsuranceBillInfos(self, InsuranceBillInfos):
        self._InsuranceBillInfos = InsuranceBillInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InsuranceBillInfos") is not None:
            self._InsuranceBillInfos = []
            for item in params.get("InsuranceBillInfos"):
                obj = InsuranceBillInfo()
                obj._deserialize(item)
                self._InsuranceBillInfos.append(obj)
        self._RequestId = params.get("RequestId")


class InvoiceDetectInfo(AbstractModel):
    """票据检测结果

    """

    def __init__(self):
        r"""
        :param _Angle: 识别出的图片在混贴票据图片中的旋转角度。
        :type Angle: float
        :param _Type: 识别出的图片所属的票据类型。
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
        :param _Rect: 识别出的图片在混贴票据图片中的位置信息。与Angel结合可以得出原图位置，组成RotatedRect((X+0.5\*Width,Y+0.5\*Height), (Width, Height), Angle)，详情可参考OpenCV文档。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _Image: 入参 ReturnImage 为 True 时返回 Base64 编码后的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        """
        self._Angle = None
        self._Type = None
        self._Rect = None
        self._Image = None

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image


    def _deserialize(self, params):
        self._Angle = params.get("Angle")
        self._Type = params.get("Type")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        self._Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvoiceGeneralInfo(AbstractModel):
    """通用机打发票信息

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段识别（注：下划线表示一个字段）：
发票代码、发票号码、日期、合计金额(小写)、合计金额(大写)、购买方识别号、销售方识别号、校验码、购买方名称、销售方名称、时间、种类、发票消费类型、省、市、是否有公司印章、发票名称、<span style="text-decoration:underline">购买方地址、电话</span>、<span style="text-decoration:underline">销售方地址、电话</span>、购买方开户行及账号、销售方开户行及账号、经办人取票用户、经办人支付信息、经办人商户号、经办人订单号、<span style="text-decoration:underline">货物或应税劳务、服务名称</span>、数量、单价、税率、税额、金额、单位、规格型号、合计税额、合计金额、备注、收款人、复核、开票人、密码区、行业分类
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Value = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvoiceGeneralOCRRequest(AbstractModel):
    """InvoiceGeneralOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvoiceGeneralOCRResponse(AbstractModel):
    """InvoiceGeneralOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvoiceGeneralInfos: 通用机打发票识别结果，具体内容请点击左侧链接。
        :type InvoiceGeneralInfos: list of InvoiceGeneralInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvoiceGeneralInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def InvoiceGeneralInfos(self):
        return self._InvoiceGeneralInfos

    @InvoiceGeneralInfos.setter
    def InvoiceGeneralInfos(self, InvoiceGeneralInfos):
        self._InvoiceGeneralInfos = InvoiceGeneralInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InvoiceGeneralInfos") is not None:
            self._InvoiceGeneralInfos = []
            for item in params.get("InvoiceGeneralInfos"):
                obj = InvoiceGeneralInfo()
                obj._deserialize(item)
                self._InvoiceGeneralInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class InvoiceItem(AbstractModel):
    """混贴票据单张发票识别信息

    """

    def __init__(self):
        r"""
        :param _Code: 识别结果。
OK：表示识别成功；FailedOperation.UnsupportedInvoice：表示不支持识别；
FailedOperation.UnKnowError：表示识别失败；
其它错误码见各个票据接口的定义。
        :type Code: str
        :param _Type: 识别出的图片所属的票据类型。
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
17：医疗发票
        :type Type: int
        :param _Polygon: 该发票在原图片中的四点坐标。
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param _Angle: 识别出的图片在混贴票据图片中的旋转角度。
        :type Angle: float
        :param _SingleInvoiceInfos: 识别到的内容。
        :type SingleInvoiceInfos: :class:`tencentcloud.ocr.v20181119.models.SingleInvoiceItem`
        :param _Page: 发票处于识别图片或PDF文件中的页教，默认从1开始。
        :type Page: int
        :param _SubType: 发票详细类型，详见票据识别（高级版）接口文档说明中 SubType 返回值说明
        :type SubType: str
        :param _TypeDescription: 发票类型描述，详见票据识别（高级版）接口文档说明中 TypeDescription  返回值说明
        :type TypeDescription: str
        :param _CutImage: 切割单图文件，Base64编码后的切图后的图片文件，开启 EnableCutImage 后进行返回
        :type CutImage: str
        :param _SubTypeDescription: 发票详细类型描述，详见上方 SubType 返回值说明
        :type SubTypeDescription: str
        :param _ItemPolygon: 该发票中所有字段坐标信息。包括字段英文名称、字段值所在位置四点坐标、字段所属行号，具体内容请点击左侧链接。
        :type ItemPolygon: list of ItemPolygonInfo
        """
        self._Code = None
        self._Type = None
        self._Polygon = None
        self._Angle = None
        self._SingleInvoiceInfos = None
        self._Page = None
        self._SubType = None
        self._TypeDescription = None
        self._CutImage = None
        self._SubTypeDescription = None
        self._ItemPolygon = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def SingleInvoiceInfos(self):
        return self._SingleInvoiceInfos

    @SingleInvoiceInfos.setter
    def SingleInvoiceInfos(self, SingleInvoiceInfos):
        self._SingleInvoiceInfos = SingleInvoiceInfos

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TypeDescription(self):
        return self._TypeDescription

    @TypeDescription.setter
    def TypeDescription(self, TypeDescription):
        self._TypeDescription = TypeDescription

    @property
    def CutImage(self):
        return self._CutImage

    @CutImage.setter
    def CutImage(self, CutImage):
        self._CutImage = CutImage

    @property
    def SubTypeDescription(self):
        return self._SubTypeDescription

    @SubTypeDescription.setter
    def SubTypeDescription(self, SubTypeDescription):
        self._SubTypeDescription = SubTypeDescription

    @property
    def ItemPolygon(self):
        return self._ItemPolygon

    @ItemPolygon.setter
    def ItemPolygon(self, ItemPolygon):
        self._ItemPolygon = ItemPolygon


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Type = params.get("Type")
        if params.get("Polygon") is not None:
            self._Polygon = Polygon()
            self._Polygon._deserialize(params.get("Polygon"))
        self._Angle = params.get("Angle")
        if params.get("SingleInvoiceInfos") is not None:
            self._SingleInvoiceInfos = SingleInvoiceItem()
            self._SingleInvoiceInfos._deserialize(params.get("SingleInvoiceInfos"))
        self._Page = params.get("Page")
        self._SubType = params.get("SubType")
        self._TypeDescription = params.get("TypeDescription")
        self._CutImage = params.get("CutImage")
        self._SubTypeDescription = params.get("SubTypeDescription")
        if params.get("ItemPolygon") is not None:
            self._ItemPolygon = []
            for item in params.get("ItemPolygon"):
                obj = ItemPolygonInfo()
                obj._deserialize(item)
                self._ItemPolygon.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemCoord(AbstractModel):
    """文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）

    """

    def __init__(self):
        r"""
        :param _X: 左上角x
        :type X: int
        :param _Y: 左上角y
        :type Y: int
        :param _Width: 宽width
        :type Width: int
        :param _Height: 高height
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
        


class ItemInfo(AbstractModel):
    """智能结构化元素组

    """

    def __init__(self):
        r"""
        :param _Key: key信息组
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: :class:`tencentcloud.ocr.v20181119.models.Key`
        :param _Value: Value信息组
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.ocr.v20181119.models.Value`
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        if params.get("Key") is not None:
            self._Key = Key()
            self._Key._deserialize(params.get("Key"))
        if params.get("Value") is not None:
            self._Value = Value()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPolygonInfo(AbstractModel):
    """发票字段坐标信息。包括字段英文名称、字段值所在位置的四点坐标、字段所属行号，具体内容请点击左侧链接。

    """

    def __init__(self):
        r"""
        :param _Key: 发票的英文字段名称（如Title）
        :type Key: str
        :param _Polygon: 字段值所在位置的四点坐标
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param _Row: 字段属于第几行，用于相同字段的排版，如发票明细表格项目，普通字段使用默认值为-1，表示无列排版。
        :type Row: int
        """
        self._Key = None
        self._Polygon = None
        self._Row = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def Row(self):
        return self._Row

    @Row.setter
    def Row(self, Row):
        self._Row = Row


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Polygon") is not None:
            self._Polygon = Polygon()
            self._Polygon._deserialize(params.get("Polygon"))
        self._Row = params.get("Row")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Key(AbstractModel):
    """key信息组

    """

    def __init__(self):
        r"""
        :param _AutoName: 自动识别的字段名称
        :type AutoName: str
        :param _ConfigName: 定义的字段名称（传key的名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigName: str
        """
        self._AutoName = None
        self._ConfigName = None

    @property
    def AutoName(self):
        return self._AutoName

    @AutoName.setter
    def AutoName(self, AutoName):
        self._AutoName = AutoName

    @property
    def ConfigName(self):
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName


    def _deserialize(self, params):
        self._AutoName = params.get("AutoName")
        self._ConfigName = params.get("ConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateInfo(AbstractModel):
    """全部车牌信息

    """

    def __init__(self):
        r"""
        :param _Number: 识别出的车牌号码。
        :type Number: str
        :param _Confidence: 置信度，0 - 100 之间。
        :type Confidence: int
        :param _Rect: 文本行在原图片中的像素坐标框。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _Color: 识别出的车牌颜色，目前支持颜色包括 “白”、“黑”、“蓝”、“绿“、“黄”、“黄绿”、“临牌”、“喷漆”、“其它”。
        :type Color: str
        """
        self._Number = None
        self._Confidence = None
        self._Rect = None
        self._Color = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateOCRRequest(AbstractModel):
    """LicensePlateOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicensePlateOCRResponse(AbstractModel):
    """LicensePlateOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Number: 识别出的车牌号码。
        :type Number: str
        :param _Confidence: 置信度，0 - 100 之间。
        :type Confidence: int
        :param _Rect: 文本行在原图片中的像素坐标框。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _Color: 识别出的车牌颜色，目前支持颜色包括 “白”、“黑”、“蓝”、“绿“、“黄”、“黄绿”、“临牌”、“喷漆”、“其它”。
        :type Color: str
        :param _LicensePlateInfos: 全部车牌信息。
        :type LicensePlateInfos: list of LicensePlateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Number = None
        self._Confidence = None
        self._Rect = None
        self._Color = None
        self._LicensePlateInfos = None
        self._RequestId = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def LicensePlateInfos(self):
        return self._LicensePlateInfos

    @LicensePlateInfos.setter
    def LicensePlateInfos(self, LicensePlateInfos):
        self._LicensePlateInfos = LicensePlateInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Number = params.get("Number")
        self._Confidence = params.get("Confidence")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        self._Color = params.get("Color")
        if params.get("LicensePlateInfos") is not None:
            self._LicensePlateInfos = []
            for item in params.get("LicensePlateInfos"):
                obj = LicensePlateInfo()
                obj._deserialize(item)
                self._LicensePlateInfos.append(obj)
        self._RequestId = params.get("RequestId")


class LineInfo(AbstractModel):
    """按行输出，行序号

    """

    def __init__(self):
        r"""
        :param _Lines: 每行的一个元素
        :type Lines: list of ItemInfo
        """
        self._Lines = None

    @property
    def Lines(self):
        return self._Lines

    @Lines.setter
    def Lines(self, Lines):
        self._Lines = Lines


    def _deserialize(self, params):
        if params.get("Lines") is not None:
            self._Lines = []
            for item in params.get("Lines"):
                obj = ItemInfo()
                obj._deserialize(item)
                self._Lines.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRRequest(AbstractModel):
    """MLIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。( 中国地区之外不支持这个字段 )
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _RetImage: 是否返回图片，默认false
        :type RetImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._RetImage = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RetImage(self):
        return self._RetImage

    @RetImage.setter
    def RetImage(self, RetImage):
        self._RetImage = RetImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDCardOCRResponse(AbstractModel):
    """MLIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 身份证号
        :type ID: str
        :param _Name: 姓名
        :type Name: str
        :param _Address: 地址
        :type Address: str
        :param _Sex: 性别
        :type Sex: str
        :param _Warn: 告警码
-9103	证照翻拍告警
-9102	证照复印件告警
-9106       证件遮挡告警
-9107       模糊图片告警
        :type Warn: list of int
        :param _Image: 证件图片
        :type Image: str
        :param _AdvancedInfo: 此字段为扩展字段。
返回字段识别结果的置信度，格式如下
{
  字段名:{
    Confidence:0.9999
  }
}
        :type AdvancedInfo: str
        :param _Type: 证件类型
MyKad  身份证
MyPR    永居证
MyTentera   军官证
MyKAS    临时身份证
POLIS  警察证
IKAD   劳工证
MyKid 儿童卡
        :type Type: str
        :param _Birthday: 出生日期（目前该字段仅支持IKAD劳工证、MyKad 身份证）
        :type Birthday: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ID = None
        self._Name = None
        self._Address = None
        self._Sex = None
        self._Warn = None
        self._Image = None
        self._AdvancedInfo = None
        self._Type = None
        self._Birthday = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Warn(self):
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        self._Warn = Warn

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Address = params.get("Address")
        self._Sex = params.get("Sex")
        self._Warn = params.get("Warn")
        self._Image = params.get("Image")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._Type = params.get("Type")
        self._Birthday = params.get("Birthday")
        self._RequestId = params.get("RequestId")


class MLIDPassportOCRRequest(AbstractModel):
    """MLIDPassportOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
        :type ImageBase64: str
        :param _RetImage: 是否返回图片，默认false
        :type RetImage: bool
        """
        self._ImageBase64 = None
        self._RetImage = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def RetImage(self):
        return self._RetImage

    @RetImage.setter
    def RetImage(self, RetImage):
        self._RetImage = RetImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._RetImage = params.get("RetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MLIDPassportOCRResponse(AbstractModel):
    """MLIDPassportOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 护照ID
        :type ID: str
        :param _Name: 姓名
        :type Name: str
        :param _DateOfBirth: 出生日期
        :type DateOfBirth: str
        :param _Sex: 性别（F女，M男）
        :type Sex: str
        :param _DateOfExpiration: 有效期
        :type DateOfExpiration: str
        :param _IssuingCountry: 发行国
        :type IssuingCountry: str
        :param _Nationality: 国家地区代码
        :type Nationality: str
        :param _Warn: 告警码
-9103	证照翻拍告警
-9102	证照复印件告警（包括黑白复印件、彩色复印件）
-9106       证件遮挡告警
        :type Warn: list of int
        :param _Image: 证件图片
        :type Image: str
        :param _AdvancedInfo: 扩展字段:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param _CodeSet: 最下方第一行 MRZ Code 序列
        :type CodeSet: str
        :param _CodeCrc: 最下方第二行 MRZ Code 序列
        :type CodeCrc: str
        :param _Surname: 姓
注意：此字段可能返回 null，表示取不到有效值。
        :type Surname: str
        :param _GivenName: 名
注意：此字段可能返回 null，表示取不到有效值。
        :type GivenName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ID = None
        self._Name = None
        self._DateOfBirth = None
        self._Sex = None
        self._DateOfExpiration = None
        self._IssuingCountry = None
        self._Nationality = None
        self._Warn = None
        self._Image = None
        self._AdvancedInfo = None
        self._CodeSet = None
        self._CodeCrc = None
        self._Surname = None
        self._GivenName = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DateOfBirth(self):
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self._DateOfBirth = DateOfBirth

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def DateOfExpiration(self):
        return self._DateOfExpiration

    @DateOfExpiration.setter
    def DateOfExpiration(self, DateOfExpiration):
        self._DateOfExpiration = DateOfExpiration

    @property
    def IssuingCountry(self):
        return self._IssuingCountry

    @IssuingCountry.setter
    def IssuingCountry(self, IssuingCountry):
        self._IssuingCountry = IssuingCountry

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Warn(self):
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        self._Warn = Warn

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def CodeSet(self):
        return self._CodeSet

    @CodeSet.setter
    def CodeSet(self, CodeSet):
        self._CodeSet = CodeSet

    @property
    def CodeCrc(self):
        return self._CodeCrc

    @CodeCrc.setter
    def CodeCrc(self, CodeCrc):
        self._CodeCrc = CodeCrc

    @property
    def Surname(self):
        return self._Surname

    @Surname.setter
    def Surname(self, Surname):
        self._Surname = Surname

    @property
    def GivenName(self):
        return self._GivenName

    @GivenName.setter
    def GivenName(self, GivenName):
        self._GivenName = GivenName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._DateOfBirth = params.get("DateOfBirth")
        self._Sex = params.get("Sex")
        self._DateOfExpiration = params.get("DateOfExpiration")
        self._IssuingCountry = params.get("IssuingCountry")
        self._Nationality = params.get("Nationality")
        self._Warn = params.get("Warn")
        self._Image = params.get("Image")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._CodeSet = params.get("CodeSet")
        self._CodeCrc = params.get("CodeCrc")
        self._Surname = params.get("Surname")
        self._GivenName = params.get("GivenName")
        self._RequestId = params.get("RequestId")


class MachinePrintedInvoice(AbstractModel):
    """通用机打发票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Date: 开票日期
        :type Date: str
        :param _Time: 时间
        :type Time: str
        :param _CheckCode: 校验码
        :type CheckCode: str
        :param _Ciphertext: 密码区
        :type Ciphertext: str
        :param _Category: 种类
        :type Category: str
        :param _PretaxAmount: 税前金额
        :type PretaxAmount: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Tax: 合计税额
        :type Tax: str
        :param _IndustryClass: 行业分类
        :type IndustryClass: str
        :param _Seller: 销售方名称
        :type Seller: str
        :param _SellerTaxID: 销售方纳税人识别号
        :type SellerTaxID: str
        :param _SellerAddrTel: 销售方地址电话
        :type SellerAddrTel: str
        :param _SellerBankAccount: 销售方银行账号
        :type SellerBankAccount: str
        :param _Buyer: 购买方名称
        :type Buyer: str
        :param _BuyerTaxID: 购买方纳税人识别号
        :type BuyerTaxID: str
        :param _BuyerAddrTel: 购买方地址电话
        :type BuyerAddrTel: str
        :param _BuyerBankAccount: 购买方银行账号
        :type BuyerBankAccount: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _CompanySealMark: 是否有公司印章（0：没有，1：有）
        :type CompanySealMark: int
        :param _ElectronicMark: 是否为浙江/广东通用机打发票（0：没有，1：有）
        :type ElectronicMark: int
        :param _Issuer: 开票人
        :type Issuer: str
        :param _Receiptor: 收款人
        :type Receiptor: str
        :param _Reviewer: 复核人
        :type Reviewer: str
        :param _Remark: 备注
        :type Remark: str
        :param _PaymentInfo: 经办人支付信息
        :type PaymentInfo: str
        :param _TicketPickupUser: 经办人取票用户
        :type TicketPickupUser: str
        :param _MerchantNumber: 经办人商户号
        :type MerchantNumber: str
        :param _OrderNumber: 经办人订单号
        :type OrderNumber: str
        :param _GeneralMachineItems: 条目
        :type GeneralMachineItems: list of GeneralMachineItem
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._Time = None
        self._CheckCode = None
        self._Ciphertext = None
        self._Category = None
        self._PretaxAmount = None
        self._Total = None
        self._TotalCn = None
        self._Tax = None
        self._IndustryClass = None
        self._Seller = None
        self._SellerTaxID = None
        self._SellerAddrTel = None
        self._SellerBankAccount = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._BuyerAddrTel = None
        self._BuyerBankAccount = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._CompanySealMark = None
        self._ElectronicMark = None
        self._Issuer = None
        self._Receiptor = None
        self._Reviewer = None
        self._Remark = None
        self._PaymentInfo = None
        self._TicketPickupUser = None
        self._MerchantNumber = None
        self._OrderNumber = None
        self._GeneralMachineItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def IndustryClass(self):
        return self._IndustryClass

    @IndustryClass.setter
    def IndustryClass(self, IndustryClass):
        self._IndustryClass = IndustryClass

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerAddrTel(self):
        return self._SellerAddrTel

    @SellerAddrTel.setter
    def SellerAddrTel(self, SellerAddrTel):
        self._SellerAddrTel = SellerAddrTel

    @property
    def SellerBankAccount(self):
        return self._SellerBankAccount

    @SellerBankAccount.setter
    def SellerBankAccount(self, SellerBankAccount):
        self._SellerBankAccount = SellerBankAccount

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def BuyerAddrTel(self):
        return self._BuyerAddrTel

    @BuyerAddrTel.setter
    def BuyerAddrTel(self, BuyerAddrTel):
        self._BuyerAddrTel = BuyerAddrTel

    @property
    def BuyerBankAccount(self):
        return self._BuyerBankAccount

    @BuyerBankAccount.setter
    def BuyerBankAccount(self, BuyerBankAccount):
        self._BuyerBankAccount = BuyerBankAccount

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def ElectronicMark(self):
        return self._ElectronicMark

    @ElectronicMark.setter
    def ElectronicMark(self, ElectronicMark):
        self._ElectronicMark = ElectronicMark

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Receiptor(self):
        return self._Receiptor

    @Receiptor.setter
    def Receiptor(self, Receiptor):
        self._Receiptor = Receiptor

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PaymentInfo(self):
        return self._PaymentInfo

    @PaymentInfo.setter
    def PaymentInfo(self, PaymentInfo):
        self._PaymentInfo = PaymentInfo

    @property
    def TicketPickupUser(self):
        return self._TicketPickupUser

    @TicketPickupUser.setter
    def TicketPickupUser(self, TicketPickupUser):
        self._TicketPickupUser = TicketPickupUser

    @property
    def MerchantNumber(self):
        return self._MerchantNumber

    @MerchantNumber.setter
    def MerchantNumber(self, MerchantNumber):
        self._MerchantNumber = MerchantNumber

    @property
    def OrderNumber(self):
        return self._OrderNumber

    @OrderNumber.setter
    def OrderNumber(self, OrderNumber):
        self._OrderNumber = OrderNumber

    @property
    def GeneralMachineItems(self):
        return self._GeneralMachineItems

    @GeneralMachineItems.setter
    def GeneralMachineItems(self, GeneralMachineItems):
        self._GeneralMachineItems = GeneralMachineItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._Time = params.get("Time")
        self._CheckCode = params.get("CheckCode")
        self._Ciphertext = params.get("Ciphertext")
        self._Category = params.get("Category")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Tax = params.get("Tax")
        self._IndustryClass = params.get("IndustryClass")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerAddrTel = params.get("SellerAddrTel")
        self._SellerBankAccount = params.get("SellerBankAccount")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._BuyerAddrTel = params.get("BuyerAddrTel")
        self._BuyerBankAccount = params.get("BuyerBankAccount")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._CompanySealMark = params.get("CompanySealMark")
        self._ElectronicMark = params.get("ElectronicMark")
        self._Issuer = params.get("Issuer")
        self._Receiptor = params.get("Receiptor")
        self._Reviewer = params.get("Reviewer")
        self._Remark = params.get("Remark")
        self._PaymentInfo = params.get("PaymentInfo")
        self._TicketPickupUser = params.get("TicketPickupUser")
        self._MerchantNumber = params.get("MerchantNumber")
        self._OrderNumber = params.get("OrderNumber")
        if params.get("GeneralMachineItems") is not None:
            self._GeneralMachineItems = []
            for item in params.get("GeneralMachineItems"):
                obj = GeneralMachineItem()
                obj._deserialize(item)
                self._GeneralMachineItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRRequest(AbstractModel):
    """MainlandPermitOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _RetProfile: 是否返回头像。默认不返回。
        :type RetProfile: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._RetProfile = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RetProfile(self):
        return self._RetProfile

    @RetProfile.setter
    def RetProfile(self, RetProfile):
        self._RetProfile = RetProfile


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._RetProfile = params.get("RetProfile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandPermitOCRResponse(AbstractModel):
    """MainlandPermitOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 中文姓名
        :type Name: str
        :param _EnglishName: 英文姓名
        :type EnglishName: str
        :param _Sex: 性别
        :type Sex: str
        :param _Birthday: 出生日期
        :type Birthday: str
        :param _IssueAuthority: 签发机关
        :type IssueAuthority: str
        :param _ValidDate: 有效期限
        :type ValidDate: str
        :param _Number: 证件号
        :type Number: str
        :param _IssueAddress: 签发地点
        :type IssueAddress: str
        :param _IssueNumber: 签发次数
        :type IssueNumber: str
        :param _Type: 证件类别， 如：台湾居民来往大陆通行证、港澳居民来往内地通行证。
        :type Type: str
        :param _Profile: RetProfile为True时返回头像字段， Base64编码
        :type Profile: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._EnglishName = None
        self._Sex = None
        self._Birthday = None
        self._IssueAuthority = None
        self._ValidDate = None
        self._Number = None
        self._IssueAddress = None
        self._IssueNumber = None
        self._Type = None
        self._Profile = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnglishName(self):
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def IssueAuthority(self):
        return self._IssueAuthority

    @IssueAuthority.setter
    def IssueAuthority(self, IssueAuthority):
        self._IssueAuthority = IssueAuthority

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def IssueAddress(self):
        return self._IssueAddress

    @IssueAddress.setter
    def IssueAddress(self, IssueAddress):
        self._IssueAddress = IssueAddress

    @property
    def IssueNumber(self):
        return self._IssueNumber

    @IssueNumber.setter
    def IssueNumber(self, IssueNumber):
        self._IssueNumber = IssueNumber

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Profile(self):
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EnglishName = params.get("EnglishName")
        self._Sex = params.get("Sex")
        self._Birthday = params.get("Birthday")
        self._IssueAuthority = params.get("IssueAuthority")
        self._ValidDate = params.get("ValidDate")
        self._Number = params.get("Number")
        self._IssueAddress = params.get("IssueAddress")
        self._IssueNumber = params.get("IssueNumber")
        self._Type = params.get("Type")
        self._Profile = params.get("Profile")
        self._RequestId = params.get("RequestId")


class MedicalInvoice(AbstractModel):
    """医疗票据信息

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Date: 开票日期
        :type Date: str
        :param _CheckCode: 校验码
        :type CheckCode: str
        :param _Place: 发票属地
        :type Place: str
        :param _Reviewer: 复核人
        :type Reviewer: str
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Total = None
        self._TotalCn = None
        self._Date = None
        self._CheckCode = None
        self._Place = None
        self._Reviewer = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Place(self):
        return self._Place

    @Place.setter
    def Place(self, Place):
        self._Place = Place

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Date = params.get("Date")
        self._CheckCode = params.get("CheckCode")
        self._Place = params.get("Place")
        self._Reviewer = params.get("Reviewer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MedicalInvoiceInfo(AbstractModel):
    """医疗发票识别结果

    """

    def __init__(self):
        r"""
        :param _MedicalInvoiceItems: 医疗发票识别结果条目
        :type MedicalInvoiceItems: list of MedicalInvoiceItem
        """
        self._MedicalInvoiceItems = None

    @property
    def MedicalInvoiceItems(self):
        return self._MedicalInvoiceItems

    @MedicalInvoiceItems.setter
    def MedicalInvoiceItems(self, MedicalInvoiceItems):
        self._MedicalInvoiceItems = MedicalInvoiceItems


    def _deserialize(self, params):
        if params.get("MedicalInvoiceItems") is not None:
            self._MedicalInvoiceItems = []
            for item in params.get("MedicalInvoiceItems"):
                obj = MedicalInvoiceItem()
                obj._deserialize(item)
                self._MedicalInvoiceItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MedicalInvoiceItem(AbstractModel):
    """医疗发票识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称
<table><tr><td>分类</td><td>name</td></tr><tr><td>票据基本信息</td><td>发票名称</td></tr><tr><td></td><td>票据代码</td></tr><tr><td></td><td>票据号码</td></tr><tr><td></td><td>电子票据代码</td></tr><tr><td></td><td>电子票据号码</td></tr><tr><td></td><td>交款人统一社会信用代码</td></tr><tr><td></td><td>校验码</td></tr><tr><td></td><td>交款人</td></tr><tr><td></td><td>开票日期</td></tr><tr><td></td><td>收款单位</td></tr><tr><td></td><td>复核人</td></tr><tr><td></td><td>收款人</td></tr><tr><td></td><td>业务流水号</td></tr><tr><td></td><td>门诊号</td></tr><tr><td></td><td>就诊日期</td></tr><tr><td></td><td>医疗机构类型</td></tr><tr><td></td><td>医保类型</td></tr><tr><td></td><td>医保编号</td></tr><tr><td></td><td>性别</td></tr><tr><td></td><td>医保统筹基金支付</td></tr><tr><td></td><td>其他支付</td></tr><tr><td></td><td>个人账户支付</td></tr><tr><td></td><td>个人现金支付</td></tr><tr><td></td><td>个人自付</td></tr><tr><td></td><td>个人自费</td></tr><tr><td></td><td>病历号</td></tr><tr><td></td><td>住院号</td></tr><tr><td></td><td>住院科别</td></tr><tr><td></td><td>住院时间</td></tr><tr><td></td><td>预缴金额</td></tr><tr><td></td><td>补缴金额</td></tr><tr><td></td><td>退费金额</td></tr><tr><td></td><td>发票属地</td></tr><tr><td></td><td>发票类型</td></tr><tr><td>总金额</td><td>总金额大写</td></tr><tr><td></td><td>总金额小写</td></tr><tr><td>收费大项</td><td>大项名称</td></tr><tr><td></td><td>大项金额</td></tr><tr><td>收费细项</td><td>项目名称</td></tr><tr><td></td><td>数量</td></tr><tr><td></td><td>单位</td></tr><tr><td></td><td>金额</td></tr><tr><td></td><td>备注</td></tr><tr><td>票据其他信息</td><td>入院时间</td></tr><tr><td></td><td>出院时间</td></tr><tr><td></td><td>住院天数</td></tr><tr><td></td><td>自付二</td></tr><tr><td></td><td>自付一</td></tr><tr><td></td><td>起付金额</td></tr><tr><td></td><td>超封顶金额</td></tr><tr><td></td><td>自费</td></tr><tr><td></td><td>本次医保范围内金额</td></tr><tr><td></td><td>累计医保内范围金额</td></tr><tr><td></td><td>门诊大额支付</td></tr><tr><td></td><td>残军补助支付</td></tr><tr><td></td><td>年度门诊大额累计支付</td></tr><tr><td></td><td>单位补充险[原公疗]支付</td></tr><tr><td></td><td>社会保障卡号</td></tr><tr><td></td><td>姓名</td></tr><tr><td></td><td>交易流水号</td></tr><tr><td></td><td>本次支付后个人账户余额</td></tr><tr><td></td><td>基金支付</td></tr><tr><td></td><td>现金支付</td></tr><tr><td></td><td>复核</td></tr><tr><td></td><td>自负</td></tr><tr><td></td><td>结算方式</td></tr><tr><td></td><td>医保统筹/公医记账</td></tr><tr><td></td><td>其他</td></tr><tr><td></td><td>个人支付金额</td></tr><tr><td></td><td>欠费</td></tr><tr><td></td><td>退休补充支付</td></tr><tr><td></td><td>医院类型</td></tr><tr><td></td><td>退款</td></tr><tr><td></td><td>补收</td></tr><tr><td></td><td>附加支付</td></tr><tr><td></td><td>分类自负</td></tr><tr><td></td><td>其它</td></tr><tr><td></td><td>预交款</td></tr><tr><td></td><td>个人缴费</td></tr></table>
        :type Name: str
        :param _Content: 识别出的字段名称对应的值，也就是字段name对应的字符串结果
        :type Content: str
        :param _Vertex: 识别出的文本行四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Vertex: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        :param _Coord: 识别出的文本行在旋转纠正之后的图像中的像素坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Content = None
        self._Vertex = None
        self._Coord = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Vertex(self):
        return self._Vertex

    @Vertex.setter
    def Vertex(self, Vertex):
        self._Vertex = Vertex

    @property
    def Coord(self):
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        if params.get("Vertex") is not None:
            self._Vertex = Polygon()
            self._Vertex._deserialize(params.get("Vertex"))
        if params.get("Coord") is not None:
            self._Coord = Rect()
            self._Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceDetectRequest(AbstractModel):
    """MixedInvoiceDetect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnImage: 是否需要返回裁剪后的图片。
        :type ReturnImage: bool
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ReturnImage = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ReturnImage(self):
        return self._ReturnImage

    @ReturnImage.setter
    def ReturnImage(self, ReturnImage):
        self._ReturnImage = ReturnImage

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ReturnImage = params.get("ReturnImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceDetectResponse(AbstractModel):
    """MixedInvoiceDetect返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvoiceDetectInfos: 检测出的票据类型列表，具体内容请点击左侧链接。
        :type InvoiceDetectInfos: list of InvoiceDetectInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvoiceDetectInfos = None
        self._RequestId = None

    @property
    def InvoiceDetectInfos(self):
        return self._InvoiceDetectInfos

    @InvoiceDetectInfos.setter
    def InvoiceDetectInfos(self, InvoiceDetectInfos):
        self._InvoiceDetectInfos = InvoiceDetectInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InvoiceDetectInfos") is not None:
            self._InvoiceDetectInfos = []
            for item in params.get("InvoiceDetectInfos"):
                obj = InvoiceDetectInfo()
                obj._deserialize(item)
                self._InvoiceDetectInfos.append(obj)
        self._RequestId = params.get("RequestId")


class MixedInvoiceItem(AbstractModel):
    """混贴票据单张发票识别信息

    """

    def __init__(self):
        r"""
        :param _Code: 识别结果。
OK：表示识别成功；FailedOperation.UnsupportedInvioce：表示不支持识别；
FailedOperation.UnKnowError：表示识别失败；
其它错误码见各个票据接口的定义。
        :type Code: str
        :param _Type: 识别出的图片所属的票据类型。
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
        :param _Rect: 识别出的图片在混贴票据图片中的位置信息。与Angel结合可以得出原图位置，组成RotatedRect((X+0.5\*Width,Y+0.5\*Height), (Width, Height), Angle)，详情可参考OpenCV文档。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _Angle: 识别出的图片在混贴票据图片中的旋转角度。
        :type Angle: float
        :param _SingleInvoiceInfos: 识别到的内容。
        :type SingleInvoiceInfos: list of SingleInvoiceInfo
        :param _Page: 发票处于识别图片或PDF文件中的页教，默认从1开始。
        :type Page: int
        """
        self._Code = None
        self._Type = None
        self._Rect = None
        self._Angle = None
        self._SingleInvoiceInfos = None
        self._Page = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def SingleInvoiceInfos(self):
        return self._SingleInvoiceInfos

    @SingleInvoiceInfos.setter
    def SingleInvoiceInfos(self, SingleInvoiceInfos):
        self._SingleInvoiceInfos = SingleInvoiceInfos

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Type = params.get("Type")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        self._Angle = params.get("Angle")
        if params.get("SingleInvoiceInfos") is not None:
            self._SingleInvoiceInfos = []
            for item in params.get("SingleInvoiceInfos"):
                obj = SingleInvoiceInfo()
                obj._deserialize(item)
                self._SingleInvoiceInfos.append(obj)
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceOCRRequest(AbstractModel):
    """MixedInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Types: 需要识别的票据类型列表，为空或不填表示识别全部类型。
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
----------------------
-1：其他发票,（只传入此类型时，图片均采用其他票类型进行识别）
        :type Types: list of int
        :param _ReturnOther: 是否识别其他类型发票，默认为Yes
Yes：识别其他类型发票
No：不识别其他类型发票
        :type ReturnOther: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param _ReturnMultiplePage: 是否开启PDF多页识别，默认值为false，开启后可同时支持多页PDF的识别返回，仅支持返回文件前30页。开启后IsPDF和PdfPageNumber入参不进行控制。
        :type ReturnMultiplePage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Types = None
        self._ReturnOther = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._ReturnMultiplePage = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def ReturnOther(self):
        return self._ReturnOther

    @ReturnOther.setter
    def ReturnOther(self, ReturnOther):
        self._ReturnOther = ReturnOther

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def ReturnMultiplePage(self):
        return self._ReturnMultiplePage

    @ReturnMultiplePage.setter
    def ReturnMultiplePage(self, ReturnMultiplePage):
        self._ReturnMultiplePage = ReturnMultiplePage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Types = params.get("Types")
        self._ReturnOther = params.get("ReturnOther")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._ReturnMultiplePage = params.get("ReturnMultiplePage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixedInvoiceOCRResponse(AbstractModel):
    """MixedInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MixedInvoiceItems: 混贴票据识别结果，具体内容请点击左侧链接。
        :type MixedInvoiceItems: list of MixedInvoiceItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MixedInvoiceItems = None
        self._RequestId = None

    @property
    def MixedInvoiceItems(self):
        return self._MixedInvoiceItems

    @MixedInvoiceItems.setter
    def MixedInvoiceItems(self, MixedInvoiceItems):
        self._MixedInvoiceItems = MixedInvoiceItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MixedInvoiceItems") is not None:
            self._MixedInvoiceItems = []
            for item in params.get("MixedInvoiceItems"):
                obj = MixedInvoiceItem()
                obj._deserialize(item)
                self._MixedInvoiceItems.append(obj)
        self._RequestId = params.get("RequestId")


class MotorVehicleSaleInvoice(AbstractModel):
    """机动车销售统一发票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Date: 开票日期
        :type Date: str
        :param _PretaxAmount: 税前金额
        :type PretaxAmount: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Seller: 销售方名称
        :type Seller: str
        :param _SellerTaxID: 销售方单位代码
        :type SellerTaxID: str
        :param _SellerTel: 销售方电话
        :type SellerTel: str
        :param _SellerAddress: 销售方地址
        :type SellerAddress: str
        :param _SellerBank: 销售方开户行
        :type SellerBank: str
        :param _SellerBankAccount: 销售方银行账号
        :type SellerBankAccount: str
        :param _Buyer: 购买方名称
        :type Buyer: str
        :param _BuyerTaxID: 购买方纳税人识别号
        :type BuyerTaxID: str
        :param _BuyerID: 购买方身份证号码/组织机构代码
        :type BuyerID: str
        :param _TaxAuthorities: 主管税务机关
        :type TaxAuthorities: str
        :param _TaxAuthoritiesCode: 主管税务机关代码
        :type TaxAuthoritiesCode: str
        :param _VIN: 车辆识别代码
        :type VIN: str
        :param _VehicleModel: 厂牌型号
        :type VehicleModel: str
        :param _VehicleEngineCode: 发动机号码
        :type VehicleEngineCode: str
        :param _CertificateNumber: 合格证号
        :type CertificateNumber: str
        :param _InspectionNumber: 商检单号
        :type InspectionNumber: str
        :param _MachineID: 机器编号
        :type MachineID: str
        :param _VehicleType: 车辆类型
        :type VehicleType: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _Tax: 合计税额
        :type Tax: str
        :param _TaxRate: 税率
        :type TaxRate: str
        :param _CompanySealMark: 是否有公司印章（0：没有，1：有）
        :type CompanySealMark: int
        :param _Tonnage: 吨位
        :type Tonnage: str
        :param _Remark: 备注
        :type Remark: str
        :param _FormType: 发票联次
        :type FormType: str
        :param _FormName: 发票联名
        :type FormName: str
        :param _Issuer: 开票人
        :type Issuer: str
        :param _TaxNum: 完税凭证号码
        :type TaxNum: str
        :param _MaxPeopleNum: 限乘人数
        :type MaxPeopleNum: str
        :param _Origin: 产地
        :type Origin: str
        :param _MachineCode: 机打发票代码
        :type MachineCode: str
        :param _MachineNumber: 机打发票号码
        :type MachineNumber: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._PretaxAmount = None
        self._Total = None
        self._TotalCn = None
        self._Seller = None
        self._SellerTaxID = None
        self._SellerTel = None
        self._SellerAddress = None
        self._SellerBank = None
        self._SellerBankAccount = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._BuyerID = None
        self._TaxAuthorities = None
        self._TaxAuthoritiesCode = None
        self._VIN = None
        self._VehicleModel = None
        self._VehicleEngineCode = None
        self._CertificateNumber = None
        self._InspectionNumber = None
        self._MachineID = None
        self._VehicleType = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._Tax = None
        self._TaxRate = None
        self._CompanySealMark = None
        self._Tonnage = None
        self._Remark = None
        self._FormType = None
        self._FormName = None
        self._Issuer = None
        self._TaxNum = None
        self._MaxPeopleNum = None
        self._Origin = None
        self._MachineCode = None
        self._MachineNumber = None
        self._QRCodeMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerTel(self):
        return self._SellerTel

    @SellerTel.setter
    def SellerTel(self, SellerTel):
        self._SellerTel = SellerTel

    @property
    def SellerAddress(self):
        return self._SellerAddress

    @SellerAddress.setter
    def SellerAddress(self, SellerAddress):
        self._SellerAddress = SellerAddress

    @property
    def SellerBank(self):
        return self._SellerBank

    @SellerBank.setter
    def SellerBank(self, SellerBank):
        self._SellerBank = SellerBank

    @property
    def SellerBankAccount(self):
        return self._SellerBankAccount

    @SellerBankAccount.setter
    def SellerBankAccount(self, SellerBankAccount):
        self._SellerBankAccount = SellerBankAccount

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def BuyerID(self):
        return self._BuyerID

    @BuyerID.setter
    def BuyerID(self, BuyerID):
        self._BuyerID = BuyerID

    @property
    def TaxAuthorities(self):
        return self._TaxAuthorities

    @TaxAuthorities.setter
    def TaxAuthorities(self, TaxAuthorities):
        self._TaxAuthorities = TaxAuthorities

    @property
    def TaxAuthoritiesCode(self):
        return self._TaxAuthoritiesCode

    @TaxAuthoritiesCode.setter
    def TaxAuthoritiesCode(self, TaxAuthoritiesCode):
        self._TaxAuthoritiesCode = TaxAuthoritiesCode

    @property
    def VIN(self):
        return self._VIN

    @VIN.setter
    def VIN(self, VIN):
        self._VIN = VIN

    @property
    def VehicleModel(self):
        return self._VehicleModel

    @VehicleModel.setter
    def VehicleModel(self, VehicleModel):
        self._VehicleModel = VehicleModel

    @property
    def VehicleEngineCode(self):
        return self._VehicleEngineCode

    @VehicleEngineCode.setter
    def VehicleEngineCode(self, VehicleEngineCode):
        self._VehicleEngineCode = VehicleEngineCode

    @property
    def CertificateNumber(self):
        return self._CertificateNumber

    @CertificateNumber.setter
    def CertificateNumber(self, CertificateNumber):
        self._CertificateNumber = CertificateNumber

    @property
    def InspectionNumber(self):
        return self._InspectionNumber

    @InspectionNumber.setter
    def InspectionNumber(self, InspectionNumber):
        self._InspectionNumber = InspectionNumber

    @property
    def MachineID(self):
        return self._MachineID

    @MachineID.setter
    def MachineID(self, MachineID):
        self._MachineID = MachineID

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def Tonnage(self):
        return self._Tonnage

    @Tonnage.setter
    def Tonnage(self, Tonnage):
        self._Tonnage = Tonnage

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FormType(self):
        return self._FormType

    @FormType.setter
    def FormType(self, FormType):
        self._FormType = FormType

    @property
    def FormName(self):
        return self._FormName

    @FormName.setter
    def FormName(self, FormName):
        self._FormName = FormName

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def TaxNum(self):
        return self._TaxNum

    @TaxNum.setter
    def TaxNum(self, TaxNum):
        self._TaxNum = TaxNum

    @property
    def MaxPeopleNum(self):
        return self._MaxPeopleNum

    @MaxPeopleNum.setter
    def MaxPeopleNum(self, MaxPeopleNum):
        self._MaxPeopleNum = MaxPeopleNum

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def MachineCode(self):
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def MachineNumber(self):
        return self._MachineNumber

    @MachineNumber.setter
    def MachineNumber(self, MachineNumber):
        self._MachineNumber = MachineNumber

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerTel = params.get("SellerTel")
        self._SellerAddress = params.get("SellerAddress")
        self._SellerBank = params.get("SellerBank")
        self._SellerBankAccount = params.get("SellerBankAccount")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._BuyerID = params.get("BuyerID")
        self._TaxAuthorities = params.get("TaxAuthorities")
        self._TaxAuthoritiesCode = params.get("TaxAuthoritiesCode")
        self._VIN = params.get("VIN")
        self._VehicleModel = params.get("VehicleModel")
        self._VehicleEngineCode = params.get("VehicleEngineCode")
        self._CertificateNumber = params.get("CertificateNumber")
        self._InspectionNumber = params.get("InspectionNumber")
        self._MachineID = params.get("MachineID")
        self._VehicleType = params.get("VehicleType")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Tax = params.get("Tax")
        self._TaxRate = params.get("TaxRate")
        self._CompanySealMark = params.get("CompanySealMark")
        self._Tonnage = params.get("Tonnage")
        self._Remark = params.get("Remark")
        self._FormType = params.get("FormType")
        self._FormName = params.get("FormName")
        self._Issuer = params.get("Issuer")
        self._TaxNum = params.get("TaxNum")
        self._MaxPeopleNum = params.get("MaxPeopleNum")
        self._Origin = params.get("Origin")
        self._MachineCode = params.get("MachineCode")
        self._MachineNumber = params.get("MachineNumber")
        self._QRCodeMark = params.get("QRCodeMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NonTaxIncomeBill(AbstractModel):
    """非税收入

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Number: 发票号码
        :type Number: str
        :param _Code: 发票代码
        :type Code: str
        :param _CheckCode: 校验码
        :type CheckCode: str
        :param _Date: 开票日期
        :type Date: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Buyer: 交款人名称
        :type Buyer: str
        :param _BuyerTaxID: 交款人纳税人识别号
        :type BuyerTaxID: str
        :param _Seller: 收款人名称
        :type Seller: str
        :param _SellerCompany: 收款单位名称
        :type SellerCompany: str
        :param _Remark: 备注
        :type Remark: str
        :param _CurrencyCode: 币种
        :type CurrencyCode: str
        :param _Reviewer: 复核人
        :type Reviewer: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _OtherInfo: 其他信息
        :type OtherInfo: str
        :param _PaymentCode: 缴款码
        :type PaymentCode: str
        :param _ReceiveUnitCode: 执收单位编码
        :type ReceiveUnitCode: str
        :param _Receiver: 执收单位名称
        :type Receiver: str
        :param _Operator: 经办人
        :type Operator: str
        :param _PayerAccount: 付款人账号
        :type PayerAccount: str
        :param _PayerBank: 付款人开户银行
        :type PayerBank: str
        :param _ReceiverAccount: 收款人账号
        :type ReceiverAccount: str
        :param _ReceiverBank: 收款人开户银行
        :type ReceiverBank: str
        :param _NonTaxItems: 条目
        :type NonTaxItems: list of NonTaxItem
        """
        self._Title = None
        self._Number = None
        self._Code = None
        self._CheckCode = None
        self._Date = None
        self._Total = None
        self._TotalCn = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._Seller = None
        self._SellerCompany = None
        self._Remark = None
        self._CurrencyCode = None
        self._Reviewer = None
        self._QRCodeMark = None
        self._OtherInfo = None
        self._PaymentCode = None
        self._ReceiveUnitCode = None
        self._Receiver = None
        self._Operator = None
        self._PayerAccount = None
        self._PayerBank = None
        self._ReceiverAccount = None
        self._ReceiverBank = None
        self._NonTaxItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerCompany(self):
        return self._SellerCompany

    @SellerCompany.setter
    def SellerCompany(self, SellerCompany):
        self._SellerCompany = SellerCompany

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CurrencyCode(self):
        return self._CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, CurrencyCode):
        self._CurrencyCode = CurrencyCode

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def OtherInfo(self):
        return self._OtherInfo

    @OtherInfo.setter
    def OtherInfo(self, OtherInfo):
        self._OtherInfo = OtherInfo

    @property
    def PaymentCode(self):
        return self._PaymentCode

    @PaymentCode.setter
    def PaymentCode(self, PaymentCode):
        self._PaymentCode = PaymentCode

    @property
    def ReceiveUnitCode(self):
        return self._ReceiveUnitCode

    @ReceiveUnitCode.setter
    def ReceiveUnitCode(self, ReceiveUnitCode):
        self._ReceiveUnitCode = ReceiveUnitCode

    @property
    def Receiver(self):
        return self._Receiver

    @Receiver.setter
    def Receiver(self, Receiver):
        self._Receiver = Receiver

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def PayerAccount(self):
        return self._PayerAccount

    @PayerAccount.setter
    def PayerAccount(self, PayerAccount):
        self._PayerAccount = PayerAccount

    @property
    def PayerBank(self):
        return self._PayerBank

    @PayerBank.setter
    def PayerBank(self, PayerBank):
        self._PayerBank = PayerBank

    @property
    def ReceiverAccount(self):
        return self._ReceiverAccount

    @ReceiverAccount.setter
    def ReceiverAccount(self, ReceiverAccount):
        self._ReceiverAccount = ReceiverAccount

    @property
    def ReceiverBank(self):
        return self._ReceiverBank

    @ReceiverBank.setter
    def ReceiverBank(self, ReceiverBank):
        self._ReceiverBank = ReceiverBank

    @property
    def NonTaxItems(self):
        return self._NonTaxItems

    @NonTaxItems.setter
    def NonTaxItems(self, NonTaxItems):
        self._NonTaxItems = NonTaxItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._Code = params.get("Code")
        self._CheckCode = params.get("CheckCode")
        self._Date = params.get("Date")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._Seller = params.get("Seller")
        self._SellerCompany = params.get("SellerCompany")
        self._Remark = params.get("Remark")
        self._CurrencyCode = params.get("CurrencyCode")
        self._Reviewer = params.get("Reviewer")
        self._QRCodeMark = params.get("QRCodeMark")
        self._OtherInfo = params.get("OtherInfo")
        self._PaymentCode = params.get("PaymentCode")
        self._ReceiveUnitCode = params.get("ReceiveUnitCode")
        self._Receiver = params.get("Receiver")
        self._Operator = params.get("Operator")
        self._PayerAccount = params.get("PayerAccount")
        self._PayerBank = params.get("PayerBank")
        self._ReceiverAccount = params.get("ReceiverAccount")
        self._ReceiverBank = params.get("ReceiverBank")
        if params.get("NonTaxItems") is not None:
            self._NonTaxItems = []
            for item in params.get("NonTaxItems"):
                obj = NonTaxItem()
                obj._deserialize(item)
                self._NonTaxItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NonTaxItem(AbstractModel):
    """非税收入条目

    """

    def __init__(self):
        r"""
        :param _ItemID: 项目编码
        :type ItemID: str
        :param _Name: 项目名称
        :type Name: str
        :param _Unit: 单位
        :type Unit: str
        :param _Quantity: 数量
        :type Quantity: str
        :param _Standard: 标准
        :type Standard: str
        :param _Total: 金额
        :type Total: str
        """
        self._ItemID = None
        self._Name = None
        self._Unit = None
        self._Quantity = None
        self._Standard = None
        self._Total = None

    @property
    def ItemID(self):
        return self._ItemID

    @ItemID.setter
    def ItemID(self, ItemID):
        self._ItemID = ItemID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Standard(self):
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._ItemID = params.get("ItemID")
        self._Name = params.get("Name")
        self._Unit = params.get("Unit")
        self._Quantity = params.get("Quantity")
        self._Standard = params.get("Standard")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnlineTaxiItineraryInfo(AbstractModel):
    """网约车行程单识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、 机打代码、 发票号码、 发动机号码、 合格证号、 机打号码、 价税合计(小写)、 销货单位名称、 身份证号码/组织机构代码、 购买方名称、 销售方纳税人识别号、 购买方纳税人识别号、主管税务机关、 主管税务机关代码、 开票日期、 不含税价(小写)、 吨位、增值税税率或征收率、 车辆识别代号/车架号码、 增值税税额、 厂牌型号、 省、 市、 发票消费类型、 销售方电话、 销售方账号、 产地、 进口证明书号、 车辆类型、 机器编号、备注、开票人、限乘人数、商检单号、销售方地址、销售方开户银行、价税合计、发票类型。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        :param _Row: 字段所在行，下标从0开始，非行字段或未能识别行号的返回-1
        :type Row: int
        """
        self._Name = None
        self._Value = None
        self._Row = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Row(self):
        return self._Row

    @Row.setter
    def Row(self, Row):
        self._Row = Row


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Row = params.get("Row")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgCodeCertOCRRequest(AbstractModel):
    """OrgCodeCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgCodeCertOCRResponse(AbstractModel):
    """OrgCodeCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgCode: 代码
        :type OrgCode: str
        :param _Name: 机构名称
        :type Name: str
        :param _Address: 地址
        :type Address: str
        :param _ValidDate: 有效期
        :type ValidDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgCode = None
        self._Name = None
        self._Address = None
        self._ValidDate = None
        self._RequestId = None

    @property
    def OrgCode(self):
        return self._OrgCode

    @OrgCode.setter
    def OrgCode(self, OrgCode):
        self._OrgCode = OrgCode

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgCode = params.get("OrgCode")
        self._Name = params.get("Name")
        self._Address = params.get("Address")
        self._ValidDate = params.get("ValidDate")
        self._RequestId = params.get("RequestId")


class OtherInvoice(AbstractModel):
    """其他发票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Total: 金额
        :type Total: str
        :param _OtherInvoiceListItems: 列表
        :type OtherInvoiceListItems: list of OtherInvoiceItem
        :param _OtherInvoiceTableItems: 表格
        :type OtherInvoiceTableItems: list of OtherInvoiceList
        :param _Date: 发票日期
        :type Date: str
        """
        self._Title = None
        self._Total = None
        self._OtherInvoiceListItems = None
        self._OtherInvoiceTableItems = None
        self._Date = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def OtherInvoiceListItems(self):
        return self._OtherInvoiceListItems

    @OtherInvoiceListItems.setter
    def OtherInvoiceListItems(self, OtherInvoiceListItems):
        self._OtherInvoiceListItems = OtherInvoiceListItems

    @property
    def OtherInvoiceTableItems(self):
        return self._OtherInvoiceTableItems

    @OtherInvoiceTableItems.setter
    def OtherInvoiceTableItems(self, OtherInvoiceTableItems):
        self._OtherInvoiceTableItems = OtherInvoiceTableItems

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Total = params.get("Total")
        if params.get("OtherInvoiceListItems") is not None:
            self._OtherInvoiceListItems = []
            for item in params.get("OtherInvoiceListItems"):
                obj = OtherInvoiceItem()
                obj._deserialize(item)
                self._OtherInvoiceListItems.append(obj)
        if params.get("OtherInvoiceTableItems") is not None:
            self._OtherInvoiceTableItems = []
            for item in params.get("OtherInvoiceTableItems"):
                obj = OtherInvoiceList()
                obj._deserialize(item)
                self._OtherInvoiceTableItems.append(obj)
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoiceItem(AbstractModel):
    """OtherInvoiceItem

    """

    def __init__(self):
        r"""
        :param _Name: 票面key值
        :type Name: str
        :param _Value: 票面value值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInvoiceList(AbstractModel):
    """其他票Table

    """

    def __init__(self):
        r"""
        :param _OtherInvoiceItemList: 列表
        :type OtherInvoiceItemList: list of OtherInvoiceItem
        """
        self._OtherInvoiceItemList = None

    @property
    def OtherInvoiceItemList(self):
        return self._OtherInvoiceItemList

    @OtherInvoiceItemList.setter
    def OtherInvoiceItemList(self, OtherInvoiceItemList):
        self._OtherInvoiceItemList = OtherInvoiceItemList


    def _deserialize(self, params):
        if params.get("OtherInvoiceItemList") is not None:
            self._OtherInvoiceItemList = []
            for item in params.get("OtherInvoiceItemList"):
                obj = OtherInvoiceItem()
                obj._deserialize(item)
                self._OtherInvoiceItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PassInvoiceInfo(AbstractModel):
    """通行费发票信息

    """

    def __init__(self):
        r"""
        :param _NumberPlate: 通行费车牌号
        :type NumberPlate: str
        :param _Type: 通行费类型
        :type Type: str
        :param _PassDateBegin: 通行日期起
        :type PassDateBegin: str
        :param _PassDateEnd: 通行日期止
        :type PassDateEnd: str
        :param _TaxClassifyCode: 税收分类编码
        :type TaxClassifyCode: str
        """
        self._NumberPlate = None
        self._Type = None
        self._PassDateBegin = None
        self._PassDateEnd = None
        self._TaxClassifyCode = None

    @property
    def NumberPlate(self):
        return self._NumberPlate

    @NumberPlate.setter
    def NumberPlate(self, NumberPlate):
        self._NumberPlate = NumberPlate

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PassDateBegin(self):
        return self._PassDateBegin

    @PassDateBegin.setter
    def PassDateBegin(self, PassDateBegin):
        self._PassDateBegin = PassDateBegin

    @property
    def PassDateEnd(self):
        return self._PassDateEnd

    @PassDateEnd.setter
    def PassDateEnd(self, PassDateEnd):
        self._PassDateEnd = PassDateEnd

    @property
    def TaxClassifyCode(self):
        return self._TaxClassifyCode

    @TaxClassifyCode.setter
    def TaxClassifyCode(self, TaxClassifyCode):
        self._TaxClassifyCode = TaxClassifyCode


    def _deserialize(self, params):
        self._NumberPlate = params.get("NumberPlate")
        self._Type = params.get("Type")
        self._PassDateBegin = params.get("PassDateBegin")
        self._PassDateEnd = params.get("PassDateEnd")
        self._TaxClassifyCode = params.get("TaxClassifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PassportOCRRequest(AbstractModel):
    """PassportOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param _Type: 默认填写CN
支持中国大陆地区护照。
        :type Type: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Type = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PassportOCRResponse(AbstractModel):
    """PassportOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Country: 国家码
        :type Country: str
        :param _PassportNo: 护照号
        :type PassportNo: str
        :param _Sex: 性别
        :type Sex: str
        :param _Nationality: 国籍
        :type Nationality: str
        :param _BirthDate: 出生日期
        :type BirthDate: str
        :param _BirthPlace: 出生地点
        :type BirthPlace: str
        :param _IssueDate: 签发日期
        :type IssueDate: str
        :param _IssuePlace: 签发地点
        :type IssuePlace: str
        :param _ExpiryDate: 有效期
        :type ExpiryDate: str
        :param _Signature: 持证人签名
        :type Signature: str
        :param _CodeSet: 最下方第一行 MRZ Code 序列
        :type CodeSet: str
        :param _CodeCrc: 最下方第二行 MRZ Code 序列
        :type CodeCrc: str
        :param _Name: 姓名
        :type Name: str
        :param _FamilyName: 姓
        :type FamilyName: str
        :param _FirstName: 名
        :type FirstName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Country = None
        self._PassportNo = None
        self._Sex = None
        self._Nationality = None
        self._BirthDate = None
        self._BirthPlace = None
        self._IssueDate = None
        self._IssuePlace = None
        self._ExpiryDate = None
        self._Signature = None
        self._CodeSet = None
        self._CodeCrc = None
        self._Name = None
        self._FamilyName = None
        self._FirstName = None
        self._RequestId = None

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def PassportNo(self):
        return self._PassportNo

    @PassportNo.setter
    def PassportNo(self, PassportNo):
        self._PassportNo = PassportNo

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def BirthDate(self):
        return self._BirthDate

    @BirthDate.setter
    def BirthDate(self, BirthDate):
        self._BirthDate = BirthDate

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def IssuePlace(self):
        return self._IssuePlace

    @IssuePlace.setter
    def IssuePlace(self, IssuePlace):
        self._IssuePlace = IssuePlace

    @property
    def ExpiryDate(self):
        return self._ExpiryDate

    @ExpiryDate.setter
    def ExpiryDate(self, ExpiryDate):
        self._ExpiryDate = ExpiryDate

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def CodeSet(self):
        return self._CodeSet

    @CodeSet.setter
    def CodeSet(self, CodeSet):
        self._CodeSet = CodeSet

    @property
    def CodeCrc(self):
        return self._CodeCrc

    @CodeCrc.setter
    def CodeCrc(self, CodeCrc):
        self._CodeCrc = CodeCrc

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FamilyName(self):
        return self._FamilyName

    @FamilyName.setter
    def FamilyName(self, FamilyName):
        self._FamilyName = FamilyName

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._PassportNo = params.get("PassportNo")
        self._Sex = params.get("Sex")
        self._Nationality = params.get("Nationality")
        self._BirthDate = params.get("BirthDate")
        self._BirthPlace = params.get("BirthPlace")
        self._IssueDate = params.get("IssueDate")
        self._IssuePlace = params.get("IssuePlace")
        self._ExpiryDate = params.get("ExpiryDate")
        self._Signature = params.get("Signature")
        self._CodeSet = params.get("CodeSet")
        self._CodeCrc = params.get("CodeCrc")
        self._Name = params.get("Name")
        self._FamilyName = params.get("FamilyName")
        self._FirstName = params.get("FirstName")
        self._RequestId = params.get("RequestId")


class PermitOCRRequest(AbstractModel):
    """PermitOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermitOCRResponse(AbstractModel):
    """PermitOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _EnglishName: 英文姓名
        :type EnglishName: str
        :param _Number: 证件号
        :type Number: str
        :param _Sex: 性别
        :type Sex: str
        :param _ValidDate: 有效期限
        :type ValidDate: str
        :param _IssueAuthority: 签发机关
        :type IssueAuthority: str
        :param _IssueAddress: 签发地点
        :type IssueAddress: str
        :param _Birthday: 出生日期
        :type Birthday: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._EnglishName = None
        self._Number = None
        self._Sex = None
        self._ValidDate = None
        self._IssueAuthority = None
        self._IssueAddress = None
        self._Birthday = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnglishName(self):
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def ValidDate(self):
        return self._ValidDate

    @ValidDate.setter
    def ValidDate(self, ValidDate):
        self._ValidDate = ValidDate

    @property
    def IssueAuthority(self):
        return self._IssueAuthority

    @IssueAuthority.setter
    def IssueAuthority(self, IssueAuthority):
        self._IssueAuthority = IssueAuthority

    @property
    def IssueAddress(self):
        return self._IssueAddress

    @IssueAddress.setter
    def IssueAddress(self, IssueAddress):
        self._IssueAddress = IssueAddress

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EnglishName = params.get("EnglishName")
        self._Number = params.get("Number")
        self._Sex = params.get("Sex")
        self._ValidDate = params.get("ValidDate")
        self._IssueAuthority = params.get("IssueAuthority")
        self._IssueAddress = params.get("IssueAddress")
        self._Birthday = params.get("Birthday")
        self._RequestId = params.get("RequestId")


class Polygon(AbstractModel):
    """文本的坐标，以四个顶点坐标表示
    注意：此字段可能返回 null，表示取不到有效值

    """

    def __init__(self):
        r"""
        :param _LeftTop: 左上顶点坐标
        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _RightTop: 右上顶点坐标
        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _RightBottom: 右下顶点坐标
        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _LeftBottom: 左下顶点坐标
        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        self._LeftTop = None
        self._RightTop = None
        self._RightBottom = None
        self._LeftBottom = None

    @property
    def LeftTop(self):
        return self._LeftTop

    @LeftTop.setter
    def LeftTop(self, LeftTop):
        self._LeftTop = LeftTop

    @property
    def RightTop(self):
        return self._RightTop

    @RightTop.setter
    def RightTop(self, RightTop):
        self._RightTop = RightTop

    @property
    def RightBottom(self):
        return self._RightBottom

    @RightBottom.setter
    def RightBottom(self, RightBottom):
        self._RightBottom = RightBottom

    @property
    def LeftBottom(self):
        return self._LeftBottom

    @LeftBottom.setter
    def LeftBottom(self, LeftBottom):
        self._LeftBottom = LeftBottom


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self._LeftTop = Coord()
            self._LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self._RightTop = Coord()
            self._RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self._RightBottom = Coord()
            self._RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self._LeftBottom = Coord()
            self._LeftBottom._deserialize(params.get("LeftBottom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PropOwnerCertOCRRequest(AbstractModel):
    """PropOwnerCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PropOwnerCertOCRResponse(AbstractModel):
    """PropOwnerCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Owner: 房地产权利人
        :type Owner: str
        :param _Possession: 共有情况
        :type Possession: str
        :param _RegisterTime: 登记时间
        :type RegisterTime: str
        :param _Purpose: 规划用途
        :type Purpose: str
        :param _Nature: 房屋性质
        :type Nature: str
        :param _Location: 房地坐落
        :type Location: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Owner = None
        self._Possession = None
        self._RegisterTime = None
        self._Purpose = None
        self._Nature = None
        self._Location = None
        self._RequestId = None

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Possession(self):
        return self._Possession

    @Possession.setter
    def Possession(self, Possession):
        self._Possession = Possession

    @property
    def RegisterTime(self):
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def Purpose(self):
        return self._Purpose

    @Purpose.setter
    def Purpose(self, Purpose):
        self._Purpose = Purpose

    @property
    def Nature(self):
        return self._Nature

    @Nature.setter
    def Nature(self, Nature):
        self._Nature = Nature

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Owner = params.get("Owner")
        self._Possession = params.get("Possession")
        self._RegisterTime = params.get("RegisterTime")
        self._Purpose = params.get("Purpose")
        self._Nature = params.get("Nature")
        self._Location = params.get("Location")
        self._RequestId = params.get("RequestId")


class QrcodeImgSize(AbstractModel):
    """图片大小

    """

    def __init__(self):
        r"""
        :param _Wide: 宽
        :type Wide: int
        :param _High: 高
        :type High: int
        """
        self._Wide = None
        self._High = None

    @property
    def Wide(self):
        return self._Wide

    @Wide.setter
    def Wide(self, Wide):
        self._Wide = Wide

    @property
    def High(self):
        return self._High

    @High.setter
    def High(self, High):
        self._High = High


    def _deserialize(self, params):
        self._Wide = params.get("Wide")
        self._High = params.get("High")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QrcodeOCRRequest(AbstractModel):
    """QrcodeOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，支持PNG、JPG、JPEG格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，支持PNG、JPG、JPEG格式。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QrcodeOCRResponse(AbstractModel):
    """QrcodeOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeResults: 二维码/条形码识别结果信息，具体内容请点击左侧链接。
        :type CodeResults: list of QrcodeResultsInfo
        :param _ImgSize: 图片大小，具体内容请点击左侧链接。
        :type ImgSize: :class:`tencentcloud.ocr.v20181119.models.QrcodeImgSize`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeResults = None
        self._ImgSize = None
        self._RequestId = None

    @property
    def CodeResults(self):
        return self._CodeResults

    @CodeResults.setter
    def CodeResults(self, CodeResults):
        self._CodeResults = CodeResults

    @property
    def ImgSize(self):
        return self._ImgSize

    @ImgSize.setter
    def ImgSize(self, ImgSize):
        self._ImgSize = ImgSize

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CodeResults") is not None:
            self._CodeResults = []
            for item in params.get("CodeResults"):
                obj = QrcodeResultsInfo()
                obj._deserialize(item)
                self._CodeResults.append(obj)
        if params.get("ImgSize") is not None:
            self._ImgSize = QrcodeImgSize()
            self._ImgSize._deserialize(params.get("ImgSize"))
        self._RequestId = params.get("RequestId")


class QrcodePositionObj(AbstractModel):
    """二维码/条形码坐标信息

    """

    def __init__(self):
        r"""
        :param _LeftTop: 左上顶点坐标（如果是条形码，X和Y都为-1）
        :type LeftTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _RightTop: 右上顶点坐标（如果是条形码，X和Y都为-1）
        :type RightTop: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _RightBottom: 右下顶点坐标（如果是条形码，X和Y都为-1）
        :type RightBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        :param _LeftBottom: 左下顶点坐标（如果是条形码，X和Y都为-1）
        :type LeftBottom: :class:`tencentcloud.ocr.v20181119.models.Coord`
        """
        self._LeftTop = None
        self._RightTop = None
        self._RightBottom = None
        self._LeftBottom = None

    @property
    def LeftTop(self):
        return self._LeftTop

    @LeftTop.setter
    def LeftTop(self, LeftTop):
        self._LeftTop = LeftTop

    @property
    def RightTop(self):
        return self._RightTop

    @RightTop.setter
    def RightTop(self, RightTop):
        self._RightTop = RightTop

    @property
    def RightBottom(self):
        return self._RightBottom

    @RightBottom.setter
    def RightBottom(self, RightBottom):
        self._RightBottom = RightBottom

    @property
    def LeftBottom(self):
        return self._LeftBottom

    @LeftBottom.setter
    def LeftBottom(self, LeftBottom):
        self._LeftBottom = LeftBottom


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self._LeftTop = Coord()
            self._LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self._RightTop = Coord()
            self._RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self._RightBottom = Coord()
            self._RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self._LeftBottom = Coord()
            self._LeftBottom._deserialize(params.get("LeftBottom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QrcodeResultsInfo(AbstractModel):
    """二维码/条形码识别结果信息

    """

    def __init__(self):
        r"""
        :param _TypeName: 类型（二维码、条形码）
        :type TypeName: str
        :param _Url: 二维码/条形码包含的地址
        :type Url: str
        :param _Position: 二维码/条形码坐标
        :type Position: :class:`tencentcloud.ocr.v20181119.models.QrcodePositionObj`
        """
        self._TypeName = None
        self._Url = None
        self._Position = None

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._Url = params.get("Url")
        if params.get("Position") is not None:
            self._Position = QrcodePositionObj()
            self._Position._deserialize(params.get("Position"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuestionBlockObj(AbstractModel):
    """数学试题识别结构化对象

    """

    def __init__(self):
        r"""
        :param _QuestionArr: 数学试题识别结构化信息数组
        :type QuestionArr: list of QuestionObj
        :param _QuestionBboxCoord: 题目主体区域检测框在图片中的像素坐标
        :type QuestionBboxCoord: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._QuestionArr = None
        self._QuestionBboxCoord = None

    @property
    def QuestionArr(self):
        return self._QuestionArr

    @QuestionArr.setter
    def QuestionArr(self, QuestionArr):
        self._QuestionArr = QuestionArr

    @property
    def QuestionBboxCoord(self):
        return self._QuestionBboxCoord

    @QuestionBboxCoord.setter
    def QuestionBboxCoord(self, QuestionBboxCoord):
        self._QuestionBboxCoord = QuestionBboxCoord


    def _deserialize(self, params):
        if params.get("QuestionArr") is not None:
            self._QuestionArr = []
            for item in params.get("QuestionArr"):
                obj = QuestionObj()
                obj._deserialize(item)
                self._QuestionArr.append(obj)
        if params.get("QuestionBboxCoord") is not None:
            self._QuestionBboxCoord = Rect()
            self._QuestionBboxCoord._deserialize(params.get("QuestionBboxCoord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuestionObj(AbstractModel):
    """试题识别结构化信息

    """

    def __init__(self):
        r"""
        :param _QuestionTextNo: 题号
        :type QuestionTextNo: str
        :param _QuestionTextType: 题型：
1: "选择题"
2: "填空题"
3: "解答题"
        :type QuestionTextType: int
        :param _QuestionText: 题干
        :type QuestionText: str
        :param _QuestionOptions: 选择题选项，包含1个或多个option
        :type QuestionOptions: str
        :param _QuestionSubquestion: 所有子题的question属性
        :type QuestionSubquestion: str
        :param _QuestionImageCoords: 示意图检测框在的图片中的像素坐标
        :type QuestionImageCoords: list of Rect
        """
        self._QuestionTextNo = None
        self._QuestionTextType = None
        self._QuestionText = None
        self._QuestionOptions = None
        self._QuestionSubquestion = None
        self._QuestionImageCoords = None

    @property
    def QuestionTextNo(self):
        return self._QuestionTextNo

    @QuestionTextNo.setter
    def QuestionTextNo(self, QuestionTextNo):
        self._QuestionTextNo = QuestionTextNo

    @property
    def QuestionTextType(self):
        return self._QuestionTextType

    @QuestionTextType.setter
    def QuestionTextType(self, QuestionTextType):
        self._QuestionTextType = QuestionTextType

    @property
    def QuestionText(self):
        return self._QuestionText

    @QuestionText.setter
    def QuestionText(self, QuestionText):
        self._QuestionText = QuestionText

    @property
    def QuestionOptions(self):
        return self._QuestionOptions

    @QuestionOptions.setter
    def QuestionOptions(self, QuestionOptions):
        self._QuestionOptions = QuestionOptions

    @property
    def QuestionSubquestion(self):
        return self._QuestionSubquestion

    @QuestionSubquestion.setter
    def QuestionSubquestion(self, QuestionSubquestion):
        self._QuestionSubquestion = QuestionSubquestion

    @property
    def QuestionImageCoords(self):
        return self._QuestionImageCoords

    @QuestionImageCoords.setter
    def QuestionImageCoords(self, QuestionImageCoords):
        self._QuestionImageCoords = QuestionImageCoords


    def _deserialize(self, params):
        self._QuestionTextNo = params.get("QuestionTextNo")
        self._QuestionTextType = params.get("QuestionTextType")
        self._QuestionText = params.get("QuestionText")
        self._QuestionOptions = params.get("QuestionOptions")
        self._QuestionSubquestion = params.get("QuestionSubquestion")
        if params.get("QuestionImageCoords") is not None:
            self._QuestionImageCoords = []
            for item in params.get("QuestionImageCoords"):
                obj = Rect()
                obj._deserialize(item)
                self._QuestionImageCoords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInvoice(AbstractModel):
    """定额发票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _CompanySealMark: 是否有公司印章（0：没有，1：有）
        :type CompanySealMark: int
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Total = None
        self._TotalCn = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._QRCodeMark = None
        self._CompanySealMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._QRCodeMark = params.get("QRCodeMark")
        self._CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInvoiceOCRRequest(AbstractModel):
    """QuotaInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInvoiceOCRResponse(AbstractModel):
    """QuotaInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvoiceNum: 发票号码
        :type InvoiceNum: str
        :param _InvoiceCode: 发票代码
        :type InvoiceCode: str
        :param _Rate: 大写金额
        :type Rate: str
        :param _RateNum: 小写金额
        :type RateNum: str
        :param _InvoiceType: 发票消费类型
        :type InvoiceType: str
        :param _Province: 省
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _City: 市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _HasStamp: 是否有公司印章（1有 0无 空为识别不出）
注意：此字段可能返回 null，表示取不到有效值。
        :type HasStamp: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvoiceNum = None
        self._InvoiceCode = None
        self._Rate = None
        self._RateNum = None
        self._InvoiceType = None
        self._Province = None
        self._City = None
        self._HasStamp = None
        self._RequestId = None

    @property
    def InvoiceNum(self):
        return self._InvoiceNum

    @InvoiceNum.setter
    def InvoiceNum(self, InvoiceNum):
        self._InvoiceNum = InvoiceNum

    @property
    def InvoiceCode(self):
        return self._InvoiceCode

    @InvoiceCode.setter
    def InvoiceCode(self, InvoiceCode):
        self._InvoiceCode = InvoiceCode

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def RateNum(self):
        return self._RateNum

    @RateNum.setter
    def RateNum(self, RateNum):
        self._RateNum = RateNum

    @property
    def InvoiceType(self):
        return self._InvoiceType

    @InvoiceType.setter
    def InvoiceType(self, InvoiceType):
        self._InvoiceType = InvoiceType

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def HasStamp(self):
        return self._HasStamp

    @HasStamp.setter
    def HasStamp(self, HasStamp):
        self._HasStamp = HasStamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvoiceNum = params.get("InvoiceNum")
        self._InvoiceCode = params.get("InvoiceCode")
        self._Rate = params.get("Rate")
        self._RateNum = params.get("RateNum")
        self._InvoiceType = params.get("InvoiceType")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._HasStamp = params.get("HasStamp")
        self._RequestId = params.get("RequestId")


class RecognizeContainerOCRRequest(AbstractModel):
    """RecognizeContainerOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeContainerOCRResponse(AbstractModel):
    """RecognizeContainerOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerId: 集装箱箱号
        :type ContainerId: str
        :param _ContainerType: 集装箱类型
        :type ContainerType: str
        :param _GrossKG: 集装箱总重量，单位：千克（KG）
        :type GrossKG: str
        :param _GrossLB: 集装箱总重量，单位：磅（LB）
        :type GrossLB: str
        :param _PayloadKG: 集装箱有效承重，单位：千克（KG）
        :type PayloadKG: str
        :param _PayloadLB: 集装箱有效承重，单位：磅（LB）
        :type PayloadLB: str
        :param _CapacityM3: 集装箱容量，单位：立方米
        :type CapacityM3: str
        :param _CapacityFT3: 集装箱容量，单位：立英尺
        :type CapacityFT3: str
        :param _Warn: 告警码
-9926	集装箱箱号不完整或者不清晰
-9927	集装箱类型不完整或者不清晰
        :type Warn: list of int
        :param _TareKG: 集装箱自身重量，单位：千克（KG）
        :type TareKG: str
        :param _TareLB: 集装箱自身重量，单位：磅（LB）
        :type TareLB: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ContainerId = None
        self._ContainerType = None
        self._GrossKG = None
        self._GrossLB = None
        self._PayloadKG = None
        self._PayloadLB = None
        self._CapacityM3 = None
        self._CapacityFT3 = None
        self._Warn = None
        self._TareKG = None
        self._TareLB = None
        self._RequestId = None

    @property
    def ContainerId(self):
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId

    @property
    def ContainerType(self):
        return self._ContainerType

    @ContainerType.setter
    def ContainerType(self, ContainerType):
        self._ContainerType = ContainerType

    @property
    def GrossKG(self):
        return self._GrossKG

    @GrossKG.setter
    def GrossKG(self, GrossKG):
        self._GrossKG = GrossKG

    @property
    def GrossLB(self):
        return self._GrossLB

    @GrossLB.setter
    def GrossLB(self, GrossLB):
        self._GrossLB = GrossLB

    @property
    def PayloadKG(self):
        return self._PayloadKG

    @PayloadKG.setter
    def PayloadKG(self, PayloadKG):
        self._PayloadKG = PayloadKG

    @property
    def PayloadLB(self):
        return self._PayloadLB

    @PayloadLB.setter
    def PayloadLB(self, PayloadLB):
        self._PayloadLB = PayloadLB

    @property
    def CapacityM3(self):
        return self._CapacityM3

    @CapacityM3.setter
    def CapacityM3(self, CapacityM3):
        self._CapacityM3 = CapacityM3

    @property
    def CapacityFT3(self):
        return self._CapacityFT3

    @CapacityFT3.setter
    def CapacityFT3(self, CapacityFT3):
        self._CapacityFT3 = CapacityFT3

    @property
    def Warn(self):
        return self._Warn

    @Warn.setter
    def Warn(self, Warn):
        self._Warn = Warn

    @property
    def TareKG(self):
        return self._TareKG

    @TareKG.setter
    def TareKG(self, TareKG):
        self._TareKG = TareKG

    @property
    def TareLB(self):
        return self._TareLB

    @TareLB.setter
    def TareLB(self, TareLB):
        self._TareLB = TareLB

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ContainerId = params.get("ContainerId")
        self._ContainerType = params.get("ContainerType")
        self._GrossKG = params.get("GrossKG")
        self._GrossLB = params.get("GrossLB")
        self._PayloadKG = params.get("PayloadKG")
        self._PayloadLB = params.get("PayloadLB")
        self._CapacityM3 = params.get("CapacityM3")
        self._CapacityFT3 = params.get("CapacityFT3")
        self._Warn = params.get("Warn")
        self._TareKG = params.get("TareKG")
        self._TareLB = params.get("TareLB")
        self._RequestId = params.get("RequestId")


class RecognizeGeneralInvoiceRequest(AbstractModel):
    """RecognizeGeneralInvoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 8M。图片下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 8M。图片下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Types: 需要识别的票据类型列表，为空或不填表示识别全部类型。当传入单个类型时，图片均采用该票类型进行处理。
暂不支持多个参数进行局部控制。
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
17：医疗发票
-1：其他发票
        :type Types: list of int
        :param _EnableOther: 是否开启其他票识别，默认值为true，开启后可支持其他发票的智能识别。	
        :type EnableOther: bool
        :param _EnablePdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type EnablePdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，传入时仅支持PDF单页识别，当上传文件为PDF且EnablePdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param _EnableMultiplePage: 是否开启PDF多页识别，默认值为false，开启后可同时支持多页PDF的识别返回，仅支持返回文件前30页。开启后EnablePdf和PdfPageNumber入参不进行控制。
        :type EnableMultiplePage: bool
        :param _EnableCutImage: 是否返回切割图片base64，默认值为false。
        :type EnableCutImage: bool
        :param _EnableItemPolygon: 是否打开字段坐标返回。默认为false。
        :type EnableItemPolygon: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Types = None
        self._EnableOther = None
        self._EnablePdf = None
        self._PdfPageNumber = None
        self._EnableMultiplePage = None
        self._EnableCutImage = None
        self._EnableItemPolygon = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def EnableOther(self):
        return self._EnableOther

    @EnableOther.setter
    def EnableOther(self, EnableOther):
        self._EnableOther = EnableOther

    @property
    def EnablePdf(self):
        return self._EnablePdf

    @EnablePdf.setter
    def EnablePdf(self, EnablePdf):
        self._EnablePdf = EnablePdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def EnableMultiplePage(self):
        return self._EnableMultiplePage

    @EnableMultiplePage.setter
    def EnableMultiplePage(self, EnableMultiplePage):
        self._EnableMultiplePage = EnableMultiplePage

    @property
    def EnableCutImage(self):
        return self._EnableCutImage

    @EnableCutImage.setter
    def EnableCutImage(self, EnableCutImage):
        self._EnableCutImage = EnableCutImage

    @property
    def EnableItemPolygon(self):
        return self._EnableItemPolygon

    @EnableItemPolygon.setter
    def EnableItemPolygon(self, EnableItemPolygon):
        self._EnableItemPolygon = EnableItemPolygon


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Types = params.get("Types")
        self._EnableOther = params.get("EnableOther")
        self._EnablePdf = params.get("EnablePdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._EnableMultiplePage = params.get("EnableMultiplePage")
        self._EnableCutImage = params.get("EnableCutImage")
        self._EnableItemPolygon = params.get("EnableItemPolygon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeGeneralInvoiceResponse(AbstractModel):
    """RecognizeGeneralInvoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MixedInvoiceItems: 混贴票据识别结果，具体内容请点击左侧链接。
        :type MixedInvoiceItems: list of InvoiceItem
        :param _TotalPDFCount: PDF文件总页码
        :type TotalPDFCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MixedInvoiceItems = None
        self._TotalPDFCount = None
        self._RequestId = None

    @property
    def MixedInvoiceItems(self):
        return self._MixedInvoiceItems

    @MixedInvoiceItems.setter
    def MixedInvoiceItems(self, MixedInvoiceItems):
        self._MixedInvoiceItems = MixedInvoiceItems

    @property
    def TotalPDFCount(self):
        return self._TotalPDFCount

    @TotalPDFCount.setter
    def TotalPDFCount(self, TotalPDFCount):
        self._TotalPDFCount = TotalPDFCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MixedInvoiceItems") is not None:
            self._MixedInvoiceItems = []
            for item in params.get("MixedInvoiceItems"):
                obj = InvoiceItem()
                obj._deserialize(item)
                self._MixedInvoiceItems.append(obj)
        self._TotalPDFCount = params.get("TotalPDFCount")
        self._RequestId = params.get("RequestId")


class RecognizeHealthCodeOCRRequest(AbstractModel):
    """RecognizeHealthCodeOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Type: 需要识别的健康码类型列表，为空或不填表示默认为自动识别。
0:自动识别
        :type Type: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Type = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeHealthCodeOCRResponse(AbstractModel):
    """RecognizeHealthCodeOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 持码人姓名，如：王*（允许返回空值）
        :type Name: str
        :param _IDNumber: 持码人身份证号，如：11**************01（允许返回空值）
        :type IDNumber: str
        :param _Time: 健康码更新时间（允许返回空值）
        :type Time: str
        :param _Color: 健康码颜色：绿色、黄色、红色（允许返回空值）
        :type Color: str
        :param _TestingInterval: 核酸检测间隔时长（允许返回空值）
        :type TestingInterval: str
        :param _TestingResult: 核酸检测结果：阴性、阳性、暂无核酸检测记录（允许返回空值）
        :type TestingResult: str
        :param _TestingTime: 核酸检测时间（允许返回空值）
        :type TestingTime: str
        :param _Vaccination: 疫苗接种信息，返回接种针数或接种情况（允许返回空值）
        :type Vaccination: str
        :param _SpotName: 场所名称（允许返回空值）
        :type SpotName: str
        :param _VaccinationTime: 疫苗接种时间
        :type VaccinationTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._IDNumber = None
        self._Time = None
        self._Color = None
        self._TestingInterval = None
        self._TestingResult = None
        self._TestingTime = None
        self._Vaccination = None
        self._SpotName = None
        self._VaccinationTime = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IDNumber(self):
        return self._IDNumber

    @IDNumber.setter
    def IDNumber(self, IDNumber):
        self._IDNumber = IDNumber

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def TestingInterval(self):
        return self._TestingInterval

    @TestingInterval.setter
    def TestingInterval(self, TestingInterval):
        self._TestingInterval = TestingInterval

    @property
    def TestingResult(self):
        return self._TestingResult

    @TestingResult.setter
    def TestingResult(self, TestingResult):
        self._TestingResult = TestingResult

    @property
    def TestingTime(self):
        return self._TestingTime

    @TestingTime.setter
    def TestingTime(self, TestingTime):
        self._TestingTime = TestingTime

    @property
    def Vaccination(self):
        return self._Vaccination

    @Vaccination.setter
    def Vaccination(self, Vaccination):
        self._Vaccination = Vaccination

    @property
    def SpotName(self):
        return self._SpotName

    @SpotName.setter
    def SpotName(self, SpotName):
        self._SpotName = SpotName

    @property
    def VaccinationTime(self):
        return self._VaccinationTime

    @VaccinationTime.setter
    def VaccinationTime(self, VaccinationTime):
        self._VaccinationTime = VaccinationTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IDNumber = params.get("IDNumber")
        self._Time = params.get("Time")
        self._Color = params.get("Color")
        self._TestingInterval = params.get("TestingInterval")
        self._TestingResult = params.get("TestingResult")
        self._TestingTime = params.get("TestingTime")
        self._Vaccination = params.get("Vaccination")
        self._SpotName = params.get("SpotName")
        self._VaccinationTime = params.get("VaccinationTime")
        self._RequestId = params.get("RequestId")


class RecognizeIndonesiaIDCardOCRRequest(AbstractModel):
    """RecognizeIndonesiaIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param _Scene: 场景参数，默认值为V1
可选值：
V1
V2
        :type Scene: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None
        self._Scene = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeIndonesiaIDCardOCRResponse(AbstractModel):
    """RecognizeIndonesiaIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NIK: 证件号码
        :type NIK: str
        :param _Nama: 姓名
        :type Nama: str
        :param _TempatTglLahir: 出生地/出生时间
        :type TempatTglLahir: str
        :param _JenisKelamin: 性别
        :type JenisKelamin: str
        :param _GolDarah: 血型
        :type GolDarah: str
        :param _Alamat: 地址
        :type Alamat: str
        :param _RTRW: 街道
        :type RTRW: str
        :param _KelDesa: 村
        :type KelDesa: str
        :param _Kecamatan: 地区
        :type Kecamatan: str
        :param _Agama: 宗教信仰
        :type Agama: str
        :param _StatusPerkawinan: 婚姻状况
        :type StatusPerkawinan: str
        :param _Perkerjaan: 职业
        :type Perkerjaan: str
        :param _KewargaNegaraan: 国籍
        :type KewargaNegaraan: str
        :param _BerlakuHingga: 身份证有效期限
        :type BerlakuHingga: str
        :param _IssuedDate: 发证日期
        :type IssuedDate: str
        :param _Photo: 人像截图
        :type Photo: str
        :param _Provinsi: 省份，Scene为V2时支持识别
        :type Provinsi: str
        :param _Kota: 城市，Scene为V2时支持识别
        :type Kota: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NIK = None
        self._Nama = None
        self._TempatTglLahir = None
        self._JenisKelamin = None
        self._GolDarah = None
        self._Alamat = None
        self._RTRW = None
        self._KelDesa = None
        self._Kecamatan = None
        self._Agama = None
        self._StatusPerkawinan = None
        self._Perkerjaan = None
        self._KewargaNegaraan = None
        self._BerlakuHingga = None
        self._IssuedDate = None
        self._Photo = None
        self._Provinsi = None
        self._Kota = None
        self._RequestId = None

    @property
    def NIK(self):
        return self._NIK

    @NIK.setter
    def NIK(self, NIK):
        self._NIK = NIK

    @property
    def Nama(self):
        return self._Nama

    @Nama.setter
    def Nama(self, Nama):
        self._Nama = Nama

    @property
    def TempatTglLahir(self):
        return self._TempatTglLahir

    @TempatTglLahir.setter
    def TempatTglLahir(self, TempatTglLahir):
        self._TempatTglLahir = TempatTglLahir

    @property
    def JenisKelamin(self):
        return self._JenisKelamin

    @JenisKelamin.setter
    def JenisKelamin(self, JenisKelamin):
        self._JenisKelamin = JenisKelamin

    @property
    def GolDarah(self):
        return self._GolDarah

    @GolDarah.setter
    def GolDarah(self, GolDarah):
        self._GolDarah = GolDarah

    @property
    def Alamat(self):
        return self._Alamat

    @Alamat.setter
    def Alamat(self, Alamat):
        self._Alamat = Alamat

    @property
    def RTRW(self):
        return self._RTRW

    @RTRW.setter
    def RTRW(self, RTRW):
        self._RTRW = RTRW

    @property
    def KelDesa(self):
        return self._KelDesa

    @KelDesa.setter
    def KelDesa(self, KelDesa):
        self._KelDesa = KelDesa

    @property
    def Kecamatan(self):
        return self._Kecamatan

    @Kecamatan.setter
    def Kecamatan(self, Kecamatan):
        self._Kecamatan = Kecamatan

    @property
    def Agama(self):
        return self._Agama

    @Agama.setter
    def Agama(self, Agama):
        self._Agama = Agama

    @property
    def StatusPerkawinan(self):
        return self._StatusPerkawinan

    @StatusPerkawinan.setter
    def StatusPerkawinan(self, StatusPerkawinan):
        self._StatusPerkawinan = StatusPerkawinan

    @property
    def Perkerjaan(self):
        return self._Perkerjaan

    @Perkerjaan.setter
    def Perkerjaan(self, Perkerjaan):
        self._Perkerjaan = Perkerjaan

    @property
    def KewargaNegaraan(self):
        return self._KewargaNegaraan

    @KewargaNegaraan.setter
    def KewargaNegaraan(self, KewargaNegaraan):
        self._KewargaNegaraan = KewargaNegaraan

    @property
    def BerlakuHingga(self):
        return self._BerlakuHingga

    @BerlakuHingga.setter
    def BerlakuHingga(self, BerlakuHingga):
        self._BerlakuHingga = BerlakuHingga

    @property
    def IssuedDate(self):
        return self._IssuedDate

    @IssuedDate.setter
    def IssuedDate(self, IssuedDate):
        self._IssuedDate = IssuedDate

    @property
    def Photo(self):
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

    @property
    def Provinsi(self):
        return self._Provinsi

    @Provinsi.setter
    def Provinsi(self, Provinsi):
        self._Provinsi = Provinsi

    @property
    def Kota(self):
        return self._Kota

    @Kota.setter
    def Kota(self, Kota):
        self._Kota = Kota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NIK = params.get("NIK")
        self._Nama = params.get("Nama")
        self._TempatTglLahir = params.get("TempatTglLahir")
        self._JenisKelamin = params.get("JenisKelamin")
        self._GolDarah = params.get("GolDarah")
        self._Alamat = params.get("Alamat")
        self._RTRW = params.get("RTRW")
        self._KelDesa = params.get("KelDesa")
        self._Kecamatan = params.get("Kecamatan")
        self._Agama = params.get("Agama")
        self._StatusPerkawinan = params.get("StatusPerkawinan")
        self._Perkerjaan = params.get("Perkerjaan")
        self._KewargaNegaraan = params.get("KewargaNegaraan")
        self._BerlakuHingga = params.get("BerlakuHingga")
        self._IssuedDate = params.get("IssuedDate")
        self._Photo = params.get("Photo")
        self._Provinsi = params.get("Provinsi")
        self._Kota = params.get("Kota")
        self._RequestId = params.get("RequestId")


class RecognizeMedicalInvoiceOCRRequest(AbstractModel):
    """RecognizeMedicalInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的Base64 值。
支持的文件格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载文件经Base64编码后不超过 7M。文件下载时间不超过 3 秒。
输入参数 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的Url 地址。
支持的文件格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载文件经 Base64 编码后不超过 7M。文件下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ReturnVertex: 是否需要返回识别出的文本行在原图上的四点坐标，默认不返回
        :type ReturnVertex: bool
        :param _ReturnCoord: 是否需要返回识别出的文本行在旋转纠正之后的图像中的四点坐标，默认不返回
        :type ReturnCoord: bool
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnVertex = None
        self._ReturnCoord = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnVertex(self):
        return self._ReturnVertex

    @ReturnVertex.setter
    def ReturnVertex(self, ReturnVertex):
        self._ReturnVertex = ReturnVertex

    @property
    def ReturnCoord(self):
        return self._ReturnCoord

    @ReturnCoord.setter
    def ReturnCoord(self, ReturnCoord):
        self._ReturnCoord = ReturnCoord

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnVertex = params.get("ReturnVertex")
        self._ReturnCoord = params.get("ReturnCoord")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMedicalInvoiceOCRResponse(AbstractModel):
    """RecognizeMedicalInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MedicalInvoiceInfos: 识别出的字段信息
        :type MedicalInvoiceInfos: list of MedicalInvoiceInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MedicalInvoiceInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def MedicalInvoiceInfos(self):
        return self._MedicalInvoiceInfos

    @MedicalInvoiceInfos.setter
    def MedicalInvoiceInfos(self, MedicalInvoiceInfos):
        self._MedicalInvoiceInfos = MedicalInvoiceInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MedicalInvoiceInfos") is not None:
            self._MedicalInvoiceInfos = []
            for item in params.get("MedicalInvoiceInfos"):
                obj = MedicalInvoiceInfo()
                obj._deserialize(item)
                self._MedicalInvoiceInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class RecognizeOnlineTaxiItineraryOCRRequest(AbstractModel):
    """RecognizeOnlineTaxiItineraryOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeOnlineTaxiItineraryOCRResponse(AbstractModel):
    """RecognizeOnlineTaxiItineraryOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OnlineTaxiItineraryInfos: 网约车行程单识别结果，具体内容请点击左侧链接。
        :type OnlineTaxiItineraryInfos: list of OnlineTaxiItineraryInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OnlineTaxiItineraryInfos = None
        self._RequestId = None

    @property
    def OnlineTaxiItineraryInfos(self):
        return self._OnlineTaxiItineraryInfos

    @OnlineTaxiItineraryInfos.setter
    def OnlineTaxiItineraryInfos(self, OnlineTaxiItineraryInfos):
        self._OnlineTaxiItineraryInfos = OnlineTaxiItineraryInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OnlineTaxiItineraryInfos") is not None:
            self._OnlineTaxiItineraryInfos = []
            for item in params.get("OnlineTaxiItineraryInfos"):
                obj = OnlineTaxiItineraryInfo()
                obj._deserialize(item)
                self._OnlineTaxiItineraryInfos.append(obj)
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesDrivingLicenseOCRRequest(AbstractModel):
    """RecognizePhilippinesDrivingLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesDrivingLicenseOCRResponse(AbstractModel):
    """RecognizePhilippinesDrivingLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: 人像照片Base64后的结果
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Name: 姓名
        :type Name: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LastName: 姓氏
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FirstName: 首姓名
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _MiddleName: 中间姓名
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Nationality: 国籍
        :type Nationality: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Sex: 性别
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: 地址
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNo: 证号
        :type LicenseNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _ExpiresDate: 有效期
        :type ExpiresDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _AgencyCode: 机构代码
        :type AgencyCode: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: 出生日期
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._Name = None
        self._LastName = None
        self._FirstName = None
        self._MiddleName = None
        self._Nationality = None
        self._Sex = None
        self._Address = None
        self._LicenseNo = None
        self._ExpiresDate = None
        self._AgencyCode = None
        self._Birthday = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def MiddleName(self):
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def LicenseNo(self):
        return self._LicenseNo

    @LicenseNo.setter
    def LicenseNo(self, LicenseNo):
        self._LicenseNo = LicenseNo

    @property
    def ExpiresDate(self):
        return self._ExpiresDate

    @ExpiresDate.setter
    def ExpiresDate(self, ExpiresDate):
        self._ExpiresDate = ExpiresDate

    @property
    def AgencyCode(self):
        return self._AgencyCode

    @AgencyCode.setter
    def AgencyCode(self, AgencyCode):
        self._AgencyCode = AgencyCode

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("Name") is not None:
            self._Name = TextDetectionResult()
            self._Name._deserialize(params.get("Name"))
        if params.get("LastName") is not None:
            self._LastName = TextDetectionResult()
            self._LastName._deserialize(params.get("LastName"))
        if params.get("FirstName") is not None:
            self._FirstName = TextDetectionResult()
            self._FirstName._deserialize(params.get("FirstName"))
        if params.get("MiddleName") is not None:
            self._MiddleName = TextDetectionResult()
            self._MiddleName._deserialize(params.get("MiddleName"))
        if params.get("Nationality") is not None:
            self._Nationality = TextDetectionResult()
            self._Nationality._deserialize(params.get("Nationality"))
        if params.get("Sex") is not None:
            self._Sex = TextDetectionResult()
            self._Sex._deserialize(params.get("Sex"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("LicenseNo") is not None:
            self._LicenseNo = TextDetectionResult()
            self._LicenseNo._deserialize(params.get("LicenseNo"))
        if params.get("ExpiresDate") is not None:
            self._ExpiresDate = TextDetectionResult()
            self._ExpiresDate._deserialize(params.get("ExpiresDate"))
        if params.get("AgencyCode") is not None:
            self._AgencyCode = TextDetectionResult()
            self._AgencyCode._deserialize(params.get("AgencyCode"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesSssIDOCRRequest(AbstractModel):
    """RecognizePhilippinesSssIDOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesSssIDOCRResponse(AbstractModel):
    """RecognizePhilippinesSssIDOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: 人像照片Base64后的结果
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNumber: 编号
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FullName: 姓名
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: 生日
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._LicenseNumber = None
        self._FullName = None
        self._Birthday = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("LicenseNumber") is not None:
            self._LicenseNumber = TextDetectionResult()
            self._LicenseNumber._deserialize(params.get("LicenseNumber"))
        if params.get("FullName") is not None:
            self._FullName = TextDetectionResult()
            self._FullName._deserialize(params.get("FullName"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesTinIDOCRRequest(AbstractModel):
    """RecognizePhilippinesTinIDOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesTinIDOCRResponse(AbstractModel):
    """RecognizePhilippinesTinIDOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: 人像照片Base64后的结果
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LicenseNumber: 编码
        :type LicenseNumber: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FullName: 姓名
        :type FullName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: 地址
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: 生日
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _IssueDate: 发证日期
        :type IssueDate: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._LicenseNumber = None
        self._FullName = None
        self._Address = None
        self._Birthday = None
        self._IssueDate = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("LicenseNumber") is not None:
            self._LicenseNumber = TextDetectionResult()
            self._LicenseNumber._deserialize(params.get("LicenseNumber"))
        if params.get("FullName") is not None:
            self._FullName = TextDetectionResult()
            self._FullName._deserialize(params.get("FullName"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        if params.get("IssueDate") is not None:
            self._IssueDate = TextDetectionResult()
            self._IssueDate._deserialize(params.get("IssueDate"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesUMIDOCRRequest(AbstractModel):
    """RecognizePhilippinesUMIDOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。 支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。 支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。 图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。 支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。 支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。 图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。 非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ReturnHeadImage = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesUMIDOCRResponse(AbstractModel):
    """RecognizePhilippinesUMIDOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Surname: 姓
        :type Surname: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _MiddleName: 中间名
        :type MiddleName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _GivenName: 名
        :type GivenName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: 地址
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: 生日
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _CRN: crn码
        :type CRN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Sex: 性别
        :type Sex: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _HeadPortrait: 人像照片Base64后的结果
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Surname = None
        self._MiddleName = None
        self._GivenName = None
        self._Address = None
        self._Birthday = None
        self._CRN = None
        self._Sex = None
        self._HeadPortrait = None
        self._RequestId = None

    @property
    def Surname(self):
        return self._Surname

    @Surname.setter
    def Surname(self, Surname):
        self._Surname = Surname

    @property
    def MiddleName(self):
        return self._MiddleName

    @MiddleName.setter
    def MiddleName(self, MiddleName):
        self._MiddleName = MiddleName

    @property
    def GivenName(self):
        return self._GivenName

    @GivenName.setter
    def GivenName(self, GivenName):
        self._GivenName = GivenName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def CRN(self):
        return self._CRN

    @CRN.setter
    def CRN(self, CRN):
        self._CRN = CRN

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Surname") is not None:
            self._Surname = TextDetectionResult()
            self._Surname._deserialize(params.get("Surname"))
        if params.get("MiddleName") is not None:
            self._MiddleName = TextDetectionResult()
            self._MiddleName._deserialize(params.get("MiddleName"))
        if params.get("GivenName") is not None:
            self._GivenName = TextDetectionResult()
            self._GivenName._deserialize(params.get("GivenName"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        if params.get("CRN") is not None:
            self._CRN = TextDetectionResult()
            self._CRN._deserialize(params.get("CRN"))
        if params.get("Sex") is not None:
            self._Sex = TextDetectionResult()
            self._Sex._deserialize(params.get("Sex"))
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        self._RequestId = params.get("RequestId")


class RecognizePhilippinesVoteIDOCRRequest(AbstractModel):
    """RecognizePhilippinesVoteIDOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnHeadImage: 是否返回人像照片。
        :type ReturnHeadImage: bool
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ReturnHeadImage = None
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ReturnHeadImage(self):
        return self._ReturnHeadImage

    @ReturnHeadImage.setter
    def ReturnHeadImage(self, ReturnHeadImage):
        self._ReturnHeadImage = ReturnHeadImage

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ReturnHeadImage = params.get("ReturnHeadImage")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizePhilippinesVoteIDOCRResponse(AbstractModel):
    """RecognizePhilippinesVoteIDOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HeadPortrait: 人像照片Base64后的结果
        :type HeadPortrait: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _VIN: 菲律宾VoteID的VIN
        :type VIN: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _FirstName: 姓名
        :type FirstName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _LastName: 姓氏
        :type LastName: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Birthday: 出生日期
        :type Birthday: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _CivilStatus: 婚姻状况
        :type CivilStatus: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Citizenship: 国籍
        :type Citizenship: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _Address: 地址
        :type Address: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _PrecinctNo: 地区
        :type PrecinctNo: :class:`tencentcloud.ocr.v20181119.models.TextDetectionResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HeadPortrait = None
        self._VIN = None
        self._FirstName = None
        self._LastName = None
        self._Birthday = None
        self._CivilStatus = None
        self._Citizenship = None
        self._Address = None
        self._PrecinctNo = None
        self._RequestId = None

    @property
    def HeadPortrait(self):
        return self._HeadPortrait

    @HeadPortrait.setter
    def HeadPortrait(self, HeadPortrait):
        self._HeadPortrait = HeadPortrait

    @property
    def VIN(self):
        return self._VIN

    @VIN.setter
    def VIN(self, VIN):
        self._VIN = VIN

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def CivilStatus(self):
        return self._CivilStatus

    @CivilStatus.setter
    def CivilStatus(self, CivilStatus):
        self._CivilStatus = CivilStatus

    @property
    def Citizenship(self):
        return self._Citizenship

    @Citizenship.setter
    def Citizenship(self, Citizenship):
        self._Citizenship = Citizenship

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def PrecinctNo(self):
        return self._PrecinctNo

    @PrecinctNo.setter
    def PrecinctNo(self, PrecinctNo):
        self._PrecinctNo = PrecinctNo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HeadPortrait") is not None:
            self._HeadPortrait = TextDetectionResult()
            self._HeadPortrait._deserialize(params.get("HeadPortrait"))
        if params.get("VIN") is not None:
            self._VIN = TextDetectionResult()
            self._VIN._deserialize(params.get("VIN"))
        if params.get("FirstName") is not None:
            self._FirstName = TextDetectionResult()
            self._FirstName._deserialize(params.get("FirstName"))
        if params.get("LastName") is not None:
            self._LastName = TextDetectionResult()
            self._LastName._deserialize(params.get("LastName"))
        if params.get("Birthday") is not None:
            self._Birthday = TextDetectionResult()
            self._Birthday._deserialize(params.get("Birthday"))
        if params.get("CivilStatus") is not None:
            self._CivilStatus = TextDetectionResult()
            self._CivilStatus._deserialize(params.get("CivilStatus"))
        if params.get("Citizenship") is not None:
            self._Citizenship = TextDetectionResult()
            self._Citizenship._deserialize(params.get("Citizenship"))
        if params.get("Address") is not None:
            self._Address = TextDetectionResult()
            self._Address._deserialize(params.get("Address"))
        if params.get("PrecinctNo") is not None:
            self._PrecinctNo = TextDetectionResult()
            self._PrecinctNo._deserialize(params.get("PrecinctNo"))
        self._RequestId = params.get("RequestId")


class RecognizeTableAccurateOCRRequest(AbstractModel):
    """RecognizeTableAccurateOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片/PDF的 Base64 值。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片支持的像素范围：需介于20-10000px之间。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片/PDF的 Url 地址。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片支持的像素范围：需介于20-10000px之间。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定
性可能受一定影响。
        :type ImageUrl: str
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTableAccurateOCRResponse(AbstractModel):
    """RecognizeTableAccurateOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableDetections: 检测到的文本信息，具体内容请点击左侧链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type TableDetections: list of TableInfo
        :param _Data: Base64 编码后的 Excel 数据。
        :type Data: str
        :param _PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :type PdfPageSize: int
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，统一以逆时针方向旋转，逆时针为负，角度范围为-360°至0°。
注意：此字段可能返回 null，表示取不到有效值。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableDetections = None
        self._Data = None
        self._PdfPageSize = None
        self._Angle = None
        self._RequestId = None

    @property
    def TableDetections(self):
        return self._TableDetections

    @TableDetections.setter
    def TableDetections(self, TableDetections):
        self._TableDetections = TableDetections

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def PdfPageSize(self):
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TableDetections") is not None:
            self._TableDetections = []
            for item in params.get("TableDetections"):
                obj = TableInfo()
                obj._deserialize(item)
                self._TableDetections.append(obj)
        self._Data = params.get("Data")
        self._PdfPageSize = params.get("PdfPageSize")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class RecognizeTableOCRRequest(AbstractModel):
    """RecognizeTableOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片/PDF的 Base64 值。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片/PDF的 Url 地址。
要求图片/PDF经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param _TableLanguage: 语言，zh：中英文（默认）jap：日文
        :type TableLanguage: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._TableLanguage = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def TableLanguage(self):
        return self._TableLanguage

    @TableLanguage.setter
    def TableLanguage(self, TableLanguage):
        self._TableLanguage = TableLanguage


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._TableLanguage = params.get("TableLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTableOCRResponse(AbstractModel):
    """RecognizeTableOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TableDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TableDetections: list of TableDetectInfo
        :param _Data: Base64 编码后的 Excel 数据。
        :type Data: str
        :param _PdfPageSize: 图片为PDF时，返回PDF的总页数，默认为0
        :type PdfPageSize: int
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，统一以逆时针方向旋转，逆时针为负，角度范围为-360°至0°。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TableDetections = None
        self._Data = None
        self._PdfPageSize = None
        self._Angle = None
        self._RequestId = None

    @property
    def TableDetections(self):
        return self._TableDetections

    @TableDetections.setter
    def TableDetections(self, TableDetections):
        self._TableDetections = TableDetections

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def PdfPageSize(self):
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TableDetections") is not None:
            self._TableDetections = []
            for item in params.get("TableDetections"):
                obj = TableDetectInfo()
                obj._deserialize(item)
                self._TableDetections.append(obj)
        self._Data = params.get("Data")
        self._PdfPageSize = params.get("PdfPageSize")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class RecognizeThaiIDCardOCRRequest(AbstractModel):
    """RecognizeThaiIDCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param _CropPortrait: 图片开关。默认为false，不返回泰国身份证头像照片的base64编码。
设置为true时，返回旋转矫正后的泰国身份证头像照片的base64编码
        :type CropPortrait: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CropPortrait = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CropPortrait(self):
        return self._CropPortrait

    @CropPortrait.setter
    def CropPortrait(self, CropPortrait):
        self._CropPortrait = CropPortrait


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CropPortrait = params.get("CropPortrait")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeThaiIDCardOCRResponse(AbstractModel):
    """RecognizeThaiIDCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 身份证号码
        :type ID: str
        :param _ThaiName: 泰文姓名
        :type ThaiName: str
        :param _EnFirstName: 英文姓名
        :type EnFirstName: str
        :param _Address: 地址
        :type Address: str
        :param _Birthday: 出生日期
        :type Birthday: str
        :param _IssueDate: 签发日期
        :type IssueDate: str
        :param _ExpirationDate: 到期日期
        :type ExpirationDate: str
        :param _EnLastName: 英文姓名
        :type EnLastName: str
        :param _PortraitImage: 证件人像照片抠取
        :type PortraitImage: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ID = None
        self._ThaiName = None
        self._EnFirstName = None
        self._Address = None
        self._Birthday = None
        self._IssueDate = None
        self._ExpirationDate = None
        self._EnLastName = None
        self._PortraitImage = None
        self._RequestId = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ThaiName(self):
        return self._ThaiName

    @ThaiName.setter
    def ThaiName(self, ThaiName):
        self._ThaiName = ThaiName

    @property
    def EnFirstName(self):
        return self._EnFirstName

    @EnFirstName.setter
    def EnFirstName(self, EnFirstName):
        self._EnFirstName = EnFirstName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def EnLastName(self):
        return self._EnLastName

    @EnLastName.setter
    def EnLastName(self, EnLastName):
        self._EnLastName = EnLastName

    @property
    def PortraitImage(self):
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ThaiName = params.get("ThaiName")
        self._EnFirstName = params.get("EnFirstName")
        self._Address = params.get("Address")
        self._Birthday = params.get("Birthday")
        self._IssueDate = params.get("IssueDate")
        self._ExpirationDate = params.get("ExpirationDate")
        self._EnLastName = params.get("EnLastName")
        self._PortraitImage = params.get("PortraitImage")
        self._RequestId = params.get("RequestId")


class RecognizeTravelCardOCRRequest(AbstractModel):
    """RecognizeTravelCardOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeTravelCardOCRResponse(AbstractModel):
    """RecognizeTravelCardOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Time: 行程卡更新时间，格式为：XXXX.XX.XX XX:XX:XX
        :type Time: str
        :param _Color: 行程卡颜色：绿色、黄色、红色
        :type Color: str
        :param _ReachedCity: 7天内到达或途经的城市（自2022年7月8日起，通信行程卡查询结果的覆盖时间范围由“14天”调整为“7天”）
        :type ReachedCity: list of str
        :param _RiskArea: 7天内到达或途径存在中高风险地区的城市（自2022年6月29日起，通信行程卡取消“星号”标记，改字段将返回空值）
        :type RiskArea: list of str
        :param _Telephone: 电话号码
        :type Telephone: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Time = None
        self._Color = None
        self._ReachedCity = None
        self._RiskArea = None
        self._Telephone = None
        self._RequestId = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def ReachedCity(self):
        return self._ReachedCity

    @ReachedCity.setter
    def ReachedCity(self, ReachedCity):
        self._ReachedCity = ReachedCity

    @property
    def RiskArea(self):
        return self._RiskArea

    @RiskArea.setter
    def RiskArea(self, RiskArea):
        self._RiskArea = RiskArea

    @property
    def Telephone(self):
        return self._Telephone

    @Telephone.setter
    def Telephone(self, Telephone):
        self._Telephone = Telephone

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Color = params.get("Color")
        self._ReachedCity = params.get("ReachedCity")
        self._RiskArea = params.get("RiskArea")
        self._Telephone = params.get("Telephone")
        self._RequestId = params.get("RequestId")


class Rect(AbstractModel):
    """矩形坐标

    """

    def __init__(self):
        r"""
        :param _X: 左上角x
        :type X: int
        :param _Y: 左上角y
        :type Y: int
        :param _Width: 宽度
        :type Width: int
        :param _Height: 高度
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
        


class ResidenceBookletOCRRequest(AbstractModel):
    """ResidenceBookletOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResidenceBookletOCRResponse(AbstractModel):
    """ResidenceBookletOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HouseholdNumber: 户号
        :type HouseholdNumber: str
        :param _Name: 姓名
        :type Name: str
        :param _Sex: 性别
        :type Sex: str
        :param _BirthPlace: 出生地
        :type BirthPlace: str
        :param _Nation: 民族
        :type Nation: str
        :param _NativePlace: 籍贯
        :type NativePlace: str
        :param _BirthDate: 出生日期
        :type BirthDate: str
        :param _IdCardNumber: 公民身份证件编号
        :type IdCardNumber: str
        :param _EducationDegree: 文化程度
        :type EducationDegree: str
        :param _ServicePlace: 服务处所
        :type ServicePlace: str
        :param _Household: 户别
        :type Household: str
        :param _Address: 住址
        :type Address: str
        :param _Signature: 承办人签章文字
        :type Signature: str
        :param _IssueDate: 签发日期
        :type IssueDate: str
        :param _HomePageNumber: 户主页编号
        :type HomePageNumber: str
        :param _HouseholderName: 户主姓名
        :type HouseholderName: str
        :param _Relationship: 户主或与户主关系
        :type Relationship: str
        :param _OtherAddresses: 本市（县）其他住址
        :type OtherAddresses: str
        :param _ReligiousBelief: 宗教信仰
        :type ReligiousBelief: str
        :param _Height: 身高
        :type Height: str
        :param _BloodType: 血型
        :type BloodType: str
        :param _MaritalStatus: 婚姻状况
        :type MaritalStatus: str
        :param _VeteranStatus: 兵役状况
        :type VeteranStatus: str
        :param _Profession: 职业
        :type Profession: str
        :param _MoveToCityInformation: 何时由何地迁来本市(县)
        :type MoveToCityInformation: str
        :param _MoveToSiteInformation: 何时由何地迁来本址
        :type MoveToSiteInformation: str
        :param _RegistrationDate: 登记日期
        :type RegistrationDate: str
        :param _FormerName: 曾用名
        :type FormerName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HouseholdNumber = None
        self._Name = None
        self._Sex = None
        self._BirthPlace = None
        self._Nation = None
        self._NativePlace = None
        self._BirthDate = None
        self._IdCardNumber = None
        self._EducationDegree = None
        self._ServicePlace = None
        self._Household = None
        self._Address = None
        self._Signature = None
        self._IssueDate = None
        self._HomePageNumber = None
        self._HouseholderName = None
        self._Relationship = None
        self._OtherAddresses = None
        self._ReligiousBelief = None
        self._Height = None
        self._BloodType = None
        self._MaritalStatus = None
        self._VeteranStatus = None
        self._Profession = None
        self._MoveToCityInformation = None
        self._MoveToSiteInformation = None
        self._RegistrationDate = None
        self._FormerName = None
        self._RequestId = None

    @property
    def HouseholdNumber(self):
        return self._HouseholdNumber

    @HouseholdNumber.setter
    def HouseholdNumber(self, HouseholdNumber):
        self._HouseholdNumber = HouseholdNumber

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def NativePlace(self):
        return self._NativePlace

    @NativePlace.setter
    def NativePlace(self, NativePlace):
        self._NativePlace = NativePlace

    @property
    def BirthDate(self):
        return self._BirthDate

    @BirthDate.setter
    def BirthDate(self, BirthDate):
        self._BirthDate = BirthDate

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def EducationDegree(self):
        return self._EducationDegree

    @EducationDegree.setter
    def EducationDegree(self, EducationDegree):
        self._EducationDegree = EducationDegree

    @property
    def ServicePlace(self):
        return self._ServicePlace

    @ServicePlace.setter
    def ServicePlace(self, ServicePlace):
        self._ServicePlace = ServicePlace

    @property
    def Household(self):
        return self._Household

    @Household.setter
    def Household(self, Household):
        self._Household = Household

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def HomePageNumber(self):
        return self._HomePageNumber

    @HomePageNumber.setter
    def HomePageNumber(self, HomePageNumber):
        self._HomePageNumber = HomePageNumber

    @property
    def HouseholderName(self):
        return self._HouseholderName

    @HouseholderName.setter
    def HouseholderName(self, HouseholderName):
        self._HouseholderName = HouseholderName

    @property
    def Relationship(self):
        return self._Relationship

    @Relationship.setter
    def Relationship(self, Relationship):
        self._Relationship = Relationship

    @property
    def OtherAddresses(self):
        return self._OtherAddresses

    @OtherAddresses.setter
    def OtherAddresses(self, OtherAddresses):
        self._OtherAddresses = OtherAddresses

    @property
    def ReligiousBelief(self):
        return self._ReligiousBelief

    @ReligiousBelief.setter
    def ReligiousBelief(self, ReligiousBelief):
        self._ReligiousBelief = ReligiousBelief

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def BloodType(self):
        return self._BloodType

    @BloodType.setter
    def BloodType(self, BloodType):
        self._BloodType = BloodType

    @property
    def MaritalStatus(self):
        return self._MaritalStatus

    @MaritalStatus.setter
    def MaritalStatus(self, MaritalStatus):
        self._MaritalStatus = MaritalStatus

    @property
    def VeteranStatus(self):
        return self._VeteranStatus

    @VeteranStatus.setter
    def VeteranStatus(self, VeteranStatus):
        self._VeteranStatus = VeteranStatus

    @property
    def Profession(self):
        return self._Profession

    @Profession.setter
    def Profession(self, Profession):
        self._Profession = Profession

    @property
    def MoveToCityInformation(self):
        return self._MoveToCityInformation

    @MoveToCityInformation.setter
    def MoveToCityInformation(self, MoveToCityInformation):
        self._MoveToCityInformation = MoveToCityInformation

    @property
    def MoveToSiteInformation(self):
        return self._MoveToSiteInformation

    @MoveToSiteInformation.setter
    def MoveToSiteInformation(self, MoveToSiteInformation):
        self._MoveToSiteInformation = MoveToSiteInformation

    @property
    def RegistrationDate(self):
        return self._RegistrationDate

    @RegistrationDate.setter
    def RegistrationDate(self, RegistrationDate):
        self._RegistrationDate = RegistrationDate

    @property
    def FormerName(self):
        return self._FormerName

    @FormerName.setter
    def FormerName(self, FormerName):
        self._FormerName = FormerName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HouseholdNumber = params.get("HouseholdNumber")
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._BirthPlace = params.get("BirthPlace")
        self._Nation = params.get("Nation")
        self._NativePlace = params.get("NativePlace")
        self._BirthDate = params.get("BirthDate")
        self._IdCardNumber = params.get("IdCardNumber")
        self._EducationDegree = params.get("EducationDegree")
        self._ServicePlace = params.get("ServicePlace")
        self._Household = params.get("Household")
        self._Address = params.get("Address")
        self._Signature = params.get("Signature")
        self._IssueDate = params.get("IssueDate")
        self._HomePageNumber = params.get("HomePageNumber")
        self._HouseholderName = params.get("HouseholderName")
        self._Relationship = params.get("Relationship")
        self._OtherAddresses = params.get("OtherAddresses")
        self._ReligiousBelief = params.get("ReligiousBelief")
        self._Height = params.get("Height")
        self._BloodType = params.get("BloodType")
        self._MaritalStatus = params.get("MaritalStatus")
        self._VeteranStatus = params.get("VeteranStatus")
        self._Profession = params.get("Profession")
        self._MoveToCityInformation = params.get("MoveToCityInformation")
        self._MoveToSiteInformation = params.get("MoveToSiteInformation")
        self._RegistrationDate = params.get("RegistrationDate")
        self._FormerName = params.get("FormerName")
        self._RequestId = params.get("RequestId")


class RideHailingDriverLicenseOCRRequest(AbstractModel):
    """RideHailingDriverLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RideHailingDriverLicenseOCRResponse(AbstractModel):
    """RideHailingDriverLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _LicenseNumber: 证号，对应网约车驾驶证字段：证号/从业资格证号/驾驶员证号/身份证号
        :type LicenseNumber: str
        :param _StartDate: 有效起始日期
        :type StartDate: str
        :param _EndDate: 有效期截止时间，对应网约车驾驶证字段：有效期至/营运期限止
        :type EndDate: str
        :param _ReleaseDate: 初始发证日期，对应网约车驾驶证字段：初始领证日期/发证日期
        :type ReleaseDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._LicenseNumber = None
        self._StartDate = None
        self._EndDate = None
        self._ReleaseDate = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LicenseNumber(self):
        return self._LicenseNumber

    @LicenseNumber.setter
    def LicenseNumber(self, LicenseNumber):
        self._LicenseNumber = LicenseNumber

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ReleaseDate(self):
        return self._ReleaseDate

    @ReleaseDate.setter
    def ReleaseDate(self, ReleaseDate):
        self._ReleaseDate = ReleaseDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._LicenseNumber = params.get("LicenseNumber")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._ReleaseDate = params.get("ReleaseDate")
        self._RequestId = params.get("RequestId")


class RideHailingTransportLicenseOCRRequest(AbstractModel):
    """RideHailingTransportLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RideHailingTransportLicenseOCRResponse(AbstractModel):
    """RideHailingTransportLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationLicenseNumber: 交运管许可字号。
        :type OperationLicenseNumber: str
        :param _VehicleOwner: 车辆所有人，对应网约车运输证字段：车辆所有人/车主名称/业户名称。
        :type VehicleOwner: str
        :param _VehicleNumber: 车牌号码，对应网约车运输证字段：车牌号码/车辆号牌。
        :type VehicleNumber: str
        :param _StartDate: 有效起始日期。
        :type StartDate: str
        :param _EndDate: 有效期截止时间，对应网约车运输证字段：有效期至/营运期限止。
        :type EndDate: str
        :param _ReleaseDate: 初始发证日期，对应网约车运输证字段：初始领证日期/发证日期。
        :type ReleaseDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OperationLicenseNumber = None
        self._VehicleOwner = None
        self._VehicleNumber = None
        self._StartDate = None
        self._EndDate = None
        self._ReleaseDate = None
        self._RequestId = None

    @property
    def OperationLicenseNumber(self):
        return self._OperationLicenseNumber

    @OperationLicenseNumber.setter
    def OperationLicenseNumber(self, OperationLicenseNumber):
        self._OperationLicenseNumber = OperationLicenseNumber

    @property
    def VehicleOwner(self):
        return self._VehicleOwner

    @VehicleOwner.setter
    def VehicleOwner(self, VehicleOwner):
        self._VehicleOwner = VehicleOwner

    @property
    def VehicleNumber(self):
        return self._VehicleNumber

    @VehicleNumber.setter
    def VehicleNumber(self, VehicleNumber):
        self._VehicleNumber = VehicleNumber

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ReleaseDate(self):
        return self._ReleaseDate

    @ReleaseDate.setter
    def ReleaseDate(self, ReleaseDate):
        self._ReleaseDate = ReleaseDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OperationLicenseNumber = params.get("OperationLicenseNumber")
        self._VehicleOwner = params.get("VehicleOwner")
        self._VehicleNumber = params.get("VehicleNumber")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._ReleaseDate = params.get("ReleaseDate")
        self._RequestId = params.get("RequestId")


class SealInfo(AbstractModel):
    """印章信息

    """

    def __init__(self):
        r"""
        :param _SealBody: 印章主体内容
        :type SealBody: str
        :param _Location: 印章坐标
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _OtherTexts: 印章其它文本内容
        :type OtherTexts: list of str
        :param _SealShape: 印章类型，表示为:
圆形印章：0
椭圆形印章：1
方形印章：2
菱形印章：3
三角形印章：4
        :type SealShape: str
        """
        self._SealBody = None
        self._Location = None
        self._OtherTexts = None
        self._SealShape = None

    @property
    def SealBody(self):
        return self._SealBody

    @SealBody.setter
    def SealBody(self, SealBody):
        self._SealBody = SealBody

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def OtherTexts(self):
        return self._OtherTexts

    @OtherTexts.setter
    def OtherTexts(self, OtherTexts):
        self._OtherTexts = OtherTexts

    @property
    def SealShape(self):
        return self._SealShape

    @SealShape.setter
    def SealShape(self, SealShape):
        self._SealShape = SealShape


    def _deserialize(self, params):
        self._SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self._Location = Rect()
            self._Location._deserialize(params.get("Location"))
        self._OtherTexts = params.get("OtherTexts")
        self._SealShape = params.get("SealShape")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SealOCRRequest(AbstractModel):
    """SealOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SealOCRResponse(AbstractModel):
    """SealOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealBody: 印章内容
        :type SealBody: str
        :param _Location: 印章坐标
        :type Location: :class:`tencentcloud.ocr.v20181119.models.Rect`
        :param _OtherTexts: 其它文本内容
        :type OtherTexts: list of str
        :param _SealInfos: 全部印章信息
        :type SealInfos: list of SealInfo
        :param _SealShape: 印章类型，表示为：
圆形印章：0
椭圆形印章：1
方形印章：2
菱形印章：3
三角形印章：4
        :type SealShape: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealBody = None
        self._Location = None
        self._OtherTexts = None
        self._SealInfos = None
        self._SealShape = None
        self._RequestId = None

    @property
    def SealBody(self):
        return self._SealBody

    @SealBody.setter
    def SealBody(self, SealBody):
        self._SealBody = SealBody

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def OtherTexts(self):
        return self._OtherTexts

    @OtherTexts.setter
    def OtherTexts(self, OtherTexts):
        self._OtherTexts = OtherTexts

    @property
    def SealInfos(self):
        return self._SealInfos

    @SealInfos.setter
    def SealInfos(self, SealInfos):
        self._SealInfos = SealInfos

    @property
    def SealShape(self):
        return self._SealShape

    @SealShape.setter
    def SealShape(self, SealShape):
        self._SealShape = SealShape

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealBody = params.get("SealBody")
        if params.get("Location") is not None:
            self._Location = Rect()
            self._Location._deserialize(params.get("Location"))
        self._OtherTexts = params.get("OtherTexts")
        if params.get("SealInfos") is not None:
            self._SealInfos = []
            for item in params.get("SealInfos"):
                obj = SealInfo()
                obj._deserialize(item)
                self._SealInfos.append(obj)
        self._SealShape = params.get("SealShape")
        self._RequestId = params.get("RequestId")


class ShipInvoiceInfo(AbstractModel):
    """轮船票字段信息

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、发票号码、日期、票价、始发地、目的地、姓名、时间、发票消费类型、省、市、币种。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Value = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipInvoiceOCRRequest(AbstractModel):
    """ShipInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShipInvoiceOCRResponse(AbstractModel):
    """ShipInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ShipInvoiceInfos: 轮船票识别结果，具体内容请点击左侧链接。
        :type ShipInvoiceInfos: list of ShipInvoiceInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ShipInvoiceInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def ShipInvoiceInfos(self):
        return self._ShipInvoiceInfos

    @ShipInvoiceInfos.setter
    def ShipInvoiceInfos(self, ShipInvoiceInfos):
        self._ShipInvoiceInfos = ShipInvoiceInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ShipInvoiceInfos") is not None:
            self._ShipInvoiceInfos = []
            for item in params.get("ShipInvoiceInfos"):
                obj = ShipInvoiceInfo()
                obj._deserialize(item)
                self._ShipInvoiceInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class ShippingInvoice(AbstractModel):
    """轮船票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _UserName: 姓名
        :type UserName: str
        :param _Date: 日期
        :type Date: str
        :param _Time: 时间
        :type Time: str
        :param _StationGetOn: 出发车站
        :type StationGetOn: str
        :param _StationGetOff: 到达车站
        :type StationGetOff: str
        :param _Total: 票价
        :type Total: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _CurrencyCode: 币种
        :type CurrencyCode: str
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._UserName = None
        self._Date = None
        self._Time = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Total = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._CurrencyCode = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def CurrencyCode(self):
        return self._CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, CurrencyCode):
        self._CurrencyCode = CurrencyCode


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._UserName = params.get("UserName")
        self._Date = params.get("Date")
        self._Time = params.get("Time")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._CurrencyCode = params.get("CurrencyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleInvoiceInfo(AbstractModel):
    """混贴票据中单张发票的内容

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        :param _Row: 字段属于第几行，用于相同字段的排版，如发票明细表格项目，普通字段使用默认值为-1，表示无列排版。
        :type Row: int
        """
        self._Name = None
        self._Value = None
        self._Row = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Row(self):
        return self._Row

    @Row.setter
    def Row(self, Row):
        self._Row = Row


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Row = params.get("Row")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleInvoiceItem(AbstractModel):
    """混贴票据中单张发票的内容

    """

    def __init__(self):
        r"""
        :param _VatSpecialInvoice: 增值税专用发票
注意：此字段可能返回 null，表示取不到有效值。
        :type VatSpecialInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatCommonInvoice: 增值税普通发票
注意：此字段可能返回 null，表示取不到有效值。
        :type VatCommonInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicCommonInvoice: 增值税电子普通发票
注意：此字段可能返回 null，表示取不到有效值。
        :type VatElectronicCommonInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicSpecialInvoice: 增值税电子专用发票
注意：此字段可能返回 null，表示取不到有效值。
        :type VatElectronicSpecialInvoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicInvoiceBlockchain: 区块链电子发票
注意：此字段可能返回 null，表示取不到有效值。
        :type VatElectronicInvoiceBlockchain: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicInvoiceToll: 增值税电子普通发票(通行费)
注意：此字段可能返回 null，表示取不到有效值。
        :type VatElectronicInvoiceToll: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        :param _VatElectronicSpecialInvoiceFull: 电子发票(专用发票)
注意：此字段可能返回 null，表示取不到有效值。
        :type VatElectronicSpecialInvoiceFull: :class:`tencentcloud.ocr.v20181119.models.VatElectronicInfo`
        :param _VatElectronicInvoiceFull: 电子发票(普通发票)
注意：此字段可能返回 null，表示取不到有效值。
        :type VatElectronicInvoiceFull: :class:`tencentcloud.ocr.v20181119.models.VatElectronicInfo`
        :param _MachinePrintedInvoice: 通用机打发票
注意：此字段可能返回 null，表示取不到有效值。
        :type MachinePrintedInvoice: :class:`tencentcloud.ocr.v20181119.models.MachinePrintedInvoice`
        :param _BusInvoice: 汽车票
注意：此字段可能返回 null，表示取不到有效值。
        :type BusInvoice: :class:`tencentcloud.ocr.v20181119.models.BusInvoice`
        :param _ShippingInvoice: 轮船票
注意：此字段可能返回 null，表示取不到有效值。
        :type ShippingInvoice: :class:`tencentcloud.ocr.v20181119.models.ShippingInvoice`
        :param _TollInvoice: 过路过桥费发票
注意：此字段可能返回 null，表示取不到有效值。
        :type TollInvoice: :class:`tencentcloud.ocr.v20181119.models.TollInvoice`
        :param _OtherInvoice: 其他发票
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherInvoice: :class:`tencentcloud.ocr.v20181119.models.OtherInvoice`
        :param _MotorVehicleSaleInvoice: 机动车销售统一发票
注意：此字段可能返回 null，表示取不到有效值。
        :type MotorVehicleSaleInvoice: :class:`tencentcloud.ocr.v20181119.models.MotorVehicleSaleInvoice`
        :param _UsedCarPurchaseInvoice: 二手车销售统一发票
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedCarPurchaseInvoice: :class:`tencentcloud.ocr.v20181119.models.UsedCarPurchaseInvoice`
        :param _VatInvoiceRoll: 增值税普通发票(卷票)
注意：此字段可能返回 null，表示取不到有效值。
        :type VatInvoiceRoll: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceRoll`
        :param _TaxiTicket: 出租车发票
注意：此字段可能返回 null，表示取不到有效值。
        :type TaxiTicket: :class:`tencentcloud.ocr.v20181119.models.TaxiTicket`
        :param _QuotaInvoice: 定额发票
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaInvoice: :class:`tencentcloud.ocr.v20181119.models.QuotaInvoice`
        :param _AirTransport: 机票行程单
注意：此字段可能返回 null，表示取不到有效值。
        :type AirTransport: :class:`tencentcloud.ocr.v20181119.models.AirTransport`
        :param _NonTaxIncomeGeneralBill: 非税收入通用票据
注意：此字段可能返回 null，表示取不到有效值。
        :type NonTaxIncomeGeneralBill: :class:`tencentcloud.ocr.v20181119.models.NonTaxIncomeBill`
        :param _NonTaxIncomeElectronicBill: 非税收入一般缴款书(电子)
注意：此字段可能返回 null，表示取不到有效值。
        :type NonTaxIncomeElectronicBill: :class:`tencentcloud.ocr.v20181119.models.NonTaxIncomeBill`
        :param _TrainTicket: 火车票
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainTicket: :class:`tencentcloud.ocr.v20181119.models.TrainTicket`
        :param _MedicalOutpatientInvoice: 医疗门诊收费票据（电子）
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalOutpatientInvoice: :class:`tencentcloud.ocr.v20181119.models.MedicalInvoice`
        :param _MedicalHospitalizedInvoice: 医疗住院收费票据（电子）
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalHospitalizedInvoice: :class:`tencentcloud.ocr.v20181119.models.MedicalInvoice`
        :param _VatSalesList: 增值税销货清单
注意：此字段可能返回 null，表示取不到有效值。
        :type VatSalesList: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceInfo`
        """
        self._VatSpecialInvoice = None
        self._VatCommonInvoice = None
        self._VatElectronicCommonInvoice = None
        self._VatElectronicSpecialInvoice = None
        self._VatElectronicInvoiceBlockchain = None
        self._VatElectronicInvoiceToll = None
        self._VatElectronicSpecialInvoiceFull = None
        self._VatElectronicInvoiceFull = None
        self._MachinePrintedInvoice = None
        self._BusInvoice = None
        self._ShippingInvoice = None
        self._TollInvoice = None
        self._OtherInvoice = None
        self._MotorVehicleSaleInvoice = None
        self._UsedCarPurchaseInvoice = None
        self._VatInvoiceRoll = None
        self._TaxiTicket = None
        self._QuotaInvoice = None
        self._AirTransport = None
        self._NonTaxIncomeGeneralBill = None
        self._NonTaxIncomeElectronicBill = None
        self._TrainTicket = None
        self._MedicalOutpatientInvoice = None
        self._MedicalHospitalizedInvoice = None
        self._VatSalesList = None

    @property
    def VatSpecialInvoice(self):
        return self._VatSpecialInvoice

    @VatSpecialInvoice.setter
    def VatSpecialInvoice(self, VatSpecialInvoice):
        self._VatSpecialInvoice = VatSpecialInvoice

    @property
    def VatCommonInvoice(self):
        return self._VatCommonInvoice

    @VatCommonInvoice.setter
    def VatCommonInvoice(self, VatCommonInvoice):
        self._VatCommonInvoice = VatCommonInvoice

    @property
    def VatElectronicCommonInvoice(self):
        return self._VatElectronicCommonInvoice

    @VatElectronicCommonInvoice.setter
    def VatElectronicCommonInvoice(self, VatElectronicCommonInvoice):
        self._VatElectronicCommonInvoice = VatElectronicCommonInvoice

    @property
    def VatElectronicSpecialInvoice(self):
        return self._VatElectronicSpecialInvoice

    @VatElectronicSpecialInvoice.setter
    def VatElectronicSpecialInvoice(self, VatElectronicSpecialInvoice):
        self._VatElectronicSpecialInvoice = VatElectronicSpecialInvoice

    @property
    def VatElectronicInvoiceBlockchain(self):
        return self._VatElectronicInvoiceBlockchain

    @VatElectronicInvoiceBlockchain.setter
    def VatElectronicInvoiceBlockchain(self, VatElectronicInvoiceBlockchain):
        self._VatElectronicInvoiceBlockchain = VatElectronicInvoiceBlockchain

    @property
    def VatElectronicInvoiceToll(self):
        return self._VatElectronicInvoiceToll

    @VatElectronicInvoiceToll.setter
    def VatElectronicInvoiceToll(self, VatElectronicInvoiceToll):
        self._VatElectronicInvoiceToll = VatElectronicInvoiceToll

    @property
    def VatElectronicSpecialInvoiceFull(self):
        return self._VatElectronicSpecialInvoiceFull

    @VatElectronicSpecialInvoiceFull.setter
    def VatElectronicSpecialInvoiceFull(self, VatElectronicSpecialInvoiceFull):
        self._VatElectronicSpecialInvoiceFull = VatElectronicSpecialInvoiceFull

    @property
    def VatElectronicInvoiceFull(self):
        return self._VatElectronicInvoiceFull

    @VatElectronicInvoiceFull.setter
    def VatElectronicInvoiceFull(self, VatElectronicInvoiceFull):
        self._VatElectronicInvoiceFull = VatElectronicInvoiceFull

    @property
    def MachinePrintedInvoice(self):
        return self._MachinePrintedInvoice

    @MachinePrintedInvoice.setter
    def MachinePrintedInvoice(self, MachinePrintedInvoice):
        self._MachinePrintedInvoice = MachinePrintedInvoice

    @property
    def BusInvoice(self):
        return self._BusInvoice

    @BusInvoice.setter
    def BusInvoice(self, BusInvoice):
        self._BusInvoice = BusInvoice

    @property
    def ShippingInvoice(self):
        return self._ShippingInvoice

    @ShippingInvoice.setter
    def ShippingInvoice(self, ShippingInvoice):
        self._ShippingInvoice = ShippingInvoice

    @property
    def TollInvoice(self):
        return self._TollInvoice

    @TollInvoice.setter
    def TollInvoice(self, TollInvoice):
        self._TollInvoice = TollInvoice

    @property
    def OtherInvoice(self):
        return self._OtherInvoice

    @OtherInvoice.setter
    def OtherInvoice(self, OtherInvoice):
        self._OtherInvoice = OtherInvoice

    @property
    def MotorVehicleSaleInvoice(self):
        return self._MotorVehicleSaleInvoice

    @MotorVehicleSaleInvoice.setter
    def MotorVehicleSaleInvoice(self, MotorVehicleSaleInvoice):
        self._MotorVehicleSaleInvoice = MotorVehicleSaleInvoice

    @property
    def UsedCarPurchaseInvoice(self):
        return self._UsedCarPurchaseInvoice

    @UsedCarPurchaseInvoice.setter
    def UsedCarPurchaseInvoice(self, UsedCarPurchaseInvoice):
        self._UsedCarPurchaseInvoice = UsedCarPurchaseInvoice

    @property
    def VatInvoiceRoll(self):
        return self._VatInvoiceRoll

    @VatInvoiceRoll.setter
    def VatInvoiceRoll(self, VatInvoiceRoll):
        self._VatInvoiceRoll = VatInvoiceRoll

    @property
    def TaxiTicket(self):
        return self._TaxiTicket

    @TaxiTicket.setter
    def TaxiTicket(self, TaxiTicket):
        self._TaxiTicket = TaxiTicket

    @property
    def QuotaInvoice(self):
        return self._QuotaInvoice

    @QuotaInvoice.setter
    def QuotaInvoice(self, QuotaInvoice):
        self._QuotaInvoice = QuotaInvoice

    @property
    def AirTransport(self):
        return self._AirTransport

    @AirTransport.setter
    def AirTransport(self, AirTransport):
        self._AirTransport = AirTransport

    @property
    def NonTaxIncomeGeneralBill(self):
        return self._NonTaxIncomeGeneralBill

    @NonTaxIncomeGeneralBill.setter
    def NonTaxIncomeGeneralBill(self, NonTaxIncomeGeneralBill):
        self._NonTaxIncomeGeneralBill = NonTaxIncomeGeneralBill

    @property
    def NonTaxIncomeElectronicBill(self):
        return self._NonTaxIncomeElectronicBill

    @NonTaxIncomeElectronicBill.setter
    def NonTaxIncomeElectronicBill(self, NonTaxIncomeElectronicBill):
        self._NonTaxIncomeElectronicBill = NonTaxIncomeElectronicBill

    @property
    def TrainTicket(self):
        return self._TrainTicket

    @TrainTicket.setter
    def TrainTicket(self, TrainTicket):
        self._TrainTicket = TrainTicket

    @property
    def MedicalOutpatientInvoice(self):
        return self._MedicalOutpatientInvoice

    @MedicalOutpatientInvoice.setter
    def MedicalOutpatientInvoice(self, MedicalOutpatientInvoice):
        self._MedicalOutpatientInvoice = MedicalOutpatientInvoice

    @property
    def MedicalHospitalizedInvoice(self):
        return self._MedicalHospitalizedInvoice

    @MedicalHospitalizedInvoice.setter
    def MedicalHospitalizedInvoice(self, MedicalHospitalizedInvoice):
        self._MedicalHospitalizedInvoice = MedicalHospitalizedInvoice

    @property
    def VatSalesList(self):
        return self._VatSalesList

    @VatSalesList.setter
    def VatSalesList(self, VatSalesList):
        self._VatSalesList = VatSalesList


    def _deserialize(self, params):
        if params.get("VatSpecialInvoice") is not None:
            self._VatSpecialInvoice = VatInvoiceInfo()
            self._VatSpecialInvoice._deserialize(params.get("VatSpecialInvoice"))
        if params.get("VatCommonInvoice") is not None:
            self._VatCommonInvoice = VatInvoiceInfo()
            self._VatCommonInvoice._deserialize(params.get("VatCommonInvoice"))
        if params.get("VatElectronicCommonInvoice") is not None:
            self._VatElectronicCommonInvoice = VatInvoiceInfo()
            self._VatElectronicCommonInvoice._deserialize(params.get("VatElectronicCommonInvoice"))
        if params.get("VatElectronicSpecialInvoice") is not None:
            self._VatElectronicSpecialInvoice = VatInvoiceInfo()
            self._VatElectronicSpecialInvoice._deserialize(params.get("VatElectronicSpecialInvoice"))
        if params.get("VatElectronicInvoiceBlockchain") is not None:
            self._VatElectronicInvoiceBlockchain = VatInvoiceInfo()
            self._VatElectronicInvoiceBlockchain._deserialize(params.get("VatElectronicInvoiceBlockchain"))
        if params.get("VatElectronicInvoiceToll") is not None:
            self._VatElectronicInvoiceToll = VatInvoiceInfo()
            self._VatElectronicInvoiceToll._deserialize(params.get("VatElectronicInvoiceToll"))
        if params.get("VatElectronicSpecialInvoiceFull") is not None:
            self._VatElectronicSpecialInvoiceFull = VatElectronicInfo()
            self._VatElectronicSpecialInvoiceFull._deserialize(params.get("VatElectronicSpecialInvoiceFull"))
        if params.get("VatElectronicInvoiceFull") is not None:
            self._VatElectronicInvoiceFull = VatElectronicInfo()
            self._VatElectronicInvoiceFull._deserialize(params.get("VatElectronicInvoiceFull"))
        if params.get("MachinePrintedInvoice") is not None:
            self._MachinePrintedInvoice = MachinePrintedInvoice()
            self._MachinePrintedInvoice._deserialize(params.get("MachinePrintedInvoice"))
        if params.get("BusInvoice") is not None:
            self._BusInvoice = BusInvoice()
            self._BusInvoice._deserialize(params.get("BusInvoice"))
        if params.get("ShippingInvoice") is not None:
            self._ShippingInvoice = ShippingInvoice()
            self._ShippingInvoice._deserialize(params.get("ShippingInvoice"))
        if params.get("TollInvoice") is not None:
            self._TollInvoice = TollInvoice()
            self._TollInvoice._deserialize(params.get("TollInvoice"))
        if params.get("OtherInvoice") is not None:
            self._OtherInvoice = OtherInvoice()
            self._OtherInvoice._deserialize(params.get("OtherInvoice"))
        if params.get("MotorVehicleSaleInvoice") is not None:
            self._MotorVehicleSaleInvoice = MotorVehicleSaleInvoice()
            self._MotorVehicleSaleInvoice._deserialize(params.get("MotorVehicleSaleInvoice"))
        if params.get("UsedCarPurchaseInvoice") is not None:
            self._UsedCarPurchaseInvoice = UsedCarPurchaseInvoice()
            self._UsedCarPurchaseInvoice._deserialize(params.get("UsedCarPurchaseInvoice"))
        if params.get("VatInvoiceRoll") is not None:
            self._VatInvoiceRoll = VatInvoiceRoll()
            self._VatInvoiceRoll._deserialize(params.get("VatInvoiceRoll"))
        if params.get("TaxiTicket") is not None:
            self._TaxiTicket = TaxiTicket()
            self._TaxiTicket._deserialize(params.get("TaxiTicket"))
        if params.get("QuotaInvoice") is not None:
            self._QuotaInvoice = QuotaInvoice()
            self._QuotaInvoice._deserialize(params.get("QuotaInvoice"))
        if params.get("AirTransport") is not None:
            self._AirTransport = AirTransport()
            self._AirTransport._deserialize(params.get("AirTransport"))
        if params.get("NonTaxIncomeGeneralBill") is not None:
            self._NonTaxIncomeGeneralBill = NonTaxIncomeBill()
            self._NonTaxIncomeGeneralBill._deserialize(params.get("NonTaxIncomeGeneralBill"))
        if params.get("NonTaxIncomeElectronicBill") is not None:
            self._NonTaxIncomeElectronicBill = NonTaxIncomeBill()
            self._NonTaxIncomeElectronicBill._deserialize(params.get("NonTaxIncomeElectronicBill"))
        if params.get("TrainTicket") is not None:
            self._TrainTicket = TrainTicket()
            self._TrainTicket._deserialize(params.get("TrainTicket"))
        if params.get("MedicalOutpatientInvoice") is not None:
            self._MedicalOutpatientInvoice = MedicalInvoice()
            self._MedicalOutpatientInvoice._deserialize(params.get("MedicalOutpatientInvoice"))
        if params.get("MedicalHospitalizedInvoice") is not None:
            self._MedicalHospitalizedInvoice = MedicalInvoice()
            self._MedicalHospitalizedInvoice._deserialize(params.get("MedicalHospitalizedInvoice"))
        if params.get("VatSalesList") is not None:
            self._VatSalesList = VatInvoiceInfo()
            self._VatSalesList._deserialize(params.get("VatSalesList"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartFormFileUrl(AbstractModel):
    """智慧表单上传文件信息

    """

    def __init__(self):
        r"""
        :param _FileUrl: 文件url地址
        :type FileUrl: str
        :param _FileOrderNumber: 文件的顺序，顺序从1开始
        :type FileOrderNumber: int
        """
        self._FileUrl = None
        self._FileOrderNumber = None

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileOrderNumber(self):
        return self._FileOrderNumber

    @FileOrderNumber.setter
    def FileOrderNumber(self, FileOrderNumber):
        self._FileOrderNumber = FileOrderNumber


    def _deserialize(self, params):
        self._FileUrl = params.get("FileUrl")
        self._FileOrderNumber = params.get("FileOrderNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRRequest(AbstractModel):
    """SmartStructuralOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ItemNames: 自定义结构化功能需返回的字段名称，例：
若客户只想返回姓名、性别两个字段的识别结果，则输入
ItemNames=["姓名","性别"]
        :type ItemNames: list of str
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param _ReturnFullText: 是否开启全文字段识别，默认值为false，开启后可返回全文字段识别结果。
        :type ReturnFullText: bool
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._ItemNames = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._ReturnFullText = None

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ItemNames(self):
        return self._ItemNames

    @ItemNames.setter
    def ItemNames(self, ItemNames):
        self._ItemNames = ItemNames

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def ReturnFullText(self):
        return self._ReturnFullText

    @ReturnFullText.setter
    def ReturnFullText(self, ReturnFullText):
        self._ReturnFullText = ReturnFullText


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._ItemNames = params.get("ItemNames")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._ReturnFullText = params.get("ReturnFullText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRResponse(AbstractModel):
    """SmartStructuralOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Angle: 图片旋转角度(角度制)，文本的水平方向
为 0；顺时针为正，逆时针为负
        :type Angle: float
        :param _StructuralItems: 识别信息
        :type StructuralItems: list of StructuralItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Angle = None
        self._StructuralItems = None
        self._RequestId = None

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def StructuralItems(self):
        return self._StructuralItems

    @StructuralItems.setter
    def StructuralItems(self, StructuralItems):
        self._StructuralItems = StructuralItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Angle = params.get("Angle")
        if params.get("StructuralItems") is not None:
            self._StructuralItems = []
            for item in params.get("StructuralItems"):
                obj = StructuralItem()
                obj._deserialize(item)
                self._StructuralItems.append(obj)
        self._RequestId = params.get("RequestId")


class SmartStructuralOCRV2Request(AbstractModel):
    """SmartStructuralOCRV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
支持的图片像素：需介于20-10000px之间。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
支持的图片像素：需介于20-10000px之间。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        :param _ItemNames: 自定义结构化功能需返回的字段名称，例：
若客户只想返回姓名、性别两个字段的识别结果，则输入
ItemNames=["姓名","性别"]
        :type ItemNames: list of str
        :param _ReturnFullText: 是否开启全文字段识别
        :type ReturnFullText: bool
        :param _ConfigId: 配置id支持：
General -- 通用场景
OnlineTaxiItinerary -- 网约车行程单
RideHailingDriverLicense -- 网约车驾驶证
RideHailingTransportLicense -- 网约车运输证
WayBill -- 快递运单
AccountOpeningPermit -- 银行开户许可证
InvoiceEng -- 海外发票模版
        :type ConfigId: str
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._IsPdf = None
        self._PdfPageNumber = None
        self._ItemNames = None
        self._ReturnFullText = None
        self._ConfigId = None

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber

    @property
    def ItemNames(self):
        return self._ItemNames

    @ItemNames.setter
    def ItemNames(self, ItemNames):
        self._ItemNames = ItemNames

    @property
    def ReturnFullText(self):
        return self._ReturnFullText

    @ReturnFullText.setter
    def ReturnFullText(self, ReturnFullText):
        self._ReturnFullText = ReturnFullText

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        self._ItemNames = params.get("ItemNames")
        self._ReturnFullText = params.get("ReturnFullText")
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartStructuralOCRV2Response(AbstractModel):
    """SmartStructuralOCRV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Angle: 图片旋转角度(角度制)，文本的水平方向
为 0；顺时针为正，逆时针为负
        :type Angle: float
        :param _StructuralList: 配置结构化文本信息
        :type StructuralList: list of GroupInfo
        :param _WordList: 还原文本信息
        :type WordList: list of WordItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Angle = None
        self._StructuralList = None
        self._WordList = None
        self._RequestId = None

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def StructuralList(self):
        return self._StructuralList

    @StructuralList.setter
    def StructuralList(self, StructuralList):
        self._StructuralList = StructuralList

    @property
    def WordList(self):
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Angle = params.get("Angle")
        if params.get("StructuralList") is not None:
            self._StructuralList = []
            for item in params.get("StructuralList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._StructuralList.append(obj)
        if params.get("WordList") is not None:
            self._WordList = []
            for item in params.get("WordList"):
                obj = WordItem()
                obj._deserialize(item)
                self._WordList.append(obj)
        self._RequestId = params.get("RequestId")


class StructuralItem(AbstractModel):
    """智能结构化识别

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值。
        :type Value: str
        :param _Confidence: 置信度 0 ~100。
        :type Confidence: int
        :param _ItemCoord: 文本行在旋转纠正之后的图像中的像素
坐标。
        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        :param _Row: 字段所在行号，下标从0开始，非行字段或未能识别行号的该值返回-1。
        :type Row: int
        """
        self._Name = None
        self._Value = None
        self._Confidence = None
        self._ItemCoord = None
        self._Row = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def ItemCoord(self):
        return self._ItemCoord

    @ItemCoord.setter
    def ItemCoord(self, ItemCoord):
        self._ItemCoord = ItemCoord

    @property
    def Row(self):
        return self._Row

    @Row.setter
    def Row(self, Row):
        self._Row = Row


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Confidence = params.get("Confidence")
        if params.get("ItemCoord") is not None:
            self._ItemCoord = ItemCoord()
            self._ItemCoord._deserialize(params.get("ItemCoord"))
        self._Row = params.get("Row")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableCell(AbstractModel):
    """单元格数据

    """

    def __init__(self):
        r"""
        :param _ColTl: 单元格左上角的列索引
        :type ColTl: int
        :param _RowTl: 单元格左上角的行索引
        :type RowTl: int
        :param _ColBr: 单元格右下角的列索引
        :type ColBr: int
        :param _RowBr: 单元格右下角的行索引
        :type RowBr: int
        :param _Text: 单元格内识别出的字符串文本，若文本存在多行，以换行符"\n"隔开
        :type Text: str
        :param _Type: 单元格类型
        :type Type: str
        :param _Confidence: 单元格置信度
        :type Confidence: float
        :param _Polygon: 单元格在图像中的四点坐标
        :type Polygon: list of Coord
        :param _AdvancedInfo: 此字段为扩展字段
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedInfo: str
        :param _Contents: 单元格文本属性
        :type Contents: list of CellContent
        """
        self._ColTl = None
        self._RowTl = None
        self._ColBr = None
        self._RowBr = None
        self._Text = None
        self._Type = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None
        self._Contents = None

    @property
    def ColTl(self):
        return self._ColTl

    @ColTl.setter
    def ColTl(self, ColTl):
        self._ColTl = ColTl

    @property
    def RowTl(self):
        return self._RowTl

    @RowTl.setter
    def RowTl(self, RowTl):
        self._RowTl = RowTl

    @property
    def ColBr(self):
        return self._ColBr

    @ColBr.setter
    def ColBr(self, ColBr):
        self._ColBr = ColBr

    @property
    def RowBr(self):
        return self._RowBr

    @RowBr.setter
    def RowBr(self, RowBr):
        self._RowBr = RowBr

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def Contents(self):
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._ColTl = params.get("ColTl")
        self._RowTl = params.get("RowTl")
        self._ColBr = params.get("ColBr")
        self._RowBr = params.get("RowBr")
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = CellContent()
                obj._deserialize(item)
                self._Contents.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableCellInfo(AbstractModel):
    """单元格数据

    """

    def __init__(self):
        r"""
        :param _ColTl: 单元格左上角的列索引
        :type ColTl: int
        :param _RowTl: 单元格左上角的行索引
        :type RowTl: int
        :param _ColBr: 单元格右下角的列索引
        :type ColBr: int
        :param _RowBr: 单元格右下角的行索引
        :type RowBr: int
        :param _Text: 单元格内识别出的字符串文本，若文本存在多行，以换行符"\n"隔开
        :type Text: str
        :param _Type: 单元格类型
        :type Type: str
        :param _Confidence: 单元格置信度
        :type Confidence: float
        :param _Polygon: 单元格在图像中的四点坐标
        :type Polygon: list of Coord
        """
        self._ColTl = None
        self._RowTl = None
        self._ColBr = None
        self._RowBr = None
        self._Text = None
        self._Type = None
        self._Confidence = None
        self._Polygon = None

    @property
    def ColTl(self):
        return self._ColTl

    @ColTl.setter
    def ColTl(self, ColTl):
        self._ColTl = ColTl

    @property
    def RowTl(self):
        return self._RowTl

    @RowTl.setter
    def RowTl(self, RowTl):
        self._RowTl = RowTl

    @property
    def ColBr(self):
        return self._ColBr

    @ColBr.setter
    def ColBr(self, ColBr):
        self._ColBr = ColBr

    @property
    def RowBr(self):
        return self._RowBr

    @RowBr.setter
    def RowBr(self, RowBr):
        self._RowBr = RowBr

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon


    def _deserialize(self, params):
        self._ColTl = params.get("ColTl")
        self._RowTl = params.get("RowTl")
        self._ColBr = params.get("ColBr")
        self._RowBr = params.get("RowBr")
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableDetectInfo(AbstractModel):
    """表格内容检测

    """

    def __init__(self):
        r"""
        :param _Cells: 单元格内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Cells: list of TableCell
        :param _Titles: 表格标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Titles: list of TableTitle
        :param _Type: 图像中的文本块类型，0 为非表格文本，
1 为有线表格，2 为无线表格
（接口暂不支持日文无线表格识别，若传入日文无线表格，返回0）
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _TableCoordPoint: 表格主体四个顶点坐标（依次为左上角，
右上角，右下角，左下角）
注意：此字段可能返回 null，表示取不到有效值。
        :type TableCoordPoint: list of Coord
        """
        self._Cells = None
        self._Titles = None
        self._Type = None
        self._TableCoordPoint = None

    @property
    def Cells(self):
        return self._Cells

    @Cells.setter
    def Cells(self, Cells):
        self._Cells = Cells

    @property
    def Titles(self):
        return self._Titles

    @Titles.setter
    def Titles(self, Titles):
        self._Titles = Titles

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableCoordPoint(self):
        return self._TableCoordPoint

    @TableCoordPoint.setter
    def TableCoordPoint(self, TableCoordPoint):
        self._TableCoordPoint = TableCoordPoint


    def _deserialize(self, params):
        if params.get("Cells") is not None:
            self._Cells = []
            for item in params.get("Cells"):
                obj = TableCell()
                obj._deserialize(item)
                self._Cells.append(obj)
        if params.get("Titles") is not None:
            self._Titles = []
            for item in params.get("Titles"):
                obj = TableTitle()
                obj._deserialize(item)
                self._Titles.append(obj)
        self._Type = params.get("Type")
        if params.get("TableCoordPoint") is not None:
            self._TableCoordPoint = []
            for item in params.get("TableCoordPoint"):
                obj = Coord()
                obj._deserialize(item)
                self._TableCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableInfo(AbstractModel):
    """表格内容检测

    """

    def __init__(self):
        r"""
        :param _Cells: 单元格内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Cells: list of TableCellInfo
        :param _Type: 图像中的文本块类型，0 为非表格文本，
1 为有线表格，2 为无线表格
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _TableCoordPoint: 表格主体四个顶点坐标（依次为左上角，
右上角，右下角，左下角）
注意：此字段可能返回 null，表示取不到有效值。
        :type TableCoordPoint: list of Coord
        """
        self._Cells = None
        self._Type = None
        self._TableCoordPoint = None

    @property
    def Cells(self):
        return self._Cells

    @Cells.setter
    def Cells(self, Cells):
        self._Cells = Cells

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TableCoordPoint(self):
        return self._TableCoordPoint

    @TableCoordPoint.setter
    def TableCoordPoint(self, TableCoordPoint):
        self._TableCoordPoint = TableCoordPoint


    def _deserialize(self, params):
        if params.get("Cells") is not None:
            self._Cells = []
            for item in params.get("Cells"):
                obj = TableCellInfo()
                obj._deserialize(item)
                self._Cells.append(obj)
        self._Type = params.get("Type")
        if params.get("TableCoordPoint") is not None:
            self._TableCoordPoint = []
            for item in params.get("TableCoordPoint"):
                obj = Coord()
                obj._deserialize(item)
                self._TableCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableOCRRequest(AbstractModel):
    """TableOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableOCRResponse(AbstractModel):
    """TableOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，具体内容请点击左侧链接
        :type TextDetections: list of TextTable
        :param _Data: Base64 编码后的 Excel 数据。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._Data = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextTable()
                obj._deserialize(item)
                self._TextDetections.append(obj)
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class TableTitle(AbstractModel):
    """表格标题

    """

    def __init__(self):
        r"""
        :param _Text: 表格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaxiInvoiceOCRRequest(AbstractModel):
    """TaxiInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaxiInvoiceOCRResponse(AbstractModel):
    """TaxiInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvoiceNum: 发票代码
        :type InvoiceNum: str
        :param _InvoiceCode: 发票号码
        :type InvoiceCode: str
        :param _Date: 日期
        :type Date: str
        :param _Fare: 金额
        :type Fare: str
        :param _GetOnTime: 上车时间
        :type GetOnTime: str
        :param _GetOffTime: 下车时间
        :type GetOffTime: str
        :param _Distance: 里程
        :type Distance: str
        :param _Location: 发票所在地
        :type Location: str
        :param _PlateNumber: 车牌号
        :type PlateNumber: str
        :param _InvoiceType: 发票消费类型
        :type InvoiceType: str
        :param _Province: 省
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _City: 市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvoiceNum = None
        self._InvoiceCode = None
        self._Date = None
        self._Fare = None
        self._GetOnTime = None
        self._GetOffTime = None
        self._Distance = None
        self._Location = None
        self._PlateNumber = None
        self._InvoiceType = None
        self._Province = None
        self._City = None
        self._RequestId = None

    @property
    def InvoiceNum(self):
        return self._InvoiceNum

    @InvoiceNum.setter
    def InvoiceNum(self, InvoiceNum):
        self._InvoiceNum = InvoiceNum

    @property
    def InvoiceCode(self):
        return self._InvoiceCode

    @InvoiceCode.setter
    def InvoiceCode(self, InvoiceCode):
        self._InvoiceCode = InvoiceCode

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Fare(self):
        return self._Fare

    @Fare.setter
    def Fare(self, Fare):
        self._Fare = Fare

    @property
    def GetOnTime(self):
        return self._GetOnTime

    @GetOnTime.setter
    def GetOnTime(self, GetOnTime):
        self._GetOnTime = GetOnTime

    @property
    def GetOffTime(self):
        return self._GetOffTime

    @GetOffTime.setter
    def GetOffTime(self, GetOffTime):
        self._GetOffTime = GetOffTime

    @property
    def Distance(self):
        return self._Distance

    @Distance.setter
    def Distance(self, Distance):
        self._Distance = Distance

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def PlateNumber(self):
        return self._PlateNumber

    @PlateNumber.setter
    def PlateNumber(self, PlateNumber):
        self._PlateNumber = PlateNumber

    @property
    def InvoiceType(self):
        return self._InvoiceType

    @InvoiceType.setter
    def InvoiceType(self, InvoiceType):
        self._InvoiceType = InvoiceType

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvoiceNum = params.get("InvoiceNum")
        self._InvoiceCode = params.get("InvoiceCode")
        self._Date = params.get("Date")
        self._Fare = params.get("Fare")
        self._GetOnTime = params.get("GetOnTime")
        self._GetOffTime = params.get("GetOffTime")
        self._Distance = params.get("Distance")
        self._Location = params.get("Location")
        self._PlateNumber = params.get("PlateNumber")
        self._InvoiceType = params.get("InvoiceType")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._RequestId = params.get("RequestId")


class TaxiTicket(AbstractModel):
    """出租车发票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Date: 开票日期
        :type Date: str
        :param _TimeGetOn: 上车时间
        :type TimeGetOn: str
        :param _TimeGetOff: 下车时间
        :type TimeGetOff: str
        :param _Price: 单价
        :type Price: str
        :param _Mileage: 里程
        :type Mileage: str
        :param _Total: 总金额
        :type Total: str
        :param _Place: 发票所在地
        :type Place: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _LicensePlate: 车牌号
        :type LicensePlate: str
        :param _FuelFee: 燃油附加费
        :type FuelFee: str
        :param _BookingCallFee: 预约叫车服务费
        :type BookingCallFee: str
        :param _CompanySealMark: 是否有公司印章（0：没有，1：有）
        :type CompanySealMark: int
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._TimeGetOn = None
        self._TimeGetOff = None
        self._Price = None
        self._Mileage = None
        self._Total = None
        self._Place = None
        self._Province = None
        self._City = None
        self._Kind = None
        self._LicensePlate = None
        self._FuelFee = None
        self._BookingCallFee = None
        self._CompanySealMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def TimeGetOff(self):
        return self._TimeGetOff

    @TimeGetOff.setter
    def TimeGetOff(self, TimeGetOff):
        self._TimeGetOff = TimeGetOff

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Mileage(self):
        return self._Mileage

    @Mileage.setter
    def Mileage(self, Mileage):
        self._Mileage = Mileage

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Place(self):
        return self._Place

    @Place.setter
    def Place(self, Place):
        self._Place = Place

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def LicensePlate(self):
        return self._LicensePlate

    @LicensePlate.setter
    def LicensePlate(self, LicensePlate):
        self._LicensePlate = LicensePlate

    @property
    def FuelFee(self):
        return self._FuelFee

    @FuelFee.setter
    def FuelFee(self, FuelFee):
        self._FuelFee = FuelFee

    @property
    def BookingCallFee(self):
        return self._BookingCallFee

    @BookingCallFee.setter
    def BookingCallFee(self, BookingCallFee):
        self._BookingCallFee = BookingCallFee

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._TimeGetOn = params.get("TimeGetOn")
        self._TimeGetOff = params.get("TimeGetOff")
        self._Price = params.get("Price")
        self._Mileage = params.get("Mileage")
        self._Total = params.get("Total")
        self._Place = params.get("Place")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Kind = params.get("Kind")
        self._LicensePlate = params.get("LicensePlate")
        self._FuelFee = params.get("FuelFee")
        self._BookingCallFee = params.get("BookingCallFee")
        self._CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextArithmetic(AbstractModel):
    """算式识别结果

    """

    def __init__(self):
        r"""
        :param _DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param _Result: 算式运算结果，true-正确   false-错误或非法参数
        :type Result: bool
        :param _Confidence: 保留字段，暂不支持
        :type Confidence: int
        :param _Polygon: 原图文本行坐标，以四个顶点坐标表示（保留字段，暂不支持）
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param _AdvancedInfo: 保留字段，暂不支持
        :type AdvancedInfo: str
        :param _ItemCoord: 文本行旋转纠正之后在图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type ItemCoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        :param _ExpressionType: 算式题型编号：
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
        :param _Answer: 错题推荐答案，算式运算结果正确返回为""，算式运算结果错误返回推荐答案 (注：暂不支持多个关系运算符（如1<10<7）、无关系运算符（如frac(1,2)+frac(2,3)）、单位换算（如1元=100角）错题的推荐答案返回)
        :type Answer: str
        """
        self._DetectedText = None
        self._Result = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None
        self._ItemCoord = None
        self._ExpressionType = None
        self._Answer = None

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def ItemCoord(self):
        return self._ItemCoord

    @ItemCoord.setter
    def ItemCoord(self, ItemCoord):
        self._ItemCoord = ItemCoord

    @property
    def ExpressionType(self):
        return self._ExpressionType

    @ExpressionType.setter
    def ExpressionType(self, ExpressionType):
        self._ExpressionType = ExpressionType

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        self._Result = params.get("Result")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        if params.get("ItemCoord") is not None:
            self._ItemCoord = ItemCoord()
            self._ItemCoord._deserialize(params.get("ItemCoord"))
        self._ExpressionType = params.get("ExpressionType")
        self._Answer = params.get("Answer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectRequest(AbstractModel):
    """TextDetect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectResponse(AbstractModel):
    """TextDetect返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HasText: 图片中是否包含文字。
        :type HasText: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HasText = None
        self._RequestId = None

    @property
    def HasText(self):
        return self._HasText

    @HasText.setter
    def HasText(self, HasText):
        self._HasText = HasText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HasText = params.get("HasText")
        self._RequestId = params.get("RequestId")


class TextDetection(AbstractModel):
    """文字识别结果

    """

    def __init__(self):
        r"""
        :param _DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param _Confidence: 置信度 0 ~100
        :type Confidence: int
        :param _Polygon: 文本行坐标，以四个顶点坐标表示
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param _AdvancedInfo: 此字段为扩展字段。
GeneralBasicOcr接口返回段落信息Parag，包含ParagNo。
        :type AdvancedInfo: str
        :param _ItemPolygon: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type ItemPolygon: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        :param _Words: 识别出来的单字信息包括单字（包括单字Character和单字置信度confidence）， 支持识别的接口：GeneralBasicOCR、GeneralAccurateOCR
        :type Words: list of DetectedWords
        :param _WordCoordPoint: 单字在原图中的四点坐标， 支持识别的接口：GeneralBasicOCR、GeneralAccurateOCR
        :type WordCoordPoint: list of DetectedWordCoordPoint
        """
        self._DetectedText = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None
        self._ItemPolygon = None
        self._Words = None
        self._WordCoordPoint = None

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def ItemPolygon(self):
        return self._ItemPolygon

    @ItemPolygon.setter
    def ItemPolygon(self, ItemPolygon):
        self._ItemPolygon = ItemPolygon

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def WordCoordPoint(self):
        return self._WordCoordPoint

    @WordCoordPoint.setter
    def WordCoordPoint(self, WordCoordPoint):
        self._WordCoordPoint = WordCoordPoint


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        if params.get("ItemPolygon") is not None:
            self._ItemPolygon = ItemCoord()
            self._ItemPolygon._deserialize(params.get("ItemPolygon"))
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = DetectedWords()
                obj._deserialize(item)
                self._Words.append(obj)
        if params.get("WordCoordPoint") is not None:
            self._WordCoordPoint = []
            for item in params.get("WordCoordPoint"):
                obj = DetectedWordCoordPoint()
                obj._deserialize(item)
                self._WordCoordPoint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectionEn(AbstractModel):
    """英文识别结果

    """

    def __init__(self):
        r"""
        :param _DetectedText: 识别出的文本行内容。
        :type DetectedText: str
        :param _Confidence: 置信度 0 ~100。
        :type Confidence: int
        :param _Polygon: 文本行在原图中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param _AdvancedInfo: 此字段为扩展字段。目前EnglishOCR接口返回内容为空。
        :type AdvancedInfo: str
        :param _WordCoordPoint: 英文单词在原图中的四点坐标。
        :type WordCoordPoint: list of WordCoordPoint
        :param _CandWord: 候选字符集(包含候选字Character以及置信度Confidence)。
        :type CandWord: list of CandWord
        :param _Words: 识别出来的单词信息（包括单词Character和单词置信度confidence）
        :type Words: list of Words
        """
        self._DetectedText = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None
        self._WordCoordPoint = None
        self._CandWord = None
        self._Words = None

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def WordCoordPoint(self):
        return self._WordCoordPoint

    @WordCoordPoint.setter
    def WordCoordPoint(self, WordCoordPoint):
        self._WordCoordPoint = WordCoordPoint

    @property
    def CandWord(self):
        return self._CandWord

    @CandWord.setter
    def CandWord(self, CandWord):
        self._CandWord = CandWord

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        if params.get("WordCoordPoint") is not None:
            self._WordCoordPoint = []
            for item in params.get("WordCoordPoint"):
                obj = WordCoordPoint()
                obj._deserialize(item)
                self._WordCoordPoint.append(obj)
        if params.get("CandWord") is not None:
            self._CandWord = []
            for item in params.get("CandWord"):
                obj = CandWord()
                obj._deserialize(item)
                self._CandWord.append(obj)
        if params.get("Words") is not None:
            self._Words = []
            for item in params.get("Words"):
                obj = Words()
                obj._deserialize(item)
                self._Words.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextDetectionResult(AbstractModel):
    """识别结果

    """

    def __init__(self):
        r"""
        :param _Value: 识别出的文本行内容
        :type Value: str
        :param _Polygon: 坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        """
        self._Value = None
        self._Polygon = None

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon


    def _deserialize(self, params):
        self._Value = params.get("Value")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextEduPaper(AbstractModel):
    """数学试题识别结果

    """

    def __init__(self):
        r"""
        :param _Item: 识别出的字段名称（关键字）
        :type Item: str
        :param _DetectedText: 识别出的字段名称对应的值，也就是字段Item对应的字符串结果
        :type DetectedText: str
        :param _Itemcoord: 文本行在旋转纠正之后的图像中的像素坐标，表示为（左上角x, 左上角y，宽width，高height）
        :type Itemcoord: :class:`tencentcloud.ocr.v20181119.models.ItemCoord`
        """
        self._Item = None
        self._DetectedText = None
        self._Itemcoord = None

    @property
    def Item(self):
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Itemcoord(self):
        return self._Itemcoord

    @Itemcoord.setter
    def Itemcoord(self, Itemcoord):
        self._Itemcoord = Itemcoord


    def _deserialize(self, params):
        self._Item = params.get("Item")
        self._DetectedText = params.get("DetectedText")
        if params.get("Itemcoord") is not None:
            self._Itemcoord = ItemCoord()
            self._Itemcoord._deserialize(params.get("Itemcoord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextFormula(AbstractModel):
    """数学公式识别结果

    """

    def __init__(self):
        r"""
        :param _DetectedText: 识别出的文本行内容
        :type DetectedText: str
        """
        self._DetectedText = None

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextGeneralHandwriting(AbstractModel):
    """文字识别结果

    """

    def __init__(self):
        r"""
        :param _DetectedText: 识别出的文本行内容
        :type DetectedText: str
        :param _Confidence: 置信度 0 - 100
        :type Confidence: int
        :param _Polygon: 文本行坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        :param _AdvancedInfo: 此字段为扩展字段。
能返回文本行的段落信息，例如：{\"Parag\":{\"ParagNo\":2}}，
其中ParagNo为段落行，从1开始。
        :type AdvancedInfo: str
        :param _WordPolygon: 字的坐标数组，以四个顶点坐标表示
注意：此字段可能返回 null，表示取不到有效值。
        :type WordPolygon: list of Polygon
        """
        self._DetectedText = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None
        self._WordPolygon = None

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def WordPolygon(self):
        return self._WordPolygon

    @WordPolygon.setter
    def WordPolygon(self, WordPolygon):
        self._WordPolygon = WordPolygon


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        if params.get("WordPolygon") is not None:
            self._WordPolygon = []
            for item in params.get("WordPolygon"):
                obj = Polygon()
                obj._deserialize(item)
                self._WordPolygon.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTable(AbstractModel):
    """表格识别结果

    """

    def __init__(self):
        r"""
        :param _ColTl: 单元格左上角的列索引
        :type ColTl: int
        :param _RowTl: 单元格左上角的行索引
        :type RowTl: int
        :param _ColBr: 单元格右下角的列索引
        :type ColBr: int
        :param _RowBr: 单元格右下角的行索引
        :type RowBr: int
        :param _Text: 单元格文字
        :type Text: str
        :param _Type: 单元格类型，包含body（表格主体）、header（表头）、footer（表尾）三种
        :type Type: str
        :param _Confidence: 置信度 0 ~100
        :type Confidence: int
        :param _Polygon: 文本行坐标，以四个顶点坐标表示
        :type Polygon: list of Coord
        :param _AdvancedInfo: 此字段为扩展字段
        :type AdvancedInfo: str
        """
        self._ColTl = None
        self._RowTl = None
        self._ColBr = None
        self._RowBr = None
        self._Text = None
        self._Type = None
        self._Confidence = None
        self._Polygon = None
        self._AdvancedInfo = None

    @property
    def ColTl(self):
        return self._ColTl

    @ColTl.setter
    def ColTl(self, ColTl):
        self._ColTl = ColTl

    @property
    def RowTl(self):
        return self._RowTl

    @RowTl.setter
    def RowTl(self, RowTl):
        self._RowTl = RowTl

    @property
    def ColBr(self):
        return self._ColBr

    @ColBr.setter
    def ColBr(self, ColBr):
        self._ColBr = ColBr

    @property
    def RowBr(self):
        return self._RowBr

    @RowBr.setter
    def RowBr(self, RowBr):
        self._RowBr = RowBr

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo


    def _deserialize(self, params):
        self._ColTl = params.get("ColTl")
        self._RowTl = params.get("RowTl")
        self._ColBr = params.get("ColBr")
        self._RowBr = params.get("RowBr")
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self._Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self._Polygon.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextVatInvoice(AbstractModel):
    """增值税发票识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称（关键字）。支持以下字段的识别：
发票代码、 发票号码、 打印发票代码、 打印发票号码、 开票日期、 购买方识别号、 小写金额、 价税合计(大写)、 销售方识别号、 校验码、 购买方名称、 销售方名称、 税额、 复核、 联次名称、 备注、 联次、 密码区、 开票人、 收款人、 （货物或应税劳务、服务名称）、省、 市、 服务类型、 通行费标志、 是否代开、 是否收购、 合计金额、 是否有公司印章、 发票消费类型、 车船税、 机器编号、 成品油标志、 税率、 合计税额、 （购买方地址、电话）、 （销售方地址、电话）、 单价、 金额、 销售方开户行及账号、 购买方开户行及账号、 规格型号、 发票名称、 单位、 数量、 校验码备选、 校验码后六位备选、发票号码备选、车牌号、类型、通行日期起、通行日期止、发票类型。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Polygon: 字段在原图中的中的四点坐标。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self._Name = None
        self._Value = None
        self._Polygon = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Polygon") is not None:
            self._Polygon = Polygon()
            self._Polygon._deserialize(params.get("Polygon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextVehicleBack(AbstractModel):
    """行驶证副页正面的识别结果

    """

    def __init__(self):
        r"""
        :param _PlateNo: 号牌号码
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateNo: str
        :param _FileNo: 档案编号
注意：此字段可能返回 null，表示取不到有效值。
        :type FileNo: str
        :param _AllowNum: 核定人数
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowNum: str
        :param _TotalMass: 总质量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalMass: str
        :param _CurbWeight: 整备质量
注意：此字段可能返回 null，表示取不到有效值。
        :type CurbWeight: str
        :param _LoadQuality: 核定载质量
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadQuality: str
        :param _ExternalSize: 外廓尺寸
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalSize: str
        :param _Marks: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Marks: str
        :param _Record: 检验记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Record: str
        :param _TotalQuasiMass: 准牵引总质量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalQuasiMass: str
        :param _SubPageCode: 副页编码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubPageCode: str
        """
        self._PlateNo = None
        self._FileNo = None
        self._AllowNum = None
        self._TotalMass = None
        self._CurbWeight = None
        self._LoadQuality = None
        self._ExternalSize = None
        self._Marks = None
        self._Record = None
        self._TotalQuasiMass = None
        self._SubPageCode = None

    @property
    def PlateNo(self):
        return self._PlateNo

    @PlateNo.setter
    def PlateNo(self, PlateNo):
        self._PlateNo = PlateNo

    @property
    def FileNo(self):
        return self._FileNo

    @FileNo.setter
    def FileNo(self, FileNo):
        self._FileNo = FileNo

    @property
    def AllowNum(self):
        return self._AllowNum

    @AllowNum.setter
    def AllowNum(self, AllowNum):
        self._AllowNum = AllowNum

    @property
    def TotalMass(self):
        return self._TotalMass

    @TotalMass.setter
    def TotalMass(self, TotalMass):
        self._TotalMass = TotalMass

    @property
    def CurbWeight(self):
        return self._CurbWeight

    @CurbWeight.setter
    def CurbWeight(self, CurbWeight):
        self._CurbWeight = CurbWeight

    @property
    def LoadQuality(self):
        return self._LoadQuality

    @LoadQuality.setter
    def LoadQuality(self, LoadQuality):
        self._LoadQuality = LoadQuality

    @property
    def ExternalSize(self):
        return self._ExternalSize

    @ExternalSize.setter
    def ExternalSize(self, ExternalSize):
        self._ExternalSize = ExternalSize

    @property
    def Marks(self):
        return self._Marks

    @Marks.setter
    def Marks(self, Marks):
        self._Marks = Marks

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def TotalQuasiMass(self):
        return self._TotalQuasiMass

    @TotalQuasiMass.setter
    def TotalQuasiMass(self, TotalQuasiMass):
        self._TotalQuasiMass = TotalQuasiMass

    @property
    def SubPageCode(self):
        return self._SubPageCode

    @SubPageCode.setter
    def SubPageCode(self, SubPageCode):
        self._SubPageCode = SubPageCode


    def _deserialize(self, params):
        self._PlateNo = params.get("PlateNo")
        self._FileNo = params.get("FileNo")
        self._AllowNum = params.get("AllowNum")
        self._TotalMass = params.get("TotalMass")
        self._CurbWeight = params.get("CurbWeight")
        self._LoadQuality = params.get("LoadQuality")
        self._ExternalSize = params.get("ExternalSize")
        self._Marks = params.get("Marks")
        self._Record = params.get("Record")
        self._TotalQuasiMass = params.get("TotalQuasiMass")
        self._SubPageCode = params.get("SubPageCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextVehicleFront(AbstractModel):
    """行驶证主页正面的识别结果

    """

    def __init__(self):
        r"""
        :param _PlateNo: 号牌号码
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateNo: str
        :param _VehicleType: 车辆类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VehicleType: str
        :param _Owner: 所有人
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param _Address: 住址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _UseCharacter: 使用性质
注意：此字段可能返回 null，表示取不到有效值。
        :type UseCharacter: str
        :param _Model: 品牌型号
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param _Vin: 车辆识别代号
注意：此字段可能返回 null，表示取不到有效值。
        :type Vin: str
        :param _EngineNo: 发动机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineNo: str
        :param _RegisterDate: 注册日期
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisterDate: str
        :param _IssueDate: 发证日期
注意：此字段可能返回 null，表示取不到有效值。
        :type IssueDate: str
        :param _Seal: 印章
注意：此字段可能返回 null，表示取不到有效值。
        :type Seal: str
        """
        self._PlateNo = None
        self._VehicleType = None
        self._Owner = None
        self._Address = None
        self._UseCharacter = None
        self._Model = None
        self._Vin = None
        self._EngineNo = None
        self._RegisterDate = None
        self._IssueDate = None
        self._Seal = None

    @property
    def PlateNo(self):
        return self._PlateNo

    @PlateNo.setter
    def PlateNo(self, PlateNo):
        self._PlateNo = PlateNo

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def UseCharacter(self):
        return self._UseCharacter

    @UseCharacter.setter
    def UseCharacter(self, UseCharacter):
        self._UseCharacter = UseCharacter

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Vin(self):
        return self._Vin

    @Vin.setter
    def Vin(self, Vin):
        self._Vin = Vin

    @property
    def EngineNo(self):
        return self._EngineNo

    @EngineNo.setter
    def EngineNo(self, EngineNo):
        self._EngineNo = EngineNo

    @property
    def RegisterDate(self):
        return self._RegisterDate

    @RegisterDate.setter
    def RegisterDate(self, RegisterDate):
        self._RegisterDate = RegisterDate

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def Seal(self):
        return self._Seal

    @Seal.setter
    def Seal(self, Seal):
        self._Seal = Seal


    def _deserialize(self, params):
        self._PlateNo = params.get("PlateNo")
        self._VehicleType = params.get("VehicleType")
        self._Owner = params.get("Owner")
        self._Address = params.get("Address")
        self._UseCharacter = params.get("UseCharacter")
        self._Model = params.get("Model")
        self._Vin = params.get("Vin")
        self._EngineNo = params.get("EngineNo")
        self._RegisterDate = params.get("RegisterDate")
        self._IssueDate = params.get("IssueDate")
        self._Seal = params.get("Seal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWaybill(AbstractModel):
    """运单识别结果

    """

    def __init__(self):
        r"""
        :param _RecName: 收件人姓名
        :type RecName: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param _RecNum: 收件人手机号
        :type RecNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param _RecAddr: 收件人地址
        :type RecAddr: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param _SenderName: 寄件人姓名
        :type SenderName: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param _SenderNum: 寄件人手机号
        :type SenderNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param _SenderAddr: 寄件人地址
        :type SenderAddr: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        :param _WaybillNum: 运单号
        :type WaybillNum: :class:`tencentcloud.ocr.v20181119.models.WaybillObj`
        """
        self._RecName = None
        self._RecNum = None
        self._RecAddr = None
        self._SenderName = None
        self._SenderNum = None
        self._SenderAddr = None
        self._WaybillNum = None

    @property
    def RecName(self):
        return self._RecName

    @RecName.setter
    def RecName(self, RecName):
        self._RecName = RecName

    @property
    def RecNum(self):
        return self._RecNum

    @RecNum.setter
    def RecNum(self, RecNum):
        self._RecNum = RecNum

    @property
    def RecAddr(self):
        return self._RecAddr

    @RecAddr.setter
    def RecAddr(self, RecAddr):
        self._RecAddr = RecAddr

    @property
    def SenderName(self):
        return self._SenderName

    @SenderName.setter
    def SenderName(self, SenderName):
        self._SenderName = SenderName

    @property
    def SenderNum(self):
        return self._SenderNum

    @SenderNum.setter
    def SenderNum(self, SenderNum):
        self._SenderNum = SenderNum

    @property
    def SenderAddr(self):
        return self._SenderAddr

    @SenderAddr.setter
    def SenderAddr(self, SenderAddr):
        self._SenderAddr = SenderAddr

    @property
    def WaybillNum(self):
        return self._WaybillNum

    @WaybillNum.setter
    def WaybillNum(self, WaybillNum):
        self._WaybillNum = WaybillNum


    def _deserialize(self, params):
        if params.get("RecName") is not None:
            self._RecName = WaybillObj()
            self._RecName._deserialize(params.get("RecName"))
        if params.get("RecNum") is not None:
            self._RecNum = WaybillObj()
            self._RecNum._deserialize(params.get("RecNum"))
        if params.get("RecAddr") is not None:
            self._RecAddr = WaybillObj()
            self._RecAddr._deserialize(params.get("RecAddr"))
        if params.get("SenderName") is not None:
            self._SenderName = WaybillObj()
            self._SenderName._deserialize(params.get("SenderName"))
        if params.get("SenderNum") is not None:
            self._SenderNum = WaybillObj()
            self._SenderNum._deserialize(params.get("SenderNum"))
        if params.get("SenderAddr") is not None:
            self._SenderAddr = WaybillObj()
            self._SenderAddr._deserialize(params.get("SenderAddr"))
        if params.get("WaybillNum") is not None:
            self._WaybillNum = WaybillObj()
            self._WaybillNum._deserialize(params.get("WaybillNum"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoice(AbstractModel):
    """过路过桥费发票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Date: 日期
        :type Date: str
        :param _Time: 时间
        :type Time: str
        :param _Entrance: 入口
        :type Entrance: str
        :param _Exit: 出口
        :type Exit: str
        :param _HighwayMark: 高速标志（0：没有，1：有）
        :type HighwayMark: int
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._Total = None
        self._Kind = None
        self._Date = None
        self._Time = None
        self._Entrance = None
        self._Exit = None
        self._HighwayMark = None
        self._QRCodeMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Entrance(self):
        return self._Entrance

    @Entrance.setter
    def Entrance(self, Entrance):
        self._Entrance = Entrance

    @property
    def Exit(self):
        return self._Exit

    @Exit.setter
    def Exit(self, Exit):
        self._Exit = Exit

    @property
    def HighwayMark(self):
        return self._HighwayMark

    @HighwayMark.setter
    def HighwayMark(self, HighwayMark):
        self._HighwayMark = HighwayMark

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._Date = params.get("Date")
        self._Time = params.get("Time")
        self._Entrance = params.get("Entrance")
        self._Exit = params.get("Exit")
        self._HighwayMark = params.get("HighwayMark")
        self._QRCodeMark = params.get("QRCodeMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoiceInfo(AbstractModel):
    """过路过桥费字段信息

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称（关键字）。支持以下字段的识别：
发票代码、发票号码、日期、金额、入口、出口、时间、发票消费类型、高速标志。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Value = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoiceOCRRequest(AbstractModel):
    """TollInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TollInvoiceOCRResponse(AbstractModel):
    """TollInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TollInvoiceInfos: 过路过桥费发票识别结果，具体内容请点击左侧链接。
        :type TollInvoiceInfos: list of TollInvoiceInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TollInvoiceInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def TollInvoiceInfos(self):
        return self._TollInvoiceInfos

    @TollInvoiceInfos.setter
    def TollInvoiceInfos(self, TollInvoiceInfos):
        self._TollInvoiceInfos = TollInvoiceInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TollInvoiceInfos") is not None:
            self._TollInvoiceInfos = []
            for item in params.get("TollInvoiceInfos"):
                obj = TollInvoiceInfo()
                obj._deserialize(item)
                self._TollInvoiceInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class TrainTicket(AbstractModel):
    """火车票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Number: 发票号码
        :type Number: str
        :param _DateGetOn: 乘车日期
        :type DateGetOn: str
        :param _TimeGetOn: 乘车时间
        :type TimeGetOn: str
        :param _Name: 乘车人姓名
        :type Name: str
        :param _StationGetOn: 出发车站
        :type StationGetOn: str
        :param _StationGetOff: 到达车站
        :type StationGetOff: str
        :param _Seat: 座位类型
        :type Seat: str
        :param _Total: 总金额
        :type Total: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _SerialNumber: 序列号
        :type SerialNumber: str
        :param _UserID: 身份证号
        :type UserID: str
        :param _GateNumber: 检票口
        :type GateNumber: str
        :param _TrainNumber: 车次
        :type TrainNumber: str
        :param _HandlingFee: 手续费
        :type HandlingFee: str
        :param _OriginalFare: 原票价
        :type OriginalFare: str
        :param _TotalCn: 大写金额
        :type TotalCn: str
        :param _SeatNumber: 座位号
        :type SeatNumber: str
        :param _PickUpAddress: 取票地址
        :type PickUpAddress: str
        :param _TicketChange: 是否始发改签
        :type TicketChange: str
        :param _AdditionalFare: 加收票价
        :type AdditionalFare: str
        :param _ReceiptNumber: 收据号码
        :type ReceiptNumber: str
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _ReimburseOnlyMark: 是否仅供报销使用（0：没有，1：有）
        :type ReimburseOnlyMark: int
        :param _RefundMark: 是否有退票费标识（0：没有，1：有）
        :type RefundMark: int
        """
        self._Title = None
        self._Number = None
        self._DateGetOn = None
        self._TimeGetOn = None
        self._Name = None
        self._StationGetOn = None
        self._StationGetOff = None
        self._Seat = None
        self._Total = None
        self._Kind = None
        self._SerialNumber = None
        self._UserID = None
        self._GateNumber = None
        self._TrainNumber = None
        self._HandlingFee = None
        self._OriginalFare = None
        self._TotalCn = None
        self._SeatNumber = None
        self._PickUpAddress = None
        self._TicketChange = None
        self._AdditionalFare = None
        self._ReceiptNumber = None
        self._QRCodeMark = None
        self._ReimburseOnlyMark = None
        self._RefundMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def DateGetOn(self):
        return self._DateGetOn

    @DateGetOn.setter
    def DateGetOn(self, DateGetOn):
        self._DateGetOn = DateGetOn

    @property
    def TimeGetOn(self):
        return self._TimeGetOn

    @TimeGetOn.setter
    def TimeGetOn(self, TimeGetOn):
        self._TimeGetOn = TimeGetOn

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StationGetOn(self):
        return self._StationGetOn

    @StationGetOn.setter
    def StationGetOn(self, StationGetOn):
        self._StationGetOn = StationGetOn

    @property
    def StationGetOff(self):
        return self._StationGetOff

    @StationGetOff.setter
    def StationGetOff(self, StationGetOff):
        self._StationGetOff = StationGetOff

    @property
    def Seat(self):
        return self._Seat

    @Seat.setter
    def Seat(self, Seat):
        self._Seat = Seat

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def UserID(self):
        return self._UserID

    @UserID.setter
    def UserID(self, UserID):
        self._UserID = UserID

    @property
    def GateNumber(self):
        return self._GateNumber

    @GateNumber.setter
    def GateNumber(self, GateNumber):
        self._GateNumber = GateNumber

    @property
    def TrainNumber(self):
        return self._TrainNumber

    @TrainNumber.setter
    def TrainNumber(self, TrainNumber):
        self._TrainNumber = TrainNumber

    @property
    def HandlingFee(self):
        return self._HandlingFee

    @HandlingFee.setter
    def HandlingFee(self, HandlingFee):
        self._HandlingFee = HandlingFee

    @property
    def OriginalFare(self):
        return self._OriginalFare

    @OriginalFare.setter
    def OriginalFare(self, OriginalFare):
        self._OriginalFare = OriginalFare

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def SeatNumber(self):
        return self._SeatNumber

    @SeatNumber.setter
    def SeatNumber(self, SeatNumber):
        self._SeatNumber = SeatNumber

    @property
    def PickUpAddress(self):
        return self._PickUpAddress

    @PickUpAddress.setter
    def PickUpAddress(self, PickUpAddress):
        self._PickUpAddress = PickUpAddress

    @property
    def TicketChange(self):
        return self._TicketChange

    @TicketChange.setter
    def TicketChange(self, TicketChange):
        self._TicketChange = TicketChange

    @property
    def AdditionalFare(self):
        return self._AdditionalFare

    @AdditionalFare.setter
    def AdditionalFare(self, AdditionalFare):
        self._AdditionalFare = AdditionalFare

    @property
    def ReceiptNumber(self):
        return self._ReceiptNumber

    @ReceiptNumber.setter
    def ReceiptNumber(self, ReceiptNumber):
        self._ReceiptNumber = ReceiptNumber

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def ReimburseOnlyMark(self):
        return self._ReimburseOnlyMark

    @ReimburseOnlyMark.setter
    def ReimburseOnlyMark(self, ReimburseOnlyMark):
        self._ReimburseOnlyMark = ReimburseOnlyMark

    @property
    def RefundMark(self):
        return self._RefundMark

    @RefundMark.setter
    def RefundMark(self, RefundMark):
        self._RefundMark = RefundMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._DateGetOn = params.get("DateGetOn")
        self._TimeGetOn = params.get("TimeGetOn")
        self._Name = params.get("Name")
        self._StationGetOn = params.get("StationGetOn")
        self._StationGetOff = params.get("StationGetOff")
        self._Seat = params.get("Seat")
        self._Total = params.get("Total")
        self._Kind = params.get("Kind")
        self._SerialNumber = params.get("SerialNumber")
        self._UserID = params.get("UserID")
        self._GateNumber = params.get("GateNumber")
        self._TrainNumber = params.get("TrainNumber")
        self._HandlingFee = params.get("HandlingFee")
        self._OriginalFare = params.get("OriginalFare")
        self._TotalCn = params.get("TotalCn")
        self._SeatNumber = params.get("SeatNumber")
        self._PickUpAddress = params.get("PickUpAddress")
        self._TicketChange = params.get("TicketChange")
        self._AdditionalFare = params.get("AdditionalFare")
        self._ReceiptNumber = params.get("ReceiptNumber")
        self._QRCodeMark = params.get("QRCodeMark")
        self._ReimburseOnlyMark = params.get("ReimburseOnlyMark")
        self._RefundMark = params.get("RefundMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainTicketOCRRequest(AbstractModel):
    """TrainTicketOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainTicketOCRResponse(AbstractModel):
    """TrainTicketOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TicketNum: 编号
        :type TicketNum: str
        :param _StartStation: 出发站
        :type StartStation: str
        :param _DestinationStation: 到达站
        :type DestinationStation: str
        :param _Date: 出发时间
        :type Date: str
        :param _TrainNum: 车次
        :type TrainNum: str
        :param _Seat: 座位号
        :type Seat: str
        :param _Name: 姓名
        :type Name: str
        :param _Price: 票价
        :type Price: str
        :param _SeatCategory: 席别
        :type SeatCategory: str
        :param _ID: 身份证号
        :type ID: str
        :param _InvoiceType: 发票消费类型：交通
        :type InvoiceType: str
        :param _SerialNumber: 序列号
        :type SerialNumber: str
        :param _AdditionalCost: 加收票价
        :type AdditionalCost: str
        :param _HandlingFee: 手续费
        :type HandlingFee: str
        :param _LegalAmount: 大写金额（票面有大写金额该字段才有值）
        :type LegalAmount: str
        :param _TicketStation: 售票站
        :type TicketStation: str
        :param _OriginalPrice: 原票价（一般有手续费的才有原始票价字段）
        :type OriginalPrice: str
        :param _InvoiceStyle: 发票类型：火车票、火车票补票、火车票退票凭证
        :type InvoiceStyle: str
        :param _ReceiptNumber: 收据号码
        :type ReceiptNumber: str
        :param _IsReceipt: 仅供报销使用：1为是，0为否
        :type IsReceipt: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TicketNum = None
        self._StartStation = None
        self._DestinationStation = None
        self._Date = None
        self._TrainNum = None
        self._Seat = None
        self._Name = None
        self._Price = None
        self._SeatCategory = None
        self._ID = None
        self._InvoiceType = None
        self._SerialNumber = None
        self._AdditionalCost = None
        self._HandlingFee = None
        self._LegalAmount = None
        self._TicketStation = None
        self._OriginalPrice = None
        self._InvoiceStyle = None
        self._ReceiptNumber = None
        self._IsReceipt = None
        self._RequestId = None

    @property
    def TicketNum(self):
        return self._TicketNum

    @TicketNum.setter
    def TicketNum(self, TicketNum):
        self._TicketNum = TicketNum

    @property
    def StartStation(self):
        return self._StartStation

    @StartStation.setter
    def StartStation(self, StartStation):
        self._StartStation = StartStation

    @property
    def DestinationStation(self):
        return self._DestinationStation

    @DestinationStation.setter
    def DestinationStation(self, DestinationStation):
        self._DestinationStation = DestinationStation

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def TrainNum(self):
        return self._TrainNum

    @TrainNum.setter
    def TrainNum(self, TrainNum):
        self._TrainNum = TrainNum

    @property
    def Seat(self):
        return self._Seat

    @Seat.setter
    def Seat(self, Seat):
        self._Seat = Seat

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def SeatCategory(self):
        return self._SeatCategory

    @SeatCategory.setter
    def SeatCategory(self, SeatCategory):
        self._SeatCategory = SeatCategory

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InvoiceType(self):
        return self._InvoiceType

    @InvoiceType.setter
    def InvoiceType(self, InvoiceType):
        self._InvoiceType = InvoiceType

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def AdditionalCost(self):
        return self._AdditionalCost

    @AdditionalCost.setter
    def AdditionalCost(self, AdditionalCost):
        self._AdditionalCost = AdditionalCost

    @property
    def HandlingFee(self):
        return self._HandlingFee

    @HandlingFee.setter
    def HandlingFee(self, HandlingFee):
        self._HandlingFee = HandlingFee

    @property
    def LegalAmount(self):
        return self._LegalAmount

    @LegalAmount.setter
    def LegalAmount(self, LegalAmount):
        self._LegalAmount = LegalAmount

    @property
    def TicketStation(self):
        return self._TicketStation

    @TicketStation.setter
    def TicketStation(self, TicketStation):
        self._TicketStation = TicketStation

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def InvoiceStyle(self):
        return self._InvoiceStyle

    @InvoiceStyle.setter
    def InvoiceStyle(self, InvoiceStyle):
        self._InvoiceStyle = InvoiceStyle

    @property
    def ReceiptNumber(self):
        return self._ReceiptNumber

    @ReceiptNumber.setter
    def ReceiptNumber(self, ReceiptNumber):
        self._ReceiptNumber = ReceiptNumber

    @property
    def IsReceipt(self):
        return self._IsReceipt

    @IsReceipt.setter
    def IsReceipt(self, IsReceipt):
        self._IsReceipt = IsReceipt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TicketNum = params.get("TicketNum")
        self._StartStation = params.get("StartStation")
        self._DestinationStation = params.get("DestinationStation")
        self._Date = params.get("Date")
        self._TrainNum = params.get("TrainNum")
        self._Seat = params.get("Seat")
        self._Name = params.get("Name")
        self._Price = params.get("Price")
        self._SeatCategory = params.get("SeatCategory")
        self._ID = params.get("ID")
        self._InvoiceType = params.get("InvoiceType")
        self._SerialNumber = params.get("SerialNumber")
        self._AdditionalCost = params.get("AdditionalCost")
        self._HandlingFee = params.get("HandlingFee")
        self._LegalAmount = params.get("LegalAmount")
        self._TicketStation = params.get("TicketStation")
        self._OriginalPrice = params.get("OriginalPrice")
        self._InvoiceStyle = params.get("InvoiceStyle")
        self._ReceiptNumber = params.get("ReceiptNumber")
        self._IsReceipt = params.get("IsReceipt")
        self._RequestId = params.get("RequestId")


class UsedCarPurchaseInvoice(AbstractModel):
    """二手车销售统一发票

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _QRCodeMark: 是否存在二维码（0：没有，1：有）
        :type QRCodeMark: int
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Date: 开票日期
        :type Date: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Seller: 销货单位名称
        :type Seller: str
        :param _SellerTel: 销售方电话
        :type SellerTel: str
        :param _SellerTaxID: 销售方单位代码/个人身份证号
        :type SellerTaxID: str
        :param _SellerAddress: 销售方地址
        :type SellerAddress: str
        :param _Buyer: 购买方名称
        :type Buyer: str
        :param _BuyerID: 购买方单位代码/个人身份证号
        :type BuyerID: str
        :param _BuyerAddress: 购买方地址
        :type BuyerAddress: str
        :param _BuyerTel: 购买方电话
        :type BuyerTel: str
        :param _CompanyName: 二手车市场
        :type CompanyName: str
        :param _CompanyTaxID: 二手车市场纳税人识别号
        :type CompanyTaxID: str
        :param _CompanyBankAccount: 二手车市场开户银行和账号
        :type CompanyBankAccount: str
        :param _CompanyTel: 二手车市场电话
        :type CompanyTel: str
        :param _CompanyAddress: 二手车市场地址
        :type CompanyAddress: str
        :param _TransferAdministrationName: 转入地车辆管理所名称
        :type TransferAdministrationName: str
        :param _LicensePlate: 车牌号
        :type LicensePlate: str
        :param _RegistrationNumber: 登记证号
        :type RegistrationNumber: str
        :param _VIN: 车辆识别代码
        :type VIN: str
        :param _VehicleModel: 厂牌型号
        :type VehicleModel: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _VehicleType: 车辆类型
        :type VehicleType: str
        :param _Remark: 备注
        :type Remark: str
        :param _FormType: 发票联次
        :type FormType: str
        :param _FormName: 发票联名
        :type FormName: str
        :param _CompanySealMark: 是否有公司印章（0：没有，1：有）
        :type CompanySealMark: int
        """
        self._Title = None
        self._QRCodeMark = None
        self._Code = None
        self._Number = None
        self._Date = None
        self._Total = None
        self._TotalCn = None
        self._Seller = None
        self._SellerTel = None
        self._SellerTaxID = None
        self._SellerAddress = None
        self._Buyer = None
        self._BuyerID = None
        self._BuyerAddress = None
        self._BuyerTel = None
        self._CompanyName = None
        self._CompanyTaxID = None
        self._CompanyBankAccount = None
        self._CompanyTel = None
        self._CompanyAddress = None
        self._TransferAdministrationName = None
        self._LicensePlate = None
        self._RegistrationNumber = None
        self._VIN = None
        self._VehicleModel = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._VehicleType = None
        self._Remark = None
        self._FormType = None
        self._FormName = None
        self._CompanySealMark = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTel(self):
        return self._SellerTel

    @SellerTel.setter
    def SellerTel(self, SellerTel):
        self._SellerTel = SellerTel

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerAddress(self):
        return self._SellerAddress

    @SellerAddress.setter
    def SellerAddress(self, SellerAddress):
        self._SellerAddress = SellerAddress

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerID(self):
        return self._BuyerID

    @BuyerID.setter
    def BuyerID(self, BuyerID):
        self._BuyerID = BuyerID

    @property
    def BuyerAddress(self):
        return self._BuyerAddress

    @BuyerAddress.setter
    def BuyerAddress(self, BuyerAddress):
        self._BuyerAddress = BuyerAddress

    @property
    def BuyerTel(self):
        return self._BuyerTel

    @BuyerTel.setter
    def BuyerTel(self, BuyerTel):
        self._BuyerTel = BuyerTel

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def CompanyTaxID(self):
        return self._CompanyTaxID

    @CompanyTaxID.setter
    def CompanyTaxID(self, CompanyTaxID):
        self._CompanyTaxID = CompanyTaxID

    @property
    def CompanyBankAccount(self):
        return self._CompanyBankAccount

    @CompanyBankAccount.setter
    def CompanyBankAccount(self, CompanyBankAccount):
        self._CompanyBankAccount = CompanyBankAccount

    @property
    def CompanyTel(self):
        return self._CompanyTel

    @CompanyTel.setter
    def CompanyTel(self, CompanyTel):
        self._CompanyTel = CompanyTel

    @property
    def CompanyAddress(self):
        return self._CompanyAddress

    @CompanyAddress.setter
    def CompanyAddress(self, CompanyAddress):
        self._CompanyAddress = CompanyAddress

    @property
    def TransferAdministrationName(self):
        return self._TransferAdministrationName

    @TransferAdministrationName.setter
    def TransferAdministrationName(self, TransferAdministrationName):
        self._TransferAdministrationName = TransferAdministrationName

    @property
    def LicensePlate(self):
        return self._LicensePlate

    @LicensePlate.setter
    def LicensePlate(self, LicensePlate):
        self._LicensePlate = LicensePlate

    @property
    def RegistrationNumber(self):
        return self._RegistrationNumber

    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        self._RegistrationNumber = RegistrationNumber

    @property
    def VIN(self):
        return self._VIN

    @VIN.setter
    def VIN(self, VIN):
        self._VIN = VIN

    @property
    def VehicleModel(self):
        return self._VehicleModel

    @VehicleModel.setter
    def VehicleModel(self, VehicleModel):
        self._VehicleModel = VehicleModel

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FormType(self):
        return self._FormType

    @FormType.setter
    def FormType(self, FormType):
        self._FormType = FormType

    @property
    def FormName(self):
        return self._FormName

    @FormName.setter
    def FormName(self, FormName):
        self._FormName = FormName

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._QRCodeMark = params.get("QRCodeMark")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Seller = params.get("Seller")
        self._SellerTel = params.get("SellerTel")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerAddress = params.get("SellerAddress")
        self._Buyer = params.get("Buyer")
        self._BuyerID = params.get("BuyerID")
        self._BuyerAddress = params.get("BuyerAddress")
        self._BuyerTel = params.get("BuyerTel")
        self._CompanyName = params.get("CompanyName")
        self._CompanyTaxID = params.get("CompanyTaxID")
        self._CompanyBankAccount = params.get("CompanyBankAccount")
        self._CompanyTel = params.get("CompanyTel")
        self._CompanyAddress = params.get("CompanyAddress")
        self._TransferAdministrationName = params.get("TransferAdministrationName")
        self._LicensePlate = params.get("LicensePlate")
        self._RegistrationNumber = params.get("RegistrationNumber")
        self._VIN = params.get("VIN")
        self._VehicleModel = params.get("VehicleModel")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._VehicleType = params.get("VehicleType")
        self._Remark = params.get("Remark")
        self._FormType = params.get("FormType")
        self._FormName = params.get("FormName")
        self._CompanySealMark = params.get("CompanySealMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsedVehicleInvoiceInfo(AbstractModel):
    """二手车销售统一发票信息

    """

    def __init__(self):
        r"""
        :param _TaxBureau: 所属税局
        :type TaxBureau: str
        :param _Buyer: 买方单位/个人
        :type Buyer: str
        :param _BuyerNo: 买方单位代码/身份证号码
        :type BuyerNo: str
        :param _BuyerAddress: 买方单位/个人地址
        :type BuyerAddress: str
        :param _BuyerTel: 买方单位电话
        :type BuyerTel: str
        :param _Seller: 卖方单位/个人
        :type Seller: str
        :param _SellerNo: 卖方单位代码/身份证号码
        :type SellerNo: str
        :param _SellerAddress: 卖方单位/个人地址
        :type SellerAddress: str
        :param _SellerTel: 卖方单位电话
        :type SellerTel: str
        :param _VehicleLicenseNo: 车牌照号
        :type VehicleLicenseNo: str
        :param _RegisterNo: 登记证号
        :type RegisterNo: str
        :param _VehicleIdentifyNo: 车架号/车辆识别代码
        :type VehicleIdentifyNo: str
        :param _ManagementOffice: 转入地车辆管理所名称
        :type ManagementOffice: str
        :param _VehicleTotalPrice: 车价合计
        :type VehicleTotalPrice: str
        :param _Auctioneer: 经营、拍卖单位
        :type Auctioneer: str
        :param _AuctioneerAddress: 经营、拍卖单位地址
        :type AuctioneerAddress: str
        :param _AuctioneerTaxpayerNum: 经营、拍卖单位纳税人识别号
        :type AuctioneerTaxpayerNum: str
        :param _AuctioneerBankAccount: 经营、拍卖单位开户银行、账号
        :type AuctioneerBankAccount: str
        :param _AuctioneerTel: 经营、拍卖单位电话
        :type AuctioneerTel: str
        :param _Market: 二手车市场
        :type Market: str
        :param _MarketTaxpayerNum: 二手车市场纳税人识别号
        :type MarketTaxpayerNum: str
        :param _MarketAddress: 二手车市场地址
        :type MarketAddress: str
        :param _MarketBankAccount: 二手车市场开户银行账号
        :type MarketBankAccount: str
        :param _MarketTel: 二手车市场电话
        :type MarketTel: str
        """
        self._TaxBureau = None
        self._Buyer = None
        self._BuyerNo = None
        self._BuyerAddress = None
        self._BuyerTel = None
        self._Seller = None
        self._SellerNo = None
        self._SellerAddress = None
        self._SellerTel = None
        self._VehicleLicenseNo = None
        self._RegisterNo = None
        self._VehicleIdentifyNo = None
        self._ManagementOffice = None
        self._VehicleTotalPrice = None
        self._Auctioneer = None
        self._AuctioneerAddress = None
        self._AuctioneerTaxpayerNum = None
        self._AuctioneerBankAccount = None
        self._AuctioneerTel = None
        self._Market = None
        self._MarketTaxpayerNum = None
        self._MarketAddress = None
        self._MarketBankAccount = None
        self._MarketTel = None

    @property
    def TaxBureau(self):
        return self._TaxBureau

    @TaxBureau.setter
    def TaxBureau(self, TaxBureau):
        self._TaxBureau = TaxBureau

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerNo(self):
        return self._BuyerNo

    @BuyerNo.setter
    def BuyerNo(self, BuyerNo):
        self._BuyerNo = BuyerNo

    @property
    def BuyerAddress(self):
        return self._BuyerAddress

    @BuyerAddress.setter
    def BuyerAddress(self, BuyerAddress):
        self._BuyerAddress = BuyerAddress

    @property
    def BuyerTel(self):
        return self._BuyerTel

    @BuyerTel.setter
    def BuyerTel(self, BuyerTel):
        self._BuyerTel = BuyerTel

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerNo(self):
        return self._SellerNo

    @SellerNo.setter
    def SellerNo(self, SellerNo):
        self._SellerNo = SellerNo

    @property
    def SellerAddress(self):
        return self._SellerAddress

    @SellerAddress.setter
    def SellerAddress(self, SellerAddress):
        self._SellerAddress = SellerAddress

    @property
    def SellerTel(self):
        return self._SellerTel

    @SellerTel.setter
    def SellerTel(self, SellerTel):
        self._SellerTel = SellerTel

    @property
    def VehicleLicenseNo(self):
        return self._VehicleLicenseNo

    @VehicleLicenseNo.setter
    def VehicleLicenseNo(self, VehicleLicenseNo):
        self._VehicleLicenseNo = VehicleLicenseNo

    @property
    def RegisterNo(self):
        return self._RegisterNo

    @RegisterNo.setter
    def RegisterNo(self, RegisterNo):
        self._RegisterNo = RegisterNo

    @property
    def VehicleIdentifyNo(self):
        return self._VehicleIdentifyNo

    @VehicleIdentifyNo.setter
    def VehicleIdentifyNo(self, VehicleIdentifyNo):
        self._VehicleIdentifyNo = VehicleIdentifyNo

    @property
    def ManagementOffice(self):
        return self._ManagementOffice

    @ManagementOffice.setter
    def ManagementOffice(self, ManagementOffice):
        self._ManagementOffice = ManagementOffice

    @property
    def VehicleTotalPrice(self):
        return self._VehicleTotalPrice

    @VehicleTotalPrice.setter
    def VehicleTotalPrice(self, VehicleTotalPrice):
        self._VehicleTotalPrice = VehicleTotalPrice

    @property
    def Auctioneer(self):
        return self._Auctioneer

    @Auctioneer.setter
    def Auctioneer(self, Auctioneer):
        self._Auctioneer = Auctioneer

    @property
    def AuctioneerAddress(self):
        return self._AuctioneerAddress

    @AuctioneerAddress.setter
    def AuctioneerAddress(self, AuctioneerAddress):
        self._AuctioneerAddress = AuctioneerAddress

    @property
    def AuctioneerTaxpayerNum(self):
        return self._AuctioneerTaxpayerNum

    @AuctioneerTaxpayerNum.setter
    def AuctioneerTaxpayerNum(self, AuctioneerTaxpayerNum):
        self._AuctioneerTaxpayerNum = AuctioneerTaxpayerNum

    @property
    def AuctioneerBankAccount(self):
        return self._AuctioneerBankAccount

    @AuctioneerBankAccount.setter
    def AuctioneerBankAccount(self, AuctioneerBankAccount):
        self._AuctioneerBankAccount = AuctioneerBankAccount

    @property
    def AuctioneerTel(self):
        return self._AuctioneerTel

    @AuctioneerTel.setter
    def AuctioneerTel(self, AuctioneerTel):
        self._AuctioneerTel = AuctioneerTel

    @property
    def Market(self):
        return self._Market

    @Market.setter
    def Market(self, Market):
        self._Market = Market

    @property
    def MarketTaxpayerNum(self):
        return self._MarketTaxpayerNum

    @MarketTaxpayerNum.setter
    def MarketTaxpayerNum(self, MarketTaxpayerNum):
        self._MarketTaxpayerNum = MarketTaxpayerNum

    @property
    def MarketAddress(self):
        return self._MarketAddress

    @MarketAddress.setter
    def MarketAddress(self, MarketAddress):
        self._MarketAddress = MarketAddress

    @property
    def MarketBankAccount(self):
        return self._MarketBankAccount

    @MarketBankAccount.setter
    def MarketBankAccount(self, MarketBankAccount):
        self._MarketBankAccount = MarketBankAccount

    @property
    def MarketTel(self):
        return self._MarketTel

    @MarketTel.setter
    def MarketTel(self, MarketTel):
        self._MarketTel = MarketTel


    def _deserialize(self, params):
        self._TaxBureau = params.get("TaxBureau")
        self._Buyer = params.get("Buyer")
        self._BuyerNo = params.get("BuyerNo")
        self._BuyerAddress = params.get("BuyerAddress")
        self._BuyerTel = params.get("BuyerTel")
        self._Seller = params.get("Seller")
        self._SellerNo = params.get("SellerNo")
        self._SellerAddress = params.get("SellerAddress")
        self._SellerTel = params.get("SellerTel")
        self._VehicleLicenseNo = params.get("VehicleLicenseNo")
        self._RegisterNo = params.get("RegisterNo")
        self._VehicleIdentifyNo = params.get("VehicleIdentifyNo")
        self._ManagementOffice = params.get("ManagementOffice")
        self._VehicleTotalPrice = params.get("VehicleTotalPrice")
        self._Auctioneer = params.get("Auctioneer")
        self._AuctioneerAddress = params.get("AuctioneerAddress")
        self._AuctioneerTaxpayerNum = params.get("AuctioneerTaxpayerNum")
        self._AuctioneerBankAccount = params.get("AuctioneerBankAccount")
        self._AuctioneerTel = params.get("AuctioneerTel")
        self._Market = params.get("Market")
        self._MarketTaxpayerNum = params.get("MarketTaxpayerNum")
        self._MarketAddress = params.get("MarketAddress")
        self._MarketBankAccount = params.get("MarketBankAccount")
        self._MarketTel = params.get("MarketTel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Value(AbstractModel):
    """value信息组

    """

    def __init__(self):
        r"""
        :param _AutoContent: 自动识别的字段内容
        :type AutoContent: str
        :param _Coord: 四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self._AutoContent = None
        self._Coord = None

    @property
    def AutoContent(self):
        return self._AutoContent

    @AutoContent.setter
    def AutoContent(self, AutoContent):
        self._AutoContent = AutoContent

    @property
    def Coord(self):
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord


    def _deserialize(self, params):
        self._AutoContent = params.get("AutoContent")
        if params.get("Coord") is not None:
            self._Coord = Polygon()
            self._Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatElectronicInfo(AbstractModel):
    """电子发票返回值

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Number: 发票号码
        :type Number: str
        :param _Date: 开票日期
        :type Date: str
        :param _PretaxAmount: 税前金额
        :type PretaxAmount: str
        :param _Tax: 合计税额
        :type Tax: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Seller: 销售方名称
        :type Seller: str
        :param _SellerTaxID: 销售方纳税人识别号
        :type SellerTaxID: str
        :param _Buyer: 购买方名称
        :type Buyer: str
        :param _BuyerTaxID: 购买方纳税人识别号
        :type BuyerTaxID: str
        :param _Issuer: 开票人
        :type Issuer: str
        :param _Remark: 备注
        :type Remark: str
        :param _SubTotal: 小计金额
        :type SubTotal: str
        :param _SubTax: 小计税额
        :type SubTax: str
        :param _VatElectronicItems: 电子发票详细条目信息
        :type VatElectronicItems: list of VatElectronicItemInfo
        """
        self._Title = None
        self._Number = None
        self._Date = None
        self._PretaxAmount = None
        self._Tax = None
        self._Total = None
        self._TotalCn = None
        self._Seller = None
        self._SellerTaxID = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._Issuer = None
        self._Remark = None
        self._SubTotal = None
        self._SubTax = None
        self._VatElectronicItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SubTotal(self):
        return self._SubTotal

    @SubTotal.setter
    def SubTotal(self, SubTotal):
        self._SubTotal = SubTotal

    @property
    def SubTax(self):
        return self._SubTax

    @SubTax.setter
    def SubTax(self, SubTax):
        self._SubTax = SubTax

    @property
    def VatElectronicItems(self):
        return self._VatElectronicItems

    @VatElectronicItems.setter
    def VatElectronicItems(self, VatElectronicItems):
        self._VatElectronicItems = VatElectronicItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Tax = params.get("Tax")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._Issuer = params.get("Issuer")
        self._Remark = params.get("Remark")
        self._SubTotal = params.get("SubTotal")
        self._SubTax = params.get("SubTax")
        if params.get("VatElectronicItems") is not None:
            self._VatElectronicItems = []
            for item in params.get("VatElectronicItems"):
                obj = VatElectronicItemInfo()
                obj._deserialize(item)
                self._VatElectronicItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatElectronicItemInfo(AbstractModel):
    """电子发票详细条目信息

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
        :type Name: str
        :param _Quantity: 数量
        :type Quantity: str
        :param _Specification: 规格型号
        :type Specification: str
        :param _Price: 单价
        :type Price: str
        :param _Total: 金额
        :type Total: str
        :param _TaxRate: 税率
        :type TaxRate: str
        :param _Tax: 税额
        :type Tax: str
        :param _Unit: 单位
        :type Unit: str
        :param _VehicleType: 运输工具类型
        :type VehicleType: str
        :param _VehicleBrand: 运输工具牌号
        :type VehicleBrand: str
        :param _DeparturePlace: 起始地
        :type DeparturePlace: str
        :param _ArrivalPlace: 到达地
        :type ArrivalPlace: str
        :param _TransportItemsName: 运输货物名称，仅货物运输服务发票返回
        :type TransportItemsName: str
        :param _PlaceOfBuildingService: 建筑服务发生地，仅建筑发票返回
        :type PlaceOfBuildingService: str
        :param _BuildingName: 建筑项目名称，仅建筑发票返回
        :type BuildingName: str
        :param _EstateNumber: 产权证书/不动产权证号，仅不动产经营租赁服务发票返回
        :type EstateNumber: str
        :param _AreaUnit: 面积单位，仅不动产经营租赁服务发票返回
        :type AreaUnit: str
        """
        self._Name = None
        self._Quantity = None
        self._Specification = None
        self._Price = None
        self._Total = None
        self._TaxRate = None
        self._Tax = None
        self._Unit = None
        self._VehicleType = None
        self._VehicleBrand = None
        self._DeparturePlace = None
        self._ArrivalPlace = None
        self._TransportItemsName = None
        self._PlaceOfBuildingService = None
        self._BuildingName = None
        self._EstateNumber = None
        self._AreaUnit = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def VehicleBrand(self):
        return self._VehicleBrand

    @VehicleBrand.setter
    def VehicleBrand(self, VehicleBrand):
        self._VehicleBrand = VehicleBrand

    @property
    def DeparturePlace(self):
        return self._DeparturePlace

    @DeparturePlace.setter
    def DeparturePlace(self, DeparturePlace):
        self._DeparturePlace = DeparturePlace

    @property
    def ArrivalPlace(self):
        return self._ArrivalPlace

    @ArrivalPlace.setter
    def ArrivalPlace(self, ArrivalPlace):
        self._ArrivalPlace = ArrivalPlace

    @property
    def TransportItemsName(self):
        return self._TransportItemsName

    @TransportItemsName.setter
    def TransportItemsName(self, TransportItemsName):
        self._TransportItemsName = TransportItemsName

    @property
    def PlaceOfBuildingService(self):
        return self._PlaceOfBuildingService

    @PlaceOfBuildingService.setter
    def PlaceOfBuildingService(self, PlaceOfBuildingService):
        self._PlaceOfBuildingService = PlaceOfBuildingService

    @property
    def BuildingName(self):
        return self._BuildingName

    @BuildingName.setter
    def BuildingName(self, BuildingName):
        self._BuildingName = BuildingName

    @property
    def EstateNumber(self):
        return self._EstateNumber

    @EstateNumber.setter
    def EstateNumber(self, EstateNumber):
        self._EstateNumber = EstateNumber

    @property
    def AreaUnit(self):
        return self._AreaUnit

    @AreaUnit.setter
    def AreaUnit(self, AreaUnit):
        self._AreaUnit = AreaUnit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Quantity = params.get("Quantity")
        self._Specification = params.get("Specification")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        self._TaxRate = params.get("TaxRate")
        self._Tax = params.get("Tax")
        self._Unit = params.get("Unit")
        self._VehicleType = params.get("VehicleType")
        self._VehicleBrand = params.get("VehicleBrand")
        self._DeparturePlace = params.get("DeparturePlace")
        self._ArrivalPlace = params.get("ArrivalPlace")
        self._TransportItemsName = params.get("TransportItemsName")
        self._PlaceOfBuildingService = params.get("PlaceOfBuildingService")
        self._BuildingName = params.get("BuildingName")
        self._EstateNumber = params.get("EstateNumber")
        self._AreaUnit = params.get("AreaUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoice(AbstractModel):
    """增值税发票信息

    """

    def __init__(self):
        r"""
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _Date: 开票日期
        :type Date: str
        :param _BuyerName: 购方抬头
        :type BuyerName: str
        :param _BuyerTaxCode: 购方税号
        :type BuyerTaxCode: str
        :param _BuyerAddressPhone: 购方地址电话
        :type BuyerAddressPhone: str
        :param _BuyerBankAccount: 购方银行账号
        :type BuyerBankAccount: str
        :param _SellerName: 销方名称
        :type SellerName: str
        :param _SellerTaxCode: 销方税号
        :type SellerTaxCode: str
        :param _SellerAddressPhone: 销方地址电话
        :type SellerAddressPhone: str
        :param _SellerBankAccount: 销方银行账号
        :type SellerBankAccount: str
        :param _Remark: 备注
        :type Remark: str
        :param _MachineNo: 机器编码
        :type MachineNo: str
        :param _Type: 票种类型
01：增值税专用发票，
02：货运运输业增值税专用发票，
03：机动车销售统一发票，
04：增值税普通发票，
08：增值税电子专用发票（含全电，全电仅新版接口支持），
10：增值税电子普通发票（含全电，全电仅新版接口支持），
11：增值税普通发票（卷式），
14：增值税电子（通行费）发票，
15：二手车销售统一发票，
32：深圳区块链发票，
102：通用机打电子发票
        :type Type: str
        :param _CheckCode: 检验码
        :type CheckCode: str
        :param _IsAbandoned: 是否作废（红冲）是否作废（红冲）
Y：已作废，N：未作废，H：红冲，HP：部分红冲，HF：全额红冲
        :type IsAbandoned: str
        :param _HasSellerList: 是否有销货清单 
Y: 有清单 N：无清单 
卷票无
        :type HasSellerList: str
        :param _SellerListTitle: 销货清单标题
        :type SellerListTitle: str
        :param _SellerListTax: 销货清单税额
        :type SellerListTax: str
        :param _AmountWithoutTax: 不含税金额
        :type AmountWithoutTax: str
        :param _TaxAmount: 税额
        :type TaxAmount: str
        :param _AmountWithTax: 含税金额
        :type AmountWithTax: str
        :param _Items: 项目明细
        :type Items: list of VatInvoiceItem
        :param _TaxBureau: 所属税局
        :type TaxBureau: str
        :param _TrafficFreeFlag: 通行费标志:Y、是;N、否
        :type TrafficFreeFlag: str
        """
        self._Code = None
        self._Number = None
        self._Date = None
        self._BuyerName = None
        self._BuyerTaxCode = None
        self._BuyerAddressPhone = None
        self._BuyerBankAccount = None
        self._SellerName = None
        self._SellerTaxCode = None
        self._SellerAddressPhone = None
        self._SellerBankAccount = None
        self._Remark = None
        self._MachineNo = None
        self._Type = None
        self._CheckCode = None
        self._IsAbandoned = None
        self._HasSellerList = None
        self._SellerListTitle = None
        self._SellerListTax = None
        self._AmountWithoutTax = None
        self._TaxAmount = None
        self._AmountWithTax = None
        self._Items = None
        self._TaxBureau = None
        self._TrafficFreeFlag = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def BuyerName(self):
        return self._BuyerName

    @BuyerName.setter
    def BuyerName(self, BuyerName):
        self._BuyerName = BuyerName

    @property
    def BuyerTaxCode(self):
        return self._BuyerTaxCode

    @BuyerTaxCode.setter
    def BuyerTaxCode(self, BuyerTaxCode):
        self._BuyerTaxCode = BuyerTaxCode

    @property
    def BuyerAddressPhone(self):
        return self._BuyerAddressPhone

    @BuyerAddressPhone.setter
    def BuyerAddressPhone(self, BuyerAddressPhone):
        self._BuyerAddressPhone = BuyerAddressPhone

    @property
    def BuyerBankAccount(self):
        return self._BuyerBankAccount

    @BuyerBankAccount.setter
    def BuyerBankAccount(self, BuyerBankAccount):
        self._BuyerBankAccount = BuyerBankAccount

    @property
    def SellerName(self):
        return self._SellerName

    @SellerName.setter
    def SellerName(self, SellerName):
        self._SellerName = SellerName

    @property
    def SellerTaxCode(self):
        return self._SellerTaxCode

    @SellerTaxCode.setter
    def SellerTaxCode(self, SellerTaxCode):
        self._SellerTaxCode = SellerTaxCode

    @property
    def SellerAddressPhone(self):
        return self._SellerAddressPhone

    @SellerAddressPhone.setter
    def SellerAddressPhone(self, SellerAddressPhone):
        self._SellerAddressPhone = SellerAddressPhone

    @property
    def SellerBankAccount(self):
        return self._SellerBankAccount

    @SellerBankAccount.setter
    def SellerBankAccount(self, SellerBankAccount):
        self._SellerBankAccount = SellerBankAccount

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MachineNo(self):
        return self._MachineNo

    @MachineNo.setter
    def MachineNo(self, MachineNo):
        self._MachineNo = MachineNo

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def IsAbandoned(self):
        return self._IsAbandoned

    @IsAbandoned.setter
    def IsAbandoned(self, IsAbandoned):
        self._IsAbandoned = IsAbandoned

    @property
    def HasSellerList(self):
        return self._HasSellerList

    @HasSellerList.setter
    def HasSellerList(self, HasSellerList):
        self._HasSellerList = HasSellerList

    @property
    def SellerListTitle(self):
        return self._SellerListTitle

    @SellerListTitle.setter
    def SellerListTitle(self, SellerListTitle):
        self._SellerListTitle = SellerListTitle

    @property
    def SellerListTax(self):
        return self._SellerListTax

    @SellerListTax.setter
    def SellerListTax(self, SellerListTax):
        self._SellerListTax = SellerListTax

    @property
    def AmountWithoutTax(self):
        return self._AmountWithoutTax

    @AmountWithoutTax.setter
    def AmountWithoutTax(self, AmountWithoutTax):
        self._AmountWithoutTax = AmountWithoutTax

    @property
    def TaxAmount(self):
        return self._TaxAmount

    @TaxAmount.setter
    def TaxAmount(self, TaxAmount):
        self._TaxAmount = TaxAmount

    @property
    def AmountWithTax(self):
        return self._AmountWithTax

    @AmountWithTax.setter
    def AmountWithTax(self, AmountWithTax):
        self._AmountWithTax = AmountWithTax

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TaxBureau(self):
        return self._TaxBureau

    @TaxBureau.setter
    def TaxBureau(self, TaxBureau):
        self._TaxBureau = TaxBureau

    @property
    def TrafficFreeFlag(self):
        return self._TrafficFreeFlag

    @TrafficFreeFlag.setter
    def TrafficFreeFlag(self, TrafficFreeFlag):
        self._TrafficFreeFlag = TrafficFreeFlag


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._Date = params.get("Date")
        self._BuyerName = params.get("BuyerName")
        self._BuyerTaxCode = params.get("BuyerTaxCode")
        self._BuyerAddressPhone = params.get("BuyerAddressPhone")
        self._BuyerBankAccount = params.get("BuyerBankAccount")
        self._SellerName = params.get("SellerName")
        self._SellerTaxCode = params.get("SellerTaxCode")
        self._SellerAddressPhone = params.get("SellerAddressPhone")
        self._SellerBankAccount = params.get("SellerBankAccount")
        self._Remark = params.get("Remark")
        self._MachineNo = params.get("MachineNo")
        self._Type = params.get("Type")
        self._CheckCode = params.get("CheckCode")
        self._IsAbandoned = params.get("IsAbandoned")
        self._HasSellerList = params.get("HasSellerList")
        self._SellerListTitle = params.get("SellerListTitle")
        self._SellerListTax = params.get("SellerListTax")
        self._AmountWithoutTax = params.get("AmountWithoutTax")
        self._TaxAmount = params.get("TaxAmount")
        self._AmountWithTax = params.get("AmountWithTax")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = VatInvoiceItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TaxBureau = params.get("TaxBureau")
        self._TrafficFreeFlag = params.get("TrafficFreeFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceGoodsInfo(AbstractModel):
    """发票商品

    """

    def __init__(self):
        r"""
        :param _Item: 项目名称
        :type Item: str
        :param _Specification: 规格型号
        :type Specification: str
        :param _MeasurementDimension: 单位
        :type MeasurementDimension: str
        :param _Price: 价格
        :type Price: str
        :param _Quantity: 数量
        :type Quantity: str
        :param _Amount: 金额
        :type Amount: str
        :param _TaxScheme: 税率(如6%、免税)
        :type TaxScheme: str
        :param _TaxAmount: 税额
        :type TaxAmount: str
        """
        self._Item = None
        self._Specification = None
        self._MeasurementDimension = None
        self._Price = None
        self._Quantity = None
        self._Amount = None
        self._TaxScheme = None
        self._TaxAmount = None

    @property
    def Item(self):
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def MeasurementDimension(self):
        return self._MeasurementDimension

    @MeasurementDimension.setter
    def MeasurementDimension(self, MeasurementDimension):
        self._MeasurementDimension = MeasurementDimension

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def TaxScheme(self):
        return self._TaxScheme

    @TaxScheme.setter
    def TaxScheme(self, TaxScheme):
        self._TaxScheme = TaxScheme

    @property
    def TaxAmount(self):
        return self._TaxAmount

    @TaxAmount.setter
    def TaxAmount(self, TaxAmount):
        self._TaxAmount = TaxAmount


    def _deserialize(self, params):
        self._Item = params.get("Item")
        self._Specification = params.get("Specification")
        self._MeasurementDimension = params.get("MeasurementDimension")
        self._Price = params.get("Price")
        self._Quantity = params.get("Quantity")
        self._Amount = params.get("Amount")
        self._TaxScheme = params.get("TaxScheme")
        self._TaxAmount = params.get("TaxAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceInfo(AbstractModel):
    """增值税发票返回值

    """

    def __init__(self):
        r"""
        :param _CheckCode: 校验码
        :type CheckCode: str
        :param _FormType: 发票联次
        :type FormType: str
        :param _TravelTax: 车船税
        :type TravelTax: str
        :param _BuyerAddrTel: 购买方地址电话
        :type BuyerAddrTel: str
        :param _BuyerBankAccount: 购买方银行账号
        :type BuyerBankAccount: str
        :param _CompanySealContent: 公司印章内容
        :type CompanySealContent: str
        :param _TaxSealContent: 税务局章内容
        :type TaxSealContent: str
        :param _ServiceName: 服务类型
        :type ServiceName: str
        :param _City: 市
        :type City: str
        :param _QRCodeMark: 是否存在二维码（0：没有，1：有）
        :type QRCodeMark: int
        :param _AgentMark: 是否有代开标记（0：没有，1：有）
        :type AgentMark: int
        :param _TransitMark: 是否有通行费标记（0：没有，1：有）
        :type TransitMark: int
        :param _OilMark: 是否有成品油标记（0：没有，1：有）
        :type OilMark: int
        :param _Title: 发票名称
        :type Title: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _NumberConfirm: 机打发票号码
        :type NumberConfirm: str
        :param _Date: 开票日期
        :type Date: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _PretaxAmount: 税前金额
        :type PretaxAmount: str
        :param _Tax: 合计税额
        :type Tax: str
        :param _MachineCode: 机器编号
        :type MachineCode: str
        :param _Ciphertext: 密码区
        :type Ciphertext: str
        :param _Remark: 备注
        :type Remark: str
        :param _Seller: 销售方名称
        :type Seller: str
        :param _SellerTaxID: 销售方纳税人识别号
        :type SellerTaxID: str
        :param _SellerAddrTel: 销售方地址电话
        :type SellerAddrTel: str
        :param _SellerBankAccount: 销售方银行账号
        :type SellerBankAccount: str
        :param _Buyer: 购买方名称
        :type Buyer: str
        :param _BuyerTaxID: 购买方纳税人识别号
        :type BuyerTaxID: str
        :param _CompanySealMark: 是否有公司印章（0：没有，1：有）
        :type CompanySealMark: int
        :param _Issuer: 开票人
        :type Issuer: str
        :param _Reviewer: 复核人
        :type Reviewer: str
        :param _Province: 省
        :type Province: str
        :param _VatInvoiceItemInfos: 增值税发票项目信息
        :type VatInvoiceItemInfos: list of VatInvoiceItemInfo
        :param _CodeConfirm: 机打发票代码
        :type CodeConfirm: str
        :param _Receiptor: 收款人
        :type Receiptor: str
        :param _ElectronicFullMark: 是否有全电纸质票（0：没有，1：有）
        :type ElectronicFullMark: int
        :param _ElectronicFullNumber: 全电号码
        :type ElectronicFullNumber: str
        :param _FormName: 发票联名
        :type FormName: str
        :param _BlockChainMark: 是否有区块链标记（0：没有，1：有）	
        :type BlockChainMark: int
        :param _AcquisitionMark: 是否有收购标记（0：没有，1：有）	
        :type AcquisitionMark: int
        :param _SubTotal: 小计金额
        :type SubTotal: str
        :param _SubTax: 小计税额
        :type SubTax: str
        """
        self._CheckCode = None
        self._FormType = None
        self._TravelTax = None
        self._BuyerAddrTel = None
        self._BuyerBankAccount = None
        self._CompanySealContent = None
        self._TaxSealContent = None
        self._ServiceName = None
        self._City = None
        self._QRCodeMark = None
        self._AgentMark = None
        self._TransitMark = None
        self._OilMark = None
        self._Title = None
        self._Kind = None
        self._Code = None
        self._Number = None
        self._NumberConfirm = None
        self._Date = None
        self._Total = None
        self._TotalCn = None
        self._PretaxAmount = None
        self._Tax = None
        self._MachineCode = None
        self._Ciphertext = None
        self._Remark = None
        self._Seller = None
        self._SellerTaxID = None
        self._SellerAddrTel = None
        self._SellerBankAccount = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._CompanySealMark = None
        self._Issuer = None
        self._Reviewer = None
        self._Province = None
        self._VatInvoiceItemInfos = None
        self._CodeConfirm = None
        self._Receiptor = None
        self._ElectronicFullMark = None
        self._ElectronicFullNumber = None
        self._FormName = None
        self._BlockChainMark = None
        self._AcquisitionMark = None
        self._SubTotal = None
        self._SubTax = None

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def FormType(self):
        return self._FormType

    @FormType.setter
    def FormType(self, FormType):
        self._FormType = FormType

    @property
    def TravelTax(self):
        return self._TravelTax

    @TravelTax.setter
    def TravelTax(self, TravelTax):
        self._TravelTax = TravelTax

    @property
    def BuyerAddrTel(self):
        return self._BuyerAddrTel

    @BuyerAddrTel.setter
    def BuyerAddrTel(self, BuyerAddrTel):
        self._BuyerAddrTel = BuyerAddrTel

    @property
    def BuyerBankAccount(self):
        return self._BuyerBankAccount

    @BuyerBankAccount.setter
    def BuyerBankAccount(self, BuyerBankAccount):
        self._BuyerBankAccount = BuyerBankAccount

    @property
    def CompanySealContent(self):
        return self._CompanySealContent

    @CompanySealContent.setter
    def CompanySealContent(self, CompanySealContent):
        self._CompanySealContent = CompanySealContent

    @property
    def TaxSealContent(self):
        return self._TaxSealContent

    @TaxSealContent.setter
    def TaxSealContent(self, TaxSealContent):
        self._TaxSealContent = TaxSealContent

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def AgentMark(self):
        return self._AgentMark

    @AgentMark.setter
    def AgentMark(self, AgentMark):
        self._AgentMark = AgentMark

    @property
    def TransitMark(self):
        return self._TransitMark

    @TransitMark.setter
    def TransitMark(self, TransitMark):
        self._TransitMark = TransitMark

    @property
    def OilMark(self):
        return self._OilMark

    @OilMark.setter
    def OilMark(self, OilMark):
        self._OilMark = OilMark

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def NumberConfirm(self):
        return self._NumberConfirm

    @NumberConfirm.setter
    def NumberConfirm(self, NumberConfirm):
        self._NumberConfirm = NumberConfirm

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def PretaxAmount(self):
        return self._PretaxAmount

    @PretaxAmount.setter
    def PretaxAmount(self, PretaxAmount):
        self._PretaxAmount = PretaxAmount

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def MachineCode(self):
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def SellerAddrTel(self):
        return self._SellerAddrTel

    @SellerAddrTel.setter
    def SellerAddrTel(self, SellerAddrTel):
        self._SellerAddrTel = SellerAddrTel

    @property
    def SellerBankAccount(self):
        return self._SellerBankAccount

    @SellerBankAccount.setter
    def SellerBankAccount(self, SellerBankAccount):
        self._SellerBankAccount = SellerBankAccount

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def VatInvoiceItemInfos(self):
        return self._VatInvoiceItemInfos

    @VatInvoiceItemInfos.setter
    def VatInvoiceItemInfos(self, VatInvoiceItemInfos):
        self._VatInvoiceItemInfos = VatInvoiceItemInfos

    @property
    def CodeConfirm(self):
        return self._CodeConfirm

    @CodeConfirm.setter
    def CodeConfirm(self, CodeConfirm):
        self._CodeConfirm = CodeConfirm

    @property
    def Receiptor(self):
        return self._Receiptor

    @Receiptor.setter
    def Receiptor(self, Receiptor):
        self._Receiptor = Receiptor

    @property
    def ElectronicFullMark(self):
        return self._ElectronicFullMark

    @ElectronicFullMark.setter
    def ElectronicFullMark(self, ElectronicFullMark):
        self._ElectronicFullMark = ElectronicFullMark

    @property
    def ElectronicFullNumber(self):
        return self._ElectronicFullNumber

    @ElectronicFullNumber.setter
    def ElectronicFullNumber(self, ElectronicFullNumber):
        self._ElectronicFullNumber = ElectronicFullNumber

    @property
    def FormName(self):
        return self._FormName

    @FormName.setter
    def FormName(self, FormName):
        self._FormName = FormName

    @property
    def BlockChainMark(self):
        return self._BlockChainMark

    @BlockChainMark.setter
    def BlockChainMark(self, BlockChainMark):
        self._BlockChainMark = BlockChainMark

    @property
    def AcquisitionMark(self):
        return self._AcquisitionMark

    @AcquisitionMark.setter
    def AcquisitionMark(self, AcquisitionMark):
        self._AcquisitionMark = AcquisitionMark

    @property
    def SubTotal(self):
        return self._SubTotal

    @SubTotal.setter
    def SubTotal(self, SubTotal):
        self._SubTotal = SubTotal

    @property
    def SubTax(self):
        return self._SubTax

    @SubTax.setter
    def SubTax(self, SubTax):
        self._SubTax = SubTax


    def _deserialize(self, params):
        self._CheckCode = params.get("CheckCode")
        self._FormType = params.get("FormType")
        self._TravelTax = params.get("TravelTax")
        self._BuyerAddrTel = params.get("BuyerAddrTel")
        self._BuyerBankAccount = params.get("BuyerBankAccount")
        self._CompanySealContent = params.get("CompanySealContent")
        self._TaxSealContent = params.get("TaxSealContent")
        self._ServiceName = params.get("ServiceName")
        self._City = params.get("City")
        self._QRCodeMark = params.get("QRCodeMark")
        self._AgentMark = params.get("AgentMark")
        self._TransitMark = params.get("TransitMark")
        self._OilMark = params.get("OilMark")
        self._Title = params.get("Title")
        self._Kind = params.get("Kind")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._NumberConfirm = params.get("NumberConfirm")
        self._Date = params.get("Date")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._PretaxAmount = params.get("PretaxAmount")
        self._Tax = params.get("Tax")
        self._MachineCode = params.get("MachineCode")
        self._Ciphertext = params.get("Ciphertext")
        self._Remark = params.get("Remark")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._SellerAddrTel = params.get("SellerAddrTel")
        self._SellerBankAccount = params.get("SellerBankAccount")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._CompanySealMark = params.get("CompanySealMark")
        self._Issuer = params.get("Issuer")
        self._Reviewer = params.get("Reviewer")
        self._Province = params.get("Province")
        if params.get("VatInvoiceItemInfos") is not None:
            self._VatInvoiceItemInfos = []
            for item in params.get("VatInvoiceItemInfos"):
                obj = VatInvoiceItemInfo()
                obj._deserialize(item)
                self._VatInvoiceItemInfos.append(obj)
        self._CodeConfirm = params.get("CodeConfirm")
        self._Receiptor = params.get("Receiptor")
        self._ElectronicFullMark = params.get("ElectronicFullMark")
        self._ElectronicFullNumber = params.get("ElectronicFullNumber")
        self._FormName = params.get("FormName")
        self._BlockChainMark = params.get("BlockChainMark")
        self._AcquisitionMark = params.get("AcquisitionMark")
        self._SubTotal = params.get("SubTotal")
        self._SubTax = params.get("SubTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceItem(AbstractModel):
    """增值税发票项目明细

    """

    def __init__(self):
        r"""
        :param _LineNo: 行号
        :type LineNo: str
        :param _Name: 名称
        :type Name: str
        :param _Spec: 规格
        :type Spec: str
        :param _Unit: 单位
        :type Unit: str
        :param _Quantity: 数量
        :type Quantity: str
        :param _UnitPrice: 单价
        :type UnitPrice: str
        :param _AmountWithoutTax: 不含税金额
        :type AmountWithoutTax: str
        :param _TaxRate: 税率
        :type TaxRate: str
        :param _TaxAmount: 税额
        :type TaxAmount: str
        :param _TaxClassifyCode: 税收分类编码
        :type TaxClassifyCode: str
        :param _VehicleType: 运输工具类型
        :type VehicleType: str
        :param _VehicleBrand: 运输工具牌号
        :type VehicleBrand: str
        :param _DeparturePlace: 起始地
        :type DeparturePlace: str
        :param _ArrivalPlace: 到达地
        :type ArrivalPlace: str
        :param _TransportItemsName: 运输货物名称
        :type TransportItemsName: str
        :param _ConstructionPlace: 建筑服务发生地
        :type ConstructionPlace: str
        :param _ConstructionName: 建筑项目名称
        :type ConstructionName: str
        """
        self._LineNo = None
        self._Name = None
        self._Spec = None
        self._Unit = None
        self._Quantity = None
        self._UnitPrice = None
        self._AmountWithoutTax = None
        self._TaxRate = None
        self._TaxAmount = None
        self._TaxClassifyCode = None
        self._VehicleType = None
        self._VehicleBrand = None
        self._DeparturePlace = None
        self._ArrivalPlace = None
        self._TransportItemsName = None
        self._ConstructionPlace = None
        self._ConstructionName = None

    @property
    def LineNo(self):
        return self._LineNo

    @LineNo.setter
    def LineNo(self, LineNo):
        self._LineNo = LineNo

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def AmountWithoutTax(self):
        return self._AmountWithoutTax

    @AmountWithoutTax.setter
    def AmountWithoutTax(self, AmountWithoutTax):
        self._AmountWithoutTax = AmountWithoutTax

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def TaxAmount(self):
        return self._TaxAmount

    @TaxAmount.setter
    def TaxAmount(self, TaxAmount):
        self._TaxAmount = TaxAmount

    @property
    def TaxClassifyCode(self):
        return self._TaxClassifyCode

    @TaxClassifyCode.setter
    def TaxClassifyCode(self, TaxClassifyCode):
        self._TaxClassifyCode = TaxClassifyCode

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def VehicleBrand(self):
        return self._VehicleBrand

    @VehicleBrand.setter
    def VehicleBrand(self, VehicleBrand):
        self._VehicleBrand = VehicleBrand

    @property
    def DeparturePlace(self):
        return self._DeparturePlace

    @DeparturePlace.setter
    def DeparturePlace(self, DeparturePlace):
        self._DeparturePlace = DeparturePlace

    @property
    def ArrivalPlace(self):
        return self._ArrivalPlace

    @ArrivalPlace.setter
    def ArrivalPlace(self, ArrivalPlace):
        self._ArrivalPlace = ArrivalPlace

    @property
    def TransportItemsName(self):
        return self._TransportItemsName

    @TransportItemsName.setter
    def TransportItemsName(self, TransportItemsName):
        self._TransportItemsName = TransportItemsName

    @property
    def ConstructionPlace(self):
        return self._ConstructionPlace

    @ConstructionPlace.setter
    def ConstructionPlace(self, ConstructionPlace):
        self._ConstructionPlace = ConstructionPlace

    @property
    def ConstructionName(self):
        return self._ConstructionName

    @ConstructionName.setter
    def ConstructionName(self, ConstructionName):
        self._ConstructionName = ConstructionName


    def _deserialize(self, params):
        self._LineNo = params.get("LineNo")
        self._Name = params.get("Name")
        self._Spec = params.get("Spec")
        self._Unit = params.get("Unit")
        self._Quantity = params.get("Quantity")
        self._UnitPrice = params.get("UnitPrice")
        self._AmountWithoutTax = params.get("AmountWithoutTax")
        self._TaxRate = params.get("TaxRate")
        self._TaxAmount = params.get("TaxAmount")
        self._TaxClassifyCode = params.get("TaxClassifyCode")
        self._VehicleType = params.get("VehicleType")
        self._VehicleBrand = params.get("VehicleBrand")
        self._DeparturePlace = params.get("DeparturePlace")
        self._ArrivalPlace = params.get("ArrivalPlace")
        self._TransportItemsName = params.get("TransportItemsName")
        self._ConstructionPlace = params.get("ConstructionPlace")
        self._ConstructionName = params.get("ConstructionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceItemInfo(AbstractModel):
    """增值税发票项目信息

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
        :type Name: str
        :param _Specification: 规格型号
        :type Specification: str
        :param _Unit: 单位
        :type Unit: str
        :param _Quantity: 数量
        :type Quantity: str
        :param _Price: 单价
        :type Price: str
        :param _Total: 金额
        :type Total: str
        :param _TaxRate: 税率
        :type TaxRate: str
        :param _Tax: 税额
        :type Tax: str
        :param _DateStart: 通行日期起
        :type DateStart: str
        :param _DateEnd: 通行日期止
        :type DateEnd: str
        :param _LicensePlate: 车牌号
        :type LicensePlate: str
        :param _VehicleType: 车辆类型
        :type VehicleType: str
        :param _SerialNumber: 序号
        :type SerialNumber: str
        """
        self._Name = None
        self._Specification = None
        self._Unit = None
        self._Quantity = None
        self._Price = None
        self._Total = None
        self._TaxRate = None
        self._Tax = None
        self._DateStart = None
        self._DateEnd = None
        self._LicensePlate = None
        self._VehicleType = None
        self._SerialNumber = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaxRate(self):
        return self._TaxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    @property
    def Tax(self):
        return self._Tax

    @Tax.setter
    def Tax(self, Tax):
        self._Tax = Tax

    @property
    def DateStart(self):
        return self._DateStart

    @DateStart.setter
    def DateStart(self, DateStart):
        self._DateStart = DateStart

    @property
    def DateEnd(self):
        return self._DateEnd

    @DateEnd.setter
    def DateEnd(self, DateEnd):
        self._DateEnd = DateEnd

    @property
    def LicensePlate(self):
        return self._LicensePlate

    @LicensePlate.setter
    def LicensePlate(self, LicensePlate):
        self._LicensePlate = LicensePlate

    @property
    def VehicleType(self):
        return self._VehicleType

    @VehicleType.setter
    def VehicleType(self, VehicleType):
        self._VehicleType = VehicleType

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Specification = params.get("Specification")
        self._Unit = params.get("Unit")
        self._Quantity = params.get("Quantity")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        self._TaxRate = params.get("TaxRate")
        self._Tax = params.get("Tax")
        self._DateStart = params.get("DateStart")
        self._DateEnd = params.get("DateEnd")
        self._LicensePlate = params.get("LicensePlate")
        self._VehicleType = params.get("VehicleType")
        self._SerialNumber = params.get("SerialNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceOCRRequest(AbstractModel):
    """VatInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片/PDF的 Base64 值。
支持的文件格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片/PDF大小：所下载文件经Base64编码后不超过 7M。文件下载时间不超过 3 秒。
支持的图片像素：需介于20-10000px之间。
输入参数 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片/PDF的 Url 地址。
支持的文件格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。
支持的图片/PDF大小：所下载文件经 Base64 编码后不超过 7M。文件下载时间不超过 3 秒。
支持的图片像素：需介于20-10000px之间。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为false，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceOCRResponse(AbstractModel):
    """VatInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VatInvoiceInfos: 检测到的文本信息，具体内容请点击左侧链接。
        :type VatInvoiceInfos: list of TextVatInvoice
        :param _Items: 明细条目。VatInvoiceInfos中关于明细项的具体条目。
        :type Items: list of VatInvoiceItem
        :param _PdfPageSize: 默认值为0。如果图片为PDF时，返回PDF的总页数。
        :type PdfPageSize: int
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。点击查看<a href="https://cloud.tencent.com/document/product/866/45139">如何纠正倾斜文本</a>
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VatInvoiceInfos = None
        self._Items = None
        self._PdfPageSize = None
        self._Angle = None
        self._RequestId = None

    @property
    def VatInvoiceInfos(self):
        return self._VatInvoiceInfos

    @VatInvoiceInfos.setter
    def VatInvoiceInfos(self, VatInvoiceInfos):
        self._VatInvoiceInfos = VatInvoiceInfos

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PdfPageSize(self):
        return self._PdfPageSize

    @PdfPageSize.setter
    def PdfPageSize(self, PdfPageSize):
        self._PdfPageSize = PdfPageSize

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VatInvoiceInfos") is not None:
            self._VatInvoiceInfos = []
            for item in params.get("VatInvoiceInfos"):
                obj = TextVatInvoice()
                obj._deserialize(item)
                self._VatInvoiceInfos.append(obj)
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = VatInvoiceItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PdfPageSize = params.get("PdfPageSize")
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class VatInvoiceRoll(AbstractModel):
    """增值税普通发票(卷票)

    """

    def __init__(self):
        r"""
        :param _Title: 发票名称
        :type Title: str
        :param _Code: 发票代码
        :type Code: str
        :param _Number: 发票号码
        :type Number: str
        :param _NumberConfirm: 机打发票号码
        :type NumberConfirm: str
        :param _Date: 开票日期
        :type Date: str
        :param _CheckCode: 校验码
        :type CheckCode: str
        :param _Seller: 销售方名称
        :type Seller: str
        :param _SellerTaxID: 销售方纳税人识别号
        :type SellerTaxID: str
        :param _Buyer: 购买方名称
        :type Buyer: str
        :param _BuyerTaxID: 购买方纳税人识别号
        :type BuyerTaxID: str
        :param _Category: 种类
        :type Category: str
        :param _Total: 价税合计（小写）
        :type Total: str
        :param _TotalCn: 价税合计（大写）
        :type TotalCn: str
        :param _Kind: 发票消费类型
        :type Kind: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _CompanySealMark: 是否有公司印章（0：没有，1：有）
        :type CompanySealMark: int
        :param _QRCodeMark: 是否存在二维码（1：有，0：无）
        :type QRCodeMark: int
        :param _ServiceName: 服务类型
        :type ServiceName: str
        :param _CompanySealContent: 公司印章内容
        :type CompanySealContent: str
        :param _TaxSealContent: 税务局章内容
        :type TaxSealContent: str
        :param _VatRollItems: 条目
        :type VatRollItems: list of VatRollItem
        """
        self._Title = None
        self._Code = None
        self._Number = None
        self._NumberConfirm = None
        self._Date = None
        self._CheckCode = None
        self._Seller = None
        self._SellerTaxID = None
        self._Buyer = None
        self._BuyerTaxID = None
        self._Category = None
        self._Total = None
        self._TotalCn = None
        self._Kind = None
        self._Province = None
        self._City = None
        self._CompanySealMark = None
        self._QRCodeMark = None
        self._ServiceName = None
        self._CompanySealContent = None
        self._TaxSealContent = None
        self._VatRollItems = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def NumberConfirm(self):
        return self._NumberConfirm

    @NumberConfirm.setter
    def NumberConfirm(self, NumberConfirm):
        self._NumberConfirm = NumberConfirm

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def SellerTaxID(self):
        return self._SellerTaxID

    @SellerTaxID.setter
    def SellerTaxID(self, SellerTaxID):
        self._SellerTaxID = SellerTaxID

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def BuyerTaxID(self):
        return self._BuyerTaxID

    @BuyerTaxID.setter
    def BuyerTaxID(self, BuyerTaxID):
        self._BuyerTaxID = BuyerTaxID

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalCn(self):
        return self._TotalCn

    @TotalCn.setter
    def TotalCn(self, TotalCn):
        self._TotalCn = TotalCn

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def CompanySealMark(self):
        return self._CompanySealMark

    @CompanySealMark.setter
    def CompanySealMark(self, CompanySealMark):
        self._CompanySealMark = CompanySealMark

    @property
    def QRCodeMark(self):
        return self._QRCodeMark

    @QRCodeMark.setter
    def QRCodeMark(self, QRCodeMark):
        self._QRCodeMark = QRCodeMark

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def CompanySealContent(self):
        return self._CompanySealContent

    @CompanySealContent.setter
    def CompanySealContent(self, CompanySealContent):
        self._CompanySealContent = CompanySealContent

    @property
    def TaxSealContent(self):
        return self._TaxSealContent

    @TaxSealContent.setter
    def TaxSealContent(self, TaxSealContent):
        self._TaxSealContent = TaxSealContent

    @property
    def VatRollItems(self):
        return self._VatRollItems

    @VatRollItems.setter
    def VatRollItems(self, VatRollItems):
        self._VatRollItems = VatRollItems


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Code = params.get("Code")
        self._Number = params.get("Number")
        self._NumberConfirm = params.get("NumberConfirm")
        self._Date = params.get("Date")
        self._CheckCode = params.get("CheckCode")
        self._Seller = params.get("Seller")
        self._SellerTaxID = params.get("SellerTaxID")
        self._Buyer = params.get("Buyer")
        self._BuyerTaxID = params.get("BuyerTaxID")
        self._Category = params.get("Category")
        self._Total = params.get("Total")
        self._TotalCn = params.get("TotalCn")
        self._Kind = params.get("Kind")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._CompanySealMark = params.get("CompanySealMark")
        self._QRCodeMark = params.get("QRCodeMark")
        self._ServiceName = params.get("ServiceName")
        self._CompanySealContent = params.get("CompanySealContent")
        self._TaxSealContent = params.get("TaxSealContent")
        if params.get("VatRollItems") is not None:
            self._VatRollItems = []
            for item in params.get("VatRollItems"):
                obj = VatRollItem()
                obj._deserialize(item)
                self._VatRollItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceUserInfo(AbstractModel):
    """发票人员信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _TaxId: 纳税人识别号
        :type TaxId: str
        :param _AddrTel: 地 址、电 话
        :type AddrTel: str
        :param _FinancialAccount: 开户行及账号
        :type FinancialAccount: str
        """
        self._Name = None
        self._TaxId = None
        self._AddrTel = None
        self._FinancialAccount = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaxId(self):
        return self._TaxId

    @TaxId.setter
    def TaxId(self, TaxId):
        self._TaxId = TaxId

    @property
    def AddrTel(self):
        return self._AddrTel

    @AddrTel.setter
    def AddrTel(self, AddrTel):
        self._AddrTel = AddrTel

    @property
    def FinancialAccount(self):
        return self._FinancialAccount

    @FinancialAccount.setter
    def FinancialAccount(self, FinancialAccount):
        self._FinancialAccount = FinancialAccount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaxId = params.get("TaxId")
        self._AddrTel = params.get("AddrTel")
        self._FinancialAccount = params.get("FinancialAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceVerifyNewRequest(AbstractModel):
    """VatInvoiceVerifyNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvoiceNo: 发票号码，8位、20位（全电票）
        :type InvoiceNo: str
        :param _InvoiceDate: 开票日期（不支持当天发票查询，支持五年以内开具的发票），格式：“YYYY-MM-DD”，如：2019-12-20。
        :type InvoiceDate: str
        :param _InvoiceCode: 发票代码（10或12 位），全电发票为空。查验未成功超过5次后当日无法再查。
        :type InvoiceCode: str
        :param _InvoiceKind: 票种类型 01:增值税专用发票， 02:货运运输业增值税专用发 票， 03:机动车销售统一发票， 04:增值税普通发票， 08:增值税电子专用发票(含全电)， 10:增值税电子普通发票(含全电)， 11:增值税普通发票(卷式)， 14:增值税电子(通行费)发 票， 15:二手车销售统一发票， 32:深圳区块链发票(云南区块链因业务调整现已下线)。
        :type InvoiceKind: str
        :param _CheckCode: 校验码后 6 位，增值税普通发票、增值税电子普通发票、增值税普通发票(卷式)、增值税电子普通发票(通行费)时必填;
区块链为 5 位
        :type CheckCode: str
        :param _Amount: 不含税金额，增值税专用发票、增值税电子专用发票、机动车销售统一发票、二手车销售统一发票、区块链发票时必填; 全电发票为价税合计(含税金额)
        :type Amount: str
        :param _RegionCode: 地区编码，通用机打电子发票时必填。
广东:4400，浙江:3300
        :type RegionCode: str
        :param _SellerTaxCode: 销方税号，通用机打电子发票必填，区块链发票时必填
        :type SellerTaxCode: str
        :param _EnableCommonElectronic: 是否开启通用机打电子发票，默认为关闭。
        :type EnableCommonElectronic: bool
        """
        self._InvoiceNo = None
        self._InvoiceDate = None
        self._InvoiceCode = None
        self._InvoiceKind = None
        self._CheckCode = None
        self._Amount = None
        self._RegionCode = None
        self._SellerTaxCode = None
        self._EnableCommonElectronic = None

    @property
    def InvoiceNo(self):
        return self._InvoiceNo

    @InvoiceNo.setter
    def InvoiceNo(self, InvoiceNo):
        self._InvoiceNo = InvoiceNo

    @property
    def InvoiceDate(self):
        return self._InvoiceDate

    @InvoiceDate.setter
    def InvoiceDate(self, InvoiceDate):
        self._InvoiceDate = InvoiceDate

    @property
    def InvoiceCode(self):
        return self._InvoiceCode

    @InvoiceCode.setter
    def InvoiceCode(self, InvoiceCode):
        self._InvoiceCode = InvoiceCode

    @property
    def InvoiceKind(self):
        return self._InvoiceKind

    @InvoiceKind.setter
    def InvoiceKind(self, InvoiceKind):
        self._InvoiceKind = InvoiceKind

    @property
    def CheckCode(self):
        return self._CheckCode

    @CheckCode.setter
    def CheckCode(self, CheckCode):
        self._CheckCode = CheckCode

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def RegionCode(self):
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def SellerTaxCode(self):
        return self._SellerTaxCode

    @SellerTaxCode.setter
    def SellerTaxCode(self, SellerTaxCode):
        self._SellerTaxCode = SellerTaxCode

    @property
    def EnableCommonElectronic(self):
        return self._EnableCommonElectronic

    @EnableCommonElectronic.setter
    def EnableCommonElectronic(self, EnableCommonElectronic):
        self._EnableCommonElectronic = EnableCommonElectronic


    def _deserialize(self, params):
        self._InvoiceNo = params.get("InvoiceNo")
        self._InvoiceDate = params.get("InvoiceDate")
        self._InvoiceCode = params.get("InvoiceCode")
        self._InvoiceKind = params.get("InvoiceKind")
        self._CheckCode = params.get("CheckCode")
        self._Amount = params.get("Amount")
        self._RegionCode = params.get("RegionCode")
        self._SellerTaxCode = params.get("SellerTaxCode")
        self._EnableCommonElectronic = params.get("EnableCommonElectronic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceVerifyNewResponse(AbstractModel):
    """VatInvoiceVerifyNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Invoice: 增值税发票信息，详情请点击左侧链接。
        :type Invoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoice`
        :param _VehicleInvoiceInfo: 机动车销售统一发票信息
        :type VehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.VehicleInvoiceInfo`
        :param _UsedVehicleInvoiceInfo: 二手车销售统一发票信息
        :type UsedVehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.UsedVehicleInvoiceInfo`
        :param _PassInvoiceInfoList: 通行费发票信息
        :type PassInvoiceInfoList: list of PassInvoiceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Invoice = None
        self._VehicleInvoiceInfo = None
        self._UsedVehicleInvoiceInfo = None
        self._PassInvoiceInfoList = None
        self._RequestId = None

    @property
    def Invoice(self):
        return self._Invoice

    @Invoice.setter
    def Invoice(self, Invoice):
        self._Invoice = Invoice

    @property
    def VehicleInvoiceInfo(self):
        return self._VehicleInvoiceInfo

    @VehicleInvoiceInfo.setter
    def VehicleInvoiceInfo(self, VehicleInvoiceInfo):
        self._VehicleInvoiceInfo = VehicleInvoiceInfo

    @property
    def UsedVehicleInvoiceInfo(self):
        return self._UsedVehicleInvoiceInfo

    @UsedVehicleInvoiceInfo.setter
    def UsedVehicleInvoiceInfo(self, UsedVehicleInvoiceInfo):
        self._UsedVehicleInvoiceInfo = UsedVehicleInvoiceInfo

    @property
    def PassInvoiceInfoList(self):
        return self._PassInvoiceInfoList

    @PassInvoiceInfoList.setter
    def PassInvoiceInfoList(self, PassInvoiceInfoList):
        self._PassInvoiceInfoList = PassInvoiceInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Invoice") is not None:
            self._Invoice = VatInvoice()
            self._Invoice._deserialize(params.get("Invoice"))
        if params.get("VehicleInvoiceInfo") is not None:
            self._VehicleInvoiceInfo = VehicleInvoiceInfo()
            self._VehicleInvoiceInfo._deserialize(params.get("VehicleInvoiceInfo"))
        if params.get("UsedVehicleInvoiceInfo") is not None:
            self._UsedVehicleInvoiceInfo = UsedVehicleInvoiceInfo()
            self._UsedVehicleInvoiceInfo._deserialize(params.get("UsedVehicleInvoiceInfo"))
        if params.get("PassInvoiceInfoList") is not None:
            self._PassInvoiceInfoList = []
            for item in params.get("PassInvoiceInfoList"):
                obj = PassInvoiceInfo()
                obj._deserialize(item)
                self._PassInvoiceInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class VatInvoiceVerifyRequest(AbstractModel):
    """VatInvoiceVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvoiceCode: 发票代码， 一张发票一天只能查询5次。
        :type InvoiceCode: str
        :param _InvoiceNo: 发票号码（8位）
        :type InvoiceNo: str
        :param _InvoiceDate: 开票日期（不支持当天发票查询，支持五年以内开具的发票），格式：“YYYY-MM-DD”，如：2019-12-20。
        :type InvoiceDate: str
        :param _Additional: 根据票种传递对应值，如果报参数错误，请仔细检查每个票种对应的值

增值税专用发票：开具金额（不含税）

增值税普通发票、增值税电子普通发票（含通行费发票）、增值税普通发票（卷票）：校验码后6位

区块链发票：不含税金额/校验码，例如：“285.01/856ab”

机动车销售统一发票：不含税价

货物运输业增值税专用发票：合计金额

二手车销售统一发票：车价合计
        :type Additional: str
        """
        self._InvoiceCode = None
        self._InvoiceNo = None
        self._InvoiceDate = None
        self._Additional = None

    @property
    def InvoiceCode(self):
        return self._InvoiceCode

    @InvoiceCode.setter
    def InvoiceCode(self, InvoiceCode):
        self._InvoiceCode = InvoiceCode

    @property
    def InvoiceNo(self):
        return self._InvoiceNo

    @InvoiceNo.setter
    def InvoiceNo(self, InvoiceNo):
        self._InvoiceNo = InvoiceNo

    @property
    def InvoiceDate(self):
        return self._InvoiceDate

    @InvoiceDate.setter
    def InvoiceDate(self, InvoiceDate):
        self._InvoiceDate = InvoiceDate

    @property
    def Additional(self):
        return self._Additional

    @Additional.setter
    def Additional(self, Additional):
        self._Additional = Additional


    def _deserialize(self, params):
        self._InvoiceCode = params.get("InvoiceCode")
        self._InvoiceNo = params.get("InvoiceNo")
        self._InvoiceDate = params.get("InvoiceDate")
        self._Additional = params.get("Additional")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatInvoiceVerifyResponse(AbstractModel):
    """VatInvoiceVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Invoice: 增值税发票信息，详情请点击左侧链接。
        :type Invoice: :class:`tencentcloud.ocr.v20181119.models.VatInvoice`
        :param _VehicleInvoiceInfo: 机动车销售统一发票信息
        :type VehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.VehicleInvoiceInfo`
        :param _UsedVehicleInvoiceInfo: 二手车销售统一发票信息
        :type UsedVehicleInvoiceInfo: :class:`tencentcloud.ocr.v20181119.models.UsedVehicleInvoiceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Invoice = None
        self._VehicleInvoiceInfo = None
        self._UsedVehicleInvoiceInfo = None
        self._RequestId = None

    @property
    def Invoice(self):
        return self._Invoice

    @Invoice.setter
    def Invoice(self, Invoice):
        self._Invoice = Invoice

    @property
    def VehicleInvoiceInfo(self):
        return self._VehicleInvoiceInfo

    @VehicleInvoiceInfo.setter
    def VehicleInvoiceInfo(self, VehicleInvoiceInfo):
        self._VehicleInvoiceInfo = VehicleInvoiceInfo

    @property
    def UsedVehicleInvoiceInfo(self):
        return self._UsedVehicleInvoiceInfo

    @UsedVehicleInvoiceInfo.setter
    def UsedVehicleInvoiceInfo(self, UsedVehicleInvoiceInfo):
        self._UsedVehicleInvoiceInfo = UsedVehicleInvoiceInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Invoice") is not None:
            self._Invoice = VatInvoice()
            self._Invoice._deserialize(params.get("Invoice"))
        if params.get("VehicleInvoiceInfo") is not None:
            self._VehicleInvoiceInfo = VehicleInvoiceInfo()
            self._VehicleInvoiceInfo._deserialize(params.get("VehicleInvoiceInfo"))
        if params.get("UsedVehicleInvoiceInfo") is not None:
            self._UsedVehicleInvoiceInfo = UsedVehicleInvoiceInfo()
            self._UsedVehicleInvoiceInfo._deserialize(params.get("UsedVehicleInvoiceInfo"))
        self._RequestId = params.get("RequestId")


class VatRollInvoiceInfo(AbstractModel):
    """增值税发票卷票信息

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
发票代码、合计金额(小写)、合计金额(大写)、开票日期、发票号码、购买方识别号、销售方识别号、校验码、销售方名称、购买方名称、发票消费类型、省、市、是否有公司印章、单价、金额、数量、服务类型、品名、种类。
        :type Name: str
        :param _Value: 识别出的字段名称对应的值，也就是字段Name对应的字符串结果。
        :type Value: str
        :param _Rect: 文本行在旋转纠正之后的图像中的像素坐标。
        :type Rect: :class:`tencentcloud.ocr.v20181119.models.Rect`
        """
        self._Name = None
        self._Value = None
        self._Rect = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        if params.get("Rect") is not None:
            self._Rect = Rect()
            self._Rect._deserialize(params.get("Rect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatRollInvoiceOCRRequest(AbstractModel):
    """VatRollInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VatRollInvoiceOCRResponse(AbstractModel):
    """VatRollInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VatRollInvoiceInfos: 增值税发票（卷票）识别结果，具体内容请点击左侧链接。
        :type VatRollInvoiceInfos: list of VatRollInvoiceInfo
        :param _Angle: 图片旋转角度（角度制），文本的水平方向为0°，顺时针为正，逆时针为负。
        :type Angle: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VatRollInvoiceInfos = None
        self._Angle = None
        self._RequestId = None

    @property
    def VatRollInvoiceInfos(self):
        return self._VatRollInvoiceInfos

    @VatRollInvoiceInfos.setter
    def VatRollInvoiceInfos(self, VatRollInvoiceInfos):
        self._VatRollInvoiceInfos = VatRollInvoiceInfos

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VatRollInvoiceInfos") is not None:
            self._VatRollInvoiceInfos = []
            for item in params.get("VatRollInvoiceInfos"):
                obj = VatRollInvoiceInfo()
                obj._deserialize(item)
                self._VatRollInvoiceInfos.append(obj)
        self._Angle = params.get("Angle")
        self._RequestId = params.get("RequestId")


class VatRollItem(AbstractModel):
    """增值税普通发票（卷票）条目

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
        :type Name: str
        :param _Quantity: 数量
        :type Quantity: str
        :param _Price: 单价
        :type Price: str
        :param _Total: 金额
        :type Total: str
        """
        self._Name = None
        self._Quantity = None
        self._Price = None
        self._Total = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Quantity(self):
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Quantity = params.get("Quantity")
        self._Price = params.get("Price")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleInvoiceInfo(AbstractModel):
    """机动车销售统一发票信息

    """

    def __init__(self):
        r"""
        :param _CarType: 车辆类型
        :type CarType: str
        :param _PlateModel: 厂牌型号
        :type PlateModel: str
        :param _ProduceAddress: 产地
        :type ProduceAddress: str
        :param _CertificateNo: 合格证号
        :type CertificateNo: str
        :param _ImportNo: 进口证明书号
        :type ImportNo: str
        :param _VinNo: LSVCA2NP9HN0xxxxx
        :type VinNo: str
        :param _PayTaxesNo: 完税证书号
        :type PayTaxesNo: str
        :param _Tonnage: 吨位
        :type Tonnage: str
        :param _LimitCount: 限乘人数
        :type LimitCount: str
        :param _EngineNo: 发动机号码
        :type EngineNo: str
        :param _BizCheckFormNo: 商检单号
        :type BizCheckFormNo: str
        :param _TaxtationOrgCode: 主管税务机关代码
        :type TaxtationOrgCode: str
        :param _TaxtationOrgName: 主管税务机关名称
        :type TaxtationOrgName: str
        :param _MotorTaxRate: 税率
        :type MotorTaxRate: str
        :param _MotorBankName: 银行账号
        :type MotorBankName: str
        :param _MotorBankAccount: 开户行
        :type MotorBankAccount: str
        :param _SellerAddress: 销售地址
        :type SellerAddress: str
        :param _SellerTel: 销售电话
        :type SellerTel: str
        :param _BuyerNo: 购方身份证
        :type BuyerNo: str
        """
        self._CarType = None
        self._PlateModel = None
        self._ProduceAddress = None
        self._CertificateNo = None
        self._ImportNo = None
        self._VinNo = None
        self._PayTaxesNo = None
        self._Tonnage = None
        self._LimitCount = None
        self._EngineNo = None
        self._BizCheckFormNo = None
        self._TaxtationOrgCode = None
        self._TaxtationOrgName = None
        self._MotorTaxRate = None
        self._MotorBankName = None
        self._MotorBankAccount = None
        self._SellerAddress = None
        self._SellerTel = None
        self._BuyerNo = None

    @property
    def CarType(self):
        return self._CarType

    @CarType.setter
    def CarType(self, CarType):
        self._CarType = CarType

    @property
    def PlateModel(self):
        return self._PlateModel

    @PlateModel.setter
    def PlateModel(self, PlateModel):
        self._PlateModel = PlateModel

    @property
    def ProduceAddress(self):
        return self._ProduceAddress

    @ProduceAddress.setter
    def ProduceAddress(self, ProduceAddress):
        self._ProduceAddress = ProduceAddress

    @property
    def CertificateNo(self):
        return self._CertificateNo

    @CertificateNo.setter
    def CertificateNo(self, CertificateNo):
        self._CertificateNo = CertificateNo

    @property
    def ImportNo(self):
        return self._ImportNo

    @ImportNo.setter
    def ImportNo(self, ImportNo):
        self._ImportNo = ImportNo

    @property
    def VinNo(self):
        return self._VinNo

    @VinNo.setter
    def VinNo(self, VinNo):
        self._VinNo = VinNo

    @property
    def PayTaxesNo(self):
        return self._PayTaxesNo

    @PayTaxesNo.setter
    def PayTaxesNo(self, PayTaxesNo):
        self._PayTaxesNo = PayTaxesNo

    @property
    def Tonnage(self):
        return self._Tonnage

    @Tonnage.setter
    def Tonnage(self, Tonnage):
        self._Tonnage = Tonnage

    @property
    def LimitCount(self):
        return self._LimitCount

    @LimitCount.setter
    def LimitCount(self, LimitCount):
        self._LimitCount = LimitCount

    @property
    def EngineNo(self):
        return self._EngineNo

    @EngineNo.setter
    def EngineNo(self, EngineNo):
        self._EngineNo = EngineNo

    @property
    def BizCheckFormNo(self):
        return self._BizCheckFormNo

    @BizCheckFormNo.setter
    def BizCheckFormNo(self, BizCheckFormNo):
        self._BizCheckFormNo = BizCheckFormNo

    @property
    def TaxtationOrgCode(self):
        return self._TaxtationOrgCode

    @TaxtationOrgCode.setter
    def TaxtationOrgCode(self, TaxtationOrgCode):
        self._TaxtationOrgCode = TaxtationOrgCode

    @property
    def TaxtationOrgName(self):
        return self._TaxtationOrgName

    @TaxtationOrgName.setter
    def TaxtationOrgName(self, TaxtationOrgName):
        self._TaxtationOrgName = TaxtationOrgName

    @property
    def MotorTaxRate(self):
        return self._MotorTaxRate

    @MotorTaxRate.setter
    def MotorTaxRate(self, MotorTaxRate):
        self._MotorTaxRate = MotorTaxRate

    @property
    def MotorBankName(self):
        return self._MotorBankName

    @MotorBankName.setter
    def MotorBankName(self, MotorBankName):
        self._MotorBankName = MotorBankName

    @property
    def MotorBankAccount(self):
        return self._MotorBankAccount

    @MotorBankAccount.setter
    def MotorBankAccount(self, MotorBankAccount):
        self._MotorBankAccount = MotorBankAccount

    @property
    def SellerAddress(self):
        return self._SellerAddress

    @SellerAddress.setter
    def SellerAddress(self, SellerAddress):
        self._SellerAddress = SellerAddress

    @property
    def SellerTel(self):
        return self._SellerTel

    @SellerTel.setter
    def SellerTel(self, SellerTel):
        self._SellerTel = SellerTel

    @property
    def BuyerNo(self):
        return self._BuyerNo

    @BuyerNo.setter
    def BuyerNo(self, BuyerNo):
        self._BuyerNo = BuyerNo


    def _deserialize(self, params):
        self._CarType = params.get("CarType")
        self._PlateModel = params.get("PlateModel")
        self._ProduceAddress = params.get("ProduceAddress")
        self._CertificateNo = params.get("CertificateNo")
        self._ImportNo = params.get("ImportNo")
        self._VinNo = params.get("VinNo")
        self._PayTaxesNo = params.get("PayTaxesNo")
        self._Tonnage = params.get("Tonnage")
        self._LimitCount = params.get("LimitCount")
        self._EngineNo = params.get("EngineNo")
        self._BizCheckFormNo = params.get("BizCheckFormNo")
        self._TaxtationOrgCode = params.get("TaxtationOrgCode")
        self._TaxtationOrgName = params.get("TaxtationOrgName")
        self._MotorTaxRate = params.get("MotorTaxRate")
        self._MotorBankName = params.get("MotorBankName")
        self._MotorBankAccount = params.get("MotorBankAccount")
        self._SellerAddress = params.get("SellerAddress")
        self._SellerTel = params.get("SellerTel")
        self._BuyerNo = params.get("BuyerNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleLicenseOCRRequest(AbstractModel):
    """VehicleLicenseOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。
建议图片存储于腾讯云，可保障更高的下载速度和稳定性。
        :type ImageUrl: str
        :param _CardSide: FRONT 为行驶证主页正面（有红色印章的一面），
BACK 为行驶证副页正面（有号码号牌的一面），
DOUBLE 为行驶证主页正面和副页正面。
默认值为：FRONT。
        :type CardSide: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._CardSide = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CardSide(self):
        return self._CardSide

    @CardSide.setter
    def CardSide(self, CardSide):
        self._CardSide = CardSide


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._CardSide = params.get("CardSide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleLicenseOCRResponse(AbstractModel):
    """VehicleLicenseOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FrontInfo: 行驶证主页正面的识别结果，CardSide 为 FRONT。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleFront`
        :param _BackInfo: 行驶证副页正面的识别结果，CardSide 为 BACK。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackInfo: :class:`tencentcloud.ocr.v20181119.models.TextVehicleBack`
        :param _RecognizeWarnCode: Code 告警码列表和释义：
-9102 复印件告警
-9103 翻拍件告警
注：告警码可以同时存在多个
        :type RecognizeWarnCode: list of int
        :param _RecognizeWarnMsg: 告警码说明：
WARN_DRIVER_LICENSE_COPY_CARD 复印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
注：告警信息可以同时存在多个
        :type RecognizeWarnMsg: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FrontInfo = None
        self._BackInfo = None
        self._RecognizeWarnCode = None
        self._RecognizeWarnMsg = None
        self._RequestId = None

    @property
    def FrontInfo(self):
        return self._FrontInfo

    @FrontInfo.setter
    def FrontInfo(self, FrontInfo):
        self._FrontInfo = FrontInfo

    @property
    def BackInfo(self):
        return self._BackInfo

    @BackInfo.setter
    def BackInfo(self, BackInfo):
        self._BackInfo = BackInfo

    @property
    def RecognizeWarnCode(self):
        return self._RecognizeWarnCode

    @RecognizeWarnCode.setter
    def RecognizeWarnCode(self, RecognizeWarnCode):
        self._RecognizeWarnCode = RecognizeWarnCode

    @property
    def RecognizeWarnMsg(self):
        return self._RecognizeWarnMsg

    @RecognizeWarnMsg.setter
    def RecognizeWarnMsg(self, RecognizeWarnMsg):
        self._RecognizeWarnMsg = RecognizeWarnMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FrontInfo") is not None:
            self._FrontInfo = TextVehicleFront()
            self._FrontInfo._deserialize(params.get("FrontInfo"))
        if params.get("BackInfo") is not None:
            self._BackInfo = TextVehicleBack()
            self._BackInfo._deserialize(params.get("BackInfo"))
        self._RecognizeWarnCode = params.get("RecognizeWarnCode")
        self._RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self._RequestId = params.get("RequestId")


class VehicleRegCertInfo(AbstractModel):
    """机动车登记证书识别结果

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的字段名称(关键字)，支持以下字段：
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
        :param _Value: 识别出的字段名称对应的值，也就是字段name对应的字符串结果。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleRegCertOCRRequest(AbstractModel):
    """VehicleRegCertOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleRegCertOCRResponse(AbstractModel):
    """VehicleRegCertOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VehicleRegCertInfos: 机动车登记证书识别结果，具体内容请点击左侧链接。
        :type VehicleRegCertInfos: list of VehicleRegCertInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VehicleRegCertInfos = None
        self._RequestId = None

    @property
    def VehicleRegCertInfos(self):
        return self._VehicleRegCertInfos

    @VehicleRegCertInfos.setter
    def VehicleRegCertInfos(self, VehicleRegCertInfos):
        self._VehicleRegCertInfos = VehicleRegCertInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VehicleRegCertInfos") is not None:
            self._VehicleRegCertInfos = []
            for item in params.get("VehicleRegCertInfos"):
                obj = VehicleRegCertInfo()
                obj._deserialize(item)
                self._VehicleRegCertInfos.append(obj)
        self._RequestId = params.get("RequestId")


class VerifyOfdVatInvoiceOCRRequest(AbstractModel):
    """VerifyOfdVatInvoiceOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OfdFileUrl: OFD文件的 Url 地址。
        :type OfdFileUrl: str
        :param _OfdFileBase64: OFD文件的 Base64 值。
OfdFileUrl 和 OfdFileBase64 必传其一，若两者都传，只解析OfdFileBase64。
        :type OfdFileBase64: str
        """
        self._OfdFileUrl = None
        self._OfdFileBase64 = None

    @property
    def OfdFileUrl(self):
        return self._OfdFileUrl

    @OfdFileUrl.setter
    def OfdFileUrl(self, OfdFileUrl):
        self._OfdFileUrl = OfdFileUrl

    @property
    def OfdFileBase64(self):
        return self._OfdFileBase64

    @OfdFileBase64.setter
    def OfdFileBase64(self, OfdFileBase64):
        self._OfdFileBase64 = OfdFileBase64


    def _deserialize(self, params):
        self._OfdFileUrl = params.get("OfdFileUrl")
        self._OfdFileBase64 = params.get("OfdFileBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyOfdVatInvoiceOCRResponse(AbstractModel):
    """VerifyOfdVatInvoiceOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 发票类型
026:增值税电子普通发票
028:增值税电子专用发票
010:电子发票（普通发票）
020:电子发票（增值税专用发票）
        :type Type: str
        :param _InvoiceCode: 发票代码
        :type InvoiceCode: str
        :param _InvoiceNumber: 发票号码
        :type InvoiceNumber: str
        :param _IssueDate: 开票日期
        :type IssueDate: str
        :param _InvoiceCheckCode: 验证码
        :type InvoiceCheckCode: str
        :param _MachineNumber: 机器编号
        :type MachineNumber: str
        :param _TaxControlCode: 密码区
        :type TaxControlCode: str
        :param _Buyer: 购买方
        :type Buyer: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceUserInfo`
        :param _Seller: 销售方
        :type Seller: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceUserInfo`
        :param _TaxInclusiveTotalAmount: 价税合计
        :type TaxInclusiveTotalAmount: str
        :param _InvoiceClerk: 开票人
        :type InvoiceClerk: str
        :param _Payee: 收款人
        :type Payee: str
        :param _Checker: 复核人
        :type Checker: str
        :param _TaxTotalAmount: 税额
        :type TaxTotalAmount: str
        :param _TaxExclusiveTotalAmount: 不含税金额
        :type TaxExclusiveTotalAmount: str
        :param _Note: 备注
        :type Note: str
        :param _GoodsInfos: 货物或服务清单
        :type GoodsInfos: list of VatInvoiceGoodsInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Type = None
        self._InvoiceCode = None
        self._InvoiceNumber = None
        self._IssueDate = None
        self._InvoiceCheckCode = None
        self._MachineNumber = None
        self._TaxControlCode = None
        self._Buyer = None
        self._Seller = None
        self._TaxInclusiveTotalAmount = None
        self._InvoiceClerk = None
        self._Payee = None
        self._Checker = None
        self._TaxTotalAmount = None
        self._TaxExclusiveTotalAmount = None
        self._Note = None
        self._GoodsInfos = None
        self._RequestId = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InvoiceCode(self):
        return self._InvoiceCode

    @InvoiceCode.setter
    def InvoiceCode(self, InvoiceCode):
        self._InvoiceCode = InvoiceCode

    @property
    def InvoiceNumber(self):
        return self._InvoiceNumber

    @InvoiceNumber.setter
    def InvoiceNumber(self, InvoiceNumber):
        self._InvoiceNumber = InvoiceNumber

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def InvoiceCheckCode(self):
        return self._InvoiceCheckCode

    @InvoiceCheckCode.setter
    def InvoiceCheckCode(self, InvoiceCheckCode):
        self._InvoiceCheckCode = InvoiceCheckCode

    @property
    def MachineNumber(self):
        return self._MachineNumber

    @MachineNumber.setter
    def MachineNumber(self, MachineNumber):
        self._MachineNumber = MachineNumber

    @property
    def TaxControlCode(self):
        return self._TaxControlCode

    @TaxControlCode.setter
    def TaxControlCode(self, TaxControlCode):
        self._TaxControlCode = TaxControlCode

    @property
    def Buyer(self):
        return self._Buyer

    @Buyer.setter
    def Buyer(self, Buyer):
        self._Buyer = Buyer

    @property
    def Seller(self):
        return self._Seller

    @Seller.setter
    def Seller(self, Seller):
        self._Seller = Seller

    @property
    def TaxInclusiveTotalAmount(self):
        return self._TaxInclusiveTotalAmount

    @TaxInclusiveTotalAmount.setter
    def TaxInclusiveTotalAmount(self, TaxInclusiveTotalAmount):
        self._TaxInclusiveTotalAmount = TaxInclusiveTotalAmount

    @property
    def InvoiceClerk(self):
        return self._InvoiceClerk

    @InvoiceClerk.setter
    def InvoiceClerk(self, InvoiceClerk):
        self._InvoiceClerk = InvoiceClerk

    @property
    def Payee(self):
        return self._Payee

    @Payee.setter
    def Payee(self, Payee):
        self._Payee = Payee

    @property
    def Checker(self):
        return self._Checker

    @Checker.setter
    def Checker(self, Checker):
        self._Checker = Checker

    @property
    def TaxTotalAmount(self):
        return self._TaxTotalAmount

    @TaxTotalAmount.setter
    def TaxTotalAmount(self, TaxTotalAmount):
        self._TaxTotalAmount = TaxTotalAmount

    @property
    def TaxExclusiveTotalAmount(self):
        return self._TaxExclusiveTotalAmount

    @TaxExclusiveTotalAmount.setter
    def TaxExclusiveTotalAmount(self, TaxExclusiveTotalAmount):
        self._TaxExclusiveTotalAmount = TaxExclusiveTotalAmount

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def GoodsInfos(self):
        return self._GoodsInfos

    @GoodsInfos.setter
    def GoodsInfos(self, GoodsInfos):
        self._GoodsInfos = GoodsInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._InvoiceCode = params.get("InvoiceCode")
        self._InvoiceNumber = params.get("InvoiceNumber")
        self._IssueDate = params.get("IssueDate")
        self._InvoiceCheckCode = params.get("InvoiceCheckCode")
        self._MachineNumber = params.get("MachineNumber")
        self._TaxControlCode = params.get("TaxControlCode")
        if params.get("Buyer") is not None:
            self._Buyer = VatInvoiceUserInfo()
            self._Buyer._deserialize(params.get("Buyer"))
        if params.get("Seller") is not None:
            self._Seller = VatInvoiceUserInfo()
            self._Seller._deserialize(params.get("Seller"))
        self._TaxInclusiveTotalAmount = params.get("TaxInclusiveTotalAmount")
        self._InvoiceClerk = params.get("InvoiceClerk")
        self._Payee = params.get("Payee")
        self._Checker = params.get("Checker")
        self._TaxTotalAmount = params.get("TaxTotalAmount")
        self._TaxExclusiveTotalAmount = params.get("TaxExclusiveTotalAmount")
        self._Note = params.get("Note")
        if params.get("GoodsInfos") is not None:
            self._GoodsInfos = []
            for item in params.get("GoodsInfos"):
                obj = VatInvoiceGoodsInfo()
                obj._deserialize(item)
                self._GoodsInfos.append(obj)
        self._RequestId = params.get("RequestId")


class VinOCRRequest(AbstractModel):
    """VinOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self._ImageBase64 = None
        self._ImageUrl = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VinOCRResponse(AbstractModel):
    """VinOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Vin: 检测到的车辆 VIN 码。
        :type Vin: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Vin = None
        self._RequestId = None

    @property
    def Vin(self):
        return self._Vin

    @Vin.setter
    def Vin(self, Vin):
        self._Vin = Vin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Vin = params.get("Vin")
        self._RequestId = params.get("RequestId")


class WaybillOCRRequest(AbstractModel):
    """WaybillOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片的 Base64 值。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。
图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param _ImageUrl: 图片的 Url 地址。
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _EnablePreDetect: 预检测开关，当待识别运单占整个输入图像的比例较小时，建议打开预检测开关。默认值为false。
        :type EnablePreDetect: bool
        :param _IsPdf: 是否开启PDF识别，默认值为true，开启后可同时支持图片和PDF的识别。
        :type IsPdf: bool
        :param _PdfPageNumber: 需要识别的PDF页面的对应页码，仅支持PDF单页识别，当上传文件为PDF且IsPdf参数值为true时有效，默认值为1。
        :type PdfPageNumber: int
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._EnablePreDetect = None
        self._IsPdf = None
        self._PdfPageNumber = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def EnablePreDetect(self):
        return self._EnablePreDetect

    @EnablePreDetect.setter
    def EnablePreDetect(self, EnablePreDetect):
        self._EnablePreDetect = EnablePreDetect

    @property
    def IsPdf(self):
        return self._IsPdf

    @IsPdf.setter
    def IsPdf(self, IsPdf):
        self._IsPdf = IsPdf

    @property
    def PdfPageNumber(self):
        return self._PdfPageNumber

    @PdfPageNumber.setter
    def PdfPageNumber(self, PdfPageNumber):
        self._PdfPageNumber = PdfPageNumber


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._EnablePreDetect = params.get("EnablePreDetect")
        self._IsPdf = params.get("IsPdf")
        self._PdfPageNumber = params.get("PdfPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaybillOCRResponse(AbstractModel):
    """WaybillOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextDetections: 检测到的文本信息，具体内容请点击左侧链接。
        :type TextDetections: :class:`tencentcloud.ocr.v20181119.models.TextWaybill`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextDetections = None
        self._RequestId = None

    @property
    def TextDetections(self):
        return self._TextDetections

    @TextDetections.setter
    def TextDetections(self, TextDetections):
        self._TextDetections = TextDetections

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self._TextDetections = TextWaybill()
            self._TextDetections._deserialize(params.get("TextDetections"))
        self._RequestId = params.get("RequestId")


class WaybillObj(AbstractModel):
    """运单识别对象

    """

    def __init__(self):
        r"""
        :param _Text: 识别出的文本行内容
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordCoordPoint(AbstractModel):
    """英文OCR识别出的单词在原图中的四点坐标数组

    """

    def __init__(self):
        r"""
        :param _WordCoordinate: 英文OCR识别出的每个单词在原图中的四点坐标。
        :type WordCoordinate: list of Coord
        """
        self._WordCoordinate = None

    @property
    def WordCoordinate(self):
        return self._WordCoordinate

    @WordCoordinate.setter
    def WordCoordinate(self, WordCoordinate):
        self._WordCoordinate = WordCoordinate


    def _deserialize(self, params):
        if params.get("WordCoordinate") is not None:
            self._WordCoordinate = []
            for item in params.get("WordCoordinate"):
                obj = Coord()
                obj._deserialize(item)
                self._WordCoordinate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordItem(AbstractModel):
    """还原文本信息

    """

    def __init__(self):
        r"""
        :param _DetectedText: 文本块内容
        :type DetectedText: str
        :param _Coord: 四点坐标
        :type Coord: :class:`tencentcloud.ocr.v20181119.models.Polygon`
        """
        self._DetectedText = None
        self._Coord = None

    @property
    def DetectedText(self):
        return self._DetectedText

    @DetectedText.setter
    def DetectedText(self, DetectedText):
        self._DetectedText = DetectedText

    @property
    def Coord(self):
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord


    def _deserialize(self, params):
        self._DetectedText = params.get("DetectedText")
        if params.get("Coord") is not None:
            self._Coord = Polygon()
            self._Coord._deserialize(params.get("Coord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Words(AbstractModel):
    """识别出来的单词信息包括单词（包括单词Character和单词置信度confidence）

    """

    def __init__(self):
        r"""
        :param _Confidence: 置信度 0 ~100
        :type Confidence: int
        :param _Character: 候选字Character
        :type Character: str
        """
        self._Confidence = None
        self._Character = None

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Character(self):
        return self._Character

    @Character.setter
    def Character(self, Character):
        self._Character = Character


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Character = params.get("Character")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        