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


class CreateSessionRequest(AbstractModel):
    """CreateSession请求参数结构体

    """

    def __init__(self):
        """
        :param ClientSession: 客户端session信息，从JSSDK请求中获得
        :type ClientSession: str
        :param UserId: 游戏用户ID
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        :param GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等
        :type GameRegion: str
        :param GameParas: 游戏参数
        :type GameParas: str
        :param Resolution: 分辨率,，可设置为1080p或720p
        :type Resolution: str
        :param ImageUrl: 背景图url，格式为png或jpeg，宽高1920*1080
        :type ImageUrl: str
        :param SetNo: 资源池编号，1表示正式，2表示测试
        :type SetNo: int
        :param Bitrate: 单位Mbps，固定码率，后端不动态调整(MaxBitrate和MinBitrate将无效)
        :type Bitrate: int
        :param MaxBitrate: 单位Mbps，动态调整最大码率
        :type MaxBitrate: int
        :param MinBitrate: 单位Mbps，动态调整最小码率
        :type MinBitrate: int
        :param Fps: 帧率，可设置为30、45或60
        :type Fps: int
        :param UserIp: 游戏用户IP，用于就近调度，例如125.127.178.228
        :type UserIp: str
        :param Optimization: 优化项，便于客户灰度开启新的优化项，默认为0
        :type Optimization: int
        """
        self.ClientSession = None
        self.UserId = None
        self.GameId = None
        self.GameRegion = None
        self.GameParas = None
        self.Resolution = None
        self.ImageUrl = None
        self.SetNo = None
        self.Bitrate = None
        self.MaxBitrate = None
        self.MinBitrate = None
        self.Fps = None
        self.UserIp = None
        self.Optimization = None


    def _deserialize(self, params):
        self.ClientSession = params.get("ClientSession")
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        self.GameRegion = params.get("GameRegion")
        self.GameParas = params.get("GameParas")
        self.Resolution = params.get("Resolution")
        self.ImageUrl = params.get("ImageUrl")
        self.SetNo = params.get("SetNo")
        self.Bitrate = params.get("Bitrate")
        self.MaxBitrate = params.get("MaxBitrate")
        self.MinBitrate = params.get("MinBitrate")
        self.Fps = params.get("Fps")
        self.UserIp = params.get("UserIp")
        self.Optimization = params.get("Optimization")


class CreateSessionResponse(AbstractModel):
    """CreateSession返回参数结构体

    """

    def __init__(self):
        """
        :param ServerSession: 服务端session信息，返回给JSSDK
        :type ServerSession: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServerSession = params.get("ServerSession")
        self.RequestId = params.get("RequestId")


class DescribeWorkersInfoRequest(AbstractModel):
    """DescribeWorkersInfo请求参数结构体

    """


class DescribeWorkersInfoResponse(AbstractModel):
    """DescribeWorkersInfo返回参数结构体

    """

    def __init__(self):
        """
        :param WorkerNum: 机器数量
        :type WorkerNum: int
        :param WorkerDetail: 机器详细信息
        :type WorkerDetail: list of WorkerDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkerNum = None
        self.WorkerDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkerNum = params.get("WorkerNum")
        if params.get("WorkerDetail") is not None:
            self.WorkerDetail = []
            for item in params.get("WorkerDetail"):
                obj = WorkerDetail()
                obj._deserialize(item)
                self.WorkerDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkersRequest(AbstractModel):
    """DescribeWorkers请求参数结构体

    """

    def __init__(self):
        """
        :param SetNo: 资源池编号，1表示正式，2表示测试
        :type SetNo: int
        """
        self.SetNo = None


    def _deserialize(self, params):
        self.SetNo = params.get("SetNo")


class DescribeWorkersResponse(AbstractModel):
    """DescribeWorkers返回参数结构体

    """

    def __init__(self):
        """
        :param Idle: 空闲机器总数量
        :type Idle: int
        :param RegionNum: 区域个数
        :type RegionNum: int
        :param RegionDetail: 各个区域的机器情况
        :type RegionDetail: list of WorkerRegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Idle = None
        self.RegionNum = None
        self.RegionDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Idle = params.get("Idle")
        self.RegionNum = params.get("RegionNum")
        if params.get("RegionDetail") is not None:
            self.RegionDetail = []
            for item in params.get("RegionDetail"):
                obj = WorkerRegionInfo()
                obj._deserialize(item)
                self.RegionDetail.append(obj)
        self.RequestId = params.get("RequestId")


class EnterQueueRequest(AbstractModel):
    """EnterQueue请求参数结构体

    """

    def __init__(self):
        """
        :param First: true：第一次请求排队 false：已在排队中，查询当前排名
        :type First: bool
        :param GameId: 游戏ID
        :type GameId: str
        :param UserId: 用户ID
        :type UserId: str
        :param SetNumber: 资源池编号
        :type SetNumber: int
        """
        self.First = None
        self.GameId = None
        self.UserId = None
        self.SetNumber = None


    def _deserialize(self, params):
        self.First = params.get("First")
        self.GameId = params.get("GameId")
        self.UserId = params.get("UserId")
        self.SetNumber = params.get("SetNumber")


class EnterQueueResponse(AbstractModel):
    """EnterQueue返回参数结构体

    """

    def __init__(self):
        """
        :param Rank: 排名
        :type Rank: int
        :param LockSuccess: 机器锁定成功
        :type LockSuccess: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rank = None
        self.LockSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Rank = params.get("Rank")
        self.LockSuccess = params.get("LockSuccess")
        self.RequestId = params.get("RequestId")


class ModifyWorkersRequest(AbstractModel):
    """ModifyWorkers请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 批量机器ID，最多不超过100个
        :type InstanceIds: list of str
        :param SetNo: 资源池编号，修改有效范围为[1,100]，在idle状态下才能修改成功
        :type SetNo: int
        """
        self.InstanceIds = None
        self.SetNo = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SetNo = params.get("SetNo")


class ModifyWorkersResponse(AbstractModel):
    """ModifyWorkers返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QuitQueueRequest(AbstractModel):
    """QuitQueue请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户ID
        :type UserId: str
        :param SetNumber: 资源池编号
        :type SetNumber: int
        """
        self.UserId = None
        self.SetNumber = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.SetNumber = params.get("SetNumber")


class QuitQueueResponse(AbstractModel):
    """QuitQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    """StopGame请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 游戏用户ID
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")


class StopGameResponse(AbstractModel):
    """StopGame返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrylockWorkerRequest(AbstractModel):
    """TrylockWorker请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 游戏用户ID
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        :param GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等
        :type GameRegion: str
        :param SetNo: 资源池编号，1表示共用，2表示测试
        :type SetNo: int
        :param UserIp: 游戏用户IP，用于就近调度，例如125.127.178.228
        :type UserIp: str
        """
        self.UserId = None
        self.GameId = None
        self.GameRegion = None
        self.SetNo = None
        self.UserIp = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        self.GameRegion = params.get("GameRegion")
        self.SetNo = params.get("SetNo")
        self.UserIp = params.get("UserIp")


class TrylockWorkerResponse(AbstractModel):
    """TrylockWorker返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WorkerDetail(AbstractModel):
    """机器详细信息

    """

    def __init__(self):
        """
        :param AppId: 客户appid
        :type AppId: int
        :param SetNo: 资源池编号
        :type SetNo: int
        :param Region: 机器所属区域
        :type Region: str
        :param InstanceId: 机器ID
        :type InstanceId: str
        :param InstanceType: 机器类型：
LARGE-大型
MEDIUM-中型
SMALL-小型
        :type InstanceType: str
        :param Ip: 机器IP
        :type Ip: str
        :param ServiceState: 服务状态：
IDLE-空闲
LOCK-锁定
ESTABLISHED-游戏中
RECONNECT-等待重连
RECOVERY-清理恢复
FORBID-禁用
UNAVAILABLE-不可用
        :type ServiceState: str
        :param UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param GameId: 游戏ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GameId: str
        """
        self.AppId = None
        self.SetNo = None
        self.Region = None
        self.InstanceId = None
        self.InstanceType = None
        self.Ip = None
        self.ServiceState = None
        self.UserId = None
        self.GameId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.SetNo = params.get("SetNo")
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        self.InstanceType = params.get("InstanceType")
        self.Ip = params.get("Ip")
        self.ServiceState = params.get("ServiceState")
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")


class WorkerRegionInfo(AbstractModel):
    """worker的区域信息

    """

    def __init__(self):
        """
        :param Region: 区域
        :type Region: str
        :param Idle: 该区域空闲机器数量
        :type Idle: int
        """
        self.Region = None
        self.Idle = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Idle = params.get("Idle")