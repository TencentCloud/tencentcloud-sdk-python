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


class AMEMusicBaseInfo(AbstractModel):
    """AME 曲库歌曲基础信息。

    """

    def __init__(self):
        r"""
        :param MusicId: 歌曲 Id。
        :type MusicId: str
        :param Name: 歌曲名称。
        :type Name: str
        :param SingerSet: 歌手列表。
        :type SingerSet: list of str
        """
        self.MusicId = None
        self.Name = None
        self.SingerSet = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.Name = params.get("Name")
        self.SingerSet = params.get("SingerSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyChorusRequest(AbstractModel):
    """ApplyChorus请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param RoomId: 房间号。
        :type RoomId: str
        :param MusicId: 歌曲 Id。
        :type MusicId: str
        :param MaxChorusNum: 最大合唱人数，默认值为 8，最大值为 20。
        :type MaxChorusNum: int
        :param ChorusUserIds: 合唱用户标识列表。
        :type ChorusUserIds: list of str
        """
        self.AppName = None
        self.UserId = None
        self.RoomId = None
        self.MusicId = None
        self.MaxChorusNum = None
        self.ChorusUserIds = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.RoomId = params.get("RoomId")
        self.MusicId = params.get("MusicId")
        self.MaxChorusNum = params.get("MaxChorusNum")
        self.ChorusUserIds = params.get("ChorusUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyChorusResponse(AbstractModel):
    """ApplyChorus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ChorusToken: 合唱 Token。
        :type ChorusToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ChorusToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ChorusToken = params.get("ChorusToken")
        self.RequestId = params.get("RequestId")


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
        :param PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param GuestUserId: 玩家用户标识
        :type GuestUserId: str
        :param RoomId: 房间Id
        :type RoomId: str
        """
        self.AppName = None
        self.UserId = None
        self.MusicIds = None
        self.PlayScene = None
        self.GuestUserId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.MusicIds = params.get("MusicIds")
        self.PlayScene = params.get("PlayScene")
        self.GuestUserId = params.get("GuestUserId")
        self.RoomId = params.get("RoomId")
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
        


class CreateKTVRobotRequest(AbstractModel):
    """CreateKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        :param JoinRoomInput: 进房参数。
        :type JoinRoomInput: :class:`tencentcloud.yinsuda.v20220527.models.JoinRoomInput`
        :param SyncRobotCommands: 创建机器人时初始化参数。
        :type SyncRobotCommands: list of SyncRobotCommand
        """
        self.AppName = None
        self.UserId = None
        self.RTCSystem = None
        self.JoinRoomInput = None
        self.SyncRobotCommands = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.RTCSystem = params.get("RTCSystem")
        if params.get("JoinRoomInput") is not None:
            self.JoinRoomInput = JoinRoomInput()
            self.JoinRoomInput._deserialize(params.get("JoinRoomInput"))
        if params.get("SyncRobotCommands") is not None:
            self.SyncRobotCommands = []
            for item in params.get("SyncRobotCommands"):
                obj = SyncRobotCommand()
                obj._deserialize(item)
                self.SyncRobotCommands.append(obj)
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


class DescribeKTVMatchMusicsRequest(AbstractModel):
    """DescribeKTVMatchMusics请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param Rules: 匹配规则列表。
        :type Rules: list of KTVMatchRule
        """
        self.AppName = None
        self.UserId = None
        self.Rules = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = KTVMatchRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMatchMusicsResponse(AbstractModel):
    """DescribeKTVMatchMusics返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchMusicSet: 匹配到的歌曲列表。
        :type MatchMusicSet: list of KTVMatchMusic
        :param NotMatchRuleSet: 未匹配的规则列表。
        :type NotMatchRuleSet: list of KTVMatchRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchMusicSet = None
        self.NotMatchRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchMusicSet") is not None:
            self.MatchMusicSet = []
            for item in params.get("MatchMusicSet"):
                obj = KTVMatchMusic()
                obj._deserialize(item)
                self.MatchMusicSet.append(obj)
        if params.get("NotMatchRuleSet") is not None:
            self.NotMatchRuleSet = []
            for item in params.get("NotMatchRuleSet"):
                obj = KTVMatchRule()
                obj._deserialize(item)
                self.NotMatchRuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKTVMusicAccompanySegmentUrlRequest(AbstractModel):
    """DescribeKTVMusicAccompanySegmentUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param MusicId: 歌曲 Id 。
        :type MusicId: str
        :param PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param RoomId: 房间Id
        :type RoomId: str
        """
        self.AppName = None
        self.UserId = None
        self.MusicId = None
        self.PlayScene = None
        self.RoomId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.MusicId = params.get("MusicId")
        self.PlayScene = params.get("PlayScene")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMusicAccompanySegmentUrlResponse(AbstractModel):
    """DescribeKTVMusicAccompanySegmentUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 歌曲状态。
0：可用
1：下线
2：没权限
3：没伴奏
当返回2时，其他参数有可能全部为空
        :type Status: int
        :param Url: 伴奏链接
        :type Url: str
        :param ExtName: 伴奏类型，如mkv，mp3等
        :type ExtName: str
        :param SegmentBegin: 高潮开始时间
        :type SegmentBegin: int
        :param SegmentEnd: 高潮结束时间
        :type SegmentEnd: int
        :param FileSize: 链接文件大小 单位 字节
        :type FileSize: int
        :param OtherSegments: 其它片段时间（可用于抢唱）
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherSegments: list of KTVOtherSegments
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Url = None
        self.ExtName = None
        self.SegmentBegin = None
        self.SegmentEnd = None
        self.FileSize = None
        self.OtherSegments = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Url = params.get("Url")
        self.ExtName = params.get("ExtName")
        self.SegmentBegin = params.get("SegmentBegin")
        self.SegmentEnd = params.get("SegmentEnd")
        self.FileSize = params.get("FileSize")
        if params.get("OtherSegments") is not None:
            self.OtherSegments = []
            for item in params.get("OtherSegments"):
                obj = KTVOtherSegments()
                obj._deserialize(item)
                self.OtherSegments.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKTVMusicsByTagRequest(AbstractModel):
    """DescribeKTVMusicsByTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param TagId: 标签 Id。
        :type TagId: str
        :param ScrollToken: 滚动标记。
        :type ScrollToken: str
        :param Limit: 返回条数限制，默认 20，最大 50。
        :type Limit: int
        :param RightFilters: 权益过滤，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightFilters: list of str
        :param MaterialFilters: 物料过滤，取值有：
<li>Lyrics：含有歌词；</li>
<li>Midi：含有音高线。</li>
        :type MaterialFilters: list of str
        """
        self.AppName = None
        self.UserId = None
        self.TagId = None
        self.ScrollToken = None
        self.Limit = None
        self.RightFilters = None
        self.MaterialFilters = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.TagId = params.get("TagId")
        self.ScrollToken = params.get("ScrollToken")
        self.Limit = params.get("Limit")
        self.RightFilters = params.get("RightFilters")
        self.MaterialFilters = params.get("MaterialFilters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMusicsByTagResponse(AbstractModel):
    """DescribeKTVMusicsByTag返回参数结构体

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
        :param PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param MaterialFilters: 物料过滤，取值有：
<li>Lyrics：含有歌词；</li>
<li>Midi：含有音高线。</li>
        :type MaterialFilters: list of str
        """
        self.AppName = None
        self.UserId = None
        self.PlaylistId = None
        self.ScrollToken = None
        self.Limit = None
        self.RightFilters = None
        self.PlayScene = None
        self.MaterialFilters = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.PlaylistId = params.get("PlaylistId")
        self.ScrollToken = params.get("ScrollToken")
        self.Limit = params.get("Limit")
        self.RightFilters = params.get("RightFilters")
        self.PlayScene = params.get("PlayScene")
        self.MaterialFilters = params.get("MaterialFilters")
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
默认值为 OfficialRec。
        :type Types: list of str
        :param Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：20，最大值：50。
        :type Limit: int
        """
        self.AppName = None
        self.UserId = None
        self.Types = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.Types = params.get("Types")
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
        :param PlaylistBaseInfoSet: 歌单基础信息。
        :type PlaylistBaseInfoSet: list of KTVPlaylistBaseInfo
        :param TotalCount: 歌单总数。
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
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param RobotIds: 机器人Id列表。
        :type RobotIds: list of str
        :param Statuses: 机器人状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :type Statuses: list of str
        :param CreateTime: 匹配创建时间在此时间段内的机器人。
<li>包含所指定的头尾时间点。</li>
        :type CreateTime: :class:`tencentcloud.yinsuda.v20220527.models.TimeRange`
        :param Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param Limit: 分页返回的起始偏移量，默认值：10。
        :type Limit: int
        """
        self.AppName = None
        self.UserId = None
        self.RobotIds = None
        self.Statuses = None
        self.CreateTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.RobotIds = params.get("RobotIds")
        self.Statuses = params.get("Statuses")
        if params.get("CreateTime") is not None:
            self.CreateTime = TimeRange()
            self.CreateTime._deserialize(params.get("CreateTime"))
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


class DescribeKTVTagsRequest(AbstractModel):
    """DescribeKTVTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        """
        self.AppName = None
        self.UserId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVTagsResponse(AbstractModel):
    """DescribeKTVTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param TagGroupInfoSet: 标签分组列表。
        :type TagGroupInfoSet: list of KTVTagGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TagGroupInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TagGroupInfoSet") is not None:
            self.TagGroupInfoSet = []
            for item in params.get("TagGroupInfoSet"):
                obj = KTVTagGroupInfo()
                obj._deserialize(item)
                self.TagGroupInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveVipTradeInfosRequest(AbstractModel):
    """DescribeLiveVipTradeInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param StartTime: 直播会员充值下单起始时间，格式为 ISO。默认为当前时间前一天。
        :type StartTime: str
        :param EndTime: 直播会员充值下单截止时间，格式为 ISO。默认为当前时间。 EndTime不能小于StartTime
        :type EndTime: str
        :param TradeSerialNos: 交易流水号集合，匹配集合指定所有流水号 。
<li>数组长度限制：10。</li>
        :type TradeSerialNos: list of str
        :param UserIds: 用户标识集合，匹配集合指定所有用户标识 。
<li>数组长度限制：10。</li>
        :type UserIds: list of str
        :param Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：20，最大值：50。
        :type Limit: int
        """
        self.AppName = None
        self.StartTime = None
        self.EndTime = None
        self.TradeSerialNos = None
        self.UserIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TradeSerialNos = params.get("TradeSerialNos")
        self.UserIds = params.get("UserIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveVipTradeInfosResponse(AbstractModel):
    """DescribeLiveVipTradeInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param LiveVipTradeInfoSet: 直播会员充值流水信息列表
        :type LiveVipTradeInfoSet: list of LiveVipTradeInfo
        :param TotalCount: 直播会员充值流水总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LiveVipTradeInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LiveVipTradeInfoSet") is not None:
            self.LiveVipTradeInfoSet = []
            for item in params.get("LiveVipTradeInfoSet"):
                obj = LiveVipTradeInfo()
                obj._deserialize(item)
                self.LiveVipTradeInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        """
        self.AppName = None
        self.UserId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserInfo: 用户信息。
        :type UserInfo: :class:`tencentcloud.yinsuda.v20220527.models.UserInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = UserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.RequestId = params.get("RequestId")


class DestroyKTVRobotRequest(AbstractModel):
    """DestroyKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param RobotId: 机器人Id。
        :type RobotId: str
        """
        self.AppName = None
        self.UserId = None
        self.RobotId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
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


class JoinRoomInput(AbstractModel):
    """直播进房输入参数

    """

    def __init__(self):
        r"""
        :param TRTCJoinRoomInput: TRTC进房参数
        :type TRTCJoinRoomInput: :class:`tencentcloud.yinsuda.v20220527.models.TRTCJoinRoomInput`
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
        


class KTVBPMInfo(AbstractModel):
    """节拍信息。

    """

    def __init__(self):
        r"""
        :param Type: 节拍类型，取值有：
<li>Slow：慢；</li>
<li>Middle：中等；</li>
<li>Fast：快；</li>
<li>Unknown：未知。</li>
        :type Type: str
        :param Value: BPM 值。
        :type Value: int
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMatchMusic(AbstractModel):
    """匹配歌曲信息。

    """

    def __init__(self):
        r"""
        :param KTVMusicBaseInfo: 匹配到的歌曲基础信息。
        :type KTVMusicBaseInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVMusicBaseInfo`
        :param MatchRule: 命中规则。
        :type MatchRule: :class:`tencentcloud.yinsuda.v20220527.models.KTVMatchRule`
        :param AMEMusicBaseInfo: AME 歌曲基础信息，仅在使用音速达歌曲 Id 匹配 AME 曲库时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AMEMusicBaseInfo: :class:`tencentcloud.yinsuda.v20220527.models.AMEMusicBaseInfo`
        """
        self.KTVMusicBaseInfo = None
        self.MatchRule = None
        self.AMEMusicBaseInfo = None


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self.KTVMusicBaseInfo = KTVMusicBaseInfo()
            self.KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        if params.get("MatchRule") is not None:
            self.MatchRule = KTVMatchRule()
            self.MatchRule._deserialize(params.get("MatchRule"))
        if params.get("AMEMusicBaseInfo") is not None:
            self.AMEMusicBaseInfo = AMEMusicBaseInfo()
            self.AMEMusicBaseInfo._deserialize(params.get("AMEMusicBaseInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMatchRule(AbstractModel):
    """歌曲匹配规则。

    """

    def __init__(self):
        r"""
        :param AMEMusicId: AME 曲库 Id。
        :type AMEMusicId: str
        :param MusicInfo: 歌曲匹配信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVMatchRuleMusicInfo`
        :param MusicIdToMatchAME: 音速达歌曲 Id，用于匹配 AME 曲库歌曲。
        :type MusicIdToMatchAME: str
        """
        self.AMEMusicId = None
        self.MusicInfo = None
        self.MusicIdToMatchAME = None


    def _deserialize(self, params):
        self.AMEMusicId = params.get("AMEMusicId")
        if params.get("MusicInfo") is not None:
            self.MusicInfo = KTVMatchRuleMusicInfo()
            self.MusicInfo._deserialize(params.get("MusicInfo"))
        self.MusicIdToMatchAME = params.get("MusicIdToMatchAME")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMatchRuleMusicInfo(AbstractModel):
    """歌曲信息匹配。

    """

    def __init__(self):
        r"""
        :param MusicName: 歌曲名称。
        :type MusicName: str
        :param SingerSet: 歌手列表。
        :type SingerSet: list of str
        """
        self.MusicName = None
        self.SingerSet = None


    def _deserialize(self, params):
        self.MusicName = params.get("MusicName")
        self.SingerSet = params.get("SingerSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param BPMInfo: 节拍信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BPMInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVBPMInfo`
        """
        self.KTVMusicBaseInfo = None
        self.PlayToken = None
        self.LyricsUrl = None
        self.MidiUrl = None
        self.ChorusClipSet = None
        self.PreludeInterval = None
        self.GenreSet = None
        self.BPMInfo = None


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
        if params.get("BPMInfo") is not None:
            self.BPMInfo = KTVBPMInfo()
            self.BPMInfo._deserialize(params.get("BPMInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVOtherSegments(AbstractModel):
    """其它片段时间（可用于抢唱）

    """

    def __init__(self):
        r"""
        :param SegmentBegin: 片段开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentBegin: int
        :param SegmentEnd: 片段结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentEnd: int
        """
        self.SegmentBegin = None
        self.SegmentEnd = None


    def _deserialize(self, params):
        self.SegmentBegin = params.get("SegmentBegin")
        self.SegmentEnd = params.get("SegmentEnd")
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
        :param SetAudioParamInput: 音频参数。
        :type SetAudioParamInput: :class:`tencentcloud.yinsuda.v20220527.models.SetAudioParamCommandInput`
        :param JoinRoomInput: 进房信息。
        :type JoinRoomInput: :class:`tencentcloud.yinsuda.v20220527.models.JoinRoomInput`
        :param RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        :param SetPlayModeInput: 播放模式，PlayMode取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :type SetPlayModeInput: :class:`tencentcloud.yinsuda.v20220527.models.SetPlayModeCommandInput`
        """
        self.RobotId = None
        self.Status = None
        self.Playlists = None
        self.CurIndex = None
        self.Position = None
        self.SetAudioParamInput = None
        self.JoinRoomInput = None
        self.RTCSystem = None
        self.SetPlayModeInput = None


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
        if params.get("SetPlayModeInput") is not None:
            self.SetPlayModeInput = SetPlayModeCommandInput()
            self.SetPlayModeInput._deserialize(params.get("SetPlayModeInput"))
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
        


class KTVTagGroupInfo(AbstractModel):
    """标签分组信息。

    """

    def __init__(self):
        r"""
        :param GroupId: 分组 Id。
        :type GroupId: str
        :param Name: 分组名。
        :type Name: str
        :param TagInfoSet: 标签列表。
        :type TagInfoSet: list of KTVTagInfo
        """
        self.GroupId = None
        self.Name = None
        self.TagInfoSet = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Name = params.get("Name")
        if params.get("TagInfoSet") is not None:
            self.TagInfoSet = []
            for item in params.get("TagInfoSet"):
                obj = KTVTagInfo()
                obj._deserialize(item)
                self.TagInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVTagInfo(AbstractModel):
    """标签信息。

    """

    def __init__(self):
        r"""
        :param TagId: 标签 Id。
        :type TagId: str
        :param Name: 标签名称。
        :type Name: str
        """
        self.TagId = None
        self.Name = None


    def _deserialize(self, params):
        self.TagId = params.get("TagId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveVipTradeInfo(AbstractModel):
    """充值直播会员流水信息

    """

    def __init__(self):
        r"""
        :param TradeSerialNo: 交易流水号。
        :type TradeSerialNo: str
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param RoomId: 房间标识。
        :type RoomId: str
        :param VipDays: 充值会员天数。
取值有： 
<li>31</li> <li>93</li><li>186</li> <li>372</li>
        :type VipDays: int
        :param Status: 订单状态。 
取值有： 
<li>Success：成功</li><li>Fail：失败</li><li>Processing：订单处理中</li>
        :type Status: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        """
        self.TradeSerialNo = None
        self.AppName = None
        self.UserId = None
        self.RoomId = None
        self.VipDays = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.RoomId = params.get("RoomId")
        self.VipDays = params.get("VipDays")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveVipUserInfo(AbstractModel):
    """直播会员用户信息

    """

    def __init__(self):
        r"""
        :param RoomId: 房间标识。
        :type RoomId: str
        :param LiveVipEndTime: 直播会员结束时间。
        :type LiveVipEndTime: str
        :param LiveVipStatus: 会员生效状态
<li>Valid：生效</li><li>Invalid：无效</li>
        :type LiveVipStatus: str
        """
        self.RoomId = None
        self.LiveVipEndTime = None
        self.LiveVipStatus = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.LiveVipEndTime = params.get("LiveVipEndTime")
        self.LiveVipStatus = params.get("LiveVipStatus")
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
        


class RechargeLiveVipRequest(AbstractModel):
    """RechargeLiveVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param TradeSerialNo: 交易流水号，用于标记此次充值记录，多次充值记录传入相同的 TradeSerialNo 会判断为失败，可用于防止重提提交造成重复计费。
        :type TradeSerialNo: str
        :param RoomId: 房间标识。
        :type RoomId: str
        :param VipDays: 充值会员天数。
取值有：
<li>31</li>
<li>93</li>
<li>186</li>
<li>372</li>
        :type VipDays: int
        :param GiveType: 充值分类。取值有：room_card-包月房卡; 其他-保留。
        :type GiveType: str
        :param PlayScene: 播放场景。默认为Live
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        """
        self.AppName = None
        self.UserId = None
        self.TradeSerialNo = None
        self.RoomId = None
        self.VipDays = None
        self.GiveType = None
        self.PlayScene = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.RoomId = params.get("RoomId")
        self.VipDays = params.get("VipDays")
        self.GiveType = params.get("GiveType")
        self.PlayScene = params.get("PlayScene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeLiveVipResponse(AbstractModel):
    """RechargeLiveVip返回参数结构体

    """

    def __init__(self):
        r"""
        :param LiveVipUserInfo: 直播会员信息。
        :type LiveVipUserInfo: :class:`tencentcloud.yinsuda.v20220527.models.LiveVipUserInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LiveVipUserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LiveVipUserInfo") is not None:
            self.LiveVipUserInfo = LiveVipUserInfo()
            self.LiveVipUserInfo._deserialize(params.get("LiveVipUserInfo"))
        self.RequestId = params.get("RequestId")


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
        :param PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param MaterialFilters: 物料过滤，取值有：
<li>Lyrics：含有歌词；</li>
<li>Midi：含有音高线。</li>
        :type MaterialFilters: list of str
        """
        self.AppName = None
        self.UserId = None
        self.KeyWord = None
        self.ScrollToken = None
        self.Limit = None
        self.RightFilters = None
        self.PlayScene = None
        self.MaterialFilters = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.KeyWord = params.get("KeyWord")
        self.ScrollToken = params.get("ScrollToken")
        self.Limit = params.get("Limit")
        self.RightFilters = params.get("RightFilters")
        self.PlayScene = params.get("PlayScene")
        self.MaterialFilters = params.get("MaterialFilters")
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
        :param Type: 音频类型，取值有：
<li>Original：原唱</li>
<li>Accompaniment：伴奏</li>
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDestroyModeCommandInput(AbstractModel):
    """设置销毁模式

    """

    def __init__(self):
        r"""
        :param DestroyMode: 销毁模式，取值有：
<li>Auto：房间没人时自动销毁</li>
<li>Expire：房间没人时过期自动销毁</li>
<li>Never：不自动销毁，需手动销毁</li>默认为：Auto。
        :type DestroyMode: str
        :param DestroyExpireTime: 过期销毁时间，单位：秒，当DestroyMode取Expire时必填。
        :type DestroyExpireTime: int
        """
        self.DestroyMode = None
        self.DestroyExpireTime = None


    def _deserialize(self, params):
        self.DestroyMode = params.get("DestroyMode")
        self.DestroyExpireTime = params.get("DestroyExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPlayModeCommandInput(AbstractModel):
    """设置播放模式

    """

    def __init__(self):
        r"""
        :param PlayMode: 播放模式，取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :type PlayMode: str
        """
        self.PlayMode = None


    def _deserialize(self, params):
        self.PlayMode = params.get("PlayMode")
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
<li>ClearList：清空歌曲列表</li>
<li>Move：移动歌曲</li>
        :type Type: str
        :param Index: 歌单索引位置，
当 Type 取 Add 时，-1表示添加在列表最后位置，大于-1表示要添加的位置；
当 Type 取 Delete 时，表示待删除歌曲的位置；
当 Type 取 Move 时，表示待调整歌曲的位置。
        :type Index: int
        :param ChangedIndex: 当 Type 取 Move 时，必填，表示移动歌曲的目标位置。
        :type ChangedIndex: int
        :param MusicIds: 歌曲 ID 列表，当 Type 取 Add 时，必填。
        :type MusicIds: list of str
        """
        self.Type = None
        self.Index = None
        self.ChangedIndex = None
        self.MusicIds = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Index = params.get("Index")
        self.ChangedIndex = params.get("ChangedIndex")
        self.MusicIds = params.get("MusicIds")
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
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param RobotId: 机器人Id。
        :type RobotId: str
        :param SyncRobotCommands: 指令及指令参数数组。
        :type SyncRobotCommands: list of SyncRobotCommand
        """
        self.AppName = None
        self.UserId = None
        self.RobotId = None
        self.SyncRobotCommands = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        self.RobotId = params.get("RobotId")
        if params.get("SyncRobotCommands") is not None:
            self.SyncRobotCommands = []
            for item in params.get("SyncRobotCommands"):
                obj = SyncRobotCommand()
                obj._deserialize(item)
                self.SyncRobotCommands.append(obj)
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


class SyncRobotCommand(AbstractModel):
    """KTV 机器人初始化参数，在创建后自动完成相关初始化工作。

    """

    def __init__(self):
        r"""
        :param Command: 可同时传入多个指令，顺序执行。取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>SwitchPrevious：上一首</li>
<li>SwitchNext：下一首</li>
<li>SetPlayMode：设置播放模式</li>
<li>Seek：调整播放进度</li>
<li>SetPlaylist：歌单变更</li>
<li>SetAudioParam：音频参数变更</li>
<li>SendMessage：发送自定义消息</li>
<li>SetDestroyMode：设置销毁模式</li>
        :type Command: str
        :param PlayCommandInput: 播放参数。
        :type PlayCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.PlayCommandInput`
        :param SetPlaylistCommandInput: 播放列表变更信息，当Command取SetPlaylist时，必填。
        :type SetPlaylistCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetPlaylistCommandInput`
        :param SeekCommandInput: 播放进度，当Command取Seek时，必填。
        :type SeekCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SeekCommandInput`
        :param SetAudioParamCommandInput: 音频参数，当Command取SetAudioParam时，必填。
        :type SetAudioParamCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetAudioParamCommandInput`
        :param SendMessageCommandInput: 自定义消息，当Command取SendMessage时，必填。
        :type SendMessageCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SendMessageCommandInput`
        :param SetPlayModeCommandInput: 播放模式，当Command取SetPlayMode时，必填。
        :type SetPlayModeCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetPlayModeCommandInput`
        :param SetDestroyModeCommandInput: 销毁模式，当Command取SetDestroyMode时，必填。
        :type SetDestroyModeCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetDestroyModeCommandInput`
        """
        self.Command = None
        self.PlayCommandInput = None
        self.SetPlaylistCommandInput = None
        self.SeekCommandInput = None
        self.SetAudioParamCommandInput = None
        self.SendMessageCommandInput = None
        self.SetPlayModeCommandInput = None
        self.SetDestroyModeCommandInput = None


    def _deserialize(self, params):
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
        if params.get("SetPlayModeCommandInput") is not None:
            self.SetPlayModeCommandInput = SetPlayModeCommandInput()
            self.SetPlayModeCommandInput._deserialize(params.get("SetPlayModeCommandInput"))
        if params.get("SetDestroyModeCommandInput") is not None:
            self.SetDestroyModeCommandInput = SetDestroyModeCommandInput()
            self.SetDestroyModeCommandInput._deserialize(params.get("SetDestroyModeCommandInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class TimeRange(AbstractModel):
    """时间范围

    """

    def __init__(self):
        r"""
        :param Before: <li>大于等于此时间（起始时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :type Before: str
        :param After: <li>小于此时间（结束时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :type After: str
        """
        self.Before = None
        self.After = None


    def _deserialize(self, params):
        self.Before = params.get("Before")
        self.After = params.get("After")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称。
        :type AppName: str
        :param UserId: 用户标识。
        :type UserId: str
        :param LiveVipUserInfo: 直播会员详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveVipUserInfo: :class:`tencentcloud.yinsuda.v20220527.models.LiveVipUserInfo`
        :param UserType: 用户类型
<li>Normal：普通用户</li>
<li>LiveVip：直播会员用户</li>
        :type UserType: str
        """
        self.AppName = None
        self.UserId = None
        self.LiveVipUserInfo = None
        self.UserType = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.UserId = params.get("UserId")
        if params.get("LiveVipUserInfo") is not None:
            self.LiveVipUserInfo = LiveVipUserInfo()
            self.LiveVipUserInfo._deserialize(params.get("LiveVipUserInfo"))
        self.UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        