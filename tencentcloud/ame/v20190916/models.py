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


class Album(AbstractModel):
    """Album

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Artist(AbstractModel):
    """Artist

    """

    def __init__(self):
        r"""
        :param ArtistName: 歌手名
        :type ArtistName: str
        """
        self.ArtistName = None


    def _deserialize(self, params):
        self.ArtistName = params.get("ArtistName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthInfo(AbstractModel):
    """AuthInfo集合

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKTVRobotRequest(AbstractModel):
    """CreateKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        :param JoinRoomInput: 进房参数。
        :type JoinRoomInput: :class:`tencentcloud.ame.v20190916.models.JoinRoomInput`
        """
        self.RTCSystem = None
        self.JoinRoomInput = None


    def _deserialize(self, params):
        self.RTCSystem = params.get("RTCSystem")
        if params.get("JoinRoomInput") is not None:
            self.JoinRoomInput = JoinRoomInput()
            self.JoinRoomInput._deserialize(params.get("JoinRoomInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKTVRobotResponse(AbstractModel):
    """CreateKTVRobot返回参数结构体

    """

    def __init__(self):
        r"""
        :param RobotId: 机器人Id。
        :type RobotId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RobotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RobotId = params.get("RobotId")
        self.RequestId = params.get("RequestId")


class DataInfo(AbstractModel):
    """数据信息

    """

    def __init__(self):
        r"""
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
        :param TagNames: 标签名称
        :type TagNames: list of str
        """
        self.Name = None
        self.Version = None
        self.Duration = None
        self.AuditionBegin = None
        self.AuditionEnd = None
        self.TagNames = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Duration = params.get("Duration")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")
        self.TagNames = params.get("TagNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthInfoRequest(AbstractModel):
    """DescribeAuthInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthInfoResponse(AbstractModel):
    """DescribeAuthInfo返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param AuthInfoId: 授权项目Id
        :type AuthInfoId: str
        """
        self.AuthInfoId = None


    def _deserialize(self, params):
        self.AuthInfoId = params.get("AuthInfoId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudMusicPurchasedResponse(AbstractModel):
    """DescribeCloudMusicPurchased返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param MusicId: 歌曲Id
        :type MusicId: str
        :param MusicType: 歌曲类型，可选值有：
<li>MP3-128K-FTW：含有水印的试听资源；</li>
<li>MP3-320K-FTD-P：320kbps歌曲热门片段；</li>
<li>MP3-320K-FTD：320kbps已核验歌曲完整资源。</li>
默认为：MP3-128K-FTW
        :type MusicType: str
        """
        self.MusicId = None
        self.MusicType = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.MusicType = params.get("MusicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudMusicResponse(AbstractModel):
    """DescribeCloudMusic返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param ItemIDs: 歌曲ID，目前暂不支持批量查询
        :type ItemIDs: str
        """
        self.ItemIDs = None


    def _deserialize(self, params):
        self.ItemIDs = params.get("ItemIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeItemByIdResponse(AbstractModel):
    """DescribeItemById返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeItemsResponse(AbstractModel):
    """DescribeItems返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeKTVMusicDetailRequest(AbstractModel):
    """DescribeKTVMusicDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param MusicId: 曲目 Id
        :type MusicId: str
        """
        self.MusicId = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMusicDetailResponse(AbstractModel):
    """DescribeKTVMusicDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param KTVMusicBaseInfo: 歌曲基础信息
        :type KTVMusicBaseInfo: :class:`tencentcloud.ame.v20190916.models.KTVMusicBaseInfo`
        :param PlayToken: 播放凭证
        :type PlayToken: str
        :param LyricsUrl: 歌词下载地址
        :type LyricsUrl: str
        :param DefinitionInfoSet: 歌曲规格信息列表
        :type DefinitionInfoSet: list of KTVMusicDefinitionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KTVMusicBaseInfo = None
        self.PlayToken = None
        self.LyricsUrl = None
        self.DefinitionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self.KTVMusicBaseInfo = KTVMusicBaseInfo()
            self.KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        self.PlayToken = params.get("PlayToken")
        self.LyricsUrl = params.get("LyricsUrl")
        if params.get("DefinitionInfoSet") is not None:
            self.DefinitionInfoSet = []
            for item in params.get("DefinitionInfoSet"):
                obj = KTVMusicDefinitionInfo()
                obj._deserialize(item)
                self.DefinitionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKTVPlaylistDetailRequest(AbstractModel):
    """DescribeKTVPlaylistDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlaylistId: 歌单Id
        :type PlaylistId: str
        :param Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Limit: int
        """
        self.PlaylistId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.PlaylistId = params.get("PlaylistId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVPlaylistDetailResponse(AbstractModel):
    """DescribeKTVPlaylistDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param KTVMusicInfoSet: 歌曲基础信息列表
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param PlaylistBaseInfo: 歌单基础信息
        :type PlaylistBaseInfo: :class:`tencentcloud.ame.v20190916.models.KTVPlaylistBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KTVMusicInfoSet = None
        self.PlaylistBaseInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KTVMusicInfoSet") is not None:
            self.KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self.KTVMusicInfoSet.append(obj)
        if params.get("PlaylistBaseInfo") is not None:
            self.PlaylistBaseInfo = KTVPlaylistBaseInfo()
            self.PlaylistBaseInfo._deserialize(params.get("PlaylistBaseInfo"))
        self.RequestId = params.get("RequestId")


class DescribeKTVPlaylistsRequest(AbstractModel):
    """DescribeKTVPlaylists请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVPlaylistsResponse(AbstractModel):
    """DescribeKTVPlaylists返回参数结构体

    """

    def __init__(self):
        r"""
        :param PlaylistBaseInfoSet: 推荐歌单列表
        :type PlaylistBaseInfoSet: list of KTVPlaylistBaseInfo
        :param TotalCount: 推荐歌单列表总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlaylistBaseInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlaylistBaseInfoSet") is not None:
            self.PlaylistBaseInfoSet = []
            for item in params.get("PlaylistBaseInfoSet"):
                obj = KTVPlaylistBaseInfo()
                obj._deserialize(item)
                self.PlaylistBaseInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeKTVRobotsRequest(AbstractModel):
    """DescribeKTVRobots请求参数结构体

    """

    def __init__(self):
        r"""
        :param RobotIds: 机器人Id列表。
        :type RobotIds: list of str
        :param Statuses: 机器人状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :type Statuses: list of str
        :param Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param Limit: 分页返回的起始偏移量，默认值：10。
        :type Limit: int
        """
        self.RobotIds = None
        self.Statuses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RobotIds = params.get("RobotIds")
        self.Statuses = params.get("Statuses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVRobotsResponse(AbstractModel):
    """DescribeKTVRobots返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 机器人总数。
        :type TotalCount: int
        :param KTVRobotInfoSet: 机器人信息集合。
        :type KTVRobotInfoSet: list of KTVRobotInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.KTVRobotInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KTVRobotInfoSet") is not None:
            self.KTVRobotInfoSet = []
            for item in params.get("KTVRobotInfoSet"):
                obj = KTVRobotInfo()
                obj._deserialize(item)
                self.KTVRobotInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLyricRequest(AbstractModel):
    """DescribeLyric请求参数结构体

    """

    def __init__(self):
        r"""
        :param ItemId: 歌曲ID
        :type ItemId: str
        :param SubItemType: 格式，可选项，可不填写，默认值为：LRC-LRC。
<li>LRC-LRC：歌词；</li>
<li>JSON-ST：波形图。</li>
        :type SubItemType: str
        """
        self.ItemId = None
        self.SubItemType = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.SubItemType = params.get("SubItemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLyricResponse(AbstractModel):
    """DescribeLyric返回参数结构体

    """

    def __init__(self):
        r"""
        :param Lyric: 歌词或者波形图详情
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
        r"""
        :param ItemId: 歌曲ID
        :type ItemId: str
        :param IdentityId: 在应用前端播放音乐C端用户的唯一标识。无需是账户信息，用户唯一标识即可。
        :type IdentityId: str
        :param SubItemType: MP3-320K-FTD-P  为获取320kbps歌曲热门片段。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMusicResponse(AbstractModel):
    """DescribeMusic返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeMusicSaleStatusRequest(AbstractModel):
    """DescribeMusicSaleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param MusicIds: 歌曲Id集合，可传单个，也可传多个，上线查询单次50个
        :type MusicIds: list of str
        :param PurchaseType: 查询哪个渠道的数据，1为曲库包，2为单曲
        :type PurchaseType: int
        """
        self.MusicIds = None
        self.PurchaseType = None


    def _deserialize(self, params):
        self.MusicIds = params.get("MusicIds")
        self.PurchaseType = params.get("PurchaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMusicSaleStatusResponse(AbstractModel):
    """DescribeMusicSaleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param MusicStatusSet: musicId对应歌曲状态
        :type MusicStatusSet: list of MusicStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MusicStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MusicStatusSet") is not None:
            self.MusicStatusSet = []
            for item in params.get("MusicStatusSet"):
                obj = MusicStatus()
                obj._deserialize(item)
                self.MusicStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePackageItemsRequest(AbstractModel):
    """DescribePackageItems请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackageItemsResponse(AbstractModel):
    """DescribePackageItems返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackagesResponse(AbstractModel):
    """DescribePackages返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePkgOfflineMusicRequest(AbstractModel):
    """DescribePkgOfflineMusic请求参数结构体

    """

    def __init__(self):
        r"""
        :param PackageOrderId: 订单id
        :type PackageOrderId: str
        :param Limit: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条(注：单次上限为100)。
        :type Limit: int
        :param Offset: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        """
        self.PackageOrderId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.PackageOrderId = params.get("PackageOrderId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePkgOfflineMusicResponse(AbstractModel):
    """DescribePkgOfflineMusic返回参数结构体

    """

    def __init__(self):
        r"""
        :param OfflineMusicSet: 曲库包中不可用歌曲信息
        :type OfflineMusicSet: list of OfflineMusicDetail
        :param TotalCount: 返回总量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OfflineMusicSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OfflineMusicSet") is not None:
            self.OfflineMusicSet = []
            for item in params.get("OfflineMusicSet"):
                obj = OfflineMusicDetail()
                obj._deserialize(item)
                self.OfflineMusicSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeStationsRequest(AbstractModel):
    """DescribeStations请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStationsResponse(AbstractModel):
    """DescribeStations返回参数结构体

    """

    def __init__(self):
        r"""
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


class DestroyKTVRobotRequest(AbstractModel):
    """DestroyKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param RobotId: 机器人Id。
        :type RobotId: str
        """
        self.RobotId = None


    def _deserialize(self, params):
        self.RobotId = params.get("RobotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyKTVRobotResponse(AbstractModel):
    """DestroyKTVRobot返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImagePath(AbstractModel):
    """图片路径

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Item(AbstractModel):
    """歌曲信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinRoomInput(AbstractModel):
    """直播进房输入参数

    """

    def __init__(self):
        r"""
        :param TRTCJoinRoomInput: TRTC进房参数
        :type TRTCJoinRoomInput: :class:`tencentcloud.ame.v20190916.models.TRTCJoinRoomInput`
        """
        self.TRTCJoinRoomInput = None


    def _deserialize(self, params):
        if params.get("TRTCJoinRoomInput") is not None:
            self.TRTCJoinRoomInput = TRTCJoinRoomInput()
            self.TRTCJoinRoomInput._deserialize(params.get("TRTCJoinRoomInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicBaseInfo(AbstractModel):
    """KTV 曲目基础信息

    """

    def __init__(self):
        r"""
        :param MusicId: 歌曲 Id
        :type MusicId: str
        :param Name: 歌曲名称
        :type Name: str
        :param SingerSet: 演唱者列表
        :type SingerSet: list of str
        :param LyricistSet: 作词者列表
        :type LyricistSet: list of str
        :param ComposerSet: 作曲者列表
        :type ComposerSet: list of str
        :param TagSet: 标签列表
        :type TagSet: list of str
        :param Duration: 歌曲时长
        :type Duration: int
        """
        self.MusicId = None
        self.Name = None
        self.SingerSet = None
        self.LyricistSet = None
        self.ComposerSet = None
        self.TagSet = None
        self.Duration = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.Name = params.get("Name")
        self.SingerSet = params.get("SingerSet")
        self.LyricistSet = params.get("LyricistSet")
        self.ComposerSet = params.get("ComposerSet")
        self.TagSet = params.get("TagSet")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicDefinitionInfo(AbstractModel):
    """直播互动歌曲规格信息。

    """

    def __init__(self):
        r"""
        :param Definition: 规格，取值有：
<li>audio/mi：低规格；</li>
<li>audio/lo：中规格；</li>
<li>audio/hi：高规格。</li>
        :type Definition: str
        :param Bitrate: 码率，单位为 bps。
        :type Bitrate: int
        :param Size: 文件大小，单位为字节。
        :type Size: int
        """
        self.Definition = None
        self.Bitrate = None
        self.Size = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVPlaylistBaseInfo(AbstractModel):
    """推荐歌单基础信息

    """

    def __init__(self):
        r"""
        :param PlaylistId: 歌单Id
        :type PlaylistId: str
        :param Title: 歌单标题
        :type Title: str
        :param Description: 歌单介绍
        :type Description: str
        :param MusicNum: 歌曲数量
        :type MusicNum: int
        """
        self.PlaylistId = None
        self.Title = None
        self.Description = None
        self.MusicNum = None


    def _deserialize(self, params):
        self.PlaylistId = params.get("PlaylistId")
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.MusicNum = params.get("MusicNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVRobotInfo(AbstractModel):
    """机器人信息

    """

    def __init__(self):
        r"""
        :param RobotId: 机器人Id。
        :type RobotId: str
        :param Status: 状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :type Status: str
        :param Playlists: 播放列表。
        :type Playlists: list of str
        :param CurIndex: 当前歌单索引位置。
        :type CurIndex: int
        :param Position: 播放进度，单位：毫秒。
        :type Position: int
        :param SetAudioParamInput: 音频参数
        :type SetAudioParamInput: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        :param JoinRoomInput: 进房信息
        :type JoinRoomInput: :class:`tencentcloud.ame.v20190916.models.JoinRoomInput`
        :param RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        """
        self.RobotId = None
        self.Status = None
        self.Playlists = None
        self.CurIndex = None
        self.Position = None
        self.SetAudioParamInput = None
        self.JoinRoomInput = None
        self.RTCSystem = None


    def _deserialize(self, params):
        self.RobotId = params.get("RobotId")
        self.Status = params.get("Status")
        self.Playlists = params.get("Playlists")
        self.CurIndex = params.get("CurIndex")
        self.Position = params.get("Position")
        if params.get("SetAudioParamInput") is not None:
            self.SetAudioParamInput = SetAudioParamCommandInput()
            self.SetAudioParamInput._deserialize(params.get("SetAudioParamInput"))
        if params.get("JoinRoomInput") is not None:
            self.JoinRoomInput = JoinRoomInput()
            self.JoinRoomInput._deserialize(params.get("JoinRoomInput"))
        self.RTCSystem = params.get("RTCSystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Lyric(AbstractModel):
    """歌词信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMusicOnShelvesRequest(AbstractModel):
    """ModifyMusicOnShelves请求参数结构体

    """

    def __init__(self):
        r"""
        :param MusicDetailInfos: 歌曲变更信息
        :type MusicDetailInfos: :class:`tencentcloud.ame.v20190916.models.MusicDetailInfo`
        :param AmeKey: ame对接资源方密钥
        :type AmeKey: str
        """
        self.MusicDetailInfos = None
        self.AmeKey = None


    def _deserialize(self, params):
        if params.get("MusicDetailInfos") is not None:
            self.MusicDetailInfos = MusicDetailInfo()
            self.MusicDetailInfos._deserialize(params.get("MusicDetailInfos"))
        self.AmeKey = params.get("AmeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMusicOnShelvesResponse(AbstractModel):
    """ModifyMusicOnShelves返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Music(AbstractModel):
    """音乐详情

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicDetailInfo(AbstractModel):
    """歌曲变更细节

    """

    def __init__(self):
        r"""
        :param MusicId: 资源方音乐Id
        :type MusicId: str
        :param AmeId: 资源方识别信息
        :type AmeId: str
        :param Tags: 分类标签
        :type Tags: list of str
        :param HitWords: 关键词
        :type HitWords: list of str
        :param Bpm: 节奏信息
        :type Bpm: int
        :param Score: 商业化权益
        :type Score: float
        :param Scene: 应用歌曲信息,1.图文/短视频,2.网络直播,3.网络电台FM,4.免费游戏,5.商业游戏,6.网店网站设计,7.广告营销,8.网络长视频
        :type Scene: list of str
        :param Region: 应用地域,1. 中国大陆,2. 中国含港澳台,3. 全球
        :type Region: list of str
        :param AuthPeriod: 授权时间,1. 1年, 5. 随片永久
        :type AuthPeriod: str
        :param Commercialization: 商业化授权，1. 支持商业化 ,2. 不支持商业化
        :type Commercialization: str
        :param Platform: 跨平台传播，1. 支持跨平台传播 ,2. 不支持跨平台传播
        :type Platform: str
        :param Channel: 传播渠道
        :type Channel: str
        """
        self.MusicId = None
        self.AmeId = None
        self.Tags = None
        self.HitWords = None
        self.Bpm = None
        self.Score = None
        self.Scene = None
        self.Region = None
        self.AuthPeriod = None
        self.Commercialization = None
        self.Platform = None
        self.Channel = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.AmeId = params.get("AmeId")
        self.Tags = params.get("Tags")
        self.HitWords = params.get("HitWords")
        self.Bpm = params.get("Bpm")
        self.Score = params.get("Score")
        self.Scene = params.get("Scene")
        self.Region = params.get("Region")
        self.AuthPeriod = params.get("AuthPeriod")
        self.Commercialization = params.get("Commercialization")
        self.Platform = params.get("Platform")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicOpenDetail(AbstractModel):
    """对外开放信息

    """

    def __init__(self):
        r"""
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
        :param WaveformUrl: 波形图url
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveformUrl: str
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
        self.WaveformUrl = None


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
        self.WaveformUrl = params.get("WaveformUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicStatus(AbstractModel):
    """返回单曲页面歌曲是否在售状态

    """

    def __init__(self):
        r"""
        :param MusicId: 歌曲Id
        :type MusicId: str
        :param SaleStatus: 在售状态,0为在售，1为临时下架，2为永久下架
        :type SaleStatus: int
        """
        self.MusicId = None
        self.SaleStatus = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.SaleStatus = params.get("SaleStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineMusicDetail(AbstractModel):
    """曲库包已下架歌曲详细信息

    """

    def __init__(self):
        r"""
        :param ItemId: 歌曲Id
        :type ItemId: str
        :param MusicName: 歌曲名称
        :type MusicName: str
        :param OffRemark: 不可用原因
        :type OffRemark: str
        :param OffTime: 不可用时间
        :type OffTime: str
        """
        self.ItemId = None
        self.MusicName = None
        self.OffRemark = None
        self.OffTime = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.MusicName = params.get("MusicName")
        self.OffRemark = params.get("OffRemark")
        self.OffTime = params.get("OffTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Package(AbstractModel):
    """曲库包信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageItem(AbstractModel):
    """曲库包歌曲信息

    """

    def __init__(self):
        r"""
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
        :param Tags: 标签数组
        :type Tags: list of str
        """
        self.OrderId = None
        self.TrackName = None
        self.ItemID = None
        self.Img = None
        self.ArtistName = None
        self.Duration = None
        self.AuthorizedArea = None
        self.Tags = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.TrackName = params.get("TrackName")
        self.ItemID = params.get("ItemID")
        self.Img = params.get("Img")
        self.ArtistName = params.get("ArtistName")
        self.Duration = params.get("Duration")
        self.AuthorizedArea = params.get("AuthorizedArea")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayCommandInput(AbstractModel):
    """播放指令输入参数

    """

    def __init__(self):
        r"""
        :param Index: 歌曲位置索引。
        :type Index: int
        """
        self.Index = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMusicOnTheShelvesRequest(AbstractModel):
    """PutMusicOnTheShelves请求参数结构体

    """

    def __init__(self):
        r"""
        :param MusicIds: 资源方歌曲Id
        :type MusicIds: list of str
        """
        self.MusicIds = None


    def _deserialize(self, params):
        self.MusicIds = params.get("MusicIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMusicOnTheShelvesResponse(AbstractModel):
    """PutMusicOnTheShelves返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessNum: 操作成功数量
        :type SuccessNum: int
        :param FailedNum: 操作失败数量
        :type FailedNum: int
        :param FailedMusicIds: 失败歌曲Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMusicIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessNum = None
        self.FailedNum = None
        self.FailedMusicIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessNum = params.get("SuccessNum")
        self.FailedNum = params.get("FailedNum")
        self.FailedMusicIds = params.get("FailedMusicIds")
        self.RequestId = params.get("RequestId")


class ReportDataRequest(AbstractModel):
    """ReportData请求参数结构体

    """

    def __init__(self):
        r"""
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
https://github.com/tencentyun/ame-documents
        :type ReportData: str
        """
        self.ReportData = None


    def _deserialize(self, params):
        self.ReportData = params.get("ReportData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportDataResponse(AbstractModel):
    """ReportData返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchKTVMusicsRequest(AbstractModel):
    """SearchKTVMusics请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyWord: 搜索关键词
        :type KeyWord: str
        :param Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000。取值范围：小于5000
        :type Offset: int
        :param Limit: 分页返回的起始偏移量，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000。
        :type Limit: int
        """
        self.KeyWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.KeyWord = params.get("KeyWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKTVMusicsResponse(AbstractModel):
    """SearchKTVMusics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param KTVMusicInfoSet: KTV 曲目列表
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.KTVMusicInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KTVMusicInfoSet") is not None:
            self.KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self.KTVMusicInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SeekCommandInput(AbstractModel):
    """调整播放进度指令参数

    """

    def __init__(self):
        r"""
        :param Position: 播放位置，单位：毫秒。
        :type Position: int
        """
        self.Position = None


    def _deserialize(self, params):
        self.Position = params.get("Position")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageCommandInput(AbstractModel):
    """发送自定义信息指令参数

    """

    def __init__(self):
        r"""
        :param Message: 自定义消息，json格式字符串。
        :type Message: str
        :param Repeat: 消息重复次数，默认为 1。
        :type Repeat: int
        """
        self.Message = None
        self.Repeat = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Repeat = params.get("Repeat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAudioParamCommandInput(AbstractModel):
    """音频参数信息

    """

    def __init__(self):
        r"""
        :param Definition: 规格，取值有：
<li>audio/mi：低规格</li>
<li>audio/lo：中规格</li>
<li>audio/hi：高规格</li>
        :type Definition: str
        :param Type: 音频类型，取值有：
<li>Original：原唱</li>
<li>Accompaniment：伴奏</li>
        :type Type: str
        """
        self.Definition = None
        self.Type = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPlaylistCommandInput(AbstractModel):
    """设置播放列表指令参数

    """

    def __init__(self):
        r"""
        :param Type: 变更类型，取值有：
<li>Add：添加</li>
<li>Delete：删除</li>
        :type Type: str
        :param Index: 歌单索引位置，
当 Type 取 Add 时，-1表示添加在列表最后位置，大于-1表示要添加的位置；
当 Type 取 Delete 时，表示要删除的位置。
        :type Index: int
        :param MusicIds: 歌曲 ID 列表，当 Type 取 Add 时，必填。
        :type MusicIds: list of str
        """
        self.Type = None
        self.Index = None
        self.MusicIds = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Index = params.get("Index")
        self.MusicIds = params.get("MusicIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Station(AbstractModel):
    """分类内容

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncKTVRobotCommandRequest(AbstractModel):
    """SyncKTVRobotCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param RobotId: 机器人Id。
        :type RobotId: str
        :param Command: 指令，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>SwitchPrevious：上一首</li>
<li>SwitchNext：下一首</li>
<li>Seek：调整播放进度</li>
<li>SetPlaylist：歌单变更</li>
<li>SetAudioParam：音频参数变更</li>
<li>SendMessage：发送自定义消息</li>
        :type Command: str
        :param PlayCommandInput: 播放参数。
        :type PlayCommandInput: :class:`tencentcloud.ame.v20190916.models.PlayCommandInput`
        :param SetPlaylistCommandInput: 播放列表变更信息，当Command取SetPlaylist时，必填。
        :type SetPlaylistCommandInput: :class:`tencentcloud.ame.v20190916.models.SetPlaylistCommandInput`
        :param SeekCommandInput: 播放进度，当Command取Seek时，必填。
        :type SeekCommandInput: :class:`tencentcloud.ame.v20190916.models.SeekCommandInput`
        :param SetAudioParamCommandInput: 音频参数，当Command取SetAudioParam时，必填。
        :type SetAudioParamCommandInput: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        :param SendMessageCommandInput: 自定义消息，当Command取SendMessage时，必填。
        :type SendMessageCommandInput: :class:`tencentcloud.ame.v20190916.models.SendMessageCommandInput`
        """
        self.RobotId = None
        self.Command = None
        self.PlayCommandInput = None
        self.SetPlaylistCommandInput = None
        self.SeekCommandInput = None
        self.SetAudioParamCommandInput = None
        self.SendMessageCommandInput = None


    def _deserialize(self, params):
        self.RobotId = params.get("RobotId")
        self.Command = params.get("Command")
        if params.get("PlayCommandInput") is not None:
            self.PlayCommandInput = PlayCommandInput()
            self.PlayCommandInput._deserialize(params.get("PlayCommandInput"))
        if params.get("SetPlaylistCommandInput") is not None:
            self.SetPlaylistCommandInput = SetPlaylistCommandInput()
            self.SetPlaylistCommandInput._deserialize(params.get("SetPlaylistCommandInput"))
        if params.get("SeekCommandInput") is not None:
            self.SeekCommandInput = SeekCommandInput()
            self.SeekCommandInput._deserialize(params.get("SeekCommandInput"))
        if params.get("SetAudioParamCommandInput") is not None:
            self.SetAudioParamCommandInput = SetAudioParamCommandInput()
            self.SetAudioParamCommandInput._deserialize(params.get("SetAudioParamCommandInput"))
        if params.get("SendMessageCommandInput") is not None:
            self.SendMessageCommandInput = SendMessageCommandInput()
            self.SendMessageCommandInput._deserialize(params.get("SendMessageCommandInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncKTVRobotCommandResponse(AbstractModel):
    """SyncKTVRobotCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TRTCJoinRoomInput(AbstractModel):
    """TRTC推流进房信息

    """

    def __init__(self):
        r"""
        :param Sign: 签名。
        :type Sign: str
        :param RoomId: 房间号。
        :type RoomId: str
        :param SdkAppId: 推流应用ID。
        :type SdkAppId: str
        :param UserId: 用户唯一标识。
        :type UserId: str
        """
        self.Sign = None
        self.RoomId = None
        self.SdkAppId = None
        self.UserId = None


    def _deserialize(self, params):
        self.Sign = params.get("Sign")
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelves(AbstractModel):
    """下架歌曲复合结构

    """

    def __init__(self):
        r"""
        :param MusicIds: 资源方对应音乐Id
        :type MusicIds: str
        :param SaleStatus: 当曲目临时下架时：已订购客户无影响，无需消息通知。当曲目封杀下架后，推送消息至已订购老客户，枚举值，判断是否上/下架
在售状态，0在售，1临时下架，2永久下架
        :type SaleStatus: str
        """
        self.MusicIds = None
        self.SaleStatus = None


    def _deserialize(self, params):
        self.MusicIds = params.get("MusicIds")
        self.SaleStatus = params.get("SaleStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelvesRequest(AbstractModel):
    """TakeMusicOffShelves请求参数结构体

    """

    def __init__(self):
        r"""
        :param TakeMusicOffShelves: 资源方下架必传结构
        :type TakeMusicOffShelves: list of TakeMusicOffShelves
        """
        self.TakeMusicOffShelves = None


    def _deserialize(self, params):
        if params.get("TakeMusicOffShelves") is not None:
            self.TakeMusicOffShelves = []
            for item in params.get("TakeMusicOffShelves"):
                obj = TakeMusicOffShelves()
                obj._deserialize(item)
                self.TakeMusicOffShelves.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelvesResponse(AbstractModel):
    """TakeMusicOffShelves返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessNum: 返回成功数量
        :type SuccessNum: int
        :param FailedNum: 返回失败数量
        :type FailedNum: int
        :param FailedMusicIds: 返回失败歌曲musicId
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMusicIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessNum = None
        self.FailedNum = None
        self.FailedMusicIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessNum = params.get("SuccessNum")
        self.FailedNum = params.get("FailedNum")
        self.FailedMusicIds = params.get("FailedMusicIds")
        self.RequestId = params.get("RequestId")


class UseRange(AbstractModel):
    """曲库包用途信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        