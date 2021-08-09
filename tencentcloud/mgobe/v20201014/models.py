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
        """
        :param GameId: 游戏资源Id。\n        :type GameId: str\n        :param PlayerId: 发起修改的玩家Id。\n        :type PlayerId: str\n        :param CustomProfile: 需要修改的玩家自定义属性。\n        :type CustomProfile: str\n        """
        self.GameId = None
        self.PlayerId = None
        self.CustomProfile = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.PlayerId = params.get("PlayerId")
        self.CustomProfile = params.get("CustomProfile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeRoomPlayerProfileResponse(AbstractModel):
    """ChangeRoomPlayerProfile返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息。\n        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GameId: 游戏资源Id。\n        :type GameId: str\n        :param CustomStatus: 玩家自定义状态。\n        :type CustomStatus: int\n        :param PlayerId: 玩家id。\n        :type PlayerId: str\n        """
        self.GameId = None
        self.CustomStatus = None
        self.PlayerId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.CustomStatus = params.get("CustomStatus")
        self.PlayerId = params.get("PlayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeRoomPlayerStatusResponse(AbstractModel):
    """ChangeRoomPlayerStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息\n        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Room = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Room") is not None:
            self.Room = Room()
            self.Room._deserialize(params.get("Room"))
        self.RequestId = params.get("RequestId")


class DescribePlayerRequest(AbstractModel):
    """DescribePlayer请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。\n        :type GameId: str\n        :param OpenId: 玩家OpenId。\n        :type OpenId: str\n        :param PlayerId: 玩家PlayerId，由后台分配，当OpenId不传的时候，PlayerId必传，传入PlayerId可以查询当前PlayerId的玩家信息，当OpenId传入的时候，PlayerId可不传，按照OpenId查询玩家信息。\n        :type PlayerId: str\n        """
        self.GameId = None
        self.OpenId = None
        self.PlayerId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.OpenId = params.get("OpenId")
        self.PlayerId = params.get("PlayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayerResponse(AbstractModel):
    """DescribePlayer返回参数结构体

    """

    def __init__(self):
        """
        :param Player: 玩家信息。\n        :type Player: :class:`tencentcloud.mgobe.v20201014.models.Player`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Player = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Player") is not None:
            self.Player = Player()
            self.Player._deserialize(params.get("Player"))
        self.RequestId = params.get("RequestId")


class DescribeRoomRequest(AbstractModel):
    """DescribeRoom请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。\n        :type GameId: str\n        :param PlayerId: 玩家Id。当房间Id不传的时候，玩家Id必传，传入玩家Id可以查询当前玩家所在的房间信息，当房间Id传入的时候，优先按照房间Id查询房间信息。\n        :type PlayerId: str\n        :param RoomId: 房间Id。\n        :type RoomId: str\n        """
        self.GameId = None
        self.PlayerId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.PlayerId = params.get("PlayerId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomResponse(AbstractModel):
    """DescribeRoom返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息。\n        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GameId: 表示游戏资源唯一 ID, 由后台自动分配, 无法修改。\n        :type GameId: str\n        :param RoomId: 表示游戏房间唯一ID。\n        :type RoomId: str\n        """
        self.GameId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    """DismissRoom返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoomRequest(AbstractModel):
    """ModifyRoom请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。\n        :type GameId: str\n        :param RoomId: 房间ID。\n        :type RoomId: str\n        :param PlayerId: 发起者的PlayerId。\n        :type PlayerId: str\n        :param ChangeRoomOptionList: 需要修改的房间选项，0表示房间名称，1表示房主，2表示是否允许观战，3表示是否支持邀请码/密码，4表示是否私有，5表示是否自定义房间属性，6表示是否禁止加人。\n        :type ChangeRoomOptionList: list of int\n        :param RoomName: 房间名称。\n        :type RoomName: str\n        :param Owner: 变更房主。\n        :type Owner: str\n        :param IsViewed: 是否支持观战。\n        :type IsViewed: bool\n        :param IsInvited: 是否支持邀请码/密码。\n        :type IsInvited: bool\n        :param IsPrivate: 是否私有。\n        :type IsPrivate: bool\n        :param CustomProperties: 自定义房间属性。\n        :type CustomProperties: str\n        :param IsForbidJoin: 房间是否禁止加人。\n        :type IsForbidJoin: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomResponse(AbstractModel):
    """ModifyRoom返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息\n        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param OpenId: 玩家 OpenId。最长不超过64个字符。\n        :type OpenId: str\n        :param Name: 玩家昵称。最长不超过32个字符。\n        :type Name: str\n        :param TeamId: 队伍 ID。最长不超过16个字符。\n        :type TeamId: str\n        :param IsRobot: 是否为机器人。\n        :type IsRobot: bool\n        :param PlayerId: 玩家 PlayerId。出参使用，由后端返回。\n        :type PlayerId: str\n        :param CustomPlayerStatus: 自定义玩家状态。非负数，最大不超过4294967295。默认为0。\n        :type CustomPlayerStatus: int\n        :param CustomProfile: 自定义玩家属性。最长不超过256个字符。默认为空字符串。\n        :type CustomProfile: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRoomPlayerRequest(AbstractModel):
    """RemoveRoomPlayer请求参数结构体

    """

    def __init__(self):
        """
        :param GameId: 游戏资源Id。\n        :type GameId: str\n        :param RemovePlayerId: 被踢出房间的玩家Id。\n        :type RemovePlayerId: str\n        """
        self.GameId = None
        self.RemovePlayerId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.RemovePlayerId = params.get("RemovePlayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRoomPlayerResponse(AbstractModel):
    """RemoveRoomPlayer返回参数结构体

    """

    def __init__(self):
        """
        :param Room: 房间信息\n        :type Room: :class:`tencentcloud.mgobe.v20201014.models.Room`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Name: 表示房间名称。最长不超过32个字符。\n        :type Name: str\n        :param MaxPlayers: 表示房间最大玩家数量。最大不超过100人。\n        :type MaxPlayers: int\n        :param OwnerOpenId: 表示房主OpenId。最长不超过16个字符。\n        :type OwnerOpenId: str\n        :param IsPrivate: 表示是否私有，私有指的是不允许其他玩家通过匹配加入房间。\n        :type IsPrivate: bool\n        :param Players: 表示玩家详情列表。\n        :type Players: list of Player\n        :param Teams: 表示团队属性列表。\n        :type Teams: list of Team\n        :param Id: 表示房间 ID。出参用，由后端返回。\n        :type Id: str\n        :param Type: 表示房间类型。最长不超过32个字符。\n        :type Type: str\n        :param CreateType: 表示创建方式：0.单人主动发起创建房间请求；1.多人在线匹配请求分配房间；2. 直接创建满员房间。调用云API的创房请求默认为3，目前通过云API调用只支持第3种方式。\n        :type CreateType: int\n        :param CustomProperties: 表示自定义房间属性，不传为空字符串。最长不超过1024个字符。\n        :type CustomProperties: str\n        :param FrameSyncState: 表示房间帧同步状态。0表示未开始帧同步，1表示已开始帧同步，用于出参。\n        :type FrameSyncState: int\n        :param FrameRate: 表示帧率。由控制台设置，用于出参。\n        :type FrameRate: int\n        :param RouteId: 表示路由ID。用于出参。\n        :type RouteId: str\n        :param CreateTime: 表示房间创建的时间戳（单位：秒）。\n        :type CreateTime: int\n        :param StartGameTime: 表示开始帧同步时的时间戳（单位：秒）,未开始帧同步时返回为0。\n        :type StartGameTime: int\n        :param IsForbidJoin: 表示是否禁止加入房间。出参使用，默认为False，通过SDK的ChangeRoom接口可以修改。\n        :type IsForbidJoin: bool\n        :param Owner: 表示房主PlayerId。\n        :type Owner: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Team(AbstractModel):
    """团队属性

    """

    def __init__(self):
        """
        :param Id: 队伍ID。最长不超过16个字符。\n        :type Id: str\n        :param Name: 队伍名称。最长不超过32个字符。\n        :type Name: str\n        :param MinPlayers: 队伍最小人数。最大不超过100人。\n        :type MinPlayers: int\n        :param MaxPlayers: 队伍最大人数。最大不超过100人。\n        :type MaxPlayers: int\n        """
        self.Id = None
        self.Name = None
        self.MinPlayers = None
        self.MaxPlayers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MinPlayers = params.get("MinPlayers")
        self.MaxPlayers = params.get("MaxPlayers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        