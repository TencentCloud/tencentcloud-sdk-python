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


class ChangeRoomPlayerProfileRequest(AbstractModel):
    """ChangeRoomPlayerProfile请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。
        :type GameId: str
        :param PlayerId: 发起修改的玩家Id。
        :type PlayerId: str
        :param CustomProfile: 需要修改的玩家自定义属性。
        :type CustomProfile: str
        """
        self.GameId = None
        self.PlayerId = None
        self.CustomProfile = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.PlayerId = params.get("PlayerId")
        self.CustomProfile = params.get("CustomProfile")


class ChangeRoomPlayerProfileResponse(AbstractModel):
    """ChangeRoomPlayerProfile返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息。
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Room = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self.Room = Room()
            self.Room._deserialize(params.get("Room"))
        self.RequestId = params.get("RequestId")


class ChangeRoomPlayerStatusRequest(AbstractModel):
    """ChangeRoomPlayerStatus请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。
        :type GameId: str
        :param CustomStatus: 玩家自定义状态。
        :type CustomStatus: int
        :param PlayerId: 玩家id。
        :type PlayerId: str
        """
        self.GameId = None
        self.CustomStatus = None
        self.PlayerId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.CustomStatus = params.get("CustomStatus")
        self.PlayerId = params.get("PlayerId")


class ChangeRoomPlayerStatusResponse(AbstractModel):
    """ChangeRoomPlayerStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Room = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self.Room = Room()
            self.Room._deserialize(params.get("Room"))
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 表示游戏资源唯一 ID, 由后台自动分配, 无法修改。
        :type GameId: str
        :param RoomId: 表示游戏房间唯一ID。
        :type RoomId: str
        """
        self.GameId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.RoomId = params.get("RoomId")


class DismissRoomResponse(AbstractModel):
    """DismissRoom返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoomRequest(AbstractModel):
    """ModifyRoom请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。
        :type GameId: str
        :param RoomId: 房间ID。
        :type RoomId: str
        :param PlayerId: 发起者的PlayerId。
        :type PlayerId: str
        :param ChangeRoomOptionList: 需要修改的房间选项，0表示房间名称，1表示房主，2表示是否允许观战，3表示是否支持邀请码/密码，4表示是否私有，5表示是否自定义房间属性，6表示是否禁止加人。
        :type ChangeRoomOptionList: list of int
        :param RoomName: 房间名称。
        :type RoomName: str
        :param Owner: 变更房主。
        :type Owner: str
        :param IsViewed: 是否支持观战。
        :type IsViewed: bool
        :param IsInvited: 是否支持邀请码/密码。
        :type IsInvited: bool
        :param IsPrivate: 是否私有。
        :type IsPrivate: bool
        :param CustomProperties: 自定义房间属性。
        :type CustomProperties: str
        :param IsForbidJoin: 房间是否禁止加人。
        :type IsForbidJoin: bool
        """
        self.GameId = None
        self.RoomId = None
        self.PlayerId = None
        self.ChangeRoomOptionList = None
        self.RoomName = None
        self.Owner = None
        self.IsViewed = None
        self.IsInvited = None
        self.IsPrivate = None
        self.CustomProperties = None
        self.IsForbidJoin = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.RoomId = params.get("RoomId")
        self.PlayerId = params.get("PlayerId")
        self.ChangeRoomOptionList = params.get("ChangeRoomOptionList")
        self.RoomName = params.get("RoomName")
        self.Owner = params.get("Owner")
        self.IsViewed = params.get("IsViewed")
        self.IsInvited = params.get("IsInvited")
        self.IsPrivate = params.get("IsPrivate")
        self.CustomProperties = params.get("CustomProperties")
        self.IsForbidJoin = params.get("IsForbidJoin")


class ModifyRoomResponse(AbstractModel):
    """ModifyRoom返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Room = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self.Room = Room()
            self.Room._deserialize(params.get("Room"))
        self.RequestId = params.get("RequestId")


class Player(AbstractModel):
    """玩家信息详情

    """

    def __init__(self):
        """
        :param OpenId: 玩家 OpenId。最长不超过64个字符。
        :type OpenId: str
        :param Name: 玩家昵称。最长不超过32个字符。
        :type Name: str
        :param TeamId: 队伍 ID。最长不超过16个字符。
        :type TeamId: str
        :param IsRobot: 是否为机器人。
        :type IsRobot: bool
        :param PlayerId: 玩家 PlayerId。出参使用，由后端返回。
        :type PlayerId: str
        :param CustomPlayerStatus: 自定义玩家状态。非负数，最大不超过4294967295。默认为0。
        :type CustomPlayerStatus: int
        :param CustomProfile: 自定义玩家属性。最长不超过256个字符。默认为空字符串。
        :type CustomProfile: str
        """
        self.OpenId = None
        self.Name = None
        self.TeamId = None
        self.IsRobot = None
        self.PlayerId = None
        self.CustomPlayerStatus = None
        self.CustomProfile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.Name = params.get("Name")
        self.TeamId = params.get("TeamId")
        self.IsRobot = params.get("IsRobot")
        self.PlayerId = params.get("PlayerId")
        self.CustomPlayerStatus = params.get("CustomPlayerStatus")
        self.CustomProfile = params.get("CustomProfile")


class RemoveRoomPlayerRequest(AbstractModel):
    """RemoveRoomPlayer请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。
        :type GameId: str
        :param RemovePlayerId: 被踢出房间的玩家Id。
        :type RemovePlayerId: str
        """
        self.GameId = None
        self.RemovePlayerId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.RemovePlayerId = params.get("RemovePlayerId")


class RemoveRoomPlayerResponse(AbstractModel):
    """RemoveRoomPlayer返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息
        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Room = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self.Room = Room()
            self.Room._deserialize(params.get("Room"))
        self.RequestId = params.get("RequestId")


class Room(AbstractModel):
    """房间信息详情。

    """

    def __init__(self):
        """
        :param Name: 表示房间名称。最长不超过32个字符。
        :type Name: str
        :param MaxPlayers: 表示房间最大玩家数量。最大不超过100人。
        :type MaxPlayers: int
        :param OwnerOpenId: 表示房主OpenId。最长不超过16个字符。
        :type OwnerOpenId: str
        :param IsPrivate: 表示是否私有，私有指的是不允许其他玩家通过匹配加入房间。
        :type IsPrivate: bool
        :param Players: 表示玩家详情列表。
        :type Players: list of Player
        :param Teams: 表示团队属性列表。
        :type Teams: list of Team
        :param Id: 表示房间 ID。出参用，由后端返回。
        :type Id: str
        :param Type: 表示房间类型。最长不超过32个字符。
        :type Type: str
        :param CreateType: 表示创建方式：0.单人主动发起创建房间请求；1.多人在线匹配请求分配房间；2. 直接创建满员房间。调用云API的创房请求默认为3，目前通过云API调用只支持第3种方式。
        :type CreateType: int
        :param CustomProperties: 表示自定义房间属性，不传为空字符串。最长不超过1024个字符。
        :type CustomProperties: str
        :param FrameSyncState: 表示房间帧同步状态。0表示未开始帧同步，1表示已开始帧同步，用于出参。
        :type FrameSyncState: int
        :param FrameRate: 表示帧率。由控制台设置，用于出参。
        :type FrameRate: int
        :param RouteId: 表示路由ID。用于出参。
        :type RouteId: str
        :param CreateTime: 表示房间创建的时间戳（单位：秒）。
        :type CreateTime: int
        :param StartGameTime: 表示开始帧同步时的时间戳（单位：秒）,未开始帧同步时返回为0。
        :type StartGameTime: int
        :param IsForbidJoin: 表示是否禁止加入房间。出参使用，默认为False，通过SDK的ChangeRoom接口可以修改。
        :type IsForbidJoin: bool
        :param Owner: 表示房主PlayerId。
        :type Owner: str
        """
        self.Name = None
        self.MaxPlayers = None
        self.OwnerOpenId = None
        self.IsPrivate = None
        self.Players = None
        self.Teams = None
        self.Id = None
        self.Type = None
        self.CreateType = None
        self.CustomProperties = None
        self.FrameSyncState = None
        self.FrameRate = None
        self.RouteId = None
        self.CreateTime = None
        self.StartGameTime = None
        self.IsForbidJoin = None
        self.Owner = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MaxPlayers = params.get("MaxPlayers")
        self.OwnerOpenId = params.get("OwnerOpenId")
        self.IsPrivate = params.get("IsPrivate")
        if params.get("Players") is not None:
            self.Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self.Players.append(obj)
        if params.get("Teams") is not None:
            self.Teams = []
            for item in params.get("Teams"):
                obj = Team()
                obj._deserialize(item)
                self.Teams.append(obj)
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.CreateType = params.get("CreateType")
        self.CustomProperties = params.get("CustomProperties")
        self.FrameSyncState = params.get("FrameSyncState")
        self.FrameRate = params.get("FrameRate")
        self.RouteId = params.get("RouteId")
        self.CreateTime = params.get("CreateTime")
        self.StartGameTime = params.get("StartGameTime")
        self.IsForbidJoin = params.get("IsForbidJoin")
        self.Owner = params.get("Owner")


class Team(AbstractModel):
    """团队属性

    """

    def __init__(self):
        """
        :param Id: 队伍ID。最长不超过16个字符。
        :type Id: str
        :param Name: 队伍名称。最长不超过32个字符。
        :type Name: str
        :param MinPlayers: 队伍最小人数。最大不超过100人。
        :type MinPlayers: int
        :param MaxPlayers: 队伍最大人数。最大不超过100人。
        :type MaxPlayers: int
        """
        self.Id = None
        self.Name = None
        self.MinPlayers = None
        self.MaxPlayers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MinPlayers = params.get("MinPlayers")
        self.MaxPlayers = params.get("MaxPlayers")