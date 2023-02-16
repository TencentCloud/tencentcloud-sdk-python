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
        :param CompanyId: 品牌Id
        :type CompanyId: int
        :param CompanyName: 企业名称
        :type CompanyName: str
        :param BrandName: 品牌名称
        :type BrandName: str
        :param Phone: 联系电话
        :type Phone: str
        :param License: 营业执照
        :type License: str
        :param LicenseStatus: 营业执照审核状态
        :type LicenseStatus: int
        :param LicenseNote: 营业执照审核状态说明
        :type LicenseNote: str
        :param Authorization: 授权书
        :type Authorization: str
        :param AuthorizationStatus: 授权书审核状态
        :type AuthorizationStatus: int
        :param AuthorizationNote: 授权书审核状态说明
        :type AuthorizationNote: str
        :param Trademarks: 商标信息
        :type Trademarks: list of TrademarkData
        :param InsertTime: 新增时间
        :type InsertTime: str
        :param Services: 服务信息
        :type Services: :class:`tencentcloud.bma.v20221115.models.ServiceData`
        """
        self.CompanyId = None
        self.CompanyName = None
        self.BrandName = None
        self.Phone = None
        self.License = None
        self.LicenseStatus = None
        self.LicenseNote = None
        self.Authorization = None
        self.AuthorizationStatus = None
        self.AuthorizationNote = None
        self.Trademarks = None
        self.InsertTime = None
        self.Services = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.CompanyName = params.get("CompanyName")
        self.BrandName = params.get("BrandName")
        self.Phone = params.get("Phone")
        self.License = params.get("License")
        self.LicenseStatus = params.get("LicenseStatus")
        self.LicenseNote = params.get("LicenseNote")
        self.Authorization = params.get("Authorization")
        self.AuthorizationStatus = params.get("AuthorizationStatus")
        self.AuthorizationNote = params.get("AuthorizationNote")
        if params.get("Trademarks") is not None:
            self.Trademarks = []
            for item in params.get("Trademarks"):
                obj = TrademarkData()
                obj._deserialize(item)
                self.Trademarks.append(obj)
        self.InsertTime = params.get("InsertTime")
        if params.get("Services") is not None:
            self.Services = ServiceData()
            self.Services._deserialize(params.get("Services"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPBrandRequest(AbstractModel):
    """CreateBPBrand请求参数结构体

    """

    def __init__(self):
        r"""
        :param BrandName: 品牌名称
        :type BrandName: str
        :param CompanyName: 企业名称
        :type CompanyName: str
        :param Phone: 联系电话
        :type Phone: str
        :param License: 营业执照
        :type License: str
        :param Authorization: 授权书
        :type Authorization: str
        :param TrademarkNames: 商标名称
        :type TrademarkNames: list of str
        :param Trademarks: 商标证明
        :type Trademarks: list of str
        :param IsTransfers: 是否涉及转让: 0-不转让 1-转让
        :type IsTransfers: list of str
        :param Transfers: 转让证明
        :type Transfers: list of str
        :param ProtectURLs: 保护网址
        :type ProtectURLs: list of str
        :param ProtectAPPs: 保护应用
        :type ProtectAPPs: list of str
        :param ProtectOfficialAccounts: 保护公众号
        :type ProtectOfficialAccounts: list of str
        :param ProtectMiniPrograms: 保护小程序
        :type ProtectMiniPrograms: list of str
        """
        self.BrandName = None
        self.CompanyName = None
        self.Phone = None
        self.License = None
        self.Authorization = None
        self.TrademarkNames = None
        self.Trademarks = None
        self.IsTransfers = None
        self.Transfers = None
        self.ProtectURLs = None
        self.ProtectAPPs = None
        self.ProtectOfficialAccounts = None
        self.ProtectMiniPrograms = None


    def _deserialize(self, params):
        self.BrandName = params.get("BrandName")
        self.CompanyName = params.get("CompanyName")
        self.Phone = params.get("Phone")
        self.License = params.get("License")
        self.Authorization = params.get("Authorization")
        self.TrademarkNames = params.get("TrademarkNames")
        self.Trademarks = params.get("Trademarks")
        self.IsTransfers = params.get("IsTransfers")
        self.Transfers = params.get("Transfers")
        self.ProtectURLs = params.get("ProtectURLs")
        self.ProtectAPPs = params.get("ProtectAPPs")
        self.ProtectOfficialAccounts = params.get("ProtectOfficialAccounts")
        self.ProtectMiniPrograms = params.get("ProtectMiniPrograms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPBrandResponse(AbstractModel):
    """CreateBPBrand返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 企业id
        :type CompanyId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.RequestId = params.get("RequestId")


class CreateBPFakeAPPListRequest(AbstractModel):
    """CreateBPFakeAPPList请求参数结构体

    """

    def __init__(self):
        r"""
        :param FakeAPPs: 批量模版
        :type FakeAPPs: str
        """
        self.FakeAPPs = None


    def _deserialize(self, params):
        self.FakeAPPs = params.get("FakeAPPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeAPPListResponse(AbstractModel):
    """CreateBPFakeAPPList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPFakeAPPRequest(AbstractModel):
    """CreateBPFakeAPP请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 企业id
        :type CompanyId: int
        :param FakeAPPName: 仿冒应用名称
        :type FakeAPPName: str
        :param APPChan: 仿冒来源
        :type APPChan: str
        :param FakeAPPPackageName: 仿冒应用包名
        :type FakeAPPPackageName: str
        :param FakeAPPCert: 仿冒应用证书
        :type FakeAPPCert: str
        :param FakeAPPSize: 仿冒应用大小
        :type FakeAPPSize: str
        :param FakeAPPSnapshots: 仿冒截图
        :type FakeAPPSnapshots: list of str
        :param Note: 备注
        :type Note: str
        """
        self.CompanyId = None
        self.FakeAPPName = None
        self.APPChan = None
        self.FakeAPPPackageName = None
        self.FakeAPPCert = None
        self.FakeAPPSize = None
        self.FakeAPPSnapshots = None
        self.Note = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.FakeAPPName = params.get("FakeAPPName")
        self.APPChan = params.get("APPChan")
        self.FakeAPPPackageName = params.get("FakeAPPPackageName")
        self.FakeAPPCert = params.get("FakeAPPCert")
        self.FakeAPPSize = params.get("FakeAPPSize")
        self.FakeAPPSnapshots = params.get("FakeAPPSnapshots")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeAPPResponse(AbstractModel):
    """CreateBPFakeAPP返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPFakeURLRequest(AbstractModel):
    """CreateBPFakeURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 企业id
        :type CompanyId: int
        :param FakeURL: 仿冒网址
        :type FakeURL: str
        :param FakeURLSnapshots: 仿冒网址截图
        :type FakeURLSnapshots: list of str
        :param Note: 备注
        :type Note: str
        """
        self.CompanyId = None
        self.FakeURL = None
        self.FakeURLSnapshots = None
        self.Note = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.FakeURL = params.get("FakeURL")
        self.FakeURLSnapshots = params.get("FakeURLSnapshots")
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


class CreateBPFakeURLsRequest(AbstractModel):
    """CreateBPFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param FakeURLs: 批量模版
        :type FakeURLs: str
        """
        self.FakeURLs = None


    def _deserialize(self, params):
        self.FakeURLs = params.get("FakeURLs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLsResponse(AbstractModel):
    """CreateBPFakeURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPWhiteListRequest(AbstractModel):
    """CreateBPWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 企业Id
        :type CompanyId: int
        :param WhiteListType: 白名单类型：0-网站 1-应用 2-公众号 3-小程
        :type WhiteListType: int
        :param WhiteLists: 白名单名称
        :type WhiteLists: list of str
        """
        self.CompanyId = None
        self.WhiteListType = None
        self.WhiteLists = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.WhiteListType = params.get("WhiteListType")
        self.WhiteLists = params.get("WhiteLists")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPWhiteListResponse(AbstractModel):
    """CreateBPWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBPWhiteListRequest(AbstractModel):
    """DeleteBPWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteListId: 白名单id
        :type WhiteListId: int
        """
        self.WhiteListId = None


    def _deserialize(self, params):
        self.WhiteListId = params.get("WhiteListId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBPWhiteListResponse(AbstractModel):
    """DeleteBPWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBPBrandsRequest(AbstractModel):
    """DescribeBPBrands请求参数结构体

    """


class DescribeBPBrandsResponse(AbstractModel):
    """DescribeBPBrands返回参数结构体

    """

    def __init__(self):
        r"""
        :param Brands: 品牌信息
        :type Brands: list of BrandData
        :param NoticeStatus: 品牌审核通知栏状态：0 不显示 1 显示
        :type NoticeStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Brands = None
        self.NoticeStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Brands") is not None:
            self.Brands = []
            for item in params.get("Brands"):
                obj = BrandData()
                obj._deserialize(item)
                self.Brands.append(obj)
        self.NoticeStatus = params.get("NoticeStatus")
        self.RequestId = params.get("RequestId")


class DescribeBPFakeAPPListRequest(AbstractModel):
    """DescribeBPFakeAPPList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
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
        


class DescribeBPFakeAPPListResponse(AbstractModel):
    """DescribeBPFakeAPPList返回参数结构体

    """

    def __init__(self):
        r"""
        :param FakeAPPList: 仿冒应用列表
        :type FakeAPPList: list of FakeAPPData
        :param TotalCount: 仿冒应用总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FakeAPPList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FakeAPPList") is not None:
            self.FakeAPPList = []
            for item in params.get("FakeAPPList"):
                obj = FakeAPPData()
                obj._deserialize(item)
                self.FakeAPPList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBPFakeURLsRequest(AbstractModel):
    """DescribeBPFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
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
        :param FakeURLs: 仿冒网址列表
        :type FakeURLs: list of FakeURLData
        :param TotalCount: 仿冒网址总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FakeURLs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FakeURLs") is not None:
            self.FakeURLs = []
            for item in params.get("FakeURLs"):
                obj = FakeURLData()
                obj._deserialize(item)
                self.FakeURLs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBPWhiteListsRequest(AbstractModel):
    """DescribeBPWhiteLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
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
        


class DescribeBPWhiteListsResponse(AbstractModel):
    """DescribeBPWhiteLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param WhiteLists: 白名单列表
        :type WhiteLists: list of WhiteListData
        :param TotalCount: 白名单总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WhiteLists = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhiteLists") is not None:
            self.WhiteLists = []
            for item in params.get("WhiteLists"):
                obj = WhiteListData()
                obj._deserialize(item)
                self.WhiteLists.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class FakeAPPData(AbstractModel):
    """仿冒应用数据

    """

    def __init__(self):
        r"""
        :param FakeAPPId: 仿冒应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPId: int
        :param BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param Origin: 仿冒来源：0-系统检测 1-人工举报
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: int
        :param FakeAPPName: 仿冒应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPName: str
        :param FakeAPPPackageName: 仿冒应用包名
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPPackageName: str
        :param FakeAPPCert: 仿冒应用证书
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPCert: str
        :param FakeAPPSize: 仿冒应用大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeAPPSize: str
        :param Heat: 热度
注意：此字段可能返回 null，表示取不到有效值。
        :type Heat: int
        :param BlockStatus: 协助处置状态：0-未处置 1-处置中 2-处置成功 3-处置失败
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockStatus: int
        :param BlockNote: 协助处置状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockNote: str
        :param OfflineStatus: 关停状态：0-未关停 1-关停中 2-关停成功 3-关停失败 4-重复上架
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineStatus: int
        :param OfflineNote: 关停状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineNote: str
        :param DownloadWay: app来源
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadWay: str
        :param InsertTime: 新增时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param DownloadCosURL: App下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadCosURL: str
        :param CertificationStatus: 资质证明状态:0-不可用 1-可用
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificationStatus: int
        """
        self.FakeAPPId = None
        self.BrandName = None
        self.Origin = None
        self.FakeAPPName = None
        self.FakeAPPPackageName = None
        self.FakeAPPCert = None
        self.FakeAPPSize = None
        self.Heat = None
        self.BlockStatus = None
        self.BlockNote = None
        self.OfflineStatus = None
        self.OfflineNote = None
        self.DownloadWay = None
        self.InsertTime = None
        self.DownloadCosURL = None
        self.CertificationStatus = None


    def _deserialize(self, params):
        self.FakeAPPId = params.get("FakeAPPId")
        self.BrandName = params.get("BrandName")
        self.Origin = params.get("Origin")
        self.FakeAPPName = params.get("FakeAPPName")
        self.FakeAPPPackageName = params.get("FakeAPPPackageName")
        self.FakeAPPCert = params.get("FakeAPPCert")
        self.FakeAPPSize = params.get("FakeAPPSize")
        self.Heat = params.get("Heat")
        self.BlockStatus = params.get("BlockStatus")
        self.BlockNote = params.get("BlockNote")
        self.OfflineStatus = params.get("OfflineStatus")
        self.OfflineNote = params.get("OfflineNote")
        self.DownloadWay = params.get("DownloadWay")
        self.InsertTime = params.get("InsertTime")
        self.DownloadCosURL = params.get("DownloadCosURL")
        self.CertificationStatus = params.get("CertificationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FakeURLData(AbstractModel):
    """仿冒网址数据

    """

    def __init__(self):
        r"""
        :param FakeURLId: 仿冒网址id
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeURLId: int
        :param BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param Origin: 仿冒来源：0-系统检测 1-人工举报
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: int
        :param FakeURL: 仿冒网址
注意：此字段可能返回 null，表示取不到有效值。
        :type FakeURL: str
        :param Heat: 热度
注意：此字段可能返回 null，表示取不到有效值。
        :type Heat: int
        :param BlockStatus: 协助处置状态：0-未处置 1-处置中 2-处置成功 3-处置失败
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockStatus: int
        :param BlockNote: 协助处置状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockNote: str
        :param OfflineStatus: 关停状态：0-未关停 1-关停中 2-关停成功 3-关停失败 4-重复上架
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineStatus: int
        :param OfflineNote: 关停状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineNote: str
        :param IP: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param IPLocation: ip地理位置
注意：此字段可能返回 null，表示取不到有效值。
        :type IPLocation: str
        :param WebCompany: 网站所属单位
注意：此字段可能返回 null，表示取不到有效值。
        :type WebCompany: str
        :param WebAttribute: 网站性质
注意：此字段可能返回 null，表示取不到有效值。
        :type WebAttribute: str
        :param WebName: 网站名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WebName: str
        :param WebICP: 备案号
注意：此字段可能返回 null，表示取不到有效值。
        :type WebICP: str
        :param WebCreateTime: 网站创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type WebCreateTime: str
        :param WebExpireTime: 网站过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type WebExpireTime: str
        :param InsertTime: 新增时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param CertificationStatus: 资质证明状态：0-不可用 1-可用
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificationStatus: int
        """
        self.FakeURLId = None
        self.BrandName = None
        self.Origin = None
        self.FakeURL = None
        self.Heat = None
        self.BlockStatus = None
        self.BlockNote = None
        self.OfflineStatus = None
        self.OfflineNote = None
        self.IP = None
        self.IPLocation = None
        self.WebCompany = None
        self.WebAttribute = None
        self.WebName = None
        self.WebICP = None
        self.WebCreateTime = None
        self.WebExpireTime = None
        self.InsertTime = None
        self.CertificationStatus = None


    def _deserialize(self, params):
        self.FakeURLId = params.get("FakeURLId")
        self.BrandName = params.get("BrandName")
        self.Origin = params.get("Origin")
        self.FakeURL = params.get("FakeURL")
        self.Heat = params.get("Heat")
        self.BlockStatus = params.get("BlockStatus")
        self.BlockNote = params.get("BlockNote")
        self.OfflineStatus = params.get("OfflineStatus")
        self.OfflineNote = params.get("OfflineNote")
        self.IP = params.get("IP")
        self.IPLocation = params.get("IPLocation")
        self.WebCompany = params.get("WebCompany")
        self.WebAttribute = params.get("WebAttribute")
        self.WebName = params.get("WebName")
        self.WebICP = params.get("WebICP")
        self.WebCreateTime = params.get("WebCreateTime")
        self.WebExpireTime = params.get("WebExpireTime")
        self.InsertTime = params.get("InsertTime")
        self.CertificationStatus = params.get("CertificationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤参数

    """

    def __init__(self):
        r"""
        :param Name: 过滤参数键
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 过滤参数值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ServiceData(AbstractModel):
    """服务响应数据

    """

    def __init__(self):
        r"""
        :param ProtectURLCount: 网站保护关联资产数
        :type ProtectURLCount: int
        :param ProtectURLExpireTime: 网站保护服务到期时间
        :type ProtectURLExpireTime: str
        :param ProtectAPPCount: 应用保护关联资产数
        :type ProtectAPPCount: int
        :param ProtectAPPExpireTime: 应用保护服务到期时间
        :type ProtectAPPExpireTime: str
        :param ProtectOfficialAccountCount: 公众号保护关联资产数
        :type ProtectOfficialAccountCount: int
        :param ProtectOfficialAccountExpireTime: 公众号保护服务到期时间
        :type ProtectOfficialAccountExpireTime: str
        :param ProtectMiniProgramCount: 小程序保护关联资产数
        :type ProtectMiniProgramCount: int
        :param ProtectMiniProgramExpireTime: 小程序保护服务到期时间
        :type ProtectMiniProgramExpireTime: str
        :param OfflineCount: 关停下架使用次数
        :type OfflineCount: int
        """
        self.ProtectURLCount = None
        self.ProtectURLExpireTime = None
        self.ProtectAPPCount = None
        self.ProtectAPPExpireTime = None
        self.ProtectOfficialAccountCount = None
        self.ProtectOfficialAccountExpireTime = None
        self.ProtectMiniProgramCount = None
        self.ProtectMiniProgramExpireTime = None
        self.OfflineCount = None


    def _deserialize(self, params):
        self.ProtectURLCount = params.get("ProtectURLCount")
        self.ProtectURLExpireTime = params.get("ProtectURLExpireTime")
        self.ProtectAPPCount = params.get("ProtectAPPCount")
        self.ProtectAPPExpireTime = params.get("ProtectAPPExpireTime")
        self.ProtectOfficialAccountCount = params.get("ProtectOfficialAccountCount")
        self.ProtectOfficialAccountExpireTime = params.get("ProtectOfficialAccountExpireTime")
        self.ProtectMiniProgramCount = params.get("ProtectMiniProgramCount")
        self.ProtectMiniProgramExpireTime = params.get("ProtectMiniProgramExpireTime")
        self.OfflineCount = params.get("OfflineCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrademarkData(AbstractModel):
    """商标响应数据

    """

    def __init__(self):
        r"""
        :param Trademark: 商标证明
        :type Trademark: str
        :param TrademarkStatus: 商标审核状态
        :type TrademarkStatus: int
        :param TrademarkNote: 商标审核状态说明
        :type TrademarkNote: str
        :param TrademarkId: 商标id
        :type TrademarkId: int
        :param Transfer: 商标转让书
        :type Transfer: str
        :param TransferStatus: 商标转让书审核状态
        :type TransferStatus: int
        :param TransferNote: 商标转让书审核状态说明
        :type TransferNote: str
        :param TrademarkName: 商标名称
        :type TrademarkName: str
        """
        self.Trademark = None
        self.TrademarkStatus = None
        self.TrademarkNote = None
        self.TrademarkId = None
        self.Transfer = None
        self.TransferStatus = None
        self.TransferNote = None
        self.TrademarkName = None


    def _deserialize(self, params):
        self.Trademark = params.get("Trademark")
        self.TrademarkStatus = params.get("TrademarkStatus")
        self.TrademarkNote = params.get("TrademarkNote")
        self.TrademarkId = params.get("TrademarkId")
        self.Transfer = params.get("Transfer")
        self.TransferStatus = params.get("TransferStatus")
        self.TransferNote = params.get("TransferNote")
        self.TrademarkName = params.get("TrademarkName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteListData(AbstractModel):
    """白名单数据

    """

    def __init__(self):
        r"""
        :param WhiteListId: 白名单id
注意：此字段可能返回 null，表示取不到有效值。
        :type WhiteListId: int
        :param CompanyId: 企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompanyId: int
        :param BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param AssetsType: 资产类型：0-网站 1-app 2-公众号 3-小程序
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetsType: int
        :param WhiteList: 白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type WhiteList: str
        :param InsertTime: 新增时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        """
        self.WhiteListId = None
        self.CompanyId = None
        self.BrandName = None
        self.AssetsType = None
        self.WhiteList = None
        self.InsertTime = None


    def _deserialize(self, params):
        self.WhiteListId = params.get("WhiteListId")
        self.CompanyId = params.get("CompanyId")
        self.BrandName = params.get("BrandName")
        self.AssetsType = params.get("AssetsType")
        self.WhiteList = params.get("WhiteList")
        self.InsertTime = params.get("InsertTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        