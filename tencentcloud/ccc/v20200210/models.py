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


class BindStaffSkillGroupListRequest(AbstractModel):
    """BindStaffSkillGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 实例ID
        :type SdkAppId: int
        :param StaffEmail: 坐席邮箱
        :type StaffEmail: str
        :param SkillGroupList: 绑定技能组列表
        :type SkillGroupList: list of int
        """
        self.SdkAppId = None
        self.StaffEmail = None
        self.SkillGroupList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StaffEmail = params.get("StaffEmail")
        self.SkillGroupList = params.get("SkillGroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindStaffSkillGroupListResponse(AbstractModel):
    """BindStaffSkillGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CallInMetrics(AbstractModel):
    """呼入实时指标

    """

    def __init__(self):
        r"""
        :param IvrCount: IVR驻留数量
        :type IvrCount: int
        :param QueueCount: 排队中数量
        :type QueueCount: int
        :param RingCount: 振铃中数量
        :type RingCount: int
        :param AcceptCount: 接通中数量
        :type AcceptCount: int
        :param TransferOuterCount: 客服转接外线中数量
        :type TransferOuterCount: int
        :param MaxQueueDuration: 最大排队时长
        :type MaxQueueDuration: int
        :param AvgQueueDuration: 平均排队时长
        :type AvgQueueDuration: int
        :param MaxRingDuration: 最大振铃时长
        :type MaxRingDuration: int
        :param AvgRingDuration: 平均振铃时长
        :type AvgRingDuration: int
        :param MaxAcceptDuration: 最大接通时长
        :type MaxAcceptDuration: int
        :param AvgAcceptDuration: 平均接通时长
        :type AvgAcceptDuration: int
        """
        self.IvrCount = None
        self.QueueCount = None
        self.RingCount = None
        self.AcceptCount = None
        self.TransferOuterCount = None
        self.MaxQueueDuration = None
        self.AvgQueueDuration = None
        self.MaxRingDuration = None
        self.AvgRingDuration = None
        self.MaxAcceptDuration = None
        self.AvgAcceptDuration = None


    def _deserialize(self, params):
        self.IvrCount = params.get("IvrCount")
        self.QueueCount = params.get("QueueCount")
        self.RingCount = params.get("RingCount")
        self.AcceptCount = params.get("AcceptCount")
        self.TransferOuterCount = params.get("TransferOuterCount")
        self.MaxQueueDuration = params.get("MaxQueueDuration")
        self.AvgQueueDuration = params.get("AvgQueueDuration")
        self.MaxRingDuration = params.get("MaxRingDuration")
        self.AvgRingDuration = params.get("AvgRingDuration")
        self.MaxAcceptDuration = params.get("MaxAcceptDuration")
        self.AvgAcceptDuration = params.get("AvgAcceptDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInNumberMetrics(AbstractModel):
    """呼入线路维度相关指标

    """

    def __init__(self):
        r"""
        :param Number: 线路号码
        :type Number: str
        :param Metrics: 线路相关指标
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param SkillGroupMetrics: 所属技能组相关指标
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        """
        self.Number = None
        self.Metrics = None
        self.SkillGroupMetrics = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        if params.get("Metrics") is not None:
            self.Metrics = CallInMetrics()
            self.Metrics._deserialize(params.get("Metrics"))
        if params.get("SkillGroupMetrics") is not None:
            self.SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self.SkillGroupMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInSkillGroupMetrics(AbstractModel):
    """呼入技能组相关指标

    """

    def __init__(self):
        r"""
        :param SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param Metrics: 数据指标
        :type Metrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param Name: 技能组名称
        :type Name: str
        """
        self.SkillGroupId = None
        self.Metrics = None
        self.Name = None


    def _deserialize(self, params):
        self.SkillGroupId = params.get("SkillGroupId")
        if params.get("Metrics") is not None:
            self.Metrics = CallInMetrics()
            self.Metrics._deserialize(params.get("Metrics"))
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSDKLoginTokenRequest(AbstractModel):
    """CreateSDKLoginToken请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSDKLoginTokenResponse(AbstractModel):
    """CreateSDKLoginToken返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStaffResponse(AbstractModel):
    """CreateStaff返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorStaffList: 错误坐席列表及错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorStaffList: list of ErrStaffItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorStaffList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ErrorStaffList") is not None:
            self.ErrorStaffList = []
            for item in params.get("ErrorStaffList"):
                obj = ErrStaffItem()
                obj._deserialize(item)
                self.ErrorStaffList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateUserSigRequest(AbstractModel):
    """CreateUserSig请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用 ID
        :type SdkAppId: int
        :param Uid: 用户 ID
        :type Uid: str
        :param ExpiredTime: 有效期，单位秒，不超过 1 小时
        :type ExpiredTime: int
        :param ClientData: 用户签名数据
        :type ClientData: str
        """
        self.SdkAppId = None
        self.Uid = None
        self.ExpiredTime = None
        self.ClientData = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Uid = params.get("Uid")
        self.ExpiredTime = params.get("ExpiredTime")
        self.ClientData = params.get("ClientData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSigResponse(AbstractModel):
    """CreateUserSig返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserSig: 签名结果
        :type UserSig: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserSig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserSig = params.get("UserSig")
        self.RequestId = params.get("RequestId")


class DeleteStaffRequest(AbstractModel):
    """DeleteStaff请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 实例ID
        :type SdkAppId: int
        :param StaffList: 待删除客服邮箱列表
        :type StaffList: list of str
        """
        self.SdkAppId = None
        self.StaffList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StaffList = params.get("StaffList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStaffResponse(AbstractModel):
    """DeleteStaff返回参数结构体

    """

    def __init__(self):
        r"""
        :param OnlineStaffList: 无法删除的状态为在线的客服列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineStaffList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OnlineStaffList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineStaffList = params.get("OnlineStaffList")
        self.RequestId = params.get("RequestId")


class DescribeCallInMetricsRequest(AbstractModel):
    """DescribeCallInMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 实例ID
        :type SdkAppId: int
        :param EnabledSkillGroup: 是否返回技能组维度信息，默认“是”
        :type EnabledSkillGroup: bool
        :param EnabledNumber: 是否返回线路维度信息，默认“否”
        :type EnabledNumber: bool
        """
        self.SdkAppId = None
        self.EnabledSkillGroup = None
        self.EnabledNumber = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.EnabledSkillGroup = params.get("EnabledSkillGroup")
        self.EnabledNumber = params.get("EnabledNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallInMetricsResponse(AbstractModel):
    """DescribeCallInMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Timestamp: 时间戳
        :type Timestamp: int
        :param TotalMetrics: 总体指标
        :type TotalMetrics: :class:`tencentcloud.ccc.v20200210.models.CallInMetrics`
        :param NumberMetrics: 线路维度指标
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberMetrics: list of CallInNumberMetrics
        :param SkillGroupMetrics: 技能组维度指标
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupMetrics: list of CallInSkillGroupMetrics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Timestamp = None
        self.TotalMetrics = None
        self.NumberMetrics = None
        self.SkillGroupMetrics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        if params.get("TotalMetrics") is not None:
            self.TotalMetrics = CallInMetrics()
            self.TotalMetrics._deserialize(params.get("TotalMetrics"))
        if params.get("NumberMetrics") is not None:
            self.NumberMetrics = []
            for item in params.get("NumberMetrics"):
                obj = CallInNumberMetrics()
                obj._deserialize(item)
                self.NumberMetrics.append(obj)
        if params.get("SkillGroupMetrics") is not None:
            self.SkillGroupMetrics = []
            for item in params.get("SkillGroupMetrics"):
                obj = CallInSkillGroupMetrics()
                obj._deserialize(item)
                self.SkillGroupMetrics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeChatMessagesRequest(AbstractModel):
    """DescribeChatMessages请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChatMessagesResponse(AbstractModel):
    """DescribeChatMessages返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIMCdrsResponse(AbstractModel):
    """DescribeIMCdrs返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePSTNActiveSessionListResponse(AbstractModel):
    """DescribePSTNActiveSessionList返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeSeatUserListRequest(AbstractModel):
    """DescribeSeatUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSeatUserListResponse(AbstractModel):
    """DescribeSeatUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 此实例的坐席用户总数
        :type TotalCount: int
        :param SeatUsers: 坐席用户信息列表
        :type SeatUsers: list of SeatUserInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SeatUsers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SeatUsers") is not None:
            self.SeatUsers = []
            for item in params.get("SeatUsers"):
                obj = SeatUserInfo()
                obj._deserialize(item)
                self.SeatUsers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSkillGroupInfoListRequest(AbstractModel):
    """DescribeSkillGroupInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param SkillGroupId: 技能组ID，查询单个技能组时使用
        :type SkillGroupId: int
        :param ModifiedTime: 查询修改时间大于等于ModifiedTime的技能组时使用
        :type ModifiedTime: int
        """
        self.SdkAppId = None
        self.PageSize = None
        self.PageNumber = None
        self.SkillGroupId = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.SkillGroupId = params.get("SkillGroupId")
        self.ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillGroupInfoListResponse(AbstractModel):
    """DescribeSkillGroupInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 技能组总数
        :type TotalCount: int
        :param SkillGroupList: 技能组信息列表
        :type SkillGroupList: list of SkillGroupInfoItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SkillGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SkillGroupList") is not None:
            self.SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupInfoItem()
                obj._deserialize(item)
                self.SkillGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStaffInfoListRequest(AbstractModel):
    """DescribeStaffInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param StaffMail: 坐席账号，查询单个坐席时使用
        :type StaffMail: str
        :param ModifiedTime: 查询修改时间大于等于ModifiedTime的坐席时使用
        :type ModifiedTime: int
        """
        self.SdkAppId = None
        self.PageSize = None
        self.PageNumber = None
        self.StaffMail = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.StaffMail = params.get("StaffMail")
        self.ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffInfoListResponse(AbstractModel):
    """DescribeStaffInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 坐席用户总数
        :type TotalCount: int
        :param StaffList: 坐席用户信息列表
        :type StaffList: list of StaffInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.StaffList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("StaffList") is not None:
            self.StaffList = []
            for item in params.get("StaffList"):
                obj = StaffInfo()
                obj._deserialize(item)
                self.StaffList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStaffStatusMetricsRequest(AbstractModel):
    """DescribeStaffStatusMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 实例ID
        :type SdkAppId: int
        :param StaffList: 筛选坐席列表，默认不传返回全部坐席信息
        :type StaffList: list of str
        """
        self.SdkAppId = None
        self.StaffList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StaffList = params.get("StaffList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStaffStatusMetricsResponse(AbstractModel):
    """DescribeStaffStatusMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Metrics: 坐席状态实时信息
        :type Metrics: list of StaffStatusMetrics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Metrics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = StaffStatusMetrics()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTelCallInfoRequest(AbstractModel):
    """DescribeTelCallInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCallInfoResponse(AbstractModel):
    """DescribeTelCallInfo返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param StartTimeStamp: 起始时间戳，Unix 时间戳
        :type StartTimeStamp: int
        :param EndTimeStamp: 结束时间戳，Unix 时间戳
        :type EndTimeStamp: int
        :param Limit: 返回数据条数，上限（deprecated）
        :type Limit: int
        :param Offset: 偏移（deprecated）
        :type Offset: int
        :param InstanceId: 实例 ID（deprecated）
        :type InstanceId: int
        :param SdkAppId: 应用 ID
        :type SdkAppId: int
        :param PageSize: 分页尺寸，上限 100
        :type PageSize: int
        :param PageNumber: 分页页码，从 0 开始
        :type PageNumber: int
        :param Phones: 按手机号筛选
        :type Phones: list of str
        """
        self.StartTimeStamp = None
        self.EndTimeStamp = None
        self.Limit = None
        self.Offset = None
        self.InstanceId = None
        self.SdkAppId = None
        self.PageSize = None
        self.PageNumber = None
        self.Phones = None


    def _deserialize(self, params):
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstanceId = params.get("InstanceId")
        self.SdkAppId = params.get("SdkAppId")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.Phones = params.get("Phones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelCdrResponse(AbstractModel):
    """DescribeTelCdr返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeTelSessionRequest(AbstractModel):
    """DescribeTelSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param SessionId: 会话ID
        :type SessionId: str
        """
        self.SdkAppId = None
        self.SessionId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTelSessionResponse(AbstractModel):
    """DescribeTelSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param Session: 会话信息
        :type Session: :class:`tencentcloud.ccc.v20200210.models.PSTNSession`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Session = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Session") is not None:
            self.Session = PSTNSession()
            self.Session._deserialize(params.get("Session"))
        self.RequestId = params.get("RequestId")


class ErrStaffItem(AbstractModel):
    """批量添加客服时，返回出错客服的像个信息

    """

    def __init__(self):
        r"""
        :param StaffEmail: 坐席邮箱地址
        :type StaffEmail: str
        :param Code: 错误码
        :type Code: str
        :param Message: 错误描述
        :type Message: str
        """
        self.StaffEmail = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.StaffEmail = params.get("StaffEmail")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IMCdrInfo(AbstractModel):
    """全媒体服务记录信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IVRKeyPressedElement(AbstractModel):
    """ivr 按键信息

    """

    def __init__(self):
        r"""
        :param Key: 按键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Label: 按键关联的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        """
        self.Key = None
        self.Label = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Message(AbstractModel):
    """单条消息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageBody(AbstractModel):
    """聊天消息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSession(AbstractModel):
    """PSTN 会话类型。

    """

    def __init__(self):
        r"""
        :param SessionID: 会话 ID
        :type SessionID: str
        :param RoomID: 会话临时房间 ID
        :type RoomID: str
        :param Caller: 主叫
        :type Caller: str
        :param Callee: 被叫
        :type Callee: str
        :param StartTimestamp: 开始时间，Unix 时间戳
        :type StartTimestamp: int
        :param RingTimestamp: 振铃时间，Unix 时间戳
        :type RingTimestamp: int
        :param AcceptTimestamp: 接听时间，Unix 时间戳
        :type AcceptTimestamp: int
        :param StaffEmail: 坐席邮箱
        :type StaffEmail: str
        :param StaffNumber: 坐席工号
        :type StaffNumber: str
        :param SessionStatus: 会话状态
ringing 振铃中
seatJoining  等待坐席接听
inProgress 进行中
finished 已完成
        :type SessionStatus: str
        :param Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出
        :type Direction: int
        :param OutBoundCaller: 转外线使用的号码（转外线主叫）
        :type OutBoundCaller: str
        :param OutBoundCallee: 转外线被叫
        :type OutBoundCallee: str
        """
        self.SessionID = None
        self.RoomID = None
        self.Caller = None
        self.Callee = None
        self.StartTimestamp = None
        self.RingTimestamp = None
        self.AcceptTimestamp = None
        self.StaffEmail = None
        self.StaffNumber = None
        self.SessionStatus = None
        self.Direction = None
        self.OutBoundCaller = None
        self.OutBoundCallee = None


    def _deserialize(self, params):
        self.SessionID = params.get("SessionID")
        self.RoomID = params.get("RoomID")
        self.Caller = params.get("Caller")
        self.Callee = params.get("Callee")
        self.StartTimestamp = params.get("StartTimestamp")
        self.RingTimestamp = params.get("RingTimestamp")
        self.AcceptTimestamp = params.get("AcceptTimestamp")
        self.StaffEmail = params.get("StaffEmail")
        self.StaffNumber = params.get("StaffNumber")
        self.SessionStatus = params.get("SessionStatus")
        self.Direction = params.get("Direction")
        self.OutBoundCaller = params.get("OutBoundCaller")
        self.OutBoundCallee = params.get("OutBoundCallee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PSTNSessionInfo(AbstractModel):
    """PSTN 会话信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeatUserInfo(AbstractModel):
    """坐席用户信息

    """

    def __init__(self):
        r"""
        :param Name: 坐席名称
        :type Name: str
        :param Mail: 坐席邮箱
        :type Mail: str
        :param Phone: 坐席电话号码（带0086前缀）
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServeParticipant(AbstractModel):
    """参与者信息

    """

    def __init__(self):
        r"""
        :param Mail: 坐席邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Mail: str
        :param Phone: 坐席电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param RingTimestamp: 振铃时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type RingTimestamp: int
        :param AcceptTimestamp: 接听时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type AcceptTimestamp: int
        :param EndedTimestamp: 结束时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type EndedTimestamp: int
        :param RecordId: 录音 ID，能够索引到坐席侧的录音
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param Type: 参与者类型，"staffSeat", "outboundSeat", "staffPhoneSeat"
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param TransferFrom: 转接来源坐席信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferFrom: str
        :param TransferTo: 转接去向坐席信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferTo: str
        :param TransferToType: 转接去向参与者类型，取值与 Type 一致
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferToType: str
        :param SkillGroupId: 技能组 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupId: int
        :param EndStatusString: 结束状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EndStatusString: str
        :param RecordURL: 录音 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordURL: str
        :param Sequence: 参与者序号，从 0 开始
注意：此字段可能返回 null，表示取不到有效值。
        :type Sequence: int
        :param StartTimestamp: 开始时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimestamp: int
        :param SkillGroupName: 技能组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupName: str
        """
        self.Mail = None
        self.Phone = None
        self.RingTimestamp = None
        self.AcceptTimestamp = None
        self.EndedTimestamp = None
        self.RecordId = None
        self.Type = None
        self.TransferFrom = None
        self.TransferTo = None
        self.TransferToType = None
        self.SkillGroupId = None
        self.EndStatusString = None
        self.RecordURL = None
        self.Sequence = None
        self.StartTimestamp = None
        self.SkillGroupName = None


    def _deserialize(self, params):
        self.Mail = params.get("Mail")
        self.Phone = params.get("Phone")
        self.RingTimestamp = params.get("RingTimestamp")
        self.AcceptTimestamp = params.get("AcceptTimestamp")
        self.EndedTimestamp = params.get("EndedTimestamp")
        self.RecordId = params.get("RecordId")
        self.Type = params.get("Type")
        self.TransferFrom = params.get("TransferFrom")
        self.TransferTo = params.get("TransferTo")
        self.TransferToType = params.get("TransferToType")
        self.SkillGroupId = params.get("SkillGroupId")
        self.EndStatusString = params.get("EndStatusString")
        self.RecordURL = params.get("RecordURL")
        self.Sequence = params.get("Sequence")
        self.StartTimestamp = params.get("StartTimestamp")
        self.SkillGroupName = params.get("SkillGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupInfoItem(AbstractModel):
    """技能组信息

    """

    def __init__(self):
        r"""
        :param SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param Type: 类型：IM、TEL、ALL（全媒体）
        :type Type: str
        :param RoutePolicy: 会话分配策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RoutePolicy: str
        :param UsingLastSeat: 会话分配是否优先上次服务坐席
注意：此字段可能返回 null，表示取不到有效值。
        :type UsingLastSeat: int
        :param MaxConcurrency: 单客服最大并发数（电话类型默认1）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConcurrency: int
        :param LastModifyTimestamp: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTimestamp: int
        """
        self.SkillGroupId = None
        self.SkillGroupName = None
        self.Type = None
        self.RoutePolicy = None
        self.UsingLastSeat = None
        self.MaxConcurrency = None
        self.LastModifyTimestamp = None


    def _deserialize(self, params):
        self.SkillGroupId = params.get("SkillGroupId")
        self.SkillGroupName = params.get("SkillGroupName")
        self.Type = params.get("Type")
        self.RoutePolicy = params.get("RoutePolicy")
        self.UsingLastSeat = params.get("UsingLastSeat")
        self.MaxConcurrency = params.get("MaxConcurrency")
        self.LastModifyTimestamp = params.get("LastModifyTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillGroupItem(AbstractModel):
    """技能组信息

    """

    def __init__(self):
        r"""
        :param SkillGroupId: 技能组ID
        :type SkillGroupId: int
        :param SkillGroupName: 技能组名称
        :type SkillGroupName: str
        :param Priority: 优先级
        :type Priority: int
        :param Type: 类型：IM、TEL、ALL（全媒体）
        :type Type: str
        """
        self.SkillGroupId = None
        self.SkillGroupName = None
        self.Priority = None
        self.Type = None


    def _deserialize(self, params):
        self.SkillGroupId = params.get("SkillGroupId")
        self.SkillGroupName = params.get("SkillGroupName")
        self.Priority = params.get("Priority")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffInfo(AbstractModel):
    """带有技能组优先级的坐席信息

    """

    def __init__(self):
        r"""
        :param Name: 坐席名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Mail: 坐席邮箱
        :type Mail: str
        :param Phone: 坐席电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param Nick: 坐席昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param StaffNumber: 坐席工号
注意：此字段可能返回 null，表示取不到有效值。
        :type StaffNumber: str
        :param SkillGroupList: 所属技能组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupList: list of SkillGroupItem
        :param LastModifyTimestamp: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTimestamp: int
        """
        self.Name = None
        self.Mail = None
        self.Phone = None
        self.Nick = None
        self.StaffNumber = None
        self.SkillGroupList = None
        self.LastModifyTimestamp = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Mail = params.get("Mail")
        self.Phone = params.get("Phone")
        self.Nick = params.get("Nick")
        self.StaffNumber = params.get("StaffNumber")
        if params.get("SkillGroupList") is not None:
            self.SkillGroupList = []
            for item in params.get("SkillGroupList"):
                obj = SkillGroupItem()
                obj._deserialize(item)
                self.SkillGroupList.append(obj)
        self.LastModifyTimestamp = params.get("LastModifyTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusExtra(AbstractModel):
    """坐席状态补充信息

    """

    def __init__(self):
        r"""
        :param Type: im - 文本 | tel - 电话 | all - 全媒体
        :type Type: str
        :param Direct: in - 呼入 | out - 呼出
        :type Direct: str
        """
        self.Type = None
        self.Direct = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Direct = params.get("Direct")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffStatusMetrics(AbstractModel):
    """坐席状态相关信息

    """

    def __init__(self):
        r"""
        :param Email: 坐席邮箱
        :type Email: str
        :param Status: 坐席状态 free 示闲 | busy 忙碌 | rest 小休 | notReady 示忙 | afterCallWork 话后调整 | offline 离线
        :type Status: str
        :param StatusExtra: 坐席状态补充信息
        :type StatusExtra: :class:`tencentcloud.ccc.v20200210.models.StaffStatusExtra`
        :param OnlineDuration: 当天在线总时长
        :type OnlineDuration: int
        :param FreeDuration: 当天示闲总时长
        :type FreeDuration: int
        :param BusyDuration: 当天忙碌总时长
        :type BusyDuration: int
        :param NotReadyDuration: 当天示忙总时长
        :type NotReadyDuration: int
        :param RestDuration: 当天小休总时长
        :type RestDuration: int
        :param AfterCallWorkDuration: 当天话后调整总时长
        :type AfterCallWorkDuration: int
        :param Reason: 小休原因
        :type Reason: str
        :param ReserveRest: 是否预约小休
        :type ReserveRest: bool
        :param ReserveNotReady: 是否预约示忙
        :type ReserveNotReady: bool
        """
        self.Email = None
        self.Status = None
        self.StatusExtra = None
        self.OnlineDuration = None
        self.FreeDuration = None
        self.BusyDuration = None
        self.NotReadyDuration = None
        self.RestDuration = None
        self.AfterCallWorkDuration = None
        self.Reason = None
        self.ReserveRest = None
        self.ReserveNotReady = None


    def _deserialize(self, params):
        self.Email = params.get("Email")
        self.Status = params.get("Status")
        if params.get("StatusExtra") is not None:
            self.StatusExtra = StaffStatusExtra()
            self.StatusExtra._deserialize(params.get("StatusExtra"))
        self.OnlineDuration = params.get("OnlineDuration")
        self.FreeDuration = params.get("FreeDuration")
        self.BusyDuration = params.get("BusyDuration")
        self.NotReadyDuration = params.get("NotReadyDuration")
        self.RestDuration = params.get("RestDuration")
        self.AfterCallWorkDuration = params.get("AfterCallWorkDuration")
        self.Reason = params.get("Reason")
        self.ReserveRest = params.get("ReserveRest")
        self.ReserveNotReady = params.get("ReserveNotReady")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TelCdrInfo(AbstractModel):
    """电话话单信息

    """

    def __init__(self):
        r"""
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
        :param EndStatus: 结束状态
0	错误
1	正常结束
2	未接通
17	坐席未接
100	黑名单
101	坐席转接
102	IVR 期间用户放弃
103	会话排队期间用户放弃
104	会话振铃期间用户放弃
105	无坐席在线
106	非工作时间
107	IVR后直接结束
201	未知状态
202	未接听
203	拒接挂断
204	关机
205	空号
206	通话中
207	欠费
208	运营商线路异常
209	主叫取消
210	不在服务区
        :type EndStatus: int
        :param SkillGroup: 技能组名称
        :type SkillGroup: str
        :param CallerLocation: 主叫归属地
        :type CallerLocation: str
        :param IVRDuration: IVR 阶段耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type IVRDuration: int
        :param RingTimestamp: 振铃时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type RingTimestamp: int
        :param AcceptTimestamp: 接听时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type AcceptTimestamp: int
        :param EndedTimestamp: 结束时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type EndedTimestamp: int
        :param IVRKeyPressed: IVR 按键信息 ，e.g. ["1","2","3"]
注意：此字段可能返回 null，表示取不到有效值。
        :type IVRKeyPressed: list of str
        :param HungUpSide: 挂机方 seat 坐席 user 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type HungUpSide: str
        :param ServeParticipants: 服务参与者列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServeParticipants: list of ServeParticipant
        :param SkillGroupId: 技能组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupId: int
        :param EndStatusString: error                   错误
ok                       正常结束
unconnected      未接通
seatGiveUp         坐席未接
blackList             黑名单
seatForward       坐席转接
ivrGiveUp           IVR 期间用户放弃
waitingGiveUp   会话排队期间用户放弃
ringingGiveUp   会话振铃期间用户放弃
noSeatOnline     无坐席在线
notWorkTime     非工作时间
ivrEnd                 IVR后直接结束
unknown            未知状态
notAnswer          未接听
userReject          拒接挂断
powerOff            关机
numberNotExist  空号
busy                    通话中
outOfCredit        欠费
operatorError     运营商线路异常
callerCancel        主叫取消
notInService       不在服务区
注意：此字段可能返回 null，表示取不到有效值。
        :type EndStatusString: str
        :param StartTimestamp: 会话开始时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimestamp: int
        :param QueuedTimestamp: 进入排队时间，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type QueuedTimestamp: int
        :param PostIVRKeyPressed: 后置IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
注意：此字段可能返回 null，表示取不到有效值。
        :type PostIVRKeyPressed: list of IVRKeyPressedElement
        :param QueuedSkillGroupId: 排队技能组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type QueuedSkillGroupId: int
        :param SessionId: 会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
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
        self.IVRDuration = None
        self.RingTimestamp = None
        self.AcceptTimestamp = None
        self.EndedTimestamp = None
        self.IVRKeyPressed = None
        self.HungUpSide = None
        self.ServeParticipants = None
        self.SkillGroupId = None
        self.EndStatusString = None
        self.StartTimestamp = None
        self.QueuedTimestamp = None
        self.PostIVRKeyPressed = None
        self.QueuedSkillGroupId = None
        self.SessionId = None


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
        self.IVRDuration = params.get("IVRDuration")
        self.RingTimestamp = params.get("RingTimestamp")
        self.AcceptTimestamp = params.get("AcceptTimestamp")
        self.EndedTimestamp = params.get("EndedTimestamp")
        self.IVRKeyPressed = params.get("IVRKeyPressed")
        self.HungUpSide = params.get("HungUpSide")
        if params.get("ServeParticipants") is not None:
            self.ServeParticipants = []
            for item in params.get("ServeParticipants"):
                obj = ServeParticipant()
                obj._deserialize(item)
                self.ServeParticipants.append(obj)
        self.SkillGroupId = params.get("SkillGroupId")
        self.EndStatusString = params.get("EndStatusString")
        self.StartTimestamp = params.get("StartTimestamp")
        self.QueuedTimestamp = params.get("QueuedTimestamp")
        if params.get("PostIVRKeyPressed") is not None:
            self.PostIVRKeyPressed = []
            for item in params.get("PostIVRKeyPressed"):
                obj = IVRKeyPressedElement()
                obj._deserialize(item)
                self.PostIVRKeyPressed.append(obj)
        self.QueuedSkillGroupId = params.get("QueuedSkillGroupId")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindStaffSkillGroupListRequest(AbstractModel):
    """UnbindStaffSkillGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 实例ID
        :type SdkAppId: int
        :param StaffEmail: 客服邮箱
        :type StaffEmail: str
        :param SkillGroupList: 解绑技能组列表
        :type SkillGroupList: list of int
        """
        self.SdkAppId = None
        self.StaffEmail = None
        self.SkillGroupList = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StaffEmail = params.get("StaffEmail")
        self.SkillGroupList = params.get("SkillGroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindStaffSkillGroupListResponse(AbstractModel):
    """UnbindStaffSkillGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")