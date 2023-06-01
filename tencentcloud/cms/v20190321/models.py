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


class CodeDetail(AbstractModel):
    """从图片中检测到的二维码，可能为多个

    """

    def __init__(self):
        r"""
        :param StrCharset: 二维码文本的编码格式
注意：此字段可能返回 null，表示取不到有效值。
        :type StrCharset: str
        :param QrCodePosition: 二维码在图片中的位置，由边界点的坐标表示
注意：此字段可能返回 null，表示取不到有效值。
        :type QrCodePosition: list of CodePosition
        :param StrQrCodeText: 二维码的文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type StrQrCodeText: str
        :param Uint32QrCodeType: 二维码的类型：1:ONED_BARCODE，2:QRCOD，3:WXCODE，4:PDF417，5:DATAMATRIX
注意：此字段可能返回 null，表示取不到有效值。
        :type Uint32QrCodeType: int
        :param CodeCharset: 二维码文本的编码格式（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeCharset: str
        :param CodePosition: 二维码在图片中的位置，由边界点的坐标表示（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodePosition: list of CodePosition
        :param CodeText: 二维码的文本内容（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeText: str
        :param CodeType: 二维码的类型：1:ONED_BARCODE，2:QRCOD，3:WXCODE，4:PDF417，5:DATAMATRIX（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: int
        """
        self.StrCharset = None
        self.QrCodePosition = None
        self.StrQrCodeText = None
        self.Uint32QrCodeType = None
        self.CodeCharset = None
        self.CodePosition = None
        self.CodeText = None
        self.CodeType = None


    def _deserialize(self, params):
        self.StrCharset = params.get("StrCharset")
        if params.get("QrCodePosition") is not None:
            self.QrCodePosition = []
            for item in params.get("QrCodePosition"):
                obj = CodePosition()
                obj._deserialize(item)
                self.QrCodePosition.append(obj)
        self.StrQrCodeText = params.get("StrQrCodeText")
        self.Uint32QrCodeType = params.get("Uint32QrCodeType")
        self.CodeCharset = params.get("CodeCharset")
        if params.get("CodePosition") is not None:
            self.CodePosition = []
            for item in params.get("CodePosition"):
                obj = CodePosition()
                obj._deserialize(item)
                self.CodePosition.append(obj)
        self.CodeText = params.get("CodeText")
        self.CodeType = params.get("CodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeDetect(AbstractModel):
    """图片二维码详情

    """

    def __init__(self):
        r"""
        :param ModerationCode: 检测是否成功，0：成功，-1：出错
注意：此字段可能返回 null，表示取不到有效值。
        :type ModerationCode: int
        :param ModerationDetail: 从图片中检测到的二维码，可能为多个
注意：此字段可能返回 null，表示取不到有效值。
        :type ModerationDetail: list of CodeDetail
        """
        self.ModerationCode = None
        self.ModerationDetail = None


    def _deserialize(self, params):
        self.ModerationCode = params.get("ModerationCode")
        if params.get("ModerationDetail") is not None:
            self.ModerationDetail = []
            for item in params.get("ModerationDetail"):
                obj = CodeDetail()
                obj._deserialize(item)
                self.ModerationDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodePosition(AbstractModel):
    """二维码在图片中的位置，由边界点的坐标表示

    """

    def __init__(self):
        r"""
        :param FloatX: 二维码边界点X轴坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type FloatX: float
        :param FloatY: 二维码边界点Y轴坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type FloatY: float
        """
        self.FloatX = None
        self.FloatY = None


    def _deserialize(self, params):
        self.FloatX = params.get("FloatX")
        self.FloatY = params.get("FloatY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param Width: 宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Cy: 左上角纵坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cy: int
        :param Cx: 左上角横坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cx: int
        :param Height: 高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self.Width = None
        self.Cy = None
        self.Cx = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Cy = params.get("Cy")
        self.Cx = params.get("Cx")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeywordsSamplesRequest(AbstractModel):
    """CreateKeywordsSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserKeywords: 关键词库信息：单次限制写入2000个，词库总容量不可超过10000个。
        :type UserKeywords: list of UserKeyword
        :param LibID: 词库ID
        :type LibID: str
        """
        self.UserKeywords = None
        self.LibID = None


    def _deserialize(self, params):
        if params.get("UserKeywords") is not None:
            self.UserKeywords = []
            for item in params.get("UserKeywords"):
                obj = UserKeyword()
                obj._deserialize(item)
                self.UserKeywords.append(obj)
        self.LibID = params.get("LibID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeywordsSamplesResponse(AbstractModel):
    """CreateKeywordsSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param SampleIDs: 添加成功的关键词ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleIDs: list of str
        :param DupInfos: 重复关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DupInfos: list of UserKeywordInfo
        :param InvalidSamples: 无效关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidSamples: list of InvalidSample
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SampleIDs = None
        self.DupInfos = None
        self.InvalidSamples = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SampleIDs = params.get("SampleIDs")
        if params.get("DupInfos") is not None:
            self.DupInfos = []
            for item in params.get("DupInfos"):
                obj = UserKeywordInfo()
                obj._deserialize(item)
                self.DupInfos.append(obj)
        if params.get("InvalidSamples") is not None:
            self.InvalidSamples = []
            for item in params.get("InvalidSamples"):
                obj = InvalidSample()
                obj._deserialize(item)
                self.InvalidSamples.append(obj)
        self.RequestId = params.get("RequestId")


class CustomResult(AbstractModel):
    """文本返回的自定义词库结果

    """

    def __init__(self):
        r"""
        :param Keywords: 命中的自定义关键词
        :type Keywords: list of str
        :param LibName: 自定义词库名称
        :type LibName: str
        :param LibId: 自定义库id
        :type LibId: str
        :param Type: 命中的自定义关键词的类型
        :type Type: str
        """
        self.Keywords = None
        self.LibName = None
        self.LibId = None
        self.Type = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.LibName = params.get("LibName")
        self.LibId = params.get("LibId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLibSamplesRequest(AbstractModel):
    """DeleteLibSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param SampleIDs: 关键词ID
        :type SampleIDs: list of str
        :param LibID: 词库ID
        :type LibID: str
        """
        self.SampleIDs = None
        self.LibID = None


    def _deserialize(self, params):
        self.SampleIDs = params.get("SampleIDs")
        self.LibID = params.get("LibID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLibSamplesResponse(AbstractModel):
    """DeleteLibSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 删除成功的数量
        :type Count: int
        :param Details: 每个关键词删除的结果
        :type Details: list of DeleteSampleDetails
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = DeleteSampleDetails()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteSampleDetails(AbstractModel):
    """词库关键词删除结果详情

    """

    def __init__(self):
        r"""
        :param SampleID: 关键词ID
        :type SampleID: str
        :param Content: 关键词内容
        :type Content: str
        :param Deleted: 是否删除成功
        :type Deleted: bool
        :param ErrorInfo: 错误信息
        :type ErrorInfo: str
        """
        self.SampleID = None
        self.Content = None
        self.Deleted = None
        self.ErrorInfo = None


    def _deserialize(self, params):
        self.SampleID = params.get("SampleID")
        self.Content = params.get("Content")
        self.Deleted = params.get("Deleted")
        self.ErrorInfo = params.get("ErrorInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeywordsLibsRequest(AbstractModel):
    """DescribeKeywordsLibs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 单页条数，最大为100条
        :type Limit: int
        :param Offset: 条数偏移量
        :type Offset: int
        :param Filters: 过滤器(支持LibName模糊查询,CustomLibIDs词库id列表过滤)
        :type Filters: list of Filters
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeywordsLibsResponse(AbstractModel):
    """DescribeKeywordsLibs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 词库记录数
        :type TotalCount: int
        :param Infos: 词库详情
        :type Infos: list of KeywordsLibInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = KeywordsLibInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLibSamplesRequest(AbstractModel):
    """DescribeLibSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 单页条数，最大为100条
        :type Limit: int
        :param Offset: 条数偏移量
        :type Offset: int
        :param LibID: 词库ID
        :type LibID: str
        :param Content: 词内容过滤
        :type Content: str
        :param EvilTypeList: 违规类型列表过滤
        :type EvilTypeList: list of int
        """
        self.Limit = None
        self.Offset = None
        self.LibID = None
        self.Content = None
        self.EvilTypeList = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.LibID = params.get("LibID")
        self.Content = params.get("Content")
        self.EvilTypeList = params.get("EvilTypeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLibSamplesResponse(AbstractModel):
    """DescribeLibSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 词记录数
        :type TotalCount: int
        :param Infos: 词详情
        :type Infos: list of UserKeywordInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = UserKeywordInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DetailResult(AbstractModel):
    """文本返回的详细结果

    """

    def __init__(self):
        r"""
        :param Keywords: 该标签下命中的关键词
        :type Keywords: list of str
        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂
20105：广告引流 
24001：暴恐
        :type EvilType: int
        :param Score: 该标签模型命中的分值
        :type Score: int
        :param EvilLabel: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义关键词
        :type EvilLabel: str
        """
        self.Keywords = None
        self.EvilType = None
        self.Score = None
        self.EvilLabel = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.EvilType = params.get("EvilType")
        self.Score = params.get("Score")
        self.EvilLabel = params.get("EvilLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param IDFV: IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）
        :type IDFV: str
        :param TokenId: 设备指纹Token
        :type TokenId: str
        :param IP: 用户IP
        :type IP: str
        :param Mac: Mac地址
        :type Mac: str
        :param IDFA: IOS设备，Identifier For Advertising（广告标识符）
        :type IDFA: str
        :param DeviceId: 设备指纹ID
        :type DeviceId: str
        :param IMEI: 设备序列号
        :type IMEI: str
        """
        self.IDFV = None
        self.TokenId = None
        self.IP = None
        self.Mac = None
        self.IDFA = None
        self.DeviceId = None
        self.IMEI = None


    def _deserialize(self, params):
        self.IDFV = params.get("IDFV")
        self.TokenId = params.get("TokenId")
        self.IP = params.get("IP")
        self.Mac = params.get("Mac")
        self.IDFA = params.get("IDFA")
        self.DeviceId = params.get("DeviceId")
        self.IMEI = params.get("IMEI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """入参过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 查询字段
        :type Name: str
        :param Values: 查询值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageData(AbstractModel):
    """图片识别结果详情

    """

    def __init__(self):
        r"""
        :param EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
20103：性感
24001：暴恐
        :type EvilType: int
        :param HotDetect: 图片性感详情
注意：此字段可能返回 null，表示取不到有效值。
        :type HotDetect: :class:`tencentcloud.cms.v20190321.models.ImageHotDetect`
        :param EvilFlag: 是否恶意 0：正常 1：可疑
        :type EvilFlag: int
        :param CodeDetect: 图片二维码详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDetect: :class:`tencentcloud.cms.v20190321.models.CodeDetect`
        :param PolityDetect: 图片涉政详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PolityDetect: :class:`tencentcloud.cms.v20190321.models.ImagePolityDetect`
        :param IllegalDetect: 图片违法详情
注意：此字段可能返回 null，表示取不到有效值。
        :type IllegalDetect: :class:`tencentcloud.cms.v20190321.models.ImageIllegalDetect`
        :param PornDetect: 图片涉黄详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PornDetect: :class:`tencentcloud.cms.v20190321.models.ImagePornDetect`
        :param TerrorDetect: 图片暴恐详情
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorDetect: :class:`tencentcloud.cms.v20190321.models.ImageTerrorDetect`
        :param OCRDetect: 图片OCR详情
注意：此字段可能返回 null，表示取不到有效值。
        :type OCRDetect: :class:`tencentcloud.cms.v20190321.models.OCRDetect`
        :param LogoDetect: logo详情
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoDetect: :class:`tencentcloud.cms.v20190321.models.LogoDetail`
        :param Similar: 图片相似度详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Similar: :class:`tencentcloud.cms.v20190321.models.Similar`
        :param PhoneDetect: 手机检测详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneDetect: :class:`tencentcloud.cms.v20190321.models.PhoneDetect`
        """
        self.EvilType = None
        self.HotDetect = None
        self.EvilFlag = None
        self.CodeDetect = None
        self.PolityDetect = None
        self.IllegalDetect = None
        self.PornDetect = None
        self.TerrorDetect = None
        self.OCRDetect = None
        self.LogoDetect = None
        self.Similar = None
        self.PhoneDetect = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        if params.get("HotDetect") is not None:
            self.HotDetect = ImageHotDetect()
            self.HotDetect._deserialize(params.get("HotDetect"))
        self.EvilFlag = params.get("EvilFlag")
        if params.get("CodeDetect") is not None:
            self.CodeDetect = CodeDetect()
            self.CodeDetect._deserialize(params.get("CodeDetect"))
        if params.get("PolityDetect") is not None:
            self.PolityDetect = ImagePolityDetect()
            self.PolityDetect._deserialize(params.get("PolityDetect"))
        if params.get("IllegalDetect") is not None:
            self.IllegalDetect = ImageIllegalDetect()
            self.IllegalDetect._deserialize(params.get("IllegalDetect"))
        if params.get("PornDetect") is not None:
            self.PornDetect = ImagePornDetect()
            self.PornDetect._deserialize(params.get("PornDetect"))
        if params.get("TerrorDetect") is not None:
            self.TerrorDetect = ImageTerrorDetect()
            self.TerrorDetect._deserialize(params.get("TerrorDetect"))
        if params.get("OCRDetect") is not None:
            self.OCRDetect = OCRDetect()
            self.OCRDetect._deserialize(params.get("OCRDetect"))
        if params.get("LogoDetect") is not None:
            self.LogoDetect = LogoDetail()
            self.LogoDetect._deserialize(params.get("LogoDetect"))
        if params.get("Similar") is not None:
            self.Similar = Similar()
            self.Similar._deserialize(params.get("Similar"))
        if params.get("PhoneDetect") is not None:
            self.PhoneDetect = PhoneDetect()
            self.PhoneDetect._deserialize(params.get("PhoneDetect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageHotDetect(AbstractModel):
    """图片性感详情

    """

    def __init__(self):
        r"""
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param EvilType: 恶意类型
100：正常
20103：性感
        :type EvilType: int
        :param Labels: 性感标签：性感特征中文描述
        :type Labels: list of str
        :param Score: 性感分：分值范围 0-100，分数越高性感倾向越明显
        :type Score: int
        :param HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        """
        self.Keywords = None
        self.EvilType = None
        self.Labels = None
        self.Score = None
        self.HitFlag = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.EvilType = params.get("EvilType")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        self.HitFlag = params.get("HitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageIllegalDetect(AbstractModel):
    """图片违法详情

    """

    def __init__(self):
        r"""
        :param EvilType: 恶意类型
100：正常 
20006：涉毒违法
        :type EvilType: int
        :param HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param Labels: 违法标签：返回违法特征中文描述，如赌桌，枪支
        :type Labels: list of str
        :param Score: 违法分：分值范围 0-100，分数越高违法倾向越明显
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrl: 文件地址
        :type FileUrl: str
        :param FileMD5: 文件MD5值
        :type FileMD5: str
        :param FileContent: 文件内容 Base64,与FileUrl必须二填一
        :type FileContent: str
        """
        self.FileUrl = None
        self.FileMD5 = None
        self.FileContent = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.FileMD5 = params.get("FileMD5")
        self.FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessCode: 业务返回码
        :type BusinessCode: int
        :param Data: 识别结果
        :type Data: :class:`tencentcloud.cms.v20190321.models.ImageData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCode = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        if params.get("Data") is not None:
            self.Data = ImageData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ImagePolityDetect(AbstractModel):
    """图片涉政详情

    """

    def __init__(self):
        r"""
        :param EvilType: 恶意类型
100：正常 
20001：政治
        :type EvilType: int
        :param HitFlag: 处置判定  0：正常 1：可疑
        :type HitFlag: int
        :param FaceNames: 命中的人脸名称
        :type FaceNames: list of str
        :param PolityLogoDetail: 命中的logo标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PolityLogoDetail: list of Logo
        :param PolityItems: 命中的政治物品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PolityItems: list of str
        :param Score: 政治（人脸）分：分值范围 0-100，分数越高可疑程度越高
        :type Score: int
        :param Keywords: 关键词明细
        :type Keywords: list of str
        """
        self.EvilType = None
        self.HitFlag = None
        self.FaceNames = None
        self.PolityLogoDetail = None
        self.PolityItems = None
        self.Score = None
        self.Keywords = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.FaceNames = params.get("FaceNames")
        if params.get("PolityLogoDetail") is not None:
            self.PolityLogoDetail = []
            for item in params.get("PolityLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self.PolityLogoDetail.append(obj)
        self.PolityItems = params.get("PolityItems")
        self.Score = params.get("Score")
        self.Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImagePornDetect(AbstractModel):
    """图片涉黄详情

    """

    def __init__(self):
        r"""
        :param EvilType: 恶意类型
100：正常
20002：色情
        :type EvilType: int
        :param HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param Labels: 色情标签：色情特征中文描述
        :type Labels: list of str
        :param Score: 色情分：分值范围 0-100，分数越高色情倾向越明显
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTerrorDetect(AbstractModel):
    """图片暴恐详情

    """

    def __init__(self):
        r"""
        :param Keywords: 关键词明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param EvilType: 恶意类型
100：正常
24001：暴恐
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilType: int
        :param Labels: 暴恐标签：返回暴恐特征中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param Score: 暴恐分：分值范围0--100，分数越高暴恐倾向越明显
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param HitFlag: 处置判定 0：正常 1：可疑
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        """
        self.Keywords = None
        self.EvilType = None
        self.Labels = None
        self.Score = None
        self.HitFlag = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.EvilType = params.get("EvilType")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        self.HitFlag = params.get("HitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvalidSample(AbstractModel):
    """无效关键词

    """

    def __init__(self):
        r"""
        :param Content: 关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param InvalidCode: 无效代码:1-标签不存在;2-词过长;3-词类型不匹配;4-备注超长
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidCode: int
        :param InvalidMessage: 无效描述
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidMessage: str
        """
        self.Content = None
        self.InvalidCode = None
        self.InvalidMessage = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.InvalidCode = params.get("InvalidCode")
        self.InvalidMessage = params.get("InvalidMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordsLibInfo(AbstractModel):
    """关键词库信息

    """

    def __init__(self):
        r"""
        :param ID: 关键词库ID
        :type ID: str
        :param LibName: 关键词库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Describe: 关键词库描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param CreateTime: 关键词库创建时间
        :type CreateTime: str
        :param Suggestion: 审核建议(Review/Block)
        :type Suggestion: str
        :param MatchType: 匹配模式(ExactMatch/FuzzyMatch)
        :type MatchType: str
        :param BizTypes: 关联策略BizType列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BizTypes: list of str
        """
        self.ID = None
        self.LibName = None
        self.Describe = None
        self.CreateTime = None
        self.Suggestion = None
        self.MatchType = None
        self.BizTypes = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.LibName = params.get("LibName")
        self.Describe = params.get("Describe")
        self.CreateTime = params.get("CreateTime")
        self.Suggestion = params.get("Suggestion")
        self.MatchType = params.get("MatchType")
        self.BizTypes = params.get("BizTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Logo(AbstractModel):
    """Logo审核结果

    """

    def __init__(self):
        r"""
        :param Confidence: logo图标置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param RrectF: logo图标坐标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RrectF: :class:`tencentcloud.cms.v20190321.models.RrectF`
        :param Name: logo图标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Confidence = None
        self.RrectF = None
        self.Name = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        if params.get("RrectF") is not None:
            self.RrectF = RrectF()
            self.RrectF._deserialize(params.get("RrectF"))
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoDetail(AbstractModel):
    """Logo命中详情

    """

    def __init__(self):
        r"""
        :param AppLogoDetail: 命中的Applogo详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AppLogoDetail: list of Logo
        """
        self.AppLogoDetail = None


    def _deserialize(self, params):
        if params.get("AppLogoDetail") is not None:
            self.AppLogoDetail = []
            for item in params.get("AppLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self.AppLogoDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OCRDetect(AbstractModel):
    """OCR识别结果详情

    """

    def __init__(self):
        r"""
        :param Item: 识别到的详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: list of OCRItem
        :param TextInfo: 识别到的文本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextInfo: str
        """
        self.Item = None
        self.TextInfo = None


    def _deserialize(self, params):
        if params.get("Item") is not None:
            self.Item = []
            for item in params.get("Item"):
                obj = OCRItem()
                obj._deserialize(item)
                self.Item.append(obj)
        self.TextInfo = params.get("TextInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OCRItem(AbstractModel):
    """OCR详情

    """

    def __init__(self):
        r"""
        :param TextPosition: 检测到的文本坐标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextPosition: :class:`tencentcloud.cms.v20190321.models.Coordinate`
        :param EvilType: 文本命中恶意违规类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilType: int
        :param TextContent: 检测到的文本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextContent: str
        :param Rate: 文本涉嫌违规分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Rate: int
        :param EvilLabel: 文本命中具体标签
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilLabel: str
        :param Keywords: 文本命中违规的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        """
        self.TextPosition = None
        self.EvilType = None
        self.TextContent = None
        self.Rate = None
        self.EvilLabel = None
        self.Keywords = None


    def _deserialize(self, params):
        if params.get("TextPosition") is not None:
            self.TextPosition = Coordinate()
            self.TextPosition._deserialize(params.get("TextPosition"))
        self.EvilType = params.get("EvilType")
        self.TextContent = params.get("TextContent")
        self.Rate = params.get("Rate")
        self.EvilLabel = params.get("EvilLabel")
        self.Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneDetect(AbstractModel):
    """手机模型识别检测

    """

    def __init__(self):
        r"""
        :param EvilType: 恶意类型
100：正常
21000：综合
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilType: int
        :param Labels: 特征中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param Score: 分值范围 0-100，分数越高倾向越明显
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param HitFlag: 处置判定 0：正常 1：可疑
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        """
        self.EvilType = None
        self.Labels = None
        self.Score = None
        self.HitFlag = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        self.HitFlag = params.get("HitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetails(AbstractModel):
    """账号风险检测结果

    """

    def __init__(self):
        r"""
        :param Keywords: 预留字段，暂时不使用
        :type Keywords: list of str
        :param Lable: 预留字段，暂时不用
        :type Lable: str
        :param Label: 风险类别，RiskAccount，RiskIP, RiskIMEI
        :type Label: str
        :param Level: 风险等级，1:疑似，2：恶意
        :type Level: int
        """
        self.Keywords = None
        self.Lable = None
        self.Label = None
        self.Level = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.Lable = params.get("Lable")
        self.Label = params.get("Label")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RrectF(AbstractModel):
    """logo位置信息

    """

    def __init__(self):
        r"""
        :param Width: logo图标宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: float
        :param Cy: logo纵坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cy: float
        :param Cx: logo横坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cx: float
        :param Rotate: logo图标中心旋转度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: float
        :param Height: logo图标高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: float
        """
        self.Width = None
        self.Cy = None
        self.Cx = None
        self.Rotate = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Cy = params.get("Cy")
        self.Cx = params.get("Cx")
        self.Rotate = params.get("Rotate")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Similar(AbstractModel):
    """相似度详情

    """

    def __init__(self):
        r"""
        :param EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
        :type EvilType: int
        :param HitFlag: 处置判定 0：未匹配到 1：恶意 2：白样本
        :type HitFlag: int
        :param SeedUrl: 返回的种子url
注意：此字段可能返回 null，表示取不到有效值。
        :type SeedUrl: str
        """
        self.EvilType = None
        self.HitFlag = None
        self.SeedUrl = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.SeedUrl = params.get("SeedUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextData(AbstractModel):
    """文本识别结果详情

    """

    def __init__(self):
        r"""
        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂
20105：广告引流 
24001：暴恐
        :type EvilType: int
        :param EvilFlag: 是否恶意 0：正常 1：可疑
        :type EvilFlag: int
        :param DataId: 和请求中的DataId一致，原样返回
        :type DataId: str
        :param Extra: 输出的其他信息，不同客户内容不同
        :type Extra: str
        :param BizType: 最终使用的BizType
        :type BizType: int
        :param Res: 消息类输出结果
        :type Res: :class:`tencentcloud.cms.v20190321.models.TextOutputRes`
        :param RiskDetails: 账号风险检测结果
        :type RiskDetails: list of RiskDetails
        :param ID: 消息类ID信息
        :type ID: :class:`tencentcloud.cms.v20190321.models.TextOutputID`
        :param Score: 命中的模型分值
        :type Score: int
        :param Common: 消息类公共相关参数
        :type Common: :class:`tencentcloud.cms.v20190321.models.TextOutputComm`
        :param Suggestion: 建议值,Block：打击,Review：待复审,Normal：正常
        :type Suggestion: str
        :param Keywords: 命中的关键词
        :type Keywords: list of str
        :param DetailResult: 返回的详细结果
        :type DetailResult: list of DetailResult
        :param CustomResult: 返回的自定义词库结果
        :type CustomResult: list of CustomResult
        :param EvilLabel: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义关键词
        :type EvilLabel: str
        """
        self.EvilType = None
        self.EvilFlag = None
        self.DataId = None
        self.Extra = None
        self.BizType = None
        self.Res = None
        self.RiskDetails = None
        self.ID = None
        self.Score = None
        self.Common = None
        self.Suggestion = None
        self.Keywords = None
        self.DetailResult = None
        self.CustomResult = None
        self.EvilLabel = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.EvilFlag = params.get("EvilFlag")
        self.DataId = params.get("DataId")
        self.Extra = params.get("Extra")
        self.BizType = params.get("BizType")
        if params.get("Res") is not None:
            self.Res = TextOutputRes()
            self.Res._deserialize(params.get("Res"))
        if params.get("RiskDetails") is not None:
            self.RiskDetails = []
            for item in params.get("RiskDetails"):
                obj = RiskDetails()
                obj._deserialize(item)
                self.RiskDetails.append(obj)
        if params.get("ID") is not None:
            self.ID = TextOutputID()
            self.ID._deserialize(params.get("ID"))
        self.Score = params.get("Score")
        if params.get("Common") is not None:
            self.Common = TextOutputComm()
            self.Common._deserialize(params.get("Common"))
        self.Suggestion = params.get("Suggestion")
        self.Keywords = params.get("Keywords")
        if params.get("DetailResult") is not None:
            self.DetailResult = []
            for item in params.get("DetailResult"):
                obj = DetailResult()
                obj._deserialize(item)
                self.DetailResult.append(obj)
        if params.get("CustomResult") is not None:
            self.CustomResult = []
            for item in params.get("CustomResult"):
                obj = CustomResult()
                obj._deserialize(item)
                self.CustomResult.append(obj)
        self.EvilLabel = params.get("EvilLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationRequest(AbstractModel):
    """TextModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param Content: 文本内容Base64编码。原文长度需小于15000字节，即5000个汉字以内。
        :type Content: str
        :param DataId: 数据ID，英文字母、下划线、-组成，不超过64个字符
        :type DataId: str
        :param BizType: 该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略
        :type BizType: int
        :param User: 用户相关信息
        :type User: :class:`tencentcloud.cms.v20190321.models.User`
        :param SdkAppId: 业务应用ID
        :type SdkAppId: int
        :param Device: 设备相关信息
        :type Device: :class:`tencentcloud.cms.v20190321.models.Device`
        """
        self.Content = None
        self.DataId = None
        self.BizType = None
        self.User = None
        self.SdkAppId = None
        self.Device = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.DataId = params.get("DataId")
        self.BizType = params.get("BizType")
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationResponse(AbstractModel):
    """TextModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessCode: 业务返回码
        :type BusinessCode: int
        :param Data: 识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cms.v20190321.models.TextData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCode = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        if params.get("Data") is not None:
            self.Data = TextData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class TextOutputComm(AbstractModel):
    """消息类输出公共参数

    """

    def __init__(self):
        r"""
        :param BUCtrlID: 接口唯一ID，旁路调用接口返回有该字段，标识唯一接口
        :type BUCtrlID: int
        :param SendTime: 消息发送时间
        :type SendTime: int
        :param AppID: 接入业务的唯一ID
        :type AppID: int
        :param Uin: 请求字段里的Common.Uin
        :type Uin: int
        """
        self.BUCtrlID = None
        self.SendTime = None
        self.AppID = None
        self.Uin = None


    def _deserialize(self, params):
        self.BUCtrlID = params.get("BUCtrlID")
        self.SendTime = params.get("SendTime")
        self.AppID = params.get("AppID")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextOutputID(AbstractModel):
    """消息类输出ID参数

    """

    def __init__(self):
        r"""
        :param MsgID: 接入业务的唯一ID
        :type MsgID: str
        :param Uin: 用户账号uin，对应请求协议里的Content.User.Uin。旁路结果有回带，串联结果无该字段
        :type Uin: str
        """
        self.MsgID = None
        self.Uin = None


    def _deserialize(self, params):
        self.MsgID = params.get("MsgID")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextOutputRes(AbstractModel):
    """消息类输出结果参数

    """

    def __init__(self):
        r"""
        :param Operator: 操作人,信安处理人企业微信ID
        :type Operator: str
        :param ResultType: 恶意类型，广告（10001）， 政治（20001）， 色情（20002）， 社会事件（20004）， 暴力（20011）， 低俗（20012）， 违法犯罪（20006）， 欺诈（20008）， 版权（20013）， 谣言（20104）， 其他（21000）
        :type ResultType: int
        :param ResultCode: 恶意操作码，
删除（1）， 通过（2）， 先审后发（100012）
        :type ResultCode: int
        :param ResultMsg: 操作结果备注说明
        :type ResultMsg: str
        """
        self.Operator = None
        self.ResultType = None
        self.ResultCode = None
        self.ResultMsg = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.ResultType = params.get("ResultType")
        self.ResultCode = params.get("ResultCode")
        self.ResultMsg = params.get("ResultMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户相关信息

    """

    def __init__(self):
        r"""
        :param Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param Age: 年龄 默认0 未知
        :type Age: int
        :param UserId: 用户账号ID，如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param Phone: 手机号
        :type Phone: str
        :param AccountType: 账号类别，"1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :type AccountType: int
        :param Nickname: 用户昵称
        :type Nickname: str
        """
        self.Level = None
        self.Gender = None
        self.Age = None
        self.UserId = None
        self.Phone = None
        self.AccountType = None
        self.Nickname = None


    def _deserialize(self, params):
        self.Level = params.get("Level")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.UserId = params.get("UserId")
        self.Phone = params.get("Phone")
        self.AccountType = params.get("AccountType")
        self.Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserKeyword(AbstractModel):
    """添加关键词。

    """

    def __init__(self):
        r"""
        :param Content: 关键词内容：最多40个字符，并且符合词类型的规则
        :type Content: str
        :param Label: 关键词类型，取值范围为："Normal","Polity","Porn","Ad","Illegal","Abuse","Terror","Spam"
        :type Label: str
        :param Remark: 关键词备注：最多100个字符。
        :type Remark: str
        :param WordType: 词类型：Default,Pinyin,English,CompoundWord,ExclusionWord,AffixWord
        :type WordType: str
        """
        self.Content = None
        self.Label = None
        self.Remark = None
        self.WordType = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Label = params.get("Label")
        self.Remark = params.get("Remark")
        self.WordType = params.get("WordType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserKeywordInfo(AbstractModel):
    """关键词信息

    """

    def __init__(self):
        r"""
        :param ID: 关键词条ID
        :type ID: str
        :param Content: 关键词内容
        :type Content: str
        :param Label: 关键词标签；取值范围为："Normal","Polity","Porn","Sexy","Ad","Illegal","Abuse","Terror","Spam","Moan"
        :type Label: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param WordType: 词类型：Default,Pinyin,English,CompoundWord,ExclusionWord,AffixWord
注意：此字段可能返回 null，表示取不到有效值。
        :type WordType: str
        """
        self.ID = None
        self.Content = None
        self.Label = None
        self.CreateTime = None
        self.Remark = None
        self.WordType = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Content = params.get("Content")
        self.Label = params.get("Label")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")
        self.WordType = params.get("WordType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        