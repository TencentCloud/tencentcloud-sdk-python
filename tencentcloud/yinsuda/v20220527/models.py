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
        :param _MusicId: 歌曲 Id。
        :type MusicId: str
        :param _Name: 歌曲名称。
        :type Name: str
        :param _SingerSet: 歌手列表。
        :type SingerSet: list of str
        """
        self._MusicId = None
        self._Name = None
        self._SingerSet = None

    @property
    def MusicId(self):
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SingerSet(self):
        return self._SingerSet

    @SingerSet.setter
    def SingerSet(self, SingerSet):
        self._SingerSet = SingerSet


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._Name = params.get("Name")
        self._SingerSet = params.get("SingerSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyChorusRequest(AbstractModel):
    """ApplyChorus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _RoomId: 房间号。
        :type RoomId: str
        :param _MusicId: 歌曲 Id。
        :type MusicId: str
        :param _MaxChorusNum: 最大合唱人数，默认值为 8，最大值为 20。
        :type MaxChorusNum: int
        :param _ChorusUserIds: 合唱用户标识列表。
        :type ChorusUserIds: list of str
        """
        self._AppName = None
        self._UserId = None
        self._RoomId = None
        self._MusicId = None
        self._MaxChorusNum = None
        self._ChorusUserIds = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def MusicId(self):
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def MaxChorusNum(self):
        return self._MaxChorusNum

    @MaxChorusNum.setter
    def MaxChorusNum(self, MaxChorusNum):
        self._MaxChorusNum = MaxChorusNum

    @property
    def ChorusUserIds(self):
        return self._ChorusUserIds

    @ChorusUserIds.setter
    def ChorusUserIds(self, ChorusUserIds):
        self._ChorusUserIds = ChorusUserIds


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._MusicId = params.get("MusicId")
        self._MaxChorusNum = params.get("MaxChorusNum")
        self._ChorusUserIds = params.get("ChorusUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyChorusResponse(AbstractModel):
    """ApplyChorus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ChorusToken: 合唱 Token。
        :type ChorusToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ChorusToken = None
        self._RequestId = None

    @property
    def ChorusToken(self):
        return self._ChorusToken

    @ChorusToken.setter
    def ChorusToken(self, ChorusToken):
        self._ChorusToken = ChorusToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ChorusToken = params.get("ChorusToken")
        self._RequestId = params.get("RequestId")


class BatchDescribeKTVMusicDetailsRequest(AbstractModel):
    """BatchDescribeKTVMusicDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _MusicIds: 歌曲 Id 列表。
        :type MusicIds: list of str
        :param _PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param _GuestUserId: 玩家用户标识
        :type GuestUserId: str
        :param _RoomId: 房间Id
        :type RoomId: str
        """
        self._AppName = None
        self._UserId = None
        self._MusicIds = None
        self._PlayScene = None
        self._GuestUserId = None
        self._RoomId = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def MusicIds(self):
        return self._MusicIds

    @MusicIds.setter
    def MusicIds(self, MusicIds):
        self._MusicIds = MusicIds

    @property
    def PlayScene(self):
        return self._PlayScene

    @PlayScene.setter
    def PlayScene(self, PlayScene):
        self._PlayScene = PlayScene

    @property
    def GuestUserId(self):
        return self._GuestUserId

    @GuestUserId.setter
    def GuestUserId(self, GuestUserId):
        self._GuestUserId = GuestUserId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._MusicIds = params.get("MusicIds")
        self._PlayScene = params.get("PlayScene")
        self._GuestUserId = params.get("GuestUserId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeKTVMusicDetailsResponse(AbstractModel):
    """BatchDescribeKTVMusicDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicDetailInfoSet: 歌曲详细信息列表。
        :type KTVMusicDetailInfoSet: list of KTVMusicDetailInfo
        :param _NotExistMusicIdSet: 不存在歌曲Id列表。
        :type NotExistMusicIdSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicDetailInfoSet = None
        self._NotExistMusicIdSet = None
        self._RequestId = None

    @property
    def KTVMusicDetailInfoSet(self):
        return self._KTVMusicDetailInfoSet

    @KTVMusicDetailInfoSet.setter
    def KTVMusicDetailInfoSet(self, KTVMusicDetailInfoSet):
        self._KTVMusicDetailInfoSet = KTVMusicDetailInfoSet

    @property
    def NotExistMusicIdSet(self):
        return self._NotExistMusicIdSet

    @NotExistMusicIdSet.setter
    def NotExistMusicIdSet(self, NotExistMusicIdSet):
        self._NotExistMusicIdSet = NotExistMusicIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicDetailInfoSet") is not None:
            self._KTVMusicDetailInfoSet = []
            for item in params.get("KTVMusicDetailInfoSet"):
                obj = KTVMusicDetailInfo()
                obj._deserialize(item)
                self._KTVMusicDetailInfoSet.append(obj)
        self._NotExistMusicIdSet = params.get("NotExistMusicIdSet")
        self._RequestId = params.get("RequestId")


class ChorusClip(AbstractModel):
    """副歌片段信息。

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，单位：毫秒。
        :type StartTime: int
        :param _EndTime: 结束时间，单位：毫秒。
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKTVRobotRequest(AbstractModel):
    """CreateKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        :param _JoinRoomInput: 进房参数。
        :type JoinRoomInput: :class:`tencentcloud.yinsuda.v20220527.models.JoinRoomInput`
        :param _SyncRobotCommands: 创建机器人时初始化参数。
        :type SyncRobotCommands: list of SyncRobotCommand
        """
        self._AppName = None
        self._UserId = None
        self._RTCSystem = None
        self._JoinRoomInput = None
        self._SyncRobotCommands = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RTCSystem(self):
        return self._RTCSystem

    @RTCSystem.setter
    def RTCSystem(self, RTCSystem):
        self._RTCSystem = RTCSystem

    @property
    def JoinRoomInput(self):
        return self._JoinRoomInput

    @JoinRoomInput.setter
    def JoinRoomInput(self, JoinRoomInput):
        self._JoinRoomInput = JoinRoomInput

    @property
    def SyncRobotCommands(self):
        return self._SyncRobotCommands

    @SyncRobotCommands.setter
    def SyncRobotCommands(self, SyncRobotCommands):
        self._SyncRobotCommands = SyncRobotCommands


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._RTCSystem = params.get("RTCSystem")
        if params.get("JoinRoomInput") is not None:
            self._JoinRoomInput = JoinRoomInput()
            self._JoinRoomInput._deserialize(params.get("JoinRoomInput"))
        if params.get("SyncRobotCommands") is not None:
            self._SyncRobotCommands = []
            for item in params.get("SyncRobotCommands"):
                obj = SyncRobotCommand()
                obj._deserialize(item)
                self._SyncRobotCommands.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKTVRobotResponse(AbstractModel):
    """CreateKTVRobot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RobotId: 机器人Id。
        :type RobotId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RobotId = None
        self._RequestId = None

    @property
    def RobotId(self):
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RobotId = params.get("RobotId")
        self._RequestId = params.get("RequestId")


class DescribeKTVMatchMusicsRequest(AbstractModel):
    """DescribeKTVMatchMusics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _Rules: 匹配规则列表。
        :type Rules: list of KTVMatchRule
        """
        self._AppName = None
        self._UserId = None
        self._Rules = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = KTVMatchRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMatchMusicsResponse(AbstractModel):
    """DescribeKTVMatchMusics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchMusicSet: 匹配到的歌曲列表。
        :type MatchMusicSet: list of KTVMatchMusic
        :param _NotMatchRuleSet: 未匹配的规则列表。
        :type NotMatchRuleSet: list of KTVMatchRule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchMusicSet = None
        self._NotMatchRuleSet = None
        self._RequestId = None

    @property
    def MatchMusicSet(self):
        return self._MatchMusicSet

    @MatchMusicSet.setter
    def MatchMusicSet(self, MatchMusicSet):
        self._MatchMusicSet = MatchMusicSet

    @property
    def NotMatchRuleSet(self):
        return self._NotMatchRuleSet

    @NotMatchRuleSet.setter
    def NotMatchRuleSet(self, NotMatchRuleSet):
        self._NotMatchRuleSet = NotMatchRuleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MatchMusicSet") is not None:
            self._MatchMusicSet = []
            for item in params.get("MatchMusicSet"):
                obj = KTVMatchMusic()
                obj._deserialize(item)
                self._MatchMusicSet.append(obj)
        if params.get("NotMatchRuleSet") is not None:
            self._NotMatchRuleSet = []
            for item in params.get("NotMatchRuleSet"):
                obj = KTVMatchRule()
                obj._deserialize(item)
                self._NotMatchRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVMusicAccompanySegmentUrlRequest(AbstractModel):
    """DescribeKTVMusicAccompanySegmentUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _MusicId: 歌曲 Id 。
        :type MusicId: str
        :param _PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param _RoomId: 房间Id
        :type RoomId: str
        """
        self._AppName = None
        self._UserId = None
        self._MusicId = None
        self._PlayScene = None
        self._RoomId = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def MusicId(self):
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def PlayScene(self):
        return self._PlayScene

    @PlayScene.setter
    def PlayScene(self, PlayScene):
        self._PlayScene = PlayScene

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._MusicId = params.get("MusicId")
        self._PlayScene = params.get("PlayScene")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMusicAccompanySegmentUrlResponse(AbstractModel):
    """DescribeKTVMusicAccompanySegmentUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 歌曲状态。
0：可用
1：下线
2：没权限
3：没伴奏
当返回2时，其他参数有可能全部为空
        :type Status: int
        :param _Url: 伴奏链接
        :type Url: str
        :param _ExtName: 伴奏类型，如mkv，mp3等
        :type ExtName: str
        :param _SegmentBegin: 高潮开始时间
        :type SegmentBegin: int
        :param _SegmentEnd: 高潮结束时间
        :type SegmentEnd: int
        :param _FileSize: 链接文件大小 单位 字节
        :type FileSize: int
        :param _OtherSegments: 其它片段时间（可用于抢唱）
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherSegments: list of KTVOtherSegments
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Url = None
        self._ExtName = None
        self._SegmentBegin = None
        self._SegmentEnd = None
        self._FileSize = None
        self._OtherSegments = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ExtName(self):
        return self._ExtName

    @ExtName.setter
    def ExtName(self, ExtName):
        self._ExtName = ExtName

    @property
    def SegmentBegin(self):
        return self._SegmentBegin

    @SegmentBegin.setter
    def SegmentBegin(self, SegmentBegin):
        self._SegmentBegin = SegmentBegin

    @property
    def SegmentEnd(self):
        return self._SegmentEnd

    @SegmentEnd.setter
    def SegmentEnd(self, SegmentEnd):
        self._SegmentEnd = SegmentEnd

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def OtherSegments(self):
        return self._OtherSegments

    @OtherSegments.setter
    def OtherSegments(self, OtherSegments):
        self._OtherSegments = OtherSegments

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Url = params.get("Url")
        self._ExtName = params.get("ExtName")
        self._SegmentBegin = params.get("SegmentBegin")
        self._SegmentEnd = params.get("SegmentEnd")
        self._FileSize = params.get("FileSize")
        if params.get("OtherSegments") is not None:
            self._OtherSegments = []
            for item in params.get("OtherSegments"):
                obj = KTVOtherSegments()
                obj._deserialize(item)
                self._OtherSegments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVMusicsByTagRequest(AbstractModel):
    """DescribeKTVMusicsByTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _TagId: 标签 Id。
        :type TagId: str
        :param _ScrollToken: 滚动标记。
        :type ScrollToken: str
        :param _Limit: 返回条数限制，默认 20，最大 50。
        :type Limit: int
        :param _RightFilters: 权益过滤，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightFilters: list of str
        :param _MaterialFilters: 物料过滤，取值有：
<li>Lyrics：含有歌词；</li>
<li>Midi：含有音高线。</li>
        :type MaterialFilters: list of str
        """
        self._AppName = None
        self._UserId = None
        self._TagId = None
        self._ScrollToken = None
        self._Limit = None
        self._RightFilters = None
        self._MaterialFilters = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RightFilters(self):
        return self._RightFilters

    @RightFilters.setter
    def RightFilters(self, RightFilters):
        self._RightFilters = RightFilters

    @property
    def MaterialFilters(self):
        return self._MaterialFilters

    @MaterialFilters.setter
    def MaterialFilters(self, MaterialFilters):
        self._MaterialFilters = MaterialFilters


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._TagId = params.get("TagId")
        self._ScrollToken = params.get("ScrollToken")
        self._Limit = params.get("Limit")
        self._RightFilters = params.get("RightFilters")
        self._MaterialFilters = params.get("MaterialFilters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMusicsByTagResponse(AbstractModel):
    """DescribeKTVMusicsByTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicInfoSet: 歌曲信息列表。
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param _ScrollToken: 滚动标记，用于设置下次请求的 ScrollToken 参数。
        :type ScrollToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicInfoSet = None
        self._ScrollToken = None
        self._RequestId = None

    @property
    def KTVMusicInfoSet(self):
        return self._KTVMusicInfoSet

    @KTVMusicInfoSet.setter
    def KTVMusicInfoSet(self, KTVMusicInfoSet):
        self._KTVMusicInfoSet = KTVMusicInfoSet

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicInfoSet") is not None:
            self._KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self._KTVMusicInfoSet.append(obj)
        self._ScrollToken = params.get("ScrollToken")
        self._RequestId = params.get("RequestId")


class DescribeKTVPlaylistDetailRequest(AbstractModel):
    """DescribeKTVPlaylistDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _PlaylistId: 歌单 Id。
        :type PlaylistId: str
        :param _ScrollToken: 滚动标记。
        :type ScrollToken: str
        :param _Limit: 返回条数，默认：20，最大：50。
        :type Limit: int
        :param _RightFilters: 权益过滤，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightFilters: list of str
        :param _PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param _MaterialFilters: 物料过滤，取值有：
<li>Lyrics：含有歌词；</li>
<li>Midi：含有音高线。</li>
        :type MaterialFilters: list of str
        """
        self._AppName = None
        self._UserId = None
        self._PlaylistId = None
        self._ScrollToken = None
        self._Limit = None
        self._RightFilters = None
        self._PlayScene = None
        self._MaterialFilters = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PlaylistId(self):
        return self._PlaylistId

    @PlaylistId.setter
    def PlaylistId(self, PlaylistId):
        self._PlaylistId = PlaylistId

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RightFilters(self):
        return self._RightFilters

    @RightFilters.setter
    def RightFilters(self, RightFilters):
        self._RightFilters = RightFilters

    @property
    def PlayScene(self):
        return self._PlayScene

    @PlayScene.setter
    def PlayScene(self, PlayScene):
        self._PlayScene = PlayScene

    @property
    def MaterialFilters(self):
        return self._MaterialFilters

    @MaterialFilters.setter
    def MaterialFilters(self, MaterialFilters):
        self._MaterialFilters = MaterialFilters


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._PlaylistId = params.get("PlaylistId")
        self._ScrollToken = params.get("ScrollToken")
        self._Limit = params.get("Limit")
        self._RightFilters = params.get("RightFilters")
        self._PlayScene = params.get("PlayScene")
        self._MaterialFilters = params.get("MaterialFilters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVPlaylistDetailResponse(AbstractModel):
    """DescribeKTVPlaylistDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicInfoSet: 歌曲信息列表。
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param _ScrollToken: 滚动标记，用于设置下次请求的 ScrollToken 参数。
        :type ScrollToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicInfoSet = None
        self._ScrollToken = None
        self._RequestId = None

    @property
    def KTVMusicInfoSet(self):
        return self._KTVMusicInfoSet

    @KTVMusicInfoSet.setter
    def KTVMusicInfoSet(self, KTVMusicInfoSet):
        self._KTVMusicInfoSet = KTVMusicInfoSet

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicInfoSet") is not None:
            self._KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self._KTVMusicInfoSet.append(obj)
        self._ScrollToken = params.get("ScrollToken")
        self._RequestId = params.get("RequestId")


class DescribeKTVPlaylistsRequest(AbstractModel):
    """DescribeKTVPlaylists请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _Types: 类型列表，取值有：
<li>OfficialRec：官方推荐；</li>
<li>Customize：自定义。</li>
默认值为 OfficialRec。
        :type Types: list of str
        :param _Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：20，最大值：50。
        :type Limit: int
        """
        self._AppName = None
        self._UserId = None
        self._Types = None
        self._Offset = None
        self._Limit = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._Types = params.get("Types")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVPlaylistsResponse(AbstractModel):
    """DescribeKTVPlaylists返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlaylistBaseInfoSet: 歌单基础信息。
        :type PlaylistBaseInfoSet: list of KTVPlaylistBaseInfo
        :param _TotalCount: 歌单总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlaylistBaseInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PlaylistBaseInfoSet(self):
        return self._PlaylistBaseInfoSet

    @PlaylistBaseInfoSet.setter
    def PlaylistBaseInfoSet(self, PlaylistBaseInfoSet):
        self._PlaylistBaseInfoSet = PlaylistBaseInfoSet

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
        if params.get("PlaylistBaseInfoSet") is not None:
            self._PlaylistBaseInfoSet = []
            for item in params.get("PlaylistBaseInfoSet"):
                obj = KTVPlaylistBaseInfo()
                obj._deserialize(item)
                self._PlaylistBaseInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeKTVRobotsRequest(AbstractModel):
    """DescribeKTVRobots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _RobotIds: 机器人Id列表。
        :type RobotIds: list of str
        :param _Statuses: 机器人状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :type Statuses: list of str
        :param _CreateTime: 匹配创建时间在此时间段内的机器人。
<li>包含所指定的头尾时间点。</li>
        :type CreateTime: :class:`tencentcloud.yinsuda.v20220527.models.TimeRange`
        :param _Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param _Limit: 分页返回的起始偏移量，默认值：10。
        :type Limit: int
        """
        self._AppName = None
        self._UserId = None
        self._RobotIds = None
        self._Statuses = None
        self._CreateTime = None
        self._Offset = None
        self._Limit = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RobotIds(self):
        return self._RobotIds

    @RobotIds.setter
    def RobotIds(self, RobotIds):
        self._RobotIds = RobotIds

    @property
    def Statuses(self):
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._RobotIds = params.get("RobotIds")
        self._Statuses = params.get("Statuses")
        if params.get("CreateTime") is not None:
            self._CreateTime = TimeRange()
            self._CreateTime._deserialize(params.get("CreateTime"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVRobotsResponse(AbstractModel):
    """DescribeKTVRobots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 机器人总数。
        :type TotalCount: int
        :param _KTVRobotInfoSet: 机器人信息集合。
        :type KTVRobotInfoSet: list of KTVRobotInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KTVRobotInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KTVRobotInfoSet(self):
        return self._KTVRobotInfoSet

    @KTVRobotInfoSet.setter
    def KTVRobotInfoSet(self, KTVRobotInfoSet):
        self._KTVRobotInfoSet = KTVRobotInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KTVRobotInfoSet") is not None:
            self._KTVRobotInfoSet = []
            for item in params.get("KTVRobotInfoSet"):
                obj = KTVRobotInfo()
                obj._deserialize(item)
                self._KTVRobotInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVSuggestionsRequest(AbstractModel):
    """DescribeKTVSuggestions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _KeyWord: 搜索词。
        :type KeyWord: str
        """
        self._AppName = None
        self._UserId = None
        self._KeyWord = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def KeyWord(self):
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVSuggestionsResponse(AbstractModel):
    """DescribeKTVSuggestions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVSuggestionInfoSet: 联想词信息列表。
        :type KTVSuggestionInfoSet: list of KTVSuggestionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVSuggestionInfoSet = None
        self._RequestId = None

    @property
    def KTVSuggestionInfoSet(self):
        return self._KTVSuggestionInfoSet

    @KTVSuggestionInfoSet.setter
    def KTVSuggestionInfoSet(self, KTVSuggestionInfoSet):
        self._KTVSuggestionInfoSet = KTVSuggestionInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVSuggestionInfoSet") is not None:
            self._KTVSuggestionInfoSet = []
            for item in params.get("KTVSuggestionInfoSet"):
                obj = KTVSuggestionInfo()
                obj._deserialize(item)
                self._KTVSuggestionInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVTagsRequest(AbstractModel):
    """DescribeKTVTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        """
        self._AppName = None
        self._UserId = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVTagsResponse(AbstractModel):
    """DescribeKTVTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TagGroupInfoSet: 标签分组列表。
        :type TagGroupInfoSet: list of KTVTagGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TagGroupInfoSet = None
        self._RequestId = None

    @property
    def TagGroupInfoSet(self):
        return self._TagGroupInfoSet

    @TagGroupInfoSet.setter
    def TagGroupInfoSet(self, TagGroupInfoSet):
        self._TagGroupInfoSet = TagGroupInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TagGroupInfoSet") is not None:
            self._TagGroupInfoSet = []
            for item in params.get("TagGroupInfoSet"):
                obj = KTVTagGroupInfo()
                obj._deserialize(item)
                self._TagGroupInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveVipTradeInfosRequest(AbstractModel):
    """DescribeLiveVipTradeInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _StartTime: 直播会员充值下单起始时间，格式为 ISO。默认为当前时间前一天。
        :type StartTime: str
        :param _EndTime: 直播会员充值下单截止时间，格式为 ISO。默认为当前时间。 EndTime不能小于StartTime
        :type EndTime: str
        :param _TradeSerialNos: 交易流水号集合，匹配集合指定所有流水号 。
<li>数组长度限制：10。</li>
        :type TradeSerialNos: list of str
        :param _UserIds: 用户标识集合，匹配集合指定所有用户标识 。
<li>数组长度限制：10。</li>
        :type UserIds: list of str
        :param _Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：20，最大值：50。
        :type Limit: int
        """
        self._AppName = None
        self._StartTime = None
        self._EndTime = None
        self._TradeSerialNos = None
        self._UserIds = None
        self._Offset = None
        self._Limit = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TradeSerialNos(self):
        return self._TradeSerialNos

    @TradeSerialNos.setter
    def TradeSerialNos(self, TradeSerialNos):
        self._TradeSerialNos = TradeSerialNos

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TradeSerialNos = params.get("TradeSerialNos")
        self._UserIds = params.get("UserIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveVipTradeInfosResponse(AbstractModel):
    """DescribeLiveVipTradeInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveVipTradeInfoSet: 直播会员充值流水信息列表
        :type LiveVipTradeInfoSet: list of LiveVipTradeInfo
        :param _TotalCount: 直播会员充值流水总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LiveVipTradeInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LiveVipTradeInfoSet(self):
        return self._LiveVipTradeInfoSet

    @LiveVipTradeInfoSet.setter
    def LiveVipTradeInfoSet(self, LiveVipTradeInfoSet):
        self._LiveVipTradeInfoSet = LiveVipTradeInfoSet

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
        if params.get("LiveVipTradeInfoSet") is not None:
            self._LiveVipTradeInfoSet = []
            for item in params.get("LiveVipTradeInfoSet"):
                obj = LiveVipTradeInfo()
                obj._deserialize(item)
                self._LiveVipTradeInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        """
        self._AppName = None
        self._UserId = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户信息。
        :type UserInfo: :class:`tencentcloud.yinsuda.v20220527.models.UserInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserInfo = None
        self._RequestId = None

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = UserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._RequestId = params.get("RequestId")


class DestroyKTVRobotRequest(AbstractModel):
    """DestroyKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _RobotId: 机器人Id。
        :type RobotId: str
        """
        self._AppName = None
        self._UserId = None
        self._RobotId = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RobotId(self):
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._RobotId = params.get("RobotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyKTVRobotResponse(AbstractModel):
    """DestroyKTVRobot返回参数结构体

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


class JoinRoomInput(AbstractModel):
    """直播进房输入参数

    """

    def __init__(self):
        r"""
        :param _TRTCJoinRoomInput: TRTC进房参数
        :type TRTCJoinRoomInput: :class:`tencentcloud.yinsuda.v20220527.models.TRTCJoinRoomInput`
        """
        self._TRTCJoinRoomInput = None

    @property
    def TRTCJoinRoomInput(self):
        return self._TRTCJoinRoomInput

    @TRTCJoinRoomInput.setter
    def TRTCJoinRoomInput(self, TRTCJoinRoomInput):
        self._TRTCJoinRoomInput = TRTCJoinRoomInput


    def _deserialize(self, params):
        if params.get("TRTCJoinRoomInput") is not None:
            self._TRTCJoinRoomInput = TRTCJoinRoomInput()
            self._TRTCJoinRoomInput._deserialize(params.get("TRTCJoinRoomInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVBPMInfo(AbstractModel):
    """节拍信息。

    """

    def __init__(self):
        r"""
        :param _Type: 节拍类型，取值有：
<li>Slow：慢；</li>
<li>Middle：中等；</li>
<li>Fast：快；</li>
<li>Unknown：未知。</li>
        :type Type: str
        :param _Value: BPM 值。
        :type Value: int
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMatchMusic(AbstractModel):
    """匹配歌曲信息。

    """

    def __init__(self):
        r"""
        :param _KTVMusicBaseInfo: 匹配到的歌曲基础信息。
        :type KTVMusicBaseInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVMusicBaseInfo`
        :param _MatchRule: 命中规则。
        :type MatchRule: :class:`tencentcloud.yinsuda.v20220527.models.KTVMatchRule`
        :param _AMEMusicBaseInfo: AME 歌曲基础信息，仅在使用音速达歌曲 Id 匹配 AME 曲库时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AMEMusicBaseInfo: :class:`tencentcloud.yinsuda.v20220527.models.AMEMusicBaseInfo`
        """
        self._KTVMusicBaseInfo = None
        self._MatchRule = None
        self._AMEMusicBaseInfo = None

    @property
    def KTVMusicBaseInfo(self):
        return self._KTVMusicBaseInfo

    @KTVMusicBaseInfo.setter
    def KTVMusicBaseInfo(self, KTVMusicBaseInfo):
        self._KTVMusicBaseInfo = KTVMusicBaseInfo

    @property
    def MatchRule(self):
        return self._MatchRule

    @MatchRule.setter
    def MatchRule(self, MatchRule):
        self._MatchRule = MatchRule

    @property
    def AMEMusicBaseInfo(self):
        return self._AMEMusicBaseInfo

    @AMEMusicBaseInfo.setter
    def AMEMusicBaseInfo(self, AMEMusicBaseInfo):
        self._AMEMusicBaseInfo = AMEMusicBaseInfo


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self._KTVMusicBaseInfo = KTVMusicBaseInfo()
            self._KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        if params.get("MatchRule") is not None:
            self._MatchRule = KTVMatchRule()
            self._MatchRule._deserialize(params.get("MatchRule"))
        if params.get("AMEMusicBaseInfo") is not None:
            self._AMEMusicBaseInfo = AMEMusicBaseInfo()
            self._AMEMusicBaseInfo._deserialize(params.get("AMEMusicBaseInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMatchRule(AbstractModel):
    """歌曲匹配规则。

    """

    def __init__(self):
        r"""
        :param _AMEMusicId: AME 曲库 Id。
        :type AMEMusicId: str
        :param _MusicInfo: 歌曲匹配信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVMatchRuleMusicInfo`
        :param _MusicIdToMatchAME: 音速达歌曲 Id，用于匹配 AME 曲库歌曲。
        :type MusicIdToMatchAME: str
        """
        self._AMEMusicId = None
        self._MusicInfo = None
        self._MusicIdToMatchAME = None

    @property
    def AMEMusicId(self):
        return self._AMEMusicId

    @AMEMusicId.setter
    def AMEMusicId(self, AMEMusicId):
        self._AMEMusicId = AMEMusicId

    @property
    def MusicInfo(self):
        return self._MusicInfo

    @MusicInfo.setter
    def MusicInfo(self, MusicInfo):
        self._MusicInfo = MusicInfo

    @property
    def MusicIdToMatchAME(self):
        return self._MusicIdToMatchAME

    @MusicIdToMatchAME.setter
    def MusicIdToMatchAME(self, MusicIdToMatchAME):
        self._MusicIdToMatchAME = MusicIdToMatchAME


    def _deserialize(self, params):
        self._AMEMusicId = params.get("AMEMusicId")
        if params.get("MusicInfo") is not None:
            self._MusicInfo = KTVMatchRuleMusicInfo()
            self._MusicInfo._deserialize(params.get("MusicInfo"))
        self._MusicIdToMatchAME = params.get("MusicIdToMatchAME")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMatchRuleMusicInfo(AbstractModel):
    """歌曲信息匹配。

    """

    def __init__(self):
        r"""
        :param _MusicName: 歌曲名称。
        :type MusicName: str
        :param _SingerSet: 歌手列表。
        :type SingerSet: list of str
        """
        self._MusicName = None
        self._SingerSet = None

    @property
    def MusicName(self):
        return self._MusicName

    @MusicName.setter
    def MusicName(self, MusicName):
        self._MusicName = MusicName

    @property
    def SingerSet(self):
        return self._SingerSet

    @SingerSet.setter
    def SingerSet(self, SingerSet):
        self._SingerSet = SingerSet


    def _deserialize(self, params):
        self._MusicName = params.get("MusicName")
        self._SingerSet = params.get("SingerSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicBaseInfo(AbstractModel):
    """歌曲基础信息。

    """

    def __init__(self):
        r"""
        :param _MusicId: 歌曲Id。
        :type MusicId: str
        :param _Name: 歌曲名称。
        :type Name: str
        :param _SingerSet: 歌手名称。
        :type SingerSet: list of str
        :param _Duration: 播放时长。
        :type Duration: int
        :param _SingerImageUrl: 歌手图片链接。
        :type SingerImageUrl: str
        :param _AlbumInfo: 专辑信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumInfo: :class:`tencentcloud.yinsuda.v20220527.models.MusicAlbumInfo`
        :param _RightSet: 权益列表，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightSet: list of str
        :param _RecommendType: 推荐类型，取值有：
<li>Featured：精选；</li>
<li>Other：其他。</li>
        :type RecommendType: str
        """
        self._MusicId = None
        self._Name = None
        self._SingerSet = None
        self._Duration = None
        self._SingerImageUrl = None
        self._AlbumInfo = None
        self._RightSet = None
        self._RecommendType = None

    @property
    def MusicId(self):
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SingerSet(self):
        return self._SingerSet

    @SingerSet.setter
    def SingerSet(self, SingerSet):
        self._SingerSet = SingerSet

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def SingerImageUrl(self):
        return self._SingerImageUrl

    @SingerImageUrl.setter
    def SingerImageUrl(self, SingerImageUrl):
        self._SingerImageUrl = SingerImageUrl

    @property
    def AlbumInfo(self):
        return self._AlbumInfo

    @AlbumInfo.setter
    def AlbumInfo(self, AlbumInfo):
        self._AlbumInfo = AlbumInfo

    @property
    def RightSet(self):
        return self._RightSet

    @RightSet.setter
    def RightSet(self, RightSet):
        self._RightSet = RightSet

    @property
    def RecommendType(self):
        return self._RecommendType

    @RecommendType.setter
    def RecommendType(self, RecommendType):
        self._RecommendType = RecommendType


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._Name = params.get("Name")
        self._SingerSet = params.get("SingerSet")
        self._Duration = params.get("Duration")
        self._SingerImageUrl = params.get("SingerImageUrl")
        if params.get("AlbumInfo") is not None:
            self._AlbumInfo = MusicAlbumInfo()
            self._AlbumInfo._deserialize(params.get("AlbumInfo"))
        self._RightSet = params.get("RightSet")
        self._RecommendType = params.get("RecommendType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicDetailInfo(AbstractModel):
    """歌曲详细信息。

    """

    def __init__(self):
        r"""
        :param _KTVMusicBaseInfo: 歌曲基础信息。
        :type KTVMusicBaseInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVMusicBaseInfo`
        :param _PlayToken: 播放凭证。
        :type PlayToken: str
        :param _LyricsUrl: 歌词下载链接。
        :type LyricsUrl: str
        :param _MidiUrl: 音高数据下载链接。
        :type MidiUrl: str
        :param _ChorusClipSet: 副歌片段信息。
        :type ChorusClipSet: list of ChorusClip
        :param _PreludeInterval: 前奏间隔。
        :type PreludeInterval: int
        :param _GenreSet: 歌曲流派列表。
        :type GenreSet: list of str
        :param _BPMInfo: 节拍信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BPMInfo: :class:`tencentcloud.yinsuda.v20220527.models.KTVBPMInfo`
        """
        self._KTVMusicBaseInfo = None
        self._PlayToken = None
        self._LyricsUrl = None
        self._MidiUrl = None
        self._ChorusClipSet = None
        self._PreludeInterval = None
        self._GenreSet = None
        self._BPMInfo = None

    @property
    def KTVMusicBaseInfo(self):
        return self._KTVMusicBaseInfo

    @KTVMusicBaseInfo.setter
    def KTVMusicBaseInfo(self, KTVMusicBaseInfo):
        self._KTVMusicBaseInfo = KTVMusicBaseInfo

    @property
    def PlayToken(self):
        return self._PlayToken

    @PlayToken.setter
    def PlayToken(self, PlayToken):
        self._PlayToken = PlayToken

    @property
    def LyricsUrl(self):
        return self._LyricsUrl

    @LyricsUrl.setter
    def LyricsUrl(self, LyricsUrl):
        self._LyricsUrl = LyricsUrl

    @property
    def MidiUrl(self):
        return self._MidiUrl

    @MidiUrl.setter
    def MidiUrl(self, MidiUrl):
        self._MidiUrl = MidiUrl

    @property
    def ChorusClipSet(self):
        return self._ChorusClipSet

    @ChorusClipSet.setter
    def ChorusClipSet(self, ChorusClipSet):
        self._ChorusClipSet = ChorusClipSet

    @property
    def PreludeInterval(self):
        return self._PreludeInterval

    @PreludeInterval.setter
    def PreludeInterval(self, PreludeInterval):
        self._PreludeInterval = PreludeInterval

    @property
    def GenreSet(self):
        return self._GenreSet

    @GenreSet.setter
    def GenreSet(self, GenreSet):
        self._GenreSet = GenreSet

    @property
    def BPMInfo(self):
        return self._BPMInfo

    @BPMInfo.setter
    def BPMInfo(self, BPMInfo):
        self._BPMInfo = BPMInfo


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self._KTVMusicBaseInfo = KTVMusicBaseInfo()
            self._KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        self._PlayToken = params.get("PlayToken")
        self._LyricsUrl = params.get("LyricsUrl")
        self._MidiUrl = params.get("MidiUrl")
        if params.get("ChorusClipSet") is not None:
            self._ChorusClipSet = []
            for item in params.get("ChorusClipSet"):
                obj = ChorusClip()
                obj._deserialize(item)
                self._ChorusClipSet.append(obj)
        self._PreludeInterval = params.get("PreludeInterval")
        self._GenreSet = params.get("GenreSet")
        if params.get("BPMInfo") is not None:
            self._BPMInfo = KTVBPMInfo()
            self._BPMInfo._deserialize(params.get("BPMInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVOtherSegments(AbstractModel):
    """其它片段时间（可用于抢唱）

    """

    def __init__(self):
        r"""
        :param _SegmentBegin: 片段开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentBegin: int
        :param _SegmentEnd: 片段结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentEnd: int
        """
        self._SegmentBegin = None
        self._SegmentEnd = None

    @property
    def SegmentBegin(self):
        return self._SegmentBegin

    @SegmentBegin.setter
    def SegmentBegin(self, SegmentBegin):
        self._SegmentBegin = SegmentBegin

    @property
    def SegmentEnd(self):
        return self._SegmentEnd

    @SegmentEnd.setter
    def SegmentEnd(self, SegmentEnd):
        self._SegmentEnd = SegmentEnd


    def _deserialize(self, params):
        self._SegmentBegin = params.get("SegmentBegin")
        self._SegmentEnd = params.get("SegmentEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVPlaylistBaseInfo(AbstractModel):
    """歌单基础信息。

    """

    def __init__(self):
        r"""
        :param _PlaylistId: 歌单Id。
        :type PlaylistId: str
        :param _Title: 歌单标题。
        :type Title: str
        """
        self._PlaylistId = None
        self._Title = None

    @property
    def PlaylistId(self):
        return self._PlaylistId

    @PlaylistId.setter
    def PlaylistId(self, PlaylistId):
        self._PlaylistId = PlaylistId

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._PlaylistId = params.get("PlaylistId")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVRobotInfo(AbstractModel):
    """机器人信息

    """

    def __init__(self):
        r"""
        :param _RobotId: 机器人Id。
        :type RobotId: str
        :param _Status: 状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :type Status: str
        :param _Playlists: 播放列表。
        :type Playlists: list of str
        :param _CurIndex: 当前歌单索引位置。
        :type CurIndex: int
        :param _Position: 播放进度，单位：毫秒。
        :type Position: int
        :param _SetAudioParamInput: 音频参数。
        :type SetAudioParamInput: :class:`tencentcloud.yinsuda.v20220527.models.SetAudioParamCommandInput`
        :param _JoinRoomInput: 进房信息。
        :type JoinRoomInput: :class:`tencentcloud.yinsuda.v20220527.models.JoinRoomInput`
        :param _RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        :param _SetPlayModeInput: 播放模式，PlayMode取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :type SetPlayModeInput: :class:`tencentcloud.yinsuda.v20220527.models.SetPlayModeCommandInput`
        """
        self._RobotId = None
        self._Status = None
        self._Playlists = None
        self._CurIndex = None
        self._Position = None
        self._SetAudioParamInput = None
        self._JoinRoomInput = None
        self._RTCSystem = None
        self._SetPlayModeInput = None

    @property
    def RobotId(self):
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Playlists(self):
        return self._Playlists

    @Playlists.setter
    def Playlists(self, Playlists):
        self._Playlists = Playlists

    @property
    def CurIndex(self):
        return self._CurIndex

    @CurIndex.setter
    def CurIndex(self, CurIndex):
        self._CurIndex = CurIndex

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def SetAudioParamInput(self):
        return self._SetAudioParamInput

    @SetAudioParamInput.setter
    def SetAudioParamInput(self, SetAudioParamInput):
        self._SetAudioParamInput = SetAudioParamInput

    @property
    def JoinRoomInput(self):
        return self._JoinRoomInput

    @JoinRoomInput.setter
    def JoinRoomInput(self, JoinRoomInput):
        self._JoinRoomInput = JoinRoomInput

    @property
    def RTCSystem(self):
        return self._RTCSystem

    @RTCSystem.setter
    def RTCSystem(self, RTCSystem):
        self._RTCSystem = RTCSystem

    @property
    def SetPlayModeInput(self):
        return self._SetPlayModeInput

    @SetPlayModeInput.setter
    def SetPlayModeInput(self, SetPlayModeInput):
        self._SetPlayModeInput = SetPlayModeInput


    def _deserialize(self, params):
        self._RobotId = params.get("RobotId")
        self._Status = params.get("Status")
        self._Playlists = params.get("Playlists")
        self._CurIndex = params.get("CurIndex")
        self._Position = params.get("Position")
        if params.get("SetAudioParamInput") is not None:
            self._SetAudioParamInput = SetAudioParamCommandInput()
            self._SetAudioParamInput._deserialize(params.get("SetAudioParamInput"))
        if params.get("JoinRoomInput") is not None:
            self._JoinRoomInput = JoinRoomInput()
            self._JoinRoomInput._deserialize(params.get("JoinRoomInput"))
        self._RTCSystem = params.get("RTCSystem")
        if params.get("SetPlayModeInput") is not None:
            self._SetPlayModeInput = SetPlayModeCommandInput()
            self._SetPlayModeInput._deserialize(params.get("SetPlayModeInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVSuggestionInfo(AbstractModel):
    """联想词信息。

    """

    def __init__(self):
        r"""
        :param _Suggestion: 联想词。
        :type Suggestion: str
        """
        self._Suggestion = None

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion


    def _deserialize(self, params):
        self._Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVTagGroupInfo(AbstractModel):
    """标签分组信息。

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组 Id。
        :type GroupId: str
        :param _Name: 分组名。
        :type Name: str
        :param _TagInfoSet: 标签列表。
        :type TagInfoSet: list of KTVTagInfo
        """
        self._GroupId = None
        self._Name = None
        self._TagInfoSet = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TagInfoSet(self):
        return self._TagInfoSet

    @TagInfoSet.setter
    def TagInfoSet(self, TagInfoSet):
        self._TagInfoSet = TagInfoSet


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        if params.get("TagInfoSet") is not None:
            self._TagInfoSet = []
            for item in params.get("TagInfoSet"):
                obj = KTVTagInfo()
                obj._deserialize(item)
                self._TagInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVTagInfo(AbstractModel):
    """标签信息。

    """

    def __init__(self):
        r"""
        :param _TagId: 标签 Id。
        :type TagId: str
        :param _Name: 标签名称。
        :type Name: str
        """
        self._TagId = None
        self._Name = None

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._TagId = params.get("TagId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveVipTradeInfo(AbstractModel):
    """充值直播会员流水信息

    """

    def __init__(self):
        r"""
        :param _TradeSerialNo: 交易流水号。
        :type TradeSerialNo: str
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _RoomId: 房间标识。
        :type RoomId: str
        :param _VipDays: 充值会员天数。
取值有： 
<li>31</li> <li>93</li><li>186</li> <li>372</li>
        :type VipDays: int
        :param _Status: 订单状态。 
取值有： 
<li>Success：成功</li><li>Fail：失败</li><li>Processing：订单处理中</li>
        :type Status: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        """
        self._TradeSerialNo = None
        self._AppName = None
        self._UserId = None
        self._RoomId = None
        self._VipDays = None
        self._Status = None
        self._CreateTime = None

    @property
    def TradeSerialNo(self):
        return self._TradeSerialNo

    @TradeSerialNo.setter
    def TradeSerialNo(self, TradeSerialNo):
        self._TradeSerialNo = TradeSerialNo

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def VipDays(self):
        return self._VipDays

    @VipDays.setter
    def VipDays(self, VipDays):
        self._VipDays = VipDays

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TradeSerialNo = params.get("TradeSerialNo")
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._VipDays = params.get("VipDays")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveVipUserInfo(AbstractModel):
    """直播会员用户信息

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间标识。
        :type RoomId: str
        :param _LiveVipEndTime: 直播会员结束时间。
        :type LiveVipEndTime: str
        :param _LiveVipStatus: 会员生效状态
<li>Valid：生效</li><li>Invalid：无效</li>
        :type LiveVipStatus: str
        """
        self._RoomId = None
        self._LiveVipEndTime = None
        self._LiveVipStatus = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def LiveVipEndTime(self):
        return self._LiveVipEndTime

    @LiveVipEndTime.setter
    def LiveVipEndTime(self, LiveVipEndTime):
        self._LiveVipEndTime = LiveVipEndTime

    @property
    def LiveVipStatus(self):
        return self._LiveVipStatus

    @LiveVipStatus.setter
    def LiveVipStatus(self, LiveVipStatus):
        self._LiveVipStatus = LiveVipStatus


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._LiveVipEndTime = params.get("LiveVipEndTime")
        self._LiveVipStatus = params.get("LiveVipStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicAlbumCoverInfo(AbstractModel):
    """歌曲专辑封面信息。

    """

    def __init__(self):
        r"""
        :param _Dimension: 尺寸规格，取值有：
<li>Mini：150 x 150 尺寸；</li>
<li>Small：240 x 240 尺寸；</li>
<li>Medium：480 x 480 尺寸。</li>
        :type Dimension: str
        :param _Url: 下载链接。
        :type Url: str
        """
        self._Dimension = None
        self._Url = None

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Dimension = params.get("Dimension")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicAlbumInfo(AbstractModel):
    """歌曲专辑信息。

    """

    def __init__(self):
        r"""
        :param _Name: 专辑名称。
        :type Name: str
        :param _CoverInfoSet: 封面列表。
        :type CoverInfoSet: list of MusicAlbumCoverInfo
        """
        self._Name = None
        self._CoverInfoSet = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CoverInfoSet(self):
        return self._CoverInfoSet

    @CoverInfoSet.setter
    def CoverInfoSet(self, CoverInfoSet):
        self._CoverInfoSet = CoverInfoSet


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("CoverInfoSet") is not None:
            self._CoverInfoSet = []
            for item in params.get("CoverInfoSet"):
                obj = MusicAlbumCoverInfo()
                obj._deserialize(item)
                self._CoverInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayCommandInput(AbstractModel):
    """播放指令输入参数

    """

    def __init__(self):
        r"""
        :param _Index: 歌曲位置索引。
        :type Index: int
        """
        self._Index = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeLiveVipRequest(AbstractModel):
    """RechargeLiveVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _TradeSerialNo: 交易流水号，用于标记此次充值记录，多次充值记录传入相同的 TradeSerialNo 会判断为失败，可用于防止重提提交造成重复计费。
        :type TradeSerialNo: str
        :param _RoomId: 房间标识。
        :type RoomId: str
        :param _VipDays: 充值会员天数。
取值有：
<li>31</li>
<li>93</li>
<li>186</li>
<li>372</li>
        :type VipDays: int
        :param _GiveType: 充值分类。取值有：room_card-包月房卡; 其他-保留。
        :type GiveType: str
        :param _PlayScene: 播放场景。默认为Live
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        """
        self._AppName = None
        self._UserId = None
        self._TradeSerialNo = None
        self._RoomId = None
        self._VipDays = None
        self._GiveType = None
        self._PlayScene = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TradeSerialNo(self):
        return self._TradeSerialNo

    @TradeSerialNo.setter
    def TradeSerialNo(self, TradeSerialNo):
        self._TradeSerialNo = TradeSerialNo

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def VipDays(self):
        return self._VipDays

    @VipDays.setter
    def VipDays(self, VipDays):
        self._VipDays = VipDays

    @property
    def GiveType(self):
        return self._GiveType

    @GiveType.setter
    def GiveType(self, GiveType):
        self._GiveType = GiveType

    @property
    def PlayScene(self):
        return self._PlayScene

    @PlayScene.setter
    def PlayScene(self, PlayScene):
        self._PlayScene = PlayScene


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._TradeSerialNo = params.get("TradeSerialNo")
        self._RoomId = params.get("RoomId")
        self._VipDays = params.get("VipDays")
        self._GiveType = params.get("GiveType")
        self._PlayScene = params.get("PlayScene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeLiveVipResponse(AbstractModel):
    """RechargeLiveVip返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveVipUserInfo: 直播会员信息。
        :type LiveVipUserInfo: :class:`tencentcloud.yinsuda.v20220527.models.LiveVipUserInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LiveVipUserInfo = None
        self._RequestId = None

    @property
    def LiveVipUserInfo(self):
        return self._LiveVipUserInfo

    @LiveVipUserInfo.setter
    def LiveVipUserInfo(self, LiveVipUserInfo):
        self._LiveVipUserInfo = LiveVipUserInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LiveVipUserInfo") is not None:
            self._LiveVipUserInfo = LiveVipUserInfo()
            self._LiveVipUserInfo._deserialize(params.get("LiveVipUserInfo"))
        self._RequestId = params.get("RequestId")


class SearchKTVMusicsRequest(AbstractModel):
    """SearchKTVMusics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _KeyWord: 关键词。
        :type KeyWord: str
        :param _ScrollToken: 滚动标记。
        :type ScrollToken: str
        :param _Limit: 返回条数限制，默认 20，最大 50.
        :type Limit: int
        :param _RightFilters: 权益过滤，取值有：
<li>Play：可播；</li>
<li>Sing：可唱。</li>
        :type RightFilters: list of str
        :param _PlayScene: 播放场景。默认为Chat
<li>Live：直播</li><li>Chat：语聊</li>
        :type PlayScene: str
        :param _MaterialFilters: 物料过滤，取值有：
<li>Lyrics：含有歌词；</li>
<li>Midi：含有音高线。</li>
        :type MaterialFilters: list of str
        """
        self._AppName = None
        self._UserId = None
        self._KeyWord = None
        self._ScrollToken = None
        self._Limit = None
        self._RightFilters = None
        self._PlayScene = None
        self._MaterialFilters = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def KeyWord(self):
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RightFilters(self):
        return self._RightFilters

    @RightFilters.setter
    def RightFilters(self, RightFilters):
        self._RightFilters = RightFilters

    @property
    def PlayScene(self):
        return self._PlayScene

    @PlayScene.setter
    def PlayScene(self, PlayScene):
        self._PlayScene = PlayScene

    @property
    def MaterialFilters(self):
        return self._MaterialFilters

    @MaterialFilters.setter
    def MaterialFilters(self, MaterialFilters):
        self._MaterialFilters = MaterialFilters


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._KeyWord = params.get("KeyWord")
        self._ScrollToken = params.get("ScrollToken")
        self._Limit = params.get("Limit")
        self._RightFilters = params.get("RightFilters")
        self._PlayScene = params.get("PlayScene")
        self._MaterialFilters = params.get("MaterialFilters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKTVMusicsResponse(AbstractModel):
    """SearchKTVMusics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicInfoSet: 歌曲信息列表。
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param _ScrollToken: 滚动标记，用于设置下次请求的 ScrollToken 参数。
        :type ScrollToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicInfoSet = None
        self._ScrollToken = None
        self._RequestId = None

    @property
    def KTVMusicInfoSet(self):
        return self._KTVMusicInfoSet

    @KTVMusicInfoSet.setter
    def KTVMusicInfoSet(self, KTVMusicInfoSet):
        self._KTVMusicInfoSet = KTVMusicInfoSet

    @property
    def ScrollToken(self):
        return self._ScrollToken

    @ScrollToken.setter
    def ScrollToken(self, ScrollToken):
        self._ScrollToken = ScrollToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicInfoSet") is not None:
            self._KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self._KTVMusicInfoSet.append(obj)
        self._ScrollToken = params.get("ScrollToken")
        self._RequestId = params.get("RequestId")


class SeekCommandInput(AbstractModel):
    """调整播放进度指令参数

    """

    def __init__(self):
        r"""
        :param _Position: 播放位置，单位：毫秒。
        :type Position: int
        """
        self._Position = None

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position


    def _deserialize(self, params):
        self._Position = params.get("Position")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageCommandInput(AbstractModel):
    """发送自定义信息指令参数

    """

    def __init__(self):
        r"""
        :param _Message: 自定义消息，json格式字符串。
        :type Message: str
        :param _Repeat: 消息重复次数，默认为 1。
        :type Repeat: int
        """
        self._Message = None
        self._Repeat = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Repeat(self):
        return self._Repeat

    @Repeat.setter
    def Repeat(self, Repeat):
        self._Repeat = Repeat


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Repeat = params.get("Repeat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAudioParamCommandInput(AbstractModel):
    """音频参数信息

    """

    def __init__(self):
        r"""
        :param _Type: 音频类型，取值有：
<li>Original：原唱</li>
<li>Accompaniment：伴奏</li>
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDestroyModeCommandInput(AbstractModel):
    """设置销毁模式

    """

    def __init__(self):
        r"""
        :param _DestroyMode: 销毁模式，取值有：
<li>Auto：房间没人时自动销毁</li>
<li>Expire：房间没人时过期自动销毁</li>
<li>Never：不自动销毁，需手动销毁</li>默认为：Auto。
        :type DestroyMode: str
        :param _DestroyExpireTime: 过期销毁时间，单位：秒，当DestroyMode取Expire时必填。
        :type DestroyExpireTime: int
        """
        self._DestroyMode = None
        self._DestroyExpireTime = None

    @property
    def DestroyMode(self):
        return self._DestroyMode

    @DestroyMode.setter
    def DestroyMode(self, DestroyMode):
        self._DestroyMode = DestroyMode

    @property
    def DestroyExpireTime(self):
        return self._DestroyExpireTime

    @DestroyExpireTime.setter
    def DestroyExpireTime(self, DestroyExpireTime):
        self._DestroyExpireTime = DestroyExpireTime


    def _deserialize(self, params):
        self._DestroyMode = params.get("DestroyMode")
        self._DestroyExpireTime = params.get("DestroyExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPlayModeCommandInput(AbstractModel):
    """设置播放模式

    """

    def __init__(self):
        r"""
        :param _PlayMode: 播放模式，取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :type PlayMode: str
        """
        self._PlayMode = None

    @property
    def PlayMode(self):
        return self._PlayMode

    @PlayMode.setter
    def PlayMode(self, PlayMode):
        self._PlayMode = PlayMode


    def _deserialize(self, params):
        self._PlayMode = params.get("PlayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPlaylistCommandInput(AbstractModel):
    """设置播放列表指令参数

    """

    def __init__(self):
        r"""
        :param _Type: 变更类型，取值有：
<li>Add：添加</li>
<li>Delete：删除</li>
<li>ClearList：清空歌曲列表</li>
<li>Move：移动歌曲</li>
        :type Type: str
        :param _Index: 歌单索引位置，
当 Type 取 Add 时，-1表示添加在列表最后位置，大于-1表示要添加的位置；
当 Type 取 Delete 时，表示待删除歌曲的位置；
当 Type 取 Move 时，表示待调整歌曲的位置。
        :type Index: int
        :param _ChangedIndex: 当 Type 取 Move 时，必填，表示移动歌曲的目标位置。
        :type ChangedIndex: int
        :param _MusicIds: 歌曲 ID 列表，当 Type 取 Add 时，必填。
        :type MusicIds: list of str
        """
        self._Type = None
        self._Index = None
        self._ChangedIndex = None
        self._MusicIds = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def ChangedIndex(self):
        return self._ChangedIndex

    @ChangedIndex.setter
    def ChangedIndex(self, ChangedIndex):
        self._ChangedIndex = ChangedIndex

    @property
    def MusicIds(self):
        return self._MusicIds

    @MusicIds.setter
    def MusicIds(self, MusicIds):
        self._MusicIds = MusicIds


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Index = params.get("Index")
        self._ChangedIndex = params.get("ChangedIndex")
        self._MusicIds = params.get("MusicIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncKTVRobotCommandRequest(AbstractModel):
    """SyncKTVRobotCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _RobotId: 机器人Id。
        :type RobotId: str
        :param _SyncRobotCommands: 指令及指令参数数组。
        :type SyncRobotCommands: list of SyncRobotCommand
        """
        self._AppName = None
        self._UserId = None
        self._RobotId = None
        self._SyncRobotCommands = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RobotId(self):
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId

    @property
    def SyncRobotCommands(self):
        return self._SyncRobotCommands

    @SyncRobotCommands.setter
    def SyncRobotCommands(self, SyncRobotCommands):
        self._SyncRobotCommands = SyncRobotCommands


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        self._RobotId = params.get("RobotId")
        if params.get("SyncRobotCommands") is not None:
            self._SyncRobotCommands = []
            for item in params.get("SyncRobotCommands"):
                obj = SyncRobotCommand()
                obj._deserialize(item)
                self._SyncRobotCommands.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncKTVRobotCommandResponse(AbstractModel):
    """SyncKTVRobotCommand返回参数结构体

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


class SyncRobotCommand(AbstractModel):
    """KTV 机器人初始化参数，在创建后自动完成相关初始化工作。

    """

    def __init__(self):
        r"""
        :param _Command: 可同时传入多个指令，顺序执行。取值有：
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
        :param _PlayCommandInput: 播放参数。
        :type PlayCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.PlayCommandInput`
        :param _SetPlaylistCommandInput: 播放列表变更信息，当Command取SetPlaylist时，必填。
        :type SetPlaylistCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetPlaylistCommandInput`
        :param _SeekCommandInput: 播放进度，当Command取Seek时，必填。
        :type SeekCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SeekCommandInput`
        :param _SetAudioParamCommandInput: 音频参数，当Command取SetAudioParam时，必填。
        :type SetAudioParamCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetAudioParamCommandInput`
        :param _SendMessageCommandInput: 自定义消息，当Command取SendMessage时，必填。
        :type SendMessageCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SendMessageCommandInput`
        :param _SetPlayModeCommandInput: 播放模式，当Command取SetPlayMode时，必填。
        :type SetPlayModeCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetPlayModeCommandInput`
        :param _SetDestroyModeCommandInput: 销毁模式，当Command取SetDestroyMode时，必填。
        :type SetDestroyModeCommandInput: :class:`tencentcloud.yinsuda.v20220527.models.SetDestroyModeCommandInput`
        """
        self._Command = None
        self._PlayCommandInput = None
        self._SetPlaylistCommandInput = None
        self._SeekCommandInput = None
        self._SetAudioParamCommandInput = None
        self._SendMessageCommandInput = None
        self._SetPlayModeCommandInput = None
        self._SetDestroyModeCommandInput = None

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def PlayCommandInput(self):
        return self._PlayCommandInput

    @PlayCommandInput.setter
    def PlayCommandInput(self, PlayCommandInput):
        self._PlayCommandInput = PlayCommandInput

    @property
    def SetPlaylistCommandInput(self):
        return self._SetPlaylistCommandInput

    @SetPlaylistCommandInput.setter
    def SetPlaylistCommandInput(self, SetPlaylistCommandInput):
        self._SetPlaylistCommandInput = SetPlaylistCommandInput

    @property
    def SeekCommandInput(self):
        return self._SeekCommandInput

    @SeekCommandInput.setter
    def SeekCommandInput(self, SeekCommandInput):
        self._SeekCommandInput = SeekCommandInput

    @property
    def SetAudioParamCommandInput(self):
        return self._SetAudioParamCommandInput

    @SetAudioParamCommandInput.setter
    def SetAudioParamCommandInput(self, SetAudioParamCommandInput):
        self._SetAudioParamCommandInput = SetAudioParamCommandInput

    @property
    def SendMessageCommandInput(self):
        return self._SendMessageCommandInput

    @SendMessageCommandInput.setter
    def SendMessageCommandInput(self, SendMessageCommandInput):
        self._SendMessageCommandInput = SendMessageCommandInput

    @property
    def SetPlayModeCommandInput(self):
        return self._SetPlayModeCommandInput

    @SetPlayModeCommandInput.setter
    def SetPlayModeCommandInput(self, SetPlayModeCommandInput):
        self._SetPlayModeCommandInput = SetPlayModeCommandInput

    @property
    def SetDestroyModeCommandInput(self):
        return self._SetDestroyModeCommandInput

    @SetDestroyModeCommandInput.setter
    def SetDestroyModeCommandInput(self, SetDestroyModeCommandInput):
        self._SetDestroyModeCommandInput = SetDestroyModeCommandInput


    def _deserialize(self, params):
        self._Command = params.get("Command")
        if params.get("PlayCommandInput") is not None:
            self._PlayCommandInput = PlayCommandInput()
            self._PlayCommandInput._deserialize(params.get("PlayCommandInput"))
        if params.get("SetPlaylistCommandInput") is not None:
            self._SetPlaylistCommandInput = SetPlaylistCommandInput()
            self._SetPlaylistCommandInput._deserialize(params.get("SetPlaylistCommandInput"))
        if params.get("SeekCommandInput") is not None:
            self._SeekCommandInput = SeekCommandInput()
            self._SeekCommandInput._deserialize(params.get("SeekCommandInput"))
        if params.get("SetAudioParamCommandInput") is not None:
            self._SetAudioParamCommandInput = SetAudioParamCommandInput()
            self._SetAudioParamCommandInput._deserialize(params.get("SetAudioParamCommandInput"))
        if params.get("SendMessageCommandInput") is not None:
            self._SendMessageCommandInput = SendMessageCommandInput()
            self._SendMessageCommandInput._deserialize(params.get("SendMessageCommandInput"))
        if params.get("SetPlayModeCommandInput") is not None:
            self._SetPlayModeCommandInput = SetPlayModeCommandInput()
            self._SetPlayModeCommandInput._deserialize(params.get("SetPlayModeCommandInput"))
        if params.get("SetDestroyModeCommandInput") is not None:
            self._SetDestroyModeCommandInput = SetDestroyModeCommandInput()
            self._SetDestroyModeCommandInput._deserialize(params.get("SetDestroyModeCommandInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TRTCJoinRoomInput(AbstractModel):
    """TRTC推流进房信息

    """

    def __init__(self):
        r"""
        :param _Sign: 签名。
        :type Sign: str
        :param _RoomId: 房间号。
        :type RoomId: str
        :param _SdkAppId: 推流应用ID。
        :type SdkAppId: str
        :param _UserId: 用户唯一标识。
        :type UserId: str
        :param _RoomIdType: TRTC房间号的类型：

Integer：数字类型
String：字符串类型
默认为：Integer 。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomIdType: str
        """
        self._Sign = None
        self._RoomId = None
        self._SdkAppId = None
        self._UserId = None
        self._RoomIdType = None

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomIdType(self):
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType


    def _deserialize(self, params):
        self._Sign = params.get("Sign")
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._RoomIdType = params.get("RoomIdType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeRange(AbstractModel):
    """时间范围

    """

    def __init__(self):
        r"""
        :param _Before: <li>大于等于此时间（起始时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :type Before: str
        :param _After: <li>小于此时间（结束时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :type After: str
        """
        self._Before = None
        self._After = None

    @property
    def Before(self):
        return self._Before

    @Before.setter
    def Before(self, Before):
        self._Before = Before

    @property
    def After(self):
        return self._After

    @After.setter
    def After(self, After):
        self._After = After


    def _deserialize(self, params):
        self._Before = params.get("Before")
        self._After = params.get("After")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _UserId: 用户标识。
        :type UserId: str
        :param _LiveVipUserInfo: 直播会员详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveVipUserInfo: :class:`tencentcloud.yinsuda.v20220527.models.LiveVipUserInfo`
        :param _UserType: 用户类型
<li>Normal：普通用户</li>
<li>LiveVip：直播会员用户</li>
        :type UserType: str
        """
        self._AppName = None
        self._UserId = None
        self._LiveVipUserInfo = None
        self._UserType = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def LiveVipUserInfo(self):
        return self._LiveVipUserInfo

    @LiveVipUserInfo.setter
    def LiveVipUserInfo(self, LiveVipUserInfo):
        self._LiveVipUserInfo = LiveVipUserInfo

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._UserId = params.get("UserId")
        if params.get("LiveVipUserInfo") is not None:
            self._LiveVipUserInfo = LiveVipUserInfo()
            self._LiveVipUserInfo._deserialize(params.get("LiveVipUserInfo"))
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        