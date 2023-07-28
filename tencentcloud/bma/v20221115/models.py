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
    """品牌响应数据

    """

    def __init__(self):
        r"""
        :param _CompanyId: 品牌Id
        :type CompanyId: int
        :param _CompanyName: 企业名称
        :type CompanyName: str
        :param _BrandName: 品牌名称
        :type BrandName: str
        :param _Phone: 联系电话
        :type Phone: str
        :param _License: 营业执照
        :type License: str
        :param _LicenseStatus: 营业执照审核状态
        :type LicenseStatus: int
        :param _LicenseNote: 营业执照审核状态说明
        :type LicenseNote: str
        :param _Authorization: 授权书
        :type Authorization: str
        :param _AuthorizationStatus: 授权书审核状态
        :type AuthorizationStatus: int
        :param _AuthorizationNote: 授权书审核状态说明
        :type AuthorizationNote: str
        :param _Trademarks: 商标信息
        :type Trademarks: list of TrademarkData
        :param _InsertTime: 新增时间
        :type InsertTime: str
        :param _Services: 服务信息
        :type Services: :class:`tencentcloud.bma.v20221115.models.ServiceData`
        :param _Uin: 账号id
        :type Uin: str
        """
        self._CompanyId = None
        self._CompanyName = None
        self._BrandName = None
        self._Phone = None
        self._License = None
        self._LicenseStatus = None
        self._LicenseNote = None
        self._Authorization = None
        self._AuthorizationStatus = None
        self._AuthorizationNote = None
        self._Trademarks = None
        self._InsertTime = None
        self._Services = None
        self._Uin = None

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

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
    def Authorization(self):
        return self._Authorization

    @Authorization.setter
    def Authorization(self, Authorization):
        self._Authorization = Authorization

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
    def Trademarks(self):
        return self._Trademarks

    @Trademarks.setter
    def Trademarks(self, Trademarks):
        self._Trademarks = Trademarks

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._CompanyName = params.get("CompanyName")
        self._BrandName = params.get("BrandName")
        self._Phone = params.get("Phone")
        self._License = params.get("License")
        self._LicenseStatus = params.get("LicenseStatus")
        self._LicenseNote = params.get("LicenseNote")
        self._Authorization = params.get("Authorization")
        self._AuthorizationStatus = params.get("AuthorizationStatus")
        self._AuthorizationNote = params.get("AuthorizationNote")
        if params.get("Trademarks") is not None:
            self._Trademarks = []
            for item in params.get("Trademarks"):
                obj = TrademarkData()
                obj._deserialize(item)
                self._Trademarks.append(obj)
        self._InsertTime = params.get("InsertTime")
        if params.get("Services") is not None:
            self._Services = ServiceData()
            self._Services._deserialize(params.get("Services"))
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPBrandRequest(AbstractModel):
    """CreateBPBrand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandName: 品牌名称
        :type BrandName: str
        :param _CompanyName: 企业名称
        :type CompanyName: str
        :param _BrandLogo: 品牌logo
        :type BrandLogo: str
        :param _Phone: 联系电话
        :type Phone: str
        :param _License: 营业执照
        :type License: str
        :param _Authorization: 授权书
        :type Authorization: str
        :param _TrademarkNames: 商标名称
        :type TrademarkNames: list of str
        :param _Trademarks: 商标证明
        :type Trademarks: list of str
        :param _IsTransfers: 是否涉及转让: 0-不转让 1-转让
        :type IsTransfers: list of str
        :param _Transfers: 转让证明
        :type Transfers: list of str
        :param _ProtectURLs: 保护网址
        :type ProtectURLs: list of str
        :param _ProtectAPPs: 保护应用
        :type ProtectAPPs: list of str
        :param _ProtectOfficialAccounts: 保护公众号
        :type ProtectOfficialAccounts: list of str
        :param _ProtectMiniPrograms: 保护小程序
        :type ProtectMiniPrograms: list of str
        :param _APISource: 请求来源：0-反钓鱼 2-反假冒
        :type APISource: int
        """
        self._BrandName = None
        self._CompanyName = None
        self._BrandLogo = None
        self._Phone = None
        self._License = None
        self._Authorization = None
        self._TrademarkNames = None
        self._Trademarks = None
        self._IsTransfers = None
        self._Transfers = None
        self._ProtectURLs = None
        self._ProtectAPPs = None
        self._ProtectOfficialAccounts = None
        self._ProtectMiniPrograms = None
        self._APISource = None

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def BrandLogo(self):
        return self._BrandLogo

    @BrandLogo.setter
    def BrandLogo(self, BrandLogo):
        self._BrandLogo = BrandLogo

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def Authorization(self):
        return self._Authorization

    @Authorization.setter
    def Authorization(self, Authorization):
        self._Authorization = Authorization

    @property
    def TrademarkNames(self):
        return self._TrademarkNames

    @TrademarkNames.setter
    def TrademarkNames(self, TrademarkNames):
        self._TrademarkNames = TrademarkNames

    @property
    def Trademarks(self):
        return self._Trademarks

    @Trademarks.setter
    def Trademarks(self, Trademarks):
        self._Trademarks = Trademarks

    @property
    def IsTransfers(self):
        return self._IsTransfers

    @IsTransfers.setter
    def IsTransfers(self, IsTransfers):
        self._IsTransfers = IsTransfers

    @property
    def Transfers(self):
        return self._Transfers

    @Transfers.setter
    def Transfers(self, Transfers):
        self._Transfers = Transfers

    @property
    def ProtectURLs(self):
        return self._ProtectURLs

    @ProtectURLs.setter
    def ProtectURLs(self, ProtectURLs):
        self._ProtectURLs = ProtectURLs

    @property
    def ProtectAPPs(self):
        return self._ProtectAPPs

    @ProtectAPPs.setter
    def ProtectAPPs(self, ProtectAPPs):
        self._ProtectAPPs = ProtectAPPs

    @property
    def ProtectOfficialAccounts(self):
        return self._ProtectOfficialAccounts

    @ProtectOfficialAccounts.setter
    def ProtectOfficialAccounts(self, ProtectOfficialAccounts):
        self._ProtectOfficialAccounts = ProtectOfficialAccounts

    @property
    def ProtectMiniPrograms(self):
        return self._ProtectMiniPrograms

    @ProtectMiniPrograms.setter
    def ProtectMiniPrograms(self, ProtectMiniPrograms):
        self._ProtectMiniPrograms = ProtectMiniPrograms

    @property
    def APISource(self):
        return self._APISource

    @APISource.setter
    def APISource(self, APISource):
        self._APISource = APISource


    def _deserialize(self, params):
        self._BrandName = params.get("BrandName")
        self._CompanyName = params.get("CompanyName")
        self._BrandLogo = params.get("BrandLogo")
        self._Phone = params.get("Phone")
        self._License = params.get("License")
        self._Authorization = params.get("Authorization")
        self._TrademarkNames = params.get("TrademarkNames")
        self._Trademarks = params.get("Trademarks")
        self._IsTransfers = params.get("IsTransfers")
        self._Transfers = params.get("Transfers")
        self._ProtectURLs = params.get("ProtectURLs")
        self._ProtectAPPs = params.get("ProtectAPPs")
        self._ProtectOfficialAccounts = params.get("ProtectOfficialAccounts")
        self._ProtectMiniPrograms = params.get("ProtectMiniPrograms")
        self._APISource = params.get("APISource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPBrandResponse(AbstractModel):
    """CreateBPBrand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 企业id
        :type CompanyId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._RequestId = None

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
        self._CompanyId = params.get("CompanyId")
        self._RequestId = params.get("RequestId")


class CreateBPFakeAPPListRequest(AbstractModel):
    """CreateBPFakeAPPList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FakeAPPs: 批量模板
        :type FakeAPPs: str
        """
        self._FakeAPPs = None

    @property
    def FakeAPPs(self):
        return self._FakeAPPs

    @FakeAPPs.setter
    def FakeAPPs(self, FakeAPPs):
        self._FakeAPPs = FakeAPPs


    def _deserialize(self, params):
        self._FakeAPPs = params.get("FakeAPPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeAPPListResponse(AbstractModel):
    """CreateBPFakeAPPList返回参数结构体

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


class CreateBPFakeAPPRequest(AbstractModel):
    """CreateBPFakeAPP请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 企业id
        :type CompanyId: int
        :param _FakeAPPName: 仿冒应用名称
        :type FakeAPPName: str
        :param _APPChan: 仿冒来源
        :type APPChan: str
        :param _FakeAPPPackageName: 仿冒应用包名
        :type FakeAPPPackageName: str
        :param _FakeAPPCert: 仿冒应用证书
        :type FakeAPPCert: str
        :param _FakeAPPSize: 仿冒应用大小
        :type FakeAPPSize: str
        :param _FakeAPPSnapshots: 仿冒截图
        :type FakeAPPSnapshots: list of str
        :param _Note: 备注
        :type Note: str
        """
        self._CompanyId = None
        self._FakeAPPName = None
        self._APPChan = None
        self._FakeAPPPackageName = None
        self._FakeAPPCert = None
        self._FakeAPPSize = None
        self._FakeAPPSnapshots = None
        self._Note = None

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def FakeAPPName(self):
        return self._FakeAPPName

    @FakeAPPName.setter
    def FakeAPPName(self, FakeAPPName):
        self._FakeAPPName = FakeAPPName

    @property
    def APPChan(self):
        return self._APPChan

    @APPChan.setter
    def APPChan(self, APPChan):
        self._APPChan = APPChan

    @property
    def FakeAPPPackageName(self):
        return self._FakeAPPPackageName

    @FakeAPPPackageName.setter
    def FakeAPPPackageName(self, FakeAPPPackageName):
        self._FakeAPPPackageName = FakeAPPPackageName

    @property
    def FakeAPPCert(self):
        return self._FakeAPPCert

    @FakeAPPCert.setter
    def FakeAPPCert(self, FakeAPPCert):
        self._FakeAPPCert = FakeAPPCert

    @property
    def FakeAPPSize(self):
        return self._FakeAPPSize

    @FakeAPPSize.setter
    def FakeAPPSize(self, FakeAPPSize):
        self._FakeAPPSize = FakeAPPSize

    @property
    def FakeAPPSnapshots(self):
        return self._FakeAPPSnapshots

    @FakeAPPSnapshots.setter
    def FakeAPPSnapshots(self, FakeAPPSnapshots):
        self._FakeAPPSnapshots = FakeAPPSnapshots

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._FakeAPPName = params.get("FakeAPPName")
        self._APPChan = params.get("APPChan")
        self._FakeAPPPackageName = params.get("FakeAPPPackageName")
        self._FakeAPPCert = params.get("FakeAPPCert")
        self._FakeAPPSize = params.get("FakeAPPSize")
        self._FakeAPPSnapshots = params.get("FakeAPPSnapshots")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeAPPResponse(AbstractModel):
    """CreateBPFakeAPP返回参数结构体

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


class CreateBPFakeURLRequest(AbstractModel):
    """CreateBPFakeURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 企业id
        :type CompanyId: int
        :param _FakeURL: 仿冒网址
        :type FakeURL: str
        :param _FakeURLSnapshots: 仿冒网址截图
        :type FakeURLSnapshots: list of str
        :param _Note: 备注
        :type Note: str
        """
        self._CompanyId = None
        self._FakeURL = None
        self._FakeURLSnapshots = None
        self._Note = None

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def FakeURL(self):
        return self._FakeURL

    @FakeURL.setter
    def FakeURL(self, FakeURL):
        self._FakeURL = FakeURL

    @property
    def FakeURLSnapshots(self):
        return self._FakeURLSnapshots

    @FakeURLSnapshots.setter
    def FakeURLSnapshots(self, FakeURLSnapshots):
        self._FakeURLSnapshots = FakeURLSnapshots

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._FakeURL = params.get("FakeURL")
        self._FakeURLSnapshots = params.get("FakeURLSnapshots")
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


class CreateBPFakeURLsRequest(AbstractModel):
    """CreateBPFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FakeURLs: 批量模板
        :type FakeURLs: str
        """
        self._FakeURLs = None

    @property
    def FakeURLs(self):
        return self._FakeURLs

    @FakeURLs.setter
    def FakeURLs(self, FakeURLs):
        self._FakeURLs = FakeURLs


    def _deserialize(self, params):
        self._FakeURLs = params.get("FakeURLs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLsResponse(AbstractModel):
    """CreateBPFakeURLs返回参数结构体

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


class CreateBPWhiteListRequest(AbstractModel):
    """CreateBPWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 企业Id
        :type CompanyId: int
        :param _WhiteListType: 白名单类型：0-网站 1-应用 2-公众号 3-小程
        :type WhiteListType: int
        :param _WhiteLists: 白名单名称
        :type WhiteLists: list of str
        """
        self._CompanyId = None
        self._WhiteListType = None
        self._WhiteLists = None

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def WhiteListType(self):
        return self._WhiteListType

    @WhiteListType.setter
    def WhiteListType(self, WhiteListType):
        self._WhiteListType = WhiteListType

    @property
    def WhiteLists(self):
        return self._WhiteLists

    @WhiteLists.setter
    def WhiteLists(self, WhiteLists):
        self._WhiteLists = WhiteLists


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._WhiteListType = params.get("WhiteListType")
        self._WhiteLists = params.get("WhiteLists")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPWhiteListResponse(AbstractModel):
    """CreateBPWhiteList返回参数结构体

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


class DeleteBPWhiteListRequest(AbstractModel):
    """DeleteBPWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WhiteListId: 白名单id
        :type WhiteListId: int
        """
        self._WhiteListId = None

    @property
    def WhiteListId(self):
        return self._WhiteListId

    @WhiteListId.setter
    def WhiteListId(self, WhiteListId):
        self._WhiteListId = WhiteListId


    def _deserialize(self, params):
        self._WhiteListId = params.get("WhiteListId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBPWhiteListResponse(AbstractModel):
    """DeleteBPWhiteList返回参数结构体

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


class DescribeBPBrandsRequest(AbstractModel):
    """DescribeBPBrands请求参数结构体

    """


class DescribeBPBrandsResponse(AbstractModel):
    """DescribeBPBrands返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Brands: 品牌信息
        :type Brands: list of BrandData
        :param _NoticeStatus: 品牌审核通知栏状态：0 不显示 1 显示
        :type NoticeStatus: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Brands = None
        self._NoticeStatus = None
        self._RequestId = None

    @property
    def Brands(self):
        return self._Brands

    @Brands.setter
    def Brands(self, Brands):
        self._Brands = Brands

    @property
    def NoticeStatus(self):
        return self._NoticeStatus

    @NoticeStatus.setter
    def NoticeStatus(self, NoticeStatus):
        self._NoticeStatus = NoticeStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Brands") is not None:
            self._Brands = []
            for item in params.get("Brands"):
                obj = BrandData()
                obj._deserialize(item)
                self._Brands.append(obj)
        self._NoticeStatus = params.get("NoticeStatus")
        self._RequestId = params.get("RequestId")


class DescribeBPFakeAPPListRequest(AbstractModel):
    """DescribeBPFakeAPPList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤参数
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
        


class DescribeBPFakeAPPListResponse(AbstractModel):
    """DescribeBPFakeAPPList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FakeAPPList: 仿冒应用列表
        :type FakeAPPList: list of FakeAPPData
        :param _TotalCount: 仿冒应用总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FakeAPPList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FakeAPPList(self):
        return self._FakeAPPList

    @FakeAPPList.setter
    def FakeAPPList(self, FakeAPPList):
        self._FakeAPPList = FakeAPPList

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
        if params.get("FakeAPPList") is not None:
            self._FakeAPPList = []
            for item in params.get("FakeAPPList"):
                obj = FakeAPPData()
                obj._deserialize(item)
                self._FakeAPPList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBPFakeURLsRequest(AbstractModel):
    """DescribeBPFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤参数
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
        :param _FakeURLs: 仿冒网址列表
        :type FakeURLs: list of FakeURLData
        :param _TotalCount: 仿冒网址总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FakeURLs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FakeURLs(self):
        return self._FakeURLs

    @FakeURLs.setter
    def FakeURLs(self, FakeURLs):
        self._FakeURLs = FakeURLs

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
        if params.get("FakeURLs") is not None:
            self._FakeURLs = []
            for item in params.get("FakeURLs"):
                obj = FakeURLData()
                obj._deserialize(item)
                self._FakeURLs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeBPWhiteListsRequest(AbstractModel):
    """DescribeBPWhiteLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤参数
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
        


class DescribeBPWhiteListsResponse(AbstractModel):
    """DescribeBPWhiteLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WhiteLists: 白名单列表
        :type WhiteLists: list of WhiteListData
        :param _TotalCount: 白名单总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WhiteLists = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WhiteLists(self):
        return self._WhiteLists

    @WhiteLists.setter
    def WhiteLists(self, WhiteLists):
        self._WhiteLists = WhiteLists

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
        if params.get("WhiteLists") is not None:
            self._WhiteLists = []
            for item in params.get("WhiteLists"):
                obj = WhiteListData()
                obj._deserialize(item)
                self._WhiteLists.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class FakeAPPData(AbstractModel):
    """仿冒应用数据

    """

    def __init__(self):
        r"""
        :param _FakeAPPId: 仿冒应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPId: int
        :param _BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param _Origin: 仿冒来源：0-系统检测 1-人工举报
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: int
        :param _FakeAPPName: 仿冒应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPName: str
        :param _FakeAPPPackageName: 仿冒应用包名
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPPackageName: str
        :param _FakeAPPCert: 仿冒应用证书
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPCert: str
        :param _FakeAPPSize: 仿冒应用大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPSize: str
        :param _Heat: 热度
注意：此字段可能返回 null，表示取不到有效值。
        :type Heat: int
        :param _BlockStatus: 协助处置状态：0-未处置 1-处置中 2-处置成功 3-处置失败
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockStatus: int
        :param _BlockNote: 协助处置状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockNote: str
        :param _OfflineStatus: 关停状态：0-未关停 1-关停中 2-关停成功 3-关停失败 4-重复上架
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineStatus: int
        :param _OfflineNote: 关停状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineNote: str
        :param _DownloadWay: app来源
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadWay: str
        :param _InsertTime: 新增时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _DownloadCosURL: App下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadCosURL: str
        :param _CertificationStatus: 资质证明状态:0-不可用 1-可用
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificationStatus: int
        """
        self._FakeAPPId = None
        self._BrandName = None
        self._Origin = None
        self._FakeAPPName = None
        self._FakeAPPPackageName = None
        self._FakeAPPCert = None
        self._FakeAPPSize = None
        self._Heat = None
        self._BlockStatus = None
        self._BlockNote = None
        self._OfflineStatus = None
        self._OfflineNote = None
        self._DownloadWay = None
        self._InsertTime = None
        self._DownloadCosURL = None
        self._CertificationStatus = None

    @property
    def FakeAPPId(self):
        return self._FakeAPPId

    @FakeAPPId.setter
    def FakeAPPId(self, FakeAPPId):
        self._FakeAPPId = FakeAPPId

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def FakeAPPName(self):
        return self._FakeAPPName

    @FakeAPPName.setter
    def FakeAPPName(self, FakeAPPName):
        self._FakeAPPName = FakeAPPName

    @property
    def FakeAPPPackageName(self):
        return self._FakeAPPPackageName

    @FakeAPPPackageName.setter
    def FakeAPPPackageName(self, FakeAPPPackageName):
        self._FakeAPPPackageName = FakeAPPPackageName

    @property
    def FakeAPPCert(self):
        return self._FakeAPPCert

    @FakeAPPCert.setter
    def FakeAPPCert(self, FakeAPPCert):
        self._FakeAPPCert = FakeAPPCert

    @property
    def FakeAPPSize(self):
        return self._FakeAPPSize

    @FakeAPPSize.setter
    def FakeAPPSize(self, FakeAPPSize):
        self._FakeAPPSize = FakeAPPSize

    @property
    def Heat(self):
        return self._Heat

    @Heat.setter
    def Heat(self, Heat):
        self._Heat = Heat

    @property
    def BlockStatus(self):
        return self._BlockStatus

    @BlockStatus.setter
    def BlockStatus(self, BlockStatus):
        self._BlockStatus = BlockStatus

    @property
    def BlockNote(self):
        return self._BlockNote

    @BlockNote.setter
    def BlockNote(self, BlockNote):
        self._BlockNote = BlockNote

    @property
    def OfflineStatus(self):
        return self._OfflineStatus

    @OfflineStatus.setter
    def OfflineStatus(self, OfflineStatus):
        self._OfflineStatus = OfflineStatus

    @property
    def OfflineNote(self):
        return self._OfflineNote

    @OfflineNote.setter
    def OfflineNote(self, OfflineNote):
        self._OfflineNote = OfflineNote

    @property
    def DownloadWay(self):
        return self._DownloadWay

    @DownloadWay.setter
    def DownloadWay(self, DownloadWay):
        self._DownloadWay = DownloadWay

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def DownloadCosURL(self):
        return self._DownloadCosURL

    @DownloadCosURL.setter
    def DownloadCosURL(self, DownloadCosURL):
        self._DownloadCosURL = DownloadCosURL

    @property
    def CertificationStatus(self):
        return self._CertificationStatus

    @CertificationStatus.setter
    def CertificationStatus(self, CertificationStatus):
        self._CertificationStatus = CertificationStatus


    def _deserialize(self, params):
        self._FakeAPPId = params.get("FakeAPPId")
        self._BrandName = params.get("BrandName")
        self._Origin = params.get("Origin")
        self._FakeAPPName = params.get("FakeAPPName")
        self._FakeAPPPackageName = params.get("FakeAPPPackageName")
        self._FakeAPPCert = params.get("FakeAPPCert")
        self._FakeAPPSize = params.get("FakeAPPSize")
        self._Heat = params.get("Heat")
        self._BlockStatus = params.get("BlockStatus")
        self._BlockNote = params.get("BlockNote")
        self._OfflineStatus = params.get("OfflineStatus")
        self._OfflineNote = params.get("OfflineNote")
        self._DownloadWay = params.get("DownloadWay")
        self._InsertTime = params.get("InsertTime")
        self._DownloadCosURL = params.get("DownloadCosURL")
        self._CertificationStatus = params.get("CertificationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FakeURLData(AbstractModel):
    """仿冒网址数据

    """

    def __init__(self):
        r"""
        :param _FakeURLId: 仿冒网址id
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeURLId: int
        :param _BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param _Origin: 仿冒来源：0-系统检测 1-人工举报
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: int
        :param _FakeURL: 仿冒网址
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeURL: str
        :param _FakeDomain: 仿冒域名
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeDomain: str
        :param _Heat: 热度
注意：此字段可能返回 null，表示取不到有效值。
        :type Heat: int
        :param _BlockStatus: 拦截处置状态：0-未处置 1-处置中 2-处置成功 3-处置失败
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockStatus: int
        :param _BlockNote: 拦截处置状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockNote: str
        :param _OfflineStatus: 关停状态：0-未关停 1-关停中 2-关停成功 3-关停失败 4-重复上架
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineStatus: int
        :param _OfflineNote: 关停状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineNote: str
        :param _IP: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _IPLocation: ip地理位置
注意：此字段可能返回 null，表示取不到有效值。
        :type IPLocation: str
        :param _WebCompany: 网站所属单位
注意：此字段可能返回 null，表示取不到有效值。
        :type WebCompany: str
        :param _WebAttribute: 网站性质
注意：此字段可能返回 null，表示取不到有效值。
        :type WebAttribute: str
        :param _WebName: 网站名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WebName: str
        :param _WebICP: 备案号
注意：此字段可能返回 null，表示取不到有效值。
        :type WebICP: str
        :param _WebCreateTime: 网站创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type WebCreateTime: str
        :param _WebExpireTime: 网站过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type WebExpireTime: str
        :param _InsertTime: 新增时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _CertificationStatus: 资质证明状态：0-不可用 1-可用
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificationStatus: int
        :param _Snapshot: 网址截图
注意：此字段可能返回 null，表示取不到有效值。
        :type Snapshot: str
        :param _AccountStatus: 账户资源状态：0-不可用 1-可用
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountStatus: int
        :param _AuditStatus: 审核状态：0-未审核 1-审核中 2-审核成功 3-审核失败
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditStatus: int
        """
        self._FakeURLId = None
        self._BrandName = None
        self._Origin = None
        self._FakeURL = None
        self._FakeDomain = None
        self._Heat = None
        self._BlockStatus = None
        self._BlockNote = None
        self._OfflineStatus = None
        self._OfflineNote = None
        self._IP = None
        self._IPLocation = None
        self._WebCompany = None
        self._WebAttribute = None
        self._WebName = None
        self._WebICP = None
        self._WebCreateTime = None
        self._WebExpireTime = None
        self._InsertTime = None
        self._CertificationStatus = None
        self._Snapshot = None
        self._AccountStatus = None
        self._AuditStatus = None

    @property
    def FakeURLId(self):
        return self._FakeURLId

    @FakeURLId.setter
    def FakeURLId(self, FakeURLId):
        self._FakeURLId = FakeURLId

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def FakeURL(self):
        return self._FakeURL

    @FakeURL.setter
    def FakeURL(self, FakeURL):
        self._FakeURL = FakeURL

    @property
    def FakeDomain(self):
        return self._FakeDomain

    @FakeDomain.setter
    def FakeDomain(self, FakeDomain):
        self._FakeDomain = FakeDomain

    @property
    def Heat(self):
        return self._Heat

    @Heat.setter
    def Heat(self, Heat):
        self._Heat = Heat

    @property
    def BlockStatus(self):
        return self._BlockStatus

    @BlockStatus.setter
    def BlockStatus(self, BlockStatus):
        self._BlockStatus = BlockStatus

    @property
    def BlockNote(self):
        return self._BlockNote

    @BlockNote.setter
    def BlockNote(self, BlockNote):
        self._BlockNote = BlockNote

    @property
    def OfflineStatus(self):
        return self._OfflineStatus

    @OfflineStatus.setter
    def OfflineStatus(self, OfflineStatus):
        self._OfflineStatus = OfflineStatus

    @property
    def OfflineNote(self):
        return self._OfflineNote

    @OfflineNote.setter
    def OfflineNote(self, OfflineNote):
        self._OfflineNote = OfflineNote

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def IPLocation(self):
        return self._IPLocation

    @IPLocation.setter
    def IPLocation(self, IPLocation):
        self._IPLocation = IPLocation

    @property
    def WebCompany(self):
        return self._WebCompany

    @WebCompany.setter
    def WebCompany(self, WebCompany):
        self._WebCompany = WebCompany

    @property
    def WebAttribute(self):
        return self._WebAttribute

    @WebAttribute.setter
    def WebAttribute(self, WebAttribute):
        self._WebAttribute = WebAttribute

    @property
    def WebName(self):
        return self._WebName

    @WebName.setter
    def WebName(self, WebName):
        self._WebName = WebName

    @property
    def WebICP(self):
        return self._WebICP

    @WebICP.setter
    def WebICP(self, WebICP):
        self._WebICP = WebICP

    @property
    def WebCreateTime(self):
        return self._WebCreateTime

    @WebCreateTime.setter
    def WebCreateTime(self, WebCreateTime):
        self._WebCreateTime = WebCreateTime

    @property
    def WebExpireTime(self):
        return self._WebExpireTime

    @WebExpireTime.setter
    def WebExpireTime(self, WebExpireTime):
        self._WebExpireTime = WebExpireTime

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def CertificationStatus(self):
        return self._CertificationStatus

    @CertificationStatus.setter
    def CertificationStatus(self, CertificationStatus):
        self._CertificationStatus = CertificationStatus

    @property
    def Snapshot(self):
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def AccountStatus(self):
        return self._AccountStatus

    @AccountStatus.setter
    def AccountStatus(self, AccountStatus):
        self._AccountStatus = AccountStatus

    @property
    def AuditStatus(self):
        return self._AuditStatus

    @AuditStatus.setter
    def AuditStatus(self, AuditStatus):
        self._AuditStatus = AuditStatus


    def _deserialize(self, params):
        self._FakeURLId = params.get("FakeURLId")
        self._BrandName = params.get("BrandName")
        self._Origin = params.get("Origin")
        self._FakeURL = params.get("FakeURL")
        self._FakeDomain = params.get("FakeDomain")
        self._Heat = params.get("Heat")
        self._BlockStatus = params.get("BlockStatus")
        self._BlockNote = params.get("BlockNote")
        self._OfflineStatus = params.get("OfflineStatus")
        self._OfflineNote = params.get("OfflineNote")
        self._IP = params.get("IP")
        self._IPLocation = params.get("IPLocation")
        self._WebCompany = params.get("WebCompany")
        self._WebAttribute = params.get("WebAttribute")
        self._WebName = params.get("WebName")
        self._WebICP = params.get("WebICP")
        self._WebCreateTime = params.get("WebCreateTime")
        self._WebExpireTime = params.get("WebExpireTime")
        self._InsertTime = params.get("InsertTime")
        self._CertificationStatus = params.get("CertificationStatus")
        self._Snapshot = params.get("Snapshot")
        self._AccountStatus = params.get("AccountStatus")
        self._AuditStatus = params.get("AuditStatus")
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

    def __init__(self):
        r"""
        :param _Name: 过滤参数键
        :type Name: str
        :param _Value: 过滤参数值
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
        


class ServiceData(AbstractModel):
    """服务响应数据

    """

    def __init__(self):
        r"""
        :param _ProtectURLCount: 网站保护关联资产数
        :type ProtectURLCount: int
        :param _ProtectURLExpireTime: 网站保护服务到期时间
        :type ProtectURLExpireTime: str
        :param _ProtectAPPCount: 应用保护关联资产数
        :type ProtectAPPCount: int
        :param _ProtectAPPExpireTime: 应用保护服务到期时间
        :type ProtectAPPExpireTime: str
        :param _ProtectOfficialAccountCount: 公众号保护关联资产数
        :type ProtectOfficialAccountCount: int
        :param _ProtectOfficialAccountExpireTime: 公众号保护服务到期时间
        :type ProtectOfficialAccountExpireTime: str
        :param _ProtectMiniProgramCount: 小程序保护关联资产数
        :type ProtectMiniProgramCount: int
        :param _ProtectMiniProgramExpireTime: 小程序保护服务到期时间
        :type ProtectMiniProgramExpireTime: str
        :param _OfflineCount: 关停下架使用次数
        :type OfflineCount: int
        """
        self._ProtectURLCount = None
        self._ProtectURLExpireTime = None
        self._ProtectAPPCount = None
        self._ProtectAPPExpireTime = None
        self._ProtectOfficialAccountCount = None
        self._ProtectOfficialAccountExpireTime = None
        self._ProtectMiniProgramCount = None
        self._ProtectMiniProgramExpireTime = None
        self._OfflineCount = None

    @property
    def ProtectURLCount(self):
        return self._ProtectURLCount

    @ProtectURLCount.setter
    def ProtectURLCount(self, ProtectURLCount):
        self._ProtectURLCount = ProtectURLCount

    @property
    def ProtectURLExpireTime(self):
        return self._ProtectURLExpireTime

    @ProtectURLExpireTime.setter
    def ProtectURLExpireTime(self, ProtectURLExpireTime):
        self._ProtectURLExpireTime = ProtectURLExpireTime

    @property
    def ProtectAPPCount(self):
        return self._ProtectAPPCount

    @ProtectAPPCount.setter
    def ProtectAPPCount(self, ProtectAPPCount):
        self._ProtectAPPCount = ProtectAPPCount

    @property
    def ProtectAPPExpireTime(self):
        return self._ProtectAPPExpireTime

    @ProtectAPPExpireTime.setter
    def ProtectAPPExpireTime(self, ProtectAPPExpireTime):
        self._ProtectAPPExpireTime = ProtectAPPExpireTime

    @property
    def ProtectOfficialAccountCount(self):
        return self._ProtectOfficialAccountCount

    @ProtectOfficialAccountCount.setter
    def ProtectOfficialAccountCount(self, ProtectOfficialAccountCount):
        self._ProtectOfficialAccountCount = ProtectOfficialAccountCount

    @property
    def ProtectOfficialAccountExpireTime(self):
        return self._ProtectOfficialAccountExpireTime

    @ProtectOfficialAccountExpireTime.setter
    def ProtectOfficialAccountExpireTime(self, ProtectOfficialAccountExpireTime):
        self._ProtectOfficialAccountExpireTime = ProtectOfficialAccountExpireTime

    @property
    def ProtectMiniProgramCount(self):
        return self._ProtectMiniProgramCount

    @ProtectMiniProgramCount.setter
    def ProtectMiniProgramCount(self, ProtectMiniProgramCount):
        self._ProtectMiniProgramCount = ProtectMiniProgramCount

    @property
    def ProtectMiniProgramExpireTime(self):
        return self._ProtectMiniProgramExpireTime

    @ProtectMiniProgramExpireTime.setter
    def ProtectMiniProgramExpireTime(self, ProtectMiniProgramExpireTime):
        self._ProtectMiniProgramExpireTime = ProtectMiniProgramExpireTime

    @property
    def OfflineCount(self):
        return self._OfflineCount

    @OfflineCount.setter
    def OfflineCount(self, OfflineCount):
        self._OfflineCount = OfflineCount


    def _deserialize(self, params):
        self._ProtectURLCount = params.get("ProtectURLCount")
        self._ProtectURLExpireTime = params.get("ProtectURLExpireTime")
        self._ProtectAPPCount = params.get("ProtectAPPCount")
        self._ProtectAPPExpireTime = params.get("ProtectAPPExpireTime")
        self._ProtectOfficialAccountCount = params.get("ProtectOfficialAccountCount")
        self._ProtectOfficialAccountExpireTime = params.get("ProtectOfficialAccountExpireTime")
        self._ProtectMiniProgramCount = params.get("ProtectMiniProgramCount")
        self._ProtectMiniProgramExpireTime = params.get("ProtectMiniProgramExpireTime")
        self._OfflineCount = params.get("OfflineCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrademarkData(AbstractModel):
    """商标响应数据

    """

    def __init__(self):
        r"""
        :param _Trademark: 商标证明
        :type Trademark: str
        :param _TrademarkStatus: 商标审核状态
        :type TrademarkStatus: int
        :param _TrademarkNote: 商标审核状态说明
        :type TrademarkNote: str
        :param _TrademarkId: 商标id
        :type TrademarkId: int
        :param _Transfer: 商标转让书
        :type Transfer: str
        :param _TransferStatus: 商标转让书审核状态
        :type TransferStatus: int
        :param _TransferNote: 商标转让书审核状态说明
        :type TransferNote: str
        :param _TrademarkName: 商标名称
        :type TrademarkName: str
        """
        self._Trademark = None
        self._TrademarkStatus = None
        self._TrademarkNote = None
        self._TrademarkId = None
        self._Transfer = None
        self._TransferStatus = None
        self._TransferNote = None
        self._TrademarkName = None

    @property
    def Trademark(self):
        return self._Trademark

    @Trademark.setter
    def Trademark(self, Trademark):
        self._Trademark = Trademark

    @property
    def TrademarkStatus(self):
        return self._TrademarkStatus

    @TrademarkStatus.setter
    def TrademarkStatus(self, TrademarkStatus):
        self._TrademarkStatus = TrademarkStatus

    @property
    def TrademarkNote(self):
        return self._TrademarkNote

    @TrademarkNote.setter
    def TrademarkNote(self, TrademarkNote):
        self._TrademarkNote = TrademarkNote

    @property
    def TrademarkId(self):
        return self._TrademarkId

    @TrademarkId.setter
    def TrademarkId(self, TrademarkId):
        self._TrademarkId = TrademarkId

    @property
    def Transfer(self):
        return self._Transfer

    @Transfer.setter
    def Transfer(self, Transfer):
        self._Transfer = Transfer

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

    @property
    def TrademarkName(self):
        return self._TrademarkName

    @TrademarkName.setter
    def TrademarkName(self, TrademarkName):
        self._TrademarkName = TrademarkName


    def _deserialize(self, params):
        self._Trademark = params.get("Trademark")
        self._TrademarkStatus = params.get("TrademarkStatus")
        self._TrademarkNote = params.get("TrademarkNote")
        self._TrademarkId = params.get("TrademarkId")
        self._Transfer = params.get("Transfer")
        self._TransferStatus = params.get("TransferStatus")
        self._TransferNote = params.get("TransferNote")
        self._TrademarkName = params.get("TrademarkName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteListData(AbstractModel):
    """白名单数据

    """

    def __init__(self):
        r"""
        :param _WhiteListId: 白名单id
注意：此字段可能返回 null，表示取不到有效值。
        :type WhiteListId: int
        :param _CompanyId: 企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompanyId: int
        :param _BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param _AssetsType: 资产类型：0-网站 1-app 2-公众号 3-小程序
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetsType: int
        :param _WhiteList: 白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type WhiteList: str
        :param _InsertTime: 新增时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        """
        self._WhiteListId = None
        self._CompanyId = None
        self._BrandName = None
        self._AssetsType = None
        self._WhiteList = None
        self._InsertTime = None

    @property
    def WhiteListId(self):
        return self._WhiteListId

    @WhiteListId.setter
    def WhiteListId(self, WhiteListId):
        self._WhiteListId = WhiteListId

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def AssetsType(self):
        return self._AssetsType

    @AssetsType.setter
    def AssetsType(self, AssetsType):
        self._AssetsType = AssetsType

    @property
    def WhiteList(self):
        return self._WhiteList

    @WhiteList.setter
    def WhiteList(self, WhiteList):
        self._WhiteList = WhiteList

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime


    def _deserialize(self, params):
        self._WhiteListId = params.get("WhiteListId")
        self._CompanyId = params.get("CompanyId")
        self._BrandName = params.get("BrandName")
        self._AssetsType = params.get("AssetsType")
        self._WhiteList = params.get("WhiteList")
        self._InsertTime = params.get("InsertTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        