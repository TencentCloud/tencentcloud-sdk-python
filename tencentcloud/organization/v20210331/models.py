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


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param ParentNodeId: 父节点ID。可以调用DescribeOrganizationNodes获取
        :type ParentNodeId: int
        :param Name: 节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :type Name: str
        :param Remark: 备注。
        :type Remark: str
        """
        self.ParentNodeId = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.ParentNodeId = params.get("ParentNodeId")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationNodeResponse(AbstractModel):
    """AddOrganizationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID。
        :type NodeId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.RequestId = params.get("RequestId")


class AuthNode(AbstractModel):
    """互信主体主要信息

    """

    def __init__(self):
        r"""
        :param RelationId: 互信主体关系ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationId: int
        :param AuthName: 互信主体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthName: str
        :param Manager: 主体管理员
注意：此字段可能返回 null，表示取不到有效值。
        :type Manager: :class:`tencentcloud.organization.v20210331.models.MemberMainInfo`
        """
        self.RelationId = None
        self.AuthName = None
        self.Manager = None


    def _deserialize(self, params):
        self.RelationId = params.get("RelationId")
        self.AuthName = params.get("AuthName")
        if params.get("Manager") is not None:
            self.Manager = MemberMainInfo()
            self.Manager._deserialize(params.get("Manager"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountRequest(AbstractModel):
    """BindOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param MemberUin: 成员Uin。
        :type MemberUin: int
        :param PolicyId: 策略ID。可以调用DescribeOrganizationMemberPolicies获取
        :type PolicyId: int
        :param OrgSubAccountUins: 组织管理员子账号Uin列表。最大5个
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


class CancelOrganizationMemberAuthAccountRequest(AbstractModel):
    """CancelOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param MemberUin: 成员Uin。
        :type MemberUin: int
        :param PolicyId: 策略ID。
        :type PolicyId: int
        :param OrgSubAccountUin: 组织子账号Uin。
        :type OrgSubAccountUin: int
        """
        self.MemberUin = None
        self.PolicyId = None
        self.OrgSubAccountUin = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.PolicyId = params.get("PolicyId")
        self.OrgSubAccountUin = params.get("OrgSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationMemberAuthAccountResponse(AbstractModel):
    """CancelOrganizationMemberAuthAccount返回参数结构体

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
        :param PolicyName: 策略名。最大长度为128个字符，支持英文字母、数字、符号+=,.@_-
        :type PolicyName: str
        :param IdentityId: 成员访问身份ID。可以调用DescribeOrganizationMemberAuthIdentities获取
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
        :param Name: 成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type Name: str
        :param PolicyType: 关系策略。取值：Financial
        :type PolicyType: str
        :param PermissionIds: 成员财务权限ID列表。取值：1-查看账单、2-查看余额、3-资金划拨、4-合并出账、5-开票、6-优惠继承、7-代付费，1、2 默认必须
        :type PermissionIds: list of int non-negative
        :param NodeId: 成员所属部门的节点ID。可以调用DescribeOrganizationNodes获取
        :type NodeId: int
        :param AccountName: 账号名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type AccountName: str
        :param Remark: 备注。
        :type Remark: str
        :param RecordId: 成员创建记录ID。创建异常重试时需要
        :type RecordId: int
        :param PayUin: 代付者Uin。成员代付费时需要
        :type PayUin: str
        :param IdentityRoleID: 成员访问身份ID列表。可以调用ListOrganizationIdentity获取，1默认支持
        :type IdentityRoleID: list of int non-negative
        :param AuthRelationId: 认证主体关系ID。给不同主体创建成员时需要，可以调用DescribeOrganizationAuthNode获取
        :type AuthRelationId: int
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
        self.AuthRelationId = None


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
        self.AuthRelationId = params.get("AuthRelationId")
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
        :param Uin: 成员Uin。
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


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param MemberUin: 被删除成员的UIN列表。
        :type MemberUin: list of int
        """
        self.MemberUin = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMembersResponse(AbstractModel):
    """DeleteOrganizationMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID列表。
        :type NodeId: list of int
        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationNodesResponse(AbstractModel):
    """DeleteOrganizationNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOrganizationAuthNodeRequest(AbstractModel):
    """DescribeOrganizationAuthNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 限制数目。最大50
        :type Limit: int
        :param AuthName: 互信主体名称。
        :type AuthName: str
        """
        self.Offset = None
        self.Limit = None
        self.AuthName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AuthName = params.get("AuthName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationAuthNodeResponse(AbstractModel):
    """DescribeOrganizationAuthNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Items: 条目详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuthNode
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = AuthNode()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthAccountsRequest(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 限制数目。
        :type Limit: int
        :param MemberUin: 成员Uin。
        :type MemberUin: int
        :param PolicyId: 策略ID。
        :type PolicyId: int
        """
        self.Offset = None
        self.Limit = None
        self.MemberUin = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MemberUin = params.get("MemberUin")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthAccountsResponse(AbstractModel):
    """DescribeOrganizationMemberAuthAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMemberAuthAccount
        :param Total: 总数目
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = OrgMemberAuthAccount()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthIdentitiesRequest(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param MemberUin: 组织成员Uin。
        :type MemberUin: int
        """
        self.Offset = None
        self.Limit = None
        self.MemberUin = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthIdentitiesResponse(AbstractModel):
    """DescribeOrganizationMemberAuthIdentities返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 授权身份列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMemberAuthIdentity
        :param Total: 总数目。
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = OrgMemberAuthIdentity()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMemberPoliciesRequest(AbstractModel):
    """DescribeOrganizationMemberPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 限制数目。最大50
        :type Limit: int
        :param MemberUin: 成员Uin。
        :type MemberUin: int
        :param SearchKey: 搜索关键字。可用于策略名或描述搜索
        :type SearchKey: str
        """
        self.Offset = None
        self.Limit = None
        self.MemberUin = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MemberUin = params.get("MemberUin")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberPoliciesResponse(AbstractModel):
    """DescribeOrganizationMemberPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMemberPolicy
        :param Total: 总数目。
注意：此字段可能返回 null，表示取不到有效值。
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
                obj = OrgMemberPolicy()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOrganizationMembersRequest(AbstractModel):
    """DescribeOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param SearchKey: 成员名称或者成员ID搜索。
        :type SearchKey: str
        :param AuthName: 主体名称搜索。
        :type AuthName: str
        :param Product: 可信服务产品简称。可信服务管理员查询时必须指定
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
        :param Items: 成员列表。
        :type Items: list of OrgMember
        :param Total: 总数目。
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


class DescribeOrganizationNodesRequest(AbstractModel):
    """DescribeOrganizationNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 限制数目。最大50
        :type Limit: int
        :param Offset: 偏移量。
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
        


class DescribeOrganizationNodesResponse(AbstractModel):
    """DescribeOrganizationNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Items: 列表详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgNode
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgNode()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrganizationRequest(AbstractModel):
    """DescribeOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param Product: 可信服务产品简称。查询是否该可信服务管理员时必须指定
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
        :param OrgId: 企业组织ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgId: int
        :param HostUin: 创建者UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostUin: int
        :param NickName: 创建者昵称。
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param OrgType: 企业组织类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgType: int
        :param IsManager: 是否组织管理员。是：true ，否：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsManager: bool
        :param OrgPolicyType: 策略类型。财务管理：Financial
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyType: str
        :param OrgPolicyName: 策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPolicyName: str
        :param OrgPermission: 成员财务权限列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgPermission: list of OrgPermission
        :param RootNodeId: 组织根节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RootNodeId: int
        :param CreateTime: 组织创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param JoinTime: 成员加入时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTime: str
        :param IsAllowQuit: 成员是否允许退出。允许：Allow，不允许：Denied
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowQuit: str
        :param PayUin: 代付者Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayUin: str
        :param PayName: 代付者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param IsAssignManager: 是否可信服务管理员。是：true，否：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssignManager: bool
        :param IsAuthManager: 是否实名主体管理员。是：true，否：false
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


class IdentityPolicy(AbstractModel):
    """组织身份策略

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param PolicyName: 策略名称
        :type PolicyName: str
        """
        self.PolicyId = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityRequest(AbstractModel):
    """ListOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 限制数目。最大50
        :type Limit: int
        :param SearchKey: 名称搜索关键字。
        :type SearchKey: str
        :param IdentityId: 身份ID搜索。
        :type IdentityId: int
        """
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.IdentityId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityResponse(AbstractModel):
    """ListOrganizationIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Items: 条目详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgIdentity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrgIdentity()
                obj._deserialize(item)
                self.Items.append(obj)
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
        


class MemberMainInfo(AbstractModel):
    """成员主要信息

    """

    def __init__(self):
        r"""
        :param MemberUin: 成员uin
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberUin: int
        :param MemberName: 成员名称j
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        """
        self.MemberUin = None
        self.MemberName = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.MemberName = params.get("MemberName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersRequest(AbstractModel):
    """MoveOrganizationNodeMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeId: 组织节点ID。
        :type NodeId: int
        :param MemberUin: 成员UIN列表。
        :type MemberUin: list of int
        """
        self.NodeId = None
        self.MemberUin = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersResponse(AbstractModel):
    """MoveOrganizationNodeMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrgIdentity(AbstractModel):
    """组织身份

    """

    def __init__(self):
        r"""
        :param IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param IdentityAliasName: 身份名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityAliasName: str
        :param Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param IdentityPolicy: 身份策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityPolicy: list of IdentityPolicy
        :param IdentityType: 身份类型。 1-预设、 2-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityType: int
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.IdentityId = None
        self.IdentityAliasName = None
        self.Description = None
        self.IdentityPolicy = None
        self.IdentityType = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.IdentityId = params.get("IdentityId")
        self.IdentityAliasName = params.get("IdentityAliasName")
        self.Description = params.get("Description")
        if params.get("IdentityPolicy") is not None:
            self.IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self.IdentityPolicy.append(obj)
        self.IdentityType = params.get("IdentityType")
        self.UpdateTime = params.get("UpdateTime")
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
        


class OrgMemberAuthAccount(AbstractModel):
    """成员和子账号的授权关系

    """

    def __init__(self):
        r"""
        :param OrgSubAccountUin: 组织子账号Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgSubAccountUin: int
        :param PolicyId: 策略ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param PolicyName: 策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param IdentityRoleName: 身份角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleName: str
        :param IdentityRoleAliasName: 身份角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleAliasName: str
        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param OrgSubAccountName: 子账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgSubAccountName: str
        """
        self.OrgSubAccountUin = None
        self.PolicyId = None
        self.PolicyName = None
        self.IdentityId = None
        self.IdentityRoleName = None
        self.IdentityRoleAliasName = None
        self.CreateTime = None
        self.UpdateTime = None
        self.OrgSubAccountName = None


    def _deserialize(self, params):
        self.OrgSubAccountUin = params.get("OrgSubAccountUin")
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.IdentityId = params.get("IdentityId")
        self.IdentityRoleName = params.get("IdentityRoleName")
        self.IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.OrgSubAccountName = params.get("OrgSubAccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthIdentity(AbstractModel):
    """组织成员可授权的身份

    """

    def __init__(self):
        r"""
        :param IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param IdentityRoleName: 身份的角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleName: str
        :param IdentityRoleAliasName: 身份的角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleAliasName: str
        :param Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param IdentityType: 身份类型。取值： 1-预设  2-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityType: int
        """
        self.IdentityId = None
        self.IdentityRoleName = None
        self.IdentityRoleAliasName = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.IdentityType = None


    def _deserialize(self, params):
        self.IdentityId = params.get("IdentityId")
        self.IdentityRoleName = params.get("IdentityRoleName")
        self.IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.IdentityType = params.get("IdentityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberPolicy(AbstractModel):
    """组织成员被授权的策略

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param PolicyName: 策略名。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param IdentityId: 身份ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param IdentityRoleName: 身份角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleName: str
        :param IdentityRoleAliasName: 身份角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleAliasName: str
        :param Description: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.IdentityId = None
        self.IdentityRoleName = None
        self.IdentityRoleAliasName = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.IdentityId = params.get("IdentityId")
        self.IdentityRoleName = params.get("IdentityRoleName")
        self.IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNode(AbstractModel):
    """企业组织单元

    """

    def __init__(self):
        r"""
        :param NodeId: 组织节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: int
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param ParentNodeId: 父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentNodeId: int
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
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
        


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID。
        :type NodeId: int
        :param Name: 节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :type Name: str
        :param Remark: 备注。
        :type Remark: str
        """
        self.NodeId = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationNodeResponse(AbstractModel):
    """UpdateOrganizationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")