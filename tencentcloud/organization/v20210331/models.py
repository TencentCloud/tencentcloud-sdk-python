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


class AddOrganizationMemberEmailRequest(AbstractModel):
    """AddOrganizationMemberEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin
        :type MemberUin: int
        :param _Email: 邮箱地址
        :type Email: str
        :param _CountryCode: 国际区号
        :type CountryCode: str
        :param _Phone: 手机号
        :type Phone: str
        """
        self._MemberUin = None
        self._Email = None
        self._CountryCode = None
        self._Phone = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Email = params.get("Email")
        self._CountryCode = params.get("CountryCode")
        self._Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationMemberEmailResponse(AbstractModel):
    """AddOrganizationMemberEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindId: 绑定Id
注意：此字段可能返回 null，表示取不到有效值。
        :type BindId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindId = None
        self._RequestId = None

    @property
    def BindId(self):
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BindId = params.get("BindId")
        self._RequestId = params.get("RequestId")


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ParentNodeId: 父节点ID。可以调用DescribeOrganizationNodes获取
        :type ParentNodeId: int
        :param _Name: 节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :type Name: str
        :param _Remark: 备注。
        :type Remark: str
        """
        self._ParentNodeId = None
        self._Name = None
        self._Remark = None

    @property
    def ParentNodeId(self):
        return self._ParentNodeId

    @ParentNodeId.setter
    def ParentNodeId(self, ParentNodeId):
        self._ParentNodeId = ParentNodeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ParentNodeId = params.get("ParentNodeId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationNodeResponse(AbstractModel):
    """AddOrganizationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID。
        :type NodeId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeId = None
        self._RequestId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._RequestId = params.get("RequestId")


class AuthNode(AbstractModel):
    """互信主体主要信息

    """

    def __init__(self):
        r"""
        :param _RelationId: 互信主体关系ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationId: int
        :param _AuthName: 互信主体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthName: str
        :param _Manager: 主体管理员
注意：此字段可能返回 null，表示取不到有效值。
        :type Manager: :class:`tencentcloud.organization.v20210331.models.MemberMainInfo`
        """
        self._RelationId = None
        self._AuthName = None
        self._Manager = None

    @property
    def RelationId(self):
        return self._RelationId

    @RelationId.setter
    def RelationId(self, RelationId):
        self._RelationId = RelationId

    @property
    def AuthName(self):
        return self._AuthName

    @AuthName.setter
    def AuthName(self, AuthName):
        self._AuthName = AuthName

    @property
    def Manager(self):
        return self._Manager

    @Manager.setter
    def Manager(self, Manager):
        self._Manager = Manager


    def _deserialize(self, params):
        self._RelationId = params.get("RelationId")
        self._AuthName = params.get("AuthName")
        if params.get("Manager") is not None:
            self._Manager = MemberMainInfo()
            self._Manager._deserialize(params.get("Manager"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountRequest(AbstractModel):
    """BindOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyId: 策略ID。可以调用DescribeOrganizationMemberPolicies获取
        :type PolicyId: int
        :param _OrgSubAccountUins: 组织管理员子账号Uin列表。最大5个
        :type OrgSubAccountUins: list of int
        """
        self._MemberUin = None
        self._PolicyId = None
        self._OrgSubAccountUins = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUins(self):
        return self._OrgSubAccountUins

    @OrgSubAccountUins.setter
    def OrgSubAccountUins(self, OrgSubAccountUins):
        self._OrgSubAccountUins = OrgSubAccountUins


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountResponse(AbstractModel):
    """BindOrganizationMemberAuthAccount返回参数结构体

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


class CancelOrganizationMemberAuthAccountRequest(AbstractModel):
    """CancelOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _OrgSubAccountUin: 组织子账号Uin。
        :type OrgSubAccountUin: int
        """
        self._MemberUin = None
        self._PolicyId = None
        self._OrgSubAccountUin = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUin(self):
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationMemberAuthAccountResponse(AbstractModel):
    """CancelOrganizationMemberAuthAccount返回参数结构体

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


class CreateOrganizationIdentityRequest(AbstractModel):
    """CreateOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityAliasName: 身份名称
        :type IdentityAliasName: str
        :param _IdentityPolicy: 身份策略
        :type IdentityPolicy: list of IdentityPolicy
        :param _Description: 身份描述
        :type Description: str
        """
        self._IdentityAliasName = None
        self._IdentityPolicy = None
        self._Description = None

    @property
    def IdentityAliasName(self):
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName

    @property
    def IdentityPolicy(self):
        return self._IdentityPolicy

    @IdentityPolicy.setter
    def IdentityPolicy(self, IdentityPolicy):
        self._IdentityPolicy = IdentityPolicy

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityAliasName = params.get("IdentityAliasName")
        if params.get("IdentityPolicy") is not None:
            self._IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self._IdentityPolicy.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationIdentityResponse(AbstractModel):
    """CreateOrganizationIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdentityId = None
        self._RequestId = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._RequestId = params.get("RequestId")


class CreateOrganizationMemberAuthIdentityRequest(AbstractModel):
    """CreateOrganizationMemberAuthIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUins: 成员uin列表。最多10个
        :type MemberUins: list of int non-negative
        :param _IdentityIds: 身份Id列表。最多5个
        :type IdentityIds: list of int non-negative
        """
        self._MemberUins = None
        self._IdentityIds = None

    @property
    def MemberUins(self):
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def IdentityIds(self):
        return self._IdentityIds

    @IdentityIds.setter
    def IdentityIds(self, IdentityIds):
        self._IdentityIds = IdentityIds


    def _deserialize(self, params):
        self._MemberUins = params.get("MemberUins")
        self._IdentityIds = params.get("IdentityIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberAuthIdentityResponse(AbstractModel):
    """CreateOrganizationMemberAuthIdentity返回参数结构体

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


class CreateOrganizationMemberPolicyRequest(AbstractModel):
    """CreateOrganizationMemberPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyName: 策略名。最大长度为128个字符，支持英文字母、数字、符号+=,.@_-
        :type PolicyName: str
        :param _IdentityId: 成员访问身份ID。可以调用DescribeOrganizationMemberAuthIdentities获取
        :type IdentityId: int
        :param _Description: 描述。
        :type Description: str
        """
        self._MemberUin = None
        self._PolicyName = None
        self._IdentityId = None
        self._Description = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberPolicyResponse(AbstractModel):
    """CreateOrganizationMemberPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateOrganizationMemberRequest(AbstractModel):
    """CreateOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type Name: str
        :param _PolicyType: 关系策略。取值：Financial
        :type PolicyType: str
        :param _PermissionIds: 成员财务权限ID列表。取值：1-查看账单、2-查看余额、3-资金划拨、4-合并出账、5-开票、6-优惠继承、7-代付费，1、2 默认必须
        :type PermissionIds: list of int non-negative
        :param _NodeId: 成员所属部门的节点ID。可以调用DescribeOrganizationNodes获取
        :type NodeId: int
        :param _AccountName: 账号名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type AccountName: str
        :param _Remark: 备注。
        :type Remark: str
        :param _RecordId: 成员创建记录ID。创建异常重试时需要
        :type RecordId: int
        :param _PayUin: 代付者Uin。成员代付费时需要
        :type PayUin: str
        :param _IdentityRoleID: 成员访问身份ID列表。可以调用ListOrganizationIdentity获取，1默认支持
        :type IdentityRoleID: list of int non-negative
        :param _AuthRelationId: 认证主体关系ID。给不同主体创建成员时需要，可以调用DescribeOrganizationAuthNode获取
        :type AuthRelationId: int
        """
        self._Name = None
        self._PolicyType = None
        self._PermissionIds = None
        self._NodeId = None
        self._AccountName = None
        self._Remark = None
        self._RecordId = None
        self._PayUin = None
        self._IdentityRoleID = None
        self._AuthRelationId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PermissionIds(self):
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def PayUin(self):
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def IdentityRoleID(self):
        return self._IdentityRoleID

    @IdentityRoleID.setter
    def IdentityRoleID(self, IdentityRoleID):
        self._IdentityRoleID = IdentityRoleID

    @property
    def AuthRelationId(self):
        return self._AuthRelationId

    @AuthRelationId.setter
    def AuthRelationId(self, AuthRelationId):
        self._AuthRelationId = AuthRelationId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PolicyType = params.get("PolicyType")
        self._PermissionIds = params.get("PermissionIds")
        self._NodeId = params.get("NodeId")
        self._AccountName = params.get("AccountName")
        self._Remark = params.get("Remark")
        self._RecordId = params.get("RecordId")
        self._PayUin = params.get("PayUin")
        self._IdentityRoleID = params.get("IdentityRoleID")
        self._AuthRelationId = params.get("AuthRelationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberResponse(AbstractModel):
    """CreateOrganizationMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 成员Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class CreateOrganizationMembersPolicyRequest(AbstractModel):
    """CreateOrganizationMembersPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUins: 成员Uin列表。最多10个
        :type MemberUins: list of int
        :param _PolicyName: 策略名。长度1～128个字符，支持英文字母、数字、符号+=,.@_-
        :type PolicyName: str
        :param _IdentityId: 成员访问身份ID。
        :type IdentityId: int
        :param _Description: 策略描述。最大长度为128个字符
        :type Description: str
        """
        self._MemberUins = None
        self._PolicyName = None
        self._IdentityId = None
        self._Description = None

    @property
    def MemberUins(self):
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._MemberUins = params.get("MemberUins")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMembersPolicyResponse(AbstractModel):
    """CreateOrganizationMembersPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateOrganizationRequest(AbstractModel):
    """CreateOrganization请求参数结构体

    """


class CreateOrganizationResponse(AbstractModel):
    """CreateOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID
        :type OrgId: int
        :param _NickName: 创建者昵称
        :type NickName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgId = None
        self._NickName = None
        self._RequestId = None

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._NickName = params.get("NickName")
        self._RequestId = params.get("RequestId")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员uin。
        :type MemberUin: int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

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


class DeleteOrganizationIdentityRequest(AbstractModel):
    """DeleteOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID
        :type IdentityId: int
        """
        self._IdentityId = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationIdentityResponse(AbstractModel):
    """DeleteOrganizationIdentity返回参数结构体

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


class DeleteOrganizationMemberAuthIdentityRequest(AbstractModel):
    """DeleteOrganizationMemberAuthIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员uin。
        :type MemberUin: int
        :param _IdentityId: 身份Id。
        :type IdentityId: int
        """
        self._MemberUin = None
        self._IdentityId = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMemberAuthIdentityResponse(AbstractModel):
    """DeleteOrganizationMemberAuthIdentity返回参数结构体

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


class DeleteOrganizationMembersPolicyRequest(AbstractModel):
    """DeleteOrganizationMembersPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 访问策略ID。
        :type PolicyId: int
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMembersPolicyResponse(AbstractModel):
    """DeleteOrganizationMembersPolicy返回参数结构体

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


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 被删除成员的UIN列表。
        :type MemberUin: list of int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMembersResponse(AbstractModel):
    """DeleteOrganizationMembers返回参数结构体

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


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID列表。
        :type NodeId: list of int
        """
        self._NodeId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationNodesResponse(AbstractModel):
    """DeleteOrganizationNodes返回参数结构体

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


class DeleteOrganizationRequest(AbstractModel):
    """DeleteOrganization请求参数结构体

    """


class DeleteOrganizationResponse(AbstractModel):
    """DeleteOrganization返回参数结构体

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


class DescribeOrganizationAuthNodeRequest(AbstractModel):
    """DescribeOrganizationAuthNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。
        :type Offset: int
        :param _Limit: 限制数目。最大50
        :type Limit: int
        :param _AuthName: 互信主体名称。
        :type AuthName: str
        """
        self._Offset = None
        self._Limit = None
        self._AuthName = None

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
    def AuthName(self):
        return self._AuthName

    @AuthName.setter
    def AuthName(self, AuthName):
        self._AuthName = AuthName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AuthName = params.get("AuthName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationAuthNodeResponse(AbstractModel):
    """DescribeOrganizationAuthNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Items: 条目详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuthNode
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuthNode()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationFinancialByMemberRequest(AbstractModel):
    """DescribeOrganizationFinancialByMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 查询开始月份。格式：yyyy-mm，例如：2021-01。
        :type Month: str
        :param _Limit: 限制数目。取值范围：1~50，默认值：10	
        :type Limit: int
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _EndMonth: 查询结束月份。格式：yyyy-mm，例如：2021-01,默认值为查询开始月份。
        :type EndMonth: str
        :param _MemberUins: 查询成员列表。 最大100个
        :type MemberUins: list of int
        :param _ProductCodes: 查询产品列表。 最大100个
        :type ProductCodes: list of str
        """
        self._Month = None
        self._Limit = None
        self._Offset = None
        self._EndMonth = None
        self._MemberUins = None
        self._ProductCodes = None

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndMonth(self):
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def MemberUins(self):
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def ProductCodes(self):
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EndMonth = params.get("EndMonth")
        self._MemberUins = params.get("MemberUins")
        self._ProductCodes = params.get("ProductCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationFinancialByMemberResponse(AbstractModel):
    """DescribeOrganizationFinancialByMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCost: 当月总消耗。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: float
        :param _Items: 成员消耗详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMemberFinancial
        :param _Total: 总数目。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCost = None
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCost = params.get("TotalCost")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberFinancial()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationFinancialByMonthRequest(AbstractModel):
    """DescribeOrganizationFinancialByMonth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 查询月数。取值范围：1~6，默认值：6
        :type Limit: int
        :param _EndMonth: 查询结束月份。格式：yyyy-mm，例如：2021-01
        :type EndMonth: str
        :param _MemberUins: 查询成员列表。 最大100个
        :type MemberUins: list of int
        :param _ProductCodes: 查询产品列表。 最大100个
        :type ProductCodes: list of str
        """
        self._Limit = None
        self._EndMonth = None
        self._MemberUins = None
        self._ProductCodes = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EndMonth(self):
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def MemberUins(self):
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def ProductCodes(self):
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._EndMonth = params.get("EndMonth")
        self._MemberUins = params.get("MemberUins")
        self._ProductCodes = params.get("ProductCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationFinancialByMonthResponse(AbstractModel):
    """DescribeOrganizationFinancialByMonth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 产品消耗详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgFinancialByMonth
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgFinancialByMonth()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationFinancialByProductRequest(AbstractModel):
    """DescribeOrganizationFinancialByProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 查询开始月份。格式：yyyy-mm，例如：2021-01
        :type Month: str
        :param _Limit: 限制数目。取值范围：1~50，默认值：10	
        :type Limit: int
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _EndMonth: 查询结束月份。格式：yyyy-mm，例如：2021-01,默认值为查询开始月份
        :type EndMonth: str
        :param _MemberUins: 查询成员列表。 最大100个
        :type MemberUins: list of int
        :param _ProductCodes: 查询产品列表。 最大100个
        :type ProductCodes: list of str
        """
        self._Month = None
        self._Limit = None
        self._Offset = None
        self._EndMonth = None
        self._MemberUins = None
        self._ProductCodes = None

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndMonth(self):
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def MemberUins(self):
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def ProductCodes(self):
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EndMonth = params.get("EndMonth")
        self._MemberUins = params.get("MemberUins")
        self._ProductCodes = params.get("ProductCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationFinancialByProductResponse(AbstractModel):
    """DescribeOrganizationFinancialByProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCost: 当月总消耗。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: float
        :param _Items: 产品消耗详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgProductFinancial
        :param _Total: 总数目。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCost = None
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCost = params.get("TotalCost")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgProductFinancial()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthAccountsRequest(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。
        :type Offset: int
        :param _Limit: 限制数目。
        :type Limit: int
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._PolicyId = None

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
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthAccountsResponse(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMemberAuthAccount
        :param _Total: 总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthAccount()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthIdentitiesRequest(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param _MemberUin: 组织成员Uin。入参MemberUin与IdentityId至少填写一个
        :type MemberUin: int
        :param _IdentityId: 身份ID。入参MemberUin与IdentityId至少填写一个
        :type IdentityId: int
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._IdentityId = None

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
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthIdentitiesResponse(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 授权身份列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMemberAuthIdentity
        :param _Total: 总数目。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthIdentity()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberEmailBindRequest(AbstractModel):
    """DescribeOrganizationMemberEmailBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin
        :type MemberUin: int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberEmailBindResponse(AbstractModel):
    """DescribeOrganizationMemberEmailBind返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindId: 绑定ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BindId: int
        :param _ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param _Email: 邮箱地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Phone: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _BindStatus: 绑定状态    未绑定：Unbound，待激活：Valid，绑定成功：Success，绑定失败：Failed
注意：此字段可能返回 null，表示取不到有效值。
        :type BindStatus: str
        :param _BindTime: 绑定时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BindTime: str
        :param _Description: 失败说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _PhoneBind: 安全手机绑定状态  未绑定：0，已绑定：1
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneBind: int
        :param _CountryCode: 国际区号
注意：此字段可能返回 null，表示取不到有效值。
        :type CountryCode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindId = None
        self._ApplyTime = None
        self._Email = None
        self._Phone = None
        self._BindStatus = None
        self._BindTime = None
        self._Description = None
        self._PhoneBind = None
        self._CountryCode = None
        self._RequestId = None

    @property
    def BindId(self):
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def ApplyTime(self):
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def BindStatus(self):
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def BindTime(self):
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PhoneBind(self):
        return self._PhoneBind

    @PhoneBind.setter
    def PhoneBind(self, PhoneBind):
        self._PhoneBind = PhoneBind

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BindId = params.get("BindId")
        self._ApplyTime = params.get("ApplyTime")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._BindStatus = params.get("BindStatus")
        self._BindTime = params.get("BindTime")
        self._Description = params.get("Description")
        self._PhoneBind = params.get("PhoneBind")
        self._CountryCode = params.get("CountryCode")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberPoliciesRequest(AbstractModel):
    """DescribeOrganizationMemberPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。
        :type Offset: int
        :param _Limit: 限制数目。最大50
        :type Limit: int
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _SearchKey: 搜索关键字。可用于策略名或描述搜索
        :type SearchKey: str
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._SearchKey = None

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
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberPoliciesResponse(AbstractModel):
    """DescribeOrganizationMemberPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMemberPolicy
        :param _Total: 总数目。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberPolicy()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMembersRequest(AbstractModel):
    """DescribeOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param _Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param _SearchKey: 成员名称或者成员ID搜索。
        :type SearchKey: str
        :param _AuthName: 主体名称搜索。
        :type AuthName: str
        :param _Product: 可信服务产品简称。可信服务管理员查询时必须指定
        :type Product: str
        """
        self._Offset = None
        self._Limit = None
        self._Lang = None
        self._SearchKey = None
        self._AuthName = None
        self._Product = None

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
    def Lang(self):
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def AuthName(self):
        return self._AuthName

    @AuthName.setter
    def AuthName(self, AuthName):
        self._AuthName = AuthName

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Lang = params.get("Lang")
        self._SearchKey = params.get("SearchKey")
        self._AuthName = params.get("AuthName")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMembersResponse(AbstractModel):
    """DescribeOrganizationMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 成员列表。
        :type Items: list of OrgMember
        :param _Total: 总数目。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMember()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationNodesRequest(AbstractModel):
    """DescribeOrganizationNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 限制数目。最大50
        :type Limit: int
        :param _Offset: 偏移量。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationNodesResponse(AbstractModel):
    """DescribeOrganizationNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Items: 列表详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgNode
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgNode()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationRequest(AbstractModel):
    """DescribeOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param _Product: 可信服务产品简称。查询是否该可信服务管理员时必须指定
        :type Product: str
        """
        self._Lang = None
        self._Product = None

    @property
    def Lang(self):
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Lang = params.get("Lang")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationResponse(AbstractModel):
    """DescribeOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgId: int
        :param _HostUin: 创建者UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostUin: int
        :param _NickName: 创建者昵称。
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _OrgType: 企业组织类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgType: int
        :param _IsManager: 是否组织管理员。是：true ，否：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsManager: bool
        :param _OrgPolicyType: 策略类型。财务管理：Financial
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyType: str
        :param _OrgPolicyName: 策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyName: str
        :param _OrgPermission: 成员财务权限列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPermission: list of OrgPermission
        :param _RootNodeId: 组织根节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RootNodeId: int
        :param _CreateTime: 组织创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _JoinTime: 成员加入时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTime: str
        :param _IsAllowQuit: 成员是否允许退出。允许：Allow，不允许：Denied
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowQuit: str
        :param _PayUin: 代付者Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayUin: str
        :param _PayName: 代付者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param _IsAssignManager: 是否可信服务管理员。是：true，否：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssignManager: bool
        :param _IsAuthManager: 是否实名主体管理员。是：true，否：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAuthManager: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgId = None
        self._HostUin = None
        self._NickName = None
        self._OrgType = None
        self._IsManager = None
        self._OrgPolicyType = None
        self._OrgPolicyName = None
        self._OrgPermission = None
        self._RootNodeId = None
        self._CreateTime = None
        self._JoinTime = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._PayName = None
        self._IsAssignManager = None
        self._IsAuthManager = None
        self._RequestId = None

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def HostUin(self):
        return self._HostUin

    @HostUin.setter
    def HostUin(self, HostUin):
        self._HostUin = HostUin

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def OrgType(self):
        return self._OrgType

    @OrgType.setter
    def OrgType(self, OrgType):
        self._OrgType = OrgType

    @property
    def IsManager(self):
        return self._IsManager

    @IsManager.setter
    def IsManager(self, IsManager):
        self._IsManager = IsManager

    @property
    def OrgPolicyType(self):
        return self._OrgPolicyType

    @OrgPolicyType.setter
    def OrgPolicyType(self, OrgPolicyType):
        self._OrgPolicyType = OrgPolicyType

    @property
    def OrgPolicyName(self):
        return self._OrgPolicyName

    @OrgPolicyName.setter
    def OrgPolicyName(self, OrgPolicyName):
        self._OrgPolicyName = OrgPolicyName

    @property
    def OrgPermission(self):
        return self._OrgPermission

    @OrgPermission.setter
    def OrgPermission(self, OrgPermission):
        self._OrgPermission = OrgPermission

    @property
    def RootNodeId(self):
        return self._RootNodeId

    @RootNodeId.setter
    def RootNodeId(self, RootNodeId):
        self._RootNodeId = RootNodeId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def JoinTime(self):
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime

    @property
    def IsAllowQuit(self):
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def PayName(self):
        return self._PayName

    @PayName.setter
    def PayName(self, PayName):
        self._PayName = PayName

    @property
    def IsAssignManager(self):
        return self._IsAssignManager

    @IsAssignManager.setter
    def IsAssignManager(self, IsAssignManager):
        self._IsAssignManager = IsAssignManager

    @property
    def IsAuthManager(self):
        return self._IsAuthManager

    @IsAuthManager.setter
    def IsAuthManager(self, IsAuthManager):
        self._IsAuthManager = IsAuthManager

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._HostUin = params.get("HostUin")
        self._NickName = params.get("NickName")
        self._OrgType = params.get("OrgType")
        self._IsManager = params.get("IsManager")
        self._OrgPolicyType = params.get("OrgPolicyType")
        self._OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self._OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self._OrgPermission.append(obj)
        self._RootNodeId = params.get("RootNodeId")
        self._CreateTime = params.get("CreateTime")
        self._JoinTime = params.get("JoinTime")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._PayName = params.get("PayName")
        self._IsAssignManager = params.get("IsAssignManager")
        self._IsAuthManager = params.get("IsAuthManager")
        self._RequestId = params.get("RequestId")


class IdentityPolicy(AbstractModel):
    """组织身份策略

    """

    def __init__(self):
        r"""
        :param _PolicyId: CAM预设策略ID。PolicyType 为预设策略时有效且必选
        :type PolicyId: int
        :param _PolicyName: CAM预设策略名称。PolicyType 为预设策略时有效且必选
        :type PolicyName: str
        :param _PolicyType: 策略类型。取值 1-自定义策略  2-预设策略；默认值2
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyType: int
        :param _PolicyDocument: 自定义策略内容，遵循CAM策略语法。PolicyType 为自定义策略时有效且必选
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._PolicyType = None
        self._PolicyDocument = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._PolicyType = params.get("PolicyType")
        self._PolicyDocument = params.get("PolicyDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityRequest(AbstractModel):
    """ListOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。默认值：10。
        :type Limit: int
        :param _SearchKey: 名称搜索关键字。
        :type SearchKey: str
        :param _IdentityId: 身份ID搜索。
        :type IdentityId: int
        :param _IdentityType: 身份类型。取值范围 1-预设, 2-自定义
        :type IdentityType: int
        """
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._IdentityId = None
        self._IdentityType = None

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityType(self):
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._IdentityId = params.get("IdentityId")
        self._IdentityType = params.get("IdentityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityResponse(AbstractModel):
    """ListOrganizationIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Items: 条目详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgIdentity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgIdentity()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class MemberIdentity(AbstractModel):
    """成员管理身份

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param _IdentityAliasName: 身份名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityAliasName: str
        """
        self._IdentityId = None
        self._IdentityAliasName = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityAliasName(self):
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityAliasName = params.get("IdentityAliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemberMainInfo(AbstractModel):
    """成员主要信息

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员uin
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberUin: int
        :param _MemberName: 成员名称j
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        """
        self._MemberUin = None
        self._MemberName = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersRequest(AbstractModel):
    """MoveOrganizationNodeMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 组织节点ID。
        :type NodeId: int
        :param _MemberUin: 成员UIN列表。
        :type MemberUin: list of int
        """
        self._NodeId = None
        self._MemberUin = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersResponse(AbstractModel):
    """MoveOrganizationNodeMembers返回参数结构体

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


class OrgFinancialByMonth(AbstractModel):
    """按月获取组织财务信息

    """

    def __init__(self):
        r"""
        :param _Id: 记录ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Month: 月份，格式：yyyy-mm，示例：2021-01。
注意：此字段可能返回 null，表示取不到有效值。
        :type Month: str
        :param _TotalCost: 消耗金额，单元：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: float
        :param _GrowthRate: 比上月增长率%。正数增长，负数下降，空值无法统计。
注意：此字段可能返回 null，表示取不到有效值。
        :type GrowthRate: str
        """
        self._Id = None
        self._Month = None
        self._TotalCost = None
        self._GrowthRate = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Month(self):
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def GrowthRate(self):
        return self._GrowthRate

    @GrowthRate.setter
    def GrowthRate(self, GrowthRate):
        self._GrowthRate = GrowthRate


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Month = params.get("Month")
        self._TotalCost = params.get("TotalCost")
        self._GrowthRate = params.get("GrowthRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgIdentity(AbstractModel):
    """组织身份

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param _IdentityAliasName: 身份名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityAliasName: str
        :param _Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _IdentityPolicy: 身份策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityPolicy: list of IdentityPolicy
        :param _IdentityType: 身份类型。 1-预设、 2-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityType: int
        :param _UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._IdentityId = None
        self._IdentityAliasName = None
        self._Description = None
        self._IdentityPolicy = None
        self._IdentityType = None
        self._UpdateTime = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityAliasName(self):
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IdentityPolicy(self):
        return self._IdentityPolicy

    @IdentityPolicy.setter
    def IdentityPolicy(self, IdentityPolicy):
        self._IdentityPolicy = IdentityPolicy

    @property
    def IdentityType(self):
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityAliasName = params.get("IdentityAliasName")
        self._Description = params.get("Description")
        if params.get("IdentityPolicy") is not None:
            self._IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self._IdentityPolicy.append(obj)
        self._IdentityType = params.get("IdentityType")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMember(AbstractModel):
    """企业组织成员

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberUin: int
        :param _Name: 成员名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _MemberType: 成员类型，邀请：Invite， 创建：Create
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberType: str
        :param _OrgPolicyType: 关系策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyType: str
        :param _OrgPolicyName: 关系策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyName: str
        :param _OrgPermission: 关系策略权限
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPermission: list of OrgPermission
        :param _NodeId: 所属节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: int
        :param _NodeName: 所属节点名
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _IsAllowQuit: 是否允许成员退出。允许：Allow，不允许：Denied。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowQuit: str
        :param _PayUin: 代付者Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type PayUin: str
        :param _PayName: 代付者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param _OrgIdentity: 管理身份
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgIdentity: list of MemberIdentity
        :param _BindStatus: 安全信息绑定状态  未绑定：Unbound，待激活：Valid，绑定成功：Success，绑定失败：Failed
注意：此字段可能返回 null，表示取不到有效值。
        :type BindStatus: str
        :param _PermissionStatus: 成员权限状态 已确认：Confirmed ，待确认：UnConfirmed
注意：此字段可能返回 null，表示取不到有效值。
        :type PermissionStatus: str
        """
        self._MemberUin = None
        self._Name = None
        self._MemberType = None
        self._OrgPolicyType = None
        self._OrgPolicyName = None
        self._OrgPermission = None
        self._NodeId = None
        self._NodeName = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._PayName = None
        self._OrgIdentity = None
        self._BindStatus = None
        self._PermissionStatus = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberType(self):
        return self._MemberType

    @MemberType.setter
    def MemberType(self, MemberType):
        self._MemberType = MemberType

    @property
    def OrgPolicyType(self):
        return self._OrgPolicyType

    @OrgPolicyType.setter
    def OrgPolicyType(self, OrgPolicyType):
        self._OrgPolicyType = OrgPolicyType

    @property
    def OrgPolicyName(self):
        return self._OrgPolicyName

    @OrgPolicyName.setter
    def OrgPolicyName(self, OrgPolicyName):
        self._OrgPolicyName = OrgPolicyName

    @property
    def OrgPermission(self):
        return self._OrgPermission

    @OrgPermission.setter
    def OrgPermission(self, OrgPermission):
        self._OrgPermission = OrgPermission

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsAllowQuit(self):
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def PayName(self):
        return self._PayName

    @PayName.setter
    def PayName(self, PayName):
        self._PayName = PayName

    @property
    def OrgIdentity(self):
        return self._OrgIdentity

    @OrgIdentity.setter
    def OrgIdentity(self, OrgIdentity):
        self._OrgIdentity = OrgIdentity

    @property
    def BindStatus(self):
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def PermissionStatus(self):
        return self._PermissionStatus

    @PermissionStatus.setter
    def PermissionStatus(self, PermissionStatus):
        self._PermissionStatus = PermissionStatus


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Name = params.get("Name")
        self._MemberType = params.get("MemberType")
        self._OrgPolicyType = params.get("OrgPolicyType")
        self._OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self._OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self._OrgPermission.append(obj)
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._PayName = params.get("PayName")
        if params.get("OrgIdentity") is not None:
            self._OrgIdentity = []
            for item in params.get("OrgIdentity"):
                obj = MemberIdentity()
                obj._deserialize(item)
                self._OrgIdentity.append(obj)
        self._BindStatus = params.get("BindStatus")
        self._PermissionStatus = params.get("PermissionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthAccount(AbstractModel):
    """成员和子账号的授权关系

    """

    def __init__(self):
        r"""
        :param _OrgSubAccountUin: 组织子账号Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgSubAccountUin: int
        :param _PolicyId: 策略ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _PolicyName: 策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param _IdentityRoleName: 身份角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: 身份角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleAliasName: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _OrgSubAccountName: 子账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgSubAccountName: str
        """
        self._OrgSubAccountUin = None
        self._PolicyId = None
        self._PolicyName = None
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._OrgSubAccountName = None

    @property
    def OrgSubAccountUin(self):
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def OrgSubAccountName(self):
        return self._OrgSubAccountName

    @OrgSubAccountName.setter
    def OrgSubAccountName(self, OrgSubAccountName):
        self._OrgSubAccountName = OrgSubAccountName


    def _deserialize(self, params):
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._OrgSubAccountName = params.get("OrgSubAccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthIdentity(AbstractModel):
    """组织成员可授权的身份

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param _IdentityRoleName: 身份的角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: 身份的角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleAliasName: str
        :param _Description: 身份描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 首次配置成功的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 最后一次配置成功的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _IdentityType: 身份类型。取值： 1-预设身份  2-自定义身份
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityType: int
        :param _Status: 配置状态。取值：1-配置完成 2-需重新配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _MemberUin: 成员Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberUin: int
        :param _MemberName: 成员名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        """
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IdentityType = None
        self._Status = None
        self._MemberUin = None
        self._MemberName = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IdentityType(self):
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IdentityType = params.get("IdentityType")
        self._Status = params.get("Status")
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberFinancial(AbstractModel):
    """组织成员财务信息。

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberUin: int
        :param _MemberName: 成员名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        :param _TotalCost: 消耗金额，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: float
        :param _Ratio: 占比%。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ratio: str
        """
        self._MemberUin = None
        self._MemberName = None
        self._TotalCost = None
        self._Ratio = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Ratio(self):
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        self._TotalCost = params.get("TotalCost")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberPolicy(AbstractModel):
    """组织成员被授权的策略

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _PolicyName: 策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param _IdentityRoleName: 身份角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: 身份角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleAliasName: str
        :param _Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNode(AbstractModel):
    """企业组织单元

    """

    def __init__(self):
        r"""
        :param _NodeId: 组织节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: int
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ParentNodeId: 父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentNodeId: int
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._NodeId = None
        self._Name = None
        self._ParentNodeId = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentNodeId(self):
        return self._ParentNodeId

    @ParentNodeId.setter
    def ParentNodeId(self, ParentNodeId):
        self._ParentNodeId = ParentNodeId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._ParentNodeId = params.get("ParentNodeId")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgPermission(AbstractModel):
    """关系策略权限

    """

    def __init__(self):
        r"""
        :param _Id: 权限Id
        :type Id: int
        :param _Name: 权限名
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgProductFinancial(AbstractModel):
    """组织产品财务信息

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品Code。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _ProductCode: 产品名。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param _TotalCost: 产品消耗，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCost: float
        :param _Ratio: 占比%。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ratio: str
        """
        self._ProductName = None
        self._ProductCode = None
        self._TotalCost = None
        self._Ratio = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Ratio(self):
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._ProductCode = params.get("ProductCode")
        self._TotalCost = params.get("TotalCost")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuitOrganizationRequest(AbstractModel):
    """QuitOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID
        :type OrgId: int
        """
        self._OrgId = None

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuitOrganizationResponse(AbstractModel):
    """QuitOrganization返回参数结构体

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


class UpdateOrganizationIdentityRequest(AbstractModel):
    """UpdateOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID
        :type IdentityId: int
        :param _Description: 身份描述
        :type Description: str
        :param _IdentityPolicy: 身份策略
        :type IdentityPolicy: list of IdentityPolicy
        """
        self._IdentityId = None
        self._Description = None
        self._IdentityPolicy = None

    @property
    def IdentityId(self):
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IdentityPolicy(self):
        return self._IdentityPolicy

    @IdentityPolicy.setter
    def IdentityPolicy(self, IdentityPolicy):
        self._IdentityPolicy = IdentityPolicy


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        if params.get("IdentityPolicy") is not None:
            self._IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self._IdentityPolicy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationIdentityResponse(AbstractModel):
    """UpdateOrganizationIdentity返回参数结构体

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


class UpdateOrganizationMemberEmailBindRequest(AbstractModel):
    """UpdateOrganizationMemberEmailBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin
        :type MemberUin: int
        :param _BindId: 绑定ID
        :type BindId: int
        :param _Email: 邮箱
        :type Email: str
        :param _CountryCode: 国际区号
        :type CountryCode: str
        :param _Phone: 手机号
        :type Phone: str
        """
        self._MemberUin = None
        self._BindId = None
        self._Email = None
        self._CountryCode = None
        self._Phone = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def BindId(self):
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._BindId = params.get("BindId")
        self._Email = params.get("Email")
        self._CountryCode = params.get("CountryCode")
        self._Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationMemberEmailBindResponse(AbstractModel):
    """UpdateOrganizationMemberEmailBind返回参数结构体

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


class UpdateOrganizationMemberRequest(AbstractModel):
    """UpdateOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _Name: 成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type Name: str
        :param _Remark: 备注。最大长度为40个字符
        :type Remark: str
        :param _PolicyType: 关系策略类型。PolicyType不为空，PermissionIds不能为空。取值：Financial
        :type PolicyType: str
        :param _PermissionIds: 成员财务权限ID列表。PermissionIds不为空，PolicyType不能为空。
取值：1-查看账单、2-查看余额、3-资金划拨、4-合并出账、5-开票、6-优惠继承、7-代付费、8-成本分析，如果有值，1、2 默认必须
        :type PermissionIds: list of int non-negative
        :param _IsAllowQuit: 是否允许成员退出组织。取值：Allow-允许、Denied-不允许
        :type IsAllowQuit: str
        :param _PayUin: 代付者Uin。成员财务权限有代付费时需要，取值为成员对应主体的主体管理员Uin
        :type PayUin: str
        """
        self._MemberUin = None
        self._Name = None
        self._Remark = None
        self._PolicyType = None
        self._PermissionIds = None
        self._IsAllowQuit = None
        self._PayUin = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PermissionIds(self):
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds

    @property
    def IsAllowQuit(self):
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._PolicyType = params.get("PolicyType")
        self._PermissionIds = params.get("PermissionIds")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationMemberResponse(AbstractModel):
    """UpdateOrganizationMember返回参数结构体

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


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID。
        :type NodeId: int
        :param _Name: 节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :type Name: str
        :param _Remark: 备注。
        :type Remark: str
        """
        self._NodeId = None
        self._Name = None
        self._Remark = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationNodeResponse(AbstractModel):
    """UpdateOrganizationNode返回参数结构体

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