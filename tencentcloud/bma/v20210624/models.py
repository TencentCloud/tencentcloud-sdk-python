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


class BrandData(AbstractModel):
    """商标信息

    """

    def __init__(self):
        r"""
        :param _BrandName: 商标名称
        :type BrandName: str
        :param _BrandCertificateName: 商标证明
        :type BrandCertificateName: str
        :param _BrandStatus: 商标审核状态 1-审核中 2-审核未通过 3-审核通过
        :type BrandStatus: int
        :param _BrandNote: 审核说明
        :type BrandNote: str
        :param _TransferName: 商标转让证明
        :type TransferName: str
        :param _TransferStatus: 商标转让证明审核状态
        :type TransferStatus: int
        :param _TransferNote: 审核说明 1-审核中 2-审核未通过 3-审核通过
        :type TransferNote: str
        """
        self._BrandName = None
        self._BrandCertificateName = None
        self._BrandStatus = None
        self._BrandNote = None
        self._TransferName = None
        self._TransferStatus = None
        self._TransferNote = None

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def BrandCertificateName(self):
        return self._BrandCertificateName

    @BrandCertificateName.setter
    def BrandCertificateName(self, BrandCertificateName):
        self._BrandCertificateName = BrandCertificateName

    @property
    def BrandStatus(self):
        return self._BrandStatus

    @BrandStatus.setter
    def BrandStatus(self, BrandStatus):
        self._BrandStatus = BrandStatus

    @property
    def BrandNote(self):
        return self._BrandNote

    @BrandNote.setter
    def BrandNote(self, BrandNote):
        self._BrandNote = BrandNote

    @property
    def TransferName(self):
        return self._TransferName

    @TransferName.setter
    def TransferName(self, TransferName):
        self._TransferName = TransferName

    @property
    def TransferStatus(self):
        return self._TransferStatus

    @TransferStatus.setter
    def TransferStatus(self, TransferStatus):
        self._TransferStatus = TransferStatus

    @property
    def TransferNote(self):
        return self._TransferNote

    @TransferNote.setter
    def TransferNote(self, TransferNote):
        self._TransferNote = TransferNote


    def _deserialize(self, params):
        self._BrandName = params.get("BrandName")
        self._BrandCertificateName = params.get("BrandCertificateName")
        self._BrandStatus = params.get("BrandStatus")
        self._BrandNote = params.get("BrandNote")
        self._TransferName = params.get("TransferName")
        self._TransferStatus = params.get("TransferStatus")
        self._TransferNote = params.get("TransferNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLRequest(AbstractModel):
    """CreateBPFakeURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectURLId: 保护网址ID
        :type ProtectURLId: int
        :param _FakeURL: 仿冒网址
        :type FakeURL: str
        :param _SnapshotNames: 截图
        :type SnapshotNames: list of str
        :param _Note: 举报说明
        :type Note: str
        """
        self._ProtectURLId = None
        self._FakeURL = None
        self._SnapshotNames = None
        self._Note = None

    @property
    def ProtectURLId(self):
        return self._ProtectURLId

    @ProtectURLId.setter
    def ProtectURLId(self, ProtectURLId):
        self._ProtectURLId = ProtectURLId

    @property
    def FakeURL(self):
        return self._FakeURL

    @FakeURL.setter
    def FakeURL(self, FakeURL):
        self._FakeURL = FakeURL

    @property
    def SnapshotNames(self):
        return self._SnapshotNames

    @SnapshotNames.setter
    def SnapshotNames(self, SnapshotNames):
        self._SnapshotNames = SnapshotNames

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._ProtectURLId = params.get("ProtectURLId")
        self._FakeURL = params.get("FakeURL")
        self._SnapshotNames = params.get("SnapshotNames")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLResponse(AbstractModel):
    """CreateBPFakeURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBPFalseTicketRequest(AbstractModel):
    """CreateBPFalseTicket请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FakeURL: 仿冒网址
        :type FakeURL: str
        """
        self._FakeURL = None

    @property
    def FakeURL(self):
        return self._FakeURL

    @FakeURL.setter
    def FakeURL(self, FakeURL):
        self._FakeURL = FakeURL


    def _deserialize(self, params):
        self._FakeURL = params.get("FakeURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFalseTicketResponse(AbstractModel):
    """CreateBPFalseTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBPOfflineAttachmentRequest(AbstractModel):
    """CreateBPOfflineAttachment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandName: 品牌名字
        :type BrandName: str
        :param _BrandCertificateName: 商标证明
        :type BrandCertificateName: str
        :param _TransferName: 商标转让证明
        :type TransferName: str
        :param _AuthorizationName: 授权书
        :type AuthorizationName: str
        """
        self._BrandName = None
        self._BrandCertificateName = None
        self._TransferName = None
        self._AuthorizationName = None

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def BrandCertificateName(self):
        return self._BrandCertificateName

    @BrandCertificateName.setter
    def BrandCertificateName(self, BrandCertificateName):
        self._BrandCertificateName = BrandCertificateName

    @property
    def TransferName(self):
        return self._TransferName

    @TransferName.setter
    def TransferName(self, TransferName):
        self._TransferName = TransferName

    @property
    def AuthorizationName(self):
        return self._AuthorizationName

    @AuthorizationName.setter
    def AuthorizationName(self, AuthorizationName):
        self._AuthorizationName = AuthorizationName


    def _deserialize(self, params):
        self._BrandName = params.get("BrandName")
        self._BrandCertificateName = params.get("BrandCertificateName")
        self._TransferName = params.get("TransferName")
        self._AuthorizationName = params.get("AuthorizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPOfflineAttachmentResponse(AbstractModel):
    """CreateBPOfflineAttachment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBPOfflineTicketRequest(AbstractModel):
    """CreateBPOfflineTicket请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FakeURLId: 仿冒网址ID
        :type FakeURLId: int
        """
        self._FakeURLId = None

    @property
    def FakeURLId(self):
        return self._FakeURLId

    @FakeURLId.setter
    def FakeURLId(self, FakeURLId):
        self._FakeURLId = FakeURLId


    def _deserialize(self, params):
        self._FakeURLId = params.get("FakeURLId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPOfflineTicketResponse(AbstractModel):
    """CreateBPOfflineTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBPProtectURLsRequest(AbstractModel):
    """CreateBPProtectURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyName: 企业名称
        :type CompanyName: str
        :param _Phone: 电话号码
        :type Phone: str
        :param _LicenseName: 营业执照
        :type LicenseName: str
        :param _ProtectURLs: 保护网站
        :type ProtectURLs: list of str
        :param _ProtectWebs: 网站名称
        :type ProtectWebs: list of str
        """
        self._CompanyName = None
        self._Phone = None
        self._LicenseName = None
        self._ProtectURLs = None
        self._ProtectWebs = None

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def LicenseName(self):
        return self._LicenseName

    @LicenseName.setter
    def LicenseName(self, LicenseName):
        self._LicenseName = LicenseName

    @property
    def ProtectURLs(self):
        return self._ProtectURLs

    @ProtectURLs.setter
    def ProtectURLs(self, ProtectURLs):
        self._ProtectURLs = ProtectURLs

    @property
    def ProtectWebs(self):
        return self._ProtectWebs

    @ProtectWebs.setter
    def ProtectWebs(self, ProtectWebs):
        self._ProtectWebs = ProtectWebs


    def _deserialize(self, params):
        self._CompanyName = params.get("CompanyName")
        self._Phone = params.get("Phone")
        self._LicenseName = params.get("LicenseName")
        self._ProtectURLs = params.get("ProtectURLs")
        self._ProtectWebs = params.get("ProtectWebs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPProtectURLsResponse(AbstractModel):
    """CreateBPProtectURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCRBlockRequest(AbstractModel):
    """CreateCRBlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _TortUrl: 侵权链接
        :type TortUrl: str
        :param _TortTitle: 侵权标题
        :type TortTitle: str
        :param _TortPlat: 侵权平台
        :type TortPlat: str
        :param _BlockUrl: 拦截结果回调地址
        :type BlockUrl: str
        :param _FileUrl: 授权书下载地址
        :type FileUrl: str
        :param _ValidStartDate: 授权书生效日期
        :type ValidStartDate: str
        :param _ValidEndDate: 授权书截止日期
        :type ValidEndDate: str
        :param _TortPic: 侵权截图
        :type TortPic: str
        :param _CommFileUrl: 委托书下载地址
        :type CommFileUrl: str
        :param _CommValidStartDate: 委托书生效日期
        :type CommValidStartDate: str
        :param _CommValidEndDate: 委托书截止日期
        :type CommValidEndDate: str
        :param _IsProducer: 是否著作权人：0-否 1-是
        :type IsProducer: str
        :param _EvidenceFileUrl: 存证证书下载地址
        :type EvidenceFileUrl: str
        :param _EvidenceValidStartDate: 存证证书生效日期
        :type EvidenceValidStartDate: str
        :param _EvidenceValidEndDate: 存证证书截止日期
        :type EvidenceValidEndDate: str
        """
        self._WorkId = None
        self._TortUrl = None
        self._TortTitle = None
        self._TortPlat = None
        self._BlockUrl = None
        self._FileUrl = None
        self._ValidStartDate = None
        self._ValidEndDate = None
        self._TortPic = None
        self._CommFileUrl = None
        self._CommValidStartDate = None
        self._CommValidEndDate = None
        self._IsProducer = None
        self._EvidenceFileUrl = None
        self._EvidenceValidStartDate = None
        self._EvidenceValidEndDate = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def TortUrl(self):
        return self._TortUrl

    @TortUrl.setter
    def TortUrl(self, TortUrl):
        self._TortUrl = TortUrl

    @property
    def TortTitle(self):
        return self._TortTitle

    @TortTitle.setter
    def TortTitle(self, TortTitle):
        self._TortTitle = TortTitle

    @property
    def TortPlat(self):
        return self._TortPlat

    @TortPlat.setter
    def TortPlat(self, TortPlat):
        self._TortPlat = TortPlat

    @property
    def BlockUrl(self):
        return self._BlockUrl

    @BlockUrl.setter
    def BlockUrl(self, BlockUrl):
        self._BlockUrl = BlockUrl

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def ValidStartDate(self):
        return self._ValidStartDate

    @ValidStartDate.setter
    def ValidStartDate(self, ValidStartDate):
        self._ValidStartDate = ValidStartDate

    @property
    def ValidEndDate(self):
        return self._ValidEndDate

    @ValidEndDate.setter
    def ValidEndDate(self, ValidEndDate):
        self._ValidEndDate = ValidEndDate

    @property
    def TortPic(self):
        return self._TortPic

    @TortPic.setter
    def TortPic(self, TortPic):
        self._TortPic = TortPic

    @property
    def CommFileUrl(self):
        return self._CommFileUrl

    @CommFileUrl.setter
    def CommFileUrl(self, CommFileUrl):
        self._CommFileUrl = CommFileUrl

    @property
    def CommValidStartDate(self):
        return self._CommValidStartDate

    @CommValidStartDate.setter
    def CommValidStartDate(self, CommValidStartDate):
        self._CommValidStartDate = CommValidStartDate

    @property
    def CommValidEndDate(self):
        return self._CommValidEndDate

    @CommValidEndDate.setter
    def CommValidEndDate(self, CommValidEndDate):
        self._CommValidEndDate = CommValidEndDate

    @property
    def IsProducer(self):
        return self._IsProducer

    @IsProducer.setter
    def IsProducer(self, IsProducer):
        self._IsProducer = IsProducer

    @property
    def EvidenceFileUrl(self):
        return self._EvidenceFileUrl

    @EvidenceFileUrl.setter
    def EvidenceFileUrl(self, EvidenceFileUrl):
        self._EvidenceFileUrl = EvidenceFileUrl

    @property
    def EvidenceValidStartDate(self):
        return self._EvidenceValidStartDate

    @EvidenceValidStartDate.setter
    def EvidenceValidStartDate(self, EvidenceValidStartDate):
        self._EvidenceValidStartDate = EvidenceValidStartDate

    @property
    def EvidenceValidEndDate(self):
        return self._EvidenceValidEndDate

    @EvidenceValidEndDate.setter
    def EvidenceValidEndDate(self, EvidenceValidEndDate):
        self._EvidenceValidEndDate = EvidenceValidEndDate


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._TortUrl = params.get("TortUrl")
        self._TortTitle = params.get("TortTitle")
        self._TortPlat = params.get("TortPlat")
        self._BlockUrl = params.get("BlockUrl")
        self._FileUrl = params.get("FileUrl")
        self._ValidStartDate = params.get("ValidStartDate")
        self._ValidEndDate = params.get("ValidEndDate")
        self._TortPic = params.get("TortPic")
        self._CommFileUrl = params.get("CommFileUrl")
        self._CommValidStartDate = params.get("CommValidStartDate")
        self._CommValidEndDate = params.get("CommValidEndDate")
        self._IsProducer = params.get("IsProducer")
        self._EvidenceFileUrl = params.get("EvidenceFileUrl")
        self._EvidenceValidStartDate = params.get("EvidenceValidStartDate")
        self._EvidenceValidEndDate = params.get("EvidenceValidEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRBlockResponse(AbstractModel):
    """CreateCRBlock返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TortId: 侵权ID
        :type TortId: int
        :param _TortNum: 该字段已废弃
        :type TortNum: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TortId = None
        self._TortNum = None
        self._RequestId = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def TortNum(self):
        return self._TortNum

    @TortNum.setter
    def TortNum(self, TortNum):
        self._TortNum = TortNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        self._TortNum = params.get("TortNum")
        self._RequestId = params.get("RequestId")


class CreateCRCompanyVerifyRequest(AbstractModel):
    """CreateCRCompanyVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyName: 企业名称
        :type CompanyName: str
        :param _CompanyID: 企业证件号码
        :type CompanyID: str
        :param _CompanyLegalName: 企业法人姓名
        :type CompanyLegalName: str
        :param _ManagerName: 联系人姓名
        :type ManagerName: str
        :param _ManagerPhone: 联系人手机号
        :type ManagerPhone: str
        :param _VerificationCode: 手机验证码，接口接入可以置空
        :type VerificationCode: str
        :param _CompanyIDType: 字段已废弃，企业认证号码类型 1：社会信用代码 2：组织机构代码 3：企业工商注册码 4：其他 默认为1
        :type CompanyIDType: str
        :param _Type: 字段已废弃，认证类型
        :type Type: str
        """
        self._CompanyName = None
        self._CompanyID = None
        self._CompanyLegalName = None
        self._ManagerName = None
        self._ManagerPhone = None
        self._VerificationCode = None
        self._CompanyIDType = None
        self._Type = None

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def CompanyID(self):
        return self._CompanyID

    @CompanyID.setter
    def CompanyID(self, CompanyID):
        self._CompanyID = CompanyID

    @property
    def CompanyLegalName(self):
        return self._CompanyLegalName

    @CompanyLegalName.setter
    def CompanyLegalName(self, CompanyLegalName):
        self._CompanyLegalName = CompanyLegalName

    @property
    def ManagerName(self):
        return self._ManagerName

    @ManagerName.setter
    def ManagerName(self, ManagerName):
        self._ManagerName = ManagerName

    @property
    def ManagerPhone(self):
        return self._ManagerPhone

    @ManagerPhone.setter
    def ManagerPhone(self, ManagerPhone):
        self._ManagerPhone = ManagerPhone

    @property
    def VerificationCode(self):
        return self._VerificationCode

    @VerificationCode.setter
    def VerificationCode(self, VerificationCode):
        self._VerificationCode = VerificationCode

    @property
    def CompanyIDType(self):
        return self._CompanyIDType

    @CompanyIDType.setter
    def CompanyIDType(self, CompanyIDType):
        self._CompanyIDType = CompanyIDType

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._CompanyName = params.get("CompanyName")
        self._CompanyID = params.get("CompanyID")
        self._CompanyLegalName = params.get("CompanyLegalName")
        self._ManagerName = params.get("ManagerName")
        self._ManagerPhone = params.get("ManagerPhone")
        self._VerificationCode = params.get("VerificationCode")
        self._CompanyIDType = params.get("CompanyIDType")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRCompanyVerifyResponse(AbstractModel):
    """CreateCRCompanyVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 认证状态：0-认证成功 1-认证失败
        :type Status: int
        :param _Note: 认证状态说明，包括认证失败的原因
        :type Note: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Note = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Note = params.get("Note")
        self._RequestId = params.get("RequestId")


class CreateCRDesktopCodeRequest(AbstractModel):
    """CreateCRDesktopCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TortId: xxx
        :type TortId: int
        :param _DesktopCode: xxx
        :type DesktopCode: str
        """
        self._TortId = None
        self._DesktopCode = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def DesktopCode(self):
        return self._DesktopCode

    @DesktopCode.setter
    def DesktopCode(self, DesktopCode):
        self._DesktopCode = DesktopCode


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        self._DesktopCode = params.get("DesktopCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRDesktopCodeResponse(AbstractModel):
    """CreateCRDesktopCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCRRightFileRequest(AbstractModel):
    """CreateCRRightFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _FileList: 权属文件列表
        :type FileList: list of File
        """
        self._WorkId = None
        self._FileList = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def FileList(self):
        return self._FileList

    @FileList.setter
    def FileList(self, FileList):
        self._FileList = FileList


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        if params.get("FileList") is not None:
            self._FileList = []
            for item in params.get("FileList"):
                obj = File()
                obj._deserialize(item)
                self._FileList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRRightFileResponse(AbstractModel):
    """CreateCRRightFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileIds: 权属文件Id，按提交顺序排序
        :type FileIds: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileIds = None
        self._RequestId = None

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileIds = params.get("FileIds")
        self._RequestId = params.get("RequestId")


class CreateCRRightRequest(AbstractModel):
    """CreateCRRight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _TortUrl: 侵权链接
        :type TortUrl: str
        :param _TortTitle: 侵权标题
        :type TortTitle: str
        :param _TortPlat: 侵权平台
        :type TortPlat: str
        :param _RightUrl: 发函结果回调地址
        :type RightUrl: str
        :param _FileUrl: 授权书下载地址
        :type FileUrl: str
        :param _ValidStartDate: 授权书生效日期
        :type ValidStartDate: str
        :param _ValidEndDate: 授权书截止日期
        :type ValidEndDate: str
        :param _CommFileUrl: 委托书下载地址
        :type CommFileUrl: str
        :param _CommValidStartDate: 委托书生效日期
        :type CommValidStartDate: str
        :param _CommValidEndDate: 委托书截止日期
        :type CommValidEndDate: str
        :param _HomeFileUrl: 主页下载地址
        :type HomeFileUrl: str
        :param _HomeValidStartDate: 主页生效日期
        :type HomeValidStartDate: str
        :param _HomeValidEndDate: 主页截止日期
        :type HomeValidEndDate: str
        :param _IsProducer: 是否著作权人：0-否 1-是
        :type IsProducer: str
        :param _EvidenceFileUrl: 存证证书下载地址
        :type EvidenceFileUrl: str
        :param _EvidenceValidStartDate: 存证证书生效日期
        :type EvidenceValidStartDate: str
        :param _EvidenceValidEndDate: 存证证书截止日期
        :type EvidenceValidEndDate: str
        """
        self._WorkId = None
        self._TortUrl = None
        self._TortTitle = None
        self._TortPlat = None
        self._RightUrl = None
        self._FileUrl = None
        self._ValidStartDate = None
        self._ValidEndDate = None
        self._CommFileUrl = None
        self._CommValidStartDate = None
        self._CommValidEndDate = None
        self._HomeFileUrl = None
        self._HomeValidStartDate = None
        self._HomeValidEndDate = None
        self._IsProducer = None
        self._EvidenceFileUrl = None
        self._EvidenceValidStartDate = None
        self._EvidenceValidEndDate = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def TortUrl(self):
        return self._TortUrl

    @TortUrl.setter
    def TortUrl(self, TortUrl):
        self._TortUrl = TortUrl

    @property
    def TortTitle(self):
        return self._TortTitle

    @TortTitle.setter
    def TortTitle(self, TortTitle):
        self._TortTitle = TortTitle

    @property
    def TortPlat(self):
        return self._TortPlat

    @TortPlat.setter
    def TortPlat(self, TortPlat):
        self._TortPlat = TortPlat

    @property
    def RightUrl(self):
        return self._RightUrl

    @RightUrl.setter
    def RightUrl(self, RightUrl):
        self._RightUrl = RightUrl

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def ValidStartDate(self):
        return self._ValidStartDate

    @ValidStartDate.setter
    def ValidStartDate(self, ValidStartDate):
        self._ValidStartDate = ValidStartDate

    @property
    def ValidEndDate(self):
        return self._ValidEndDate

    @ValidEndDate.setter
    def ValidEndDate(self, ValidEndDate):
        self._ValidEndDate = ValidEndDate

    @property
    def CommFileUrl(self):
        return self._CommFileUrl

    @CommFileUrl.setter
    def CommFileUrl(self, CommFileUrl):
        self._CommFileUrl = CommFileUrl

    @property
    def CommValidStartDate(self):
        return self._CommValidStartDate

    @CommValidStartDate.setter
    def CommValidStartDate(self, CommValidStartDate):
        self._CommValidStartDate = CommValidStartDate

    @property
    def CommValidEndDate(self):
        return self._CommValidEndDate

    @CommValidEndDate.setter
    def CommValidEndDate(self, CommValidEndDate):
        self._CommValidEndDate = CommValidEndDate

    @property
    def HomeFileUrl(self):
        return self._HomeFileUrl

    @HomeFileUrl.setter
    def HomeFileUrl(self, HomeFileUrl):
        self._HomeFileUrl = HomeFileUrl

    @property
    def HomeValidStartDate(self):
        return self._HomeValidStartDate

    @HomeValidStartDate.setter
    def HomeValidStartDate(self, HomeValidStartDate):
        self._HomeValidStartDate = HomeValidStartDate

    @property
    def HomeValidEndDate(self):
        return self._HomeValidEndDate

    @HomeValidEndDate.setter
    def HomeValidEndDate(self, HomeValidEndDate):
        self._HomeValidEndDate = HomeValidEndDate

    @property
    def IsProducer(self):
        return self._IsProducer

    @IsProducer.setter
    def IsProducer(self, IsProducer):
        self._IsProducer = IsProducer

    @property
    def EvidenceFileUrl(self):
        return self._EvidenceFileUrl

    @EvidenceFileUrl.setter
    def EvidenceFileUrl(self, EvidenceFileUrl):
        self._EvidenceFileUrl = EvidenceFileUrl

    @property
    def EvidenceValidStartDate(self):
        return self._EvidenceValidStartDate

    @EvidenceValidStartDate.setter
    def EvidenceValidStartDate(self, EvidenceValidStartDate):
        self._EvidenceValidStartDate = EvidenceValidStartDate

    @property
    def EvidenceValidEndDate(self):
        return self._EvidenceValidEndDate

    @EvidenceValidEndDate.setter
    def EvidenceValidEndDate(self, EvidenceValidEndDate):
        self._EvidenceValidEndDate = EvidenceValidEndDate


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._TortUrl = params.get("TortUrl")
        self._TortTitle = params.get("TortTitle")
        self._TortPlat = params.get("TortPlat")
        self._RightUrl = params.get("RightUrl")
        self._FileUrl = params.get("FileUrl")
        self._ValidStartDate = params.get("ValidStartDate")
        self._ValidEndDate = params.get("ValidEndDate")
        self._CommFileUrl = params.get("CommFileUrl")
        self._CommValidStartDate = params.get("CommValidStartDate")
        self._CommValidEndDate = params.get("CommValidEndDate")
        self._HomeFileUrl = params.get("HomeFileUrl")
        self._HomeValidStartDate = params.get("HomeValidStartDate")
        self._HomeValidEndDate = params.get("HomeValidEndDate")
        self._IsProducer = params.get("IsProducer")
        self._EvidenceFileUrl = params.get("EvidenceFileUrl")
        self._EvidenceValidStartDate = params.get("EvidenceValidStartDate")
        self._EvidenceValidEndDate = params.get("EvidenceValidEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRRightResponse(AbstractModel):
    """CreateCRRight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TortId: 侵权ID
        :type TortId: int
        :param _TortNum: 该字段已废弃
        :type TortNum: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TortId = None
        self._TortNum = None
        self._RequestId = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def TortNum(self):
        return self._TortNum

    @TortNum.setter
    def TortNum(self, TortNum):
        self._TortNum = TortNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        self._TortNum = params.get("TortNum")
        self._RequestId = params.get("RequestId")


class CreateCRTortRequest(AbstractModel):
    """CreateCRTort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _TortURL: 侵权网址
        :type TortURL: str
        :param _TortPlat: 侵权平台
        :type TortPlat: str
        :param _TortTitle: 侵权标题
        :type TortTitle: str
        """
        self._WorkId = None
        self._TortURL = None
        self._TortPlat = None
        self._TortTitle = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def TortURL(self):
        return self._TortURL

    @TortURL.setter
    def TortURL(self, TortURL):
        self._TortURL = TortURL

    @property
    def TortPlat(self):
        return self._TortPlat

    @TortPlat.setter
    def TortPlat(self, TortPlat):
        self._TortPlat = TortPlat

    @property
    def TortTitle(self):
        return self._TortTitle

    @TortTitle.setter
    def TortTitle(self, TortTitle):
        self._TortTitle = TortTitle


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._TortURL = params.get("TortURL")
        self._TortPlat = params.get("TortPlat")
        self._TortTitle = params.get("TortTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRTortResponse(AbstractModel):
    """CreateCRTort返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _TortId: 侵权ID
        :type TortId: int
        :param _TortTitle: 侵权标题
        :type TortTitle: str
        :param _TortPlat: 侵权平台
        :type TortPlat: str
        :param _TortURL: 侵权网址
        :type TortURL: str
        :param _TortDomain: 侵权域名
        :type TortDomain: str
        :param _TortBodyName: 侵权主体
        :type TortBodyName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkId = None
        self._TortId = None
        self._TortTitle = None
        self._TortPlat = None
        self._TortURL = None
        self._TortDomain = None
        self._TortBodyName = None
        self._RequestId = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def TortTitle(self):
        return self._TortTitle

    @TortTitle.setter
    def TortTitle(self, TortTitle):
        self._TortTitle = TortTitle

    @property
    def TortPlat(self):
        return self._TortPlat

    @TortPlat.setter
    def TortPlat(self, TortPlat):
        self._TortPlat = TortPlat

    @property
    def TortURL(self):
        return self._TortURL

    @TortURL.setter
    def TortURL(self, TortURL):
        self._TortURL = TortURL

    @property
    def TortDomain(self):
        return self._TortDomain

    @TortDomain.setter
    def TortDomain(self, TortDomain):
        self._TortDomain = TortDomain

    @property
    def TortBodyName(self):
        return self._TortBodyName

    @TortBodyName.setter
    def TortBodyName(self, TortBodyName):
        self._TortBodyName = TortBodyName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._TortId = params.get("TortId")
        self._TortTitle = params.get("TortTitle")
        self._TortPlat = params.get("TortPlat")
        self._TortURL = params.get("TortURL")
        self._TortDomain = params.get("TortDomain")
        self._TortBodyName = params.get("TortBodyName")
        self._RequestId = params.get("RequestId")


class CreateCRUserVerifyRequest(AbstractModel):
    """CreateCRUserVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户真实姓名
        :type UserName: str
        :param _UserID: 用户身份证号
        :type UserID: str
        :param _UserPhone: 用户手机号码
        :type UserPhone: str
        :param _VerificationCode: 短信验证码，接口接入可以置空
        :type VerificationCode: str
        :param _Type: 字段已废弃，认证类型
        :type Type: str
        """
        self._UserName = None
        self._UserID = None
        self._UserPhone = None
        self._VerificationCode = None
        self._Type = None

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
    def UserPhone(self):
        return self._UserPhone

    @UserPhone.setter
    def UserPhone(self, UserPhone):
        self._UserPhone = UserPhone

    @property
    def VerificationCode(self):
        return self._VerificationCode

    @VerificationCode.setter
    def VerificationCode(self, VerificationCode):
        self._VerificationCode = VerificationCode

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserID = params.get("UserID")
        self._UserPhone = params.get("UserPhone")
        self._VerificationCode = params.get("VerificationCode")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRUserVerifyResponse(AbstractModel):
    """CreateCRUserVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 认证状态：0-认证成功 1-认证失败
        :type Status: int
        :param _Note: 认证状态说明，包括认证失败原因等
        :type Note: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Note = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Note = params.get("Note")
        self._RequestId = params.get("RequestId")


class CreateCRWorkRequest(AbstractModel):
    """CreateCRWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkName: 作品名称
        :type WorkName: str
        :param _WorkCategory: 作品分类
        :type WorkCategory: str
        :param _WorkType: 作品内容类型
        :type WorkType: str
        :param _WorkSign: 作品标签
        :type WorkSign: str
        :param _WorkPic: 字段已废弃，作品图片
        :type WorkPic: str
        :param _WorkDesc: 作品描述
        :type WorkDesc: str
        :param _IsOriginal: 是否原创：0-否 1-是
        :type IsOriginal: str
        :param _IsRelease: 是否发布：0-未发布 1-已发布
        :type IsRelease: str
        :param _ProducerID: 字段已废弃，著作权人ID
        :type ProducerID: int
        :param _ProduceTime: 创作时间
        :type ProduceTime: str
        :param _SampleContentURL: 字段已废弃
        :type SampleContentURL: str
        :param _SampleDownloadURL: 作品下载地址
        :type SampleDownloadURL: str
        :param _SamplePublicURL: 作品在线地址
        :type SamplePublicURL: str
        :param _GrantType: 字段已废弃，授予类型
        :type GrantType: str
        :param _IsMonitor: 是否监测：0-不监测 1-监测
        :type IsMonitor: str
        :param _IsCert: 是否存证：0-不存证  2-存证 注意是2
        :type IsCert: str
        :param _CertUrl: 存证回调地址
        :type CertUrl: str
        :param _MonitorUrl: 监测回调地址
        :type MonitorUrl: str
        :param _ProduceType: 字段已废弃，创作性质
        :type ProduceType: str
        :param _WhiteLists: 白名单列表
        :type WhiteLists: list of str
        :param _WorkId: 作品ID，忽略该字段
        :type WorkId: int
        :param _ProducerName: 著作权人姓名
        :type ProducerName: str
        :param _Nickname: 作者，小说类型必填
        :type Nickname: str
        :param _Authorization: 授权书下载地址
        :type Authorization: str
        :param _AuthorizationStartTime: 授权书开始时间
        :type AuthorizationStartTime: str
        :param _AuthorizationEndTime: 授权书结束时间
        :type AuthorizationEndTime: str
        :param _ContentType: 内容格式，支持txt、doc等，表示Content的具体格式
        :type ContentType: str
        :param _Content: 文件内容base64编码，该字段仅在无法提供下载链接时使用
        :type Content: str
        :param _MonitorEndTime: 监测结束时间
        :type MonitorEndTime: str
        :param _ApplierId: 申请人ID，用于存证和取证
        :type ApplierId: str
        :param _ApplierName: 申请人姓名，用于存证和取证
        :type ApplierName: str
        :param _IsAutoRenew: 是否自动续期
        :type IsAutoRenew: str
        """
        self._WorkName = None
        self._WorkCategory = None
        self._WorkType = None
        self._WorkSign = None
        self._WorkPic = None
        self._WorkDesc = None
        self._IsOriginal = None
        self._IsRelease = None
        self._ProducerID = None
        self._ProduceTime = None
        self._SampleContentURL = None
        self._SampleDownloadURL = None
        self._SamplePublicURL = None
        self._GrantType = None
        self._IsMonitor = None
        self._IsCert = None
        self._CertUrl = None
        self._MonitorUrl = None
        self._ProduceType = None
        self._WhiteLists = None
        self._WorkId = None
        self._ProducerName = None
        self._Nickname = None
        self._Authorization = None
        self._AuthorizationStartTime = None
        self._AuthorizationEndTime = None
        self._ContentType = None
        self._Content = None
        self._MonitorEndTime = None
        self._ApplierId = None
        self._ApplierName = None
        self._IsAutoRenew = None

    @property
    def WorkName(self):
        return self._WorkName

    @WorkName.setter
    def WorkName(self, WorkName):
        self._WorkName = WorkName

    @property
    def WorkCategory(self):
        return self._WorkCategory

    @WorkCategory.setter
    def WorkCategory(self, WorkCategory):
        self._WorkCategory = WorkCategory

    @property
    def WorkType(self):
        return self._WorkType

    @WorkType.setter
    def WorkType(self, WorkType):
        self._WorkType = WorkType

    @property
    def WorkSign(self):
        return self._WorkSign

    @WorkSign.setter
    def WorkSign(self, WorkSign):
        self._WorkSign = WorkSign

    @property
    def WorkPic(self):
        return self._WorkPic

    @WorkPic.setter
    def WorkPic(self, WorkPic):
        self._WorkPic = WorkPic

    @property
    def WorkDesc(self):
        return self._WorkDesc

    @WorkDesc.setter
    def WorkDesc(self, WorkDesc):
        self._WorkDesc = WorkDesc

    @property
    def IsOriginal(self):
        return self._IsOriginal

    @IsOriginal.setter
    def IsOriginal(self, IsOriginal):
        self._IsOriginal = IsOriginal

    @property
    def IsRelease(self):
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease

    @property
    def ProducerID(self):
        return self._ProducerID

    @ProducerID.setter
    def ProducerID(self, ProducerID):
        self._ProducerID = ProducerID

    @property
    def ProduceTime(self):
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def SampleContentURL(self):
        return self._SampleContentURL

    @SampleContentURL.setter
    def SampleContentURL(self, SampleContentURL):
        self._SampleContentURL = SampleContentURL

    @property
    def SampleDownloadURL(self):
        return self._SampleDownloadURL

    @SampleDownloadURL.setter
    def SampleDownloadURL(self, SampleDownloadURL):
        self._SampleDownloadURL = SampleDownloadURL

    @property
    def SamplePublicURL(self):
        return self._SamplePublicURL

    @SamplePublicURL.setter
    def SamplePublicURL(self, SamplePublicURL):
        self._SamplePublicURL = SamplePublicURL

    @property
    def GrantType(self):
        return self._GrantType

    @GrantType.setter
    def GrantType(self, GrantType):
        self._GrantType = GrantType

    @property
    def IsMonitor(self):
        return self._IsMonitor

    @IsMonitor.setter
    def IsMonitor(self, IsMonitor):
        self._IsMonitor = IsMonitor

    @property
    def IsCert(self):
        return self._IsCert

    @IsCert.setter
    def IsCert(self, IsCert):
        self._IsCert = IsCert

    @property
    def CertUrl(self):
        return self._CertUrl

    @CertUrl.setter
    def CertUrl(self, CertUrl):
        self._CertUrl = CertUrl

    @property
    def MonitorUrl(self):
        return self._MonitorUrl

    @MonitorUrl.setter
    def MonitorUrl(self, MonitorUrl):
        self._MonitorUrl = MonitorUrl

    @property
    def ProduceType(self):
        return self._ProduceType

    @ProduceType.setter
    def ProduceType(self, ProduceType):
        self._ProduceType = ProduceType

    @property
    def WhiteLists(self):
        return self._WhiteLists

    @WhiteLists.setter
    def WhiteLists(self, WhiteLists):
        self._WhiteLists = WhiteLists

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def ProducerName(self):
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Authorization(self):
        return self._Authorization

    @Authorization.setter
    def Authorization(self, Authorization):
        self._Authorization = Authorization

    @property
    def AuthorizationStartTime(self):
        return self._AuthorizationStartTime

    @AuthorizationStartTime.setter
    def AuthorizationStartTime(self, AuthorizationStartTime):
        self._AuthorizationStartTime = AuthorizationStartTime

    @property
    def AuthorizationEndTime(self):
        return self._AuthorizationEndTime

    @AuthorizationEndTime.setter
    def AuthorizationEndTime(self, AuthorizationEndTime):
        self._AuthorizationEndTime = AuthorizationEndTime

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def MonitorEndTime(self):
        return self._MonitorEndTime

    @MonitorEndTime.setter
    def MonitorEndTime(self, MonitorEndTime):
        self._MonitorEndTime = MonitorEndTime

    @property
    def ApplierId(self):
        return self._ApplierId

    @ApplierId.setter
    def ApplierId(self, ApplierId):
        self._ApplierId = ApplierId

    @property
    def ApplierName(self):
        return self._ApplierName

    @ApplierName.setter
    def ApplierName(self, ApplierName):
        self._ApplierName = ApplierName

    @property
    def IsAutoRenew(self):
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew


    def _deserialize(self, params):
        self._WorkName = params.get("WorkName")
        self._WorkCategory = params.get("WorkCategory")
        self._WorkType = params.get("WorkType")
        self._WorkSign = params.get("WorkSign")
        self._WorkPic = params.get("WorkPic")
        self._WorkDesc = params.get("WorkDesc")
        self._IsOriginal = params.get("IsOriginal")
        self._IsRelease = params.get("IsRelease")
        self._ProducerID = params.get("ProducerID")
        self._ProduceTime = params.get("ProduceTime")
        self._SampleContentURL = params.get("SampleContentURL")
        self._SampleDownloadURL = params.get("SampleDownloadURL")
        self._SamplePublicURL = params.get("SamplePublicURL")
        self._GrantType = params.get("GrantType")
        self._IsMonitor = params.get("IsMonitor")
        self._IsCert = params.get("IsCert")
        self._CertUrl = params.get("CertUrl")
        self._MonitorUrl = params.get("MonitorUrl")
        self._ProduceType = params.get("ProduceType")
        self._WhiteLists = params.get("WhiteLists")
        self._WorkId = params.get("WorkId")
        self._ProducerName = params.get("ProducerName")
        self._Nickname = params.get("Nickname")
        self._Authorization = params.get("Authorization")
        self._AuthorizationStartTime = params.get("AuthorizationStartTime")
        self._AuthorizationEndTime = params.get("AuthorizationEndTime")
        self._ContentType = params.get("ContentType")
        self._Content = params.get("Content")
        self._MonitorEndTime = params.get("MonitorEndTime")
        self._ApplierId = params.get("ApplierId")
        self._ApplierName = params.get("ApplierName")
        self._IsAutoRenew = params.get("IsAutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRWorkResponse(AbstractModel):
    """CreateCRWork返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID，一个作品对应唯一的workid
        :type WorkId: int
        :param _EvidenceId: 存证ID，忽略该字段
        :type EvidenceId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class DescribeBPCompanyInfoRequest(AbstractModel):
    """DescribeBPCompanyInfo请求参数结构体

    """


class DescribeBPCompanyInfoResponse(AbstractModel):
    """DescribeBPCompanyInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyName: 企业名称
        :type CompanyName: str
        :param _Phone: 电话号码
        :type Phone: str
        :param _LicenseName: 营业执照
        :type LicenseName: str
        :param _LicenseStatus: 营业执照审核状态 1-审核中 2-审核未通过，3、审核通过
        :type LicenseStatus: int
        :param _LicenseNote: 营业执照备注
        :type LicenseNote: str
        :param _AuthorizationName: 授权书
        :type AuthorizationName: str
        :param _AuthorizationStatus: 授权书审核状态
        :type AuthorizationStatus: int
        :param _AuthorizationNote: 授权书备注
        :type AuthorizationNote: str
        :param _BrandDatas: 品牌信息
        :type BrandDatas: list of BrandData
        :param _CompanyId: 企业ID
        :type CompanyId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyName = None
        self._Phone = None
        self._LicenseName = None
        self._LicenseStatus = None
        self._LicenseNote = None
        self._AuthorizationName = None
        self._AuthorizationStatus = None
        self._AuthorizationNote = None
        self._BrandDatas = None
        self._CompanyId = None
        self._RequestId = None

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def LicenseName(self):
        return self._LicenseName

    @LicenseName.setter
    def LicenseName(self, LicenseName):
        self._LicenseName = LicenseName

    @property
    def LicenseStatus(self):
        return self._LicenseStatus

    @LicenseStatus.setter
    def LicenseStatus(self, LicenseStatus):
        self._LicenseStatus = LicenseStatus

    @property
    def LicenseNote(self):
        return self._LicenseNote

    @LicenseNote.setter
    def LicenseNote(self, LicenseNote):
        self._LicenseNote = LicenseNote

    @property
    def AuthorizationName(self):
        return self._AuthorizationName

    @AuthorizationName.setter
    def AuthorizationName(self, AuthorizationName):
        self._AuthorizationName = AuthorizationName

    @property
    def AuthorizationStatus(self):
        return self._AuthorizationStatus

    @AuthorizationStatus.setter
    def AuthorizationStatus(self, AuthorizationStatus):
        self._AuthorizationStatus = AuthorizationStatus

    @property
    def AuthorizationNote(self):
        return self._AuthorizationNote

    @AuthorizationNote.setter
    def AuthorizationNote(self, AuthorizationNote):
        self._AuthorizationNote = AuthorizationNote

    @property
    def BrandDatas(self):
        return self._BrandDatas

    @BrandDatas.setter
    def BrandDatas(self, BrandDatas):
        self._BrandDatas = BrandDatas

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyName = params.get("CompanyName")
        self._Phone = params.get("Phone")
        self._LicenseName = params.get("LicenseName")
        self._LicenseStatus = params.get("LicenseStatus")
        self._LicenseNote = params.get("LicenseNote")
        self._AuthorizationName = params.get("AuthorizationName")
        self._AuthorizationStatus = params.get("AuthorizationStatus")
        self._AuthorizationNote = params.get("AuthorizationNote")
        if params.get("BrandDatas") is not None:
            self._BrandDatas = []
            for item in params.get("BrandDatas"):
                obj = BrandData()
                obj._deserialize(item)
                self._BrandDatas.append(obj)
        self._CompanyId = params.get("CompanyId")
        self._RequestId = params.get("RequestId")


class DescribeBPFakeURLsRequest(AbstractModel):
    """DescribeBPFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _PageSize: 页数
        :type PageSize: int
        :param _PageNumber: 页码
        :type PageNumber: int
        """
        self._Filters = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBPFakeURLsResponse(AbstractModel):
    """DescribeBPFakeURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FakeURLInfos: 仿冒网址列表
        :type FakeURLInfos: list of FakeURLInfo
        :param _TotalCount: 总量
        :type TotalCount: int
        :param _ExportURL: 导出量
        :type ExportURL: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FakeURLInfos = None
        self._TotalCount = None
        self._ExportURL = None
        self._RequestId = None

    @property
    def FakeURLInfos(self):
        return self._FakeURLInfos

    @FakeURLInfos.setter
    def FakeURLInfos(self, FakeURLInfos):
        self._FakeURLInfos = FakeURLInfos

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ExportURL(self):
        return self._ExportURL

    @ExportURL.setter
    def ExportURL(self, ExportURL):
        self._ExportURL = ExportURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FakeURLInfos") is not None:
            self._FakeURLInfos = []
            for item in params.get("FakeURLInfos"):
                obj = FakeURLInfo()
                obj._deserialize(item)
                self._FakeURLInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._ExportURL = params.get("ExportURL")
        self._RequestId = params.get("RequestId")


class DescribeBPProtectURLsRequest(AbstractModel):
    """DescribeBPProtectURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 页数
        :type PageSize: int
        :param _PageNumber: 页码
        :type PageNumber: int
        """
        self._PageSize = None
        self._PageNumber = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBPProtectURLsResponse(AbstractModel):
    """DescribeBPProtectURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectURLInfos: 保护网址列表
        :type ProtectURLInfos: list of ProtectURLInfo
        :param _TotalCount: 总量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProtectURLInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProtectURLInfos(self):
        return self._ProtectURLInfos

    @ProtectURLInfos.setter
    def ProtectURLInfos(self, ProtectURLInfos):
        self._ProtectURLInfos = ProtectURLInfos

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProtectURLInfos") is not None:
            self._ProtectURLInfos = []
            for item in params.get("ProtectURLInfos"):
                obj = ProtectURLInfo()
                obj._deserialize(item)
                self._ProtectURLInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBPReportFakeURLsRequest(AbstractModel):
    """DescribeBPReportFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _PageSize: 页数
        :type PageSize: int
        :param _PageNumber: 页码
        :type PageNumber: int
        """
        self._Filters = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBPReportFakeURLsResponse(AbstractModel):
    """DescribeBPReportFakeURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportFakeURLInfos: 举报网站列表
        :type ReportFakeURLInfos: list of ReportFakeURLInfo
        :param _TotalCount: 总量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportFakeURLInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ReportFakeURLInfos(self):
        return self._ReportFakeURLInfos

    @ReportFakeURLInfos.setter
    def ReportFakeURLInfos(self, ReportFakeURLInfos):
        self._ReportFakeURLInfos = ReportFakeURLInfos

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReportFakeURLInfos") is not None:
            self._ReportFakeURLInfos = []
            for item in params.get("ReportFakeURLInfos"):
                obj = ReportFakeURLInfo()
                obj._deserialize(item)
                self._ReportFakeURLInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCRMonitorDetailRequest(AbstractModel):
    """DescribeCRMonitorDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _PageSize: 页数
        :type PageSize: int
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._WorkId = None
        self._PageSize = None
        self._PageNumber = None
        self._Filters = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRMonitorDetailResponse(AbstractModel):
    """DescribeCRMonitorDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Torts: 侵权数组
        :type Torts: list of MonitorTort
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _MonitorStatus: 监测状态
        :type MonitorStatus: int
        :param _ExportURL: 导出地址
        :type ExportURL: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Torts = None
        self._TotalCount = None
        self._MonitorStatus = None
        self._ExportURL = None
        self._RequestId = None

    @property
    def Torts(self):
        return self._Torts

    @Torts.setter
    def Torts(self, Torts):
        self._Torts = Torts

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def ExportURL(self):
        return self._ExportURL

    @ExportURL.setter
    def ExportURL(self, ExportURL):
        self._ExportURL = ExportURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Torts") is not None:
            self._Torts = []
            for item in params.get("Torts"):
                obj = MonitorTort()
                obj._deserialize(item)
                self._Torts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._MonitorStatus = params.get("MonitorStatus")
        self._ExportURL = params.get("ExportURL")
        self._RequestId = params.get("RequestId")


class DescribeCRMonitorsRequest(AbstractModel):
    """DescribeCRMonitors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _PageSize: 页数
        :type PageSize: int
        :param _PageNumber: 页码
        :type PageNumber: int
        """
        self._Filters = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRMonitorsResponse(AbstractModel):
    """DescribeCRMonitors返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Monitors: 监测结果
        :type Monitors: list of Monitor
        :param _TotalCount: 记录总条数
        :type TotalCount: int
        :param _ExportURL: 导出地址
        :type ExportURL: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Monitors = None
        self._TotalCount = None
        self._ExportURL = None
        self._RequestId = None

    @property
    def Monitors(self):
        return self._Monitors

    @Monitors.setter
    def Monitors(self, Monitors):
        self._Monitors = Monitors

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ExportURL(self):
        return self._ExportURL

    @ExportURL.setter
    def ExportURL(self, ExportURL):
        self._ExportURL = ExportURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Monitors") is not None:
            self._Monitors = []
            for item in params.get("Monitors"):
                obj = Monitor()
                obj._deserialize(item)
                self._Monitors.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._ExportURL = params.get("ExportURL")
        self._RequestId = params.get("RequestId")


class DescribeCRObtainDetailRequest(AbstractModel):
    """DescribeCRObtainDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TortId: 侵权ID
        :type TortId: int
        """
        self._TortId = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRObtainDetailResponse(AbstractModel):
    """DescribeCRObtainDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkName: 作品名称
        :type WorkName: str
        :param _TortURL: 侵权链接
        :type TortURL: str
        :param _ObtainTime: 取证时间
        :type ObtainTime: str
        :param _ObtainType: 取证类型
        :type ObtainType: str
        :param _ObtainNum: 取证号
        :type ObtainNum: str
        :param _DepositFile: 证据地址
        :type DepositFile: str
        :param _DepositCert: 公证信息地址
        :type DepositCert: str
        :param _WorkType: 内容类型
        :type WorkType: str
        :param _WorkCategory: 作品类型
        :type WorkCategory: str
        :param _TortId: 侵权ID
        :type TortId: int
        :param _TortNum: 侵权编号
        :type TortNum: str
        :param _ObtainStatus: 取证状态
        :type ObtainStatus: int
        :param _ObtainNote: 取证状态说明
        :type ObtainNote: str
        :param _ObtainDuration: 取证时长
        :type ObtainDuration: str
        :param _ObtainName: 取证名称
        :type ObtainName: str
        :param _DepositPdfCert: 取证公证信息
        :type DepositPdfCert: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkName = None
        self._TortURL = None
        self._ObtainTime = None
        self._ObtainType = None
        self._ObtainNum = None
        self._DepositFile = None
        self._DepositCert = None
        self._WorkType = None
        self._WorkCategory = None
        self._TortId = None
        self._TortNum = None
        self._ObtainStatus = None
        self._ObtainNote = None
        self._ObtainDuration = None
        self._ObtainName = None
        self._DepositPdfCert = None
        self._RequestId = None

    @property
    def WorkName(self):
        return self._WorkName

    @WorkName.setter
    def WorkName(self, WorkName):
        self._WorkName = WorkName

    @property
    def TortURL(self):
        return self._TortURL

    @TortURL.setter
    def TortURL(self, TortURL):
        self._TortURL = TortURL

    @property
    def ObtainTime(self):
        return self._ObtainTime

    @ObtainTime.setter
    def ObtainTime(self, ObtainTime):
        self._ObtainTime = ObtainTime

    @property
    def ObtainType(self):
        return self._ObtainType

    @ObtainType.setter
    def ObtainType(self, ObtainType):
        self._ObtainType = ObtainType

    @property
    def ObtainNum(self):
        return self._ObtainNum

    @ObtainNum.setter
    def ObtainNum(self, ObtainNum):
        self._ObtainNum = ObtainNum

    @property
    def DepositFile(self):
        return self._DepositFile

    @DepositFile.setter
    def DepositFile(self, DepositFile):
        self._DepositFile = DepositFile

    @property
    def DepositCert(self):
        return self._DepositCert

    @DepositCert.setter
    def DepositCert(self, DepositCert):
        self._DepositCert = DepositCert

    @property
    def WorkType(self):
        return self._WorkType

    @WorkType.setter
    def WorkType(self, WorkType):
        self._WorkType = WorkType

    @property
    def WorkCategory(self):
        return self._WorkCategory

    @WorkCategory.setter
    def WorkCategory(self, WorkCategory):
        self._WorkCategory = WorkCategory

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def TortNum(self):
        return self._TortNum

    @TortNum.setter
    def TortNum(self, TortNum):
        self._TortNum = TortNum

    @property
    def ObtainStatus(self):
        return self._ObtainStatus

    @ObtainStatus.setter
    def ObtainStatus(self, ObtainStatus):
        self._ObtainStatus = ObtainStatus

    @property
    def ObtainNote(self):
        return self._ObtainNote

    @ObtainNote.setter
    def ObtainNote(self, ObtainNote):
        self._ObtainNote = ObtainNote

    @property
    def ObtainDuration(self):
        return self._ObtainDuration

    @ObtainDuration.setter
    def ObtainDuration(self, ObtainDuration):
        self._ObtainDuration = ObtainDuration

    @property
    def ObtainName(self):
        return self._ObtainName

    @ObtainName.setter
    def ObtainName(self, ObtainName):
        self._ObtainName = ObtainName

    @property
    def DepositPdfCert(self):
        return self._DepositPdfCert

    @DepositPdfCert.setter
    def DepositPdfCert(self, DepositPdfCert):
        self._DepositPdfCert = DepositPdfCert

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkName = params.get("WorkName")
        self._TortURL = params.get("TortURL")
        self._ObtainTime = params.get("ObtainTime")
        self._ObtainType = params.get("ObtainType")
        self._ObtainNum = params.get("ObtainNum")
        self._DepositFile = params.get("DepositFile")
        self._DepositCert = params.get("DepositCert")
        self._WorkType = params.get("WorkType")
        self._WorkCategory = params.get("WorkCategory")
        self._TortId = params.get("TortId")
        self._TortNum = params.get("TortNum")
        self._ObtainStatus = params.get("ObtainStatus")
        self._ObtainNote = params.get("ObtainNote")
        self._ObtainDuration = params.get("ObtainDuration")
        self._ObtainName = params.get("ObtainName")
        self._DepositPdfCert = params.get("DepositPdfCert")
        self._RequestId = params.get("RequestId")


class DescribeCRWorkInfoRequest(AbstractModel):
    """DescribeCRWorkInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        """
        self._WorkId = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRWorkInfoResponse(AbstractModel):
    """DescribeCRWorkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkName: 作品名称
        :type WorkName: str
        :param _MonitorStatus: 监测状态
        :type MonitorStatus: int
        :param _AuthStatus: 授权文件状态
        :type AuthStatus: int
        :param _CommStatus: 委托书状态
        :type CommStatus: int
        :param _IsProducer: 是否著作权人
        :type IsProducer: int
        :param _EvidenceStatus: 存证证书状态
        :type EvidenceStatus: int
        :param _WorkCategory: 作品类型
        :type WorkCategory: str
        :param _IsOriginal: 是否原创
        :type IsOriginal: str
        :param _IsRelease: 是否已发表
        :type IsRelease: str
        :param _ProducerName: 著作权人姓名
        :type ProducerName: str
        :param _ProduceTime: 发表时间
        :type ProduceTime: str
        :param _WhiteLists: 白名单
        :type WhiteLists: list of str
        :param _WorkDesc: 作品描述
        :type WorkDesc: str
        :param _Authorization: 授权书
        :type Authorization: str
        :param _AuthorizationStartTime: 授权书生效日期
        :type AuthorizationStartTime: str
        :param _AuthorizationEndTime: 授权书截止日期
        :type AuthorizationEndTime: str
        :param _Commission: 委托书
        :type Commission: str
        :param _CommissionStartTime: 委托书生效日期
        :type CommissionStartTime: str
        :param _CommissionEndTime: 委托书截止日期
        :type CommissionEndTime: str
        :param _EvidenceUrl: 存证证书
        :type EvidenceUrl: str
        :param _EvidenceStartTime: 存证证书生效日期
        :type EvidenceStartTime: str
        :param _EvidenceEndTime: 存证证书截止日期
        :type EvidenceEndTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkName = None
        self._MonitorStatus = None
        self._AuthStatus = None
        self._CommStatus = None
        self._IsProducer = None
        self._EvidenceStatus = None
        self._WorkCategory = None
        self._IsOriginal = None
        self._IsRelease = None
        self._ProducerName = None
        self._ProduceTime = None
        self._WhiteLists = None
        self._WorkDesc = None
        self._Authorization = None
        self._AuthorizationStartTime = None
        self._AuthorizationEndTime = None
        self._Commission = None
        self._CommissionStartTime = None
        self._CommissionEndTime = None
        self._EvidenceUrl = None
        self._EvidenceStartTime = None
        self._EvidenceEndTime = None
        self._RequestId = None

    @property
    def WorkName(self):
        return self._WorkName

    @WorkName.setter
    def WorkName(self, WorkName):
        self._WorkName = WorkName

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def AuthStatus(self):
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def CommStatus(self):
        return self._CommStatus

    @CommStatus.setter
    def CommStatus(self, CommStatus):
        self._CommStatus = CommStatus

    @property
    def IsProducer(self):
        return self._IsProducer

    @IsProducer.setter
    def IsProducer(self, IsProducer):
        self._IsProducer = IsProducer

    @property
    def EvidenceStatus(self):
        return self._EvidenceStatus

    @EvidenceStatus.setter
    def EvidenceStatus(self, EvidenceStatus):
        self._EvidenceStatus = EvidenceStatus

    @property
    def WorkCategory(self):
        return self._WorkCategory

    @WorkCategory.setter
    def WorkCategory(self, WorkCategory):
        self._WorkCategory = WorkCategory

    @property
    def IsOriginal(self):
        return self._IsOriginal

    @IsOriginal.setter
    def IsOriginal(self, IsOriginal):
        self._IsOriginal = IsOriginal

    @property
    def IsRelease(self):
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease

    @property
    def ProducerName(self):
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def ProduceTime(self):
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def WhiteLists(self):
        return self._WhiteLists

    @WhiteLists.setter
    def WhiteLists(self, WhiteLists):
        self._WhiteLists = WhiteLists

    @property
    def WorkDesc(self):
        return self._WorkDesc

    @WorkDesc.setter
    def WorkDesc(self, WorkDesc):
        self._WorkDesc = WorkDesc

    @property
    def Authorization(self):
        return self._Authorization

    @Authorization.setter
    def Authorization(self, Authorization):
        self._Authorization = Authorization

    @property
    def AuthorizationStartTime(self):
        return self._AuthorizationStartTime

    @AuthorizationStartTime.setter
    def AuthorizationStartTime(self, AuthorizationStartTime):
        self._AuthorizationStartTime = AuthorizationStartTime

    @property
    def AuthorizationEndTime(self):
        return self._AuthorizationEndTime

    @AuthorizationEndTime.setter
    def AuthorizationEndTime(self, AuthorizationEndTime):
        self._AuthorizationEndTime = AuthorizationEndTime

    @property
    def Commission(self):
        return self._Commission

    @Commission.setter
    def Commission(self, Commission):
        self._Commission = Commission

    @property
    def CommissionStartTime(self):
        return self._CommissionStartTime

    @CommissionStartTime.setter
    def CommissionStartTime(self, CommissionStartTime):
        self._CommissionStartTime = CommissionStartTime

    @property
    def CommissionEndTime(self):
        return self._CommissionEndTime

    @CommissionEndTime.setter
    def CommissionEndTime(self, CommissionEndTime):
        self._CommissionEndTime = CommissionEndTime

    @property
    def EvidenceUrl(self):
        return self._EvidenceUrl

    @EvidenceUrl.setter
    def EvidenceUrl(self, EvidenceUrl):
        self._EvidenceUrl = EvidenceUrl

    @property
    def EvidenceStartTime(self):
        return self._EvidenceStartTime

    @EvidenceStartTime.setter
    def EvidenceStartTime(self, EvidenceStartTime):
        self._EvidenceStartTime = EvidenceStartTime

    @property
    def EvidenceEndTime(self):
        return self._EvidenceEndTime

    @EvidenceEndTime.setter
    def EvidenceEndTime(self, EvidenceEndTime):
        self._EvidenceEndTime = EvidenceEndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkName = params.get("WorkName")
        self._MonitorStatus = params.get("MonitorStatus")
        self._AuthStatus = params.get("AuthStatus")
        self._CommStatus = params.get("CommStatus")
        self._IsProducer = params.get("IsProducer")
        self._EvidenceStatus = params.get("EvidenceStatus")
        self._WorkCategory = params.get("WorkCategory")
        self._IsOriginal = params.get("IsOriginal")
        self._IsRelease = params.get("IsRelease")
        self._ProducerName = params.get("ProducerName")
        self._ProduceTime = params.get("ProduceTime")
        self._WhiteLists = params.get("WhiteLists")
        self._WorkDesc = params.get("WorkDesc")
        self._Authorization = params.get("Authorization")
        self._AuthorizationStartTime = params.get("AuthorizationStartTime")
        self._AuthorizationEndTime = params.get("AuthorizationEndTime")
        self._Commission = params.get("Commission")
        self._CommissionStartTime = params.get("CommissionStartTime")
        self._CommissionEndTime = params.get("CommissionEndTime")
        self._EvidenceUrl = params.get("EvidenceUrl")
        self._EvidenceStartTime = params.get("EvidenceStartTime")
        self._EvidenceEndTime = params.get("EvidenceEndTime")
        self._RequestId = params.get("RequestId")


class FakeURLInfo(AbstractModel):
    """仿冒网站信息

    """

    def __init__(self):
        r"""
        :param _FakeURLId: 仿冒网址ID
        :type FakeURLId: int
        :param _ProtectWeb: 保护网站
        :type ProtectWeb: str
        :param _DetectTime: 检测时间
        :type DetectTime: str
        :param _FakeURL: 仿冒网址
        :type FakeURL: str
        :param _Snapshot: 截图
        :type Snapshot: str
        :param _IP: IP地址
        :type IP: str
        :param _IPLoc: IP地理位置
        :type IPLoc: str
        :param _Heat: 热度
        :type Heat: int
        :param _Status: 网址状态
        :type Status: int
        :param _Note: 备注
        :type Note: str
        :param _FakeURLCompany: 仿冒网站所属单位
        :type FakeURLCompany: str
        :param _FakeURLAttr: 仿冒网站性质
        :type FakeURLAttr: str
        :param _FakeURLName: 仿冒网站名称
        :type FakeURLName: str
        :param _FakeURLICP: 仿冒网站备案号
        :type FakeURLICP: str
        :param _FakeURLCreateTime: 仿冒网站创建时间
        :type FakeURLCreateTime: str
        :param _FakeURLExpireTime: 仿冒网站过期时间
        :type FakeURLExpireTime: str
        """
        self._FakeURLId = None
        self._ProtectWeb = None
        self._DetectTime = None
        self._FakeURL = None
        self._Snapshot = None
        self._IP = None
        self._IPLoc = None
        self._Heat = None
        self._Status = None
        self._Note = None
        self._FakeURLCompany = None
        self._FakeURLAttr = None
        self._FakeURLName = None
        self._FakeURLICP = None
        self._FakeURLCreateTime = None
        self._FakeURLExpireTime = None

    @property
    def FakeURLId(self):
        return self._FakeURLId

    @FakeURLId.setter
    def FakeURLId(self, FakeURLId):
        self._FakeURLId = FakeURLId

    @property
    def ProtectWeb(self):
        return self._ProtectWeb

    @ProtectWeb.setter
    def ProtectWeb(self, ProtectWeb):
        self._ProtectWeb = ProtectWeb

    @property
    def DetectTime(self):
        return self._DetectTime

    @DetectTime.setter
    def DetectTime(self, DetectTime):
        self._DetectTime = DetectTime

    @property
    def FakeURL(self):
        return self._FakeURL

    @FakeURL.setter
    def FakeURL(self, FakeURL):
        self._FakeURL = FakeURL

    @property
    def Snapshot(self):
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def IPLoc(self):
        return self._IPLoc

    @IPLoc.setter
    def IPLoc(self, IPLoc):
        self._IPLoc = IPLoc

    @property
    def Heat(self):
        return self._Heat

    @Heat.setter
    def Heat(self, Heat):
        self._Heat = Heat

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def FakeURLCompany(self):
        return self._FakeURLCompany

    @FakeURLCompany.setter
    def FakeURLCompany(self, FakeURLCompany):
        self._FakeURLCompany = FakeURLCompany

    @property
    def FakeURLAttr(self):
        return self._FakeURLAttr

    @FakeURLAttr.setter
    def FakeURLAttr(self, FakeURLAttr):
        self._FakeURLAttr = FakeURLAttr

    @property
    def FakeURLName(self):
        return self._FakeURLName

    @FakeURLName.setter
    def FakeURLName(self, FakeURLName):
        self._FakeURLName = FakeURLName

    @property
    def FakeURLICP(self):
        return self._FakeURLICP

    @FakeURLICP.setter
    def FakeURLICP(self, FakeURLICP):
        self._FakeURLICP = FakeURLICP

    @property
    def FakeURLCreateTime(self):
        return self._FakeURLCreateTime

    @FakeURLCreateTime.setter
    def FakeURLCreateTime(self, FakeURLCreateTime):
        self._FakeURLCreateTime = FakeURLCreateTime

    @property
    def FakeURLExpireTime(self):
        return self._FakeURLExpireTime

    @FakeURLExpireTime.setter
    def FakeURLExpireTime(self, FakeURLExpireTime):
        self._FakeURLExpireTime = FakeURLExpireTime


    def _deserialize(self, params):
        self._FakeURLId = params.get("FakeURLId")
        self._ProtectWeb = params.get("ProtectWeb")
        self._DetectTime = params.get("DetectTime")
        self._FakeURL = params.get("FakeURL")
        self._Snapshot = params.get("Snapshot")
        self._IP = params.get("IP")
        self._IPLoc = params.get("IPLoc")
        self._Heat = params.get("Heat")
        self._Status = params.get("Status")
        self._Note = params.get("Note")
        self._FakeURLCompany = params.get("FakeURLCompany")
        self._FakeURLAttr = params.get("FakeURLAttr")
        self._FakeURLName = params.get("FakeURLName")
        self._FakeURLICP = params.get("FakeURLICP")
        self._FakeURLCreateTime = params.get("FakeURLCreateTime")
        self._FakeURLExpireTime = params.get("FakeURLExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class File(AbstractModel):
    """权属文件列表

    """

    def __init__(self):
        r"""
        :param _FileUrl: 文件下载地址
        :type FileUrl: str
        :param _FileType: 文件类型 1-委托书 2-授权书 5-存证证书 11-营业执照
        :type FileType: int
        :param _ValidStartDate: 文件有效开始日期
        :type ValidStartDate: str
        :param _ValidEndDate: 文件有效截止日期
        :type ValidEndDate: str
        """
        self._FileUrl = None
        self._FileType = None
        self._ValidStartDate = None
        self._ValidEndDate = None

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def ValidStartDate(self):
        return self._ValidStartDate

    @ValidStartDate.setter
    def ValidStartDate(self, ValidStartDate):
        self._ValidStartDate = ValidStartDate

    @property
    def ValidEndDate(self):
        return self._ValidEndDate

    @ValidEndDate.setter
    def ValidEndDate(self, ValidEndDate):
        self._ValidEndDate = ValidEndDate


    def _deserialize(self, params):
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        self._ValidStartDate = params.get("ValidStartDate")
        self._ValidEndDate = params.get("ValidEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤参数

    """


class ModifyBPOfflineAttachmentRequest(AbstractModel):
    """ModifyBPOfflineAttachment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseName: 营业执照
        :type LicenseName: str
        :param _AuthorizationName: 授权书
        :type AuthorizationName: str
        :param _BrandName: 商标名称
        :type BrandName: str
        :param _BrandCertificateName: 商标证明
        :type BrandCertificateName: str
        :param _TransferName: 商标转让证明
        :type TransferName: str
        """
        self._LicenseName = None
        self._AuthorizationName = None
        self._BrandName = None
        self._BrandCertificateName = None
        self._TransferName = None

    @property
    def LicenseName(self):
        return self._LicenseName

    @LicenseName.setter
    def LicenseName(self, LicenseName):
        self._LicenseName = LicenseName

    @property
    def AuthorizationName(self):
        return self._AuthorizationName

    @AuthorizationName.setter
    def AuthorizationName(self, AuthorizationName):
        self._AuthorizationName = AuthorizationName

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def BrandCertificateName(self):
        return self._BrandCertificateName

    @BrandCertificateName.setter
    def BrandCertificateName(self, BrandCertificateName):
        self._BrandCertificateName = BrandCertificateName

    @property
    def TransferName(self):
        return self._TransferName

    @TransferName.setter
    def TransferName(self, TransferName):
        self._TransferName = TransferName


    def _deserialize(self, params):
        self._LicenseName = params.get("LicenseName")
        self._AuthorizationName = params.get("AuthorizationName")
        self._BrandName = params.get("BrandName")
        self._BrandCertificateName = params.get("BrandCertificateName")
        self._TransferName = params.get("TransferName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBPOfflineAttachmentResponse(AbstractModel):
    """ModifyBPOfflineAttachment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCRBlockStatusRequest(AbstractModel):
    """ModifyCRBlockStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TortId: 侵权ID
        :type TortId: int
        :param _BlockUrl: 拦截结果回调地址
        :type BlockUrl: str
        """
        self._TortId = None
        self._BlockUrl = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def BlockUrl(self):
        return self._BlockUrl

    @BlockUrl.setter
    def BlockUrl(self, BlockUrl):
        self._BlockUrl = BlockUrl


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        self._BlockUrl = params.get("BlockUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRBlockStatusResponse(AbstractModel):
    """ModifyCRBlockStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCRMonitorRequest(AbstractModel):
    """ModifyCRMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _MonitorStatus: 监测状态：1-开启监测 2-关闭监测
        :type MonitorStatus: str
        :param _MonitorEnd: 监测截止时间
        :type MonitorEnd: str
        """
        self._WorkId = None
        self._MonitorStatus = None
        self._MonitorEnd = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def MonitorEnd(self):
        return self._MonitorEnd

    @MonitorEnd.setter
    def MonitorEnd(self, MonitorEnd):
        self._MonitorEnd = MonitorEnd


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._MonitorStatus = params.get("MonitorStatus")
        self._MonitorEnd = params.get("MonitorEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRMonitorResponse(AbstractModel):
    """ModifyCRMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCRObtainStatusRequest(AbstractModel):
    """ModifyCRObtainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TortId: 侵权ID
        :type TortId: int
        :param _ObtainType: 取证类型：1-网页取证 2-过程取证(暂不提供)
        :type ObtainType: int
        :param _ObtainDuration: 过程取证的取证时长，单位分钟，范围0-120
        :type ObtainDuration: int
        :param _ObtainUrl: 取证结果回调地址
        :type ObtainUrl: str
        """
        self._TortId = None
        self._ObtainType = None
        self._ObtainDuration = None
        self._ObtainUrl = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def ObtainType(self):
        return self._ObtainType

    @ObtainType.setter
    def ObtainType(self, ObtainType):
        self._ObtainType = ObtainType

    @property
    def ObtainDuration(self):
        return self._ObtainDuration

    @ObtainDuration.setter
    def ObtainDuration(self, ObtainDuration):
        self._ObtainDuration = ObtainDuration

    @property
    def ObtainUrl(self):
        return self._ObtainUrl

    @ObtainUrl.setter
    def ObtainUrl(self, ObtainUrl):
        self._ObtainUrl = ObtainUrl


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        self._ObtainType = params.get("ObtainType")
        self._ObtainDuration = params.get("ObtainDuration")
        self._ObtainUrl = params.get("ObtainUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRObtainStatusResponse(AbstractModel):
    """ModifyCRObtainStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCRRightStatusRequest(AbstractModel):
    """ModifyCRRightStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TortId: 侵权ID
        :type TortId: int
        :param _RightUrl: 发函结果回调地址
        :type RightUrl: str
        """
        self._TortId = None
        self._RightUrl = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def RightUrl(self):
        return self._RightUrl

    @RightUrl.setter
    def RightUrl(self, RightUrl):
        self._RightUrl = RightUrl


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        self._RightUrl = params.get("RightUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRRightStatusResponse(AbstractModel):
    """ModifyCRRightStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCRWhiteListRequest(AbstractModel):
    """ModifyCRWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WhiteListId: 该字段已废弃，白名单ID
        :type WhiteListId: int
        :param _PlatForm: 该字段已废弃，平台名称
        :type PlatForm: str
        :param _PlatUrl: 该字段已废弃，平台站点链接
        :type PlatUrl: str
        :param _AuthorId: 该字段已废弃，作者ID
        :type AuthorId: str
        :param _WorksId: 该字段已废弃，作品ID
        :type WorksId: int
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _WhiteSites: 白名单列表，以\n分割
        :type WhiteSites: str
        """
        self._WhiteListId = None
        self._PlatForm = None
        self._PlatUrl = None
        self._AuthorId = None
        self._WorksId = None
        self._WorkId = None
        self._WhiteSites = None

    @property
    def WhiteListId(self):
        return self._WhiteListId

    @WhiteListId.setter
    def WhiteListId(self, WhiteListId):
        self._WhiteListId = WhiteListId

    @property
    def PlatForm(self):
        return self._PlatForm

    @PlatForm.setter
    def PlatForm(self, PlatForm):
        self._PlatForm = PlatForm

    @property
    def PlatUrl(self):
        return self._PlatUrl

    @PlatUrl.setter
    def PlatUrl(self, PlatUrl):
        self._PlatUrl = PlatUrl

    @property
    def AuthorId(self):
        return self._AuthorId

    @AuthorId.setter
    def AuthorId(self, AuthorId):
        self._AuthorId = AuthorId

    @property
    def WorksId(self):
        return self._WorksId

    @WorksId.setter
    def WorksId(self, WorksId):
        self._WorksId = WorksId

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def WhiteSites(self):
        return self._WhiteSites

    @WhiteSites.setter
    def WhiteSites(self, WhiteSites):
        self._WhiteSites = WhiteSites


    def _deserialize(self, params):
        self._WhiteListId = params.get("WhiteListId")
        self._PlatForm = params.get("PlatForm")
        self._PlatUrl = params.get("PlatUrl")
        self._AuthorId = params.get("AuthorId")
        self._WorksId = params.get("WorksId")
        self._WorkId = params.get("WorkId")
        self._WhiteSites = params.get("WhiteSites")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRWhiteListResponse(AbstractModel):
    """ModifyCRWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Monitor(AbstractModel):
    """版权保护-监测结果

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _WorkName: 作品名称
        :type WorkName: str
        :param _WorkType: 作品内容类型 01-视频 02-音频 03-文本 04-图片
        :type WorkType: str
        :param _TortPlatNum: 侵权平台数量
        :type TortPlatNum: int
        :param _TortURLNum: 侵权链接数量
        :type TortURLNum: int
        :param _MonitorTime: 监测时间
        :type MonitorTime: str
        :param _MonitorStatus: 0-待监测 1-监测中 2-不监测 3-暂停监测
        :type MonitorStatus: int
        :param _WorkCategory: 作品类型
        :type WorkCategory: str
        :param _InsertTime: 新增时间
        :type InsertTime: str
        :param _MonitorNote: 监测状态说明
        :type MonitorNote: str
        :param _WorkCategoryAll: 作品类型全部展示
        :type WorkCategoryAll: str
        :param _EvidenceStatus: 存证状态
        :type EvidenceStatus: int
        :param _EvidenceNote: 存证状态说明
        :type EvidenceNote: str
        :param _TortSiteNum: 侵权站点数量
        :type TortSiteNum: int
        :param _MonitorEndTime: 监测截止时间
        :type MonitorEndTime: str
        :param _AutoRenew: 是否自动续费
        :type AutoRenew: int
        """
        self._WorkId = None
        self._WorkName = None
        self._WorkType = None
        self._TortPlatNum = None
        self._TortURLNum = None
        self._MonitorTime = None
        self._MonitorStatus = None
        self._WorkCategory = None
        self._InsertTime = None
        self._MonitorNote = None
        self._WorkCategoryAll = None
        self._EvidenceStatus = None
        self._EvidenceNote = None
        self._TortSiteNum = None
        self._MonitorEndTime = None
        self._AutoRenew = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def WorkName(self):
        return self._WorkName

    @WorkName.setter
    def WorkName(self, WorkName):
        self._WorkName = WorkName

    @property
    def WorkType(self):
        return self._WorkType

    @WorkType.setter
    def WorkType(self, WorkType):
        self._WorkType = WorkType

    @property
    def TortPlatNum(self):
        return self._TortPlatNum

    @TortPlatNum.setter
    def TortPlatNum(self, TortPlatNum):
        self._TortPlatNum = TortPlatNum

    @property
    def TortURLNum(self):
        return self._TortURLNum

    @TortURLNum.setter
    def TortURLNum(self, TortURLNum):
        self._TortURLNum = TortURLNum

    @property
    def MonitorTime(self):
        return self._MonitorTime

    @MonitorTime.setter
    def MonitorTime(self, MonitorTime):
        self._MonitorTime = MonitorTime

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def WorkCategory(self):
        return self._WorkCategory

    @WorkCategory.setter
    def WorkCategory(self, WorkCategory):
        self._WorkCategory = WorkCategory

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def MonitorNote(self):
        return self._MonitorNote

    @MonitorNote.setter
    def MonitorNote(self, MonitorNote):
        self._MonitorNote = MonitorNote

    @property
    def WorkCategoryAll(self):
        return self._WorkCategoryAll

    @WorkCategoryAll.setter
    def WorkCategoryAll(self, WorkCategoryAll):
        self._WorkCategoryAll = WorkCategoryAll

    @property
    def EvidenceStatus(self):
        return self._EvidenceStatus

    @EvidenceStatus.setter
    def EvidenceStatus(self, EvidenceStatus):
        self._EvidenceStatus = EvidenceStatus

    @property
    def EvidenceNote(self):
        return self._EvidenceNote

    @EvidenceNote.setter
    def EvidenceNote(self, EvidenceNote):
        self._EvidenceNote = EvidenceNote

    @property
    def TortSiteNum(self):
        return self._TortSiteNum

    @TortSiteNum.setter
    def TortSiteNum(self, TortSiteNum):
        self._TortSiteNum = TortSiteNum

    @property
    def MonitorEndTime(self):
        return self._MonitorEndTime

    @MonitorEndTime.setter
    def MonitorEndTime(self, MonitorEndTime):
        self._MonitorEndTime = MonitorEndTime

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._WorkName = params.get("WorkName")
        self._WorkType = params.get("WorkType")
        self._TortPlatNum = params.get("TortPlatNum")
        self._TortURLNum = params.get("TortURLNum")
        self._MonitorTime = params.get("MonitorTime")
        self._MonitorStatus = params.get("MonitorStatus")
        self._WorkCategory = params.get("WorkCategory")
        self._InsertTime = params.get("InsertTime")
        self._MonitorNote = params.get("MonitorNote")
        self._WorkCategoryAll = params.get("WorkCategoryAll")
        self._EvidenceStatus = params.get("EvidenceStatus")
        self._EvidenceNote = params.get("EvidenceNote")
        self._TortSiteNum = params.get("TortSiteNum")
        self._MonitorEndTime = params.get("MonitorEndTime")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorTort(AbstractModel):
    """监测侵权信息详情

    """

    def __init__(self):
        r"""
        :param _TortId: 侵权信息ID
        :type TortId: int
        :param _TortTitle: 侵权标题
        :type TortTitle: str
        :param _TortPlat: 侵权平台
        :type TortPlat: str
        :param _TortURL: 侵权链接
        :type TortURL: str
        :param _PubTime: 侵权链接发布时间
        :type PubTime: str
        :param _Author: 作者
        :type Author: str
        :param _DetectTime: 发现时间
        :type DetectTime: str
        :param _ObtainStatus: 取证状态
        :type ObtainStatus: int
        :param _RightStatus: 维权状态
        :type RightStatus: int
        :param _BlockStatus: 拦截状态
        :type BlockStatus: int
        :param _TortNum: 侵权编号
        :type TortNum: str
        :param _ObtainNote: 取证状态说明
        :type ObtainNote: str
        :param _WorkTitle: 作品标题
        :type WorkTitle: str
        :param _TortSite: 侵权站点
        :type TortSite: str
        :param _ICP: ICP备案信息
        :type ICP: str
        :param _RightNote: 维权状态说明
        :type RightNote: str
        :param _ObtainType: 取证类型
        :type ObtainType: int
        :param _BlockNote: 拦截状态说明
        :type BlockNote: str
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _WorkName: 作品名称
        :type WorkName: str
        :param _AuthStatus: 授权书状态
        :type AuthStatus: int
        :param _CommStatus: 委托书状态
        :type CommStatus: int
        :param _EvidenceStatus: 存证证书状态
        :type EvidenceStatus: int
        :param _IsProducer: 是否著作权人
        :type IsProducer: int
        :param _IsOverseas: 是否境外网址
        :type IsOverseas: int
        :param _IPLoc: ip地理位置
        :type IPLoc: str
        """
        self._TortId = None
        self._TortTitle = None
        self._TortPlat = None
        self._TortURL = None
        self._PubTime = None
        self._Author = None
        self._DetectTime = None
        self._ObtainStatus = None
        self._RightStatus = None
        self._BlockStatus = None
        self._TortNum = None
        self._ObtainNote = None
        self._WorkTitle = None
        self._TortSite = None
        self._ICP = None
        self._RightNote = None
        self._ObtainType = None
        self._BlockNote = None
        self._WorkId = None
        self._WorkName = None
        self._AuthStatus = None
        self._CommStatus = None
        self._EvidenceStatus = None
        self._IsProducer = None
        self._IsOverseas = None
        self._IPLoc = None

    @property
    def TortId(self):
        return self._TortId

    @TortId.setter
    def TortId(self, TortId):
        self._TortId = TortId

    @property
    def TortTitle(self):
        return self._TortTitle

    @TortTitle.setter
    def TortTitle(self, TortTitle):
        self._TortTitle = TortTitle

    @property
    def TortPlat(self):
        return self._TortPlat

    @TortPlat.setter
    def TortPlat(self, TortPlat):
        self._TortPlat = TortPlat

    @property
    def TortURL(self):
        return self._TortURL

    @TortURL.setter
    def TortURL(self, TortURL):
        self._TortURL = TortURL

    @property
    def PubTime(self):
        return self._PubTime

    @PubTime.setter
    def PubTime(self, PubTime):
        self._PubTime = PubTime

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def DetectTime(self):
        return self._DetectTime

    @DetectTime.setter
    def DetectTime(self, DetectTime):
        self._DetectTime = DetectTime

    @property
    def ObtainStatus(self):
        return self._ObtainStatus

    @ObtainStatus.setter
    def ObtainStatus(self, ObtainStatus):
        self._ObtainStatus = ObtainStatus

    @property
    def RightStatus(self):
        return self._RightStatus

    @RightStatus.setter
    def RightStatus(self, RightStatus):
        self._RightStatus = RightStatus

    @property
    def BlockStatus(self):
        return self._BlockStatus

    @BlockStatus.setter
    def BlockStatus(self, BlockStatus):
        self._BlockStatus = BlockStatus

    @property
    def TortNum(self):
        return self._TortNum

    @TortNum.setter
    def TortNum(self, TortNum):
        self._TortNum = TortNum

    @property
    def ObtainNote(self):
        return self._ObtainNote

    @ObtainNote.setter
    def ObtainNote(self, ObtainNote):
        self._ObtainNote = ObtainNote

    @property
    def WorkTitle(self):
        return self._WorkTitle

    @WorkTitle.setter
    def WorkTitle(self, WorkTitle):
        self._WorkTitle = WorkTitle

    @property
    def TortSite(self):
        return self._TortSite

    @TortSite.setter
    def TortSite(self, TortSite):
        self._TortSite = TortSite

    @property
    def ICP(self):
        return self._ICP

    @ICP.setter
    def ICP(self, ICP):
        self._ICP = ICP

    @property
    def RightNote(self):
        return self._RightNote

    @RightNote.setter
    def RightNote(self, RightNote):
        self._RightNote = RightNote

    @property
    def ObtainType(self):
        return self._ObtainType

    @ObtainType.setter
    def ObtainType(self, ObtainType):
        self._ObtainType = ObtainType

    @property
    def BlockNote(self):
        return self._BlockNote

    @BlockNote.setter
    def BlockNote(self, BlockNote):
        self._BlockNote = BlockNote

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def WorkName(self):
        return self._WorkName

    @WorkName.setter
    def WorkName(self, WorkName):
        self._WorkName = WorkName

    @property
    def AuthStatus(self):
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def CommStatus(self):
        return self._CommStatus

    @CommStatus.setter
    def CommStatus(self, CommStatus):
        self._CommStatus = CommStatus

    @property
    def EvidenceStatus(self):
        return self._EvidenceStatus

    @EvidenceStatus.setter
    def EvidenceStatus(self, EvidenceStatus):
        self._EvidenceStatus = EvidenceStatus

    @property
    def IsProducer(self):
        return self._IsProducer

    @IsProducer.setter
    def IsProducer(self, IsProducer):
        self._IsProducer = IsProducer

    @property
    def IsOverseas(self):
        return self._IsOverseas

    @IsOverseas.setter
    def IsOverseas(self, IsOverseas):
        self._IsOverseas = IsOverseas

    @property
    def IPLoc(self):
        return self._IPLoc

    @IPLoc.setter
    def IPLoc(self, IPLoc):
        self._IPLoc = IPLoc


    def _deserialize(self, params):
        self._TortId = params.get("TortId")
        self._TortTitle = params.get("TortTitle")
        self._TortPlat = params.get("TortPlat")
        self._TortURL = params.get("TortURL")
        self._PubTime = params.get("PubTime")
        self._Author = params.get("Author")
        self._DetectTime = params.get("DetectTime")
        self._ObtainStatus = params.get("ObtainStatus")
        self._RightStatus = params.get("RightStatus")
        self._BlockStatus = params.get("BlockStatus")
        self._TortNum = params.get("TortNum")
        self._ObtainNote = params.get("ObtainNote")
        self._WorkTitle = params.get("WorkTitle")
        self._TortSite = params.get("TortSite")
        self._ICP = params.get("ICP")
        self._RightNote = params.get("RightNote")
        self._ObtainType = params.get("ObtainType")
        self._BlockNote = params.get("BlockNote")
        self._WorkId = params.get("WorkId")
        self._WorkName = params.get("WorkName")
        self._AuthStatus = params.get("AuthStatus")
        self._CommStatus = params.get("CommStatus")
        self._EvidenceStatus = params.get("EvidenceStatus")
        self._IsProducer = params.get("IsProducer")
        self._IsOverseas = params.get("IsOverseas")
        self._IPLoc = params.get("IPLoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectURLInfo(AbstractModel):
    """保护网站信息

    """

    def __init__(self):
        r"""
        :param _ProtectURLId: 保护网站ID
        :type ProtectURLId: int
        :param _ProtectURL: 保护网站
        :type ProtectURL: str
        :param _ProtectWeb: 保护网站名称
        :type ProtectWeb: str
        :param _ProtectURLStatus: 保护网站审核状态 1-审核中 2-审核不通过 3-审核通过
        :type ProtectURLStatus: int
        :param _ProtectURLNote: 网站审核不通过原因
        :type ProtectURLNote: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ProtectURLId = None
        self._ProtectURL = None
        self._ProtectWeb = None
        self._ProtectURLStatus = None
        self._ProtectURLNote = None
        self._CreateTime = None

    @property
    def ProtectURLId(self):
        return self._ProtectURLId

    @ProtectURLId.setter
    def ProtectURLId(self, ProtectURLId):
        self._ProtectURLId = ProtectURLId

    @property
    def ProtectURL(self):
        return self._ProtectURL

    @ProtectURL.setter
    def ProtectURL(self, ProtectURL):
        self._ProtectURL = ProtectURL

    @property
    def ProtectWeb(self):
        return self._ProtectWeb

    @ProtectWeb.setter
    def ProtectWeb(self, ProtectWeb):
        self._ProtectWeb = ProtectWeb

    @property
    def ProtectURLStatus(self):
        return self._ProtectURLStatus

    @ProtectURLStatus.setter
    def ProtectURLStatus(self, ProtectURLStatus):
        self._ProtectURLStatus = ProtectURLStatus

    @property
    def ProtectURLNote(self):
        return self._ProtectURLNote

    @ProtectURLNote.setter
    def ProtectURLNote(self, ProtectURLNote):
        self._ProtectURLNote = ProtectURLNote

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProtectURLId = params.get("ProtectURLId")
        self._ProtectURL = params.get("ProtectURL")
        self._ProtectWeb = params.get("ProtectWeb")
        self._ProtectURLStatus = params.get("ProtectURLStatus")
        self._ProtectURLNote = params.get("ProtectURLNote")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFakeURLInfo(AbstractModel):
    """举报网址信息

    """

    def __init__(self):
        r"""
        :param _FakeURLId: 仿冒网址ID
        :type FakeURLId: int
        :param _DetectTime: 检测时间
        :type DetectTime: str
        :param _ProtectURL: 保护网站
        :type ProtectURL: str
        :param _ProtectWeb: 保护网站名称
        :type ProtectWeb: str
        :param _FakeURL: 仿冒网址
        :type FakeURL: str
        :param _Snapshot: 截图
        :type Snapshot: str
        :param _IP: IP地址
        :type IP: str
        :param _IPLoc: IP地理位置
        :type IPLoc: str
        :param _Heat: 热度
        :type Heat: int
        :param _Status: 网站状态
        :type Status: int
        :param _Note: 网站不处理原因
        :type Note: str
        :param _FakeURLCompany: 仿冒网站的企业名称
        :type FakeURLCompany: str
        :param _FakeURLAttr: 仿冒网站的网站性质
        :type FakeURLAttr: str
        :param _FakeURLName: 仿冒网站的网站名称
        :type FakeURLName: str
        :param _FakeURLICP: 仿冒网站的备案
        :type FakeURLICP: str
        :param _FakeURLCreateTime: 仿冒网站创建时间
        :type FakeURLCreateTime: str
        :param _FakeURLExpireTime: 仿冒网站过期时间
        :type FakeURLExpireTime: str
        :param _BlockTime: 协查处置时间
        :type BlockTime: str
        """
        self._FakeURLId = None
        self._DetectTime = None
        self._ProtectURL = None
        self._ProtectWeb = None
        self._FakeURL = None
        self._Snapshot = None
        self._IP = None
        self._IPLoc = None
        self._Heat = None
        self._Status = None
        self._Note = None
        self._FakeURLCompany = None
        self._FakeURLAttr = None
        self._FakeURLName = None
        self._FakeURLICP = None
        self._FakeURLCreateTime = None
        self._FakeURLExpireTime = None
        self._BlockTime = None

    @property
    def FakeURLId(self):
        return self._FakeURLId

    @FakeURLId.setter
    def FakeURLId(self, FakeURLId):
        self._FakeURLId = FakeURLId

    @property
    def DetectTime(self):
        return self._DetectTime

    @DetectTime.setter
    def DetectTime(self, DetectTime):
        self._DetectTime = DetectTime

    @property
    def ProtectURL(self):
        return self._ProtectURL

    @ProtectURL.setter
    def ProtectURL(self, ProtectURL):
        self._ProtectURL = ProtectURL

    @property
    def ProtectWeb(self):
        return self._ProtectWeb

    @ProtectWeb.setter
    def ProtectWeb(self, ProtectWeb):
        self._ProtectWeb = ProtectWeb

    @property
    def FakeURL(self):
        return self._FakeURL

    @FakeURL.setter
    def FakeURL(self, FakeURL):
        self._FakeURL = FakeURL

    @property
    def Snapshot(self):
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def IPLoc(self):
        return self._IPLoc

    @IPLoc.setter
    def IPLoc(self, IPLoc):
        self._IPLoc = IPLoc

    @property
    def Heat(self):
        return self._Heat

    @Heat.setter
    def Heat(self, Heat):
        self._Heat = Heat

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def FakeURLCompany(self):
        return self._FakeURLCompany

    @FakeURLCompany.setter
    def FakeURLCompany(self, FakeURLCompany):
        self._FakeURLCompany = FakeURLCompany

    @property
    def FakeURLAttr(self):
        return self._FakeURLAttr

    @FakeURLAttr.setter
    def FakeURLAttr(self, FakeURLAttr):
        self._FakeURLAttr = FakeURLAttr

    @property
    def FakeURLName(self):
        return self._FakeURLName

    @FakeURLName.setter
    def FakeURLName(self, FakeURLName):
        self._FakeURLName = FakeURLName

    @property
    def FakeURLICP(self):
        return self._FakeURLICP

    @FakeURLICP.setter
    def FakeURLICP(self, FakeURLICP):
        self._FakeURLICP = FakeURLICP

    @property
    def FakeURLCreateTime(self):
        return self._FakeURLCreateTime

    @FakeURLCreateTime.setter
    def FakeURLCreateTime(self, FakeURLCreateTime):
        self._FakeURLCreateTime = FakeURLCreateTime

    @property
    def FakeURLExpireTime(self):
        return self._FakeURLExpireTime

    @FakeURLExpireTime.setter
    def FakeURLExpireTime(self, FakeURLExpireTime):
        self._FakeURLExpireTime = FakeURLExpireTime

    @property
    def BlockTime(self):
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime


    def _deserialize(self, params):
        self._FakeURLId = params.get("FakeURLId")
        self._DetectTime = params.get("DetectTime")
        self._ProtectURL = params.get("ProtectURL")
        self._ProtectWeb = params.get("ProtectWeb")
        self._FakeURL = params.get("FakeURL")
        self._Snapshot = params.get("Snapshot")
        self._IP = params.get("IP")
        self._IPLoc = params.get("IPLoc")
        self._Heat = params.get("Heat")
        self._Status = params.get("Status")
        self._Note = params.get("Note")
        self._FakeURLCompany = params.get("FakeURLCompany")
        self._FakeURLAttr = params.get("FakeURLAttr")
        self._FakeURLName = params.get("FakeURLName")
        self._FakeURLICP = params.get("FakeURLICP")
        self._FakeURLCreateTime = params.get("FakeURLCreateTime")
        self._FakeURLExpireTime = params.get("FakeURLExpireTime")
        self._BlockTime = params.get("BlockTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCRWorkRequest(AbstractModel):
    """UpdateCRWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _ContentType: 文件的扩展名，例如txt，docx
        :type ContentType: str
        :param _Content: 内容的base64编码
        :type Content: str
        :param _CertType: 本次存证类型：0-不存证 1-存当前文件 2-存历史全量文件
        :type CertType: str
        """
        self._WorkId = None
        self._ContentType = None
        self._Content = None
        self._CertType = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._ContentType = params.get("ContentType")
        self._Content = params.get("Content")
        self._CertType = params.get("CertType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCRWorkResponse(AbstractModel):
    """UpdateCRWork返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkId: 作品ID
        :type WorkId: int
        :param _EvidenceId: 存证ID
        :type EvidenceId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def WorkId(self):
        return self._WorkId

    @WorkId.setter
    def WorkId(self, WorkId):
        self._WorkId = WorkId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkId = params.get("WorkId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")