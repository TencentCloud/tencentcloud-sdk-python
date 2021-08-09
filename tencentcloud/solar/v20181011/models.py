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
        """
        :param TemplateId: 活动使用模板id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TemplateId: str\n        :param ActivityTitle: 活动标题
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityTitle: str\n        :param ActivityDesc: 活动描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityDesc: str\n        :param ActivityCover: 活动封面地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityCover: str\n        :param ActivityType: 活动类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityType: str\n        :param ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityId: str\n        :param PersonalConfig: 活动模板自定义配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type PersonalConfig: str\n        """
        self.TemplateId = None
        self.ActivityTitle = None
        self.ActivityDesc = None
        self.ActivityCover = None
        self.ActivityType = None
        self.ActivityId = None
        self.PersonalConfig = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.ActivityTitle = params.get("ActivityTitle")
        self.ActivityDesc = params.get("ActivityDesc")
        self.ActivityCover = params.get("ActivityCover")
        self.ActivityType = params.get("ActivityType")
        self.ActivityId = params.get("ActivityId")
        self.PersonalConfig = params.get("PersonalConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStaffChUserRequest(AbstractModel):
    """CheckStaffChUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 员工ID\n        :type UserId: list of str\n        :param OperateType: 渠道状态：checkpass审核通过, checkreject审核拒绝, enableoperate启用, stopoperate停用\n        :type OperateType: str\n        """
        self.UserId = None
        self.OperateType = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.OperateType = params.get("OperateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckStaffChUserResponse(AbstractModel):
    """CheckStaffChUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CopyActivityChannelRequest(AbstractModel):
    """CopyActivityChannel请求参数结构体

    """

    def __init__(self):
        """
        :param ActivityId: 活动ID\n        :type ActivityId: str\n        :param ChannelFrom: 来源渠道ID\n        :type ChannelFrom: str\n        :param ChannelTo: 目的渠道id\n        :type ChannelTo: list of str\n        """
        self.ActivityId = None
        self.ChannelFrom = None
        self.ChannelTo = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.ChannelFrom = params.get("ChannelFrom")
        self.ChannelTo = params.get("ChannelTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyActivityChannelResponse(AbstractModel):
    """CopyActivityChannel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectOrg: 项目机构\n        :type ProjectOrg: str\n        :param ProjectBudget: 项目预算\n        :type ProjectBudget: str\n        :param ProjectIntroduction: 项目简介\n        :type ProjectIntroduction: str\n        :param ProjectOrgId: 所属部门ID\n        :type ProjectOrgId: str\n        """
        self.ProjectName = None
        self.ProjectOrg = None
        self.ProjectBudget = None
        self.ProjectIntroduction = None
        self.ProjectOrgId = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectOrg = params.get("ProjectOrg")
        self.ProjectBudget = params.get("ProjectBudget")
        self.ProjectIntroduction = params.get("ProjectIntroduction")
        self.ProjectOrgId = params.get("ProjectOrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RequestId = params.get("RequestId")


class CreateSubProjectRequest(AbstractModel):
    """CreateSubProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 所属项目id\n        :type ProjectId: str\n        :param SubProjectName: 子项目名称\n        :type SubProjectName: str\n        """
        self.ProjectId = None
        self.SubProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SubProjectName = params.get("SubProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubProjectResponse(AbstractModel):
    """CreateSubProject返回参数结构体

    """

    def __init__(self):
        """
        :param SubProjectId: 子项目id\n        :type SubProjectId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SubProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubProjectId = params.get("SubProjectId")
        self.RequestId = params.get("RequestId")


class CustomerInfo(AbstractModel):
    """客户档案

    """

    def __init__(self):
        """
        :param Activity: 总活跃度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Activity: int\n        :param AudienceUserId: 客户ID\n        :type AudienceUserId: str\n        :param Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。\n        :type Avatar: str\n        :param City: 最近记录城市
注意：此字段可能返回 null，表示取不到有效值。\n        :type City: str\n        :param LastActiveTime: 最活跃时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastActiveTime: str\n        :param MarkFlag: 是否星标客户
注意：此字段可能返回 null，表示取不到有效值。\n        :type MarkFlag: str\n        :param MonthActive: 30天活跃度
注意：此字段可能返回 null，表示取不到有效值。\n        :type MonthActive: int\n        :param MonthRecommend: 30天推荐度
注意：此字段可能返回 null，表示取不到有效值。\n        :type MonthRecommend: int\n        :param Phone: 手机号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Phone: str\n        :param Province: 最近记录省份
注意：此字段可能返回 null，表示取不到有效值。\n        :type Province: str\n        :param RealName: 姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealName: str\n        :param RelChannelFlag: 员工标识 0 未关联 1 已关联
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelChannelFlag: int\n        :param Sex: 性别 1男 2女
注意：此字段可能返回 null，表示取不到有效值。\n        :type Sex: int\n        :param Spread: 传播力（好友数）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Spread: int\n        :param WeekActive: 7天活跃度
注意：此字段可能返回 null，表示取不到有效值。\n        :type WeekActive: int\n        :param WeekRecommend: 7天推荐度
注意：此字段可能返回 null，表示取不到有效值。\n        :type WeekRecommend: int\n        :param WxCity: 微信城市
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxCity: str\n        :param WxCountry: 微信国家或地区
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxCountry: str\n        :param WxNickname: 微信呢称
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxNickname: str\n        :param WxProvince: 微信省份
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxProvince: str\n        """
        self.Activity = None
        self.AudienceUserId = None
        self.Avatar = None
        self.City = None
        self.LastActiveTime = None
        self.MarkFlag = None
        self.MonthActive = None
        self.MonthRecommend = None
        self.Phone = None
        self.Province = None
        self.RealName = None
        self.RelChannelFlag = None
        self.Sex = None
        self.Spread = None
        self.WeekActive = None
        self.WeekRecommend = None
        self.WxCity = None
        self.WxCountry = None
        self.WxNickname = None
        self.WxProvince = None


    def _deserialize(self, params):
        self.Activity = params.get("Activity")
        self.AudienceUserId = params.get("AudienceUserId")
        self.Avatar = params.get("Avatar")
        self.City = params.get("City")
        self.LastActiveTime = params.get("LastActiveTime")
        self.MarkFlag = params.get("MarkFlag")
        self.MonthActive = params.get("MonthActive")
        self.MonthRecommend = params.get("MonthRecommend")
        self.Phone = params.get("Phone")
        self.Province = params.get("Province")
        self.RealName = params.get("RealName")
        self.RelChannelFlag = params.get("RelChannelFlag")
        self.Sex = params.get("Sex")
        self.Spread = params.get("Spread")
        self.WeekActive = params.get("WeekActive")
        self.WeekRecommend = params.get("WeekRecommend")
        self.WxCity = params.get("WxCity")
        self.WxCountry = params.get("WxCountry")
        self.WxNickname = params.get("WxNickname")
        self.WxProvince = params.get("WxProvince")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomerRequest(AbstractModel):
    """DescribeCustomer请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户ID\n        :type UserId: str\n        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerResponse(AbstractModel):
    """DescribeCustomer返回参数结构体

    """

    def __init__(self):
        """
        :param AddressList: 地址列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddressList: list of str\n        :param UserId: 用户id
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserId: str\n        :param Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。\n        :type Avatar: str\n        :param Birthday: 生日
注意：此字段可能返回 null，表示取不到有效值。\n        :type Birthday: str\n        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。\n        :type City: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Device: 设备
注意：此字段可能返回 null，表示取不到有效值。\n        :type Device: str\n        :param Industrys: 行业
注意：此字段可能返回 null，表示取不到有效值。\n        :type Industrys: list of str\n        :param LastActiveTime: 上次登录时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastActiveTime: str\n        :param MarkFlag: 是否星标 1是 0否
注意：此字段可能返回 null，表示取不到有效值。\n        :type MarkFlag: str\n        :param Model: 手机型号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Model: str\n        :param OpenId: 微信openid
注意：此字段可能返回 null，表示取不到有效值。\n        :type OpenId: str\n        :param PayFeature: 消费特点
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayFeature: str\n        :param Phone: 手机号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Phone: str\n        :param PhoneList: 手机号码列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneList: str\n        :param Province: 最近记录省份
注意：此字段可能返回 null，表示取不到有效值。\n        :type Province: str\n        :param RealName: 姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealName: str\n        :param RelChannelFlag: 员工标识 0：非员工 1：员工
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelChannelFlag: str\n        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param Sex: 性别 1男 2女
注意：此字段可能返回 null，表示取不到有效值。\n        :type Sex: str\n        :param SourceAudienceVo: 最初来源
注意：此字段可能返回 null，表示取不到有效值。\n        :type SourceAudienceVo: str\n        :param SubWechats: 关注公众号列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubWechats: list of str\n        :param UnionId: 微信unionid
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnionId: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param UserTypes: 用户类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserTypes: list of str\n        :param WxCity: 城市
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxCity: str\n        :param WxCountry: 国家
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxCountry: str\n        :param WxNickname: 昵称
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxNickname: str\n        :param WxProvince: 省份
注意：此字段可能返回 null，表示取不到有效值。\n        :type WxProvince: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddressList = None
        self.UserId = None
        self.Avatar = None
        self.Birthday = None
        self.City = None
        self.CreateTime = None
        self.Device = None
        self.Industrys = None
        self.LastActiveTime = None
        self.MarkFlag = None
        self.Model = None
        self.OpenId = None
        self.PayFeature = None
        self.Phone = None
        self.PhoneList = None
        self.Province = None
        self.RealName = None
        self.RelChannelFlag = None
        self.Remark = None
        self.Sex = None
        self.SourceAudienceVo = None
        self.SubWechats = None
        self.UnionId = None
        self.UpdateTime = None
        self.UserTypes = None
        self.WxCity = None
        self.WxCountry = None
        self.WxNickname = None
        self.WxProvince = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressList = params.get("AddressList")
        self.UserId = params.get("UserId")
        self.Avatar = params.get("Avatar")
        self.Birthday = params.get("Birthday")
        self.City = params.get("City")
        self.CreateTime = params.get("CreateTime")
        self.Device = params.get("Device")
        self.Industrys = params.get("Industrys")
        self.LastActiveTime = params.get("LastActiveTime")
        self.MarkFlag = params.get("MarkFlag")
        self.Model = params.get("Model")
        self.OpenId = params.get("OpenId")
        self.PayFeature = params.get("PayFeature")
        self.Phone = params.get("Phone")
        self.PhoneList = params.get("PhoneList")
        self.Province = params.get("Province")
        self.RealName = params.get("RealName")
        self.RelChannelFlag = params.get("RelChannelFlag")
        self.Remark = params.get("Remark")
        self.Sex = params.get("Sex")
        self.SourceAudienceVo = params.get("SourceAudienceVo")
        self.SubWechats = params.get("SubWechats")
        self.UnionId = params.get("UnionId")
        self.UpdateTime = params.get("UpdateTime")
        self.UserTypes = params.get("UserTypes")
        self.WxCity = params.get("WxCity")
        self.WxCountry = params.get("WxCountry")
        self.WxNickname = params.get("WxNickname")
        self.WxProvince = params.get("WxProvince")
        self.RequestId = params.get("RequestId")


class DescribeCustomersRequest(AbstractModel):
    """DescribeCustomers请求参数结构体

    """

    def __init__(self):
        """
        :param QueryType: 查询类型，0.个人，1负责部门，2.指定部门\n        :type QueryType: str\n        :param GroupId: 分组ID\n        :type GroupId: str\n        :param MarkFlag: 是否星级标记 1是 0否\n        :type MarkFlag: int\n        :param TagIds: 客户标签，多个标签用逗号隔开\n        :type TagIds: str\n        :param RelChannelFlag: 员工标识筛选，0：非员工，1：员工\n        :type RelChannelFlag: str\n        :param NeedPhoneFlag: 必须存在手机 1是 0否\n        :type NeedPhoneFlag: int\n        :param Province: 省份\n        :type Province: str\n        :param City: 城市\n        :type City: str\n        :param Sex: 性别 1男 2女\n        :type Sex: str\n        :param KeyWord: 城市\n        :type KeyWord: str\n        :param Offset: 查询开始位置\n        :type Offset: int\n        :param Limit: 每页记录条数\n        :type Limit: int\n        :param SubProjectId: 子项目ID\n        :type SubProjectId: str\n        """
        self.QueryType = None
        self.GroupId = None
        self.MarkFlag = None
        self.TagIds = None
        self.RelChannelFlag = None
        self.NeedPhoneFlag = None
        self.Province = None
        self.City = None
        self.Sex = None
        self.KeyWord = None
        self.Offset = None
        self.Limit = None
        self.SubProjectId = None


    def _deserialize(self, params):
        self.QueryType = params.get("QueryType")
        self.GroupId = params.get("GroupId")
        self.MarkFlag = params.get("MarkFlag")
        self.TagIds = params.get("TagIds")
        self.RelChannelFlag = params.get("RelChannelFlag")
        self.NeedPhoneFlag = params.get("NeedPhoneFlag")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Sex = params.get("Sex")
        self.KeyWord = params.get("KeyWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubProjectId = params.get("SubProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomersResponse(AbstractModel):
    """DescribeCustomers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录条数\n        :type TotalCount: int\n        :param UserList: 数据列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserList: list of CustomerInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.UserList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = CustomerInfo()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目id\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectBudget: 项目预算\n        :type ProjectBudget: float\n        :param ProjectOrg: 项目机构\n        :type ProjectOrg: str\n        :param ProjectIntroduction: 项目简介\n        :type ProjectIntroduction: str\n        :param SubProjectList: 子项目列表\n        :type SubProjectList: list of SubProjectInfo\n        :param ProjectStatus: 项目状态\n        :type ProjectStatus: str\n        :param ProjectOrgId: 项目机构Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectOrgId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectBudget = None
        self.ProjectOrg = None
        self.ProjectIntroduction = None
        self.SubProjectList = None
        self.ProjectStatus = None
        self.ProjectOrgId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectBudget = params.get("ProjectBudget")
        self.ProjectOrg = params.get("ProjectOrg")
        self.ProjectIntroduction = params.get("ProjectIntroduction")
        if params.get("SubProjectList") is not None:
            self.SubProjectList = []
            for item in params.get("SubProjectList"):
                obj = SubProjectInfo()
                obj._deserialize(item)
                self.SubProjectList.append(obj)
        self.ProjectStatus = params.get("ProjectStatus")
        self.ProjectOrgId = params.get("ProjectOrgId")
        self.RequestId = params.get("RequestId")


class DescribeProjectStockRequest(AbstractModel):
    """DescribeProjectStock请求参数结构体

    """

    def __init__(self):
        """
        :param SubProjectId: 子项目id\n        :type SubProjectId: str\n        """
        self.SubProjectId = None


    def _deserialize(self, params):
        self.SubProjectId = params.get("SubProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectStockResponse(AbstractModel):
    """DescribeProjectStock返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectStocks: 项目库存列表\n        :type ProjectStocks: list of ProjectStock\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProjectStocks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectStocks") is not None:
            self.ProjectStocks = []
            for item in params.get("ProjectStocks"):
                obj = ProjectStock()
                obj._deserialize(item)
                self.ProjectStocks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        """
        :param PageNo: 页码\n        :type PageNo: int\n        :param PageSize: 页面大小\n        :type PageSize: int\n        :param SearchWord: 过滤规则\n        :type SearchWord: str\n        :param Filters: 部门范围过滤\n        :type Filters: :class:`tencentcloud.solar.v20181011.models.Filters`\n        :param ProjectStatus: 项目状态, 0:编辑中 1:运营中 2:已下线 3:已删除 4:审批中\n        :type ProjectStatus: int\n        """
        self.PageNo = None
        self.PageSize = None
        self.SearchWord = None
        self.Filters = None
        self.ProjectStatus = None


    def _deserialize(self, params):
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.SearchWord = params.get("SearchWord")
        if params.get("Filters") is not None:
            self.Filters = Filters()
            self.Filters._deserialize(params.get("Filters"))
        self.ProjectStatus = params.get("ProjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectList: 项目列表\n        :type ProjectList: list of ProjectInfo\n        :param TotalCount: 项目数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProjectList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectList") is not None:
            self.ProjectList = []
            for item in params.get("ProjectList"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self.ProjectList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeResourceTemplateHeadersRequest(AbstractModel):
    """DescribeResourceTemplateHeaders请求参数结构体

    """

    def __init__(self):
        """
        :param WxAppId: 微信公众号appId\n        :type WxAppId: str\n        """
        self.WxAppId = None


    def _deserialize(self, params):
        self.WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTemplateHeadersResponse(AbstractModel):
    """DescribeResourceTemplateHeaders返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录条数\n        :type TotalCount: int\n        :param TmplList: 模板列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TmplList: list of ResourceTemplateHeader\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TmplList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TmplList") is not None:
            self.TmplList = []
            for item in params.get("TmplList"):
                obj = ResourceTemplateHeader()
                obj._deserialize(item)
                self.TmplList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubProjectRequest(AbstractModel):
    """DescribeSubProject请求参数结构体

    """

    def __init__(self):
        """
        :param SubProjectId: 子项目id\n        :type SubProjectId: str\n        """
        self.SubProjectId = None


    def _deserialize(self, params):
        self.SubProjectId = params.get("SubProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubProjectResponse(AbstractModel):
    """DescribeSubProject返回参数结构体

    """

    def __init__(self):
        """
        :param ProductInfo: 作品信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductInfo: :class:`tencentcloud.solar.v20181011.models.ProductInfo`\n        :param ActivityInfo: 活动信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityInfo: :class:`tencentcloud.solar.v20181011.models.ActivityInfo`\n        :param ShareTitle: 分享标题
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShareTitle: str\n        :param ShareDesc: 分享描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShareDesc: str\n        :param ShareImg: 分享图标
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShareImg: str\n        :param HasStrategy: 是否已创建策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type HasStrategy: int\n        :param SubProjectStatus: 子项目状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubProjectStatus: str\n        :param ShareAppId: 分享公众号的appId
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShareAppId: str\n        :param ShareWsId: 分享公众号的wsId
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShareWsId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProductInfo = None
        self.ActivityInfo = None
        self.ShareTitle = None
        self.ShareDesc = None
        self.ShareImg = None
        self.HasStrategy = None
        self.SubProjectStatus = None
        self.ShareAppId = None
        self.ShareWsId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProductInfo") is not None:
            self.ProductInfo = ProductInfo()
            self.ProductInfo._deserialize(params.get("ProductInfo"))
        if params.get("ActivityInfo") is not None:
            self.ActivityInfo = ActivityInfo()
            self.ActivityInfo._deserialize(params.get("ActivityInfo"))
        self.ShareTitle = params.get("ShareTitle")
        self.ShareDesc = params.get("ShareDesc")
        self.ShareImg = params.get("ShareImg")
        self.HasStrategy = params.get("HasStrategy")
        self.SubProjectStatus = params.get("SubProjectStatus")
        self.ShareAppId = params.get("ShareAppId")
        self.ShareWsId = params.get("ShareWsId")
        self.RequestId = params.get("RequestId")


class ExpireFlowRequest(AbstractModel):
    """ExpireFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工单ID\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpireFlowResponse(AbstractModel):
    """ExpireFlow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filters(AbstractModel):
    """可见范围过滤参数

    """

    def __init__(self):
        """
        :param Type: 过滤类型, 0: 默认(可见部门+自创) 1: 自创 2: 指定部门(部门在可见范围内)\n        :type Type: int\n        :param DeptIds: 指定部门Id, 类型2使用\n        :type DeptIds: list of str\n        :param UserIds: 用户Id列表\n        :type UserIds: list of str\n        """
        self.Type = None
        self.DeptIds = None
        self.UserIds = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.DeptIds = params.get("DeptIds")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectBudget: 项目预算\n        :type ProjectBudget: str\n        :param ProjectOrg: 项目机构\n        :type ProjectOrg: str\n        :param ProjectIntroduction: 项目简介\n        :type ProjectIntroduction: str\n        :param ProjectOrgId: 项目机构Id\n        :type ProjectOrgId: str\n        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectBudget = None
        self.ProjectOrg = None
        self.ProjectIntroduction = None
        self.ProjectOrgId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectBudget = params.get("ProjectBudget")
        self.ProjectOrg = params.get("ProjectOrg")
        self.ProjectIntroduction = params.get("ProjectIntroduction")
        self.ProjectOrgId = params.get("ProjectOrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OffLineProjectRequest(AbstractModel):
    """OffLineProject请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffLineProjectResponse(AbstractModel):
    """OffLineProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProductInfo(AbstractModel):
    """内容页结构

    """

    def __init__(self):
        """
        :param TemplateId: 模板id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TemplateId: str\n        :param ProductTitle: 模板主题
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductTitle: str\n        :param ProductDesc: 模板描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductDesc: str\n        :param ProductCover: 模板封面地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductCover: str\n        :param ProductId: 内容作品id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param ProductUrl: 作品预览链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductUrl: str\n        :param ProductName: 作品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductName: str\n        """
        self.TemplateId = None
        self.ProductTitle = None
        self.ProductDesc = None
        self.ProductCover = None
        self.ProductId = None
        self.ProductUrl = None
        self.ProductName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.ProductTitle = params.get("ProductTitle")
        self.ProductDesc = params.get("ProductDesc")
        self.ProductCover = params.get("ProductCover")
        self.ProductId = params.get("ProductId")
        self.ProductUrl = params.get("ProductUrl")
        self.ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """项目基础信息

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param ProjectOrg: 项目所属机构\n        :type ProjectOrg: str\n        :param ProjectBudget: 项目预算\n        :type ProjectBudget: float\n        :param ProjectStatus: 项目状态\n        :type ProjectStatus: str\n        :param CreateTime: 项目创建时间\n        :type CreateTime: str\n        :param ProjectIntroduction: 项目简介\n        :type ProjectIntroduction: str\n        :param ProjectOrgId: 项目所属机构Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectOrgId: str\n        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectOrg = None
        self.ProjectBudget = None
        self.ProjectStatus = None
        self.CreateTime = None
        self.ProjectIntroduction = None
        self.ProjectOrgId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectOrg = params.get("ProjectOrg")
        self.ProjectBudget = params.get("ProjectBudget")
        self.ProjectStatus = params.get("ProjectStatus")
        self.CreateTime = params.get("CreateTime")
        self.ProjectIntroduction = params.get("ProjectIntroduction")
        self.ProjectOrgId = params.get("ProjectOrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectStock(AbstractModel):
    """项目奖品库存

    """

    def __init__(self):
        """
        :param PrizeId: 奖品id\n        :type PrizeId: str\n        :param PrizeBat: 奖品批次\n        :type PrizeBat: int\n        :param PrizeName: 奖品名称\n        :type PrizeName: str\n        :param UsedStock: 已分配奖品数量\n        :type UsedStock: int\n        :param RemainStock: 该奖品剩余库存数量\n        :type RemainStock: int\n        :param PoolIdx: 奖品所在奖池index\n        :type PoolIdx: int\n        :param PoolName: 奖品所在奖池名称\n        :type PoolName: str\n        """
        self.PrizeId = None
        self.PrizeBat = None
        self.PrizeName = None
        self.UsedStock = None
        self.RemainStock = None
        self.PoolIdx = None
        self.PoolName = None


    def _deserialize(self, params):
        self.PrizeId = params.get("PrizeId")
        self.PrizeBat = params.get("PrizeBat")
        self.PrizeName = params.get("PrizeName")
        self.UsedStock = params.get("UsedStock")
        self.RemainStock = params.get("RemainStock")
        self.PoolIdx = params.get("PoolIdx")
        self.PoolName = params.get("PoolName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplenishProjectStockRequest(AbstractModel):
    """ReplenishProjectStock请求参数结构体

    """

    def __init__(self):
        """
        :param SubProjectId: 项目id\n        :type SubProjectId: str\n        :param PrizeId: 奖品id\n        :type PrizeId: str\n        :param PrizeNum: 奖品数量\n        :type PrizeNum: int\n        :param PoolIndex: 奖池索引\n        :type PoolIndex: int\n        :param PoolName: 奖池名称\n        :type PoolName: str\n        """
        self.SubProjectId = None
        self.PrizeId = None
        self.PrizeNum = None
        self.PoolIndex = None
        self.PoolName = None


    def _deserialize(self, params):
        self.SubProjectId = params.get("SubProjectId")
        self.PrizeId = params.get("PrizeId")
        self.PrizeNum = params.get("PrizeNum")
        self.PoolIndex = params.get("PoolIndex")
        self.PoolName = params.get("PoolName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplenishProjectStockResponse(AbstractModel):
    """ReplenishProjectStock返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceTemplateHeader(AbstractModel):
    """素材模板消息标题的样例列表

    """

    def __init__(self):
        """
        :param Content: 模板预览区内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: str\n        :param Example: 模板预览示例
注意：此字段可能返回 null，表示取不到有效值。\n        :type Example: str\n        :param KeyArray: 模板预览区域键数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyArray: str\n        :param TemplateId: 模板id\n        :type TemplateId: str\n        :param Title: 模板标题
注意：此字段可能返回 null，表示取不到有效值。\n        :type Title: str\n        """
        self.Content = None
        self.Example = None
        self.KeyArray = None
        self.TemplateId = None
        self.Title = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Example = params.get("Example")
        self.KeyArray = params.get("KeyArray")
        self.TemplateId = params.get("TemplateId")
        self.Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendWxTouchTaskRequest(AbstractModel):
    """SendWxTouchTask请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 客户分组ID\n        :type GroupId: str\n        :param DistinctFlag: 去除今日已发送的客户\n        :type DistinctFlag: bool\n        :param IsSendNow: 是否立马发送\n        :type IsSendNow: bool\n        :param SendDate: 发送时间，一般为0\n        :type SendDate: int\n        :param TaskName: 任务名称\n        :type TaskName: str\n        :param WxTouchType: 微信触达类型，text, news, smallapp, tmplmsg\n        :type WxTouchType: str\n        :param Title: 标题\n        :type Title: str\n        :param Content: 文本内容\n        :type Content: str\n        :param NewsId: 图文素材ID\n        :type NewsId: str\n        :param SmallProgramId: 小程序卡片ID\n        :type SmallProgramId: str\n        :param TemplateId: 模板消息ID\n        :type TemplateId: str\n        :param WxAppId: 微信公众号appId\n        :type WxAppId: str\n        """
        self.GroupId = None
        self.DistinctFlag = None
        self.IsSendNow = None
        self.SendDate = None
        self.TaskName = None
        self.WxTouchType = None
        self.Title = None
        self.Content = None
        self.NewsId = None
        self.SmallProgramId = None
        self.TemplateId = None
        self.WxAppId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.DistinctFlag = params.get("DistinctFlag")
        self.IsSendNow = params.get("IsSendNow")
        self.SendDate = params.get("SendDate")
        self.TaskName = params.get("TaskName")
        self.WxTouchType = params.get("WxTouchType")
        self.Title = params.get("Title")
        self.Content = params.get("Content")
        self.NewsId = params.get("NewsId")
        self.SmallProgramId = params.get("SmallProgramId")
        self.TemplateId = params.get("TemplateId")
        self.WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendWxTouchTaskResponse(AbstractModel):
    """SendWxTouchTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubProjectInfo(AbstractModel):
    """子项目信息

    """

    def __init__(self):
        """
        :param SubProjectId: 子项目id\n        :type SubProjectId: str\n        :param SubProjectName: 子项目名称\n        :type SubProjectName: str\n        :param SubProjectStatus: 子项目状态\n        :type SubProjectStatus: str\n        """
        self.SubProjectId = None
        self.SubProjectName = None
        self.SubProjectStatus = None


    def _deserialize(self, params):
        self.SubProjectId = params.get("SubProjectId")
        self.SubProjectName = params.get("SubProjectName")
        self.SubProjectStatus = params.get("SubProjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        