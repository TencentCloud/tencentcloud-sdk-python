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


class ActivityInfo(AbstractModel):
    """活动详情

    """

    def __init__(self):
        r"""
        :param _TemplateId: 活动使用模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _ActivityTitle: 活动标题
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityTitle: str
        :param _ActivityDesc: 活动描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityDesc: str
        :param _ActivityCover: 活动封面地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityCover: str
        :param _ActivityType: 活动类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityType: str
        :param _ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityId: str
        :param _PersonalConfig: 活动模板自定义配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalConfig: str
        """
        self._TemplateId = None
        self._ActivityTitle = None
        self._ActivityDesc = None
        self._ActivityCover = None
        self._ActivityType = None
        self._ActivityId = None
        self._PersonalConfig = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ActivityTitle(self):
        return self._ActivityTitle

    @ActivityTitle.setter
    def ActivityTitle(self, ActivityTitle):
        self._ActivityTitle = ActivityTitle

    @property
    def ActivityDesc(self):
        return self._ActivityDesc

    @ActivityDesc.setter
    def ActivityDesc(self, ActivityDesc):
        self._ActivityDesc = ActivityDesc

    @property
    def ActivityCover(self):
        return self._ActivityCover

    @ActivityCover.setter
    def ActivityCover(self, ActivityCover):
        self._ActivityCover = ActivityCover

    @property
    def ActivityType(self):
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def PersonalConfig(self):
        return self._PersonalConfig

    @PersonalConfig.setter
    def PersonalConfig(self, PersonalConfig):
        self._PersonalConfig = PersonalConfig


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._ActivityTitle = params.get("ActivityTitle")
        self._ActivityDesc = params.get("ActivityDesc")
        self._ActivityCover = params.get("ActivityCover")
        self._ActivityType = params.get("ActivityType")
        self._ActivityId = params.get("ActivityId")
        self._PersonalConfig = params.get("PersonalConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStaffChUserRequest(AbstractModel):
    """CheckStaffChUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 员工ID
        :type UserId: list of str
        :param _OperateType: 渠道状态：checkpass审核通过, checkreject审核拒绝, enableoperate启用, stopoperate停用
        :type OperateType: str
        """
        self._UserId = None
        self._OperateType = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def OperateType(self):
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._OperateType = params.get("OperateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStaffChUserResponse(AbstractModel):
    """CheckStaffChUser返回参数结构体

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


class CopyActivityChannelRequest(AbstractModel):
    """CopyActivityChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动ID
        :type ActivityId: str
        :param _ChannelFrom: 来源渠道ID
        :type ChannelFrom: str
        :param _ChannelTo: 目的渠道id
        :type ChannelTo: list of str
        """
        self._ActivityId = None
        self._ChannelFrom = None
        self._ChannelTo = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ChannelFrom(self):
        return self._ChannelFrom

    @ChannelFrom.setter
    def ChannelFrom(self, ChannelFrom):
        self._ChannelFrom = ChannelFrom

    @property
    def ChannelTo(self):
        return self._ChannelTo

    @ChannelTo.setter
    def ChannelTo(self, ChannelTo):
        self._ChannelTo = ChannelTo


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._ChannelFrom = params.get("ChannelFrom")
        self._ChannelTo = params.get("ChannelTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyActivityChannelResponse(AbstractModel):
    """CopyActivityChannel返回参数结构体

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


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectOrg: 项目机构
        :type ProjectOrg: str
        :param _ProjectBudget: 项目预算
        :type ProjectBudget: str
        :param _ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param _ProjectOrgId: 所属部门ID
        :type ProjectOrgId: str
        """
        self._ProjectName = None
        self._ProjectOrg = None
        self._ProjectBudget = None
        self._ProjectIntroduction = None
        self._ProjectOrgId = None

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectOrg(self):
        return self._ProjectOrg

    @ProjectOrg.setter
    def ProjectOrg(self, ProjectOrg):
        self._ProjectOrg = ProjectOrg

    @property
    def ProjectBudget(self):
        return self._ProjectBudget

    @ProjectBudget.setter
    def ProjectBudget(self, ProjectBudget):
        self._ProjectBudget = ProjectBudget

    @property
    def ProjectIntroduction(self):
        return self._ProjectIntroduction

    @ProjectIntroduction.setter
    def ProjectIntroduction(self, ProjectIntroduction):
        self._ProjectIntroduction = ProjectIntroduction

    @property
    def ProjectOrgId(self):
        return self._ProjectOrgId

    @ProjectOrgId.setter
    def ProjectOrgId(self, ProjectOrgId):
        self._ProjectOrgId = ProjectOrgId


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectOrg = params.get("ProjectOrg")
        self._ProjectBudget = params.get("ProjectBudget")
        self._ProjectIntroduction = params.get("ProjectIntroduction")
        self._ProjectOrgId = params.get("ProjectOrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RequestId = params.get("RequestId")


class CreateSubProjectRequest(AbstractModel):
    """CreateSubProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 所属项目id
        :type ProjectId: str
        :param _SubProjectName: 子项目名称
        :type SubProjectName: str
        """
        self._ProjectId = None
        self._SubProjectName = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubProjectName(self):
        return self._SubProjectName

    @SubProjectName.setter
    def SubProjectName(self, SubProjectName):
        self._SubProjectName = SubProjectName


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SubProjectName = params.get("SubProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubProjectResponse(AbstractModel):
    """CreateSubProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubProjectId: 子项目id
        :type SubProjectId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubProjectId = None
        self._RequestId = None

    @property
    def SubProjectId(self):
        return self._SubProjectId

    @SubProjectId.setter
    def SubProjectId(self, SubProjectId):
        self._SubProjectId = SubProjectId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubProjectId = params.get("SubProjectId")
        self._RequestId = params.get("RequestId")


class CustomerInfo(AbstractModel):
    """客户档案

    """

    def __init__(self):
        r"""
        :param _Activity: 总活跃度
注意：此字段可能返回 null，表示取不到有效值。
        :type Activity: int
        :param _AudienceUserId: 客户ID
        :type AudienceUserId: str
        :param _Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _City: 最近记录城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _LastActiveTime: 最活跃时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastActiveTime: str
        :param _MarkFlag: 是否星标客户
注意：此字段可能返回 null，表示取不到有效值。
        :type MarkFlag: str
        :param _MonthActive: 30天活跃度
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthActive: int
        :param _MonthRecommend: 30天推荐度
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthRecommend: int
        :param _Phone: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _Province: 最近记录省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _RealName: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type RealName: str
        :param _RelChannelFlag: 员工标识 0 未关联 1 已关联
注意：此字段可能返回 null，表示取不到有效值。
        :type RelChannelFlag: int
        :param _Sex: 性别 1男 2女
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: int
        :param _Spread: 传播力（好友数）
注意：此字段可能返回 null，表示取不到有效值。
        :type Spread: int
        :param _WeekActive: 7天活跃度
注意：此字段可能返回 null，表示取不到有效值。
        :type WeekActive: int
        :param _WeekRecommend: 7天推荐度
注意：此字段可能返回 null，表示取不到有效值。
        :type WeekRecommend: int
        :param _WxCity: 微信城市
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCity: str
        :param _WxCountry: 微信国家或地区
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCountry: str
        :param _WxNickname: 微信呢称
注意：此字段可能返回 null，表示取不到有效值。
        :type WxNickname: str
        :param _WxProvince: 微信省份
注意：此字段可能返回 null，表示取不到有效值。
        :type WxProvince: str
        """
        self._Activity = None
        self._AudienceUserId = None
        self._Avatar = None
        self._City = None
        self._LastActiveTime = None
        self._MarkFlag = None
        self._MonthActive = None
        self._MonthRecommend = None
        self._Phone = None
        self._Province = None
        self._RealName = None
        self._RelChannelFlag = None
        self._Sex = None
        self._Spread = None
        self._WeekActive = None
        self._WeekRecommend = None
        self._WxCity = None
        self._WxCountry = None
        self._WxNickname = None
        self._WxProvince = None

    @property
    def Activity(self):
        return self._Activity

    @Activity.setter
    def Activity(self, Activity):
        self._Activity = Activity

    @property
    def AudienceUserId(self):
        return self._AudienceUserId

    @AudienceUserId.setter
    def AudienceUserId(self, AudienceUserId):
        self._AudienceUserId = AudienceUserId

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def LastActiveTime(self):
        return self._LastActiveTime

    @LastActiveTime.setter
    def LastActiveTime(self, LastActiveTime):
        self._LastActiveTime = LastActiveTime

    @property
    def MarkFlag(self):
        return self._MarkFlag

    @MarkFlag.setter
    def MarkFlag(self, MarkFlag):
        self._MarkFlag = MarkFlag

    @property
    def MonthActive(self):
        return self._MonthActive

    @MonthActive.setter
    def MonthActive(self, MonthActive):
        self._MonthActive = MonthActive

    @property
    def MonthRecommend(self):
        return self._MonthRecommend

    @MonthRecommend.setter
    def MonthRecommend(self, MonthRecommend):
        self._MonthRecommend = MonthRecommend

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def RealName(self):
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def RelChannelFlag(self):
        return self._RelChannelFlag

    @RelChannelFlag.setter
    def RelChannelFlag(self, RelChannelFlag):
        self._RelChannelFlag = RelChannelFlag

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Spread(self):
        return self._Spread

    @Spread.setter
    def Spread(self, Spread):
        self._Spread = Spread

    @property
    def WeekActive(self):
        return self._WeekActive

    @WeekActive.setter
    def WeekActive(self, WeekActive):
        self._WeekActive = WeekActive

    @property
    def WeekRecommend(self):
        return self._WeekRecommend

    @WeekRecommend.setter
    def WeekRecommend(self, WeekRecommend):
        self._WeekRecommend = WeekRecommend

    @property
    def WxCity(self):
        return self._WxCity

    @WxCity.setter
    def WxCity(self, WxCity):
        self._WxCity = WxCity

    @property
    def WxCountry(self):
        return self._WxCountry

    @WxCountry.setter
    def WxCountry(self, WxCountry):
        self._WxCountry = WxCountry

    @property
    def WxNickname(self):
        return self._WxNickname

    @WxNickname.setter
    def WxNickname(self, WxNickname):
        self._WxNickname = WxNickname

    @property
    def WxProvince(self):
        return self._WxProvince

    @WxProvince.setter
    def WxProvince(self, WxProvince):
        self._WxProvince = WxProvince


    def _deserialize(self, params):
        self._Activity = params.get("Activity")
        self._AudienceUserId = params.get("AudienceUserId")
        self._Avatar = params.get("Avatar")
        self._City = params.get("City")
        self._LastActiveTime = params.get("LastActiveTime")
        self._MarkFlag = params.get("MarkFlag")
        self._MonthActive = params.get("MonthActive")
        self._MonthRecommend = params.get("MonthRecommend")
        self._Phone = params.get("Phone")
        self._Province = params.get("Province")
        self._RealName = params.get("RealName")
        self._RelChannelFlag = params.get("RelChannelFlag")
        self._Sex = params.get("Sex")
        self._Spread = params.get("Spread")
        self._WeekActive = params.get("WeekActive")
        self._WeekRecommend = params.get("WeekRecommend")
        self._WxCity = params.get("WxCity")
        self._WxCountry = params.get("WxCountry")
        self._WxNickname = params.get("WxNickname")
        self._WxProvince = params.get("WxProvince")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

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


class DescribeCustomerRequest(AbstractModel):
    """DescribeCustomer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerResponse(AbstractModel):
    """DescribeCustomer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressList: 地址列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressList: list of str
        :param _UserId: 用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _Birthday: 生日
注意：此字段可能返回 null，表示取不到有效值。
        :type Birthday: str
        :param _City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Device: 设备
注意：此字段可能返回 null，表示取不到有效值。
        :type Device: str
        :param _Industrys: 行业
注意：此字段可能返回 null，表示取不到有效值。
        :type Industrys: list of str
        :param _LastActiveTime: 上次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastActiveTime: str
        :param _MarkFlag: 是否星标 1是 0否
注意：此字段可能返回 null，表示取不到有效值。
        :type MarkFlag: str
        :param _Model: 手机型号
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param _OpenId: 微信openid
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _PayFeature: 消费特点
注意：此字段可能返回 null，表示取不到有效值。
        :type PayFeature: str
        :param _Phone: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _PhoneList: 手机号码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneList: str
        :param _Province: 最近记录省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _RealName: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type RealName: str
        :param _RelChannelFlag: 员工标识 0：非员工 1：员工
注意：此字段可能返回 null，表示取不到有效值。
        :type RelChannelFlag: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Sex: 性别 1男 2女
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param _SourceAudienceVo: 最初来源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAudienceVo: str
        :param _SubWechats: 关注公众号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubWechats: list of str
        :param _UnionId: 微信unionid
注意：此字段可能返回 null，表示取不到有效值。
        :type UnionId: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _UserTypes: 用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserTypes: list of str
        :param _WxCity: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCity: str
        :param _WxCountry: 国家
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCountry: str
        :param _WxNickname: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type WxNickname: str
        :param _WxProvince: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type WxProvince: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddressList = None
        self._UserId = None
        self._Avatar = None
        self._Birthday = None
        self._City = None
        self._CreateTime = None
        self._Device = None
        self._Industrys = None
        self._LastActiveTime = None
        self._MarkFlag = None
        self._Model = None
        self._OpenId = None
        self._PayFeature = None
        self._Phone = None
        self._PhoneList = None
        self._Province = None
        self._RealName = None
        self._RelChannelFlag = None
        self._Remark = None
        self._Sex = None
        self._SourceAudienceVo = None
        self._SubWechats = None
        self._UnionId = None
        self._UpdateTime = None
        self._UserTypes = None
        self._WxCity = None
        self._WxCountry = None
        self._WxNickname = None
        self._WxProvince = None
        self._RequestId = None

    @property
    def AddressList(self):
        return self._AddressList

    @AddressList.setter
    def AddressList(self, AddressList):
        self._AddressList = AddressList

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Birthday(self):
        return self._Birthday

    @Birthday.setter
    def Birthday(self, Birthday):
        self._Birthday = Birthday

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Industrys(self):
        return self._Industrys

    @Industrys.setter
    def Industrys(self, Industrys):
        self._Industrys = Industrys

    @property
    def LastActiveTime(self):
        return self._LastActiveTime

    @LastActiveTime.setter
    def LastActiveTime(self, LastActiveTime):
        self._LastActiveTime = LastActiveTime

    @property
    def MarkFlag(self):
        return self._MarkFlag

    @MarkFlag.setter
    def MarkFlag(self, MarkFlag):
        self._MarkFlag = MarkFlag

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def PayFeature(self):
        return self._PayFeature

    @PayFeature.setter
    def PayFeature(self, PayFeature):
        self._PayFeature = PayFeature

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def PhoneList(self):
        return self._PhoneList

    @PhoneList.setter
    def PhoneList(self, PhoneList):
        self._PhoneList = PhoneList

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def RealName(self):
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def RelChannelFlag(self):
        return self._RelChannelFlag

    @RelChannelFlag.setter
    def RelChannelFlag(self, RelChannelFlag):
        self._RelChannelFlag = RelChannelFlag

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def SourceAudienceVo(self):
        return self._SourceAudienceVo

    @SourceAudienceVo.setter
    def SourceAudienceVo(self, SourceAudienceVo):
        self._SourceAudienceVo = SourceAudienceVo

    @property
    def SubWechats(self):
        return self._SubWechats

    @SubWechats.setter
    def SubWechats(self, SubWechats):
        self._SubWechats = SubWechats

    @property
    def UnionId(self):
        return self._UnionId

    @UnionId.setter
    def UnionId(self, UnionId):
        self._UnionId = UnionId

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def UserTypes(self):
        return self._UserTypes

    @UserTypes.setter
    def UserTypes(self, UserTypes):
        self._UserTypes = UserTypes

    @property
    def WxCity(self):
        return self._WxCity

    @WxCity.setter
    def WxCity(self, WxCity):
        self._WxCity = WxCity

    @property
    def WxCountry(self):
        return self._WxCountry

    @WxCountry.setter
    def WxCountry(self, WxCountry):
        self._WxCountry = WxCountry

    @property
    def WxNickname(self):
        return self._WxNickname

    @WxNickname.setter
    def WxNickname(self, WxNickname):
        self._WxNickname = WxNickname

    @property
    def WxProvince(self):
        return self._WxProvince

    @WxProvince.setter
    def WxProvince(self, WxProvince):
        self._WxProvince = WxProvince

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AddressList = params.get("AddressList")
        self._UserId = params.get("UserId")
        self._Avatar = params.get("Avatar")
        self._Birthday = params.get("Birthday")
        self._City = params.get("City")
        self._CreateTime = params.get("CreateTime")
        self._Device = params.get("Device")
        self._Industrys = params.get("Industrys")
        self._LastActiveTime = params.get("LastActiveTime")
        self._MarkFlag = params.get("MarkFlag")
        self._Model = params.get("Model")
        self._OpenId = params.get("OpenId")
        self._PayFeature = params.get("PayFeature")
        self._Phone = params.get("Phone")
        self._PhoneList = params.get("PhoneList")
        self._Province = params.get("Province")
        self._RealName = params.get("RealName")
        self._RelChannelFlag = params.get("RelChannelFlag")
        self._Remark = params.get("Remark")
        self._Sex = params.get("Sex")
        self._SourceAudienceVo = params.get("SourceAudienceVo")
        self._SubWechats = params.get("SubWechats")
        self._UnionId = params.get("UnionId")
        self._UpdateTime = params.get("UpdateTime")
        self._UserTypes = params.get("UserTypes")
        self._WxCity = params.get("WxCity")
        self._WxCountry = params.get("WxCountry")
        self._WxNickname = params.get("WxNickname")
        self._WxProvince = params.get("WxProvince")
        self._RequestId = params.get("RequestId")


class DescribeCustomersRequest(AbstractModel):
    """DescribeCustomers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueryType: 查询类型，0.个人，1负责部门，2.指定部门
        :type QueryType: str
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _MarkFlag: 是否星级标记 1是 0否
        :type MarkFlag: int
        :param _TagIds: 客户标签，多个标签用逗号隔开
        :type TagIds: str
        :param _RelChannelFlag: 员工标识筛选，0：非员工，1：员工
        :type RelChannelFlag: str
        :param _NeedPhoneFlag: 必须存在手机 1是 0否
        :type NeedPhoneFlag: int
        :param _Province: 省份
        :type Province: str
        :param _City: 城市
        :type City: str
        :param _Sex: 性别 1男 2女
        :type Sex: str
        :param _KeyWord: 城市
        :type KeyWord: str
        :param _Offset: 查询开始位置
        :type Offset: int
        :param _Limit: 每页记录条数
        :type Limit: int
        :param _SubProjectId: 子项目ID
        :type SubProjectId: str
        """
        self._QueryType = None
        self._GroupId = None
        self._MarkFlag = None
        self._TagIds = None
        self._RelChannelFlag = None
        self._NeedPhoneFlag = None
        self._Province = None
        self._City = None
        self._Sex = None
        self._KeyWord = None
        self._Offset = None
        self._Limit = None
        self._SubProjectId = None

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MarkFlag(self):
        return self._MarkFlag

    @MarkFlag.setter
    def MarkFlag(self, MarkFlag):
        self._MarkFlag = MarkFlag

    @property
    def TagIds(self):
        return self._TagIds

    @TagIds.setter
    def TagIds(self, TagIds):
        self._TagIds = TagIds

    @property
    def RelChannelFlag(self):
        return self._RelChannelFlag

    @RelChannelFlag.setter
    def RelChannelFlag(self, RelChannelFlag):
        self._RelChannelFlag = RelChannelFlag

    @property
    def NeedPhoneFlag(self):
        return self._NeedPhoneFlag

    @NeedPhoneFlag.setter
    def NeedPhoneFlag(self, NeedPhoneFlag):
        self._NeedPhoneFlag = NeedPhoneFlag

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def KeyWord(self):
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SubProjectId(self):
        return self._SubProjectId

    @SubProjectId.setter
    def SubProjectId(self, SubProjectId):
        self._SubProjectId = SubProjectId


    def _deserialize(self, params):
        self._QueryType = params.get("QueryType")
        self._GroupId = params.get("GroupId")
        self._MarkFlag = params.get("MarkFlag")
        self._TagIds = params.get("TagIds")
        self._RelChannelFlag = params.get("RelChannelFlag")
        self._NeedPhoneFlag = params.get("NeedPhoneFlag")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._Sex = params.get("Sex")
        self._KeyWord = params.get("KeyWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SubProjectId = params.get("SubProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomersResponse(AbstractModel):
    """DescribeCustomers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录条数
        :type TotalCount: int
        :param _UserList: 数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of CustomerInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = CustomerInfo()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectBudget: 项目预算
        :type ProjectBudget: float
        :param _ProjectOrg: 项目机构
        :type ProjectOrg: str
        :param _ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param _SubProjectList: 子项目列表
        :type SubProjectList: list of SubProjectInfo
        :param _ProjectStatus: 项目状态
        :type ProjectStatus: str
        :param _ProjectOrgId: 项目机构Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectOrgId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectBudget = None
        self._ProjectOrg = None
        self._ProjectIntroduction = None
        self._SubProjectList = None
        self._ProjectStatus = None
        self._ProjectOrgId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectBudget(self):
        return self._ProjectBudget

    @ProjectBudget.setter
    def ProjectBudget(self, ProjectBudget):
        self._ProjectBudget = ProjectBudget

    @property
    def ProjectOrg(self):
        return self._ProjectOrg

    @ProjectOrg.setter
    def ProjectOrg(self, ProjectOrg):
        self._ProjectOrg = ProjectOrg

    @property
    def ProjectIntroduction(self):
        return self._ProjectIntroduction

    @ProjectIntroduction.setter
    def ProjectIntroduction(self, ProjectIntroduction):
        self._ProjectIntroduction = ProjectIntroduction

    @property
    def SubProjectList(self):
        return self._SubProjectList

    @SubProjectList.setter
    def SubProjectList(self, SubProjectList):
        self._SubProjectList = SubProjectList

    @property
    def ProjectStatus(self):
        return self._ProjectStatus

    @ProjectStatus.setter
    def ProjectStatus(self, ProjectStatus):
        self._ProjectStatus = ProjectStatus

    @property
    def ProjectOrgId(self):
        return self._ProjectOrgId

    @ProjectOrgId.setter
    def ProjectOrgId(self, ProjectOrgId):
        self._ProjectOrgId = ProjectOrgId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectBudget = params.get("ProjectBudget")
        self._ProjectOrg = params.get("ProjectOrg")
        self._ProjectIntroduction = params.get("ProjectIntroduction")
        if params.get("SubProjectList") is not None:
            self._SubProjectList = []
            for item in params.get("SubProjectList"):
                obj = SubProjectInfo()
                obj._deserialize(item)
                self._SubProjectList.append(obj)
        self._ProjectStatus = params.get("ProjectStatus")
        self._ProjectOrgId = params.get("ProjectOrgId")
        self._RequestId = params.get("RequestId")


class DescribeProjectStockRequest(AbstractModel):
    """DescribeProjectStock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubProjectId: 子项目id
        :type SubProjectId: str
        """
        self._SubProjectId = None

    @property
    def SubProjectId(self):
        return self._SubProjectId

    @SubProjectId.setter
    def SubProjectId(self, SubProjectId):
        self._SubProjectId = SubProjectId


    def _deserialize(self, params):
        self._SubProjectId = params.get("SubProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectStockResponse(AbstractModel):
    """DescribeProjectStock返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectStocks: 项目库存列表
        :type ProjectStocks: list of ProjectStock
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectStocks = None
        self._RequestId = None

    @property
    def ProjectStocks(self):
        return self._ProjectStocks

    @ProjectStocks.setter
    def ProjectStocks(self, ProjectStocks):
        self._ProjectStocks = ProjectStocks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProjectStocks") is not None:
            self._ProjectStocks = []
            for item in params.get("ProjectStocks"):
                obj = ProjectStock()
                obj._deserialize(item)
                self._ProjectStocks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页面大小
        :type PageSize: int
        :param _SearchWord: 过滤规则
        :type SearchWord: str
        :param _Filters: 部门范围过滤
        :type Filters: :class:`tencentcloud.solar.v20181011.models.Filters`
        :param _ProjectStatus: 项目状态, 0:编辑中 1:运营中 2:已下线 3:已删除 4:审批中
        :type ProjectStatus: int
        """
        self._PageNo = None
        self._PageSize = None
        self._SearchWord = None
        self._Filters = None
        self._ProjectStatus = None

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ProjectStatus(self):
        return self._ProjectStatus

    @ProjectStatus.setter
    def ProjectStatus(self, ProjectStatus):
        self._ProjectStatus = ProjectStatus


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._SearchWord = params.get("SearchWord")
        if params.get("Filters") is not None:
            self._Filters = Filters()
            self._Filters._deserialize(params.get("Filters"))
        self._ProjectStatus = params.get("ProjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectList: 项目列表
        :type ProjectList: list of ProjectInfo
        :param _TotalCount: 项目数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProjectList(self):
        return self._ProjectList

    @ProjectList.setter
    def ProjectList(self, ProjectList):
        self._ProjectList = ProjectList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProjectList") is not None:
            self._ProjectList = []
            for item in params.get("ProjectList"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self._ProjectList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeResourceTemplateHeadersRequest(AbstractModel):
    """DescribeResourceTemplateHeaders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WxAppId: 微信公众号appId
        :type WxAppId: str
        """
        self._WxAppId = None

    @property
    def WxAppId(self):
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId


    def _deserialize(self, params):
        self._WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTemplateHeadersResponse(AbstractModel):
    """DescribeResourceTemplateHeaders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录条数
        :type TotalCount: int
        :param _TmplList: 模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplList: list of ResourceTemplateHeader
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TmplList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TmplList(self):
        return self._TmplList

    @TmplList.setter
    def TmplList(self, TmplList):
        self._TmplList = TmplList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TmplList") is not None:
            self._TmplList = []
            for item in params.get("TmplList"):
                obj = ResourceTemplateHeader()
                obj._deserialize(item)
                self._TmplList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubProjectRequest(AbstractModel):
    """DescribeSubProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubProjectId: 子项目id
        :type SubProjectId: str
        """
        self._SubProjectId = None

    @property
    def SubProjectId(self):
        return self._SubProjectId

    @SubProjectId.setter
    def SubProjectId(self, SubProjectId):
        self._SubProjectId = SubProjectId


    def _deserialize(self, params):
        self._SubProjectId = params.get("SubProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubProjectResponse(AbstractModel):
    """DescribeSubProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductInfo: 作品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductInfo: :class:`tencentcloud.solar.v20181011.models.ProductInfo`
        :param _ActivityInfo: 活动信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityInfo: :class:`tencentcloud.solar.v20181011.models.ActivityInfo`
        :param _ShareTitle: 分享标题
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareTitle: str
        :param _ShareDesc: 分享描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareDesc: str
        :param _ShareImg: 分享图标
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareImg: str
        :param _HasStrategy: 是否已创建策略
注意：此字段可能返回 null，表示取不到有效值。
        :type HasStrategy: int
        :param _SubProjectStatus: 子项目状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProjectStatus: str
        :param _ShareAppId: 分享公众号的appId
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareAppId: str
        :param _ShareWsId: 分享公众号的wsId
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareWsId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductInfo = None
        self._ActivityInfo = None
        self._ShareTitle = None
        self._ShareDesc = None
        self._ShareImg = None
        self._HasStrategy = None
        self._SubProjectStatus = None
        self._ShareAppId = None
        self._ShareWsId = None
        self._RequestId = None

    @property
    def ProductInfo(self):
        return self._ProductInfo

    @ProductInfo.setter
    def ProductInfo(self, ProductInfo):
        self._ProductInfo = ProductInfo

    @property
    def ActivityInfo(self):
        return self._ActivityInfo

    @ActivityInfo.setter
    def ActivityInfo(self, ActivityInfo):
        self._ActivityInfo = ActivityInfo

    @property
    def ShareTitle(self):
        return self._ShareTitle

    @ShareTitle.setter
    def ShareTitle(self, ShareTitle):
        self._ShareTitle = ShareTitle

    @property
    def ShareDesc(self):
        return self._ShareDesc

    @ShareDesc.setter
    def ShareDesc(self, ShareDesc):
        self._ShareDesc = ShareDesc

    @property
    def ShareImg(self):
        return self._ShareImg

    @ShareImg.setter
    def ShareImg(self, ShareImg):
        self._ShareImg = ShareImg

    @property
    def HasStrategy(self):
        return self._HasStrategy

    @HasStrategy.setter
    def HasStrategy(self, HasStrategy):
        self._HasStrategy = HasStrategy

    @property
    def SubProjectStatus(self):
        return self._SubProjectStatus

    @SubProjectStatus.setter
    def SubProjectStatus(self, SubProjectStatus):
        self._SubProjectStatus = SubProjectStatus

    @property
    def ShareAppId(self):
        return self._ShareAppId

    @ShareAppId.setter
    def ShareAppId(self, ShareAppId):
        self._ShareAppId = ShareAppId

    @property
    def ShareWsId(self):
        return self._ShareWsId

    @ShareWsId.setter
    def ShareWsId(self, ShareWsId):
        self._ShareWsId = ShareWsId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProductInfo") is not None:
            self._ProductInfo = ProductInfo()
            self._ProductInfo._deserialize(params.get("ProductInfo"))
        if params.get("ActivityInfo") is not None:
            self._ActivityInfo = ActivityInfo()
            self._ActivityInfo._deserialize(params.get("ActivityInfo"))
        self._ShareTitle = params.get("ShareTitle")
        self._ShareDesc = params.get("ShareDesc")
        self._ShareImg = params.get("ShareImg")
        self._HasStrategy = params.get("HasStrategy")
        self._SubProjectStatus = params.get("SubProjectStatus")
        self._ShareAppId = params.get("ShareAppId")
        self._ShareWsId = params.get("ShareWsId")
        self._RequestId = params.get("RequestId")


class ExpireFlowRequest(AbstractModel):
    """ExpireFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 工单ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpireFlowResponse(AbstractModel):
    """ExpireFlow返回参数结构体

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


class Filters(AbstractModel):
    """可见范围过滤参数

    """

    def __init__(self):
        r"""
        :param _Type: 过滤类型, 0: 默认(可见部门+自创) 1: 自创 2: 指定部门(部门在可见范围内)
        :type Type: int
        :param _DeptIds: 指定部门Id, 类型2使用
        :type DeptIds: list of str
        :param _UserIds: 用户Id列表
        :type UserIds: list of str
        """
        self._Type = None
        self._DeptIds = None
        self._UserIds = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DeptIds(self):
        return self._DeptIds

    @DeptIds.setter
    def DeptIds(self, DeptIds):
        self._DeptIds = DeptIds

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._DeptIds = params.get("DeptIds")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectBudget: 项目预算
        :type ProjectBudget: str
        :param _ProjectOrg: 项目机构
        :type ProjectOrg: str
        :param _ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param _ProjectOrgId: 项目机构Id
        :type ProjectOrgId: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectBudget = None
        self._ProjectOrg = None
        self._ProjectIntroduction = None
        self._ProjectOrgId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectBudget(self):
        return self._ProjectBudget

    @ProjectBudget.setter
    def ProjectBudget(self, ProjectBudget):
        self._ProjectBudget = ProjectBudget

    @property
    def ProjectOrg(self):
        return self._ProjectOrg

    @ProjectOrg.setter
    def ProjectOrg(self, ProjectOrg):
        self._ProjectOrg = ProjectOrg

    @property
    def ProjectIntroduction(self):
        return self._ProjectIntroduction

    @ProjectIntroduction.setter
    def ProjectIntroduction(self, ProjectIntroduction):
        self._ProjectIntroduction = ProjectIntroduction

    @property
    def ProjectOrgId(self):
        return self._ProjectOrgId

    @ProjectOrgId.setter
    def ProjectOrgId(self, ProjectOrgId):
        self._ProjectOrgId = ProjectOrgId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectBudget = params.get("ProjectBudget")
        self._ProjectOrg = params.get("ProjectOrg")
        self._ProjectIntroduction = params.get("ProjectIntroduction")
        self._ProjectOrgId = params.get("ProjectOrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

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


class OffLineProjectRequest(AbstractModel):
    """OffLineProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffLineProjectResponse(AbstractModel):
    """OffLineProject返回参数结构体

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


class ProductInfo(AbstractModel):
    """内容页结构

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _ProductTitle: 模板主题
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductTitle: str
        :param _ProductDesc: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductDesc: str
        :param _ProductCover: 模板封面地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCover: str
        :param _ProductId: 内容作品id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _ProductUrl: 作品预览链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductUrl: str
        :param _ProductName: 作品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        """
        self._TemplateId = None
        self._ProductTitle = None
        self._ProductDesc = None
        self._ProductCover = None
        self._ProductId = None
        self._ProductUrl = None
        self._ProductName = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ProductTitle(self):
        return self._ProductTitle

    @ProductTitle.setter
    def ProductTitle(self, ProductTitle):
        self._ProductTitle = ProductTitle

    @property
    def ProductDesc(self):
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def ProductCover(self):
        return self._ProductCover

    @ProductCover.setter
    def ProductCover(self, ProductCover):
        self._ProductCover = ProductCover

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductUrl(self):
        return self._ProductUrl

    @ProductUrl.setter
    def ProductUrl(self, ProductUrl):
        self._ProductUrl = ProductUrl

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._ProductTitle = params.get("ProductTitle")
        self._ProductDesc = params.get("ProductDesc")
        self._ProductCover = params.get("ProductCover")
        self._ProductId = params.get("ProductId")
        self._ProductUrl = params.get("ProductUrl")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """项目基础信息

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectOrg: 项目所属机构
        :type ProjectOrg: str
        :param _ProjectBudget: 项目预算
        :type ProjectBudget: float
        :param _ProjectStatus: 项目状态
        :type ProjectStatus: str
        :param _CreateTime: 项目创建时间
        :type CreateTime: str
        :param _ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param _ProjectOrgId: 项目所属机构Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectOrgId: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectOrg = None
        self._ProjectBudget = None
        self._ProjectStatus = None
        self._CreateTime = None
        self._ProjectIntroduction = None
        self._ProjectOrgId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectOrg(self):
        return self._ProjectOrg

    @ProjectOrg.setter
    def ProjectOrg(self, ProjectOrg):
        self._ProjectOrg = ProjectOrg

    @property
    def ProjectBudget(self):
        return self._ProjectBudget

    @ProjectBudget.setter
    def ProjectBudget(self, ProjectBudget):
        self._ProjectBudget = ProjectBudget

    @property
    def ProjectStatus(self):
        return self._ProjectStatus

    @ProjectStatus.setter
    def ProjectStatus(self, ProjectStatus):
        self._ProjectStatus = ProjectStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectIntroduction(self):
        return self._ProjectIntroduction

    @ProjectIntroduction.setter
    def ProjectIntroduction(self, ProjectIntroduction):
        self._ProjectIntroduction = ProjectIntroduction

    @property
    def ProjectOrgId(self):
        return self._ProjectOrgId

    @ProjectOrgId.setter
    def ProjectOrgId(self, ProjectOrgId):
        self._ProjectOrgId = ProjectOrgId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectOrg = params.get("ProjectOrg")
        self._ProjectBudget = params.get("ProjectBudget")
        self._ProjectStatus = params.get("ProjectStatus")
        self._CreateTime = params.get("CreateTime")
        self._ProjectIntroduction = params.get("ProjectIntroduction")
        self._ProjectOrgId = params.get("ProjectOrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectStock(AbstractModel):
    """项目奖品库存

    """

    def __init__(self):
        r"""
        :param _PrizeId: 奖品id
        :type PrizeId: str
        :param _PrizeBat: 奖品批次
        :type PrizeBat: int
        :param _PrizeName: 奖品名称
        :type PrizeName: str
        :param _UsedStock: 已分配奖品数量
        :type UsedStock: int
        :param _RemainStock: 该奖品剩余库存数量
        :type RemainStock: int
        :param _PoolIdx: 奖品所在奖池index
        :type PoolIdx: int
        :param _PoolName: 奖品所在奖池名称
        :type PoolName: str
        """
        self._PrizeId = None
        self._PrizeBat = None
        self._PrizeName = None
        self._UsedStock = None
        self._RemainStock = None
        self._PoolIdx = None
        self._PoolName = None

    @property
    def PrizeId(self):
        return self._PrizeId

    @PrizeId.setter
    def PrizeId(self, PrizeId):
        self._PrizeId = PrizeId

    @property
    def PrizeBat(self):
        return self._PrizeBat

    @PrizeBat.setter
    def PrizeBat(self, PrizeBat):
        self._PrizeBat = PrizeBat

    @property
    def PrizeName(self):
        return self._PrizeName

    @PrizeName.setter
    def PrizeName(self, PrizeName):
        self._PrizeName = PrizeName

    @property
    def UsedStock(self):
        return self._UsedStock

    @UsedStock.setter
    def UsedStock(self, UsedStock):
        self._UsedStock = UsedStock

    @property
    def RemainStock(self):
        return self._RemainStock

    @RemainStock.setter
    def RemainStock(self, RemainStock):
        self._RemainStock = RemainStock

    @property
    def PoolIdx(self):
        return self._PoolIdx

    @PoolIdx.setter
    def PoolIdx(self, PoolIdx):
        self._PoolIdx = PoolIdx

    @property
    def PoolName(self):
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName


    def _deserialize(self, params):
        self._PrizeId = params.get("PrizeId")
        self._PrizeBat = params.get("PrizeBat")
        self._PrizeName = params.get("PrizeName")
        self._UsedStock = params.get("UsedStock")
        self._RemainStock = params.get("RemainStock")
        self._PoolIdx = params.get("PoolIdx")
        self._PoolName = params.get("PoolName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplenishProjectStockRequest(AbstractModel):
    """ReplenishProjectStock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubProjectId: 项目id
        :type SubProjectId: str
        :param _PrizeId: 奖品id
        :type PrizeId: str
        :param _PrizeNum: 奖品数量
        :type PrizeNum: int
        :param _PoolIndex: 奖池索引
        :type PoolIndex: int
        :param _PoolName: 奖池名称
        :type PoolName: str
        """
        self._SubProjectId = None
        self._PrizeId = None
        self._PrizeNum = None
        self._PoolIndex = None
        self._PoolName = None

    @property
    def SubProjectId(self):
        return self._SubProjectId

    @SubProjectId.setter
    def SubProjectId(self, SubProjectId):
        self._SubProjectId = SubProjectId

    @property
    def PrizeId(self):
        return self._PrizeId

    @PrizeId.setter
    def PrizeId(self, PrizeId):
        self._PrizeId = PrizeId

    @property
    def PrizeNum(self):
        return self._PrizeNum

    @PrizeNum.setter
    def PrizeNum(self, PrizeNum):
        self._PrizeNum = PrizeNum

    @property
    def PoolIndex(self):
        return self._PoolIndex

    @PoolIndex.setter
    def PoolIndex(self, PoolIndex):
        self._PoolIndex = PoolIndex

    @property
    def PoolName(self):
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName


    def _deserialize(self, params):
        self._SubProjectId = params.get("SubProjectId")
        self._PrizeId = params.get("PrizeId")
        self._PrizeNum = params.get("PrizeNum")
        self._PoolIndex = params.get("PoolIndex")
        self._PoolName = params.get("PoolName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplenishProjectStockResponse(AbstractModel):
    """ReplenishProjectStock返回参数结构体

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


class ResourceTemplateHeader(AbstractModel):
    """素材模板消息标题的样例列表

    """

    def __init__(self):
        r"""
        :param _Content: 模板预览区内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Example: 模板预览示例
注意：此字段可能返回 null，表示取不到有效值。
        :type Example: str
        :param _KeyArray: 模板预览区域键数组
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyArray: str
        :param _TemplateId: 模板id
        :type TemplateId: str
        :param _Title: 模板标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        """
        self._Content = None
        self._Example = None
        self._KeyArray = None
        self._TemplateId = None
        self._Title = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Example(self):
        return self._Example

    @Example.setter
    def Example(self, Example):
        self._Example = Example

    @property
    def KeyArray(self):
        return self._KeyArray

    @KeyArray.setter
    def KeyArray(self, KeyArray):
        self._KeyArray = KeyArray

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Example = params.get("Example")
        self._KeyArray = params.get("KeyArray")
        self._TemplateId = params.get("TemplateId")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendWxTouchTaskRequest(AbstractModel):
    """SendWxTouchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 客户分组ID
        :type GroupId: str
        :param _DistinctFlag: 去除今日已发送的客户
        :type DistinctFlag: bool
        :param _IsSendNow: 是否立马发送
        :type IsSendNow: bool
        :param _SendDate: 发送时间，一般为0
        :type SendDate: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _WxTouchType: 微信触达类型，text, news, smallapp, tmplmsg
        :type WxTouchType: str
        :param _Title: 标题
        :type Title: str
        :param _Content: 文本内容
        :type Content: str
        :param _NewsId: 图文素材ID
        :type NewsId: str
        :param _SmallProgramId: 小程序卡片ID
        :type SmallProgramId: str
        :param _TemplateId: 模板消息ID
        :type TemplateId: str
        :param _WxAppId: 微信公众号appId
        :type WxAppId: str
        """
        self._GroupId = None
        self._DistinctFlag = None
        self._IsSendNow = None
        self._SendDate = None
        self._TaskName = None
        self._WxTouchType = None
        self._Title = None
        self._Content = None
        self._NewsId = None
        self._SmallProgramId = None
        self._TemplateId = None
        self._WxAppId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DistinctFlag(self):
        return self._DistinctFlag

    @DistinctFlag.setter
    def DistinctFlag(self, DistinctFlag):
        self._DistinctFlag = DistinctFlag

    @property
    def IsSendNow(self):
        return self._IsSendNow

    @IsSendNow.setter
    def IsSendNow(self, IsSendNow):
        self._IsSendNow = IsSendNow

    @property
    def SendDate(self):
        return self._SendDate

    @SendDate.setter
    def SendDate(self, SendDate):
        self._SendDate = SendDate

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def WxTouchType(self):
        return self._WxTouchType

    @WxTouchType.setter
    def WxTouchType(self, WxTouchType):
        self._WxTouchType = WxTouchType

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def NewsId(self):
        return self._NewsId

    @NewsId.setter
    def NewsId(self, NewsId):
        self._NewsId = NewsId

    @property
    def SmallProgramId(self):
        return self._SmallProgramId

    @SmallProgramId.setter
    def SmallProgramId(self, SmallProgramId):
        self._SmallProgramId = SmallProgramId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def WxAppId(self):
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._DistinctFlag = params.get("DistinctFlag")
        self._IsSendNow = params.get("IsSendNow")
        self._SendDate = params.get("SendDate")
        self._TaskName = params.get("TaskName")
        self._WxTouchType = params.get("WxTouchType")
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._NewsId = params.get("NewsId")
        self._SmallProgramId = params.get("SmallProgramId")
        self._TemplateId = params.get("TemplateId")
        self._WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendWxTouchTaskResponse(AbstractModel):
    """SendWxTouchTask返回参数结构体

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


class SubProjectInfo(AbstractModel):
    """子项目信息

    """

    def __init__(self):
        r"""
        :param _SubProjectId: 子项目id
        :type SubProjectId: str
        :param _SubProjectName: 子项目名称
        :type SubProjectName: str
        :param _SubProjectStatus: 子项目状态
        :type SubProjectStatus: str
        """
        self._SubProjectId = None
        self._SubProjectName = None
        self._SubProjectStatus = None

    @property
    def SubProjectId(self):
        return self._SubProjectId

    @SubProjectId.setter
    def SubProjectId(self, SubProjectId):
        self._SubProjectId = SubProjectId

    @property
    def SubProjectName(self):
        return self._SubProjectName

    @SubProjectName.setter
    def SubProjectName(self, SubProjectName):
        self._SubProjectName = SubProjectName

    @property
    def SubProjectStatus(self):
        return self._SubProjectStatus

    @SubProjectStatus.setter
    def SubProjectStatus(self, SubProjectStatus):
        self._SubProjectStatus = SubProjectStatus


    def _deserialize(self, params):
        self._SubProjectId = params.get("SubProjectId")
        self._SubProjectName = params.get("SubProjectName")
        self._SubProjectStatus = params.get("SubProjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        