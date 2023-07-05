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


class ChangeRoomPlayerProfileRequest(AbstractModel):
    """ChangeRoomPlayerProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏资源Id。
        :type GameId: str
        :param _PlayerId: 发起修改的玩家Id。
        :type PlayerId: str
        :param _CustomProfile: 需要修改的玩家自定义属性。
        :type CustomProfile: str
        """
        self._GameId = None
        self._PlayerId = None
        self._CustomProfile = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def CustomProfile(self):
        return self._CustomProfile

    @CustomProfile.setter
    def CustomProfile(self, CustomProfile):
        self._CustomProfile = CustomProfile


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._PlayerId = params.get("PlayerId")
        self._CustomProfile = params.get("CustomProfile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeRoomPlayerProfileResponse(AbstractModel):
    """ChangeRoomPlayerProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Room: 房间信息。
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Room = None
        self._RequestId = None

    @property
    def Room(self):
        return self._Room

    @Room.setter
    def Room(self, Room):
        self._Room = Room

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self._Room = Room()
            self._Room._deserialize(params.get("Room"))
        self._RequestId = params.get("RequestId")


class ChangeRoomPlayerStatusRequest(AbstractModel):
    """ChangeRoomPlayerStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏资源Id。
        :type GameId: str
        :param _CustomStatus: 玩家自定义状态。
        :type CustomStatus: int
        :param _PlayerId: 玩家id。
        :type PlayerId: str
        """
        self._GameId = None
        self._CustomStatus = None
        self._PlayerId = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def CustomStatus(self):
        return self._CustomStatus

    @CustomStatus.setter
    def CustomStatus(self, CustomStatus):
        self._CustomStatus = CustomStatus

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._CustomStatus = params.get("CustomStatus")
        self._PlayerId = params.get("PlayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeRoomPlayerStatusResponse(AbstractModel):
    """ChangeRoomPlayerStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Room: 房间信息
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Room = None
        self._RequestId = None

    @property
    def Room(self):
        return self._Room

    @Room.setter
    def Room(self, Room):
        self._Room = Room

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self._Room = Room()
            self._Room._deserialize(params.get("Room"))
        self._RequestId = params.get("RequestId")


class DescribePlayerRequest(AbstractModel):
    """DescribePlayer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏资源Id。
        :type GameId: str
        :param _OpenId: 玩家OpenId。
        :type OpenId: str
        :param _PlayerId: 玩家PlayerId，由后台分配，当OpenId不传的时候，PlayerId必传，传入PlayerId可以查询当前PlayerId的玩家信息，当OpenId传入的时候，PlayerId可不传，按照OpenId查询玩家信息。
        :type PlayerId: str
        """
        self._GameId = None
        self._OpenId = None
        self._PlayerId = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._OpenId = params.get("OpenId")
        self._PlayerId = params.get("PlayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayerResponse(AbstractModel):
    """DescribePlayer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Player: 玩家信息。
        :type Player: :class:`tencentcloud.mgobe.v20201014.models.Player`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Player = None
        self._RequestId = None

    @property
    def Player(self):
        return self._Player

    @Player.setter
    def Player(self, Player):
        self._Player = Player

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Player") is not None:
            self._Player = Player()
            self._Player._deserialize(params.get("Player"))
        self._RequestId = params.get("RequestId")


class DescribeRoomRequest(AbstractModel):
    """DescribeRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏资源Id。
        :type GameId: str
        :param _PlayerId: 玩家Id。当房间Id不传的时候，玩家Id必传，传入玩家Id可以查询当前玩家所在的房间信息，当房间Id传入的时候，优先按照房间Id查询房间信息。
        :type PlayerId: str
        :param _RoomId: 房间Id。
        :type RoomId: str
        """
        self._GameId = None
        self._PlayerId = None
        self._RoomId = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._PlayerId = params.get("PlayerId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomResponse(AbstractModel):
    """DescribeRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Room: 房间信息。
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Room = None
        self._RequestId = None

    @property
    def Room(self):
        return self._Room

    @Room.setter
    def Room(self, Room):
        self._Room = Room

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self._Room = Room()
            self._Room._deserialize(params.get("Room"))
        self._RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 表示游戏资源唯一 ID, 由后台自动分配, 无法修改。
        :type GameId: str
        :param _RoomId: 表示游戏房间唯一ID。
        :type RoomId: str
        """
        self._GameId = None
        self._RoomId = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    """DismissRoom返回参数结构体

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


class ModifyRoomRequest(AbstractModel):
    """ModifyRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏资源Id。
        :type GameId: str
        :param _RoomId: 房间ID。
        :type RoomId: str
        :param _PlayerId: 发起者的PlayerId。
        :type PlayerId: str
        :param _ChangeRoomOptionList: 需要修改的房间选项，0表示房间名称，1表示房主，2表示是否允许观战，3表示是否支持邀请码/密码，4表示是否私有，5表示是否自定义房间属性，6表示是否禁止加人。
        :type ChangeRoomOptionList: list of int
        :param _RoomName: 房间名称。
        :type RoomName: str
        :param _Owner: 变更房主。
        :type Owner: str
        :param _IsViewed: 是否支持观战。
        :type IsViewed: bool
        :param _IsInvited: 是否支持邀请码/密码。
        :type IsInvited: bool
        :param _IsPrivate: 是否私有。
        :type IsPrivate: bool
        :param _CustomProperties: 自定义房间属性。
        :type CustomProperties: str
        :param _IsForbidJoin: 房间是否禁止加人。
        :type IsForbidJoin: bool
        """
        self._GameId = None
        self._RoomId = None
        self._PlayerId = None
        self._ChangeRoomOptionList = None
        self._RoomName = None
        self._Owner = None
        self._IsViewed = None
        self._IsInvited = None
        self._IsPrivate = None
        self._CustomProperties = None
        self._IsForbidJoin = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def ChangeRoomOptionList(self):
        return self._ChangeRoomOptionList

    @ChangeRoomOptionList.setter
    def ChangeRoomOptionList(self, ChangeRoomOptionList):
        self._ChangeRoomOptionList = ChangeRoomOptionList

    @property
    def RoomName(self):
        return self._RoomName

    @RoomName.setter
    def RoomName(self, RoomName):
        self._RoomName = RoomName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def IsViewed(self):
        return self._IsViewed

    @IsViewed.setter
    def IsViewed(self, IsViewed):
        self._IsViewed = IsViewed

    @property
    def IsInvited(self):
        return self._IsInvited

    @IsInvited.setter
    def IsInvited(self, IsInvited):
        self._IsInvited = IsInvited

    @property
    def IsPrivate(self):
        return self._IsPrivate

    @IsPrivate.setter
    def IsPrivate(self, IsPrivate):
        self._IsPrivate = IsPrivate

    @property
    def CustomProperties(self):
        return self._CustomProperties

    @CustomProperties.setter
    def CustomProperties(self, CustomProperties):
        self._CustomProperties = CustomProperties

    @property
    def IsForbidJoin(self):
        return self._IsForbidJoin

    @IsForbidJoin.setter
    def IsForbidJoin(self, IsForbidJoin):
        self._IsForbidJoin = IsForbidJoin


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._RoomId = params.get("RoomId")
        self._PlayerId = params.get("PlayerId")
        self._ChangeRoomOptionList = params.get("ChangeRoomOptionList")
        self._RoomName = params.get("RoomName")
        self._Owner = params.get("Owner")
        self._IsViewed = params.get("IsViewed")
        self._IsInvited = params.get("IsInvited")
        self._IsPrivate = params.get("IsPrivate")
        self._CustomProperties = params.get("CustomProperties")
        self._IsForbidJoin = params.get("IsForbidJoin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomResponse(AbstractModel):
    """ModifyRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Room: 房间信息
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Room = None
        self._RequestId = None

    @property
    def Room(self):
        return self._Room

    @Room.setter
    def Room(self, Room):
        self._Room = Room

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self._Room = Room()
            self._Room._deserialize(params.get("Room"))
        self._RequestId = params.get("RequestId")


class Player(AbstractModel):
    """玩家信息详情

    """

    def __init__(self):
        r"""
        :param _OpenId: 玩家 OpenId。最长不超过64个字符。
        :type OpenId: str
        :param _Name: 玩家昵称。最长不超过32个字符。
        :type Name: str
        :param _TeamId: 队伍 ID。最长不超过16个字符。
        :type TeamId: str
        :param _IsRobot: 是否为机器人。
        :type IsRobot: bool
        :param _PlayerId: 玩家 PlayerId。出参使用，由后端返回。
        :type PlayerId: str
        :param _CustomPlayerStatus: 自定义玩家状态。非负数，最大不超过4294967295。默认为0。
        :type CustomPlayerStatus: int
        :param _CustomProfile: 自定义玩家属性。最长不超过256个字符。默认为空字符串。
        :type CustomProfile: str
        """
        self._OpenId = None
        self._Name = None
        self._TeamId = None
        self._IsRobot = None
        self._PlayerId = None
        self._CustomPlayerStatus = None
        self._CustomProfile = None

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TeamId(self):
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def IsRobot(self):
        return self._IsRobot

    @IsRobot.setter
    def IsRobot(self, IsRobot):
        self._IsRobot = IsRobot

    @property
    def PlayerId(self):
        return self._PlayerId

    @PlayerId.setter
    def PlayerId(self, PlayerId):
        self._PlayerId = PlayerId

    @property
    def CustomPlayerStatus(self):
        return self._CustomPlayerStatus

    @CustomPlayerStatus.setter
    def CustomPlayerStatus(self, CustomPlayerStatus):
        self._CustomPlayerStatus = CustomPlayerStatus

    @property
    def CustomProfile(self):
        return self._CustomProfile

    @CustomProfile.setter
    def CustomProfile(self, CustomProfile):
        self._CustomProfile = CustomProfile


    def _deserialize(self, params):
        self._OpenId = params.get("OpenId")
        self._Name = params.get("Name")
        self._TeamId = params.get("TeamId")
        self._IsRobot = params.get("IsRobot")
        self._PlayerId = params.get("PlayerId")
        self._CustomPlayerStatus = params.get("CustomPlayerStatus")
        self._CustomProfile = params.get("CustomProfile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRoomPlayerRequest(AbstractModel):
    """RemoveRoomPlayer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏资源Id。
        :type GameId: str
        :param _RemovePlayerId: 被踢出房间的玩家Id。
        :type RemovePlayerId: str
        """
        self._GameId = None
        self._RemovePlayerId = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def RemovePlayerId(self):
        return self._RemovePlayerId

    @RemovePlayerId.setter
    def RemovePlayerId(self, RemovePlayerId):
        self._RemovePlayerId = RemovePlayerId


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._RemovePlayerId = params.get("RemovePlayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRoomPlayerResponse(AbstractModel):
    """RemoveRoomPlayer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Room: 房间信息
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Room = None
        self._RequestId = None

    @property
    def Room(self):
        return self._Room

    @Room.setter
    def Room(self, Room):
        self._Room = Room

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self._Room = Room()
            self._Room._deserialize(params.get("Room"))
        self._RequestId = params.get("RequestId")


class Room(AbstractModel):
    """房间信息详情。

    """

    def __init__(self):
        r"""
        :param _Name: 表示房间名称。最长不超过32个字符。
        :type Name: str
        :param _MaxPlayers: 表示房间最大玩家数量。最大不超过100人。
        :type MaxPlayers: int
        :param _OwnerOpenId: 表示房主OpenId。最长不超过16个字符。
        :type OwnerOpenId: str
        :param _IsPrivate: 表示是否私有，私有指的是不允许其他玩家通过匹配加入房间。
        :type IsPrivate: bool
        :param _Players: 表示玩家详情列表。
        :type Players: list of Player
        :param _Teams: 表示团队属性列表。
        :type Teams: list of Team
        :param _Id: 表示房间 ID。出参用，由后端返回。
        :type Id: str
        :param _Type: 表示房间类型。最长不超过32个字符。
        :type Type: str
        :param _CreateType: 表示创建方式：0.单人主动发起创建房间请求；1.多人在线匹配请求分配房间；2. 直接创建满员房间。调用云API的创房请求默认为3，目前通过云API调用只支持第3种方式。
        :type CreateType: int
        :param _CustomProperties: 表示自定义房间属性，不传为空字符串。最长不超过1024个字符。
        :type CustomProperties: str
        :param _FrameSyncState: 表示房间帧同步状态。0表示未开始帧同步，1表示已开始帧同步，用于出参。
        :type FrameSyncState: int
        :param _FrameRate: 表示帧率。由控制台设置，用于出参。
        :type FrameRate: int
        :param _RouteId: 表示路由ID。用于出参。
        :type RouteId: str
        :param _CreateTime: 表示房间创建的时间戳（单位：秒）。
        :type CreateTime: int
        :param _StartGameTime: 表示开始帧同步时的时间戳（单位：秒）,未开始帧同步时返回为0。
        :type StartGameTime: int
        :param _IsForbidJoin: 表示是否禁止加入房间。出参使用，默认为False，通过SDK的ChangeRoom接口可以修改。
        :type IsForbidJoin: bool
        :param _Owner: 表示房主PlayerId。
        :type Owner: str
        """
        self._Name = None
        self._MaxPlayers = None
        self._OwnerOpenId = None
        self._IsPrivate = None
        self._Players = None
        self._Teams = None
        self._Id = None
        self._Type = None
        self._CreateType = None
        self._CustomProperties = None
        self._FrameSyncState = None
        self._FrameRate = None
        self._RouteId = None
        self._CreateTime = None
        self._StartGameTime = None
        self._IsForbidJoin = None
        self._Owner = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MaxPlayers(self):
        return self._MaxPlayers

    @MaxPlayers.setter
    def MaxPlayers(self, MaxPlayers):
        self._MaxPlayers = MaxPlayers

    @property
    def OwnerOpenId(self):
        return self._OwnerOpenId

    @OwnerOpenId.setter
    def OwnerOpenId(self, OwnerOpenId):
        self._OwnerOpenId = OwnerOpenId

    @property
    def IsPrivate(self):
        return self._IsPrivate

    @IsPrivate.setter
    def IsPrivate(self, IsPrivate):
        self._IsPrivate = IsPrivate

    @property
    def Players(self):
        return self._Players

    @Players.setter
    def Players(self, Players):
        self._Players = Players

    @property
    def Teams(self):
        return self._Teams

    @Teams.setter
    def Teams(self, Teams):
        self._Teams = Teams

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateType(self):
        return self._CreateType

    @CreateType.setter
    def CreateType(self, CreateType):
        self._CreateType = CreateType

    @property
    def CustomProperties(self):
        return self._CustomProperties

    @CustomProperties.setter
    def CustomProperties(self, CustomProperties):
        self._CustomProperties = CustomProperties

    @property
    def FrameSyncState(self):
        return self._FrameSyncState

    @FrameSyncState.setter
    def FrameSyncState(self, FrameSyncState):
        self._FrameSyncState = FrameSyncState

    @property
    def FrameRate(self):
        return self._FrameRate

    @FrameRate.setter
    def FrameRate(self, FrameRate):
        self._FrameRate = FrameRate

    @property
    def RouteId(self):
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartGameTime(self):
        return self._StartGameTime

    @StartGameTime.setter
    def StartGameTime(self, StartGameTime):
        self._StartGameTime = StartGameTime

    @property
    def IsForbidJoin(self):
        return self._IsForbidJoin

    @IsForbidJoin.setter
    def IsForbidJoin(self, IsForbidJoin):
        self._IsForbidJoin = IsForbidJoin

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MaxPlayers = params.get("MaxPlayers")
        self._OwnerOpenId = params.get("OwnerOpenId")
        self._IsPrivate = params.get("IsPrivate")
        if params.get("Players") is not None:
            self._Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self._Players.append(obj)
        if params.get("Teams") is not None:
            self._Teams = []
            for item in params.get("Teams"):
                obj = Team()
                obj._deserialize(item)
                self._Teams.append(obj)
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._CreateType = params.get("CreateType")
        self._CustomProperties = params.get("CustomProperties")
        self._FrameSyncState = params.get("FrameSyncState")
        self._FrameRate = params.get("FrameRate")
        self._RouteId = params.get("RouteId")
        self._CreateTime = params.get("CreateTime")
        self._StartGameTime = params.get("StartGameTime")
        self._IsForbidJoin = params.get("IsForbidJoin")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Team(AbstractModel):
    """团队属性

    """

    def __init__(self):
        r"""
        :param _Id: 队伍ID。最长不超过16个字符。
        :type Id: str
        :param _Name: 队伍名称。最长不超过32个字符。
        :type Name: str
        :param _MinPlayers: 队伍最小人数。最大不超过100人。
        :type MinPlayers: int
        :param _MaxPlayers: 队伍最大人数。最大不超过100人。
        :type MaxPlayers: int
        """
        self._Id = None
        self._Name = None
        self._MinPlayers = None
        self._MaxPlayers = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MinPlayers(self):
        return self._MinPlayers

    @MinPlayers.setter
    def MinPlayers(self, MinPlayers):
        self._MinPlayers = MinPlayers

    @property
    def MaxPlayers(self):
        return self._MaxPlayers

    @MaxPlayers.setter
    def MaxPlayers(self, MaxPlayers):
        self._MaxPlayers = MaxPlayers


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MinPlayers = params.get("MinPlayers")
        self._MaxPlayers = params.get("MaxPlayers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        