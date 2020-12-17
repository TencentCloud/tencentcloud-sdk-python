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


class CreateSDKLoginTokenRequest(AbstractModel):
    """CreateSDKLoginToken请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 应用ID。
        :type SdkAppId: int
        :param SeatUserId: 坐席账号。
        :type SeatUserId: str
        """
        self.SdkAppId = None
        self.SeatUserId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.SeatUserId = params.get("SeatUserId")


class CreateSDKLoginTokenResponse(AbstractModel):
    """CreateSDKLoginToken返回参数结构体

    """

    def __init__(self):
        """
        :param Token: SDK 登录 Token。
        :type Token: str
        :param ExpiredTime: 过期时间戳，Unix 时间戳。
        :type ExpiredTime: int
        :param SdkURL: SDK 加载路径会随着 SDK 的发布而变动。
        :type SdkURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Token = None
        self.ExpiredTime = None
        self.SdkURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.ExpiredTime = params.get("ExpiredTime")
        self.SdkURL = params.get("SdkURL")
        self.RequestId = params.get("RequestId")


class CreateStaffRequest(AbstractModel):
    """CreateStaff请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param Staffs: 客服信息，个数不超过 10
        :type Staffs: list of SeatUserInfo
        """
        self.SdkAppId = None
        self.Staffs = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Staffs") is not None:
            self.Staffs = []
            for item in params.get("Staffs"):
                obj = SeatUserInfo()
                obj._deserialize(item)
                self.Staffs.append(obj)


class CreateStaffResponse(AbstractModel):
    """CreateStaff返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeChatMessagesRequest(AbstractModel):
    """DescribeChatMessages请求参数结构体

    """

    def __init__(self):
        """
        :param CdrId: 服务记录ID
        :type CdrId: str
        :param InstanceId: 实例ID
        :type InstanceId: int
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param Limit: 返回记录条数 最大为100默认20
        :type Limit: int
        :param Offset: 返回记录偏移 默认为0
        :type Offset: int
        :param Order: 1为从早到晚，2为从晚到早，默认为2
        :type Order: int
        """
        self.CdrId = None
        self.InstanceId = None
        self.SdkAppId = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.CdrId = params.get("CdrId")
        self.InstanceId = params.get("InstanceId")
        self.SdkAppId = params.get("SdkAppId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")


class DescribeChatMessagesResponse(AbstractModel):
    """DescribeChatMessages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Messages: 消息列表
        :type Messages: list of MessageBody
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Messages = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Messages") is not None:
            self.Messages = []
            for item in params.get("Messages"):
                obj = MessageBody()
                obj._deserialize(item)
                self.Messages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIMCdrsRequest(AbstractModel):
    """DescribeIMCdrs请求参数结构体

    """

    def __init__(self):
        """
        :param StartTimestamp: 起始时间
        :type StartTimestamp: int
        :param EndTimestamp: 结束时间
        :type EndTimestamp: int
        :param InstanceId: 实例ID
        :type InstanceId: int
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param Limit: 返回记录条数 最大为100默认20
        :type Limit: int
        :param Offset: 返回记录偏移 默认为0
        :type Offset: int
        :param Type: 1为全媒体，2为文本客服，不填则查询全部
        :type Type: int
        """
        self.StartTimestamp = None
        self.EndTimestamp = None
        self.InstanceId = None
        self.SdkAppId = None
        self.Limit = None
        self.Offset = None
        self.Type = None


    def _deserialize(self, params):
        self.StartTimestamp = params.get("StartTimestamp")
        self.EndTimestamp = params.get("EndTimestamp")
        self.InstanceId = params.get("InstanceId")
        self.SdkAppId = params.get("SdkAppId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Type = params.get("Type")


class DescribeIMCdrsResponse(AbstractModel):
    """DescribeIMCdrs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param IMCdrs: 服务记录列表
        :type IMCdrs: list of IMCdrInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.IMCdrs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IMCdrs") is not None:
            self.IMCdrs = []
            for item in params.get("IMCdrs"):
                obj = IMCdrInfo()
                obj._deserialize(item)
                self.IMCdrs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePSTNActiveSessionListRequest(AbstractModel):
    """DescribePSTNActiveSessionList请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 应用 ID
        :type SdkAppId: int
        :param Offset: 数据偏移
        :type Offset: int
        :param Limit: 返回的数据条数，最大 25
        :type Limit: int
        """
        self.SdkAppId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePSTNActiveSessionListResponse(AbstractModel):
    """DescribePSTNActiveSessionList返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 列表总条数
        :type Total: int
        :param Sessions: 列表内容
        :type Sessions: list of PSTNSessionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Sessions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Sessions") is not None:
            self.Sessions = []
            for item in params.get("Sessions"):
                obj = PSTNSessionInfo()
                obj._deserialize(item)
                self.Sessions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTelCallInfoRequest(AbstractModel):
    """DescribeTelCallInfo请求参数结构体

    """

    def __init__(self):
        """
        :param StartTimeStamp: 起始时间戳，Unix 时间戳
        :type StartTimeStamp: int
        :param EndTimeStamp: 结束时间戳，Unix 时间戳，查询时间范围最大为90天
        :type EndTimeStamp: int
        :param SdkAppIdList: 应用ID列表，多个ID时，返回值为多个ID使用总和
        :type SdkAppIdList: list of int
        """
        self.StartTimeStamp = None
        self.EndTimeStamp = None
        self.SdkAppIdList = None


    def _deserialize(self, params):
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")
        self.SdkAppIdList = params.get("SdkAppIdList")


class DescribeTelCallInfoResponse(AbstractModel):
    """DescribeTelCallInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TelCallOutCount: 电话呼出统计分钟数
        :type TelCallOutCount: int
        :param TelCallInCount: 电话呼入统计分钟数
        :type TelCallInCount: int
        :param SeatUsedCount: 坐席使用统计个数
        :type SeatUsedCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TelCallOutCount = None
        self.TelCallInCount = None
        self.SeatUsedCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TelCallOutCount = params.get("TelCallOutCount")
        self.TelCallInCount = params.get("TelCallInCount")
        self.SeatUsedCount = params.get("SeatUsedCount")
        self.RequestId = params.get("RequestId")


class DescribeTelCdrRequest(AbstractModel):
    """DescribeTelCdr请求参数结构体

    """

    def __init__(self):
        """
        :param StartTimeStamp: 起始时间戳，Unix 时间戳
        :type StartTimeStamp: int
        :param EndTimeStamp: 结束时间戳，Unix 时间戳
        :type EndTimeStamp: int
        :param Limit: 返回记录条数，上限 100
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param InstanceId: 实例 ID
        :type InstanceId: int
        :param SdkAppId: 应用ID。
        :type SdkAppId: int
        """
        self.StartTimeStamp = None
        self.EndTimeStamp = None
        self.Limit = None
        self.Offset = None
        self.InstanceId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstanceId = params.get("InstanceId")
        self.SdkAppId = params.get("SdkAppId")


class DescribeTelCdrResponse(AbstractModel):
    """DescribeTelCdr返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 话单记录总数
        :type TotalCount: int
        :param TelCdrs: 话单记录
        :type TelCdrs: list of TelCdrInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TelCdrs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TelCdrs") is not None:
            self.TelCdrs = []
            for item in params.get("TelCdrs"):
                obj = TelCdrInfo()
                obj._deserialize(item)
                self.TelCdrs.append(obj)
        self.RequestId = params.get("RequestId")


class IMCdrInfo(AbstractModel):
    """全媒体服务记录信息

    """

    def __init__(self):
        """
        :param Id: 服务记录ID
        :type Id: str
        :param Duration: 服务时长秒数
        :type Duration: int
        :param EndStatus: 结束状态
        :type EndStatus: int
        :param Nickname: 用户昵称
        :type Nickname: str
        :param Type: 服务类型 1为全媒体，2为文本客服
        :type Type: int
        :param StaffId: 客服ID
        :type StaffId: str
        :param Timestamp: 服务时间戳
        :type Timestamp: int
        """
        self.Id = None
        self.Duration = None
        self.EndStatus = None
        self.Nickname = None
        self.Type = None
        self.StaffId = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Duration = params.get("Duration")
        self.EndStatus = params.get("EndStatus")
        self.Nickname = params.get("Nickname")
        self.Type = params.get("Type")
        self.StaffId = params.get("StaffId")
        self.Timestamp = params.get("Timestamp")


class Message(AbstractModel):
    """单条消息

    """

    def __init__(self):
        """
        :param Type: 消息类型
        :type Type: str
        :param Content: 消息内容
        :type Content: str
        """
        self.Type = None
        self.Content = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Content = params.get("Content")


class MessageBody(AbstractModel):
    """聊天消息

    """

    def __init__(self):
        """
        :param Timestamp: 消息时间戳
        :type Timestamp: int
        :param From: 发消息的用户ID
        :type From: str
        :param Messages: 消息列表
        :type Messages: list of Message
        """
        self.Timestamp = None
        self.From = None
        self.Messages = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.From = params.get("From")
        if params.get("Messages") is not None:
            self.Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self.Messages.append(obj)


class PSTNSessionInfo(AbstractModel):
    """PSTN 会话信息

    """

    def __init__(self):
        """
        :param SessionID: 会话 ID
        :type SessionID: str
        :param RoomID: 会话临时房间 ID
        :type RoomID: str
        :param Caller: 主叫
        :type Caller: str
        :param Callee: 被叫
        :type Callee: str
        :param StartTimestamp: 开始时间，Unix 时间戳
        :type StartTimestamp: str
        :param AcceptTimestamp: 接听时间，Unix 时间戳
        :type AcceptTimestamp: str
        :param StaffEmail: 坐席邮箱
        :type StaffEmail: str
        :param StaffNumber: 坐席工号
        :type StaffNumber: str
        :param SessionStatus: 坐席状态 inProgress 进行中
        :type SessionStatus: str
        :param Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出
        :type Direction: int
        :param RingTimestamp: 振铃时间，Unix 时间戳
        :type RingTimestamp: int
        """
        self.SessionID = None
        self.RoomID = None
        self.Caller = None
        self.Callee = None
        self.StartTimestamp = None
        self.AcceptTimestamp = None
        self.StaffEmail = None
        self.StaffNumber = None
        self.SessionStatus = None
        self.Direction = None
        self.RingTimestamp = None


    def _deserialize(self, params):
        self.SessionID = params.get("SessionID")
        self.RoomID = params.get("RoomID")
        self.Caller = params.get("Caller")
        self.Callee = params.get("Callee")
        self.StartTimestamp = params.get("StartTimestamp")
        self.AcceptTimestamp = params.get("AcceptTimestamp")
        self.StaffEmail = params.get("StaffEmail")
        self.StaffNumber = params.get("StaffNumber")
        self.SessionStatus = params.get("SessionStatus")
        self.Direction = params.get("Direction")
        self.RingTimestamp = params.get("RingTimestamp")


class SeatUserInfo(AbstractModel):
    """坐席用户信息

    """

    def __init__(self):
        """
        :param Name: 坐席名称
        :type Name: str
        :param Mail: 坐席邮箱
        :type Mail: str
        :param Phone: 坐席电话号码
        :type Phone: str
        :param Nick: 坐席昵称
        :type Nick: str
        :param UserId: 用户ID
        :type UserId: str
        :param SkillGroupNameList: 坐席关联的技能组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupNameList: list of str
        :param StaffNumber: 工号
注意：此字段可能返回 null，表示取不到有效值。
        :type StaffNumber: str
        """
        self.Name = None
        self.Mail = None
        self.Phone = None
        self.Nick = None
        self.UserId = None
        self.SkillGroupNameList = None
        self.StaffNumber = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Mail = params.get("Mail")
        self.Phone = params.get("Phone")
        self.Nick = params.get("Nick")
        self.UserId = params.get("UserId")
        self.SkillGroupNameList = params.get("SkillGroupNameList")
        self.StaffNumber = params.get("StaffNumber")


class TelCdrInfo(AbstractModel):
    """电话话单信息

    """

    def __init__(self):
        """
        :param Caller: 主叫号码
        :type Caller: str
        :param Callee: 被叫号码
        :type Callee: str
        :param Time: 呼叫发起时间戳，Unix 时间戳
        :type Time: int
        :param Direction: 呼入呼出方向 0 呼入 1 呼出
        :type Direction: int
        :param Duration: 通话时长
        :type Duration: int
        :param RecordURL: 录音信息
        :type RecordURL: str
        :param SeatUser: 坐席信息
        :type SeatUser: :class:`tencentcloud.ccc.v20200210.models.SeatUserInfo`
        :param EndStatus: 结束状态 0 未知 1 正常通话 2 未接通
        :type EndStatus: int
        :param SkillGroup: 技能组
        :type SkillGroup: str
        :param CallerLocation: 主叫归属地
        :type CallerLocation: str
        """
        self.Caller = None
        self.Callee = None
        self.Time = None
        self.Direction = None
        self.Duration = None
        self.RecordURL = None
        self.SeatUser = None
        self.EndStatus = None
        self.SkillGroup = None
        self.CallerLocation = None


    def _deserialize(self, params):
        self.Caller = params.get("Caller")
        self.Callee = params.get("Callee")
        self.Time = params.get("Time")
        self.Direction = params.get("Direction")
        self.Duration = params.get("Duration")
        self.RecordURL = params.get("RecordURL")
        if params.get("SeatUser") is not None:
            self.SeatUser = SeatUserInfo()
            self.SeatUser._deserialize(params.get("SeatUser"))
        self.EndStatus = params.get("EndStatus")
        self.SkillGroup = params.get("SkillGroup")
        self.CallerLocation = params.get("CallerLocation")