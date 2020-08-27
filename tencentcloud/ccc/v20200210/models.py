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


class DescribeTelCdrRequest(AbstractModel):
    """DescribeTelCdr请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID
        :type InstanceId: int
        :param StartTimeStamp: 起始时间戳，Unix 时间戳
        :type StartTimeStamp: int
        :param EndTimeStamp: 结束时间戳，Unix 时间戳
        :type EndTimeStamp: int
        :param Limit: 返回记录条数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTimeStamp = None
        self.EndTimeStamp = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


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


class SeatUserInfo(AbstractModel):
    """坐席用户信息

    """

    def __init__(self):
        """
        :param Phone: 坐席电话号码
        :type Phone: str
        :param Name: 坐席名称
        :type Name: str
        :param Mail: 坐席邮箱
        :type Mail: str
        :param Nick: 坐席昵称
        :type Nick: str
        :param UserId: 用户ID
        :type UserId: str
        :param SkillGroupNameList: 坐席关联的技能组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillGroupNameList: list of str
        """
        self.Phone = None
        self.Name = None
        self.Mail = None
        self.Nick = None
        self.UserId = None
        self.SkillGroupNameList = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Name = params.get("Name")
        self.Mail = params.get("Mail")
        self.Nick = params.get("Nick")
        self.UserId = params.get("UserId")
        self.SkillGroupNameList = params.get("SkillGroupNameList")


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