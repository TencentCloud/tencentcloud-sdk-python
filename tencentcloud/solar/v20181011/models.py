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
        :param TemplateId: 活动使用模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param ActivityTitle: 活动标题
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityTitle: str
        :param ActivityDesc: 活动描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityDesc: str
        :param ActivityCover: 活动封面地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityCover: str
        :param ActivityType: 活动类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityType: str
        :param ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityId: str
        :param PersonalConfig: 活动模板自定义配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalConfig: str
        """
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
        r"""
        :param UserId: 员工ID
        :type UserId: list of str
        :param OperateType: 渠道状态：checkpass审核通过, checkreject审核拒绝, enableoperate启用, stopoperate停用
        :type OperateType: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CopyActivityChannelRequest(AbstractModel):
    """CopyActivityChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param ActivityId: 活动ID
        :type ActivityId: str
        :param ChannelFrom: 来源渠道ID
        :type ChannelFrom: str
        :param ChannelTo: 目的渠道id
        :type ChannelTo: list of str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectOrg: 项目机构
        :type ProjectOrg: str
        :param ProjectBudget: 项目预算
        :type ProjectBudget: str
        :param ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param ProjectOrgId: 所属部门ID
        :type ProjectOrgId: str
        """
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
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RequestId = params.get("RequestId")


class CreateSubProjectRequest(AbstractModel):
    """CreateSubProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 所属项目id
        :type ProjectId: str
        :param SubProjectName: 子项目名称
        :type SubProjectName: str
        """
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
        r"""
        :param SubProjectId: 子项目id
        :type SubProjectId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubProjectId = params.get("SubProjectId")
        self.RequestId = params.get("RequestId")


class CustomerInfo(AbstractModel):
    """客户档案

    """

    def __init__(self):
        r"""
        :param Activity: 总活跃度
注意：此字段可能返回 null，表示取不到有效值。
        :type Activity: int
        :param AudienceUserId: 客户ID
        :type AudienceUserId: str
        :param Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param City: 最近记录城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param LastActiveTime: 最活跃时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastActiveTime: str
        :param MarkFlag: 是否星标客户
注意：此字段可能返回 null，表示取不到有效值。
        :type MarkFlag: str
        :param MonthActive: 30天活跃度
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthActive: int
        :param MonthRecommend: 30天推荐度
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthRecommend: int
        :param Phone: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param Province: 最近记录省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param RealName: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type RealName: str
        :param RelChannelFlag: 员工标识 0 未关联 1 已关联
注意：此字段可能返回 null，表示取不到有效值。
        :type RelChannelFlag: int
        :param Sex: 性别 1男 2女
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: int
        :param Spread: 传播力（好友数）
注意：此字段可能返回 null，表示取不到有效值。
        :type Spread: int
        :param WeekActive: 7天活跃度
注意：此字段可能返回 null，表示取不到有效值。
        :type WeekActive: int
        :param WeekRecommend: 7天推荐度
注意：此字段可能返回 null，表示取不到有效值。
        :type WeekRecommend: int
        :param WxCity: 微信城市
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCity: str
        :param WxCountry: 微信国家或地区
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCountry: str
        :param WxNickname: 微信呢称
注意：此字段可能返回 null，表示取不到有效值。
        :type WxNickname: str
        :param WxProvince: 微信省份
注意：此字段可能返回 null，表示取不到有效值。
        :type WxProvince: str
        """
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
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomerRequest(AbstractModel):
    """DescribeCustomer请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        """
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
        r"""
        :param AddressList: 地址列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressList: list of str
        :param UserId: 用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param Birthday: 生日
注意：此字段可能返回 null，表示取不到有效值。
        :type Birthday: str
        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Device: 设备
注意：此字段可能返回 null，表示取不到有效值。
        :type Device: str
        :param Industrys: 行业
注意：此字段可能返回 null，表示取不到有效值。
        :type Industrys: list of str
        :param LastActiveTime: 上次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastActiveTime: str
        :param MarkFlag: 是否星标 1是 0否
注意：此字段可能返回 null，表示取不到有效值。
        :type MarkFlag: str
        :param Model: 手机型号
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: str
        :param OpenId: 微信openid
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param PayFeature: 消费特点
注意：此字段可能返回 null，表示取不到有效值。
        :type PayFeature: str
        :param Phone: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param PhoneList: 手机号码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneList: str
        :param Province: 最近记录省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param RealName: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type RealName: str
        :param RelChannelFlag: 员工标识 0：非员工 1：员工
注意：此字段可能返回 null，表示取不到有效值。
        :type RelChannelFlag: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Sex: 性别 1男 2女
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param SourceAudienceVo: 最初来源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAudienceVo: str
        :param SubWechats: 关注公众号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubWechats: list of str
        :param UnionId: 微信unionid
注意：此字段可能返回 null，表示取不到有效值。
        :type UnionId: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param UserTypes: 用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserTypes: list of str
        :param WxCity: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCity: str
        :param WxCountry: 国家
注意：此字段可能返回 null，表示取不到有效值。
        :type WxCountry: str
        :param WxNickname: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type WxNickname: str
        :param WxProvince: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type WxProvince: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param QueryType: 查询类型，0.个人，1负责部门，2.指定部门
        :type QueryType: str
        :param GroupId: 分组ID
        :type GroupId: str
        :param MarkFlag: 是否星级标记 1是 0否
        :type MarkFlag: int
        :param TagIds: 客户标签，多个标签用逗号隔开
        :type TagIds: str
        :param RelChannelFlag: 员工标识筛选，0：非员工，1：员工
        :type RelChannelFlag: str
        :param NeedPhoneFlag: 必须存在手机 1是 0否
        :type NeedPhoneFlag: int
        :param Province: 省份
        :type Province: str
        :param City: 城市
        :type City: str
        :param Sex: 性别 1男 2女
        :type Sex: str
        :param KeyWord: 城市
        :type KeyWord: str
        :param Offset: 查询开始位置
        :type Offset: int
        :param Limit: 每页记录条数
        :type Limit: int
        :param SubProjectId: 子项目ID
        :type SubProjectId: str
        """
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
        r"""
        :param TotalCount: 总记录条数
        :type TotalCount: int
        :param UserList: 数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of CustomerInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
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
        r"""
        :param ProjectId: 项目id
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectBudget: 项目预算
        :type ProjectBudget: float
        :param ProjectOrg: 项目机构
        :type ProjectOrg: str
        :param ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param SubProjectList: 子项目列表
        :type SubProjectList: list of SubProjectInfo
        :param ProjectStatus: 项目状态
        :type ProjectStatus: str
        :param ProjectOrgId: 项目机构Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectOrgId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param SubProjectId: 子项目id
        :type SubProjectId: str
        """
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
        r"""
        :param ProjectStocks: 项目库存列表
        :type ProjectStocks: list of ProjectStock
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param PageNo: 页码
        :type PageNo: int
        :param PageSize: 页面大小
        :type PageSize: int
        :param SearchWord: 过滤规则
        :type SearchWord: str
        :param Filters: 部门范围过滤
        :type Filters: :class:`tencentcloud.solar.v20181011.models.Filters`
        :param ProjectStatus: 项目状态, 0:编辑中 1:运营中 2:已下线 3:已删除 4:审批中
        :type ProjectStatus: int
        """
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
        r"""
        :param ProjectList: 项目列表
        :type ProjectList: list of ProjectInfo
        :param TotalCount: 项目数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param WxAppId: 微信公众号appId
        :type WxAppId: str
        """
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
        r"""
        :param TotalCount: 记录条数
        :type TotalCount: int
        :param TmplList: 模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TmplList: list of ResourceTemplateHeader
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param SubProjectId: 子项目id
        :type SubProjectId: str
        """
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
        r"""
        :param ProductInfo: 作品信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductInfo: :class:`tencentcloud.solar.v20181011.models.ProductInfo`
        :param ActivityInfo: 活动信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityInfo: :class:`tencentcloud.solar.v20181011.models.ActivityInfo`
        :param ShareTitle: 分享标题
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareTitle: str
        :param ShareDesc: 分享描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareDesc: str
        :param ShareImg: 分享图标
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareImg: str
        :param HasStrategy: 是否已创建策略
注意：此字段可能返回 null，表示取不到有效值。
        :type HasStrategy: int
        :param SubProjectStatus: 子项目状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProjectStatus: str
        :param ShareAppId: 分享公众号的appId
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareAppId: str
        :param ShareWsId: 分享公众号的wsId
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareWsId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param FlowId: 工单ID
        :type FlowId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filters(AbstractModel):
    """可见范围过滤参数

    """

    def __init__(self):
        r"""
        :param Type: 过滤类型, 0: 默认(可见部门+自创) 1: 自创 2: 指定部门(部门在可见范围内)
        :type Type: int
        :param DeptIds: 指定部门Id, 类型2使用
        :type DeptIds: list of str
        :param UserIds: 用户Id列表
        :type UserIds: list of str
        """
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
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectBudget: 项目预算
        :type ProjectBudget: str
        :param ProjectOrg: 项目机构
        :type ProjectOrg: str
        :param ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param ProjectOrgId: 项目机构Id
        :type ProjectOrgId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OffLineProjectRequest(AbstractModel):
    """OffLineProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProductInfo(AbstractModel):
    """内容页结构

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param ProductTitle: 模板主题
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductTitle: str
        :param ProductDesc: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductDesc: str
        :param ProductCover: 模板封面地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCover: str
        :param ProductId: 内容作品id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param ProductUrl: 作品预览链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductUrl: str
        :param ProductName: 作品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        """
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
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectOrg: 项目所属机构
        :type ProjectOrg: str
        :param ProjectBudget: 项目预算
        :type ProjectBudget: float
        :param ProjectStatus: 项目状态
        :type ProjectStatus: str
        :param CreateTime: 项目创建时间
        :type CreateTime: str
        :param ProjectIntroduction: 项目简介
        :type ProjectIntroduction: str
        :param ProjectOrgId: 项目所属机构Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectOrgId: str
        """
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
        r"""
        :param PrizeId: 奖品id
        :type PrizeId: str
        :param PrizeBat: 奖品批次
        :type PrizeBat: int
        :param PrizeName: 奖品名称
        :type PrizeName: str
        :param UsedStock: 已分配奖品数量
        :type UsedStock: int
        :param RemainStock: 该奖品剩余库存数量
        :type RemainStock: int
        :param PoolIdx: 奖品所在奖池index
        :type PoolIdx: int
        :param PoolName: 奖品所在奖池名称
        :type PoolName: str
        """
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
        r"""
        :param SubProjectId: 项目id
        :type SubProjectId: str
        :param PrizeId: 奖品id
        :type PrizeId: str
        :param PrizeNum: 奖品数量
        :type PrizeNum: int
        :param PoolIndex: 奖池索引
        :type PoolIndex: int
        :param PoolName: 奖池名称
        :type PoolName: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceTemplateHeader(AbstractModel):
    """素材模板消息标题的样例列表

    """

    def __init__(self):
        r"""
        :param Content: 模板预览区内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param Example: 模板预览示例
注意：此字段可能返回 null，表示取不到有效值。
        :type Example: str
        :param KeyArray: 模板预览区域键数组
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyArray: str
        :param TemplateId: 模板id
        :type TemplateId: str
        :param Title: 模板标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        """
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
        r"""
        :param GroupId: 客户分组ID
        :type GroupId: str
        :param DistinctFlag: 去除今日已发送的客户
        :type DistinctFlag: bool
        :param IsSendNow: 是否立马发送
        :type IsSendNow: bool
        :param SendDate: 发送时间，一般为0
        :type SendDate: int
        :param TaskName: 任务名称
        :type TaskName: str
        :param WxTouchType: 微信触达类型，text, news, smallapp, tmplmsg
        :type WxTouchType: str
        :param Title: 标题
        :type Title: str
        :param Content: 文本内容
        :type Content: str
        :param NewsId: 图文素材ID
        :type NewsId: str
        :param SmallProgramId: 小程序卡片ID
        :type SmallProgramId: str
        :param TemplateId: 模板消息ID
        :type TemplateId: str
        :param WxAppId: 微信公众号appId
        :type WxAppId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubProjectInfo(AbstractModel):
    """子项目信息

    """

    def __init__(self):
        r"""
        :param SubProjectId: 子项目id
        :type SubProjectId: str
        :param SubProjectName: 子项目名称
        :type SubProjectName: str
        :param SubProjectStatus: 子项目状态
        :type SubProjectStatus: str
        """
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
        