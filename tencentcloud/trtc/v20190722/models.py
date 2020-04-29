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


class DescribeCallDetailRequest(AbstractModel):
    """DescribeCallDetail请求参数结构体

    """

    def __init__(self):
        """
        :param CommId: 通话ID
        :type CommId: str
        :param StartTime: 查询开始时间
        :type StartTime: int
        :param EndTime: 查询结束时间
        :type EndTime: int
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param UserIds: 需查询的用户数组，不填默认返回6个用户
        :type UserIds: list of str
        :param DataType: 需查询的指标，不填则只返回用户列表，填all则返回所有指标。
appCpu：APP CPU使用率；
sysCpu：系统 CPU使用率；
aBit：上/下行音频码率；
aBlock：音频卡顿时长；
vBit：上/下行视频码率；
vCapFps：视频采集帧率；
vEncFps：视频发送帧率；
vDecFps：渲染帧率；
vBlock：视频卡顿时长；
aLoss：上/下行音频丢包；
vLoss：上/下行视频丢包；
vWidth：上/下行分辨率宽；
vHeight：上/下行分辨率高
        :type DataType: list of str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.DataType = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.DataType = params.get("DataType")


class DescribeCallDetailResponse(AbstractModel):
    """DescribeCallDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 返回的用户总条数
        :type Total: int
        :param UserList: 用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param Data: 质量数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of QualityData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeNetworkRequest(AbstractModel):
    """DescribeRealtimeNetwork请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间
        :type StartTime: int
        :param EndTime: 查询结束时间
        :type EndTime: int
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param DataType: 需查询的数据类型
sendLossRateRaw：上行丢包率；
recvLossRateRaw：下行丢包率
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeNetworkResponse(AbstractModel):
    """DescribeRealtimeNetwork返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 查询返回的数据
        :type Data: list of RealtimeData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeQualityRequest(AbstractModel):
    """DescribeRealtimeQuality请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间
        :type StartTime: int
        :param EndTime: 查询结束时间
        :type EndTime: int
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param DataType: 查询的数据类型
enterTotalSuccPercent：进房成功率
fistFreamInSecRate：首帧秒开率
blockPercent：视频卡顿率
audioBlockPercent：音频卡顿率
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeQualityResponse(AbstractModel):
    """DescribeRealtimeQuality返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回的数据类型
        :type Data: list of RealtimeData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeScaleRequest(AbstractModel):
    """DescribeRealtimeScale请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询开始时间
        :type StartTime: int
        :param EndTime: 查询结束时间
        :type EndTime: int
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param DataType: 查询的数据类型
UserNum：通话人数；
RoomNum：房间数
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeScaleResponse(AbstractModel):
    """DescribeRealtimeScale返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回的数据数组
        :type Data: list of RealtimeData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoomInformationRequest(AbstractModel):
    """DescribeRoomInformation请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 用户sdkappid
        :type SdkAppId: str
        :param StartTime: 查询开始时间
        :type StartTime: int
        :param EndTime: 查询结束时间
        :type EndTime: int
        :param RoomId: 数字房间号
        :type RoomId: str
        :param PageNumber: 分页index（不填默认只返回10个）
        :type PageNumber: str
        :param PageSize: 分页大小（不填默认返回10个,最多不超过100条）
        :type PageSize: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")


class DescribeRoomInformationResponse(AbstractModel):
    """DescribeRoomInformation返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 返回的数据总条数
        :type Total: int
        :param RoomList: 房间信息列表
        :type RoomList: list of RoomState
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.RoomList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RoomList") is not None:
            self.RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self.RoomList.append(obj)
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
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


class QualityData(AbstractModel):
    """Es返回的质量数据

    """

    def __init__(self):
        """
        :param Content: 数据内容
        :type Content: list of TimeValue
        :param UserId: 用户ID
        :type UserId: str
        :param PeerId: 对端Id,为空时表示上行数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerId: str
        :param DataType: 数据类型
        :type DataType: str
        """
        self.Content = None
        self.UserId = None
        self.PeerId = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.UserId = params.get("UserId")
        self.PeerId = params.get("PeerId")
        self.DataType = params.get("DataType")


class RealtimeData(AbstractModel):
    """查询秒级监控返回的数据

    """

    def __init__(self):
        """
        :param Content: 返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of TimeValue
        :param DataType: 数据类型字段
        :type DataType: str
        """
        self.Content = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.DataType = params.get("DataType")


class RemoveUserRequest(AbstractModel):
    """RemoveUser请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        :param UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")


class RemoveUserResponse(AbstractModel):
    """RemoveUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoomState(AbstractModel):
    """房间信息列表

    """

    def __init__(self):
        """
        :param CommId: 通话ID（唯一标识一次通话）
        :type CommId: str
        :param RoomString: 房间号
        :type RoomString: str
        :param CreateTime: 房间创建时间
        :type CreateTime: int
        :param DestroyTime: 房间销毁时间
        :type DestroyTime: int
        :param IsFinished: 房间是否已经结束
        :type IsFinished: bool
        :param UserId: 房间创建者Id
        :type UserId: str
        """
        self.CommId = None
        self.RoomString = None
        self.CreateTime = None
        self.DestroyTime = None
        self.IsFinished = None
        self.UserId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.RoomString = params.get("RoomString")
        self.CreateTime = params.get("CreateTime")
        self.DestroyTime = params.get("DestroyTime")
        self.IsFinished = params.get("IsFinished")
        self.UserId = params.get("UserId")


class TimeValue(AbstractModel):
    """返回的质量数据，时间:值

    """

    def __init__(self):
        """
        :param Time: 时间
        :type Time: int
        :param Value: 当前时间取值
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class UserInformation(AbstractModel):
    """用户信息，包括用户进房时间，退房时间等

    """

    def __init__(self):
        """
        :param RoomStr: 房间号
        :type RoomStr: str
        :param UserId: 用户Id
        :type UserId: str
        :param JoinTs: 用户进房事件
        :type JoinTs: int
        :param LeaveTs: 用户退房时间
        :type LeaveTs: int
        :param DeviceType: 终端类型
        :type DeviceType: str
        :param SdkVersion: Sdk版本号
        :type SdkVersion: str
        :param ClientIp: 客户端IP地址
        :type ClientIp: str
        """
        self.RoomStr = None
        self.UserId = None
        self.JoinTs = None
        self.LeaveTs = None
        self.DeviceType = None
        self.SdkVersion = None
        self.ClientIp = None


    def _deserialize(self, params):
        self.RoomStr = params.get("RoomStr")
        self.UserId = params.get("UserId")
        self.JoinTs = params.get("JoinTs")
        self.LeaveTs = params.get("LeaveTs")
        self.DeviceType = params.get("DeviceType")
        self.SdkVersion = params.get("SdkVersion")
        self.ClientIp = params.get("ClientIp")