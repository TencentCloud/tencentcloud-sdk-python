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


class BatchDescribeKTVMusicDetailsRequest(AbstractModel):
    """BatchDescribeKTVMusicDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param MusicIds: 歌曲 Id 列表。
        :type MusicIds: list of str
        """
        self.AppName = None
        self.UserId = None
        self.MusicIds = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.MusicIds = params.get("MusicIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeKTVMusicDetailsResponse(AbstractModel):
    """BatchDescribeKTVMusicDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param KTVMusicDetailInfoSet: 歌曲详细信息列表。
        :type KTVMusicDetailInfoSet: list of KTVMusicDetailInfo
        :param NotExistMusicIdSet: 不存在歌曲Id列表。
        :type NotExistMusicIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KTVMusicDetailInfoSet = None
        self.NotExistMusicIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KTVMusicDetailInfoSet") is not None:
            self.KTVMusicDetailInfoSet = []
            for item in params.get("KTVMusicDetailInfoSet"):
                obj = KTVMusicDetailInfo()
                obj._deserialize(item)
                self.KTVMusicDetailInfoSet.append(obj)
        self.NotExistMusicIdSet = params.get("NotExistMusicIdSet")
        self.RequestId = params.get("RequestId")


class ChorusClip(AbstractModel):
    """副歌片段信息。

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间，单位：毫秒。
        :type StartTime: int
        :param EndTime: 结束时间，单位：毫秒。
        :type EndTime: int
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVPlaylistDetailRequest(AbstractModel):
    """DescribeKTVPlaylistDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param PlaylistId: 歌单 Id。
        :type PlaylistId: str
        :param ScrollToken: 滚动标记。
        :type ScrollToken: str
        :param Limit: 返回条数，默认：20，最大：50。
        :type Limit: int
        :param RightFilters: 权益过滤，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightFilters: list of str
        """
        self.AppName = None
        self.UserId = None
        self.PlaylistId = None
        self.ScrollToken = None
        self.Limit = None
        self.RightFilters = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.PlaylistId = params.get("PlaylistId")
        self.ScrollToken = params.get("ScrollToken")
        self.Limit = params.get("Limit")
        self.RightFilters = params.get("RightFilters")
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
        :param KTVMusicInfoSet: 歌曲信息列表。
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param ScrollToken: 滚动标记，用于设置下次请求的 ScrollToken 参数。
        :type ScrollToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KTVMusicInfoSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KTVMusicInfoSet") is not None:
            self.KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self.KTVMusicInfoSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")


class DescribeKTVPlaylistsRequest(AbstractModel):
    """DescribeKTVPlaylists请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param Types: 类型列表，取值有：
<li>OfficialRec：官方推荐；</li>
<li>Customize：自定义。</li>
        :type Types: list of str
        """
        self.AppName = None
        self.UserId = None
        self.Types = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.Types = params.get("Types")
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
        :param PlaylistBaseInfoSet: 歌单基础信息。
        :type PlaylistBaseInfoSet: list of KTVPlaylistBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlaylistBaseInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlaylistBaseInfoSet") is not None:
            self.PlaylistBaseInfoSet = []
            for item in params.get("PlaylistBaseInfoSet"):
                obj = KTVPlaylistBaseInfo()
                obj._deserialize(item)
                self.PlaylistBaseInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKTVSuggestionsRequest(AbstractModel):
    """DescribeKTVSuggestions请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param KeyWord: 搜索词。
        :type KeyWord: str
        """
        self.AppName = None
        self.UserId = None
        self.KeyWord = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVSuggestionsResponse(AbstractModel):
    """DescribeKTVSuggestions返回参数结构体

    """

    def __init__(self):
        r"""
        :param KTVSuggestionInfoSet: 联想词信息列表。
        :type KTVSuggestionInfoSet: list of KTVSuggestionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KTVSuggestionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KTVSuggestionInfoSet") is not None:
            self.KTVSuggestionInfoSet = []
            for item in params.get("KTVSuggestionInfoSet"):
                obj = KTVSuggestionInfo()
                obj._deserialize(item)
                self.KTVSuggestionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class KTVMusicBaseInfo(AbstractModel):
    """歌曲基础信息。

    """

    def __init__(self):
        r"""
        :param MusicId: 歌曲Id。
        :type MusicId: str
        :param Name: 歌曲名称。
        :type Name: str
        :param SingerSet: 歌手名称。
        :type SingerSet: list of str
        :param Duration: 播放时长。
        :type Duration: int
        :param SingerImageUrl: 歌手图片链接。
        :type SingerImageUrl: str
        :param AlbumInfo: 专辑信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumInfo: :class:`tencentcloud.yinsuda.v20220527.models.MusicAlbumInfo`
        :param RightSet: 权益列表，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightSet: list of str
        :param RecommendType: 推荐类型，取值有：
<li>Featured：精选；</li>
<li>Other：其他。</li>
        :type RecommendType: str
        """
        self.MusicId = None
        self.Name = None
        self.SingerSet = None
        self.Duration = None
        self.SingerImageUrl = None
        self.AlbumInfo = None
        self.RightSet = None
        self.RecommendType = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.Name = params.get("Name")
        self.SingerSet = params.get("SingerSet")
        self.Duration = params.get("Duration")
        self.SingerImageUrl = params.get("SingerImageUrl")
        if params.get("AlbumInfo") is not None:
            self.AlbumInfo = MusicAlbumInfo()
            self.AlbumInfo._deserialize(params.get("AlbumInfo"))
        self.RightSet = params.get("RightSet")
        self.RecommendType = params.get("RecommendType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicDetailInfo(AbstractModel):
    """歌曲详细信息。

    """

    def __init__(self):
        r"""
        :param KTVMusicBaseInfo: 歌曲基础信息。
        :type KTVMusicBaseInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVMusicBaseInfo`
        :param PlayToken: 播放凭证。
        :type PlayToken: str
        :param LyricsUrl: 歌词下载链接。
        :type LyricsUrl: str
        :param MidiUrl: 音高数据下载链接。
        :type MidiUrl: str
        :param ChorusClipSet: 副歌片段信息。
        :type ChorusClipSet: list of ChorusClip
        :param PreludeInterval: 前奏间隔。
        :type PreludeInterval: int
        :param GenreSet: 歌曲流派列表。
        :type GenreSet: list of str
        """
        self.KTVMusicBaseInfo = None
        self.PlayToken = None
        self.LyricsUrl = None
        self.MidiUrl = None
        self.ChorusClipSet = None
        self.PreludeInterval = None
        self.GenreSet = None


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self.KTVMusicBaseInfo = KTVMusicBaseInfo()
            self.KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        self.PlayToken = params.get("PlayToken")
        self.LyricsUrl = params.get("LyricsUrl")
        self.MidiUrl = params.get("MidiUrl")
        if params.get("ChorusClipSet") is not None:
            self.ChorusClipSet = []
            for item in params.get("ChorusClipSet"):
                obj = ChorusClip()
                obj._deserialize(item)
                self.ChorusClipSet.append(obj)
        self.PreludeInterval = params.get("PreludeInterval")
        self.GenreSet = params.get("GenreSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVPlaylistBaseInfo(AbstractModel):
    """歌单基础信息。

    """

    def __init__(self):
        r"""
        :param PlaylistId: 歌单Id。
        :type PlaylistId: str
        :param Title: 歌单标题。
        :type Title: str
        """
        self.PlaylistId = None
        self.Title = None


    def _deserialize(self, params):
        self.PlaylistId = params.get("PlaylistId")
        self.Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVSuggestionInfo(AbstractModel):
    """联想词信息。

    """

    def __init__(self):
        r"""
        :param Suggestion: 联想词。
        :type Suggestion: str
        """
        self.Suggestion = None


    def _deserialize(self, params):
        self.Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicAlbumCoverInfo(AbstractModel):
    """歌曲专辑封面信息。

    """

    def __init__(self):
        r"""
        :param Dimension: 尺寸规格，取值有：
<li>Mini：150 x 150 尺寸；</li>
<li>Small：240 x 240 尺寸；</li>
<li>Medium：480 x 480 尺寸。</li>
        :type Dimension: str
        :param Url: 下载链接。
        :type Url: str
        """
        self.Dimension = None
        self.Url = None


    def _deserialize(self, params):
        self.Dimension = params.get("Dimension")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicAlbumInfo(AbstractModel):
    """歌曲专辑信息。

    """

    def __init__(self):
        r"""
        :param Name: 专辑名称。
        :type Name: str
        :param CoverInfoSet: 封面列表。
        :type CoverInfoSet: list of MusicAlbumCoverInfo
        """
        self.Name = None
        self.CoverInfoSet = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("CoverInfoSet") is not None:
            self.CoverInfoSet = []
            for item in params.get("CoverInfoSet"):
                obj = MusicAlbumCoverInfo()
                obj._deserialize(item)
                self.CoverInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKTVMusicsRequest(AbstractModel):
    """SearchKTVMusics请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param KeyWord: 关键词。
        :type KeyWord: str
        :param ScrollToken: 滚动标记。
        :type ScrollToken: str
        :param Limit: 返回条数限制，默认 20，最大 50.
        :type Limit: int
        :param RightFilters: 权益过滤，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightFilters: list of str
        """
        self.AppName = None
        self.UserId = None
        self.KeyWord = None
        self.ScrollToken = None
        self.Limit = None
        self.RightFilters = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.KeyWord = params.get("KeyWord")
        self.ScrollToken = params.get("ScrollToken")
        self.Limit = params.get("Limit")
        self.RightFilters = params.get("RightFilters")
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
        :param KTVMusicInfoSet: 歌曲信息列表。
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param ScrollToken: 滚动标记，用于设置下次请求的 ScrollToken 参数。
        :type ScrollToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KTVMusicInfoSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KTVMusicInfoSet") is not None:
            self.KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self.KTVMusicInfoSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")