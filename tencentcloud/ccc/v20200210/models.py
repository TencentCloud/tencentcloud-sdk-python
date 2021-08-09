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
        """
        :param SdkAppId: 实例ID\n        :type SdkAppId: int\n        :param StaffEmail: 坐席邮箱\n        :type StaffEmail: str\n        :param SkillGroupList: 绑定技能组列表\n        :type SkillGroupList: list of int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSDKLoginTokenRequest(AbstractModel):
    """CreateSDKLoginToken请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 应用ID。\n        :type SdkAppId: int\n        :param SeatUserId: 坐席账号。\n        :type SeatUserId: str\n        """
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
        """
        :param Token: SDK 登录 Token。\n        :type Token: str\n        :param ExpiredTime: 过期时间戳，Unix 时间戳。\n        :type ExpiredTime: int\n        :param SdkURL: SDK 加载路径会随着 SDK 的发布而变动。\n        :type SdkURL: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SdkAppId: 应用ID\n        :type SdkAppId: int\n        :param Staffs: 客服信息，个数不超过 10\n        :type Staffs: list of SeatUserInfo\n        """
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
        """
        :param ErrorStaffList: 错误坐席列表及错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorStaffList: list of ErrStaffItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param SdkAppId: 应用 ID\n        :type SdkAppId: int\n        :param Uid: 用户 ID\n        :type Uid: str\n        :param ExpiredTime: 有效期，单位秒，不超过 1 小时\n        :type ExpiredTime: int\n        :param ClientData: 用户签名数据\n        :type ClientData: str\n        """
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
        """
        :param UserSig: 签名结果\n        :type UserSig: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.UserSig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserSig = params.get("UserSig")
        self.RequestId = params.get("RequestId")


class DeleteStaffRequest(AbstractModel):
    """DeleteStaff请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 实例ID\n        :type SdkAppId: int\n        :param StaffList: 待删除客服邮箱列表\n        :type StaffList: list of str\n        """
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
        """
        :param OnlineStaffList: 无法删除的状态为在线的客服列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type OnlineStaffList: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OnlineStaffList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineStaffList = params.get("OnlineStaffList")
        self.RequestId = params.get("RequestId")


class DescribeChatMessagesRequest(AbstractModel):
    """DescribeChatMessages请求参数结构体

    """

    def __init__(self):
        """
        :param CdrId: 服务记录ID\n        :type CdrId: str\n        :param InstanceId: 实例ID\n        :type InstanceId: int\n        :param SdkAppId: 应用ID\n        :type SdkAppId: int\n        :param Limit: 返回记录条数 最大为100默认20\n        :type Limit: int\n        :param Offset: 返回记录偏移 默认为0\n        :type Offset: int\n        :param Order: 1为从早到晚，2为从晚到早，默认为2\n        :type Order: int\n        """
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
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param Messages: 消息列表\n        :type Messages: list of MessageBody\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param StartTimestamp: 起始时间\n        :type StartTimestamp: int\n        :param EndTimestamp: 结束时间\n        :type EndTimestamp: int\n        :param InstanceId: 实例ID\n        :type InstanceId: int\n        :param SdkAppId: 应用ID\n        :type SdkAppId: int\n        :param Limit: 返回记录条数 最大为100默认20\n        :type Limit: int\n        :param Offset: 返回记录偏移 默认为0\n        :type Offset: int\n        :param Type: 1为全媒体，2为文本客服，不填则查询全部\n        :type Type: int\n        """
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
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param IMCdrs: 服务记录列表\n        :type IMCdrs: list of IMCdrInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SdkAppId: 应用 ID\n        :type SdkAppId: int\n        :param Offset: 数据偏移\n        :type Offset: int\n        :param Limit: 返回的数据条数，最大 25\n        :type Limit: int\n        """
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
        """
        :param Total: 列表总条数\n        :type Total: int\n        :param Sessions: 列表内容\n        :type Sessions: list of PSTNSessionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param InstanceId: 实例ID\n        :type InstanceId: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        """
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
        """
        :param TotalCount: 此实例的坐席用户总数\n        :type TotalCount: int\n        :param SeatUsers: 坐席用户信息列表\n        :type SeatUsers: list of SeatUserInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param SdkAppId: 应用ID\n        :type SdkAppId: int\n        :param PageSize: 分页尺寸，上限 100\n        :type PageSize: int\n        :param PageNumber: 分页页码，从 0 开始\n        :type PageNumber: int\n        :param SkillGroupId: 技能组ID，查询单个技能组时使用\n        :type SkillGroupId: int\n        :param ModifiedTime: 查询修改时间大于等于ModifiedTime的技能组时使用\n        :type ModifiedTime: int\n        """
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
        """
        :param TotalCount: 技能组总数\n        :type TotalCount: int\n        :param SkillGroupList: 技能组信息列表\n        :type SkillGroupList: list of SkillGroupInfoItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param SdkAppId: 应用ID\n        :type SdkAppId: int\n        :param PageSize: 分页尺寸，上限 100\n        :type PageSize: int\n        :param PageNumber: 分页页码，从 0 开始\n        :type PageNumber: int\n        :param StaffMail: 坐席账号，查询单个坐席时使用\n        :type StaffMail: str\n        :param ModifiedTime: 查询修改时间大于等于ModifiedTime的坐席时使用\n        :type ModifiedTime: int\n        """
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
        """
        :param TotalCount: 坐席用户总数\n        :type TotalCount: int\n        :param StaffList: 坐席用户信息列表\n        :type StaffList: list of StaffInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeTelCallInfoRequest(AbstractModel):
    """DescribeTelCallInfo请求参数结构体

    """

    def __init__(self):
        """
        :param StartTimeStamp: 起始时间戳，Unix 时间戳\n        :type StartTimeStamp: int\n        :param EndTimeStamp: 结束时间戳，Unix 时间戳，查询时间范围最大为90天\n        :type EndTimeStamp: int\n        :param SdkAppIdList: 应用ID列表，多个ID时，返回值为多个ID使用总和\n        :type SdkAppIdList: list of int\n        """
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
        """
        :param TelCallOutCount: 电话呼出统计分钟数\n        :type TelCallOutCount: int\n        :param TelCallInCount: 电话呼入统计分钟数\n        :type TelCallInCount: int\n        :param SeatUsedCount: 坐席使用统计个数\n        :type SeatUsedCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param StartTimeStamp: 起始时间戳，Unix 时间戳\n        :type StartTimeStamp: int\n        :param EndTimeStamp: 结束时间戳，Unix 时间戳\n        :type EndTimeStamp: int\n        :param Limit: 返回数据条数，上限（deprecated）\n        :type Limit: int\n        :param Offset: 偏移（deprecated）\n        :type Offset: int\n        :param InstanceId: 实例 ID（deprecated）\n        :type InstanceId: int\n        :param SdkAppId: 应用 ID\n        :type SdkAppId: int\n        :param PageSize: 分页尺寸，上限 100\n        :type PageSize: int\n        :param PageNumber: 分页页码，从 0 开始\n        :type PageNumber: int\n        :param Phones: 按手机号筛选\n        :type Phones: list of str\n        """
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
        """
        :param TotalCount: 话单记录总数\n        :type TotalCount: int\n        :param TelCdrs: 话单记录\n        :type TelCdrs: list of TelCdrInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param SdkAppId: 应用ID\n        :type SdkAppId: int\n        :param SessionId: 会话ID\n        :type SessionId: str\n        """
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
        """
        :param Session: 会话信息\n        :type Session: :class:`tencentcloud.ccc.v20200210.models.PSTNSession`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param StaffEmail: 坐席邮箱地址\n        :type StaffEmail: str\n        :param Code: 错误码\n        :type Code: str\n        :param Message: 错误描述\n        :type Message: str\n        """
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
        """
        :param Id: 服务记录ID\n        :type Id: str\n        :param Duration: 服务时长秒数\n        :type Duration: int\n        :param EndStatus: 结束状态\n        :type EndStatus: int\n        :param Nickname: 用户昵称\n        :type Nickname: str\n        :param Type: 服务类型 1为全媒体，2为文本客服\n        :type Type: int\n        :param StaffId: 客服ID\n        :type StaffId: str\n        :param Timestamp: 服务时间戳\n        :type Timestamp: int\n        """
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
        """
        :param Key: 按键
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Label: 按键关联的标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Label: str\n        """
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
        """
        :param Type: 消息类型\n        :type Type: str\n        :param Content: 消息内容\n        :type Content: str\n        """
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
        """
        :param Timestamp: 消息时间戳\n        :type Timestamp: int\n        :param From: 发消息的用户ID\n        :type From: str\n        :param Messages: 消息列表\n        :type Messages: list of Message\n        """
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
        """
        :param SessionID: 会话 ID\n        :type SessionID: str\n        :param RoomID: 会话临时房间 ID\n        :type RoomID: str\n        :param Caller: 主叫\n        :type Caller: str\n        :param Callee: 被叫\n        :type Callee: str\n        :param StartTimestamp: 开始时间，Unix 时间戳\n        :type StartTimestamp: int\n        :param RingTimestamp: 振铃时间，Unix 时间戳\n        :type RingTimestamp: int\n        :param AcceptTimestamp: 接听时间，Unix 时间戳\n        :type AcceptTimestamp: int\n        :param StaffEmail: 坐席邮箱\n        :type StaffEmail: str\n        :param StaffNumber: 坐席工号\n        :type StaffNumber: str\n        :param SessionStatus: 会话状态
ringing 振铃中
seatJoining  等待坐席接听
inProgress 进行中
finished 已完成\n        :type SessionStatus: str\n        :param Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出\n        :type Direction: int\n        :param OutBoundCaller: 转外线使用的号码（转外线主叫）\n        :type OutBoundCaller: str\n        :param OutBoundCallee: 转外线被叫\n        :type OutBoundCallee: str\n        """
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
        """
        :param SessionID: 会话 ID\n        :type SessionID: str\n        :param RoomID: 会话临时房间 ID\n        :type RoomID: str\n        :param Caller: 主叫\n        :type Caller: str\n        :param Callee: 被叫\n        :type Callee: str\n        :param StartTimestamp: 开始时间，Unix 时间戳\n        :type StartTimestamp: str\n        :param AcceptTimestamp: 接听时间，Unix 时间戳\n        :type AcceptTimestamp: str\n        :param StaffEmail: 坐席邮箱\n        :type StaffEmail: str\n        :param StaffNumber: 坐席工号\n        :type StaffNumber: str\n        :param SessionStatus: 坐席状态 inProgress 进行中\n        :type SessionStatus: str\n        :param Direction: 会话呼叫方向， 0 呼入 | 1 - 呼出\n        :type Direction: int\n        :param RingTimestamp: 振铃时间，Unix 时间戳\n        :type RingTimestamp: int\n        """
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
        """
        :param Name: 坐席名称\n        :type Name: str\n        :param Mail: 坐席邮箱\n        :type Mail: str\n        :param Phone: 坐席电话号码（带0086前缀）\n        :type Phone: str\n        :param Nick: 坐席昵称\n        :type Nick: str\n        :param UserId: 用户ID\n        :type UserId: str\n        :param SkillGroupNameList: 坐席关联的技能组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkillGroupNameList: list of str\n        :param StaffNumber: 工号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StaffNumber: str\n        """
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
        """
        :param Mail: 坐席邮箱
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mail: str\n        :param Phone: 坐席电话
注意：此字段可能返回 null，表示取不到有效值。\n        :type Phone: str\n        :param RingTimestamp: 振铃时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type RingTimestamp: int\n        :param AcceptTimestamp: 接听时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type AcceptTimestamp: int\n        :param EndedTimestamp: 结束时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndedTimestamp: int\n        :param RecordId: 录音 ID，能够索引到坐席侧的录音
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordId: str\n        :param Type: 参与者类型，"staffSeat", "outboundSeat", "staffPhoneSeat"
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param TransferFrom: 转接来源坐席信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferFrom: str\n        :param TransferTo: 转接去向坐席信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferTo: str\n        :param TransferToType: 转接去向参与者类型，取值与 Type 一致
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferToType: str\n        :param SkillGroupId: 技能组 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkillGroupId: int\n        :param EndStatusString: 结束状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndStatusString: str\n        :param RecordURL: 录音 URL
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordURL: str\n        :param Sequence: 参与者序号，从 0 开始
注意：此字段可能返回 null，表示取不到有效值。\n        :type Sequence: int\n        :param StartTimestamp: 开始时间戳，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTimestamp: int\n        :param SkillGroupName: 技能组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkillGroupName: str\n        """
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
        """
        :param SkillGroupId: 技能组ID\n        :type SkillGroupId: int\n        :param SkillGroupName: 技能组名称\n        :type SkillGroupName: str\n        :param Type: 类型：IM、TEL、ALL（全媒体）\n        :type Type: str\n        :param RoutePolicy: 会话分配策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type RoutePolicy: str\n        :param UsingLastSeat: 会话分配是否优先上次服务坐席
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsingLastSeat: int\n        :param MaxConcurrency: 单客服最大并发数（电话类型默认1）
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxConcurrency: int\n        :param LastModifyTimestamp: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTimestamp: int\n        """
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
        """
        :param SkillGroupId: 技能组ID\n        :type SkillGroupId: int\n        :param SkillGroupName: 技能组名称\n        :type SkillGroupName: str\n        :param Priority: 优先级\n        :type Priority: int\n        :param Type: 类型：IM、TEL、ALL（全媒体）\n        :type Type: str\n        """
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
        """
        :param Name: 坐席名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Mail: 坐席邮箱\n        :type Mail: str\n        :param Phone: 坐席电话号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type Phone: str\n        :param Nick: 坐席昵称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Nick: str\n        :param StaffNumber: 坐席工号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StaffNumber: str\n        :param SkillGroupList: 所属技能组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkillGroupList: list of SkillGroupItem\n        :param LastModifyTimestamp: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTimestamp: int\n        """
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
        


class TelCdrInfo(AbstractModel):
    """电话话单信息

    """

    def __init__(self):
        """
        :param Caller: 主叫号码\n        :type Caller: str\n        :param Callee: 被叫号码\n        :type Callee: str\n        :param Time: 呼叫发起时间戳，Unix 时间戳\n        :type Time: int\n        :param Direction: 呼入呼出方向 0 呼入 1 呼出\n        :type Direction: int\n        :param Duration: 通话时长\n        :type Duration: int\n        :param RecordURL: 录音信息\n        :type RecordURL: str\n        :param SeatUser: 坐席信息\n        :type SeatUser: :class:`tencentcloud.ccc.v20200210.models.SeatUserInfo`\n        :param EndStatus: 结束状态
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
210	不在服务区\n        :type EndStatus: int\n        :param SkillGroup: 技能组名称\n        :type SkillGroup: str\n        :param CallerLocation: 主叫归属地\n        :type CallerLocation: str\n        :param IVRDuration: IVR 阶段耗时
注意：此字段可能返回 null，表示取不到有效值。\n        :type IVRDuration: int\n        :param RingTimestamp: 振铃时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type RingTimestamp: int\n        :param AcceptTimestamp: 接听时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type AcceptTimestamp: int\n        :param EndedTimestamp: 结束时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndedTimestamp: int\n        :param IVRKeyPressed: IVR 按键信息 ，e.g. ["1","2","3"]
注意：此字段可能返回 null，表示取不到有效值。\n        :type IVRKeyPressed: list of str\n        :param HungUpSide: 挂机方 seat 坐席 user 用户
注意：此字段可能返回 null，表示取不到有效值。\n        :type HungUpSide: str\n        :param ServeParticipants: 服务参与者列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServeParticipants: list of ServeParticipant\n        :param SkillGroupId: 技能组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkillGroupId: int\n        :param EndStatusString: error                   错误
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndStatusString: str\n        :param StartTimestamp: 会话开始时间戳，UNIX 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTimestamp: int\n        :param QueuedTimestamp: 进入排队时间，Unix 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueuedTimestamp: int\n        :param PostIVRKeyPressed: 后置IVR按键信息（e.g. [{"Key":"1","Label":"非常满意"}]）
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostIVRKeyPressed: list of IVRKeyPressedElement\n        :param QueuedSkillGroupId: 排队技能组Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueuedSkillGroupId: int\n        :param SessionId: 会话 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SessionId: str\n        """
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
        """
        :param SdkAppId: 实例ID\n        :type SdkAppId: int\n        :param StaffEmail: 客服邮箱\n        :type StaffEmail: str\n        :param SkillGroupList: 解绑技能组列表\n        :type SkillGroupList: list of int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")