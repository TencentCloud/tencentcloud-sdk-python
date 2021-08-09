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


class AuthInfo(AbstractModel):
    """授权人信息

    """

    def __init__(self):
        """
        :param Id: 主键\n        :type Id: str\n        :param Name: 授权人名称\n        :type Name: str\n        :param Code: 身份证号/社会信用代码\n        :type Code: str\n        :param Type: 授权人类型\n        :type Type: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        """
        self.Id = None
        self.Name = None
        self.Code = None
        self.Type = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeOrderCertificateRequest(AbstractModel):
    """BatchDescribeOrderCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param OrderIds: 要下载授权书的订单id\n        :type OrderIds: list of str\n        """
        self.OrderIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeOrderCertificateResponse(AbstractModel):
    """BatchDescribeOrderCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateUrls: 授权书的下载地址\n        :type CertificateUrls: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateUrls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateUrls = params.get("CertificateUrls")
        self.RequestId = params.get("RequestId")


class BatchDescribeOrderImageRequest(AbstractModel):
    """BatchDescribeOrderImage请求参数结构体

    """

    def __init__(self):
        """
        :param OrderIds: 要下载图片的订单id\n        :type OrderIds: list of str\n        """
        self.OrderIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeOrderImageResponse(AbstractModel):
    """BatchDescribeOrderImage返回参数结构体

    """

    def __init__(self):
        """
        :param ImageUrls: 图片的下载地址\n        :type ImageUrls: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImageUrls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrls = params.get("ImageUrls")
        self.RequestId = params.get("RequestId")


class CreateOrderAndDownloadsRequest(AbstractModel):
    """CreateOrderAndDownloads请求参数结构体

    """

    def __init__(self):
        """
        :param ImageInfos: ImageId必填，单张购买，所有必填，会员身份可以省略部分参数\n        :type ImageInfos: list of ImageInfo\n        """
        self.ImageInfos = None


    def _deserialize(self, params):
        if params.get("ImageInfos") is not None:
            self.ImageInfos = []
            for item in params.get("ImageInfos"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.ImageInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderAndDownloadsResponse(AbstractModel):
    """CreateOrderAndDownloads返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadInfos: 成功核销后可以获取图片基本信息和原图地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownloadInfos: list of DownloadInfo\n        :param TotalCount: 可下载图片数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DownloadInfos = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DownloadInfos") is not None:
            self.DownloadInfos = []
            for item in params.get("DownloadInfos"):
                obj = DownloadInfo()
                obj._deserialize(item)
                self.DownloadInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class CreateOrderAndPayRequest(AbstractModel):
    """CreateOrderAndPay请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 图片ID\n        :type ImageId: int\n        :param AuthUserId: 授权人ID\n        :type AuthUserId: str\n        :param MarshalId: 售卖组合id\n        :type MarshalId: int\n        """
        self.ImageId = None
        self.AuthUserId = None
        self.MarshalId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.AuthUserId = params.get("AuthUserId")
        self.MarshalId = params.get("MarshalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderAndPayResponse(AbstractModel):
    """CreateOrderAndPay返回参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单ID\n        :type OrderId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OrderId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.RequestId = params.get("RequestId")


class DescribeAuthUsersRequest(AbstractModel):
    """DescribeAuthUsers请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页大小\n        :type Limit: int\n        :param Offset: 页偏移量\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthUsersResponse(AbstractModel):
    """DescribeAuthUsers返回参数结构体

    """

    def __init__(self):
        """
        :param Users: 授权人信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Users: list of AuthInfo\n        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param OldUser: 是否是老策略用户\n        :type OldUser: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Users = None
        self.TotalCount = None
        self.OldUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = AuthInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.OldUser = params.get("OldUser")
        self.RequestId = params.get("RequestId")


class DescribeDownloadInfosRequest(AbstractModel):
    """DescribeDownloadInfos请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 默认10\n        :type Limit: int\n        :param Offset: 默认0\n        :type Offset: int\n        :param BeginTime: 开始时间晚于指定时间\n        :type BeginTime: str\n        :param EndTime: 结束时间早于指定时间\n        :type EndTime: str\n        :param ImageIds: 无效值，过滤结果为空\n        :type ImageIds: list of int\n        """
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None
        self.ImageIds = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDownloadInfosResponse(AbstractModel):
    """DescribeDownloadInfos返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadInfos: 核销下载记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownloadInfos: list of DownloadInfo\n        :param TotalCount: 总记录数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DownloadInfos = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DownloadInfos") is not None:
            self.DownloadInfos = []
            for item in params.get("DownloadInfos"):
                obj = DownloadInfo()
                obj._deserialize(item)
                self.DownloadInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 图片ID\n        :type ImageId: int\n        """
        self.ImageId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 图片ID\n        :type ImageId: int\n        :param Title: 图片标题\n        :type Title: str\n        :param Description: 图片描述\n        :type Description: str\n        :param PreviewUrl: 图片预览链接\n        :type PreviewUrl: str\n        :param ThumbUrl: 图片缩略图\n        :type ThumbUrl: str\n        :param Vendor: 图片供应商\n        :type Vendor: str\n        :param Marshals: 图片售卖组合信息\n        :type Marshals: list of ImageMarshal\n        :param Width: 宽\n        :type Width: int\n        :param Height: 高\n        :type Height: int\n        :param ImageFormat: 图片格式 jpg/eps/psd/...\n        :type ImageFormat: str\n        :param ImageSenseType: 图片类型 摄影图片、插画、漫画、图表、矢量、psd、全景、gif、模板\n        :type ImageSenseType: str\n        :param Keywords: 关键词，多关键词用空格分隔\n        :type Keywords: str\n        :param LayeredGalleryId: 分层图库id\n        :type LayeredGalleryId: int\n        :param Orientation: 构图方式：horizontal:横图、vertical:竖图、square:方图\n        :type Orientation: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImageId = None
        self.Title = None
        self.Description = None
        self.PreviewUrl = None
        self.ThumbUrl = None
        self.Vendor = None
        self.Marshals = None
        self.Width = None
        self.Height = None
        self.ImageFormat = None
        self.ImageSenseType = None
        self.Keywords = None
        self.LayeredGalleryId = None
        self.Orientation = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.PreviewUrl = params.get("PreviewUrl")
        self.ThumbUrl = params.get("ThumbUrl")
        self.Vendor = params.get("Vendor")
        if params.get("Marshals") is not None:
            self.Marshals = []
            for item in params.get("Marshals"):
                obj = ImageMarshal()
                obj._deserialize(item)
                self.Marshals.append(obj)
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ImageFormat = params.get("ImageFormat")
        self.ImageSenseType = params.get("ImageSenseType")
        self.Keywords = params.get("Keywords")
        self.LayeredGalleryId = params.get("LayeredGalleryId")
        self.Orientation = params.get("Orientation")
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 页偏移量\n        :type Offset: int\n        :param Limit: 页大小\n        :type Limit: int\n        :param Keyword: 搜索关键字\n        :type Keyword: str\n        :param Orientation: 构图方式，可选以下值：horizontal、vertical、square，分别代表以下含义：横图、竖图、方图\n        :type Orientation: str\n        :param ImageSenseType: 图片类型，可选以下值：照片、插画\n        :type ImageSenseType: str\n        :param LayeredGalleryIds: 分层图库id数组，可选以下数值：1(基础)，2(精选)，3(高级)\n        :type LayeredGalleryIds: list of int\n        """
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Orientation = None
        self.ImageSenseType = None
        self.LayeredGalleryIds = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Orientation = params.get("Orientation")
        self.ImageSenseType = params.get("ImageSenseType")
        self.LayeredGalleryIds = params.get("LayeredGalleryIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        """
        :param Offset: 页偏移量\n        :type Offset: int\n        :param Limit: 页大小\n        :type Limit: int\n        :param Total: 总条数\n        :type Total: int\n        :param HaveMore: 是否有下一页\n        :type HaveMore: bool\n        :param Items: 图片信息数组\n        :type Items: list of ImageItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Offset = None
        self.Limit = None
        self.Total = None
        self.HaveMore = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Total = params.get("Total")
        self.HaveMore = params.get("HaveMore")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ImageItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadInfo(AbstractModel):
    """图片下载信息

    """

    def __init__(self):
        """
        :param ImageInfo: 图片基础信息\n        :type ImageInfo: :class:`tencentcloud.ape.v20200513.models.ImageInfo`\n        :param ImageUrl: 图片原图URL\n        :type ImageUrl: str\n        :param ImageThumbUrl: 图片缩略图URL\n        :type ImageThumbUrl: str\n        :param OrderId: 订单Id\n        :type OrderId: str\n        :param OrderCreateTime: 订单创建时间\n        :type OrderCreateTime: str\n        :param DownloadId: 下载Id\n        :type DownloadId: str\n        :param DownloadTime: 下载时间\n        :type DownloadTime: str\n        :param ConsumeType: 图片购买类型，单张/会员\n        :type ConsumeType: int\n        :param FirstDownload: 是否首次下载\n        :type FirstDownload: bool\n        """
        self.ImageInfo = None
        self.ImageUrl = None
        self.ImageThumbUrl = None
        self.OrderId = None
        self.OrderCreateTime = None
        self.DownloadId = None
        self.DownloadTime = None
        self.ConsumeType = None
        self.FirstDownload = None


    def _deserialize(self, params):
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.ImageUrl = params.get("ImageUrl")
        self.ImageThumbUrl = params.get("ImageThumbUrl")
        self.OrderId = params.get("OrderId")
        self.OrderCreateTime = params.get("OrderCreateTime")
        self.DownloadId = params.get("DownloadId")
        self.DownloadTime = params.get("DownloadTime")
        self.ConsumeType = params.get("ConsumeType")
        self.FirstDownload = params.get("FirstDownload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """图片基础信息

    """

    def __init__(self):
        """
        :param ImageId: 图片Id\n        :type ImageId: int\n        :param LicenseScopeId: 授权场景Id\n        :type LicenseScopeId: int\n        :param DimensionsNameId: 尺寸名称Id\n        :type DimensionsNameId: int\n        :param UserId: 平台用户标识\n        :type UserId: str\n        :param DownloadPrice: 平台用户下载图片购买的价格(单位:分)\n        :type DownloadPrice: int\n        :param DownloadType: 下载类型。匹配集合中的任意元素：
<li>Single: 单张购买下载</li>
<li>BasicEnterpriseMember: 企业基础会员下载</li>
<li>AdvancedEnterpriseMember: 企业高级会员下载</li>
<li>DistinguishedEnterpriseMember: 企业尊享会员下载</li>\n        :type DownloadType: str\n        """
        self.ImageId = None
        self.LicenseScopeId = None
        self.DimensionsNameId = None
        self.UserId = None
        self.DownloadPrice = None
        self.DownloadType = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.LicenseScopeId = params.get("LicenseScopeId")
        self.DimensionsNameId = params.get("DimensionsNameId")
        self.UserId = params.get("UserId")
        self.DownloadPrice = params.get("DownloadPrice")
        self.DownloadType = params.get("DownloadType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageItem(AbstractModel):
    """图片信息条目

    """

    def __init__(self):
        """
        :param ImageId: 图片ID\n        :type ImageId: int\n        :param Title: 图片标题\n        :type Title: str\n        :param Description: 图片描述\n        :type Description: str\n        :param PreviewUrl: 图片预览链接\n        :type PreviewUrl: str\n        :param ThumbUrl: 图片缩略图\n        :type ThumbUrl: str\n        :param Vendor: 图片供应商\n        :type Vendor: str\n        :param Keywords: 图片关键词\n        :type Keywords: str\n        :param Width: 宽\n        :type Width: int\n        :param Height: 高\n        :type Height: int\n        """
        self.ImageId = None
        self.Title = None
        self.Description = None
        self.PreviewUrl = None
        self.ThumbUrl = None
        self.Vendor = None
        self.Keywords = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.PreviewUrl = params.get("PreviewUrl")
        self.ThumbUrl = params.get("ThumbUrl")
        self.Vendor = params.get("Vendor")
        self.Keywords = params.get("Keywords")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageMarshal(AbstractModel):
    """图片售卖组合信息

    """

    def __init__(self):
        """
        :param MarshalId: 售卖组合唯一标识\n        :type MarshalId: int\n        :param Height: 图片高度\n        :type Height: int\n        :param Width: 图片宽度\n        :type Width: int\n        :param Size: 图片大小\n        :type Size: int\n        :param Format: 图片格式\n        :type Format: str\n        :param Price: 图片价格(单位:分)\n        :type Price: int\n        :param LicenseScope: 授权范围\n        :type LicenseScope: str\n        :param IsVip: 是否支持VIP购买\n        :type IsVip: bool\n        :param LicenseScopeId: 授权范围id\n        :type LicenseScopeId: int\n        :param DimensionsName: 尺寸\n        :type DimensionsName: str\n        :param DimensionsNameId: 尺寸id\n        :type DimensionsNameId: int\n        """
        self.MarshalId = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Format = None
        self.Price = None
        self.LicenseScope = None
        self.IsVip = None
        self.LicenseScopeId = None
        self.DimensionsName = None
        self.DimensionsNameId = None


    def _deserialize(self, params):
        self.MarshalId = params.get("MarshalId")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Format = params.get("Format")
        self.Price = params.get("Price")
        self.LicenseScope = params.get("LicenseScope")
        self.IsVip = params.get("IsVip")
        self.LicenseScopeId = params.get("LicenseScopeId")
        self.DimensionsName = params.get("DimensionsName")
        self.DimensionsNameId = params.get("DimensionsNameId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        