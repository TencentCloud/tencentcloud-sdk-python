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


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param AliasId: 别名ID
        :type AliasId: str
        :param CreatorId: 创建者ID
        :type CreatorId: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameProperties: 游戏属性
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 游戏服务器会话属性详情
        :type GameServerSessionData: str
        :param GameServerSessionId: 游戏服务器会话自定义ID
        :type GameServerSessionId: str
        :param IdempotencyToken: 幂等token
        :type IdempotencyToken: str
        :param Name: 游戏服务器会话名称
        :type Name: str
        """
        self.MaximumPlayerSessionCount = None
        self.AliasId = None
        self.CreatorId = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IdempotencyToken = None
        self.Name = None


    def _deserialize(self, params):
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.AliasId = params.get("AliasId")
        self.CreatorId = params.get("CreatorId")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IdempotencyToken = params.get("IdempotencyToken")
        self.Name = params.get("Name")


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSession: 游戏服务器会话
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """访问实例所需要的凭据

    """

    def __init__(self):
        """
        :param Secret: ssh私钥
        :type Secret: str
        :param UserName: 用户名
        :type UserName: str
        """
        self.Secret = None
        self.UserName = None


    def _deserialize(self, params):
        self.Secret = params.get("Secret")
        self.UserName = params.get("UserName")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
        :type FleetId: str
        :param Name: 名称
        :type Name: str
        """
        self.FleetId = None
        self.Name = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param Limit: 单次查询记录数上限
        :type Limit: int
        :param NextToken: 页偏移，用于查询下一页
        :type NextToken: str
        :param StatusFilter: 游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :type StatusFilter: str
        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionDetails: 游戏服务器会话详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionDetails: list of GameServerSessionDetail
        :param NextToken: 页偏移，用于查询下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionDetails = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionDetails") is not None:
            self.GameServerSessionDetails = []
            for item in params.get("GameServerSessionDetails"):
                obj = GameServerSessionDetail()
                obj._deserialize(item)
                self.GameServerSessionDetails.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionPlacementRequest(AbstractModel):
    """DescribeGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 游戏服务器会话放置的唯一标识符
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionQueuesRequest(AbstractModel):
    """DescribeGameServerSessionQueues请求参数结构体

    """

    def __init__(self):
        """
        :param Names: 游戏服务器会话队列数组
        :type Names: list of str
        :param Limit: 要返回的最大结果数
        :type Limit: int
        :param Offset: 偏移
        :type Offset: int
        """
        self.Names = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeGameServerSessionQueuesResponse(AbstractModel):
    """DescribeGameServerSessionQueues返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionQueues: 游戏服务器会话队列数组
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionQueues: list of GameServerSessionQueue
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionQueues = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionQueues") is not None:
            self.GameServerSessionQueues = []
            for item in params.get("GameServerSessionQueues"):
                obj = GameServerSessionQueue()
                obj._deserialize(item)
                self.GameServerSessionQueues.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionsRequest(AbstractModel):
    """DescribeGameServerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param Limit: 单次查询记录数上限
        :type Limit: int
        :param NextToken: 页偏移，用于查询下一页
        :type NextToken: str
        :param StatusFilter: 游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :type StatusFilter: str
        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessions: 游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessions: list of GameServerSession
        :param NextToken: 页便宜，用于查询下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
        :type FleetId: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Offset: 结果返回最大数量
        :type Offset: int
        :param Limit: 返回结果偏移
        :type Limit: int
        """
        self.FleetId = None
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Instances: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of Instance
        :param TotalCount: 结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param Limit: 单次查询记录数上限
        :type Limit: int
        :param NextToken: 页偏移，用于查询下一页
        :type NextToken: str
        :param PlayerId: 玩家ID
        :type PlayerId: str
        :param PlayerSessionId: 玩家会话ID
        :type PlayerSessionId: str
        :param PlayerSessionStatusFilter: 玩家会话状态（RESERVED,ACTIVE,COMPLETED,TIMEDOUT）
        :type PlayerSessionStatusFilter: str
        """
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.PlayerSessionStatusFilter = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.PlayerSessionStatusFilter = params.get("PlayerSessionStatusFilter")


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param PlayerSessions: 玩家会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessions: list of PlayerSession
        :param NextToken: 页偏移
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlayerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self.PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self.PlayerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
        :type FleetId: str
        :param StatusFilter: 状态过滤条件
        :type StatusFilter: str
        :param Offset: 结果返回最大数量
        :type Offset: int
        :param Limit: 返回结果偏移
        :type Limit: int
        """
        self.FleetId = None
        self.StatusFilter = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.StatusFilter = params.get("StatusFilter")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param ScalingPolicies: 动态扩缩容配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingPolicies: list of ScalingPolicy
        :param TotalCount: 返回总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScalingPolicies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScalingPolicies") is not None:
            self.ScalingPolicies = []
            for item in params.get("ScalingPolicies"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self.ScalingPolicies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DesiredPlayerSession(AbstractModel):
    """玩家游戏会话信息

    """

    def __init__(self):
        """
        :param PlayerId: 与玩家会话关联的唯一玩家标识
        :type PlayerId: str
        :param PlayerData: 开发人员定义的玩家数据
        :type PlayerData: str
        """
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class GameProperty(AbstractModel):
    """游戏属性详情

    """

    def __init__(self):
        """
        :param Key: 属性名称
        :type Key: str
        :param Value: 属性值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class GameServerSession(AbstractModel):
    """游戏会话详情

    """

    def __init__(self):
        """
        :param CreationTime: 游戏服务器会话创建时间
        :type CreationTime: str
        :param CreatorId: 创建者ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorId: str
        :param CurrentPlayerSessionCount: 当前玩家数量
        :type CurrentPlayerSessionCount: int
        :param DnsName: CVM的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 游戏服务器会话属性详情
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param IpAddress: CVM IP地址
        :type IpAddress: str
        :param MatchmakerData: 对战进程详情
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param Name: 游戏服务器会话名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param PlayerSessionCreationPolicy: 玩家会话创建策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSessionCreationPolicy: str
        :param Port: 端口号
        :type Port: int
        :param Status: 游戏服务器会话状态
        :type Status: str
        :param StatusReason: 游戏服务器会话状态附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReason: str
        :param TerminationTime: 终止的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        :param InstanceType: 实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param CurrentCustomCount: 当前自定义数
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentCustomCount: int
        :param MaxCustomCount: 最大自定义数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCustomCount: int
        :param Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param AvailabilityStatus: 会话可用性状态，是否被屏蔽
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailabilityStatus: str
        """
        self.CreationTime = None
        self.CreatorId = None
        self.CurrentPlayerSessionCount = None
        self.DnsName = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.MatchmakerData = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.Port = None
        self.Status = None
        self.StatusReason = None
        self.TerminationTime = None
        self.InstanceType = None
        self.CurrentCustomCount = None
        self.MaxCustomCount = None
        self.Weight = None
        self.AvailabilityStatus = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreatorId = params.get("CreatorId")
        self.CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.MatchmakerData = params.get("MatchmakerData")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.StatusReason = params.get("StatusReason")
        self.TerminationTime = params.get("TerminationTime")
        self.InstanceType = params.get("InstanceType")
        self.CurrentCustomCount = params.get("CurrentCustomCount")
        self.MaxCustomCount = params.get("MaxCustomCount")
        self.Weight = params.get("Weight")
        self.AvailabilityStatus = params.get("AvailabilityStatus")


class GameServerSessionDetail(AbstractModel):
    """游戏服务器会话详情（GameServerSessionDetail）

    """

    def __init__(self):
        """
        :param GameServerSession: 游戏服务器会话
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param ProtectionPolicy: 保护策略，可选（NoProtection,FullProtection）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectionPolicy: str
        """
        self.GameServerSession = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.ProtectionPolicy = params.get("ProtectionPolicy")


class GameServerSessionPlacement(AbstractModel):
    """游戏会话部署对象

    """

    def __init__(self):
        """
        :param PlacementId: 部署Id
        :type PlacementId: str
        :param GameServerSessionQueueName: 服务部署组名称
        :type GameServerSessionQueueName: str
        :param PlayerLatencies: 玩家延迟
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerLatencies: list of PlayerLatency
        :param Status: 服务部署状态
        :type Status: str
        :param DnsName: 分配给正在运行游戏会话的实例的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param GameServerSessionId: 游戏会话Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionId: str
        :param GameServerSessionName: 游戏会话名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionName: str
        :param GameServerSessionRegion: 服务部署区域
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionRegion: str
        :param GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param GameServerSessionData: 游戏会话数据
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param IpAddress: 运行游戏会话的实例的IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param Port: 运行游戏会话的实例的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param MatchmakerData: 游戏匹配数据
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param PlacedPlayerSessions: 部署的玩家游戏数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacedPlayerSessions: list of PlacedPlayerSession
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.PlayerLatencies = None
        self.Status = None
        self.DnsName = None
        self.GameServerSessionId = None
        self.GameServerSessionName = None
        self.GameServerSessionRegion = None
        self.GameProperties = None
        self.MaximumPlayerSessionCount = None
        self.GameServerSessionData = None
        self.IpAddress = None
        self.Port = None
        self.MatchmakerData = None
        self.PlacedPlayerSessions = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)
        self.Status = params.get("Status")
        self.DnsName = params.get("DnsName")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.GameServerSessionName = params.get("GameServerSessionName")
        self.GameServerSessionRegion = params.get("GameServerSessionRegion")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.IpAddress = params.get("IpAddress")
        self.Port = params.get("Port")
        self.MatchmakerData = params.get("MatchmakerData")
        if params.get("PlacedPlayerSessions") is not None:
            self.PlacedPlayerSessions = []
            for item in params.get("PlacedPlayerSessions"):
                obj = PlacedPlayerSession()
                obj._deserialize(item)
                self.PlacedPlayerSessions.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GameServerSessionQueue(AbstractModel):
    """服务部署组对象

    """

    def __init__(self):
        """
        :param Name: 服务部署组名字
        :type Name: str
        :param GameServerSessionQueueArn: 服务部署组资源
        :type GameServerSessionQueueArn: str
        :param Destinations: 目的fleet（可为别名）列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Destinations: list of GameServerSessionQueueDestination
        :param PlayerLatencyPolicies: 延迟策略集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerLatencyPolicies: list of PlayerLatencyPolicy
        :param TimeoutInSeconds: 超时时间
        :type TimeoutInSeconds: int
        """
        self.Name = None
        self.GameServerSessionQueueArn = None
        self.Destinations = None
        self.PlayerLatencyPolicies = None
        self.TimeoutInSeconds = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.GameServerSessionQueueArn = params.get("GameServerSessionQueueArn")
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = GameServerSessionQueueDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        if params.get("PlayerLatencyPolicies") is not None:
            self.PlayerLatencyPolicies = []
            for item in params.get("PlayerLatencyPolicies"):
                obj = PlayerLatencyPolicy()
                obj._deserialize(item)
                self.PlayerLatencyPolicies.append(obj)
        self.TimeoutInSeconds = params.get("TimeoutInSeconds")


class GameServerSessionQueueDestination(AbstractModel):
    """服务部署组目的集合

    """

    def __init__(self):
        """
        :param DestinationArn: 服务部署组目的的资源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DestinationArn: str
        """
        self.DestinationArn = None


    def _deserialize(self, params):
        self.DestinationArn = params.get("DestinationArn")


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        """
        self.GameServerSessionId = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl返回参数结构体

    """

    def __init__(self):
        """
        :param PreSignedUrl: 日志下载URL
注意：此字段可能返回 null，表示取不到有效值。
        :type PreSignedUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PreSignedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedUrl = params.get("PreSignedUrl")
        self.RequestId = params.get("RequestId")


class GetInstanceAccessRequest(AbstractModel):
    """GetInstanceAccess请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署Id
        :type FleetId: str
        :param InstanceId: 实例Id
        :type InstanceId: str
        """
        self.FleetId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")


class GetInstanceAccessResponse(AbstractModel):
    """GetInstanceAccess返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceAccess: 实例登录所需要的凭据
        :type InstanceAccess: :class:`tencentcloud.gse.v20191112.models.InstanceAccess`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceAccess") is not None:
            self.InstanceAccess = InstanceAccess()
            self.InstanceAccess._deserialize(params.get("InstanceAccess"))
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param IpAddress: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param DnsName: dns
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param OperatingSystem: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatingSystem: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.FleetId = None
        self.InstanceId = None
        self.IpAddress = None
        self.DnsName = None
        self.OperatingSystem = None
        self.Status = None
        self.Type = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.IpAddress = params.get("IpAddress")
        self.DnsName = params.get("DnsName")
        self.OperatingSystem = params.get("OperatingSystem")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")


class InstanceAccess(AbstractModel):
    """实例访问凭证信息

    """

    def __init__(self):
        """
        :param Credentials: 访问实例所需要的凭据
        :type Credentials: :class:`tencentcloud.gse.v20191112.models.Credentials`
        :param FleetId: 服务部署Id
        :type FleetId: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param IpAddress: 实例公网IP
        :type IpAddress: str
        :param OperatingSystem: 操作系统
        :type OperatingSystem: str
        """
        self.Credentials = None
        self.FleetId = None
        self.InstanceId = None
        self.IpAddress = None
        self.OperatingSystem = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.IpAddress = params.get("IpAddress")
        self.OperatingSystem = params.get("OperatingSystem")


class JoinGameServerSessionRequest(AbstractModel):
    """JoinGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param PlayerId: 玩家ID
        :type PlayerId: str
        :param PlayerData: 玩家自定义信息
        :type PlayerData: str
        """
        self.GameServerSessionId = None
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param PlayerSession: 玩家会话
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerSession: :class:`tencentcloud.gse.v20191112.models.PlayerSession`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlayerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSession") is not None:
            self.PlayerSession = PlayerSession()
            self.PlayerSession._deserialize(params.get("PlayerSession"))
        self.RequestId = params.get("RequestId")


class PlacedPlayerSession(AbstractModel):
    """部署的玩家游戏会话

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id
        :type PlayerId: str
        :param PlayerSessionId: 玩家会话Id
        :type PlayerSessionId: str
        """
        self.PlayerId = None
        self.PlayerSessionId = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")


class PlayerLatency(AbstractModel):
    """玩家延迟信息

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param RegionIdentifier: 延迟对应的区域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionIdentifier: str
        :param LatencyInMilliseconds: 毫秒级延迟
        :type LatencyInMilliseconds: int
        """
        self.PlayerId = None
        self.RegionIdentifier = None
        self.LatencyInMilliseconds = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.RegionIdentifier = params.get("RegionIdentifier")
        self.LatencyInMilliseconds = params.get("LatencyInMilliseconds")


class PlayerLatencyPolicy(AbstractModel):
    """延迟策略

    """

    def __init__(self):
        """
        :param MaximumIndividualPlayerLatencyMilliseconds: 任意player允许的最大延迟，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MaximumIndividualPlayerLatencyMilliseconds: int
        :param PolicyDurationSeconds: 放置新GameServerSession时强制实施策略的时间长度，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDurationSeconds: int
        """
        self.MaximumIndividualPlayerLatencyMilliseconds = None
        self.PolicyDurationSeconds = None


    def _deserialize(self, params):
        self.MaximumIndividualPlayerLatencyMilliseconds = params.get("MaximumIndividualPlayerLatencyMilliseconds")
        self.PolicyDurationSeconds = params.get("PolicyDurationSeconds")


class PlayerSession(AbstractModel):
    """玩家会话详情

    """

    def __init__(self):
        """
        :param CreationTime: 玩家会话创建时间
        :type CreationTime: str
        :param DnsName: 游戏服务器会话运行的DNS标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param IpAddress: 游戏服务器会话运行的CVM地址
        :type IpAddress: str
        :param PlayerData: 玩家相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerData: str
        :param PlayerId: 玩家ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param PlayerSessionId: 玩家会话ID
        :type PlayerSessionId: str
        :param Port: 端口号
        :type Port: int
        :param Status: 玩家会话的状态
        :type Status: str
        :param TerminationTime: 玩家会话终止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        """
        self.CreationTime = None
        self.DnsName = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.PlayerData = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.Port = None
        self.Status = None
        self.TerminationTime = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.PlayerData = params.get("PlayerData")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.TerminationTime = params.get("TerminationTime")


class PutScalingPolicyRequest(AbstractModel):
    """PutScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 基于规则的扩缩容配置
        :type FleetId: str
        :param Name: 名称
        :type Name: str
        :param ScalingAdjustment: 调整值
        :type ScalingAdjustment: int
        :param ScalingAdjustmentType: 调整类型
        :type ScalingAdjustmentType: str
        :param Threshold: 指标阈值
        :type Threshold: float
        :param ComparisonOperator: 比较符
        :type ComparisonOperator: str
        :param EvaluationPeriods: 时间长度（分钟）
        :type EvaluationPeriods: int
        :param MetricName: 指标名称
        :type MetricName: str
        :param PolicyType: 策略类型
        :type PolicyType: str
        :param TargetConfiguration: 扩缩容配置类型
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self.FleetId = None
        self.Name = None
        self.ScalingAdjustment = None
        self.ScalingAdjustmentType = None
        self.Threshold = None
        self.ComparisonOperator = None
        self.EvaluationPeriods = None
        self.MetricName = None
        self.PolicyType = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")
        self.ScalingAdjustment = params.get("ScalingAdjustment")
        self.ScalingAdjustmentType = params.get("ScalingAdjustmentType")
        self.Threshold = params.get("Threshold")
        self.ComparisonOperator = params.get("ComparisonOperator")
        self.EvaluationPeriods = params.get("EvaluationPeriods")
        self.MetricName = params.get("MetricName")
        self.PolicyType = params.get("PolicyType")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))


class PutScalingPolicyResponse(AbstractModel):
    """PutScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Name: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class ScalingPolicy(AbstractModel):
    """动态扩缩容配置

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ScalingAdjustment: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingAdjustment: str
        :param ScalingAdjustmentType: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingAdjustmentType: str
        :param ComparisonOperator: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComparisonOperator: str
        :param Threshold: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: str
        :param EvaluationPeriods: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type EvaluationPeriods: str
        :param MetricName: 保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param PolicyType: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param TargetConfiguration: 基于规则的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`
        """
        self.FleetId = None
        self.Name = None
        self.Status = None
        self.ScalingAdjustment = None
        self.ScalingAdjustmentType = None
        self.ComparisonOperator = None
        self.Threshold = None
        self.EvaluationPeriods = None
        self.MetricName = None
        self.PolicyType = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ScalingAdjustment = params.get("ScalingAdjustment")
        self.ScalingAdjustmentType = params.get("ScalingAdjustmentType")
        self.ComparisonOperator = params.get("ComparisonOperator")
        self.Threshold = params.get("Threshold")
        self.EvaluationPeriods = params.get("EvaluationPeriods")
        self.MetricName = params.get("MetricName")
        self.PolicyType = params.get("PolicyType")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))


class SearchGameServerSessionsRequest(AbstractModel):
    """SearchGameServerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 舰队ID
        :type FleetId: str
        :param Limit: 单次查询记录数上限
        :type Limit: int
        :param NextToken: 页偏移，用于查询下一页
        :type NextToken: str
        :param FilterExpression: 搜索条件表达式，支持如下变量
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number
hasAvailablePlayerSessions 是否有可用玩家数 String 取值true或false
gameServerSessionProperties 游戏会话属性 String

表达式String类型 等于=，不等于<>判断
表示Number类型支持 =,<>,>,>=,<,<=
        :type FilterExpression: str
        :param SortExpression: 排序条件关键字
支持排序字段
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number
        :type SortExpression: str
        """
        self.AliasId = None
        self.FleetId = None
        self.Limit = None
        self.NextToken = None
        self.FilterExpression = None
        self.SortExpression = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.FilterExpression = params.get("FilterExpression")
        self.SortExpression = params.get("SortExpression")


class SearchGameServerSessionsResponse(AbstractModel):
    """SearchGameServerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessions: 游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GameServerSessions: list of GameServerSession
        :param NextToken: 页偏移，用于查询下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class SetServerWeightRequest(AbstractModel):
    """SetServerWeight请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务舰队ID
        :type FleetId: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Weight: 权重
        :type Weight: int
        """
        self.FleetId = None
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")


class SetServerWeightResponse(AbstractModel):
    """SetServerWeight返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 开始部署游戏服务器会话的唯一标识符
        :type PlacementId: str
        :param GameServerSessionQueueName: 游戏服务器会话队列名称
        :type GameServerSessionQueueName: str
        :param MaximumPlayerSessionCount: 游戏服务器允许同时连接到游戏会话的最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param DesiredPlayerSessions: 玩家游戏会话信息
        :type DesiredPlayerSessions: list of DesiredPlayerSession
        :param GameProperties: 玩家游戏会话属性
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 游戏服务器会话数据
        :type GameServerSessionData: str
        :param GameServerSessionName: 游戏服务器会话名称
        :type GameServerSessionName: str
        :param PlayerLatencies: 玩家延迟
        :type PlayerLatencies: list of PlayerLatency
        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.MaximumPlayerSessionCount = None
        self.DesiredPlayerSessions = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionName = None
        self.PlayerLatencies = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        if params.get("DesiredPlayerSessions") is not None:
            self.DesiredPlayerSessions = []
            for item in params.get("DesiredPlayerSessions"):
                obj = DesiredPlayerSession()
                obj._deserialize(item)
                self.DesiredPlayerSessions.append(obj)
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionName = params.get("GameServerSessionName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class StopGameServerSessionPlacementRequest(AbstractModel):
    """StopGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 游戏服务器会话放置的唯一标识符
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置
        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class TargetConfiguration(AbstractModel):
    """基于规则的动态扩缩容配置项

    """

    def __init__(self):
        """
        :param TargetValue: 预留存率
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetValue: int
        """
        self.TargetValue = None


    def _deserialize(self, params):
        self.TargetValue = params.get("TargetValue")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID
        :type GameServerSessionId: str
        :param MaximumPlayerSessionCount: 最大玩家数量
        :type MaximumPlayerSessionCount: int
        :param Name: 游戏服务器会话名称
        :type Name: str
        :param PlayerSessionCreationPolicy: 玩家会话创建策略（ACCEPT_ALL,DENY_ALL）
        :type PlayerSessionCreationPolicy: str
        :param ProtectionPolicy: 保护策略(NoProtection,TimeLimitProtection,FullProtection)
        :type ProtectionPolicy: str
        """
        self.GameServerSessionId = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.ProtectionPolicy = params.get("ProtectionPolicy")


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSession: 更新后的游戏会话
        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")