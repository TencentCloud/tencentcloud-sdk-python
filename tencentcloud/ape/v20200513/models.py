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
        r"""
        :param _Id: 主键
        :type Id: str
        :param _Name: 授权人名称
        :type Name: str
        :param _Code: 身份证号/社会信用代码
        :type Code: str
        :param _Type: 授权人类型
        :type Type: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._Id = None
        self._Name = None
        self._Code = None
        self._Type = None
        self._CreateTime = None

    @property
    def Id(self):
        """主键
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """授权人名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Code(self):
        """身份证号/社会信用代码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Type(self):
        """授权人类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Code = params.get("Code")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeOrderCertificateRequest(AbstractModel):
    """BatchDescribeOrderCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderIds: 要下载授权书的订单id
        :type OrderIds: list of str
        """
        self._OrderIds = None

    @property
    def OrderIds(self):
        """要下载授权书的订单id
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeOrderCertificateResponse(AbstractModel):
    """BatchDescribeOrderCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateUrls: 授权书的下载地址
        :type CertificateUrls: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateUrls = None
        self._RequestId = None

    @property
    def CertificateUrls(self):
        """授权书的下载地址
        :rtype: list of str
        """
        return self._CertificateUrls

    @CertificateUrls.setter
    def CertificateUrls(self, CertificateUrls):
        self._CertificateUrls = CertificateUrls

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateUrls = params.get("CertificateUrls")
        self._RequestId = params.get("RequestId")


class BatchDescribeOrderImageRequest(AbstractModel):
    """BatchDescribeOrderImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderIds: 要下载图片的订单id
        :type OrderIds: list of str
        """
        self._OrderIds = None

    @property
    def OrderIds(self):
        """要下载图片的订单id
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeOrderImageResponse(AbstractModel):
    """BatchDescribeOrderImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrls: 图片的下载地址
        :type ImageUrls: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageUrls = None
        self._RequestId = None

    @property
    def ImageUrls(self):
        """图片的下载地址
        :rtype: list of str
        """
        return self._ImageUrls

    @ImageUrls.setter
    def ImageUrls(self, ImageUrls):
        self._ImageUrls = ImageUrls

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageUrls = params.get("ImageUrls")
        self._RequestId = params.get("RequestId")


class CreateOrderAndDownloadsRequest(AbstractModel):
    """CreateOrderAndDownloads请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageInfos: ImageId必填，单张购买，所有必填，会员身份可以省略部分参数
        :type ImageInfos: list of ImageInfo
        """
        self._ImageInfos = None

    @property
    def ImageInfos(self):
        """ImageId必填，单张购买，所有必填，会员身份可以省略部分参数
        :rtype: list of ImageInfo
        """
        return self._ImageInfos

    @ImageInfos.setter
    def ImageInfos(self, ImageInfos):
        self._ImageInfos = ImageInfos


    def _deserialize(self, params):
        if params.get("ImageInfos") is not None:
            self._ImageInfos = []
            for item in params.get("ImageInfos"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._ImageInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderAndDownloadsResponse(AbstractModel):
    """CreateOrderAndDownloads返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadInfos: 成功核销后可以获取图片基本信息和原图地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadInfos: list of DownloadInfo
        :param _TotalCount: 可下载图片数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DownloadInfos(self):
        """成功核销后可以获取图片基本信息和原图地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DownloadInfo
        """
        return self._DownloadInfos

    @DownloadInfos.setter
    def DownloadInfos(self, DownloadInfos):
        self._DownloadInfos = DownloadInfos

    @property
    def TotalCount(self):
        """可下载图片数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DownloadInfos") is not None:
            self._DownloadInfos = []
            for item in params.get("DownloadInfos"):
                obj = DownloadInfo()
                obj._deserialize(item)
                self._DownloadInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class CreateOrderAndPayRequest(AbstractModel):
    """CreateOrderAndPay请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 图片ID
        :type ImageId: int
        :param _AuthUserId: 授权人ID
        :type AuthUserId: str
        :param _MarshalId: 售卖组合id
        :type MarshalId: int
        """
        self._ImageId = None
        self._AuthUserId = None
        self._MarshalId = None

    @property
    def ImageId(self):
        """图片ID
        :rtype: int
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def AuthUserId(self):
        """授权人ID
        :rtype: str
        """
        return self._AuthUserId

    @AuthUserId.setter
    def AuthUserId(self, AuthUserId):
        self._AuthUserId = AuthUserId

    @property
    def MarshalId(self):
        """售卖组合id
        :rtype: int
        """
        return self._MarshalId

    @MarshalId.setter
    def MarshalId(self, MarshalId):
        self._MarshalId = MarshalId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._AuthUserId = params.get("AuthUserId")
        self._MarshalId = params.get("MarshalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderAndPayResponse(AbstractModel):
    """CreateOrderAndPay返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单ID
        :type OrderId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._RequestId = None

    @property
    def OrderId(self):
        """订单ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._RequestId = params.get("RequestId")


class DescribeAuthUsersRequest(AbstractModel):
    """DescribeAuthUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 页偏移量
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthUsersResponse(AbstractModel):
    """DescribeAuthUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 授权人信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of AuthInfo
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _OldUser: 是否是老策略用户
        :type OldUser: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Users = None
        self._TotalCount = None
        self._OldUser = None
        self._RequestId = None

    @property
    def Users(self):
        """授权人信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AuthInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def TotalCount(self):
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OldUser(self):
        """是否是老策略用户
        :rtype: bool
        """
        return self._OldUser

    @OldUser.setter
    def OldUser(self, OldUser):
        self._OldUser = OldUser

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = AuthInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._OldUser = params.get("OldUser")
        self._RequestId = params.get("RequestId")


class DescribeDownloadInfosRequest(AbstractModel):
    """DescribeDownloadInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 默认10
        :type Limit: int
        :param _Offset: 默认0
        :type Offset: int
        :param _BeginTime: 开始时间晚于指定时间
        :type BeginTime: str
        :param _EndTime: 结束时间早于指定时间
        :type EndTime: str
        :param _ImageIds: 无效值，过滤结果为空
        :type ImageIds: list of int
        """
        self._Limit = None
        self._Offset = None
        self._BeginTime = None
        self._EndTime = None
        self._ImageIds = None

    @property
    def Limit(self):
        """默认10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BeginTime(self):
        """开始时间晚于指定时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """结束时间早于指定时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ImageIds(self):
        """无效值，过滤结果为空
        :rtype: list of int
        """
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDownloadInfosResponse(AbstractModel):
    """DescribeDownloadInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadInfos: 核销下载记录
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadInfos: list of DownloadInfo
        :param _TotalCount: 总记录数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DownloadInfos(self):
        """核销下载记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DownloadInfo
        """
        return self._DownloadInfos

    @DownloadInfos.setter
    def DownloadInfos(self, DownloadInfos):
        self._DownloadInfos = DownloadInfos

    @property
    def TotalCount(self):
        """总记录数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DownloadInfos") is not None:
            self._DownloadInfos = []
            for item in params.get("DownloadInfos"):
                obj = DownloadInfo()
                obj._deserialize(item)
                self._DownloadInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 图片ID
        :type ImageId: int
        """
        self._ImageId = None

    @property
    def ImageId(self):
        """图片ID
        :rtype: int
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 图片ID
        :type ImageId: int
        :param _Title: 图片标题
        :type Title: str
        :param _Description: 图片描述
        :type Description: str
        :param _PreviewUrl: 图片预览链接
        :type PreviewUrl: str
        :param _ThumbUrl: 图片缩略图
        :type ThumbUrl: str
        :param _Vendor: 图片供应商
        :type Vendor: str
        :param _Marshals: 图片售卖组合信息
        :type Marshals: list of ImageMarshal
        :param _Width: 宽
        :type Width: int
        :param _Height: 高
        :type Height: int
        :param _ImageFormat: 图片格式 jpg/eps/psd/...
        :type ImageFormat: str
        :param _ImageSenseType: 图片类型 摄影图片、插画、漫画、图表、矢量、psd、全景、gif、模板
        :type ImageSenseType: str
        :param _Keywords: 关键词，多关键词用空格分隔
        :type Keywords: str
        :param _LayeredGalleryId: 分层图库id
        :type LayeredGalleryId: int
        :param _Orientation: 构图方式：horizontal:横图、vertical:竖图、square:方图
        :type Orientation: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageId = None
        self._Title = None
        self._Description = None
        self._PreviewUrl = None
        self._ThumbUrl = None
        self._Vendor = None
        self._Marshals = None
        self._Width = None
        self._Height = None
        self._ImageFormat = None
        self._ImageSenseType = None
        self._Keywords = None
        self._LayeredGalleryId = None
        self._Orientation = None
        self._RequestId = None

    @property
    def ImageId(self):
        """图片ID
        :rtype: int
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Title(self):
        """图片标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        """图片描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PreviewUrl(self):
        """图片预览链接
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def ThumbUrl(self):
        """图片缩略图
        :rtype: str
        """
        return self._ThumbUrl

    @ThumbUrl.setter
    def ThumbUrl(self, ThumbUrl):
        self._ThumbUrl = ThumbUrl

    @property
    def Vendor(self):
        """图片供应商
        :rtype: str
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Marshals(self):
        """图片售卖组合信息
        :rtype: list of ImageMarshal
        """
        return self._Marshals

    @Marshals.setter
    def Marshals(self, Marshals):
        self._Marshals = Marshals

    @property
    def Width(self):
        """宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """高
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def ImageFormat(self):
        """图片格式 jpg/eps/psd/...
        :rtype: str
        """
        return self._ImageFormat

    @ImageFormat.setter
    def ImageFormat(self, ImageFormat):
        self._ImageFormat = ImageFormat

    @property
    def ImageSenseType(self):
        """图片类型 摄影图片、插画、漫画、图表、矢量、psd、全景、gif、模板
        :rtype: str
        """
        return self._ImageSenseType

    @ImageSenseType.setter
    def ImageSenseType(self, ImageSenseType):
        self._ImageSenseType = ImageSenseType

    @property
    def Keywords(self):
        """关键词，多关键词用空格分隔
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def LayeredGalleryId(self):
        """分层图库id
        :rtype: int
        """
        return self._LayeredGalleryId

    @LayeredGalleryId.setter
    def LayeredGalleryId(self, LayeredGalleryId):
        self._LayeredGalleryId = LayeredGalleryId

    @property
    def Orientation(self):
        """构图方式：horizontal:横图、vertical:竖图、square:方图
        :rtype: str
        """
        return self._Orientation

    @Orientation.setter
    def Orientation(self, Orientation):
        self._Orientation = Orientation

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        self._PreviewUrl = params.get("PreviewUrl")
        self._ThumbUrl = params.get("ThumbUrl")
        self._Vendor = params.get("Vendor")
        if params.get("Marshals") is not None:
            self._Marshals = []
            for item in params.get("Marshals"):
                obj = ImageMarshal()
                obj._deserialize(item)
                self._Marshals.append(obj)
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._ImageFormat = params.get("ImageFormat")
        self._ImageSenseType = params.get("ImageSenseType")
        self._Keywords = params.get("Keywords")
        self._LayeredGalleryId = params.get("LayeredGalleryId")
        self._Orientation = params.get("Orientation")
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页偏移量
        :type Offset: int
        :param _Limit: 页大小
        :type Limit: int
        :param _Keyword: 搜索关键字
        :type Keyword: str
        :param _Orientation: 构图方式，可选以下值：horizontal、vertical、square，分别代表以下含义：横图、竖图、方图
        :type Orientation: str
        :param _ImageSenseType: 图片类型，可选以下值：照片、插画
        :type ImageSenseType: str
        :param _LayeredGalleryIds: 分层图库id数组，可选以下数值：1(基础)，2(精选)，3(高级)
        :type LayeredGalleryIds: list of int
        """
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Orientation = None
        self._ImageSenseType = None
        self._LayeredGalleryIds = None

    @property
    def Offset(self):
        """页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        """搜索关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Orientation(self):
        """构图方式，可选以下值：horizontal、vertical、square，分别代表以下含义：横图、竖图、方图
        :rtype: str
        """
        return self._Orientation

    @Orientation.setter
    def Orientation(self, Orientation):
        self._Orientation = Orientation

    @property
    def ImageSenseType(self):
        """图片类型，可选以下值：照片、插画
        :rtype: str
        """
        return self._ImageSenseType

    @ImageSenseType.setter
    def ImageSenseType(self, ImageSenseType):
        self._ImageSenseType = ImageSenseType

    @property
    def LayeredGalleryIds(self):
        """分层图库id数组，可选以下数值：1(基础)，2(精选)，3(高级)
        :rtype: list of int
        """
        return self._LayeredGalleryIds

    @LayeredGalleryIds.setter
    def LayeredGalleryIds(self, LayeredGalleryIds):
        self._LayeredGalleryIds = LayeredGalleryIds


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Orientation = params.get("Orientation")
        self._ImageSenseType = params.get("ImageSenseType")
        self._LayeredGalleryIds = params.get("LayeredGalleryIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页偏移量
        :type Offset: int
        :param _Limit: 页大小
        :type Limit: int
        :param _Total: 总条数
        :type Total: int
        :param _HaveMore: 是否有下一页
        :type HaveMore: bool
        :param _Items: 图片信息数组
        :type Items: list of ImageItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Offset = None
        self._Limit = None
        self._Total = None
        self._HaveMore = None
        self._Items = None
        self._RequestId = None

    @property
    def Offset(self):
        """页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def HaveMore(self):
        """是否有下一页
        :rtype: bool
        """
        return self._HaveMore

    @HaveMore.setter
    def HaveMore(self, HaveMore):
        self._HaveMore = HaveMore

    @property
    def Items(self):
        """图片信息数组
        :rtype: list of ImageItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Total = params.get("Total")
        self._HaveMore = params.get("HaveMore")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ImageItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadInfo(AbstractModel):
    """图片下载信息

    """

    def __init__(self):
        r"""
        :param _ImageInfo: 图片基础信息
        :type ImageInfo: :class:`tencentcloud.ape.v20200513.models.ImageInfo`
        :param _ImageUrl: 图片原图URL
        :type ImageUrl: str
        :param _ImageThumbUrl: 图片缩略图URL
        :type ImageThumbUrl: str
        :param _OrderId: 订单Id
        :type OrderId: str
        :param _OrderCreateTime: 订单创建时间
        :type OrderCreateTime: str
        :param _DownloadId: 下载Id
        :type DownloadId: str
        :param _DownloadTime: 下载时间
        :type DownloadTime: str
        :param _ConsumeType: 图片购买类型，单张/会员
        :type ConsumeType: int
        :param _FirstDownload: 是否首次下载
        :type FirstDownload: bool
        """
        self._ImageInfo = None
        self._ImageUrl = None
        self._ImageThumbUrl = None
        self._OrderId = None
        self._OrderCreateTime = None
        self._DownloadId = None
        self._DownloadTime = None
        self._ConsumeType = None
        self._FirstDownload = None

    @property
    def ImageInfo(self):
        """图片基础信息
        :rtype: :class:`tencentcloud.ape.v20200513.models.ImageInfo`
        """
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def ImageUrl(self):
        """图片原图URL
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageThumbUrl(self):
        """图片缩略图URL
        :rtype: str
        """
        return self._ImageThumbUrl

    @ImageThumbUrl.setter
    def ImageThumbUrl(self, ImageThumbUrl):
        self._ImageThumbUrl = ImageThumbUrl

    @property
    def OrderId(self):
        """订单Id
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def OrderCreateTime(self):
        """订单创建时间
        :rtype: str
        """
        return self._OrderCreateTime

    @OrderCreateTime.setter
    def OrderCreateTime(self, OrderCreateTime):
        self._OrderCreateTime = OrderCreateTime

    @property
    def DownloadId(self):
        """下载Id
        :rtype: str
        """
        return self._DownloadId

    @DownloadId.setter
    def DownloadId(self, DownloadId):
        self._DownloadId = DownloadId

    @property
    def DownloadTime(self):
        """下载时间
        :rtype: str
        """
        return self._DownloadTime

    @DownloadTime.setter
    def DownloadTime(self, DownloadTime):
        self._DownloadTime = DownloadTime

    @property
    def ConsumeType(self):
        """图片购买类型，单张/会员
        :rtype: int
        """
        return self._ConsumeType

    @ConsumeType.setter
    def ConsumeType(self, ConsumeType):
        self._ConsumeType = ConsumeType

    @property
    def FirstDownload(self):
        """是否首次下载
        :rtype: bool
        """
        return self._FirstDownload

    @FirstDownload.setter
    def FirstDownload(self, FirstDownload):
        self._FirstDownload = FirstDownload


    def _deserialize(self, params):
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._ImageUrl = params.get("ImageUrl")
        self._ImageThumbUrl = params.get("ImageThumbUrl")
        self._OrderId = params.get("OrderId")
        self._OrderCreateTime = params.get("OrderCreateTime")
        self._DownloadId = params.get("DownloadId")
        self._DownloadTime = params.get("DownloadTime")
        self._ConsumeType = params.get("ConsumeType")
        self._FirstDownload = params.get("FirstDownload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """图片基础信息

    """

    def __init__(self):
        r"""
        :param _ImageId: 图片Id
        :type ImageId: int
        :param _LicenseScopeId: 授权场景Id
        :type LicenseScopeId: int
        :param _DimensionsNameId: 尺寸名称Id
        :type DimensionsNameId: int
        :param _UserId: 平台用户标识
        :type UserId: str
        :param _DownloadPrice: 平台用户下载图片购买的价格(单位:分)
        :type DownloadPrice: int
        :param _DownloadType: 下载类型。匹配集合中的任意元素：
<li>Single: 单张购买下载</li>
<li>BasicEnterpriseMember: 企业基础会员下载</li>
<li>AdvancedEnterpriseMember: 企业高级会员下载</li>
<li>DistinguishedEnterpriseMember: 企业尊享会员下载</li>
        :type DownloadType: str
        """
        self._ImageId = None
        self._LicenseScopeId = None
        self._DimensionsNameId = None
        self._UserId = None
        self._DownloadPrice = None
        self._DownloadType = None

    @property
    def ImageId(self):
        """图片Id
        :rtype: int
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LicenseScopeId(self):
        """授权场景Id
        :rtype: int
        """
        return self._LicenseScopeId

    @LicenseScopeId.setter
    def LicenseScopeId(self, LicenseScopeId):
        self._LicenseScopeId = LicenseScopeId

    @property
    def DimensionsNameId(self):
        """尺寸名称Id
        :rtype: int
        """
        return self._DimensionsNameId

    @DimensionsNameId.setter
    def DimensionsNameId(self, DimensionsNameId):
        self._DimensionsNameId = DimensionsNameId

    @property
    def UserId(self):
        """平台用户标识
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DownloadPrice(self):
        """平台用户下载图片购买的价格(单位:分)
        :rtype: int
        """
        return self._DownloadPrice

    @DownloadPrice.setter
    def DownloadPrice(self, DownloadPrice):
        self._DownloadPrice = DownloadPrice

    @property
    def DownloadType(self):
        """下载类型。匹配集合中的任意元素：
<li>Single: 单张购买下载</li>
<li>BasicEnterpriseMember: 企业基础会员下载</li>
<li>AdvancedEnterpriseMember: 企业高级会员下载</li>
<li>DistinguishedEnterpriseMember: 企业尊享会员下载</li>
        :rtype: str
        """
        return self._DownloadType

    @DownloadType.setter
    def DownloadType(self, DownloadType):
        self._DownloadType = DownloadType


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._LicenseScopeId = params.get("LicenseScopeId")
        self._DimensionsNameId = params.get("DimensionsNameId")
        self._UserId = params.get("UserId")
        self._DownloadPrice = params.get("DownloadPrice")
        self._DownloadType = params.get("DownloadType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageItem(AbstractModel):
    """图片信息条目

    """

    def __init__(self):
        r"""
        :param _ImageId: 图片ID
        :type ImageId: int
        :param _Title: 图片标题
        :type Title: str
        :param _Description: 图片描述
        :type Description: str
        :param _PreviewUrl: 图片预览链接
        :type PreviewUrl: str
        :param _ThumbUrl: 图片缩略图
        :type ThumbUrl: str
        :param _Vendor: 图片供应商
        :type Vendor: str
        :param _Keywords: 图片关键词
        :type Keywords: str
        :param _Width: 宽
        :type Width: int
        :param _Height: 高
        :type Height: int
        """
        self._ImageId = None
        self._Title = None
        self._Description = None
        self._PreviewUrl = None
        self._ThumbUrl = None
        self._Vendor = None
        self._Keywords = None
        self._Width = None
        self._Height = None

    @property
    def ImageId(self):
        """图片ID
        :rtype: int
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Title(self):
        """图片标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        """图片描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PreviewUrl(self):
        """图片预览链接
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def ThumbUrl(self):
        """图片缩略图
        :rtype: str
        """
        return self._ThumbUrl

    @ThumbUrl.setter
    def ThumbUrl(self, ThumbUrl):
        self._ThumbUrl = ThumbUrl

    @property
    def Vendor(self):
        """图片供应商
        :rtype: str
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Keywords(self):
        """图片关键词
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Width(self):
        """宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """高
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        self._PreviewUrl = params.get("PreviewUrl")
        self._ThumbUrl = params.get("ThumbUrl")
        self._Vendor = params.get("Vendor")
        self._Keywords = params.get("Keywords")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageMarshal(AbstractModel):
    """图片售卖组合信息

    """

    def __init__(self):
        r"""
        :param _MarshalId: 售卖组合唯一标识
        :type MarshalId: int
        :param _Height: 图片高度
        :type Height: int
        :param _Width: 图片宽度
        :type Width: int
        :param _Size: 图片大小
        :type Size: int
        :param _Format: 图片格式
        :type Format: str
        :param _Price: 图片价格(单位:分)
        :type Price: int
        :param _LicenseScope: 授权范围
        :type LicenseScope: str
        :param _IsVip: 是否支持VIP购买
        :type IsVip: bool
        :param _LicenseScopeId: 授权范围id
        :type LicenseScopeId: int
        :param _DimensionsName: 尺寸
        :type DimensionsName: str
        :param _DimensionsNameId: 尺寸id
        :type DimensionsNameId: int
        """
        self._MarshalId = None
        self._Height = None
        self._Width = None
        self._Size = None
        self._Format = None
        self._Price = None
        self._LicenseScope = None
        self._IsVip = None
        self._LicenseScopeId = None
        self._DimensionsName = None
        self._DimensionsNameId = None

    @property
    def MarshalId(self):
        """售卖组合唯一标识
        :rtype: int
        """
        return self._MarshalId

    @MarshalId.setter
    def MarshalId(self, MarshalId):
        self._MarshalId = MarshalId

    @property
    def Height(self):
        """图片高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        """图片宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Size(self):
        """图片大小
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Format(self):
        """图片格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Price(self):
        """图片价格(单位:分)
        :rtype: int
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def LicenseScope(self):
        """授权范围
        :rtype: str
        """
        return self._LicenseScope

    @LicenseScope.setter
    def LicenseScope(self, LicenseScope):
        self._LicenseScope = LicenseScope

    @property
    def IsVip(self):
        """是否支持VIP购买
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def LicenseScopeId(self):
        """授权范围id
        :rtype: int
        """
        return self._LicenseScopeId

    @LicenseScopeId.setter
    def LicenseScopeId(self, LicenseScopeId):
        self._LicenseScopeId = LicenseScopeId

    @property
    def DimensionsName(self):
        """尺寸
        :rtype: str
        """
        return self._DimensionsName

    @DimensionsName.setter
    def DimensionsName(self, DimensionsName):
        self._DimensionsName = DimensionsName

    @property
    def DimensionsNameId(self):
        """尺寸id
        :rtype: int
        """
        return self._DimensionsNameId

    @DimensionsNameId.setter
    def DimensionsNameId(self, DimensionsNameId):
        self._DimensionsNameId = DimensionsNameId


    def _deserialize(self, params):
        self._MarshalId = params.get("MarshalId")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._Size = params.get("Size")
        self._Format = params.get("Format")
        self._Price = params.get("Price")
        self._LicenseScope = params.get("LicenseScope")
        self._IsVip = params.get("IsVip")
        self._LicenseScopeId = params.get("LicenseScopeId")
        self._DimensionsName = params.get("DimensionsName")
        self._DimensionsNameId = params.get("DimensionsNameId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        