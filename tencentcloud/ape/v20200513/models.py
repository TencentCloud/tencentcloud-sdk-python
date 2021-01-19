# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AuthInfo(AbstractModel):
    """授权人信息

    """

    def __init__(self):
        """
        :param Id: 主键
        :type Id: str
        :param Name: 授权人名称
        :type Name: str
        :param Code: 身份证号/社会信用代码
        :type Code: str
        :param Type: 授权人类型
        :type Type: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
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


class BatchDescribeOrderCertificateRequest(AbstractModel):
    """BatchDescribeOrderCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param OrderIds: 要下载授权书的订单id
        :type OrderIds: list of str
        """
        self.OrderIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")


class BatchDescribeOrderCertificateResponse(AbstractModel):
    """BatchDescribeOrderCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateUrls: 授权书的下载地址
        :type CertificateUrls: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param OrderIds: 要下载图片的订单id
        :type OrderIds: list of str
        """
        self.OrderIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")


class BatchDescribeOrderImageResponse(AbstractModel):
    """BatchDescribeOrderImage返回参数结构体

    """

    def __init__(self):
        """
        :param ImageUrls: 图片的下载地址
        :type ImageUrls: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageUrls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrls = params.get("ImageUrls")
        self.RequestId = params.get("RequestId")


class CreateOrderAndPayRequest(AbstractModel):
    """CreateOrderAndPay请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 图片ID
        :type ImageId: int
        :param AuthUserId: 授权人ID
        :type AuthUserId: str
        :param MarshalId: 售卖组合id
        :type MarshalId: int
        """
        self.ImageId = None
        self.AuthUserId = None
        self.MarshalId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.AuthUserId = params.get("AuthUserId")
        self.MarshalId = params.get("MarshalId")


class CreateOrderAndPayResponse(AbstractModel):
    """CreateOrderAndPay返回参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单ID
        :type OrderId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Limit: 分页大小
        :type Limit: int
        :param Offset: 页偏移量
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAuthUsersResponse(AbstractModel):
    """DescribeAuthUsers返回参数结构体

    """

    def __init__(self):
        """
        :param Users: 授权人信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of AuthInfo
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param OldUser: 是否是老策略用户
        :type OldUser: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 图片ID
        :type ImageId: int
        """
        self.ImageId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 图片ID
        :type ImageId: int
        :param Title: 图片标题
        :type Title: str
        :param Description: 图片描述
        :type Description: str
        :param PreviewUrl: 图片预览链接
        :type PreviewUrl: str
        :param ThumbUrl: 图片缩略图
        :type ThumbUrl: str
        :param Vendor: 图片供应商
        :type Vendor: str
        :param Marshals: 图片售卖组合信息
        :type Marshals: list of ImageMarshal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageId = None
        self.Title = None
        self.Description = None
        self.PreviewUrl = None
        self.ThumbUrl = None
        self.Vendor = None
        self.Marshals = None
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
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 页偏移量
        :type Offset: int
        :param Limit: 页大小
        :type Limit: int
        :param Keyword: 搜索关键字
        :type Keyword: str
        :param Orientation: 构图方式，可选以下值：horizontal、vertical、square，分别代表以下含义：横图、竖图、方图
        :type Orientation: str
        :param ImageSenseType: 图片类型，可选以下值：照片、插画
        :type ImageSenseType: str
        :param LayeredGalleryIds: 分层图库id数组，可选以下数值：1(基础)，2(精选)，3(高级)
        :type LayeredGalleryIds: list of int
        """
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


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        """
        :param Offset: 页偏移量
        :type Offset: int
        :param Limit: 页大小
        :type Limit: int
        :param Total: 总条数
        :type Total: int
        :param HaveMore: 是否有下一页
        :type HaveMore: bool
        :param Items: 图片信息数组
        :type Items: list of ImageItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class ImageItem(AbstractModel):
    """图片信息条目

    """

    def __init__(self):
        """
        :param ImageId: 图片ID
        :type ImageId: int
        :param Title: 图片标题
        :type Title: str
        :param Description: 图片描述
        :type Description: str
        :param PreviewUrl: 图片预览链接
        :type PreviewUrl: str
        :param ThumbUrl: 图片缩略图
        :type ThumbUrl: str
        :param Vendor: 图片供应商
        :type Vendor: str
        """
        self.ImageId = None
        self.Title = None
        self.Description = None
        self.PreviewUrl = None
        self.ThumbUrl = None
        self.Vendor = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.PreviewUrl = params.get("PreviewUrl")
        self.ThumbUrl = params.get("ThumbUrl")
        self.Vendor = params.get("Vendor")


class ImageMarshal(AbstractModel):
    """图片售卖组合信息

    """

    def __init__(self):
        """
        :param MarshalId: 售卖组合唯一标识
        :type MarshalId: int
        :param Height: 图片高度
        :type Height: int
        :param Width: 图片宽度
        :type Width: int
        :param Size: 图片大小
        :type Size: int
        :param Format: 图片格式
        :type Format: str
        :param Price: 图片价格(单位:分)
        :type Price: int
        :param LicenseScope: 授权范围
        :type LicenseScope: str
        :param IsVip: 是否支持VIP购买
        :type IsVip: bool
        """
        self.MarshalId = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Format = None
        self.Price = None
        self.LicenseScope = None
        self.IsVip = None


    def _deserialize(self, params):
        self.MarshalId = params.get("MarshalId")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Format = params.get("Format")
        self.Price = params.get("Price")
        self.LicenseScope = params.get("LicenseScope")
        self.IsVip = params.get("IsVip")