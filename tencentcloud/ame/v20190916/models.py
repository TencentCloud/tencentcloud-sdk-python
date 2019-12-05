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


class DescribeItemsRequest(AbstractModel):
    """DescribeItems请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: offset (Default = 0)，(当前页-1) * Limit
        :type Offset: int
        :param Limit: 条数，必须大于0，最大值为30
        :type Limit: int
        :param CategoryId: （电台/歌单）ID，CategoryId和CategoryCode两个必传1个
        :type CategoryId: str
        :param CategoryCode: （电台/歌单）代码，CategoryId和CategoryCode两个必传1个
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
        :param IdentityId: User identity ID，用来唯一标识用户
        :type IdentityId: str
        :param SubItemType: 填 MP3-64K-FTD-P 获取歌曲热门片段
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


class DescribeStationsRequest(AbstractModel):
    """DescribeStations请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 条数，必须大于0
        :type Limit: int
        :param Offset: offset (Default = 0)，(当前页-1) * Limit
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
    """Item

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
        """
        self.ItemID = None
        self.DataInfo = None
        self.Album = None
        self.Artists = None


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
    """Music

    """

    def __init__(self):
        """
        :param Url: 音乐播放链接相对路径，必须通过在音乐版权助手上登记的域名进行拼接。
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
        """
        self.Url = None
        self.FileSize = None
        self.FileExtension = None
        self.AuditionBegin = None
        self.AuditionEnd = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileSize = params.get("FileSize")
        self.FileExtension = params.get("FileExtension")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")


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