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


class Album(AbstractModel):
    """Album

    """

    def __init__(self):
        """
        :param AlbumName: 专辑名
        :type AlbumName: str
        :param ImagePathMap: 专辑图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePathMap: list of ImagePath
        """
        self.AlbumName = None
        self.ImagePathMap = None


    def _deserialize(self, params):
        self.AlbumName = params.get("AlbumName")
        if params.get("ImagePathMap") is not None:
            self.ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self.ImagePathMap.append(obj)


class Artist(AbstractModel):
    """Artist

    """

    def __init__(self):
        """
        :param ArtistName: 歌手名
        :type ArtistName: str
        """
        self.ArtistName = None


    def _deserialize(self, params):
        self.ArtistName = params.get("ArtistName")


class AuthInfo(AbstractModel):
    """AuthInfo集合

    """

    def __init__(self):
        """
        :param SubjectName: 主体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectName: str
        :param ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param AppScene: 应用场景
        :type AppScene: int
        :param AppRegion: 应用地域
        :type AppRegion: int
        :param AuthPeriod: 授权时间
        :type AuthPeriod: int
        :param Commercialization: 是否可商业化
        :type Commercialization: int
        :param Platform: 是否可跨平台
        :type Platform: int
        :param Id: 加密后Id
        :type Id: str
        """
        self.SubjectName = None
        self.ProjectName = None
        self.AppScene = None
        self.AppRegion = None
        self.AuthPeriod = None
        self.Commercialization = None
        self.Platform = None
        self.Id = None


    def _deserialize(self, params):
        self.SubjectName = params.get("SubjectName")
        self.ProjectName = params.get("ProjectName")
        self.AppScene = params.get("AppScene")
        self.AppRegion = params.get("AppRegion")
        self.AuthPeriod = params.get("AuthPeriod")
        self.Commercialization = params.get("Commercialization")
        self.Platform = params.get("Platform")
        self.Id = params.get("Id")


class DataInfo(AbstractModel):
    """数据信息

    """

    def __init__(self):
        """
        :param Name: Song Name
        :type Name: str
        :param Version: 歌曲版本
        :type Version: str
        :param Duration: 歌曲总时长（非试听时长）
        :type Duration: str
        :param AuditionBegin: 试听开始时间
        :type AuditionBegin: int
        :param AuditionEnd: 试听结束时间
        :type AuditionEnd: int
        """
        self.Name = None
        self.Version = None
        self.Duration = None
        self.AuditionBegin = None
        self.AuditionEnd = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Duration = params.get("Duration")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")


class DescribeAuthInfoRequest(AbstractModel):
    """DescribeAuthInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量：Offset=Offset+Limit
        :type Offset: int
        :param Limit: 数据条数
        :type Limit: int
        :param Key: 搜索关键字
        :type Key: str
        """
        self.Offset = None
        self.Limit = None
        self.Key = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Key = params.get("Key")


class DescribeAuthInfoResponse(AbstractModel):
    """DescribeAuthInfo返回参数结构体

    """

    def __init__(self):
        """
        :param AuthInfo: 授权项目列表
        :type AuthInfo: list of AuthInfo
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuthInfo = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuthInfo") is not None:
            self.AuthInfo = []
            for item in params.get("AuthInfo"):
                obj = AuthInfo()
                obj._deserialize(item)
                self.AuthInfo.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCloudMusicPurchasedRequest(AbstractModel):
    """DescribeCloudMusicPurchased请求参数结构体

    """

    def __init__(self):
        """
        :param AuthInfoId: 授权项目Id
        :type AuthInfoId: str
        """
        self.AuthInfoId = None


    def _deserialize(self, params):
        self.AuthInfoId = params.get("AuthInfoId")


class DescribeCloudMusicPurchasedResponse(AbstractModel):
    """DescribeCloudMusicPurchased返回参数结构体

    """

    def __init__(self):
        """
        :param MusicOpenDetail: 云音乐列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicOpenDetail: list of MusicOpenDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MusicOpenDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MusicOpenDetail") is not None:
            self.MusicOpenDetail = []
            for item in params.get("MusicOpenDetail"):
                obj = MusicOpenDetail()
                obj._deserialize(item)
                self.MusicOpenDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudMusicRequest(AbstractModel):
    """DescribeCloudMusic请求参数结构体

    """

    def __init__(self):
        """
        :param MusicId: 歌曲Id
        :type MusicId: str
        :param MusicType: 歌曲类型，请填写：MP3-320K-FTD
        :type MusicType: str
        """
        self.MusicId = None
        self.MusicType = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.MusicType = params.get("MusicType")


class DescribeCloudMusicResponse(AbstractModel):
    """DescribeCloudMusic返回参数结构体

    """

    def __init__(self):
        """
        :param MusicId: 歌曲Id
        :type MusicId: str
        :param MusicName: 歌曲名称
        :type MusicName: str
        :param Duration: 歌曲时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param MusicUrl: 歌曲链接
        :type MusicUrl: str
        :param MusicImageUrl: 歌曲图片
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicImageUrl: str
        :param Singers: 歌手列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Singers: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MusicId = None
        self.MusicName = None
        self.Duration = None
        self.MusicUrl = None
        self.MusicImageUrl = None
        self.Singers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.MusicName = params.get("MusicName")
        self.Duration = params.get("Duration")
        self.MusicUrl = params.get("MusicUrl")
        self.MusicImageUrl = params.get("MusicImageUrl")
        self.Singers = params.get("Singers")
        self.RequestId = params.get("RequestId")


class DescribeItemByIdRequest(AbstractModel):
    """DescribeItemById请求参数结构体

    """

    def __init__(self):
        """
        :param ItemIDs: 歌曲ID，目前暂不支持批量查询
        :type ItemIDs: str
        """
        self.ItemIDs = None


    def _deserialize(self, params):
        self.ItemIDs = params.get("ItemIDs")


class DescribeItemByIdResponse(AbstractModel):
    """DescribeItemById返回参数结构体

    """

    def __init__(self):
        """
        :param Items: 歌曲信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeItemsRequest(AbstractModel):
    """DescribeItems请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: offset (Default = 0)，(当前页-1) * Limit
        :type Offset: int
        :param Limit: 条数，必须大于0，最大值为30
        :type Limit: int
        :param CategoryId: （电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。
        :type CategoryId: str
        :param CategoryCode: （电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。
        :type CategoryCode: str
        """
        self.Offset = None
        self.Limit = None
        self.CategoryId = None
        self.CategoryCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CategoryId = params.get("CategoryId")
        self.CategoryCode = params.get("CategoryCode")


class DescribeItemsResponse(AbstractModel):
    """DescribeItems返回参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移量
        :type Offset: int
        :param Size: 当前页歌曲数量
        :type Size: int
        :param Total: 总数据条数
        :type Total: int
        :param HaveMore: 剩余数量（total-offset-size），通过这个值判断是否
还有下一页
        :type HaveMore: int
        :param Items: Items 歌曲列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Offset = None
        self.Size = None
        self.Total = None
        self.HaveMore = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Size = params.get("Size")
        self.Total = params.get("Total")
        self.HaveMore = params.get("HaveMore")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLyricRequest(AbstractModel):
    """DescribeLyric请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 歌曲ID
        :type ItemId: str
        :param SubItemType: 歌词格式，可选项，可不填写，目前填写只能填LRC-LRC。该字段为预留的扩展字段。后续如果不填，会返回歌曲的所有格式的歌词。如果填写某个正确的格式，则只返回该格式的歌词。
        :type SubItemType: str
        """
        self.ItemId = None
        self.SubItemType = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.SubItemType = params.get("SubItemType")


class DescribeLyricResponse(AbstractModel):
    """DescribeLyric返回参数结构体

    """

    def __init__(self):
        """
        :param Lyric: 歌词详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Lyric: :class:`tencentcloud.ame.v20190916.models.Lyric`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Lyric = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Lyric") is not None:
            self.Lyric = Lyric()
            self.Lyric._deserialize(params.get("Lyric"))
        self.RequestId = params.get("RequestId")


class DescribeMusicRequest(AbstractModel):
    """DescribeMusic请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 歌曲ID
        :type ItemId: str
        :param IdentityId: 在应用前端播放音乐C端用户的唯一标识。无需是账户信息，用户唯一标识即可。
        :type IdentityId: str
        :param SubItemType: MP3-64K-FTD-P  为获取64kbps歌曲热门片段。
MP3-320K-FTD 为获取320kbps已核验歌曲完整资源。
        :type SubItemType: str
        :param Ssl: CDN URL Protocol:HTTP or HTTPS/SSL
Values:Y , N(default)
        :type Ssl: str
        """
        self.ItemId = None
        self.IdentityId = None
        self.SubItemType = None
        self.Ssl = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.IdentityId = params.get("IdentityId")
        self.SubItemType = params.get("SubItemType")
        self.Ssl = params.get("Ssl")


class DescribeMusicResponse(AbstractModel):
    """DescribeMusic返回参数结构体

    """

    def __init__(self):
        """
        :param Music: 音乐相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Music: :class:`tencentcloud.ame.v20190916.models.Music`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Music = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Music") is not None:
            self.Music = Music()
            self.Music._deserialize(params.get("Music"))
        self.RequestId = params.get("RequestId")


class DescribePackageItemsRequest(AbstractModel):
    """DescribePackageItems请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单id，从获取已购曲库包列表中获取
        :type OrderId: str
        :param Offset: 默认0，Offset=Offset+Length
        :type Offset: int
        :param Length: 默认20
        :type Length: int
        """
        self.OrderId = None
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class DescribePackageItemsResponse(AbstractModel):
    """DescribePackageItems返回参数结构体

    """

    def __init__(self):
        """
        :param PackageItems: 已核销歌曲信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageItems: list of PackageItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PackageItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PackageItems") is not None:
            self.PackageItems = []
            for item in params.get("PackageItems"):
                obj = PackageItem()
                obj._deserialize(item)
                self.PackageItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePackagesRequest(AbstractModel):
    """DescribePackages请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 默认0，Offset=Offset+Length
        :type Offset: int
        :param Length: 默认20
        :type Length: int
        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class DescribePackagesResponse(AbstractModel):
    """DescribePackages返回参数结构体

    """

    def __init__(self):
        """
        :param Packages: 已购曲库包列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Packages: list of Package
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Packages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Packages") is not None:
            self.Packages = []
            for item in params.get("Packages"):
                obj = Package()
                obj._deserialize(item)
                self.Packages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStationsRequest(AbstractModel):
    """DescribeStations请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 条数，必须大于0
        :type Limit: int
        :param Offset: offset (Default = 0)，Offset=Offset+Limit
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeStationsResponse(AbstractModel):
    """DescribeStations返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总数量
        :type Total: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param Size: 当前页station数量
        :type Size: int
        :param HaveMore: 剩余数量（total-offset-size），通过这个值判断是否还有下一页
        :type HaveMore: int
        :param Stations: Stations 素材库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Stations: list of Station
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Offset = None
        self.Size = None
        self.HaveMore = None
        self.Stations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Offset = params.get("Offset")
        self.Size = params.get("Size")
        self.HaveMore = params.get("HaveMore")
        if params.get("Stations") is not None:
            self.Stations = []
            for item in params.get("Stations"):
                obj = Station()
                obj._deserialize(item)
                self.Stations.append(obj)
        self.RequestId = params.get("RequestId")


class ImagePath(AbstractModel):
    """图片路径

    """

    def __init__(self):
        """
        :param Key: station图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: station图片地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class Item(AbstractModel):
    """歌曲信息

    """

    def __init__(self):
        """
        :param ItemID: Song ID
        :type ItemID: str
        :param DataInfo: Song info
注意：此字段可能返回 null，表示取不到有效值。
        :type DataInfo: :class:`tencentcloud.ame.v20190916.models.DataInfo`
        :param Album: 专辑信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Album: :class:`tencentcloud.ame.v20190916.models.Album`
        :param Artists: 多个歌手集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Artists: list of Artist
        :param Status: 歌曲状态，1:添加进购物车；2:核销进曲库包
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.ItemID = None
        self.DataInfo = None
        self.Album = None
        self.Artists = None
        self.Status = None


    def _deserialize(self, params):
        self.ItemID = params.get("ItemID")
        if params.get("DataInfo") is not None:
            self.DataInfo = DataInfo()
            self.DataInfo._deserialize(params.get("DataInfo"))
        if params.get("Album") is not None:
            self.Album = Album()
            self.Album._deserialize(params.get("Album"))
        if params.get("Artists") is not None:
            self.Artists = []
            for item in params.get("Artists"):
                obj = Artist()
                obj._deserialize(item)
                self.Artists.append(obj)
        self.Status = params.get("Status")


class Lyric(AbstractModel):
    """歌词信息

    """

    def __init__(self):
        """
        :param Url: 歌词cdn地址
        :type Url: str
        :param FileNameExt: 歌词后缀名
        :type FileNameExt: str
        :param SubItemType: 歌词类型
        :type SubItemType: str
        """
        self.Url = None
        self.FileNameExt = None
        self.SubItemType = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileNameExt = params.get("FileNameExt")
        self.SubItemType = params.get("SubItemType")


class Music(AbstractModel):
    """音乐详情

    """

    def __init__(self):
        """
        :param Url: 音乐播放链接相对路径，必须通过在正版曲库直通车控制台上登记的域名进行拼接。
        :type Url: str
        :param FileSize: 音频文件大小
        :type FileSize: int
        :param FileExtension: 音频文件类型
        :type FileExtension: str
        :param AuditionBegin: Song fragment start.试听片段开始时间，试听时长为auditionEnd-auditionBegin
Unit :ms
        :type AuditionBegin: int
        :param AuditionEnd: Song fragment end.试听片段结束时间, 试听时长为auditionEnd-auditionBegin
Unit :ms
        :type AuditionEnd: int
        :param FullUrl: 音乐播放链接全路径，前提是在正版曲库直通车控制台添加过域名，否则返回空字符。
如果添加过多个域名只返回第一个添加域名的播放全路径。
        :type FullUrl: str
        """
        self.Url = None
        self.FileSize = None
        self.FileExtension = None
        self.AuditionBegin = None
        self.AuditionEnd = None
        self.FullUrl = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileSize = params.get("FileSize")
        self.FileExtension = params.get("FileExtension")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")
        self.FullUrl = params.get("FullUrl")


class MusicOpenDetail(AbstractModel):
    """对外开放信息

    """

    def __init__(self):
        """
        :param MusicId: 音乐Id
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicId: str
        :param AlbumName: 专辑名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumName: str
        :param AlbumImageUrl: 专辑图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumImageUrl: str
        :param MusicName: 音乐名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicName: str
        :param MusicImageUrl: 音乐图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicImageUrl: str
        :param Singers: 歌手
注意：此字段可能返回 null，表示取不到有效值。
        :type Singers: list of str
        :param Duration: 播放时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param LyricUrl: 歌词url
注意：此字段可能返回 null，表示取不到有效值。
        :type LyricUrl: str
        """
        self.MusicId = None
        self.AlbumName = None
        self.AlbumImageUrl = None
        self.MusicName = None
        self.MusicImageUrl = None
        self.Singers = None
        self.Duration = None
        self.Tags = None
        self.LyricUrl = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.AlbumName = params.get("AlbumName")
        self.AlbumImageUrl = params.get("AlbumImageUrl")
        self.MusicName = params.get("MusicName")
        self.MusicImageUrl = params.get("MusicImageUrl")
        self.Singers = params.get("Singers")
        self.Duration = params.get("Duration")
        self.Tags = params.get("Tags")
        self.LyricUrl = params.get("LyricUrl")


class Package(AbstractModel):
    """曲库包信息

    """

    def __init__(self):
        """
        :param OrderId: 订单id
        :type OrderId: str
        :param Name: 曲库包名称
        :type Name: str
        :param AuthorizedArea: 授权地区-global: 全球  CN: 中国
        :type AuthorizedArea: str
        :param AuthorizedLimit: 授权次数
        :type AuthorizedLimit: int
        :param TermOfValidity: 套餐有效期，单位:天
        :type TermOfValidity: int
        :param Commercial: 0:不可商业化；1:可商业化
        :type Commercial: int
        :param PackagePrice: 套餐价格，单位：元
        :type PackagePrice: float
        :param EffectTime: 生效开始时间,格式yyyy-MM-dd HH:mm:ss
        :type EffectTime: str
        :param ExpireTime: 生效结束时间,格式yyyy-MM-dd HH:mm:ss
        :type ExpireTime: str
        :param UsedCount: 剩余授权次数
        :type UsedCount: int
        :param UseRanges: 曲库包用途信息
        :type UseRanges: list of UseRange
        """
        self.OrderId = None
        self.Name = None
        self.AuthorizedArea = None
        self.AuthorizedLimit = None
        self.TermOfValidity = None
        self.Commercial = None
        self.PackagePrice = None
        self.EffectTime = None
        self.ExpireTime = None
        self.UsedCount = None
        self.UseRanges = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Name = params.get("Name")
        self.AuthorizedArea = params.get("AuthorizedArea")
        self.AuthorizedLimit = params.get("AuthorizedLimit")
        self.TermOfValidity = params.get("TermOfValidity")
        self.Commercial = params.get("Commercial")
        self.PackagePrice = params.get("PackagePrice")
        self.EffectTime = params.get("EffectTime")
        self.ExpireTime = params.get("ExpireTime")
        self.UsedCount = params.get("UsedCount")
        if params.get("UseRanges") is not None:
            self.UseRanges = []
            for item in params.get("UseRanges"):
                obj = UseRange()
                obj._deserialize(item)
                self.UseRanges.append(obj)


class PackageItem(AbstractModel):
    """曲库包歌曲信息

    """

    def __init__(self):
        """
        :param OrderId: 订单id
        :type OrderId: str
        :param TrackName: 歌曲名
        :type TrackName: str
        :param ItemID: 歌曲ID
        :type ItemID: str
        :param Img: 专辑图片
        :type Img: str
        :param ArtistName: 歌手名
        :type ArtistName: str
        :param Duration: 歌曲时长
        :type Duration: str
        :param AuthorizedArea: 授权区域，global: 全球 CN: 中国
        :type AuthorizedArea: str
        """
        self.OrderId = None
        self.TrackName = None
        self.ItemID = None
        self.Img = None
        self.ArtistName = None
        self.Duration = None
        self.AuthorizedArea = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.TrackName = params.get("TrackName")
        self.ItemID = params.get("ItemID")
        self.Img = params.get("Img")
        self.ArtistName = params.get("ArtistName")
        self.Duration = params.get("Duration")
        self.AuthorizedArea = params.get("AuthorizedArea")


class ReportDataRequest(AbstractModel):
    """ReportData请求参数结构体

    """

    def __init__(self):
        """
        :param ReportData: 上报数据
注:reportData为客户端压缩后的上报数据进行16进制转换的字符串数据
压缩说明：
a) 上报的json格式字符串通过流的转换（ByteArrayInputStream, java.util.zip.GZIPOutputStream），获取到压缩后的字节数组。
b) 将压缩后的字节数组转成16进制字符串。

reportData由两部分数据组成：
1）report_type（上报类型）
2）data（歌曲上报数据）
不同的report_type对应的data数据结构不一样。

详细说明请参考文档reportdata.docx：
https://github.com/ame-demo/doc
        :type ReportData: str
        """
        self.ReportData = None


    def _deserialize(self, params):
        self.ReportData = params.get("ReportData")


class ReportDataResponse(AbstractModel):
    """ReportData返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Station(AbstractModel):
    """分类内容

    """

    def __init__(self):
        """
        :param CategoryID: StationID
        :type CategoryID: str
        :param CategoryCode: Station MCCode
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryCode: str
        :param Name: Category Name
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Rank: Station的排序值，供参考（返回结果已按其升序）
注意：此字段可能返回 null，表示取不到有效值。
        :type Rank: int
        :param ImagePathMap: station图片集合
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePathMap: list of ImagePath
        """
        self.CategoryID = None
        self.CategoryCode = None
        self.Name = None
        self.Rank = None
        self.ImagePathMap = None


    def _deserialize(self, params):
        self.CategoryID = params.get("CategoryID")
        self.CategoryCode = params.get("CategoryCode")
        self.Name = params.get("Name")
        self.Rank = params.get("Rank")
        if params.get("ImagePathMap") is not None:
            self.ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self.ImagePathMap.append(obj)


class UseRange(AbstractModel):
    """曲库包用途信息

    """

    def __init__(self):
        """
        :param UseRangeId: 用途id
        :type UseRangeId: int
        :param Name: 用途范围名称
        :type Name: str
        """
        self.UseRangeId = None
        self.Name = None


    def _deserialize(self, params):
        self.UseRangeId = params.get("UseRangeId")
        self.Name = params.get("Name")