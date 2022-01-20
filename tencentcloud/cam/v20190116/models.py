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


class AccessKey(AbstractModel):
    """访问密钥列表

    """

    def __init__(self):
        r"""
        :param AccessKeyId: 访问密钥标识
        :type AccessKeyId: str
        :param Status: 密钥状态，激活（Active）或未激活（Inactive）
        :type Status: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.AccessKeyId = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserRequest(AbstractModel):
    """AddUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 子用户用户名
        :type Name: str
        :param Remark: 子用户备注
        :type Remark: str
        :param ConsoleLogin: 子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :type ConsoleLogin: int
        :param UseApi: 是否生成子用户密钥。传0不生成子用户密钥，传1生成子用户密钥。
        :type UseApi: int
        :param Password: 子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。
        :type Password: str
        :param NeedResetPassword: 子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。
        :type NeedResetPassword: int
        :param PhoneNum: 手机号
        :type PhoneNum: str
        :param CountryCode: 区号
        :type CountryCode: str
        :param Email: 邮箱
        :type Email: str
        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.UseApi = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.UseApi = params.get("UseApi")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserResponse(AbstractModel):
    """AddUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param Uin: 子用户 UIN
        :type Uin: int
        :param Name: 子用户用户名
        :type Name: str
        :param Password: 如果输入参数组合为自动生成随机密码，则返回生成的密码
        :type Password: str
        :param SecretId: 子用户密钥 ID
        :type SecretId: str
        :param SecretKey: 子用户密钥 Key
        :type SecretKey: str
        :param Uid: 子用户 UID
        :type Uid: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Password = None
        self.SecretId = None
        self.SecretKey = None
        self.Uid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Uid = params.get("Uid")
        self.RequestId = params.get("RequestId")


class AddUserToGroupRequest(AbstractModel):
    """AddUserToGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 添加的子用户 UIN/UID 和用户组 ID 关联关系
        :type Info: list of GroupIdOfUidInfo
        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToGroupResponse(AbstractModel):
    """AddUserToGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachEntityOfPolicy(AbstractModel):
    """策略关联的实体信息

    """

    def __init__(self):
        r"""
        :param Id: 实体ID
        :type Id: str
        :param Name: 实体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Uin: 实体Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: int
        :param RelatedType: 关联类型。1 用户关联 ； 2 用户组关联
        :type RelatedType: int
        :param AttachmentTime: 策略关联时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachmentTime: str
        """
        self.Id = None
        self.Name = None
        self.Uin = None
        self.RelatedType = None
        self.AttachmentTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Uin = params.get("Uin")
        self.RelatedType = params.get("RelatedType")
        self.AttachmentTime = params.get("AttachmentTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param AttachGroupId: 用户组 id
        :type AttachGroupId: int
        """
        self.PolicyId = None
        self.AttachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachGroupId = params.get("AttachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyResponse(AbstractModel):
    """AttachGroupPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachPolicyInfo(AbstractModel):
    """关联策略信息

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略id
        :type PolicyId: int
        :param PolicyName: 策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param CreateMode: 创建来源，1 通过控制台创建, 2 通过策略语法创建。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateMode: int
        :param PolicyType: 取值为user和QCS
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param Remark: 策略备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param OperateOwnerUin: 策略关联操作者主帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateOwnerUin: str
        :param OperateUin: 策略关联操作者ID，如果UinType为0表示子帐号Uin，如果UinType为1表示角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUin: str
        :param OperateUinType: UinType为0表示OperateUin字段是子帐号Uin，如果UinType为1表示OperateUin字段是角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUinType: int
        :param Deactived: 是否已下线
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param DeactivedDetail: 已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.CreateMode = None
        self.PolicyType = None
        self.Remark = None
        self.OperateOwnerUin = None
        self.OperateUin = None
        self.OperateUinType = None
        self.Deactived = None
        self.DeactivedDetail = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.CreateMode = params.get("CreateMode")
        self.PolicyType = params.get("PolicyType")
        self.Remark = params.get("Remark")
        self.OperateOwnerUin = params.get("OperateOwnerUin")
        self.OperateUin = params.get("OperateUin")
        self.OperateUinType = params.get("OperateUinType")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyRequest(AbstractModel):
    """AttachRolePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID，入参PolicyId与PolicyName二选一
        :type PolicyId: int
        :param AttachRoleId: 角色ID，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :type AttachRoleId: str
        :param AttachRoleName: 角色名称，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :type AttachRoleName: str
        :param PolicyName: 策略名，入参PolicyId与PolicyName二选一
        :type PolicyName: str
        """
        self.PolicyId = None
        self.AttachRoleId = None
        self.AttachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachRoleId = params.get("AttachRoleId")
        self.AttachRoleName = params.get("AttachRoleName")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyResponse(AbstractModel):
    """AttachRolePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param AttachUin: 子账号 uin
        :type AttachUin: int
        """
        self.PolicyId = None
        self.AttachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachUin = params.get("AttachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachedPolicyOfRole(AbstractModel):
    """角色关联的策略信息

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param PolicyName: 策略名称
        :type PolicyName: str
        :param AddTime: 绑定时间
        :type AddTime: str
        :param PolicyType: 策略类型，User表示自定义策略，QCS表示预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param CreateMode: 策略创建方式，1表示按产品功能或项目权限创建，其他表示按策略语法创建
        :type CreateMode: int
        :param Deactived: 是否已下线(0:否 1:是)
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param DeactivedDetail: 已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        :param Description: 策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.PolicyType = None
        self.CreateMode = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.PolicyType = params.get("PolicyType")
        self.CreateMode = params.get("CreateMode")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicy(AbstractModel):
    """用户关联的策略详情

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Description: 策略描述
        :type Description: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param StrategyType: 策略类型(1表示自定义策略，2表示预设策略)
        :type StrategyType: str
        :param CreateMode: 创建模式(1表示按产品或项目权限创建的策略，其他表示策略语法创建的策略)
        :type CreateMode: str
        :param Groups: 随组关联信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of AttachedUserPolicyGroupInfo
        :param Deactived: 是否已下线(0:否 1:是)
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param DeactivedDetail: 已下线的产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.AddTime = None
        self.StrategyType = None
        self.CreateMode = None
        self.Groups = None
        self.Deactived = None
        self.DeactivedDetail = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.StrategyType = params.get("StrategyType")
        self.CreateMode = params.get("CreateMode")
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = AttachedUserPolicyGroupInfo()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicyGroupInfo(AbstractModel):
    """用户关联策略(随组关联)信息

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: int
        :param GroupName: 分组名称
        :type GroupName: str
        """
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenRequest(AbstractModel):
    """ConsumeCustomMFAToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param MFAToken: 自定义多因子验证Token
        :type MFAToken: str
        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenResponse(AbstractModel):
    """ConsumeCustomMFAToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupName: 用户组名
        :type GroupName: str
        :param Remark: 用户组描述
        :type Remark: str
        """
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreatePolicyRequest(AbstractModel):
    """CreatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyName: 策略名
        :type PolicyName: str
        :param PolicyDocument: 策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :type PolicyDocument: str
        :param Description: 策略描述
        :type Description: str
        """
        self.PolicyName = None
        self.PolicyDocument = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyResponse(AbstractModel):
    """CreatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 新增策略ID
        :type PolicyId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreatePolicyVersionRequest(AbstractModel):
    """CreatePolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param PolicyDocument: 策略文本信息
        :type PolicyDocument: str
        :param SetAsDefault: 是否设置为当前策略的版本
        :type SetAsDefault: bool
        """
        self.PolicyId = None
        self.PolicyDocument = None
        self.SetAsDefault = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyDocument = params.get("PolicyDocument")
        self.SetAsDefault = params.get("SetAsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyVersionResponse(AbstractModel):
    """CreatePolicyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param VersionId: 策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称
        :type RoleName: str
        :param PolicyDocument: 策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :type PolicyDocument: str
        :param Description: 角色描述
        :type Description: str
        :param ConsoleLogin: 是否允许登录 1 为允许 0 为不允许
        :type ConsoleLogin: int
        :param SessionDuration: 申请角色临时密钥的最长有效期限制(范围：0~43200)
        :type SessionDuration: int
        """
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.ConsoleLogin = None
        self.SessionDuration = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.SessionDuration = params.get("SessionDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoleId: 角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class CreateSAMLProviderRequest(AbstractModel):
    """CreateSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: SAML身份提供商名称
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param SAMLMetadataDocument: SAML身份提供商Base64编码的元数据文档
        :type SAMLMetadataDocument: str
        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSAMLProviderResponse(AbstractModel):
    """CreateSAMLProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProviderArn: SAML身份提供商资源描述符
        :type ProviderArn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProviderArn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProviderArn = params.get("ProviderArn")
        self.RequestId = params.get("RequestId")


class CreateServiceLinkedRoleRequest(AbstractModel):
    """CreateServiceLinkedRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param QCSServiceName: 授权服务，附加了此角色的腾讯云服务主体。
        :type QCSServiceName: list of str
        :param CustomSuffix: 自定义后缀，根据您提供的字符串，与服务提供的前缀组合在一起以形成完整的角色名称。
        :type CustomSuffix: str
        :param Description: 角色说明。
        :type Description: str
        """
        self.QCSServiceName = None
        self.CustomSuffix = None
        self.Description = None


    def _deserialize(self, params):
        self.QCSServiceName = params.get("QCSServiceName")
        self.CustomSuffix = params.get("CustomSuffix")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceLinkedRoleResponse(AbstractModel):
    """CreateServiceLinkedRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoleId: 角色ID
        :type RoleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class CreateUserSAMLConfigRequest(AbstractModel):
    """CreateUserSAMLConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param SAMLMetadataDocument: SAML元数据文档，需要base64 encode
        :type SAMLMetadataDocument: str
        """
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSAMLConfigResponse(AbstractModel):
    """CreateUserSAMLConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyRequest(AbstractModel):
    """DeletePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 数组，数组成员是策略 id，支持批量删除策略
        :type PolicyId: list of int non-negative
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyResponse(AbstractModel):
    """DeletePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyVersionRequest(AbstractModel):
    """DeletePolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param VersionId: 策略版本号
        :type VersionId: list of int non-negative
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyVersionResponse(AbstractModel):
    """DeletePolicyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRolePermissionsBoundaryRequest(AbstractModel):
    """DeleteRolePermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleId: 角色ID（与角色名至少填一个）
        :type RoleId: str
        :param RoleName: 角色名（与角色ID至少填一个）
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolePermissionsBoundaryResponse(AbstractModel):
    """DeleteRolePermissionsBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoleRequest(AbstractModel):
    """DeleteRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleId: 角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param RoleName: 角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleResponse(AbstractModel):
    """DeleteRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSAMLProviderRequest(AbstractModel):
    """DeleteSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: SAML身份提供商名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSAMLProviderResponse(AbstractModel):
    """DeleteSAMLProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceLinkedRoleRequest(AbstractModel):
    """DeleteServiceLinkedRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleName: 要删除的服务相关角色的名称。
        :type RoleName: str
        """
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceLinkedRoleResponse(AbstractModel):
    """DeleteServiceLinkedRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeletionTaskId: 删除任务ID，可用于检查删除服务相关角色状态。
        :type DeletionTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeletionTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")
        self.RequestId = params.get("RequestId")


class DeleteUserPermissionsBoundaryRequest(AbstractModel):
    """DeleteUserPermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 子账号Uin
        :type TargetUin: int
        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserPermissionsBoundaryResponse(AbstractModel):
    """DeleteUserPermissionsBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 子用户用户名
        :type Name: str
        :param Force: 是否强制删除该子用户，默认入参为0。0：若该用户存在未删除API密钥，则不删除用户；1：若该用户存在未删除API密钥，则先删除密钥后删除用户。删除密钥需要您拥有cam:DeleteApiKey权限，您将可以删除该用户下启用或禁用状态的所有密钥，无权限则删除密钥和用户失败
        :type Force: int
        """
        self.Name = None
        self.Force = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    """DescribeRoleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Page: 页码，从1开始
        :type Page: int
        :param Rp: 每页行数，不能大于200
        :type Rp: int
        """
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListResponse(AbstractModel):
    """DescribeRoleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 角色详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of RoleInfo
        :param TotalNum: 角色总数
        :type TotalNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = RoleInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagCollRequest(AbstractModel):
    """DescribeSafeAuthFlagColl请求参数结构体

    """

    def __init__(self):
        r"""
        :param SubUin: 子账号
        :type SubUin: int
        """
        self.SubUin = None


    def _deserialize(self, params):
        self.SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSafeAuthFlagCollResponse(AbstractModel):
    """DescribeSafeAuthFlagColl返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param ActionFlag: 敏感操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param OffsiteFlag: 异地登录保护设置
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagIntlRequest(AbstractModel):
    """DescribeSafeAuthFlagIntl请求参数结构体

    """


class DescribeSafeAuthFlagIntlResponse(AbstractModel):
    """DescribeSafeAuthFlagIntl返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param ActionFlag: 敏感操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param OffsiteFlag: 异地登录保护设置
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlagIntl()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlagIntl()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagRequest(AbstractModel):
    """DescribeSafeAuthFlag请求参数结构体

    """


class DescribeSafeAuthFlagResponse(AbstractModel):
    """DescribeSafeAuthFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param ActionFlag: 敏感操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param OffsiteFlag: 异地登录保护设置
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSubAccountsRequest(AbstractModel):
    """DescribeSubAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param FilterSubAccountUin: 子用户UIN列表，最多支持50个UIN
        :type FilterSubAccountUin: list of int non-negative
        """
        self.FilterSubAccountUin = None


    def _deserialize(self, params):
        self.FilterSubAccountUin = params.get("FilterSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubAccountsResponse(AbstractModel):
    """DescribeSubAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubAccounts: 子用户列表
        :type SubAccounts: list of SubAccountUser
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubAccounts") is not None:
            self.SubAccounts = []
            for item in params.get("SubAccounts"):
                obj = SubAccountUser()
                obj._deserialize(item)
                self.SubAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserSAMLConfigRequest(AbstractModel):
    """DescribeUserSAMLConfig请求参数结构体

    """


class DescribeUserSAMLConfigResponse(AbstractModel):
    """DescribeUserSAMLConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param SAMLMetadata: SAML元数据文档
        :type SAMLMetadata: str
        :param Status: 状态：0:未设置，1:已开启，2:已禁用
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SAMLMetadata = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SAMLMetadata = params.get("SAMLMetadata")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param DetachGroupId: 用户组 id
        :type DetachGroupId: int
        """
        self.PolicyId = None
        self.DetachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachGroupId = params.get("DetachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachGroupPolicyResponse(AbstractModel):
    """DetachGroupPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachRolePolicyRequest(AbstractModel):
    """DetachRolePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID，入参PolicyId与PolicyName二选一
        :type PolicyId: int
        :param DetachRoleId: 角色ID，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :type DetachRoleId: str
        :param DetachRoleName: 角色名称，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一
        :type DetachRoleName: str
        :param PolicyName: 策略名，入参PolicyId与PolicyName二选一
        :type PolicyName: str
        """
        self.PolicyId = None
        self.DetachRoleId = None
        self.DetachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachRoleId = params.get("DetachRoleId")
        self.DetachRoleName = params.get("DetachRoleName")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachRolePolicyResponse(AbstractModel):
    """DetachRolePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param DetachUin: 子账号 uin
        :type DetachUin: int
        """
        self.PolicyId = None
        self.DetachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachUin = params.get("DetachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetAccountSummaryRequest(AbstractModel):
    """GetAccountSummary请求参数结构体

    """


class GetAccountSummaryResponse(AbstractModel):
    """GetAccountSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param Policies: 策略数
        :type Policies: int
        :param Roles: 角色数
        :type Roles: int
        :param Idps: 身份提供商数
        :type Idps: int
        :param User: 子账户数
        :type User: int
        :param Group: 分组数
        :type Group: int
        :param Member: 分组用户总数
        :type Member: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Policies = None
        self.Roles = None
        self.Idps = None
        self.User = None
        self.Group = None
        self.Member = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Policies = params.get("Policies")
        self.Roles = params.get("Roles")
        self.Idps = params.get("Idps")
        self.User = params.get("User")
        self.Group = params.get("Group")
        self.Member = params.get("Member")
        self.RequestId = params.get("RequestId")


class GetCustomMFATokenInfoRequest(AbstractModel):
    """GetCustomMFATokenInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param MFAToken: 自定义多因子验证Token
        :type MFAToken: str
        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomMFATokenInfoResponse(AbstractModel):
    """GetCustomMFATokenInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Uin: 自定义多因子验证Token对应的帐号Id
        :type Uin: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    """GetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupResponse(AbstractModel):
    """GetGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID
        :type GroupId: int
        :param GroupName: 用户组名称
        :type GroupName: str
        :param GroupNum: 用户组成员数量
        :type GroupNum: int
        :param Remark: 用户组描述
        :type Remark: str
        :param CreateTime: 用户组创建时间
        :type CreateTime: str
        :param UserInfo: 用户组成员信息
        :type UserInfo: list of GroupMemberInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupNum = None
        self.Remark = None
        self.CreateTime = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupNum = params.get("GroupNum")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class GetPolicyRequest(AbstractModel):
    """GetPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略Id
        :type PolicyId: int
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyResponse(AbstractModel):
    """GetPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param Description: 策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Type: 1 表示自定义策略，2 表示预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param AddTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param UpdateTime: 最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param PolicyDocument: 策略文档
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        :param PresetAlias: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type PresetAlias: str
        :param IsServiceLinkedRolePolicy: 是否服务相关策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsServiceLinkedRolePolicy: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyName = None
        self.Description = None
        self.Type = None
        self.AddTime = None
        self.UpdateTime = None
        self.PolicyDocument = None
        self.PresetAlias = None
        self.IsServiceLinkedRolePolicy = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.PolicyDocument = params.get("PolicyDocument")
        self.PresetAlias = params.get("PresetAlias")
        self.IsServiceLinkedRolePolicy = params.get("IsServiceLinkedRolePolicy")
        self.RequestId = params.get("RequestId")


class GetPolicyVersionRequest(AbstractModel):
    """GetPolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param VersionId: 策略版本号，可由ListPolicyVersions获取
        :type VersionId: int
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyVersionResponse(AbstractModel):
    """GetPolicyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyVersion: 策略版本详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyVersion: :class:`tencentcloud.cam.v20190116.models.PolicyVersionDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyVersion") is not None:
            self.PolicyVersion = PolicyVersionDetail()
            self.PolicyVersion._deserialize(params.get("PolicyVersion"))
        self.RequestId = params.get("RequestId")


class GetRolePermissionBoundaryRequest(AbstractModel):
    """GetRolePermissionBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleId: 角色ID
        :type RoleId: str
        """
        self.RoleId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRolePermissionBoundaryResponse(AbstractModel):
    """GetRolePermissionBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param PolicyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param PolicyDocument: 策略语法
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        :param PolicyType: 策略类型：1.自定义策略，2.预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: int
        :param CreateMode: 创建方式：1.按产品功能或项目权限创建，2.按策略语法创建，3.按策略生成器创建，4.按标签授权创建，5.按权限边界规则创建
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateMode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.PolicyDocument = None
        self.PolicyType = None
        self.CreateMode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.PolicyType = params.get("PolicyType")
        self.CreateMode = params.get("CreateMode")
        self.RequestId = params.get("RequestId")


class GetRoleRequest(AbstractModel):
    """GetRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleId: 角色 ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param RoleName: 角色名，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoleResponse(AbstractModel):
    """GetRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoleInfo: 角色详情
        :type RoleInfo: :class:`tencentcloud.cam.v20190116.models.RoleInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoleInfo") is not None:
            self.RoleInfo = RoleInfo()
            self.RoleInfo._deserialize(params.get("RoleInfo"))
        self.RequestId = params.get("RequestId")


class GetSAMLProviderRequest(AbstractModel):
    """GetSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: SAML身份提供商名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSAMLProviderResponse(AbstractModel):
    """GetSAMLProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: SAML身份提供商名称
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param CreateTime: SAML身份提供商创建时间
        :type CreateTime: str
        :param ModifyTime: SAML身份提供商上次修改时间
        :type ModifyTime: str
        :param SAMLMetadata: SAML身份提供商元数据文档
        :type SAMLMetadata: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None
        self.SAMLMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.SAMLMetadata = params.get("SAMLMetadata")
        self.RequestId = params.get("RequestId")


class GetSecurityLastUsedRequest(AbstractModel):
    """GetSecurityLastUsed请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecretIdList: 查询密钥ID列表
        :type SecretIdList: list of str
        """
        self.SecretIdList = None


    def _deserialize(self, params):
        self.SecretIdList = params.get("SecretIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecurityLastUsedResponse(AbstractModel):
    """GetSecurityLastUsed返回参数结构体

    """

    def __init__(self):
        r"""
        :param SecretIdLastUsedRows: 密钥ID最近访问列表
        :type SecretIdLastUsedRows: list of SecretIdLastUsed
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretIdLastUsedRows = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecretIdLastUsedRows") is not None:
            self.SecretIdLastUsedRows = []
            for item in params.get("SecretIdLastUsedRows"):
                obj = SecretIdLastUsed()
                obj._deserialize(item)
                self.SecretIdLastUsedRows.append(obj)
        self.RequestId = params.get("RequestId")


class GetServiceLinkedRoleDeletionStatusRequest(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeletionTaskId: 删除任务ID
        :type DeletionTaskId: str
        """
        self.DeletionTaskId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetServiceLinkedRoleDeletionStatusResponse(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 状态：NOT_STARTED，IN_PROGRESS，SUCCEEDED，FAILED
        :type Status: str
        :param Reason: 失败原因
        :type Reason: str
        :param ServiceType: 服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param ServiceName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Reason = None
        self.ServiceType = None
        self.ServiceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.ServiceType = params.get("ServiceType")
        self.ServiceName = params.get("ServiceName")
        self.RequestId = params.get("RequestId")


class GetUserPermissionBoundaryRequest(AbstractModel):
    """GetUserPermissionBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 子账号Uin
        :type TargetUin: int
        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserPermissionBoundaryResponse(AbstractModel):
    """GetUserPermissionBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param PolicyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param PolicyDocument: 策略语法
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        :param PolicyType: 策略类型：1.自定义策略，2.预设策略
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: int
        :param CreateMode: 创建方式：1.按产品功能或项目权限创建，2.按策略语法创建，3.按策略生成器创建，4.按标签授权创建，5.按权限边界规则创建
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateMode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.PolicyDocument = None
        self.PolicyType = None
        self.CreateMode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.PolicyType = params.get("PolicyType")
        self.CreateMode = params.get("CreateMode")
        self.RequestId = params.get("RequestId")


class GetUserRequest(AbstractModel):
    """GetUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 子用户用户名
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserResponse(AbstractModel):
    """GetUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param Uin: 子用户用户 UIN
        :type Uin: int
        :param Name: 子用户用户名
        :type Name: str
        :param Uid: 子用户 UID
        :type Uid: int
        :param Remark: 子用户备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param ConsoleLogin: 子用户能否登录控制台 0-无法登录控制台，1-可以登录控制台
        :type ConsoleLogin: int
        :param PhoneNum: 手机号
        :type PhoneNum: str
        :param CountryCode: 区号
        :type CountryCode: str
        :param Email: 邮箱
        :type Email: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.RequestId = params.get("RequestId")


class GroupIdOfUidInfo(AbstractModel):
    """子用户和用户组关联信息

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID
        :type GroupId: int
        :param Uid: 子用户 UID
        :type Uid: int
        :param Uin: 子用户 Uin，Uid和Uin至少有一个必填
        :type Uin: int
        """
        self.GroupId = None
        self.Uid = None
        self.Uin = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Uid = params.get("Uid")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """用户组信息

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID。
        :type GroupId: int
        :param GroupName: 用户组名称。
        :type GroupName: str
        :param CreateTime: 用户组创建时间。
        :type CreateTime: str
        :param Remark: 用户组描述。
        :type Remark: str
        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupMemberInfo(AbstractModel):
    """用户组用户信息

    """

    def __init__(self):
        r"""
        :param Uid: 子用户 Uid。
        :type Uid: int
        :param Uin: 子用户 Uin。
        :type Uin: int
        :param Name: 子用户名称。
        :type Name: str
        :param PhoneNum: 手机号。
        :type PhoneNum: str
        :param CountryCode: 手机区域代码。
        :type CountryCode: str
        :param PhoneFlag: 是否已验证手机。0-未验证  1-验证
        :type PhoneFlag: int
        :param Email: 邮箱地址。
        :type Email: str
        :param EmailFlag: 是否已验证邮箱。0-未验证  1-验证
        :type EmailFlag: int
        :param UserType: 用户类型。1-全局协作者 2-项目协作者 3-消息接收者
        :type UserType: int
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param IsReceiverOwner: 是否为主消息接收人。0-否 1-是
        :type IsReceiverOwner: int
        """
        self.Uid = None
        self.Uin = None
        self.Name = None
        self.PhoneNum = None
        self.CountryCode = None
        self.PhoneFlag = None
        self.Email = None
        self.EmailFlag = None
        self.UserType = None
        self.CreateTime = None
        self.IsReceiverOwner = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.PhoneFlag = params.get("PhoneFlag")
        self.Email = params.get("Email")
        self.EmailFlag = params.get("EmailFlag")
        self.UserType = params.get("UserType")
        self.CreateTime = params.get("CreateTime")
        self.IsReceiverOwner = params.get("IsReceiverOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysRequest(AbstractModel):
    """ListAccessKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 指定用户Uin，不填默认列出当前用户访问密钥
        :type TargetUin: int
        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysResponse(AbstractModel):
    """ListAccessKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccessKeys: 访问密钥列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKeys: list of AccessKey
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessKeys") is not None:
            self.AccessKeys = []
            for item in params.get("AccessKeys"):
                obj = AccessKey()
                obj._deserialize(item)
                self.AccessKeys.append(obj)
        self.RequestId = params.get("RequestId")


class ListAttachedGroupPoliciesRequest(AbstractModel):
    """ListAttachedGroupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetGroupId: 用户组ID
        :type TargetGroupId: int
        :param Page: 页码，默认值是 1，从 1 开始
        :type Page: int
        :param Rp: 每页大小，默认值是 20
        :type Rp: int
        :param Keyword: 搜索关键字
        :type Keyword: str
        """
        self.TargetGroupId = None
        self.Page = None
        self.Rp = None
        self.Keyword = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedGroupPoliciesResponse(AbstractModel):
    """ListAttachedGroupPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 策略总数
        :type TotalNum: int
        :param List: 策略列表
        :type List: list of AttachPolicyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListAttachedRolePoliciesRequest(AbstractModel):
    """ListAttachedRolePolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param Page: 页码，从 1 开始
        :type Page: int
        :param Rp: 每页行数，不能大于200
        :type Rp: int
        :param RoleId: 角色 ID。用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param RoleName: 角色名。用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        :param PolicyType: 按策略类型过滤，User表示仅查询自定义策略，QCS表示仅查询预设策略
        :type PolicyType: str
        :param Keyword: 搜索关键字
        :type Keyword: str
        """
        self.Page = None
        self.Rp = None
        self.RoleId = None
        self.RoleName = None
        self.PolicyType = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyType = params.get("PolicyType")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedRolePoliciesResponse(AbstractModel):
    """ListAttachedRolePolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 角色关联的策略列表
        :type List: list of AttachedPolicyOfRole
        :param TotalNum: 角色关联的策略总数
        :type TotalNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachedPolicyOfRole()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ListAttachedUserAllPoliciesRequest(AbstractModel):
    """ListAttachedUserAllPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 目标用户ID
        :type TargetUin: int
        :param Rp: 每页数量，必须大于 0 且小于或等于 200
        :type Rp: int
        :param Page: 页码，从 1开始，不能大于 200
        :type Page: int
        :param AttachType: 0:返回直接关联和随组关联策略，1:只返回直接关联策略，2:只返回随组关联策略
        :type AttachType: int
        :param StrategyType: 策略类型
        :type StrategyType: int
        :param Keyword: 搜索关键字
        :type Keyword: str
        """
        self.TargetUin = None
        self.Rp = None
        self.Page = None
        self.AttachType = None
        self.StrategyType = None
        self.Keyword = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.AttachType = params.get("AttachType")
        self.StrategyType = params.get("StrategyType")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserAllPoliciesResponse(AbstractModel):
    """ListAttachedUserAllPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyList: 策略列表数据
        :type PolicyList: list of AttachedUserPolicy
        :param TotalNum: 策略总数
        :type TotalNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyList = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyList") is not None:
            self.PolicyList = []
            for item in params.get("PolicyList"):
                obj = AttachedUserPolicy()
                obj._deserialize(item)
                self.PolicyList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 子账号 uin
        :type TargetUin: int
        :param Page: 页码，默认值是 1，从 1 开始
        :type Page: int
        :param Rp: 每页大小，默认值是 20
        :type Rp: int
        """
        self.TargetUin = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserPoliciesResponse(AbstractModel):
    """ListAttachedUserPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 策略总数
        :type TotalNum: int
        :param List: 策略列表
        :type List: list of AttachPolicyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListCollaboratorsRequest(AbstractModel):
    """ListCollaborators请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页条数，缺省为20
        :type Limit: int
        :param Offset: 分页起始值，缺省为0
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCollaboratorsResponse(AbstractModel):
    """ListCollaborators返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 总数
        :type TotalNum: int
        :param Data: 协作者信息
        :type Data: list of SubAccountInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param Page: 页码，默认值是 1，从 1 开始
        :type Page: int
        :param Rp: 每页大小，默认值是 20
        :type Rp: int
        :param EntityFilter: 可取值 'All'、'User'、'Group' 和 'Role'，'All' 表示获取所有实体类型，'User' 表示只获取子账号，'Group' 表示只获取用户组，'Role' 表示只获取角色，默认取 'All'
        :type EntityFilter: str
        """
        self.PolicyId = None
        self.Page = None
        self.Rp = None
        self.EntityFilter = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.EntityFilter = params.get("EntityFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEntitiesForPolicyResponse(AbstractModel):
    """ListEntitiesForPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 实体总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param List: 实体列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of AttachEntityOfPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachEntityOfPolicy()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListGrantServiceAccessActionNode(AbstractModel):
    """ListGrantServiceAccessAction节点

    """

    def __init__(self):
        r"""
        :param Name: 接口名
        :type Name: str
        :param Description: 接口描述
        :type Description: str
        """
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGrantServiceAccessNode(AbstractModel):
    """用于ListPoliciesGrantingServiceAccess接口的List节点

    """

    def __init__(self):
        r"""
        :param Service: 服务
        :type Service: :class:`tencentcloud.cam.v20190116.models.ListGrantServiceAccessService`
        :param Action: 接口信息
        :type Action: list of ListGrantServiceAccessActionNode
        :param Policy: 授权的策略
        :type Policy: list of ListGrantServiceAccessPolicy
        """
        self.Service = None
        self.Action = None
        self.Policy = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = ListGrantServiceAccessService()
            self.Service._deserialize(params.get("Service"))
        if params.get("Action") is not None:
            self.Action = []
            for item in params.get("Action"):
                obj = ListGrantServiceAccessActionNode()
                obj._deserialize(item)
                self.Action.append(obj)
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = ListGrantServiceAccessPolicy()
                obj._deserialize(item)
                self.Policy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGrantServiceAccessPolicy(AbstractModel):
    """用于ListPoliciesGrantingServiceAccess接口的Policy节点

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param PolicyName: 策略名
        :type PolicyName: str
        :param PolicyType: 策略类型: Custom自定义策略，Presetting预设策略
        :type PolicyType: str
        :param PolicyDescription: 策略描述
        :type PolicyDescription: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.PolicyType = None
        self.PolicyDescription = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.PolicyType = params.get("PolicyType")
        self.PolicyDescription = params.get("PolicyDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGrantServiceAccessService(AbstractModel):
    """用于ListPoliciesGrantingServiceAccess接口的Service节点

    """

    def __init__(self):
        r"""
        :param ServiceType: 服务
        :type ServiceType: str
        :param ServiceName: 服务名
        :type ServiceName: str
        """
        self.ServiceType = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uid: 子用户 UID
        :type Uid: int
        :param Rp: 每页数量。默认为20。
        :type Rp: int
        :param Page: 页码。默认为1。
        :type Page: int
        :param SubUin: 子账号UIN
        :type SubUin: int
        """
        self.Uid = None
        self.Rp = None
        self.Page = None
        self.SubUin = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsForUserResponse(AbstractModel):
    """ListGroupsForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 子用户加入的用户组总数
        :type TotalNum: int
        :param GroupInfo: 用户组信息
        :type GroupInfo: list of GroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListGroupsRequest(AbstractModel):
    """ListGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Page: 页码。默认为1。
        :type Page: int
        :param Rp: 每页数量。默认为20。
        :type Rp: int
        :param Keyword: 按用户组名称匹配。
        :type Keyword: str
        """
        self.Page = None
        self.Rp = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsResponse(AbstractModel):
    """ListGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 用户组总数。
        :type TotalNum: int
        :param GroupInfo: 用户组数组信息。
        :type GroupInfo: list of GroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListPoliciesGrantingServiceAccessRequest(AbstractModel):
    """ListPoliciesGrantingServiceAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 子账号uin，与RoleId、GroupId三选一必传
        :type TargetUin: int
        :param RoleId: 角色ID，与TargetUin、GroupId三选一必传
        :type RoleId: int
        :param GroupId: 用户组ID，与TargetUin、RoleId三选一必传
        :type GroupId: int
        :param ServiceType: 服务名，查看服务授权接口详情时需传该字段
        :type ServiceType: str
        """
        self.TargetUin = None
        self.RoleId = None
        self.GroupId = None
        self.ServiceType = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.RoleId = params.get("RoleId")
        self.GroupId = params.get("GroupId")
        self.ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesGrantingServiceAccessResponse(AbstractModel):
    """ListPoliciesGrantingServiceAccess返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 列表
        :type List: list of ListGrantServiceAccessNode
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ListGrantServiceAccessNode()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListPoliciesRequest(AbstractModel):
    """ListPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param Rp: 每页数量，默认值是 20，必须大于 0 且小于或等于 200
        :type Rp: int
        :param Page: 页码，默认值是 1，从 1开始，不能大于 200
        :type Page: int
        :param Scope: 可取值 'All'、'QCS' 和 'Local'，'All' 获取所有策略，'QCS' 只获取预设策略，'Local' 只获取自定义策略，默认取 'All'
        :type Scope: str
        :param Keyword: 按策略名匹配
        :type Keyword: str
        """
        self.Rp = None
        self.Page = None
        self.Scope = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.Scope = params.get("Scope")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesResponse(AbstractModel):
    """ListPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 策略总数
        :type TotalNum: int
        :param List: 策略数组，数组每个成员包括 policyId、policyName、addTime、type、description、 createMode 字段。其中： 
policyId：策略 id 
policyName：策略名
addTime：策略创建时间
type：1 表示自定义策略，2 表示预设策略 
description：策略描述 
createMode：1 表示按业务权限创建的策略，其他值表示可以查看策略语法和通过策略语法更新策略
Attachments: 关联的用户数
ServiceType: 策略关联的产品
IsAttached: 当需要查询标记实体是否已经关联策略时不为null。0表示未关联策略，1表示已关联策略
        :type List: list of StrategyInfo
        :param ServiceTypeList: 保留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTypeList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.ServiceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = StrategyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.ServiceTypeList = params.get("ServiceTypeList")
        self.RequestId = params.get("RequestId")


class ListPolicyVersionsRequest(AbstractModel):
    """ListPolicyVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPolicyVersionsResponse(AbstractModel):
    """ListPolicyVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Versions: 策略版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of PolicyVersionItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = PolicyVersionItem()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class ListSAMLProvidersRequest(AbstractModel):
    """ListSAMLProviders请求参数结构体

    """


class ListSAMLProvidersResponse(AbstractModel):
    """ListSAMLProviders返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: SAML身份提供商总数
        :type TotalCount: int
        :param SAMLProviderSet: SAML身份提供商列表
        :type SAMLProviderSet: list of SAMLProviderInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SAMLProviderSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SAMLProviderSet") is not None:
            self.SAMLProviderSet = []
            for item in params.get("SAMLProviderSet"):
                obj = SAMLProviderInfo()
                obj._deserialize(item)
                self.SAMLProviderSet.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersForGroupRequest(AbstractModel):
    """ListUsersForGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID。
        :type GroupId: int
        :param Page: 页码。默认为1。
        :type Page: int
        :param Rp: 每页数量。默认为20。
        :type Rp: int
        """
        self.GroupId = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersForGroupResponse(AbstractModel):
    """ListUsersForGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 用户组关联的用户总数。
        :type TotalNum: int
        :param UserInfo: 子用户信息。
        :type UserInfo: list of GroupMemberInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers请求参数结构体

    """


class ListUsersResponse(AbstractModel):
    """ListUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 子用户信息
        :type Data: list of SubAccountInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ListWeChatWorkSubAccountsRequest(AbstractModel):
    """ListWeChatWorkSubAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListWeChatWorkSubAccountsResponse(AbstractModel):
    """ListWeChatWorkSubAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 企业微信子用户列表。
        :type Data: list of WeChatWorkSubAccount
        :param TotalCount: 总数目。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = WeChatWorkSubAccount()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class LoginActionFlag(AbstractModel):
    """登录和敏感操作flag

    """

    def __init__(self):
        r"""
        :param Phone: 手机
        :type Phone: int
        :param Token: 硬token
        :type Token: int
        :param Stoken: 软token
        :type Stoken: int
        :param Wechat: 微信
        :type Wechat: int
        :param Custom: 自定义
        :type Custom: int
        """
        self.Phone = None
        self.Token = None
        self.Stoken = None
        self.Wechat = None
        self.Custom = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Token = params.get("Token")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        self.Custom = params.get("Custom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionFlagIntl(AbstractModel):
    """登录和敏感操作flag

    """

    def __init__(self):
        r"""
        :param Phone: 手机
        :type Phone: int
        :param Token: 硬token
        :type Token: int
        :param Stoken: 软token
        :type Stoken: int
        :param Wechat: 微信
        :type Wechat: int
        :param Custom: 自定义
        :type Custom: int
        :param Mail: 邮件
        :type Mail: int
        """
        self.Phone = None
        self.Token = None
        self.Stoken = None
        self.Wechat = None
        self.Custom = None
        self.Mail = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Token = params.get("Token")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        self.Custom = params.get("Custom")
        self.Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionMfaFlag(AbstractModel):
    """登录和敏感操作flag

    """

    def __init__(self):
        r"""
        :param Phone: 手机
        :type Phone: int
        :param Stoken: 软token
        :type Stoken: int
        :param Wechat: 微信
        :type Wechat: int
        """
        self.Phone = None
        self.Stoken = None
        self.Wechat = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffsiteFlag(AbstractModel):
    """异地登录设置

    """

    def __init__(self):
        r"""
        :param VerifyFlag: 验证标识
        :type VerifyFlag: int
        :param NotifyPhone: 手机通知
        :type NotifyPhone: int
        :param NotifyEmail: 邮箱通知
        :type NotifyEmail: int
        :param NotifyWechat: 微信通知
        :type NotifyWechat: int
        :param Tips: 提示
        :type Tips: int
        """
        self.VerifyFlag = None
        self.NotifyPhone = None
        self.NotifyEmail = None
        self.NotifyWechat = None
        self.Tips = None


    def _deserialize(self, params):
        self.VerifyFlag = params.get("VerifyFlag")
        self.NotifyPhone = params.get("NotifyPhone")
        self.NotifyEmail = params.get("NotifyEmail")
        self.NotifyWechat = params.get("NotifyWechat")
        self.Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionDetail(AbstractModel):
    """策略版本详情

    """

    def __init__(self):
        r"""
        :param VersionId: 策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param CreateDate: 策略版本创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param IsDefaultVersion: 是否是正在生效的版本。0表示不是，1表示是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultVersion: int
        :param Document: 策略语法文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Document: str
        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None
        self.Document = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        self.Document = params.get("Document")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionItem(AbstractModel):
    """策略版本列表元素结构

    """

    def __init__(self):
        r"""
        :param VersionId: 策略版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param CreateDate: 策略版本创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param IsDefaultVersion: 是否是正在生效的版本。0表示不是，1表示是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultVersion: int
        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryRequest(AbstractModel):
    """PutRolePermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param RoleId: 角色ID（与角色名至少填一个）
        :type RoleId: str
        :param RoleName: 角色名（与角色ID至少填一个）
        :type RoleName: str
        """
        self.PolicyId = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryResponse(AbstractModel):
    """PutRolePermissionsBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutUserPermissionsBoundaryRequest(AbstractModel):
    """PutUserPermissionsBoundary请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 子账号Uin
        :type TargetUin: int
        :param PolicyId: 策略ID
        :type PolicyId: int
        """
        self.TargetUin = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutUserPermissionsBoundaryResponse(AbstractModel):
    """PutUserPermissionsBoundary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 要删除的用户 UIN/UID和用户组 ID对应数组
        :type Info: list of GroupIdOfUidInfo
        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromGroupResponse(AbstractModel):
    """RemoveUserFromGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoleInfo(AbstractModel):
    """角色详细信息

    """

    def __init__(self):
        r"""
        :param RoleId: 角色ID
        :type RoleId: str
        :param RoleName: 角色名称
        :type RoleName: str
        :param PolicyDocument: 角色的策略文档
        :type PolicyDocument: str
        :param Description: 角色描述
        :type Description: str
        :param AddTime: 角色的创建时间
        :type AddTime: str
        :param UpdateTime: 角色的最近一次时间
        :type UpdateTime: str
        :param ConsoleLogin: 角色是否允许登录
        :type ConsoleLogin: int
        :param RoleType: 角色类型，取user、system或service_linked
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleType: str
        :param SessionDuration: 有效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionDuration: int
        :param DeletionTaskId: 服务相关角色删除TaskId
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletionTaskId: str
        """
        self.RoleId = None
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.AddTime = None
        self.UpdateTime = None
        self.ConsoleLogin = None
        self.RoleType = None
        self.SessionDuration = None
        self.DeletionTaskId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleType = params.get("RoleType")
        self.SessionDuration = params.get("SessionDuration")
        self.DeletionTaskId = params.get("DeletionTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SAMLProviderInfo(AbstractModel):
    """SAML身份提供商

    """

    def __init__(self):
        r"""
        :param Name: SAML身份提供商名称
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param CreateTime: SAML身份提供商创建时间
        :type CreateTime: str
        :param ModifyTime: SAML身份提供商上次修改时间
        :type ModifyTime: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecretIdLastUsed(AbstractModel):
    """密钥最后使用时间

    """

    def __init__(self):
        r"""
        :param SecretId: 密钥ID
        :type SecretId: str
        :param LastUsedDate: 最后访问日期(有1天延迟)
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUsedDate: str
        """
        self.SecretId = None
        self.LastUsedDate = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.LastUsedDate = params.get("LastUsedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionRequest(AbstractModel):
    """SetDefaultPolicyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param VersionId: 策略版本号，可由ListPolicyVersions获取
        :type VersionId: int
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionResponse(AbstractModel):
    """SetDefaultPolicyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetMfaFlagRequest(AbstractModel):
    """SetMfaFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpUin: 设置用户的uin
        :type OpUin: int
        :param LoginFlag: 登录保护设置
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        :param ActionFlag: 操作保护设置
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        """
        self.OpUin = None
        self.LoginFlag = None
        self.ActionFlag = None


    def _deserialize(self, params):
        self.OpUin = params.get("OpUin")
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionMfaFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionMfaFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetMfaFlagResponse(AbstractModel):
    """SetMfaFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StrategyInfo(AbstractModel):
    """策略信息

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID。
        :type PolicyId: int
        :param PolicyName: 策略名称。
        :type PolicyName: str
        :param AddTime: 策略创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param Type: 策略类型。1 表示自定义策略，2 表示预设策略。
        :type Type: int
        :param Description: 策略描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateMode: 创建来源，1 通过控制台创建, 2 通过策略语法创建。
        :type CreateMode: int
        :param Attachments: 关联的用户数
        :type Attachments: int
        :param ServiceType: 策略关联的产品
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param IsAttached: 当需要查询标记实体是否已经关联策略时不为null。0表示未关联策略，1表示已关联策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAttached: int
        :param Deactived: 是否已下线
注意：此字段可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param DeactivedDetail: 已下线产品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        :param IsServiceLinkedPolicy: 是否是服务相关角色策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsServiceLinkedPolicy: int
        :param AttachEntityCount: 关联策略实体数
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachEntityCount: int
        :param AttachEntityBoundaryCount: 关联权限边界实体数
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachEntityBoundaryCount: int
        :param UpdateTime: 最后编辑时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.Type = None
        self.Description = None
        self.CreateMode = None
        self.Attachments = None
        self.ServiceType = None
        self.IsAttached = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.IsServiceLinkedPolicy = None
        self.AttachEntityCount = None
        self.AttachEntityBoundaryCount = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.CreateMode = params.get("CreateMode")
        self.Attachments = params.get("Attachments")
        self.ServiceType = params.get("ServiceType")
        self.IsAttached = params.get("IsAttached")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.IsServiceLinkedPolicy = params.get("IsServiceLinkedPolicy")
        self.AttachEntityCount = params.get("AttachEntityCount")
        self.AttachEntityBoundaryCount = params.get("AttachEntityBoundaryCount")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountInfo(AbstractModel):
    """子用户信息

    """

    def __init__(self):
        r"""
        :param Uin: 子用户用户 ID
        :type Uin: int
        :param Name: 子用户用户名
        :type Name: str
        :param Uid: 子用户 UID
        :type Uid: int
        :param Remark: 子用户备注
        :type Remark: str
        :param ConsoleLogin: 子用户能否登录控制台
        :type ConsoleLogin: int
        :param PhoneNum: 手机号
        :type PhoneNum: str
        :param CountryCode: 区号
        :type CountryCode: str
        :param Email: 邮箱
        :type Email: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountUser(AbstractModel):
    """子用户信息

    """

    def __init__(self):
        r"""
        :param Uin: 子用户用户 ID
        :type Uin: int
        :param Name: 子用户用户名
        :type Name: str
        :param Uid: 子用户 UID
        :type Uid: int
        :param Remark: 子用户备注
        :type Remark: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UserType: 用户类型(2:子用户;3:企业微信子用户;4:协作者;5:消息接收人)
        :type UserType: int
        :param LastLoginIp: 最近登录IP
        :type LastLoginIp: str
        :param LastLoginTime: 最近登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLoginTime: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.CreateTime = None
        self.UserType = None
        self.LastLoginIp = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UserType = params.get("UserType")
        self.LastLoginIp = params.get("LastLoginIp")
        self.LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssumeRolePolicyRequest(AbstractModel):
    """UpdateAssumeRolePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyDocument: 策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :type PolicyDocument: str
        :param RoleId: 角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param RoleName: 角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self.PolicyDocument = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.PolicyDocument = params.get("PolicyDocument")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssumeRolePolicyResponse(AbstractModel):
    """UpdateAssumeRolePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 用户组 ID
        :type GroupId: int
        :param GroupName: 用户组名
        :type GroupName: str
        :param Remark: 用户组描述
        :type Remark: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGroupResponse(AbstractModel):
    """UpdateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePolicyRequest(AbstractModel):
    """UpdatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID，与PolicyName二选一必填
        :type PolicyId: int
        :param PolicyName: 策略名，与PolicyId二选一必填
        :type PolicyName: str
        :param Description: 策略描述
        :type Description: str
        :param PolicyDocument: 策略文档，示例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo
        :type PolicyDocument: str
        :param Alias: 预设策略备注
        :type Alias: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.PolicyDocument = None
        self.Alias = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略id，入参是PolicyName时，才会返回
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class UpdateRoleConsoleLoginRequest(AbstractModel):
    """UpdateRoleConsoleLogin请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConsoleLogin: 是否可登录，可登录：1，不可登录：0
        :type ConsoleLogin: int
        :param RoleId: 角色ID，入参 RoleId 与 RoleName 二选一
        :type RoleId: int
        :param RoleName: 角色名，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self.ConsoleLogin = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleConsoleLoginResponse(AbstractModel):
    """UpdateRoleConsoleLogin返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRoleDescriptionRequest(AbstractModel):
    """UpdateRoleDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param Description: 角色描述
        :type Description: str
        :param RoleId: 角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleId: str
        :param RoleName: 角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一
        :type RoleName: str
        """
        self.Description = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleDescriptionResponse(AbstractModel):
    """UpdateRoleDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateSAMLProviderRequest(AbstractModel):
    """UpdateSAMLProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: SAML身份提供商名称
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param SAMLMetadataDocument: SAML身份提供商Base64编码的元数据文档
        :type SAMLMetadataDocument: str
        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSAMLProviderResponse(AbstractModel):
    """UpdateSAMLProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    """UpdateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 子用户用户名
        :type Name: str
        :param Remark: 子用户备注
        :type Remark: str
        :param ConsoleLogin: 子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :type ConsoleLogin: int
        :param Password: 子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。
        :type Password: str
        :param NeedResetPassword: 子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。
        :type NeedResetPassword: int
        :param PhoneNum: 手机号
        :type PhoneNum: str
        :param CountryCode: 区号
        :type CountryCode: str
        :param Email: 邮箱
        :type Email: str
        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserSAMLConfigRequest(AbstractModel):
    """UpdateUserSAMLConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operate: 修改的操作类型:enable:启用,disable:禁用,updateSAML:修改元数据文档
        :type Operate: str
        :param SAMLMetadataDocument: 元数据文档，需要base64 encode，仅当Operate为updateSAML时需要此参数
        :type SAMLMetadataDocument: str
        """
        self.Operate = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Operate = params.get("Operate")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserSAMLConfigResponse(AbstractModel):
    """UpdateUserSAMLConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WeChatWorkSubAccount(AbstractModel):
    """企业微信子用户

    """

    def __init__(self):
        r"""
        :param Uin: 子用户用户 ID
        :type Uin: int
        :param Name: 子用户用户名
        :type Name: str
        :param Uid: 子用户 UID
        :type Uid: int
        :param Remark: 备注
        :type Remark: str
        :param ConsoleLogin: 子用户能否登录控制台
        :type ConsoleLogin: int
        :param PhoneNum: 手机号
        :type PhoneNum: str
        :param CountryCode: 区号
        :type CountryCode: str
        :param Email: 邮箱
        :type Email: str
        :param WeChatWorkUserId: 企业微信UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type WeChatWorkUserId: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.WeChatWorkUserId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.WeChatWorkUserId = params.get("WeChatWorkUserId")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        