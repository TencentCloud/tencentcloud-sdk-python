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
        :param _StrCharset: 二维码文本的编码格式
注意：此字段可能返回 null，表示取不到有效值。
        :type StrCharset: str
        :param _QrCodePosition: 二维码在图片中的位置，由边界点的坐标表示
注意：此字段可能返回 null，表示取不到有效值。
        :type QrCodePosition: list of CodePosition
        :param _StrQrCodeText: 二维码的文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type StrQrCodeText: str
        :param _Uint32QrCodeType: 二维码的类型：1:ONED_BARCODE，2:QRCOD，3:WXCODE，4:PDF417，5:DATAMATRIX
注意：此字段可能返回 null，表示取不到有效值。
        :type Uint32QrCodeType: int
        :param _CodeCharset: 二维码文本的编码格式（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeCharset: str
        :param _CodePosition: 二维码在图片中的位置，由边界点的坐标表示（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodePosition: list of CodePosition
        :param _CodeText: 二维码的文本内容（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeText: str
        :param _CodeType: 二维码的类型：1:ONED_BARCODE，2:QRCOD，3:WXCODE，4:PDF417，5:DATAMATRIX（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: int
        """
        self._StrCharset = None
        self._QrCodePosition = None
        self._StrQrCodeText = None
        self._Uint32QrCodeType = None
        self._CodeCharset = None
        self._CodePosition = None
        self._CodeText = None
        self._CodeType = None

    @property
    def StrCharset(self):
        return self._StrCharset

    @StrCharset.setter
    def StrCharset(self, StrCharset):
        self._StrCharset = StrCharset

    @property
    def QrCodePosition(self):
        return self._QrCodePosition

    @QrCodePosition.setter
    def QrCodePosition(self, QrCodePosition):
        self._QrCodePosition = QrCodePosition

    @property
    def StrQrCodeText(self):
        return self._StrQrCodeText

    @StrQrCodeText.setter
    def StrQrCodeText(self, StrQrCodeText):
        self._StrQrCodeText = StrQrCodeText

    @property
    def Uint32QrCodeType(self):
        return self._Uint32QrCodeType

    @Uint32QrCodeType.setter
    def Uint32QrCodeType(self, Uint32QrCodeType):
        self._Uint32QrCodeType = Uint32QrCodeType

    @property
    def CodeCharset(self):
        return self._CodeCharset

    @CodeCharset.setter
    def CodeCharset(self, CodeCharset):
        self._CodeCharset = CodeCharset

    @property
    def CodePosition(self):
        return self._CodePosition

    @CodePosition.setter
    def CodePosition(self, CodePosition):
        self._CodePosition = CodePosition

    @property
    def CodeText(self):
        return self._CodeText

    @CodeText.setter
    def CodeText(self, CodeText):
        self._CodeText = CodeText

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType


    def _deserialize(self, params):
        self._StrCharset = params.get("StrCharset")
        if params.get("QrCodePosition") is not None:
            self._QrCodePosition = []
            for item in params.get("QrCodePosition"):
                obj = CodePosition()
                obj._deserialize(item)
                self._QrCodePosition.append(obj)
        self._StrQrCodeText = params.get("StrQrCodeText")
        self._Uint32QrCodeType = params.get("Uint32QrCodeType")
        self._CodeCharset = params.get("CodeCharset")
        if params.get("CodePosition") is not None:
            self._CodePosition = []
            for item in params.get("CodePosition"):
                obj = CodePosition()
                obj._deserialize(item)
                self._CodePosition.append(obj)
        self._CodeText = params.get("CodeText")
        self._CodeType = params.get("CodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeDetect(AbstractModel):
    """图片二维码详情

    """

    def __init__(self):
        r"""
        :param _ModerationCode: 检测是否成功，0：成功，-1：出错
注意：此字段可能返回 null，表示取不到有效值。
        :type ModerationCode: int
        :param _ModerationDetail: 从图片中检测到的二维码，可能为多个
注意：此字段可能返回 null，表示取不到有效值。
        :type ModerationDetail: list of CodeDetail
        """
        self._ModerationCode = None
        self._ModerationDetail = None

    @property
    def ModerationCode(self):
        return self._ModerationCode

    @ModerationCode.setter
    def ModerationCode(self, ModerationCode):
        self._ModerationCode = ModerationCode

    @property
    def ModerationDetail(self):
        return self._ModerationDetail

    @ModerationDetail.setter
    def ModerationDetail(self, ModerationDetail):
        self._ModerationDetail = ModerationDetail


    def _deserialize(self, params):
        self._ModerationCode = params.get("ModerationCode")
        if params.get("ModerationDetail") is not None:
            self._ModerationDetail = []
            for item in params.get("ModerationDetail"):
                obj = CodeDetail()
                obj._deserialize(item)
                self._ModerationDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodePosition(AbstractModel):
    """二维码在图片中的位置，由边界点的坐标表示

    """

    def __init__(self):
        r"""
        :param _FloatX: 二维码边界点X轴坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type FloatX: float
        :param _FloatY: 二维码边界点Y轴坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type FloatY: float
        """
        self._FloatX = None
        self._FloatY = None

    @property
    def FloatX(self):
        return self._FloatX

    @FloatX.setter
    def FloatX(self, FloatX):
        self._FloatX = FloatX

    @property
    def FloatY(self):
        return self._FloatY

    @FloatY.setter
    def FloatY(self, FloatY):
        self._FloatY = FloatY


    def _deserialize(self, params):
        self._FloatX = params.get("FloatX")
        self._FloatY = params.get("FloatY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param _Width: 宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Cy: 左上角纵坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cy: int
        :param _Cx: 左上角横坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cx: int
        :param _Height: 高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self._Width = None
        self._Cy = None
        self._Cx = None
        self._Height = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Cy(self):
        return self._Cy

    @Cy.setter
    def Cy(self, Cy):
        self._Cy = Cy

    @property
    def Cx(self):
        return self._Cx

    @Cx.setter
    def Cx(self, Cx):
        self._Cx = Cx

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Cy = params.get("Cy")
        self._Cx = params.get("Cx")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeywordsSamplesRequest(AbstractModel):
    """CreateKeywordsSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserKeywords: 关键词库信息：单次限制写入2000个，词库总容量不可超过10000个。
        :type UserKeywords: list of UserKeyword
        :param _LibID: 词库ID
        :type LibID: str
        """
        self._UserKeywords = None
        self._LibID = None

    @property
    def UserKeywords(self):
        return self._UserKeywords

    @UserKeywords.setter
    def UserKeywords(self, UserKeywords):
        self._UserKeywords = UserKeywords

    @property
    def LibID(self):
        return self._LibID

    @LibID.setter
    def LibID(self, LibID):
        self._LibID = LibID


    def _deserialize(self, params):
        if params.get("UserKeywords") is not None:
            self._UserKeywords = []
            for item in params.get("UserKeywords"):
                obj = UserKeyword()
                obj._deserialize(item)
                self._UserKeywords.append(obj)
        self._LibID = params.get("LibID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeywordsSamplesResponse(AbstractModel):
    """CreateKeywordsSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SampleIDs: 添加成功的关键词ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleIDs: list of str
        :param _DupInfos: 重复关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DupInfos: list of UserKeywordInfo
        :param _InvalidSamples: 无效关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidSamples: list of InvalidSample
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SampleIDs = None
        self._DupInfos = None
        self._InvalidSamples = None
        self._RequestId = None

    @property
    def SampleIDs(self):
        return self._SampleIDs

    @SampleIDs.setter
    def SampleIDs(self, SampleIDs):
        self._SampleIDs = SampleIDs

    @property
    def DupInfos(self):
        return self._DupInfos

    @DupInfos.setter
    def DupInfos(self, DupInfos):
        self._DupInfos = DupInfos

    @property
    def InvalidSamples(self):
        return self._InvalidSamples

    @InvalidSamples.setter
    def InvalidSamples(self, InvalidSamples):
        self._InvalidSamples = InvalidSamples

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SampleIDs = params.get("SampleIDs")
        if params.get("DupInfos") is not None:
            self._DupInfos = []
            for item in params.get("DupInfos"):
                obj = UserKeywordInfo()
                obj._deserialize(item)
                self._DupInfos.append(obj)
        if params.get("InvalidSamples") is not None:
            self._InvalidSamples = []
            for item in params.get("InvalidSamples"):
                obj = InvalidSample()
                obj._deserialize(item)
                self._InvalidSamples.append(obj)
        self._RequestId = params.get("RequestId")


class CustomResult(AbstractModel):
    """文本返回的自定义词库结果

    """

    def __init__(self):
        r"""
        :param _Keywords: 命中的自定义关键词
        :type Keywords: list of str
        :param _LibName: 自定义词库名称
        :type LibName: str
        :param _LibId: 自定义库id
        :type LibId: str
        :param _Type: 命中的自定义关键词的类型
        :type Type: str
        """
        self._Keywords = None
        self._LibName = None
        self._LibId = None
        self._Type = None

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Keywords = params.get("Keywords")
        self._LibName = params.get("LibName")
        self._LibId = params.get("LibId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLibSamplesRequest(AbstractModel):
    """DeleteLibSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SampleIDs: 关键词ID
        :type SampleIDs: list of str
        :param _LibID: 词库ID
        :type LibID: str
        """
        self._SampleIDs = None
        self._LibID = None

    @property
    def SampleIDs(self):
        return self._SampleIDs

    @SampleIDs.setter
    def SampleIDs(self, SampleIDs):
        self._SampleIDs = SampleIDs

    @property
    def LibID(self):
        return self._LibID

    @LibID.setter
    def LibID(self, LibID):
        self._LibID = LibID


    def _deserialize(self, params):
        self._SampleIDs = params.get("SampleIDs")
        self._LibID = params.get("LibID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLibSamplesResponse(AbstractModel):
    """DeleteLibSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 删除成功的数量
        :type Count: int
        :param _Details: 每个关键词删除的结果
        :type Details: list of DeleteSampleDetails
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._Details = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = DeleteSampleDetails()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteSampleDetails(AbstractModel):
    """词库关键词删除结果详情

    """

    def __init__(self):
        r"""
        :param _SampleID: 关键词ID
        :type SampleID: str
        :param _Content: 关键词内容
        :type Content: str
        :param _Deleted: 是否删除成功
        :type Deleted: bool
        :param _ErrorInfo: 错误信息
        :type ErrorInfo: str
        """
        self._SampleID = None
        self._Content = None
        self._Deleted = None
        self._ErrorInfo = None

    @property
    def SampleID(self):
        return self._SampleID

    @SampleID.setter
    def SampleID(self, SampleID):
        self._SampleID = SampleID

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Deleted(self):
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo


    def _deserialize(self, params):
        self._SampleID = params.get("SampleID")
        self._Content = params.get("Content")
        self._Deleted = params.get("Deleted")
        self._ErrorInfo = params.get("ErrorInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeywordsLibsRequest(AbstractModel):
    """DescribeKeywordsLibs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 单页条数，最大为100条
        :type Limit: int
        :param _Offset: 条数偏移量
        :type Offset: int
        :param _Filters: 过滤器(支持LibName模糊查询,CustomLibIDs词库id列表过滤)
        :type Filters: list of Filters
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeywordsLibsResponse(AbstractModel):
    """DescribeKeywordsLibs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 词库记录数
        :type TotalCount: int
        :param _Infos: 词库详情
        :type Infos: list of KeywordsLibInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Infos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = KeywordsLibInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLibSamplesRequest(AbstractModel):
    """DescribeLibSamples请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 单页条数，最大为100条
        :type Limit: int
        :param _Offset: 条数偏移量
        :type Offset: int
        :param _LibID: 词库ID
        :type LibID: str
        :param _Content: 词内容过滤
        :type Content: str
        :param _EvilTypeList: 违规类型列表过滤
        :type EvilTypeList: list of int
        """
        self._Limit = None
        self._Offset = None
        self._LibID = None
        self._Content = None
        self._EvilTypeList = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def LibID(self):
        return self._LibID

    @LibID.setter
    def LibID(self, LibID):
        self._LibID = LibID

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def EvilTypeList(self):
        return self._EvilTypeList

    @EvilTypeList.setter
    def EvilTypeList(self, EvilTypeList):
        self._EvilTypeList = EvilTypeList


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._LibID = params.get("LibID")
        self._Content = params.get("Content")
        self._EvilTypeList = params.get("EvilTypeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLibSamplesResponse(AbstractModel):
    """DescribeLibSamples返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 词记录数
        :type TotalCount: int
        :param _Infos: 词详情
        :type Infos: list of UserKeywordInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Infos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = UserKeywordInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DetailResult(AbstractModel):
    """文本返回的详细结果

    """

    def __init__(self):
        r"""
        :param _Keywords: 该标签下命中的关键词
        :type Keywords: list of str
        :param _EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂
20105：广告引流 
24001：暴恐
        :type EvilType: int
        :param _Score: 该标签模型命中的分值
        :type Score: int
        :param _EvilLabel: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义关键词
        :type EvilLabel: str
        """
        self._Keywords = None
        self._EvilType = None
        self._Score = None
        self._EvilLabel = None

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def EvilLabel(self):
        return self._EvilLabel

    @EvilLabel.setter
    def EvilLabel(self, EvilLabel):
        self._EvilLabel = EvilLabel


    def _deserialize(self, params):
        self._Keywords = params.get("Keywords")
        self._EvilType = params.get("EvilType")
        self._Score = params.get("Score")
        self._EvilLabel = params.get("EvilLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param _IDFV: IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）
        :type IDFV: str
        :param _TokenId: 设备指纹Token
        :type TokenId: str
        :param _IP: 用户IP
        :type IP: str
        :param _Mac: Mac地址
        :type Mac: str
        :param _IDFA: IOS设备，Identifier For Advertising（广告标识符）
        :type IDFA: str
        :param _DeviceId: 设备指纹ID
        :type DeviceId: str
        :param _IMEI: 设备序列号
        :type IMEI: str
        """
        self._IDFV = None
        self._TokenId = None
        self._IP = None
        self._Mac = None
        self._IDFA = None
        self._DeviceId = None
        self._IMEI = None

    @property
    def IDFV(self):
        return self._IDFV

    @IDFV.setter
    def IDFV(self, IDFV):
        self._IDFV = IDFV

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Mac(self):
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def IDFA(self):
        return self._IDFA

    @IDFA.setter
    def IDFA(self, IDFA):
        self._IDFA = IDFA

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def IMEI(self):
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI


    def _deserialize(self, params):
        self._IDFV = params.get("IDFV")
        self._TokenId = params.get("TokenId")
        self._IP = params.get("IP")
        self._Mac = params.get("Mac")
        self._IDFA = params.get("IDFA")
        self._DeviceId = params.get("DeviceId")
        self._IMEI = params.get("IMEI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """入参过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 查询字段
        :type Name: str
        :param _Values: 查询值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageData(AbstractModel):
    """图片识别结果详情

    """

    def __init__(self):
        r"""
        :param _EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
20103：性感
24001：暴恐
        :type EvilType: int
        :param _HotDetect: 图片性感详情
注意：此字段可能返回 null，表示取不到有效值。
        :type HotDetect: :class:`tencentcloud.cms.v20190321.models.ImageHotDetect`
        :param _EvilFlag: 是否恶意 0：正常 1：可疑
        :type EvilFlag: int
        :param _CodeDetect: 图片二维码详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDetect: :class:`tencentcloud.cms.v20190321.models.CodeDetect`
        :param _PolityDetect: 图片涉政详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PolityDetect: :class:`tencentcloud.cms.v20190321.models.ImagePolityDetect`
        :param _IllegalDetect: 图片违法详情
注意：此字段可能返回 null，表示取不到有效值。
        :type IllegalDetect: :class:`tencentcloud.cms.v20190321.models.ImageIllegalDetect`
        :param _PornDetect: 图片涉黄详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PornDetect: :class:`tencentcloud.cms.v20190321.models.ImagePornDetect`
        :param _TerrorDetect: 图片暴恐详情
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorDetect: :class:`tencentcloud.cms.v20190321.models.ImageTerrorDetect`
        :param _OCRDetect: 图片OCR详情
注意：此字段可能返回 null，表示取不到有效值。
        :type OCRDetect: :class:`tencentcloud.cms.v20190321.models.OCRDetect`
        :param _LogoDetect: logo详情
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoDetect: :class:`tencentcloud.cms.v20190321.models.LogoDetail`
        :param _Similar: 图片相似度详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Similar: :class:`tencentcloud.cms.v20190321.models.Similar`
        :param _PhoneDetect: 手机检测详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneDetect: :class:`tencentcloud.cms.v20190321.models.PhoneDetect`
        """
        self._EvilType = None
        self._HotDetect = None
        self._EvilFlag = None
        self._CodeDetect = None
        self._PolityDetect = None
        self._IllegalDetect = None
        self._PornDetect = None
        self._TerrorDetect = None
        self._OCRDetect = None
        self._LogoDetect = None
        self._Similar = None
        self._PhoneDetect = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def HotDetect(self):
        return self._HotDetect

    @HotDetect.setter
    def HotDetect(self, HotDetect):
        self._HotDetect = HotDetect

    @property
    def EvilFlag(self):
        return self._EvilFlag

    @EvilFlag.setter
    def EvilFlag(self, EvilFlag):
        self._EvilFlag = EvilFlag

    @property
    def CodeDetect(self):
        return self._CodeDetect

    @CodeDetect.setter
    def CodeDetect(self, CodeDetect):
        self._CodeDetect = CodeDetect

    @property
    def PolityDetect(self):
        return self._PolityDetect

    @PolityDetect.setter
    def PolityDetect(self, PolityDetect):
        self._PolityDetect = PolityDetect

    @property
    def IllegalDetect(self):
        return self._IllegalDetect

    @IllegalDetect.setter
    def IllegalDetect(self, IllegalDetect):
        self._IllegalDetect = IllegalDetect

    @property
    def PornDetect(self):
        return self._PornDetect

    @PornDetect.setter
    def PornDetect(self, PornDetect):
        self._PornDetect = PornDetect

    @property
    def TerrorDetect(self):
        return self._TerrorDetect

    @TerrorDetect.setter
    def TerrorDetect(self, TerrorDetect):
        self._TerrorDetect = TerrorDetect

    @property
    def OCRDetect(self):
        return self._OCRDetect

    @OCRDetect.setter
    def OCRDetect(self, OCRDetect):
        self._OCRDetect = OCRDetect

    @property
    def LogoDetect(self):
        return self._LogoDetect

    @LogoDetect.setter
    def LogoDetect(self, LogoDetect):
        self._LogoDetect = LogoDetect

    @property
    def Similar(self):
        return self._Similar

    @Similar.setter
    def Similar(self, Similar):
        self._Similar = Similar

    @property
    def PhoneDetect(self):
        return self._PhoneDetect

    @PhoneDetect.setter
    def PhoneDetect(self, PhoneDetect):
        self._PhoneDetect = PhoneDetect


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        if params.get("HotDetect") is not None:
            self._HotDetect = ImageHotDetect()
            self._HotDetect._deserialize(params.get("HotDetect"))
        self._EvilFlag = params.get("EvilFlag")
        if params.get("CodeDetect") is not None:
            self._CodeDetect = CodeDetect()
            self._CodeDetect._deserialize(params.get("CodeDetect"))
        if params.get("PolityDetect") is not None:
            self._PolityDetect = ImagePolityDetect()
            self._PolityDetect._deserialize(params.get("PolityDetect"))
        if params.get("IllegalDetect") is not None:
            self._IllegalDetect = ImageIllegalDetect()
            self._IllegalDetect._deserialize(params.get("IllegalDetect"))
        if params.get("PornDetect") is not None:
            self._PornDetect = ImagePornDetect()
            self._PornDetect._deserialize(params.get("PornDetect"))
        if params.get("TerrorDetect") is not None:
            self._TerrorDetect = ImageTerrorDetect()
            self._TerrorDetect._deserialize(params.get("TerrorDetect"))
        if params.get("OCRDetect") is not None:
            self._OCRDetect = OCRDetect()
            self._OCRDetect._deserialize(params.get("OCRDetect"))
        if params.get("LogoDetect") is not None:
            self._LogoDetect = LogoDetail()
            self._LogoDetect._deserialize(params.get("LogoDetect"))
        if params.get("Similar") is not None:
            self._Similar = Similar()
            self._Similar._deserialize(params.get("Similar"))
        if params.get("PhoneDetect") is not None:
            self._PhoneDetect = PhoneDetect()
            self._PhoneDetect._deserialize(params.get("PhoneDetect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageHotDetect(AbstractModel):
    """图片性感详情

    """

    def __init__(self):
        r"""
        :param _Keywords: 关键词明细
        :type Keywords: list of str
        :param _EvilType: 恶意类型
100：正常
20103：性感
        :type EvilType: int
        :param _Labels: 性感标签：性感特征中文描述
        :type Labels: list of str
        :param _Score: 性感分：分值范围 0-100，分数越高性感倾向越明显
        :type Score: int
        :param _HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        """
        self._Keywords = None
        self._EvilType = None
        self._Labels = None
        self._Score = None
        self._HitFlag = None

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag


    def _deserialize(self, params):
        self._Keywords = params.get("Keywords")
        self._EvilType = params.get("EvilType")
        self._Labels = params.get("Labels")
        self._Score = params.get("Score")
        self._HitFlag = params.get("HitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageIllegalDetect(AbstractModel):
    """图片违法详情

    """

    def __init__(self):
        r"""
        :param _EvilType: 恶意类型
100：正常 
20006：涉毒违法
        :type EvilType: int
        :param _HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param _Keywords: 关键词明细
        :type Keywords: list of str
        :param _Labels: 违法标签：返回违法特征中文描述，如赌桌，枪支
        :type Labels: list of str
        :param _Score: 违法分：分值范围 0-100，分数越高违法倾向越明显
        :type Score: int
        """
        self._EvilType = None
        self._HitFlag = None
        self._Keywords = None
        self._Labels = None
        self._Score = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._HitFlag = params.get("HitFlag")
        self._Keywords = params.get("Keywords")
        self._Labels = params.get("Labels")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileUrl: 文件地址
        :type FileUrl: str
        :param _FileMD5: 文件MD5值
        :type FileMD5: str
        :param _FileContent: 文件内容 Base64,与FileUrl必须二填一
        :type FileContent: str
        """
        self._FileUrl = None
        self._FileMD5 = None
        self._FileContent = None

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileMD5(self):
        return self._FileMD5

    @FileMD5.setter
    def FileMD5(self, FileMD5):
        self._FileMD5 = FileMD5

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._FileUrl = params.get("FileUrl")
        self._FileMD5 = params.get("FileMD5")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 业务返回码
        :type BusinessCode: int
        :param _Data: 识别结果
        :type Data: :class:`tencentcloud.cms.v20190321.models.ImageData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessCode = None
        self._Data = None
        self._RequestId = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

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
        self._BusinessCode = params.get("BusinessCode")
        if params.get("Data") is not None:
            self._Data = ImageData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ImagePolityDetect(AbstractModel):
    """图片涉政详情

    """

    def __init__(self):
        r"""
        :param _EvilType: 恶意类型
100：正常 
20001：政治
        :type EvilType: int
        :param _HitFlag: 处置判定  0：正常 1：可疑
        :type HitFlag: int
        :param _FaceNames: 命中的人脸名称
        :type FaceNames: list of str
        :param _PolityLogoDetail: 命中的logo标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PolityLogoDetail: list of Logo
        :param _PolityItems: 命中的政治物品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PolityItems: list of str
        :param _Score: 政治（人脸）分：分值范围 0-100，分数越高可疑程度越高
        :type Score: int
        :param _Keywords: 关键词明细
        :type Keywords: list of str
        """
        self._EvilType = None
        self._HitFlag = None
        self._FaceNames = None
        self._PolityLogoDetail = None
        self._PolityItems = None
        self._Score = None
        self._Keywords = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def FaceNames(self):
        return self._FaceNames

    @FaceNames.setter
    def FaceNames(self, FaceNames):
        self._FaceNames = FaceNames

    @property
    def PolityLogoDetail(self):
        return self._PolityLogoDetail

    @PolityLogoDetail.setter
    def PolityLogoDetail(self, PolityLogoDetail):
        self._PolityLogoDetail = PolityLogoDetail

    @property
    def PolityItems(self):
        return self._PolityItems

    @PolityItems.setter
    def PolityItems(self, PolityItems):
        self._PolityItems = PolityItems

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._HitFlag = params.get("HitFlag")
        self._FaceNames = params.get("FaceNames")
        if params.get("PolityLogoDetail") is not None:
            self._PolityLogoDetail = []
            for item in params.get("PolityLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self._PolityLogoDetail.append(obj)
        self._PolityItems = params.get("PolityItems")
        self._Score = params.get("Score")
        self._Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImagePornDetect(AbstractModel):
    """图片涉黄详情

    """

    def __init__(self):
        r"""
        :param _EvilType: 恶意类型
100：正常
20002：色情
        :type EvilType: int
        :param _HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param _Keywords: 关键词明细
        :type Keywords: list of str
        :param _Labels: 色情标签：色情特征中文描述
        :type Labels: list of str
        :param _Score: 色情分：分值范围 0-100，分数越高色情倾向越明显
        :type Score: int
        """
        self._EvilType = None
        self._HitFlag = None
        self._Keywords = None
        self._Labels = None
        self._Score = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._HitFlag = params.get("HitFlag")
        self._Keywords = params.get("Keywords")
        self._Labels = params.get("Labels")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTerrorDetect(AbstractModel):
    """图片暴恐详情

    """

    def __init__(self):
        r"""
        :param _Keywords: 关键词明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param _EvilType: 恶意类型
100：正常
24001：暴恐
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilType: int
        :param _Labels: 暴恐标签：返回暴恐特征中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param _Score: 暴恐分：分值范围0--100，分数越高暴恐倾向越明显
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _HitFlag: 处置判定 0：正常 1：可疑
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        """
        self._Keywords = None
        self._EvilType = None
        self._Labels = None
        self._Score = None
        self._HitFlag = None

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag


    def _deserialize(self, params):
        self._Keywords = params.get("Keywords")
        self._EvilType = params.get("EvilType")
        self._Labels = params.get("Labels")
        self._Score = params.get("Score")
        self._HitFlag = params.get("HitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvalidSample(AbstractModel):
    """无效关键词

    """

    def __init__(self):
        r"""
        :param _Content: 关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _InvalidCode: 无效代码:1-标签不存在;2-词过长;3-词类型不匹配;4-备注超长
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidCode: int
        :param _InvalidMessage: 无效描述
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidMessage: str
        """
        self._Content = None
        self._InvalidCode = None
        self._InvalidMessage = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def InvalidCode(self):
        return self._InvalidCode

    @InvalidCode.setter
    def InvalidCode(self, InvalidCode):
        self._InvalidCode = InvalidCode

    @property
    def InvalidMessage(self):
        return self._InvalidMessage

    @InvalidMessage.setter
    def InvalidMessage(self, InvalidMessage):
        self._InvalidMessage = InvalidMessage


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._InvalidCode = params.get("InvalidCode")
        self._InvalidMessage = params.get("InvalidMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordsLibInfo(AbstractModel):
    """关键词库信息

    """

    def __init__(self):
        r"""
        :param _ID: 关键词库ID
        :type ID: str
        :param _LibName: 关键词库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _Describe: 关键词库描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _CreateTime: 关键词库创建时间
        :type CreateTime: str
        :param _Suggestion: 审核建议(Review/Block)
        :type Suggestion: str
        :param _MatchType: 匹配模式(ExactMatch/FuzzyMatch)
        :type MatchType: str
        :param _BizTypes: 关联策略BizType列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BizTypes: list of str
        """
        self._ID = None
        self._LibName = None
        self._Describe = None
        self._CreateTime = None
        self._Suggestion = None
        self._MatchType = None
        self._BizTypes = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def BizTypes(self):
        return self._BizTypes

    @BizTypes.setter
    def BizTypes(self, BizTypes):
        self._BizTypes = BizTypes


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._LibName = params.get("LibName")
        self._Describe = params.get("Describe")
        self._CreateTime = params.get("CreateTime")
        self._Suggestion = params.get("Suggestion")
        self._MatchType = params.get("MatchType")
        self._BizTypes = params.get("BizTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Logo(AbstractModel):
    """Logo审核结果

    """

    def __init__(self):
        r"""
        :param _Confidence: logo图标置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _RrectF: logo图标坐标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RrectF: :class:`tencentcloud.cms.v20190321.models.RrectF`
        :param _Name: logo图标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Confidence = None
        self._RrectF = None
        self._Name = None

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def RrectF(self):
        return self._RrectF

    @RrectF.setter
    def RrectF(self, RrectF):
        self._RrectF = RrectF

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        if params.get("RrectF") is not None:
            self._RrectF = RrectF()
            self._RrectF._deserialize(params.get("RrectF"))
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoDetail(AbstractModel):
    """Logo命中详情

    """

    def __init__(self):
        r"""
        :param _AppLogoDetail: 命中的Applogo详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AppLogoDetail: list of Logo
        """
        self._AppLogoDetail = None

    @property
    def AppLogoDetail(self):
        return self._AppLogoDetail

    @AppLogoDetail.setter
    def AppLogoDetail(self, AppLogoDetail):
        self._AppLogoDetail = AppLogoDetail


    def _deserialize(self, params):
        if params.get("AppLogoDetail") is not None:
            self._AppLogoDetail = []
            for item in params.get("AppLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self._AppLogoDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OCRDetect(AbstractModel):
    """OCR识别结果详情

    """

    def __init__(self):
        r"""
        :param _Item: 识别到的详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: list of OCRItem
        :param _TextInfo: 识别到的文本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextInfo: str
        """
        self._Item = None
        self._TextInfo = None

    @property
    def Item(self):
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def TextInfo(self):
        return self._TextInfo

    @TextInfo.setter
    def TextInfo(self, TextInfo):
        self._TextInfo = TextInfo


    def _deserialize(self, params):
        if params.get("Item") is not None:
            self._Item = []
            for item in params.get("Item"):
                obj = OCRItem()
                obj._deserialize(item)
                self._Item.append(obj)
        self._TextInfo = params.get("TextInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OCRItem(AbstractModel):
    """OCR详情

    """

    def __init__(self):
        r"""
        :param _TextPosition: 检测到的文本坐标信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextPosition: :class:`tencentcloud.cms.v20190321.models.Coordinate`
        :param _EvilType: 文本命中恶意违规类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilType: int
        :param _TextContent: 检测到的文本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextContent: str
        :param _Rate: 文本涉嫌违规分值
注意：此字段可能返回 null，表示取不到有效值。
        :type Rate: int
        :param _EvilLabel: 文本命中具体标签
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilLabel: str
        :param _Keywords: 文本命中违规的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        """
        self._TextPosition = None
        self._EvilType = None
        self._TextContent = None
        self._Rate = None
        self._EvilLabel = None
        self._Keywords = None

    @property
    def TextPosition(self):
        return self._TextPosition

    @TextPosition.setter
    def TextPosition(self, TextPosition):
        self._TextPosition = TextPosition

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def TextContent(self):
        return self._TextContent

    @TextContent.setter
    def TextContent(self, TextContent):
        self._TextContent = TextContent

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def EvilLabel(self):
        return self._EvilLabel

    @EvilLabel.setter
    def EvilLabel(self, EvilLabel):
        self._EvilLabel = EvilLabel

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords


    def _deserialize(self, params):
        if params.get("TextPosition") is not None:
            self._TextPosition = Coordinate()
            self._TextPosition._deserialize(params.get("TextPosition"))
        self._EvilType = params.get("EvilType")
        self._TextContent = params.get("TextContent")
        self._Rate = params.get("Rate")
        self._EvilLabel = params.get("EvilLabel")
        self._Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneDetect(AbstractModel):
    """手机模型识别检测

    """

    def __init__(self):
        r"""
        :param _EvilType: 恶意类型
100：正常
21000：综合
注意：此字段可能返回 null，表示取不到有效值。
        :type EvilType: int
        :param _Labels: 特征中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param _Score: 分值范围 0-100，分数越高倾向越明显
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _HitFlag: 处置判定 0：正常 1：可疑
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        """
        self._EvilType = None
        self._Labels = None
        self._Score = None
        self._HitFlag = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._Labels = params.get("Labels")
        self._Score = params.get("Score")
        self._HitFlag = params.get("HitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetails(AbstractModel):
    """账号风险检测结果

    """

    def __init__(self):
        r"""
        :param _Keywords: 预留字段，暂时不使用
        :type Keywords: list of str
        :param _Lable: 预留字段，暂时不用
        :type Lable: str
        :param _Label: 风险类别，RiskAccount，RiskIP, RiskIMEI
        :type Label: str
        :param _Level: 风险等级，1:疑似，2：恶意
        :type Level: int
        """
        self._Keywords = None
        self._Lable = None
        self._Label = None
        self._Level = None

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Lable(self):
        return self._Lable

    @Lable.setter
    def Lable(self, Lable):
        self._Lable = Lable

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Keywords = params.get("Keywords")
        self._Lable = params.get("Lable")
        self._Label = params.get("Label")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RrectF(AbstractModel):
    """logo位置信息

    """

    def __init__(self):
        r"""
        :param _Width: logo图标宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: float
        :param _Cy: logo纵坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cy: float
        :param _Cx: logo横坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Cx: float
        :param _Rotate: logo图标中心旋转度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: float
        :param _Height: logo图标高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: float
        """
        self._Width = None
        self._Cy = None
        self._Cx = None
        self._Rotate = None
        self._Height = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Cy(self):
        return self._Cy

    @Cy.setter
    def Cy(self, Cy):
        self._Cy = Cy

    @property
    def Cx(self):
        return self._Cx

    @Cx.setter
    def Cx(self, Cx):
        self._Cx = Cx

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Cy = params.get("Cy")
        self._Cx = params.get("Cx")
        self._Rotate = params.get("Rotate")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Similar(AbstractModel):
    """相似度详情

    """

    def __init__(self):
        r"""
        :param _EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
        :type EvilType: int
        :param _HitFlag: 处置判定 0：未匹配到 1：恶意 2：白样本
        :type HitFlag: int
        :param _SeedUrl: 返回的种子url
注意：此字段可能返回 null，表示取不到有效值。
        :type SeedUrl: str
        """
        self._EvilType = None
        self._HitFlag = None
        self._SeedUrl = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def SeedUrl(self):
        return self._SeedUrl

    @SeedUrl.setter
    def SeedUrl(self, SeedUrl):
        self._SeedUrl = SeedUrl


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._HitFlag = params.get("HitFlag")
        self._SeedUrl = params.get("SeedUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextData(AbstractModel):
    """文本识别结果详情

    """

    def __init__(self):
        r"""
        :param _EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂
20105：广告引流 
24001：暴恐
        :type EvilType: int
        :param _EvilFlag: 是否恶意 0：正常 1：可疑
        :type EvilFlag: int
        :param _DataId: 和请求中的DataId一致，原样返回
        :type DataId: str
        :param _Extra: 输出的其他信息，不同客户内容不同
        :type Extra: str
        :param _BizType: 最终使用的BizType
        :type BizType: int
        :param _Res: 消息类输出结果
        :type Res: :class:`tencentcloud.cms.v20190321.models.TextOutputRes`
        :param _RiskDetails: 账号风险检测结果
        :type RiskDetails: list of RiskDetails
        :param _ID: 消息类ID信息
        :type ID: :class:`tencentcloud.cms.v20190321.models.TextOutputID`
        :param _Score: 命中的模型分值
        :type Score: int
        :param _Common: 消息类公共相关参数
        :type Common: :class:`tencentcloud.cms.v20190321.models.TextOutputComm`
        :param _Suggestion: 建议值,Block：打击,Review：待复审,Normal：正常
        :type Suggestion: str
        :param _Keywords: 命中的关键词
        :type Keywords: list of str
        :param _DetailResult: 返回的详细结果
        :type DetailResult: list of DetailResult
        :param _CustomResult: 返回的自定义词库结果
        :type CustomResult: list of CustomResult
        :param _EvilLabel: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义关键词
        :type EvilLabel: str
        """
        self._EvilType = None
        self._EvilFlag = None
        self._DataId = None
        self._Extra = None
        self._BizType = None
        self._Res = None
        self._RiskDetails = None
        self._ID = None
        self._Score = None
        self._Common = None
        self._Suggestion = None
        self._Keywords = None
        self._DetailResult = None
        self._CustomResult = None
        self._EvilLabel = None

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def EvilFlag(self):
        return self._EvilFlag

    @EvilFlag.setter
    def EvilFlag(self, EvilFlag):
        self._EvilFlag = EvilFlag

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Res(self):
        return self._Res

    @Res.setter
    def Res(self, Res):
        self._Res = Res

    @property
    def RiskDetails(self):
        return self._RiskDetails

    @RiskDetails.setter
    def RiskDetails(self, RiskDetails):
        self._RiskDetails = RiskDetails

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Common(self):
        return self._Common

    @Common.setter
    def Common(self, Common):
        self._Common = Common

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def DetailResult(self):
        return self._DetailResult

    @DetailResult.setter
    def DetailResult(self, DetailResult):
        self._DetailResult = DetailResult

    @property
    def CustomResult(self):
        return self._CustomResult

    @CustomResult.setter
    def CustomResult(self, CustomResult):
        self._CustomResult = CustomResult

    @property
    def EvilLabel(self):
        return self._EvilLabel

    @EvilLabel.setter
    def EvilLabel(self, EvilLabel):
        self._EvilLabel = EvilLabel


    def _deserialize(self, params):
        self._EvilType = params.get("EvilType")
        self._EvilFlag = params.get("EvilFlag")
        self._DataId = params.get("DataId")
        self._Extra = params.get("Extra")
        self._BizType = params.get("BizType")
        if params.get("Res") is not None:
            self._Res = TextOutputRes()
            self._Res._deserialize(params.get("Res"))
        if params.get("RiskDetails") is not None:
            self._RiskDetails = []
            for item in params.get("RiskDetails"):
                obj = RiskDetails()
                obj._deserialize(item)
                self._RiskDetails.append(obj)
        if params.get("ID") is not None:
            self._ID = TextOutputID()
            self._ID._deserialize(params.get("ID"))
        self._Score = params.get("Score")
        if params.get("Common") is not None:
            self._Common = TextOutputComm()
            self._Common._deserialize(params.get("Common"))
        self._Suggestion = params.get("Suggestion")
        self._Keywords = params.get("Keywords")
        if params.get("DetailResult") is not None:
            self._DetailResult = []
            for item in params.get("DetailResult"):
                obj = DetailResult()
                obj._deserialize(item)
                self._DetailResult.append(obj)
        if params.get("CustomResult") is not None:
            self._CustomResult = []
            for item in params.get("CustomResult"):
                obj = CustomResult()
                obj._deserialize(item)
                self._CustomResult.append(obj)
        self._EvilLabel = params.get("EvilLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationRequest(AbstractModel):
    """TextModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 文本内容Base64编码。原文长度需小于15000字节，即5000个汉字以内。
        :type Content: str
        :param _DataId: 数据ID，英文字母、下划线、-组成，不超过64个字符
        :type DataId: str
        :param _BizType: 该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略
        :type BizType: int
        :param _User: 用户相关信息
        :type User: :class:`tencentcloud.cms.v20190321.models.User`
        :param _SdkAppId: 业务应用ID
        :type SdkAppId: int
        :param _Device: 设备相关信息
        :type Device: :class:`tencentcloud.cms.v20190321.models.Device`
        """
        self._Content = None
        self._DataId = None
        self._BizType = None
        self._User = None
        self._SdkAppId = None
        self._Device = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._DataId = params.get("DataId")
        self._BizType = params.get("BizType")
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationResponse(AbstractModel):
    """TextModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 业务返回码
        :type BusinessCode: int
        :param _Data: 识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cms.v20190321.models.TextData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessCode = None
        self._Data = None
        self._RequestId = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

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
        self._BusinessCode = params.get("BusinessCode")
        if params.get("Data") is not None:
            self._Data = TextData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class TextOutputComm(AbstractModel):
    """消息类输出公共参数

    """

    def __init__(self):
        r"""
        :param _BUCtrlID: 接口唯一ID，旁路调用接口返回有该字段，标识唯一接口
        :type BUCtrlID: int
        :param _SendTime: 消息发送时间
        :type SendTime: int
        :param _AppID: 接入业务的唯一ID
        :type AppID: int
        :param _Uin: 请求字段里的Common.Uin
        :type Uin: int
        """
        self._BUCtrlID = None
        self._SendTime = None
        self._AppID = None
        self._Uin = None

    @property
    def BUCtrlID(self):
        return self._BUCtrlID

    @BUCtrlID.setter
    def BUCtrlID(self, BUCtrlID):
        self._BUCtrlID = BUCtrlID

    @property
    def SendTime(self):
        return self._SendTime

    @SendTime.setter
    def SendTime(self, SendTime):
        self._SendTime = SendTime

    @property
    def AppID(self):
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._BUCtrlID = params.get("BUCtrlID")
        self._SendTime = params.get("SendTime")
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextOutputID(AbstractModel):
    """消息类输出ID参数

    """

    def __init__(self):
        r"""
        :param _MsgID: 接入业务的唯一ID
        :type MsgID: str
        :param _Uin: 用户账号uin，对应请求协议里的Content.User.Uin。旁路结果有回带，串联结果无该字段
        :type Uin: str
        """
        self._MsgID = None
        self._Uin = None

    @property
    def MsgID(self):
        return self._MsgID

    @MsgID.setter
    def MsgID(self, MsgID):
        self._MsgID = MsgID

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._MsgID = params.get("MsgID")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextOutputRes(AbstractModel):
    """消息类输出结果参数

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人,信安处理人企业微信ID
        :type Operator: str
        :param _ResultType: 恶意类型，广告（10001）， 政治（20001）， 色情（20002）， 社会事件（20004）， 暴力（20011）， 低俗（20012）， 违法犯罪（20006）， 欺诈（20008）， 版权（20013）， 谣言（20104）， 其他（21000）
        :type ResultType: int
        :param _ResultCode: 恶意操作码，
删除（1）， 通过（2）， 先审后发（100012）
        :type ResultCode: int
        :param _ResultMsg: 操作结果备注说明
        :type ResultMsg: str
        """
        self._Operator = None
        self._ResultType = None
        self._ResultCode = None
        self._ResultMsg = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ResultType(self):
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultMsg(self):
        return self._ResultMsg

    @ResultMsg.setter
    def ResultMsg(self, ResultMsg):
        self._ResultMsg = ResultMsg


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        self._ResultType = params.get("ResultType")
        self._ResultCode = params.get("ResultCode")
        self._ResultMsg = params.get("ResultMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户相关信息

    """

    def __init__(self):
        r"""
        :param _Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param _Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param _Age: 年龄 默认0 未知
        :type Age: int
        :param _UserId: 用户账号ID，如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param _Phone: 手机号
        :type Phone: str
        :param _AccountType: 账号类别，"1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :type AccountType: int
        :param _Nickname: 用户昵称
        :type Nickname: str
        """
        self._Level = None
        self._Gender = None
        self._Age = None
        self._UserId = None
        self._Phone = None
        self._AccountType = None
        self._Nickname = None

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._UserId = params.get("UserId")
        self._Phone = params.get("Phone")
        self._AccountType = params.get("AccountType")
        self._Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserKeyword(AbstractModel):
    """添加关键词。

    """

    def __init__(self):
        r"""
        :param _Content: 关键词内容：最多40个字符，并且符合词类型的规则
        :type Content: str
        :param _Label: 关键词类型，取值范围为："Normal","Polity","Porn","Ad","Illegal","Abuse","Terror","Spam"
        :type Label: str
        :param _Remark: 关键词备注：最多100个字符。
        :type Remark: str
        :param _WordType: 词类型：Default,Pinyin,English,CompoundWord,ExclusionWord,AffixWord
        :type WordType: str
        """
        self._Content = None
        self._Label = None
        self._Remark = None
        self._WordType = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def WordType(self):
        return self._WordType

    @WordType.setter
    def WordType(self, WordType):
        self._WordType = WordType


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Label = params.get("Label")
        self._Remark = params.get("Remark")
        self._WordType = params.get("WordType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserKeywordInfo(AbstractModel):
    """关键词信息

    """

    def __init__(self):
        r"""
        :param _ID: 关键词条ID
        :type ID: str
        :param _Content: 关键词内容
        :type Content: str
        :param _Label: 关键词标签；取值范围为："Normal","Polity","Porn","Sexy","Ad","Illegal","Abuse","Terror","Spam","Moan"
        :type Label: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _WordType: 词类型：Default,Pinyin,English,CompoundWord,ExclusionWord,AffixWord
注意：此字段可能返回 null，表示取不到有效值。
        :type WordType: str
        """
        self._ID = None
        self._Content = None
        self._Label = None
        self._CreateTime = None
        self._Remark = None
        self._WordType = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def WordType(self):
        return self._WordType

    @WordType.setter
    def WordType(self, WordType):
        self._WordType = WordType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Content = params.get("Content")
        self._Label = params.get("Label")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        self._WordType = params.get("WordType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        