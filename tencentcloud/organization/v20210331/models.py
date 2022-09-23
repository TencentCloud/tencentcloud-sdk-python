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


class BindOrganizationMemberAuthAccountRequest(AbstractModel):
    """BindOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param MemberUin: 成员Uin。
        :type MemberUin: int
        :param PolicyId: 策略ID。
        :type PolicyId: int
        :param OrgSubAccountUins: 组织子账号Uin。
        :type OrgSubAccountUins: list of int
        """
        self.MemberUin = None
        self.PolicyId = None
        self.OrgSubAccountUins = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.PolicyId = params.get("PolicyId")
        self.OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountResponse(AbstractModel):
    """BindOrganizationMemberAuthAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOrganizationMemberPolicyRequest(AbstractModel):
    """CreateOrganizationMemberPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param MemberUin: 成员Uin。
        :type MemberUin: int
        :param PolicyName: 策略名。
        :type PolicyName: str
        :param IdentityId: 身份ID。
        :type IdentityId: int
        :param Description: 描述。
        :type Description: str
        """
        self.MemberUin = None
        self.PolicyName = None
        self.IdentityId = None
        self.Description = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.PolicyName = params.get("PolicyName")
        self.IdentityId = params.get("IdentityId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberPolicyResponse(AbstractModel):
    """CreateOrganizationMemberPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID。
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


class CreateOrganizationMemberRequest(AbstractModel):
    """CreateOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param PolicyType: 关系策略  取值：Financial
        :type PolicyType: str
        :param PermissionIds: 关系权限 取值：1-查看账单、2-查看余额、3-资金划拨、4-合并出账、5-开票 ，1、2 默认必须
        :type PermissionIds: list of int non-negative
        :param NodeId: 成员所属部门的节点ID
        :type NodeId: int
        :param AccountName: 账号名
        :type AccountName: str
        :param Remark: 备注
        :type Remark: str
        :param RecordId: 重试创建传记录ID
        :type RecordId: int
        :param PayUin: 代付者Uin
        :type PayUin: str
        :param IdentityRoleID: 管理身份
        :type IdentityRoleID: list of int non-negative
        """
        self.Name = None
        self.PolicyType = None
        self.PermissionIds = None
        self.NodeId = None
        self.AccountName = None
        self.Remark = None
        self.RecordId = None
        self.PayUin = None
        self.IdentityRoleID = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.PolicyType = params.get("PolicyType")
        self.PermissionIds = params.get("PermissionIds")
        self.NodeId = params.get("NodeId")
        self.AccountName = params.get("AccountName")
        self.Remark = params.get("Remark")
        self.RecordId = params.get("RecordId")
        self.PayUin = params.get("PayUin")
        self.IdentityRoleID = params.get("IdentityRoleID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberResponse(AbstractModel):
    """CreateOrganizationMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param Uin: 成员Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMembersRequest(AbstractModel):
    """DescribeOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param SearchKey: 成员名或者成员ID搜索
        :type SearchKey: str
        :param AuthName: 主体名称
        :type AuthName: str
        :param Product: 集团服务（服务管理员查询时，必须指定）
        :type Product: str
        """
        self.Offset = None
        self.Limit = None
        self.Lang = None
        self.SearchKey = None
        self.AuthName = None
        self.Product = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Lang = params.get("Lang")
        self.SearchKey = params.get("SearchKey")
        self.AuthName = params.get("AuthName")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMembersResponse(AbstractModel):
    """DescribeOrganizationMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 成员列表
        :type Items: list of OrgMember
        :param Total: 总数目
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationRequest(AbstractModel):
    """DescribeOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param Product: 产品简称（查询是否集团服务委派管理员必填）
        :type Product: str
        """
        self.Lang = None
        self.Product = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationResponse(AbstractModel):
    """DescribeOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param OrgId: 企业组织ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgId: int
        :param HostUin: 创建者UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type HostUin: int
        :param NickName: 创建者昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param OrgType: 企业组织类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgType: int
        :param IsManager: 组织管理员：true，组织成员：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsManager: bool
        :param OrgPolicyType: 策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyType: str
        :param OrgPolicyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyName: str
        :param OrgPermission: 策略权限
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPermission: list of OrgPermission
        :param RootNodeId: 根节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RootNodeId: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param JoinTime: 成员加入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTime: str
        :param IsAllowQuit: 是否允许退出。允许：Allow，不允许：Denied。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowQuit: str
        :param PayUin: 代付者Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type PayUin: str
        :param PayName: 代付者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param IsAssignManager: 是否集团服务委派管理员 true-是、false-否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssignManager: bool
        :param IsAuthManager: 是否主体管理员 true-是、false-否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAuthManager: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrgId = None
        self.HostUin = None
        self.NickName = None
        self.OrgType = None
        self.IsManager = None
        self.OrgPolicyType = None
        self.OrgPolicyName = None
        self.OrgPermission = None
        self.RootNodeId = None
        self.CreateTime = None
        self.JoinTime = None
        self.IsAllowQuit = None
        self.PayUin = None
        self.PayName = None
        self.IsAssignManager = None
        self.IsAuthManager = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.HostUin = params.get("HostUin")
        self.NickName = params.get("NickName")
        self.OrgType = params.get("OrgType")
        self.IsManager = params.get("IsManager")
        self.OrgPolicyType = params.get("OrgPolicyType")
        self.OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self.OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self.OrgPermission.append(obj)
        self.RootNodeId = params.get("RootNodeId")
        self.CreateTime = params.get("CreateTime")
        self.JoinTime = params.get("JoinTime")
        self.IsAllowQuit = params.get("IsAllowQuit")
        self.PayUin = params.get("PayUin")
        self.PayName = params.get("PayName")
        self.IsAssignManager = params.get("IsAssignManager")
        self.IsAuthManager = params.get("IsAuthManager")
        self.RequestId = params.get("RequestId")


class MemberIdentity(AbstractModel):
    """成员管理身份

    """

    def __init__(self):
        r"""
        :param IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param IdentityAliasName: 身份名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityAliasName: str
        """
        self.IdentityId = None
        self.IdentityAliasName = None


    def _deserialize(self, params):
        self.IdentityId = params.get("IdentityId")
        self.IdentityAliasName = params.get("IdentityAliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMember(AbstractModel):
    """企业组织成员

    """

    def __init__(self):
        r"""
        :param MemberUin: 成员Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberUin: int
        :param Name: 成员名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param MemberType: 成员类型，邀请：Invite， 创建：Create
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberType: str
        :param OrgPolicyType: 关系策略类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyType: str
        :param OrgPolicyName: 关系策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyName: str
        :param OrgPermission: 关系策略权限
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPermission: list of OrgPermission
        :param NodeId: 所属节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: int
        :param NodeName: 所属节点名
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param IsAllowQuit: 是否允许成员退出。允许：Allow，不允许：Denied。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowQuit: str
        :param PayUin: 代付者Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type PayUin: str
        :param PayName: 代付者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param OrgIdentity: 管理身份
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgIdentity: list of MemberIdentity
        :param BindStatus: 安全信息绑定状态  未绑定：Unbound，待激活：Valid，绑定成功：Success，绑定失败：Failed
注意：此字段可能返回 null，表示取不到有效值。
        :type BindStatus: str
        :param PermissionStatus: 成员权限状态 已确认：Confirmed ，待确认：UnConfirmed
注意：此字段可能返回 null，表示取不到有效值。
        :type PermissionStatus: str
        """
        self.MemberUin = None
        self.Name = None
        self.MemberType = None
        self.OrgPolicyType = None
        self.OrgPolicyName = None
        self.OrgPermission = None
        self.NodeId = None
        self.NodeName = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None
        self.IsAllowQuit = None
        self.PayUin = None
        self.PayName = None
        self.OrgIdentity = None
        self.BindStatus = None
        self.PermissionStatus = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.Name = params.get("Name")
        self.MemberType = params.get("MemberType")
        self.OrgPolicyType = params.get("OrgPolicyType")
        self.OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self.OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self.OrgPermission.append(obj)
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.IsAllowQuit = params.get("IsAllowQuit")
        self.PayUin = params.get("PayUin")
        self.PayName = params.get("PayName")
        if params.get("OrgIdentity") is not None:
            self.OrgIdentity = []
            for item in params.get("OrgIdentity"):
                obj = MemberIdentity()
                obj._deserialize(item)
                self.OrgIdentity.append(obj)
        self.BindStatus = params.get("BindStatus")
        self.PermissionStatus = params.get("PermissionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgPermission(AbstractModel):
    """关系策略权限

    """

    def __init__(self):
        r"""
        :param Id: 权限Id
        :type Id: int
        :param Name: 权限名
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        