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
        :param BrandName: 商标名称
        :type BrandName: str
        :param BrandCertificateName: 商标证明
        :type BrandCertificateName: str
        :param BrandStatus: 商标审核状态 1-审核中 2-审核未通过 3-审核通过
        :type BrandStatus: int
        :param BrandNote: 审核说明
        :type BrandNote: str
        :param TransferName: 商标转让证明
        :type TransferName: str
        :param TransferStatus: 商标转让证明审核状态
        :type TransferStatus: int
        :param TransferNote: 审核说明 1-审核中 2-审核未通过 3-审核通过
        :type TransferNote: str
        """
        self.BrandName = None
        self.BrandCertificateName = None
        self.BrandStatus = None
        self.BrandNote = None
        self.TransferName = None
        self.TransferStatus = None
        self.TransferNote = None


    def _deserialize(self, params):
        self.BrandName = params.get("BrandName")
        self.BrandCertificateName = params.get("BrandCertificateName")
        self.BrandStatus = params.get("BrandStatus")
        self.BrandNote = params.get("BrandNote")
        self.TransferName = params.get("TransferName")
        self.TransferStatus = params.get("TransferStatus")
        self.TransferNote = params.get("TransferNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLRequest(AbstractModel):
    """CreateBPFakeURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProtectURLId: 保护网址ID
        :type ProtectURLId: int
        :param FakeURL: 仿冒网址
        :type FakeURL: str
        :param SnapshotNames: 截图
        :type SnapshotNames: list of str
        :param Note: 举报说明
        :type Note: str
        """
        self.ProtectURLId = None
        self.FakeURL = None
        self.SnapshotNames = None
        self.Note = None


    def _deserialize(self, params):
        self.ProtectURLId = params.get("ProtectURLId")
        self.FakeURL = params.get("FakeURL")
        self.SnapshotNames = params.get("SnapshotNames")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLResponse(AbstractModel):
    """CreateBPFakeURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPFalseTicketRequest(AbstractModel):
    """CreateBPFalseTicket请求参数结构体

    """

    def __init__(self):
        r"""
        :param FakeURL: 仿冒网址
        :type FakeURL: str
        """
        self.FakeURL = None


    def _deserialize(self, params):
        self.FakeURL = params.get("FakeURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFalseTicketResponse(AbstractModel):
    """CreateBPFalseTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPOfflineAttachmentRequest(AbstractModel):
    """CreateBPOfflineAttachment请求参数结构体

    """

    def __init__(self):
        r"""
        :param BrandName: 品牌名字
        :type BrandName: str
        :param BrandCertificateName: 商标证明
        :type BrandCertificateName: str
        :param TransferName: 商标转让证明
        :type TransferName: str
        :param AuthorizationName: 授权书
        :type AuthorizationName: str
        """
        self.BrandName = None
        self.BrandCertificateName = None
        self.TransferName = None
        self.AuthorizationName = None


    def _deserialize(self, params):
        self.BrandName = params.get("BrandName")
        self.BrandCertificateName = params.get("BrandCertificateName")
        self.TransferName = params.get("TransferName")
        self.AuthorizationName = params.get("AuthorizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPOfflineAttachmentResponse(AbstractModel):
    """CreateBPOfflineAttachment返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPOfflineTicketRequest(AbstractModel):
    """CreateBPOfflineTicket请求参数结构体

    """

    def __init__(self):
        r"""
        :param FakeURLId: 仿冒网址ID
        :type FakeURLId: int
        """
        self.FakeURLId = None


    def _deserialize(self, params):
        self.FakeURLId = params.get("FakeURLId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPOfflineTicketResponse(AbstractModel):
    """CreateBPOfflineTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPProtectURLsRequest(AbstractModel):
    """CreateBPProtectURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyName: 企业名称
        :type CompanyName: str
        :param Phone: 电话号码
        :type Phone: str
        :param LicenseName: 营业执照
        :type LicenseName: str
        :param ProtectURLs: 保护网站
        :type ProtectURLs: list of str
        :param ProtectWebs: 网站名称
        :type ProtectWebs: list of str
        """
        self.CompanyName = None
        self.Phone = None
        self.LicenseName = None
        self.ProtectURLs = None
        self.ProtectWebs = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.Phone = params.get("Phone")
        self.LicenseName = params.get("LicenseName")
        self.ProtectURLs = params.get("ProtectURLs")
        self.ProtectWebs = params.get("ProtectWebs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPProtectURLsResponse(AbstractModel):
    """CreateBPProtectURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCRBlockRequest(AbstractModel):
    """CreateCRBlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param TortUrl: 侵权链接
        :type TortUrl: str
        :param TortTitle: 侵权标题
        :type TortTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param BlockUrl: 拦截结果回调地址
        :type BlockUrl: str
        :param FileUrl: 授权书下载地址
        :type FileUrl: str
        :param ValidStartDate: 授权书生效日期
        :type ValidStartDate: str
        :param ValidEndDate: 授权书截止日期
        :type ValidEndDate: str
        :param TortPic: 侵权截图
        :type TortPic: str
        :param CommFileUrl: 委托书下载地址
        :type CommFileUrl: str
        :param CommValidStartDate: 委托书生效日期
        :type CommValidStartDate: str
        :param CommValidEndDate: 委托书截止日期
        :type CommValidEndDate: str
        :param IsProducer: 是否著作权人：0-否 1-是
        :type IsProducer: str
        :param EvidenceFileUrl: 存证证书下载地址
        :type EvidenceFileUrl: str
        :param EvidenceValidStartDate: 存证证书生效日期
        :type EvidenceValidStartDate: str
        :param EvidenceValidEndDate: 存证证书截止日期
        :type EvidenceValidEndDate: str
        """
        self.WorkId = None
        self.TortUrl = None
        self.TortTitle = None
        self.TortPlat = None
        self.BlockUrl = None
        self.FileUrl = None
        self.ValidStartDate = None
        self.ValidEndDate = None
        self.TortPic = None
        self.CommFileUrl = None
        self.CommValidStartDate = None
        self.CommValidEndDate = None
        self.IsProducer = None
        self.EvidenceFileUrl = None
        self.EvidenceValidStartDate = None
        self.EvidenceValidEndDate = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.TortUrl = params.get("TortUrl")
        self.TortTitle = params.get("TortTitle")
        self.TortPlat = params.get("TortPlat")
        self.BlockUrl = params.get("BlockUrl")
        self.FileUrl = params.get("FileUrl")
        self.ValidStartDate = params.get("ValidStartDate")
        self.ValidEndDate = params.get("ValidEndDate")
        self.TortPic = params.get("TortPic")
        self.CommFileUrl = params.get("CommFileUrl")
        self.CommValidStartDate = params.get("CommValidStartDate")
        self.CommValidEndDate = params.get("CommValidEndDate")
        self.IsProducer = params.get("IsProducer")
        self.EvidenceFileUrl = params.get("EvidenceFileUrl")
        self.EvidenceValidStartDate = params.get("EvidenceValidStartDate")
        self.EvidenceValidEndDate = params.get("EvidenceValidEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRBlockResponse(AbstractModel):
    """CreateCRBlock返回参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param TortNum: 该字段已废弃
        :type TortNum: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TortId = None
        self.TortNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.TortNum = params.get("TortNum")
        self.RequestId = params.get("RequestId")


class CreateCRCompanyVerifyRequest(AbstractModel):
    """CreateCRCompanyVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyName: 企业名称
        :type CompanyName: str
        :param CompanyID: 企业证件号码
        :type CompanyID: str
        :param CompanyLegalName: 企业法人姓名
        :type CompanyLegalName: str
        :param ManagerName: 联系人姓名
        :type ManagerName: str
        :param ManagerPhone: 联系人手机号
        :type ManagerPhone: str
        :param VerificationCode: 手机验证码，接口接入可以置空
        :type VerificationCode: str
        :param CompanyIDType: 字段已废弃，企业认证号码类型 1：社会信用代码 2：组织机构代码 3：企业工商注册码 4：其他 默认为1
        :type CompanyIDType: str
        :param Type: 字段已废弃，认证类型
        :type Type: str
        """
        self.CompanyName = None
        self.CompanyID = None
        self.CompanyLegalName = None
        self.ManagerName = None
        self.ManagerPhone = None
        self.VerificationCode = None
        self.CompanyIDType = None
        self.Type = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.CompanyID = params.get("CompanyID")
        self.CompanyLegalName = params.get("CompanyLegalName")
        self.ManagerName = params.get("ManagerName")
        self.ManagerPhone = params.get("ManagerPhone")
        self.VerificationCode = params.get("VerificationCode")
        self.CompanyIDType = params.get("CompanyIDType")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRCompanyVerifyResponse(AbstractModel):
    """CreateCRCompanyVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 认证状态：0-认证成功 1-认证失败
        :type Status: int
        :param Note: 认证状态说明，包括认证失败的原因
        :type Note: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Note = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Note = params.get("Note")
        self.RequestId = params.get("RequestId")


class CreateCRDesktopCodeRequest(AbstractModel):
    """CreateCRDesktopCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: xxx
        :type TortId: int
        :param DesktopCode: xxx
        :type DesktopCode: str
        """
        self.TortId = None
        self.DesktopCode = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.DesktopCode = params.get("DesktopCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRDesktopCodeResponse(AbstractModel):
    """CreateCRDesktopCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCRObtainRequest(AbstractModel):
    """CreateCRObtain请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 已存证的作品ID
        :type WorkId: int
        :param TortUrl: 侵权链接
        :type TortUrl: str
        :param ObtainType: 取证类型 1-网页取证 2-过程取证
        :type ObtainType: int
        :param WorkTitle: 侵权标题
        :type WorkTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param ObtainDuration: 过程取证的取证时长 6-300分钟
        :type ObtainDuration: int
        :param ObtainUrl: 取证回调地址
        :type ObtainUrl: str
        :param WorkCategory: xxx
        :type WorkCategory: str
        :param WorkType: xxx
        :type WorkType: str
        """
        self.WorkId = None
        self.TortUrl = None
        self.ObtainType = None
        self.WorkTitle = None
        self.TortPlat = None
        self.ObtainDuration = None
        self.ObtainUrl = None
        self.WorkCategory = None
        self.WorkType = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.TortUrl = params.get("TortUrl")
        self.ObtainType = params.get("ObtainType")
        self.WorkTitle = params.get("WorkTitle")
        self.TortPlat = params.get("TortPlat")
        self.ObtainDuration = params.get("ObtainDuration")
        self.ObtainUrl = params.get("ObtainUrl")
        self.WorkCategory = params.get("WorkCategory")
        self.WorkType = params.get("WorkType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRObtainResponse(AbstractModel):
    """CreateCRObtain返回参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param TortNum: xxx
        :type TortNum: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TortId = None
        self.TortNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.TortNum = params.get("TortNum")
        self.RequestId = params.get("RequestId")


class CreateCRRightFileRequest(AbstractModel):
    """CreateCRRightFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param FileList: 权属文件列表
        :type FileList: list of File
        """
        self.WorkId = None
        self.FileList = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        if params.get("FileList") is not None:
            self.FileList = []
            for item in params.get("FileList"):
                obj = File()
                obj._deserialize(item)
                self.FileList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRRightFileResponse(AbstractModel):
    """CreateCRRightFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileIds: 权属文件Id，按提交顺序排序
        :type FileIds: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.RequestId = params.get("RequestId")


class CreateCRRightRequest(AbstractModel):
    """CreateCRRight请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param TortUrl: 侵权链接
        :type TortUrl: str
        :param TortTitle: 侵权标题
        :type TortTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param RightUrl: 发函结果回调地址
        :type RightUrl: str
        :param FileUrl: 授权书下载地址
        :type FileUrl: str
        :param ValidStartDate: 授权书生效日期
        :type ValidStartDate: str
        :param ValidEndDate: 授权书截止日期
        :type ValidEndDate: str
        :param CommFileUrl: 委托书下载地址
        :type CommFileUrl: str
        :param CommValidStartDate: 委托书生效日期
        :type CommValidStartDate: str
        :param CommValidEndDate: 委托书截止日期
        :type CommValidEndDate: str
        :param HomeFileUrl: 主页下载地址
        :type HomeFileUrl: str
        :param HomeValidStartDate: 主页生效日期
        :type HomeValidStartDate: str
        :param HomeValidEndDate: 主页截止日期
        :type HomeValidEndDate: str
        :param IsProducer: 是否著作权人：0-否 1-是
        :type IsProducer: str
        :param EvidenceFileUrl: 存证证书下载地址
        :type EvidenceFileUrl: str
        :param EvidenceValidStartDate: 存证证书生效日期
        :type EvidenceValidStartDate: str
        :param EvidenceValidEndDate: 存证证书截止日期
        :type EvidenceValidEndDate: str
        """
        self.WorkId = None
        self.TortUrl = None
        self.TortTitle = None
        self.TortPlat = None
        self.RightUrl = None
        self.FileUrl = None
        self.ValidStartDate = None
        self.ValidEndDate = None
        self.CommFileUrl = None
        self.CommValidStartDate = None
        self.CommValidEndDate = None
        self.HomeFileUrl = None
        self.HomeValidStartDate = None
        self.HomeValidEndDate = None
        self.IsProducer = None
        self.EvidenceFileUrl = None
        self.EvidenceValidStartDate = None
        self.EvidenceValidEndDate = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.TortUrl = params.get("TortUrl")
        self.TortTitle = params.get("TortTitle")
        self.TortPlat = params.get("TortPlat")
        self.RightUrl = params.get("RightUrl")
        self.FileUrl = params.get("FileUrl")
        self.ValidStartDate = params.get("ValidStartDate")
        self.ValidEndDate = params.get("ValidEndDate")
        self.CommFileUrl = params.get("CommFileUrl")
        self.CommValidStartDate = params.get("CommValidStartDate")
        self.CommValidEndDate = params.get("CommValidEndDate")
        self.HomeFileUrl = params.get("HomeFileUrl")
        self.HomeValidStartDate = params.get("HomeValidStartDate")
        self.HomeValidEndDate = params.get("HomeValidEndDate")
        self.IsProducer = params.get("IsProducer")
        self.EvidenceFileUrl = params.get("EvidenceFileUrl")
        self.EvidenceValidStartDate = params.get("EvidenceValidStartDate")
        self.EvidenceValidEndDate = params.get("EvidenceValidEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRRightResponse(AbstractModel):
    """CreateCRRight返回参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param TortNum: 该字段已废弃
        :type TortNum: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TortId = None
        self.TortNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.TortNum = params.get("TortNum")
        self.RequestId = params.get("RequestId")


class CreateCRTortRequest(AbstractModel):
    """CreateCRTort请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param TortURL: 侵权网址
        :type TortURL: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param TortTitle: 侵权标题
        :type TortTitle: str
        """
        self.WorkId = None
        self.TortURL = None
        self.TortPlat = None
        self.TortTitle = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.TortURL = params.get("TortURL")
        self.TortPlat = params.get("TortPlat")
        self.TortTitle = params.get("TortTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRTortResponse(AbstractModel):
    """CreateCRTort返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param TortId: 侵权ID
        :type TortId: int
        :param TortTitle: 侵权标题
        :type TortTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param TortURL: 侵权网址
        :type TortURL: str
        :param TortDomain: 侵权域名
        :type TortDomain: str
        :param TortBodyName: 侵权主体
        :type TortBodyName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkId = None
        self.TortId = None
        self.TortTitle = None
        self.TortPlat = None
        self.TortURL = None
        self.TortDomain = None
        self.TortBodyName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.TortId = params.get("TortId")
        self.TortTitle = params.get("TortTitle")
        self.TortPlat = params.get("TortPlat")
        self.TortURL = params.get("TortURL")
        self.TortDomain = params.get("TortDomain")
        self.TortBodyName = params.get("TortBodyName")
        self.RequestId = params.get("RequestId")


class CreateCRUserVerifyRequest(AbstractModel):
    """CreateCRUserVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserName: 用户真实姓名
        :type UserName: str
        :param UserID: 用户身份证号
        :type UserID: str
        :param UserPhone: 用户手机号码
        :type UserPhone: str
        :param VerificationCode: 短信验证码，接口接入可以置空
        :type VerificationCode: str
        :param Type: 字段已废弃，认证类型
        :type Type: str
        """
        self.UserName = None
        self.UserID = None
        self.UserPhone = None
        self.VerificationCode = None
        self.Type = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserID = params.get("UserID")
        self.UserPhone = params.get("UserPhone")
        self.VerificationCode = params.get("VerificationCode")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRUserVerifyResponse(AbstractModel):
    """CreateCRUserVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 认证状态：0-认证成功 1-认证失败
        :type Status: int
        :param Note: 认证状态说明，包括认证失败原因等
        :type Note: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Note = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Note = params.get("Note")
        self.RequestId = params.get("RequestId")


class CreateCRWorkRequest(AbstractModel):
    """CreateCRWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkName: 作品名称
        :type WorkName: str
        :param WorkCategory: 作品分类
        :type WorkCategory: str
        :param WorkType: 作品内容类型
        :type WorkType: str
        :param WorkSign: 作品标签
        :type WorkSign: str
        :param WorkPic: 字段已废弃，作品图片
        :type WorkPic: str
        :param WorkDesc: 作品描述
        :type WorkDesc: str
        :param IsOriginal: 是否原创：0-否 1-是
        :type IsOriginal: str
        :param IsRelease: 是否发布：0-未发布 1-已发布
        :type IsRelease: str
        :param ProducerID: 字段已废弃，著作权人ID
        :type ProducerID: int
        :param ProduceTime: 创作时间
        :type ProduceTime: str
        :param SampleContentURL: 字段已废弃
        :type SampleContentURL: str
        :param SampleDownloadURL: 作品下载地址
        :type SampleDownloadURL: str
        :param SamplePublicURL: 作品在线地址
        :type SamplePublicURL: str
        :param GrantType: 字段已废弃，授予类型
        :type GrantType: str
        :param IsMonitor: 是否监测：0-不监测 1-监测
        :type IsMonitor: str
        :param IsCert: 是否存证：0-不存证  2-存证 注意是2
        :type IsCert: str
        :param CertUrl: 存证回调地址
        :type CertUrl: str
        :param MonitorUrl: 监测回调地址
        :type MonitorUrl: str
        :param ProduceType: 字段已废弃，创作性质
        :type ProduceType: str
        :param WhiteLists: 白名单列表
        :type WhiteLists: list of str
        :param WorkId: 作品ID，忽略该字段
        :type WorkId: int
        :param ProducerName: 著作权人姓名
        :type ProducerName: str
        :param Nickname: 作者，小说类型必填
        :type Nickname: str
        :param Authorization: 授权书下载地址
        :type Authorization: str
        :param AuthorizationStartTime: 授权书开始时间
        :type AuthorizationStartTime: str
        :param AuthorizationEndTime: 授权书结束时间
        :type AuthorizationEndTime: str
        :param ContentType: 内容格式，支持txt、doc等，表示Content的具体格式
        :type ContentType: str
        :param Content: 文件内容base64编码，该字段仅在无法提供下载链接时使用
        :type Content: str
        :param MonitorEndTime: 监测结束时间
        :type MonitorEndTime: str
        :param ApplierId: 申请人ID，用于存证和取证
        :type ApplierId: str
        :param ApplierName: 申请人姓名，用于存证和取证
        :type ApplierName: str
        """
        self.WorkName = None
        self.WorkCategory = None
        self.WorkType = None
        self.WorkSign = None
        self.WorkPic = None
        self.WorkDesc = None
        self.IsOriginal = None
        self.IsRelease = None
        self.ProducerID = None
        self.ProduceTime = None
        self.SampleContentURL = None
        self.SampleDownloadURL = None
        self.SamplePublicURL = None
        self.GrantType = None
        self.IsMonitor = None
        self.IsCert = None
        self.CertUrl = None
        self.MonitorUrl = None
        self.ProduceType = None
        self.WhiteLists = None
        self.WorkId = None
        self.ProducerName = None
        self.Nickname = None
        self.Authorization = None
        self.AuthorizationStartTime = None
        self.AuthorizationEndTime = None
        self.ContentType = None
        self.Content = None
        self.MonitorEndTime = None
        self.ApplierId = None
        self.ApplierName = None


    def _deserialize(self, params):
        self.WorkName = params.get("WorkName")
        self.WorkCategory = params.get("WorkCategory")
        self.WorkType = params.get("WorkType")
        self.WorkSign = params.get("WorkSign")
        self.WorkPic = params.get("WorkPic")
        self.WorkDesc = params.get("WorkDesc")
        self.IsOriginal = params.get("IsOriginal")
        self.IsRelease = params.get("IsRelease")
        self.ProducerID = params.get("ProducerID")
        self.ProduceTime = params.get("ProduceTime")
        self.SampleContentURL = params.get("SampleContentURL")
        self.SampleDownloadURL = params.get("SampleDownloadURL")
        self.SamplePublicURL = params.get("SamplePublicURL")
        self.GrantType = params.get("GrantType")
        self.IsMonitor = params.get("IsMonitor")
        self.IsCert = params.get("IsCert")
        self.CertUrl = params.get("CertUrl")
        self.MonitorUrl = params.get("MonitorUrl")
        self.ProduceType = params.get("ProduceType")
        self.WhiteLists = params.get("WhiteLists")
        self.WorkId = params.get("WorkId")
        self.ProducerName = params.get("ProducerName")
        self.Nickname = params.get("Nickname")
        self.Authorization = params.get("Authorization")
        self.AuthorizationStartTime = params.get("AuthorizationStartTime")
        self.AuthorizationEndTime = params.get("AuthorizationEndTime")
        self.ContentType = params.get("ContentType")
        self.Content = params.get("Content")
        self.MonitorEndTime = params.get("MonitorEndTime")
        self.ApplierId = params.get("ApplierId")
        self.ApplierName = params.get("ApplierName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRWorkResponse(AbstractModel):
    """CreateCRWork返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID，一个作品对应唯一的workid
        :type WorkId: int
        :param EvidenceId: 存证ID，忽略该字段
        :type EvidenceId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")


class DescribeBPCompanyInfoRequest(AbstractModel):
    """DescribeBPCompanyInfo请求参数结构体

    """


class DescribeBPCompanyInfoResponse(AbstractModel):
    """DescribeBPCompanyInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyName: 企业名称
        :type CompanyName: str
        :param Phone: 电话号码
        :type Phone: str
        :param LicenseName: 营业执照
        :type LicenseName: str
        :param LicenseStatus: 营业执照审核状态 1-审核中 2-审核未通过，3、审核通过
        :type LicenseStatus: int
        :param LicenseNote: 营业执照备注
        :type LicenseNote: str
        :param AuthorizationName: 授权书
        :type AuthorizationName: str
        :param AuthorizationStatus: 授权书审核状态
        :type AuthorizationStatus: int
        :param AuthorizationNote: 授权书备注
        :type AuthorizationNote: str
        :param BrandDatas: 品牌信息
        :type BrandDatas: list of BrandData
        :param CompanyId: 企业ID
        :type CompanyId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyName = None
        self.Phone = None
        self.LicenseName = None
        self.LicenseStatus = None
        self.LicenseNote = None
        self.AuthorizationName = None
        self.AuthorizationStatus = None
        self.AuthorizationNote = None
        self.BrandDatas = None
        self.CompanyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.Phone = params.get("Phone")
        self.LicenseName = params.get("LicenseName")
        self.LicenseStatus = params.get("LicenseStatus")
        self.LicenseNote = params.get("LicenseNote")
        self.AuthorizationName = params.get("AuthorizationName")
        self.AuthorizationStatus = params.get("AuthorizationStatus")
        self.AuthorizationNote = params.get("AuthorizationNote")
        if params.get("BrandDatas") is not None:
            self.BrandDatas = []
            for item in params.get("BrandDatas"):
                obj = BrandData()
                obj._deserialize(item)
                self.BrandDatas.append(obj)
        self.CompanyId = params.get("CompanyId")
        self.RequestId = params.get("RequestId")


class DescribeBPFakeURLsRequest(AbstractModel):
    """DescribeBPFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param PageSize: 页数
        :type PageSize: int
        :param PageNumber: 页码
        :type PageNumber: int
        """
        self.Filters = None
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBPFakeURLsResponse(AbstractModel):
    """DescribeBPFakeURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param FakeURLInfos: 仿冒网址列表
        :type FakeURLInfos: list of FakeURLInfo
        :param TotalCount: 总量
        :type TotalCount: int
        :param ExportURL: 导出量
        :type ExportURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FakeURLInfos = None
        self.TotalCount = None
        self.ExportURL = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FakeURLInfos") is not None:
            self.FakeURLInfos = []
            for item in params.get("FakeURLInfos"):
                obj = FakeURLInfo()
                obj._deserialize(item)
                self.FakeURLInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.ExportURL = params.get("ExportURL")
        self.RequestId = params.get("RequestId")


class DescribeBPProtectURLsRequest(AbstractModel):
    """DescribeBPProtectURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 页数
        :type PageSize: int
        :param PageNumber: 页码
        :type PageNumber: int
        """
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBPProtectURLsResponse(AbstractModel):
    """DescribeBPProtectURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProtectURLInfos: 保护网址列表
        :type ProtectURLInfos: list of ProtectURLInfo
        :param TotalCount: 总量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProtectURLInfos = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProtectURLInfos") is not None:
            self.ProtectURLInfos = []
            for item in params.get("ProtectURLInfos"):
                obj = ProtectURLInfo()
                obj._deserialize(item)
                self.ProtectURLInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBPReportFakeURLsRequest(AbstractModel):
    """DescribeBPReportFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param PageSize: 页数
        :type PageSize: int
        :param PageNumber: 页码
        :type PageNumber: int
        """
        self.Filters = None
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBPReportFakeURLsResponse(AbstractModel):
    """DescribeBPReportFakeURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReportFakeURLInfos: 举报网站列表
        :type ReportFakeURLInfos: list of ReportFakeURLInfo
        :param TotalCount: 总量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReportFakeURLInfos = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReportFakeURLInfos") is not None:
            self.ReportFakeURLInfos = []
            for item in params.get("ReportFakeURLInfos"):
                obj = ReportFakeURLInfo()
                obj._deserialize(item)
                self.ReportFakeURLInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCRMonitorDetailRequest(AbstractModel):
    """DescribeCRMonitorDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param PageSize: 页数
        :type PageSize: int
        :param PageNumber: 页码
        :type PageNumber: int
        :param Filters: 过滤参数
        :type Filters: list of Filter
        """
        self.WorkId = None
        self.PageSize = None
        self.PageNumber = None
        self.Filters = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRMonitorDetailResponse(AbstractModel):
    """DescribeCRMonitorDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Torts: 侵权数组
        :type Torts: list of MonitorTort
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param MonitorStatus: 监测状态
        :type MonitorStatus: int
        :param ExportURL: 导出地址
        :type ExportURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Torts = None
        self.TotalCount = None
        self.MonitorStatus = None
        self.ExportURL = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Torts") is not None:
            self.Torts = []
            for item in params.get("Torts"):
                obj = MonitorTort()
                obj._deserialize(item)
                self.Torts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.MonitorStatus = params.get("MonitorStatus")
        self.ExportURL = params.get("ExportURL")
        self.RequestId = params.get("RequestId")


class DescribeCRMonitorsRequest(AbstractModel):
    """DescribeCRMonitors请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param PageSize: 页数
        :type PageSize: int
        :param PageNumber: 页码
        :type PageNumber: int
        """
        self.Filters = None
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRMonitorsResponse(AbstractModel):
    """DescribeCRMonitors返回参数结构体

    """

    def __init__(self):
        r"""
        :param Monitors: 监测结果
        :type Monitors: list of Monitor
        :param TotalCount: 记录总条数
        :type TotalCount: int
        :param ExportURL: 导出地址
        :type ExportURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Monitors = None
        self.TotalCount = None
        self.ExportURL = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Monitors") is not None:
            self.Monitors = []
            for item in params.get("Monitors"):
                obj = Monitor()
                obj._deserialize(item)
                self.Monitors.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.ExportURL = params.get("ExportURL")
        self.RequestId = params.get("RequestId")


class DescribeCRObtainDetailRequest(AbstractModel):
    """DescribeCRObtainDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        """
        self.TortId = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRObtainDetailResponse(AbstractModel):
    """DescribeCRObtainDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkName: 作品名称
        :type WorkName: str
        :param TortURL: 侵权链接
        :type TortURL: str
        :param ObtainTime: 取证时间
        :type ObtainTime: str
        :param ObtainType: 取证类型
        :type ObtainType: str
        :param ObtainNum: 取证号
        :type ObtainNum: str
        :param DepositFile: 证据地址
        :type DepositFile: str
        :param DepositCert: 公证信息地址
        :type DepositCert: str
        :param WorkType: 内容类型
        :type WorkType: str
        :param WorkCategory: 作品类型
        :type WorkCategory: str
        :param TortId: 侵权ID
        :type TortId: int
        :param TortNum: 侵权编号
        :type TortNum: str
        :param ObtainStatus: 取证状态
        :type ObtainStatus: int
        :param ObtainNote: 取证状态说明
        :type ObtainNote: str
        :param ObtainDuration: 取证时长
        :type ObtainDuration: str
        :param ObtainName: 取证名称
        :type ObtainName: str
        :param DepositPdfCert: 取证公证信息
        :type DepositPdfCert: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkName = None
        self.TortURL = None
        self.ObtainTime = None
        self.ObtainType = None
        self.ObtainNum = None
        self.DepositFile = None
        self.DepositCert = None
        self.WorkType = None
        self.WorkCategory = None
        self.TortId = None
        self.TortNum = None
        self.ObtainStatus = None
        self.ObtainNote = None
        self.ObtainDuration = None
        self.ObtainName = None
        self.DepositPdfCert = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkName = params.get("WorkName")
        self.TortURL = params.get("TortURL")
        self.ObtainTime = params.get("ObtainTime")
        self.ObtainType = params.get("ObtainType")
        self.ObtainNum = params.get("ObtainNum")
        self.DepositFile = params.get("DepositFile")
        self.DepositCert = params.get("DepositCert")
        self.WorkType = params.get("WorkType")
        self.WorkCategory = params.get("WorkCategory")
        self.TortId = params.get("TortId")
        self.TortNum = params.get("TortNum")
        self.ObtainStatus = params.get("ObtainStatus")
        self.ObtainNote = params.get("ObtainNote")
        self.ObtainDuration = params.get("ObtainDuration")
        self.ObtainName = params.get("ObtainName")
        self.DepositPdfCert = params.get("DepositPdfCert")
        self.RequestId = params.get("RequestId")


class DescribeCRWorkInfoRequest(AbstractModel):
    """DescribeCRWorkInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        """
        self.WorkId = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRWorkInfoResponse(AbstractModel):
    """DescribeCRWorkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkName: 作品名称
        :type WorkName: str
        :param MonitorStatus: 监测状态
        :type MonitorStatus: int
        :param AuthStatus: 授权文件状态
        :type AuthStatus: int
        :param CommStatus: 委托书状态
        :type CommStatus: int
        :param IsProducer: 是否著作权人
        :type IsProducer: int
        :param EvidenceStatus: 存证证书状态
        :type EvidenceStatus: int
        :param WorkCategory: 作品类型
        :type WorkCategory: str
        :param IsOriginal: 是否原创
        :type IsOriginal: str
        :param IsRelease: 是否已发表
        :type IsRelease: str
        :param ProducerName: 著作权人姓名
        :type ProducerName: str
        :param ProduceTime: 发表时间
        :type ProduceTime: str
        :param WhiteLists: 白名单
        :type WhiteLists: list of str
        :param WorkDesc: 作品描述
        :type WorkDesc: str
        :param Authorization: 授权书
        :type Authorization: str
        :param AuthorizationStartTime: 授权书生效日期
        :type AuthorizationStartTime: str
        :param AuthorizationEndTime: 授权书截止日期
        :type AuthorizationEndTime: str
        :param Commission: 委托书
        :type Commission: str
        :param CommissionStartTime: 委托书生效日期
        :type CommissionStartTime: str
        :param CommissionEndTime: 委托书截止日期
        :type CommissionEndTime: str
        :param EvidenceUrl: 存证证书
        :type EvidenceUrl: str
        :param EvidenceStartTime: 存证证书生效日期
        :type EvidenceStartTime: str
        :param EvidenceEndTime: 存证证书截止日期
        :type EvidenceEndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkName = None
        self.MonitorStatus = None
        self.AuthStatus = None
        self.CommStatus = None
        self.IsProducer = None
        self.EvidenceStatus = None
        self.WorkCategory = None
        self.IsOriginal = None
        self.IsRelease = None
        self.ProducerName = None
        self.ProduceTime = None
        self.WhiteLists = None
        self.WorkDesc = None
        self.Authorization = None
        self.AuthorizationStartTime = None
        self.AuthorizationEndTime = None
        self.Commission = None
        self.CommissionStartTime = None
        self.CommissionEndTime = None
        self.EvidenceUrl = None
        self.EvidenceStartTime = None
        self.EvidenceEndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkName = params.get("WorkName")
        self.MonitorStatus = params.get("MonitorStatus")
        self.AuthStatus = params.get("AuthStatus")
        self.CommStatus = params.get("CommStatus")
        self.IsProducer = params.get("IsProducer")
        self.EvidenceStatus = params.get("EvidenceStatus")
        self.WorkCategory = params.get("WorkCategory")
        self.IsOriginal = params.get("IsOriginal")
        self.IsRelease = params.get("IsRelease")
        self.ProducerName = params.get("ProducerName")
        self.ProduceTime = params.get("ProduceTime")
        self.WhiteLists = params.get("WhiteLists")
        self.WorkDesc = params.get("WorkDesc")
        self.Authorization = params.get("Authorization")
        self.AuthorizationStartTime = params.get("AuthorizationStartTime")
        self.AuthorizationEndTime = params.get("AuthorizationEndTime")
        self.Commission = params.get("Commission")
        self.CommissionStartTime = params.get("CommissionStartTime")
        self.CommissionEndTime = params.get("CommissionEndTime")
        self.EvidenceUrl = params.get("EvidenceUrl")
        self.EvidenceStartTime = params.get("EvidenceStartTime")
        self.EvidenceEndTime = params.get("EvidenceEndTime")
        self.RequestId = params.get("RequestId")


class FakeURLInfo(AbstractModel):
    """仿冒网站信息

    """

    def __init__(self):
        r"""
        :param FakeURLId: 仿冒网址ID
        :type FakeURLId: int
        :param ProtectWeb: 保护网站
        :type ProtectWeb: str
        :param DetectTime: 检测时间
        :type DetectTime: str
        :param FakeURL: 仿冒网址
        :type FakeURL: str
        :param Snapshot: 截图
        :type Snapshot: str
        :param IP: IP地址
        :type IP: str
        :param IPLoc: IP地理位置
        :type IPLoc: str
        :param Heat: 热度
        :type Heat: int
        :param Status: 网址状态
        :type Status: int
        :param Note: 备注
        :type Note: str
        :param FakeURLCompany: 仿冒网站所属单位
        :type FakeURLCompany: str
        :param FakeURLAttr: 仿冒网站性质
        :type FakeURLAttr: str
        :param FakeURLName: 仿冒网站名称
        :type FakeURLName: str
        :param FakeURLICP: 仿冒网站备案号
        :type FakeURLICP: str
        :param FakeURLCreateTime: 仿冒网站创建时间
        :type FakeURLCreateTime: str
        :param FakeURLExpireTime: 仿冒网站过期时间
        :type FakeURLExpireTime: str
        """
        self.FakeURLId = None
        self.ProtectWeb = None
        self.DetectTime = None
        self.FakeURL = None
        self.Snapshot = None
        self.IP = None
        self.IPLoc = None
        self.Heat = None
        self.Status = None
        self.Note = None
        self.FakeURLCompany = None
        self.FakeURLAttr = None
        self.FakeURLName = None
        self.FakeURLICP = None
        self.FakeURLCreateTime = None
        self.FakeURLExpireTime = None


    def _deserialize(self, params):
        self.FakeURLId = params.get("FakeURLId")
        self.ProtectWeb = params.get("ProtectWeb")
        self.DetectTime = params.get("DetectTime")
        self.FakeURL = params.get("FakeURL")
        self.Snapshot = params.get("Snapshot")
        self.IP = params.get("IP")
        self.IPLoc = params.get("IPLoc")
        self.Heat = params.get("Heat")
        self.Status = params.get("Status")
        self.Note = params.get("Note")
        self.FakeURLCompany = params.get("FakeURLCompany")
        self.FakeURLAttr = params.get("FakeURLAttr")
        self.FakeURLName = params.get("FakeURLName")
        self.FakeURLICP = params.get("FakeURLICP")
        self.FakeURLCreateTime = params.get("FakeURLCreateTime")
        self.FakeURLExpireTime = params.get("FakeURLExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class File(AbstractModel):
    """权属文件列表

    """

    def __init__(self):
        r"""
        :param FileUrl: 文件下载地址
        :type FileUrl: str
        :param FileType: 文件类型 1-委托书 2-授权书 5-存证证书 11-营业执照
        :type FileType: int
        :param ValidStartDate: 文件有效开始日期
        :type ValidStartDate: str
        :param ValidEndDate: 文件有效截止日期
        :type ValidEndDate: str
        """
        self.FileUrl = None
        self.FileType = None
        self.ValidStartDate = None
        self.ValidEndDate = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.FileType = params.get("FileType")
        self.ValidStartDate = params.get("ValidStartDate")
        self.ValidEndDate = params.get("ValidEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param LicenseName: 营业执照
        :type LicenseName: str
        :param AuthorizationName: 授权书
        :type AuthorizationName: str
        :param BrandName: 商标名称
        :type BrandName: str
        :param BrandCertificateName: 商标证明
        :type BrandCertificateName: str
        :param TransferName: 商标转让证明
        :type TransferName: str
        """
        self.LicenseName = None
        self.AuthorizationName = None
        self.BrandName = None
        self.BrandCertificateName = None
        self.TransferName = None


    def _deserialize(self, params):
        self.LicenseName = params.get("LicenseName")
        self.AuthorizationName = params.get("AuthorizationName")
        self.BrandName = params.get("BrandName")
        self.BrandCertificateName = params.get("BrandCertificateName")
        self.TransferName = params.get("TransferName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBPOfflineAttachmentResponse(AbstractModel):
    """ModifyBPOfflineAttachment返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRBlockStatusRequest(AbstractModel):
    """ModifyCRBlockStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param BlockUrl: 拦截结果回调地址
        :type BlockUrl: str
        """
        self.TortId = None
        self.BlockUrl = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.BlockUrl = params.get("BlockUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRBlockStatusResponse(AbstractModel):
    """ModifyCRBlockStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRMonitorRequest(AbstractModel):
    """ModifyCRMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param MonitorStatus: 监测状态：1-开启监测 2-关闭监测
        :type MonitorStatus: str
        :param MonitorEnd: 监测截止时间
        :type MonitorEnd: str
        """
        self.WorkId = None
        self.MonitorStatus = None
        self.MonitorEnd = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.MonitorStatus = params.get("MonitorStatus")
        self.MonitorEnd = params.get("MonitorEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRMonitorResponse(AbstractModel):
    """ModifyCRMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRObtainStatusRequest(AbstractModel):
    """ModifyCRObtainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param ObtainType: 取证类型：1-网页取证 2-过程取证(暂不提供)
        :type ObtainType: int
        :param ObtainDuration: 过程取证的取证时长，单位分钟，范围0-120
        :type ObtainDuration: int
        :param ObtainUrl: 取证结果回调地址
        :type ObtainUrl: str
        """
        self.TortId = None
        self.ObtainType = None
        self.ObtainDuration = None
        self.ObtainUrl = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.ObtainType = params.get("ObtainType")
        self.ObtainDuration = params.get("ObtainDuration")
        self.ObtainUrl = params.get("ObtainUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRObtainStatusResponse(AbstractModel):
    """ModifyCRObtainStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRRightStatusRequest(AbstractModel):
    """ModifyCRRightStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param RightUrl: 发函结果回调地址
        :type RightUrl: str
        """
        self.TortId = None
        self.RightUrl = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.RightUrl = params.get("RightUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRRightStatusResponse(AbstractModel):
    """ModifyCRRightStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRWhiteListRequest(AbstractModel):
    """ModifyCRWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListId: 该字段已废弃，白名单ID
        :type WhiteListId: int
        :param PlatForm: 该字段已废弃，平台名称
        :type PlatForm: str
        :param PlatUrl: 该字段已废弃，平台站点链接
        :type PlatUrl: str
        :param AuthorId: 该字段已废弃，作者ID
        :type AuthorId: str
        :param WorksId: 该字段已废弃，作品ID
        :type WorksId: int
        :param WorkId: 作品ID
        :type WorkId: int
        :param WhiteSites: 白名单列表，以\n分割
        :type WhiteSites: str
        """
        self.WhiteListId = None
        self.PlatForm = None
        self.PlatUrl = None
        self.AuthorId = None
        self.WorksId = None
        self.WorkId = None
        self.WhiteSites = None


    def _deserialize(self, params):
        self.WhiteListId = params.get("WhiteListId")
        self.PlatForm = params.get("PlatForm")
        self.PlatUrl = params.get("PlatUrl")
        self.AuthorId = params.get("AuthorId")
        self.WorksId = params.get("WorksId")
        self.WorkId = params.get("WorkId")
        self.WhiteSites = params.get("WhiteSites")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRWhiteListResponse(AbstractModel):
    """ModifyCRWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Monitor(AbstractModel):
    """版权保护-监测结果

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param WorkName: 作品名称
        :type WorkName: str
        :param WorkType: 作品内容类型 01-视频 02-音频 03-文本 04-图片
        :type WorkType: str
        :param TortPlatNum: 侵权平台数量
        :type TortPlatNum: int
        :param TortURLNum: 侵权链接数量
        :type TortURLNum: int
        :param MonitorTime: 监测时间
        :type MonitorTime: str
        :param MonitorStatus: 0-待监测 1-监测中 2-不监测 3-暂停监测
        :type MonitorStatus: int
        :param WorkCategory: 作品类型
        :type WorkCategory: str
        :param InsertTime: 新增时间
        :type InsertTime: str
        :param MonitorNote: 监测状态说明
        :type MonitorNote: str
        :param WorkCategoryAll: 作品类型全部展示
        :type WorkCategoryAll: str
        :param EvidenceStatus: 存证状态
        :type EvidenceStatus: int
        :param EvidenceNote: 存证状态说明
        :type EvidenceNote: str
        :param TortSiteNum: 侵权站点数量
        :type TortSiteNum: int
        """
        self.WorkId = None
        self.WorkName = None
        self.WorkType = None
        self.TortPlatNum = None
        self.TortURLNum = None
        self.MonitorTime = None
        self.MonitorStatus = None
        self.WorkCategory = None
        self.InsertTime = None
        self.MonitorNote = None
        self.WorkCategoryAll = None
        self.EvidenceStatus = None
        self.EvidenceNote = None
        self.TortSiteNum = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.WorkName = params.get("WorkName")
        self.WorkType = params.get("WorkType")
        self.TortPlatNum = params.get("TortPlatNum")
        self.TortURLNum = params.get("TortURLNum")
        self.MonitorTime = params.get("MonitorTime")
        self.MonitorStatus = params.get("MonitorStatus")
        self.WorkCategory = params.get("WorkCategory")
        self.InsertTime = params.get("InsertTime")
        self.MonitorNote = params.get("MonitorNote")
        self.WorkCategoryAll = params.get("WorkCategoryAll")
        self.EvidenceStatus = params.get("EvidenceStatus")
        self.EvidenceNote = params.get("EvidenceNote")
        self.TortSiteNum = params.get("TortSiteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorTort(AbstractModel):
    """监测侵权信息详情

    """

    def __init__(self):
        r"""
        :param TortId: 侵权信息ID
        :type TortId: int
        :param TortTitle: 侵权标题
        :type TortTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param TortURL: 侵权链接
        :type TortURL: str
        :param PubTime: 侵权链接发布时间
        :type PubTime: str
        :param Author: 作者
        :type Author: str
        :param DetectTime: 发现时间
        :type DetectTime: str
        :param ObtainStatus: 取证状态
        :type ObtainStatus: int
        :param RightStatus: 维权状态
        :type RightStatus: int
        :param BlockStatus: 拦截状态
        :type BlockStatus: int
        :param TortNum: 侵权编号
        :type TortNum: str
        :param ObtainNote: 取证状态说明
        :type ObtainNote: str
        :param WorkTitle: 作品标题
        :type WorkTitle: str
        :param TortSite: 侵权站点
        :type TortSite: str
        :param ICP: ICP备案信息
        :type ICP: str
        :param RightNote: 维权状态说明
        :type RightNote: str
        :param ObtainType: 取证类型
        :type ObtainType: int
        :param BlockNote: 拦截状态说明
        :type BlockNote: str
        :param WorkId: 作品ID
        :type WorkId: int
        :param WorkName: 作品名称
        :type WorkName: str
        :param AuthStatus: 授权书状态
        :type AuthStatus: int
        :param CommStatus: 委托书状态
        :type CommStatus: int
        :param EvidenceStatus: 存证证书状态
        :type EvidenceStatus: int
        :param IsProducer: 是否著作权人
        :type IsProducer: int
        :param IsOverseas: 是否境外网址
        :type IsOverseas: int
        :param IPLoc: ip地理位置
        :type IPLoc: str
        """
        self.TortId = None
        self.TortTitle = None
        self.TortPlat = None
        self.TortURL = None
        self.PubTime = None
        self.Author = None
        self.DetectTime = None
        self.ObtainStatus = None
        self.RightStatus = None
        self.BlockStatus = None
        self.TortNum = None
        self.ObtainNote = None
        self.WorkTitle = None
        self.TortSite = None
        self.ICP = None
        self.RightNote = None
        self.ObtainType = None
        self.BlockNote = None
        self.WorkId = None
        self.WorkName = None
        self.AuthStatus = None
        self.CommStatus = None
        self.EvidenceStatus = None
        self.IsProducer = None
        self.IsOverseas = None
        self.IPLoc = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.TortTitle = params.get("TortTitle")
        self.TortPlat = params.get("TortPlat")
        self.TortURL = params.get("TortURL")
        self.PubTime = params.get("PubTime")
        self.Author = params.get("Author")
        self.DetectTime = params.get("DetectTime")
        self.ObtainStatus = params.get("ObtainStatus")
        self.RightStatus = params.get("RightStatus")
        self.BlockStatus = params.get("BlockStatus")
        self.TortNum = params.get("TortNum")
        self.ObtainNote = params.get("ObtainNote")
        self.WorkTitle = params.get("WorkTitle")
        self.TortSite = params.get("TortSite")
        self.ICP = params.get("ICP")
        self.RightNote = params.get("RightNote")
        self.ObtainType = params.get("ObtainType")
        self.BlockNote = params.get("BlockNote")
        self.WorkId = params.get("WorkId")
        self.WorkName = params.get("WorkName")
        self.AuthStatus = params.get("AuthStatus")
        self.CommStatus = params.get("CommStatus")
        self.EvidenceStatus = params.get("EvidenceStatus")
        self.IsProducer = params.get("IsProducer")
        self.IsOverseas = params.get("IsOverseas")
        self.IPLoc = params.get("IPLoc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectURLInfo(AbstractModel):
    """保护网站信息

    """

    def __init__(self):
        r"""
        :param ProtectURLId: 保护网站ID
        :type ProtectURLId: int
        :param ProtectURL: 保护网站
        :type ProtectURL: str
        :param ProtectWeb: 保护网站名称
        :type ProtectWeb: str
        :param ProtectURLStatus: 保护网站审核状态 1-审核中 2-审核不通过 3-审核通过
        :type ProtectURLStatus: int
        :param ProtectURLNote: 网站审核不通过原因
        :type ProtectURLNote: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.ProtectURLId = None
        self.ProtectURL = None
        self.ProtectWeb = None
        self.ProtectURLStatus = None
        self.ProtectURLNote = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProtectURLId = params.get("ProtectURLId")
        self.ProtectURL = params.get("ProtectURL")
        self.ProtectWeb = params.get("ProtectWeb")
        self.ProtectURLStatus = params.get("ProtectURLStatus")
        self.ProtectURLNote = params.get("ProtectURLNote")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFakeURLInfo(AbstractModel):
    """举报网址信息

    """

    def __init__(self):
        r"""
        :param FakeURLId: 仿冒网址ID
        :type FakeURLId: int
        :param DetectTime: 检测时间
        :type DetectTime: str
        :param ProtectURL: 保护网站
        :type ProtectURL: str
        :param ProtectWeb: 保护网站名称
        :type ProtectWeb: str
        :param FakeURL: 仿冒网址
        :type FakeURL: str
        :param Snapshot: 截图
        :type Snapshot: str
        :param IP: IP地址
        :type IP: str
        :param IPLoc: IP地理位置
        :type IPLoc: str
        :param Heat: 热度
        :type Heat: int
        :param Status: 网站状态
        :type Status: int
        :param Note: 网站不处理原因
        :type Note: str
        :param FakeURLCompany: 仿冒网站的企业名称
        :type FakeURLCompany: str
        :param FakeURLAttr: 仿冒网站的网站性质
        :type FakeURLAttr: str
        :param FakeURLName: 仿冒网站的网站名称
        :type FakeURLName: str
        :param FakeURLICP: 仿冒网站的备案
        :type FakeURLICP: str
        :param FakeURLCreateTime: 仿冒网站创建时间
        :type FakeURLCreateTime: str
        :param FakeURLExpireTime: 仿冒网站过期时间
        :type FakeURLExpireTime: str
        :param BlockTime: 协查处置时间
        :type BlockTime: str
        """
        self.FakeURLId = None
        self.DetectTime = None
        self.ProtectURL = None
        self.ProtectWeb = None
        self.FakeURL = None
        self.Snapshot = None
        self.IP = None
        self.IPLoc = None
        self.Heat = None
        self.Status = None
        self.Note = None
        self.FakeURLCompany = None
        self.FakeURLAttr = None
        self.FakeURLName = None
        self.FakeURLICP = None
        self.FakeURLCreateTime = None
        self.FakeURLExpireTime = None
        self.BlockTime = None


    def _deserialize(self, params):
        self.FakeURLId = params.get("FakeURLId")
        self.DetectTime = params.get("DetectTime")
        self.ProtectURL = params.get("ProtectURL")
        self.ProtectWeb = params.get("ProtectWeb")
        self.FakeURL = params.get("FakeURL")
        self.Snapshot = params.get("Snapshot")
        self.IP = params.get("IP")
        self.IPLoc = params.get("IPLoc")
        self.Heat = params.get("Heat")
        self.Status = params.get("Status")
        self.Note = params.get("Note")
        self.FakeURLCompany = params.get("FakeURLCompany")
        self.FakeURLAttr = params.get("FakeURLAttr")
        self.FakeURLName = params.get("FakeURLName")
        self.FakeURLICP = params.get("FakeURLICP")
        self.FakeURLCreateTime = params.get("FakeURLCreateTime")
        self.FakeURLExpireTime = params.get("FakeURLExpireTime")
        self.BlockTime = params.get("BlockTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCRWorkRequest(AbstractModel):
    """UpdateCRWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param ContentType: 文件的扩展名，例如txt，docx
        :type ContentType: str
        :param Content: 内容的base64编码
        :type Content: str
        :param CertType: 本次存证类型：0-不存证 1-存当前文件 2-存历史全量文件
        :type CertType: str
        """
        self.WorkId = None
        self.ContentType = None
        self.Content = None
        self.CertType = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.ContentType = params.get("ContentType")
        self.Content = params.get("Content")
        self.CertType = params.get("CertType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCRWorkResponse(AbstractModel):
    """UpdateCRWork返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param EvidenceId: 存证ID
        :type EvidenceId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")