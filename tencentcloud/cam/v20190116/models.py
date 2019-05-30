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


class AddUserRequest(AbstractModel):
    """AddUser请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 子用户用户名
        :type Name: str
        :param Remark: 子用户备注
        :type Remark: str
        :param ConsoleLogin: 子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :type ConsoleLogin: int
        :param UseApi: 是否生成子用户密钥。传0不生成子用户密钥，传1生成子用户密钥。
        :type UseApi: int
        :param Password: 子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大写小字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大写小字母、数字和特殊字符。
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


class AddUserResponse(AbstractModel):
    """AddUser返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Info: 添加的子用户 UID 和用户组 ID 关联关系
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


class AddUserToGroupResponse(AbstractModel):
    """AddUserToGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        self.Id = None
        self.Name = None
        self.Uin = None
        self.RelatedType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Uin = params.get("Uin")
        self.RelatedType = params.get("RelatedType")


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
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


class AttachGroupPolicyResponse(AbstractModel):
    """AttachGroupPolicy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.CreateMode = None
        self.PolicyType = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.CreateMode = params.get("CreateMode")
        self.PolicyType = params.get("PolicyType")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy请求参数结构体

    """

    def __init__(self):
        """
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


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param PolicyName: 策略名
        :type PolicyName: str
        :param PolicyDocument: 策略文档
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


class CreatePolicyResponse(AbstractModel):
    """CreatePolicy返回参数结构体

    """

    def __init__(self):
        """
        :param PolicyId: 新增策略id
        :type PolicyId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateSAMLProviderRequest(AbstractModel):
    """CreateSAMLProvider请求参数结构体

    """

    def __init__(self):
        """
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


class CreateSAMLProviderResponse(AbstractModel):
    """CreateSAMLProvider返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 用户组 ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param PolicyId: 数组，数组成员是策略 id，支持批量删除策略
        :type PolicyId: list of int non-negative
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")


class DeletePolicyResponse(AbstractModel):
    """DeletePolicy返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Name: SAML身份提供商名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class DeleteSAMLProviderResponse(AbstractModel):
    """DeleteSAMLProvider返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Name: 子用户用户名
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
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


class DetachGroupPolicyResponse(AbstractModel):
    """DetachGroupPolicy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    """GetGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 用户组 ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetGroupResponse(AbstractModel):
    """GetGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param PolicyId: 策略Id
        :type PolicyId: int
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")


class GetPolicyResponse(AbstractModel):
    """GetPolicy返回参数结构体

    """

    def __init__(self):
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyName = None
        self.Description = None
        self.Type = None
        self.AddTime = None
        self.UpdateTime = None
        self.PolicyDocument = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.PolicyDocument = params.get("PolicyDocument")
        self.RequestId = params.get("RequestId")


class GetSAMLProviderRequest(AbstractModel):
    """GetSAMLProvider请求参数结构体

    """

    def __init__(self):
        """
        :param Name: SAML身份提供商名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class GetSAMLProviderResponse(AbstractModel):
    """GetSAMLProvider返回参数结构体

    """

    def __init__(self):
        """
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


class GetUserRequest(AbstractModel):
    """GetUser请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 子用户用户名
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class GetUserResponse(AbstractModel):
    """GetUser返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Uid: 子用户 UID
        :type Uid: int
        :param GroupId: 用户组 ID
        :type GroupId: int
        """
        self.Uid = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.GroupId = params.get("GroupId")


class GroupInfo(AbstractModel):
    """用户组信息

    """

    def __init__(self):
        """
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


class GroupMemberInfo(AbstractModel):
    """用户组用户信息

    """

    def __init__(self):
        """
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
        :param PhoneFlag: 是否已验证手机。
        :type PhoneFlag: int
        :param Email: 邮箱地址。
        :type Email: str
        :param EmailFlag: 是否已验证邮箱。
        :type EmailFlag: int
        :param UserType: 用户类型。
        :type UserType: int
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param IsReceiverOwner: 是否为主消息接收人。
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


class ListAttachedGroupPoliciesRequest(AbstractModel):
    """ListAttachedGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param TargetGroupId: 用户组 id
        :type TargetGroupId: int
        :param Page: 页码，默认值是 1，从 1 开始
        :type Page: int
        :param Rp: 每页大小，默认值是 20
        :type Rp: int
        """
        self.TargetGroupId = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")


class ListAttachedGroupPoliciesResponse(AbstractModel):
    """ListAttachedGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
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


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies请求参数结构体

    """

    def __init__(self):
        """
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


class ListAttachedUserPoliciesResponse(AbstractModel):
    """ListAttachedUserPolicies返回参数结构体

    """

    def __init__(self):
        """
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


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy请求参数结构体

    """

    def __init__(self):
        """
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


class ListEntitiesForPolicyResponse(AbstractModel):
    """ListEntitiesForPolicy返回参数结构体

    """

    def __init__(self):
        """
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


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser请求参数结构体

    """

    def __init__(self):
        """
        :param Uid: 子用户 UID
        :type Uid: int
        :param Rp: 每页数量。默认为20。
        :type Rp: int
        :param Page: 页码。默认为1。
        :type Page: int
        """
        self.Uid = None
        self.Rp = None
        self.Page = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")


class ListGroupsForUserResponse(AbstractModel):
    """ListGroupsForUser返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ListGroupsResponse(AbstractModel):
    """ListGroups返回参数结构体

    """

    def __init__(self):
        """
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


class ListPoliciesRequest(AbstractModel):
    """ListPolicies请求参数结构体

    """

    def __init__(self):
        """
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


class ListPoliciesResponse(AbstractModel):
    """ListPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 策略总数
        :type TotalNum: int
        :param List: 策略数组，数组每个成员包括 policyId、policyName、addTime、type、description、 createMode 字段。其中： 
policyId：策略 id 
policyName：策略名
addTime：策略创建时间
type：1 表示自定义策略，2 表示预设策略 
description：策略描述 
createMode：1 表示按业务权限创建的策略，其他值表示可以查看策略语法和通过策略语法更新策略
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


class ListSAMLProvidersRequest(AbstractModel):
    """ListSAMLProviders请求参数结构体

    """


class ListSAMLProvidersResponse(AbstractModel):
    """ListSAMLProviders返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ListUsersForGroupResponse(AbstractModel):
    """ListUsersForGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup请求参数结构体

    """

    def __init__(self):
        """
        :param Info: 要删除的用户 UID和用户组 ID对应数组
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


class RemoveUserFromGroupResponse(AbstractModel):
    """RemoveUserFromGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SAMLProviderInfo(AbstractModel):
    """SAML身份提供商

    """

    def __init__(self):
        """
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


class StrategyInfo(AbstractModel):
    """策略信息

    """

    def __init__(self):
        """
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
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.Type = None
        self.Description = None
        self.CreateMode = None
        self.Attachments = None
        self.ServiceType = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.CreateMode = params.get("CreateMode")
        self.Attachments = params.get("Attachments")
        self.ServiceType = params.get("ServiceType")


class SubAccountInfo(AbstractModel):
    """子用户信息

    """

    def __init__(self):
        """
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
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup请求参数结构体

    """

    def __init__(self):
        """
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


class UpdateGroupResponse(AbstractModel):
    """UpdateGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Description: 策略描述
        :type Description: str
        :param PolicyDocument: 策略文档
        :type PolicyDocument: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.PolicyDocument = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.PolicyDocument = params.get("PolicyDocument")


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UpdateSAMLProviderResponse(AbstractModel):
    """UpdateSAMLProvider返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Name: 子用户用户名
        :type Name: str
        :param Remark: 子用户备注
        :type Remark: str
        :param ConsoleLogin: 子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。
        :type ConsoleLogin: int
        :param Password: 子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大写小字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大写小字母、数字和特殊字符。
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


class UpdateUserResponse(AbstractModel):
    """UpdateUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")