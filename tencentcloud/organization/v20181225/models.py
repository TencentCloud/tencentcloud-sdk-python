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


class AcceptOrganizationInvitationRequest(AbstractModel):
    """AcceptOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 邀请ID\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptOrganizationInvitationResponse(AbstractModel):
    """AcceptOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode请求参数结构体

    """

    def __init__(self):
        """
        :param ParentNodeId: 父组织单元ID\n        :type ParentNodeId: int\n        :param Name: 组织单元名字\n        :type Name: str\n        """
        self.ParentNodeId = None
        self.Name = None


    def _deserialize(self, params):
        self.ParentNodeId = params.get("ParentNodeId")
        self.Name = params.get("Name")
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
        """
        :param NodeId: 组织单元ID\n        :type NodeId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.RequestId = params.get("RequestId")


class CancelOrganizationInvitationRequest(AbstractModel):
    """CancelOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 邀请ID\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationInvitationResponse(AbstractModel):
    """CancelOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOrganizationRequest(AbstractModel):
    """CreateOrganization请求参数结构体

    """

    def __init__(self):
        """
        :param OrgType: 组织类型（目前固定为1）\n        :type OrgType: int\n        """
        self.OrgType = None


    def _deserialize(self, params):
        self.OrgType = params.get("OrgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationResponse(AbstractModel):
    """CreateOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param OrgId: 企业组织ID\n        :type OrgId: int\n        :param Nickname: 创建者昵称\n        :type Nickname: str\n        :param Mail: 创建者邮箱\n        :type Mail: str\n        :param OrgType: 组织类型\n        :type OrgType: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OrgId = None
        self.Nickname = None
        self.Mail = None
        self.OrgType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.Nickname = params.get("Nickname")
        self.Mail = params.get("Mail")
        self.OrgType = params.get("OrgType")
        self.RequestId = params.get("RequestId")


class DeleteOrganizationMemberFromNodeRequest(AbstractModel):
    """DeleteOrganizationMemberFromNode请求参数结构体

    """

    def __init__(self):
        """
        :param MemberUin: 被删除成员UIN\n        :type MemberUin: int\n        :param NodeId: 组织单元ID\n        :type NodeId: int\n        """
        self.MemberUin = None
        self.NodeId = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMemberFromNodeResponse(AbstractModel):
    """DeleteOrganizationMemberFromNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers请求参数结构体

    """

    def __init__(self):
        """
        :param Uins: 被删除成员的UIN列表\n        :type Uins: list of int non-negative\n        """
        self.Uins = None


    def _deserialize(self, params):
        self.Uins = params.get("Uins")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes请求参数结构体

    """

    def __init__(self):
        """
        :param NodeIds: 组织单元ID列表\n        :type NodeIds: list of int non-negative\n        """
        self.NodeIds = None


    def _deserialize(self, params):
        self.NodeIds = params.get("NodeIds")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationRequest(AbstractModel):
    """DeleteOrganization请求参数结构体

    """


class DeleteOrganizationResponse(AbstractModel):
    """DeleteOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DenyOrganizationInvitationRequest(AbstractModel):
    """DenyOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 邀请ID\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DenyOrganizationInvitationResponse(AbstractModel):
    """DenyOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetOrganizationMemberRequest(AbstractModel):
    """GetOrganizationMember请求参数结构体

    """

    def __init__(self):
        """
        :param MemberUin: 组织成员UIN\n        :type MemberUin: int\n        """
        self.MemberUin = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOrganizationMemberResponse(AbstractModel):
    """GetOrganizationMember返回参数结构体

    """

    def __init__(self):
        """
        :param Uin: 组织成员UIN\n        :type Uin: int\n        :param Name: 组织成员名称\n        :type Name: str\n        :param Remark: 备注\n        :type Remark: str\n        :param JoinTime: 加入时间\n        :type JoinTime: str\n        :param NodeId: 组织单元ID\n        :type NodeId: int\n        :param NodeName: 组织单元名称\n        :type NodeName: str\n        :param ParentNodeId: 父组织单元ID\n        :type ParentNodeId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Uin = None
        self.Name = None
        self.Remark = None
        self.JoinTime = None
        self.NodeId = None
        self.NodeName = None
        self.ParentNodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.JoinTime = params.get("JoinTime")
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        self.ParentNodeId = params.get("ParentNodeId")
        self.RequestId = params.get("RequestId")


class GetOrganizationRequest(AbstractModel):
    """GetOrganization请求参数结构体

    """


class GetOrganizationResponse(AbstractModel):
    """GetOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param OrgId: 企业组织ID\n        :type OrgId: int\n        :param HostUin: 创建者UIN\n        :type HostUin: int\n        :param Nickname: 创建者昵称\n        :type Nickname: str\n        :param Mail: 创建者邮箱\n        :type Mail: str\n        :param OrgType: 企业组织类型\n        :type OrgType: int\n        :param IsEmpty: 是否为空\n        :type IsEmpty: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OrgId = None
        self.HostUin = None
        self.Nickname = None
        self.Mail = None
        self.OrgType = None
        self.IsEmpty = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.HostUin = params.get("HostUin")
        self.Nickname = params.get("Nickname")
        self.Mail = params.get("Mail")
        self.OrgType = params.get("OrgType")
        self.IsEmpty = params.get("IsEmpty")
        self.RequestId = params.get("RequestId")


class ListOrganizationInvitationsRequest(AbstractModel):
    """ListOrganizationInvitations请求参数结构体

    """

    def __init__(self):
        """
        :param Invited: 是否被邀请。1：被邀请，0：发出的邀请\n        :type Invited: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        """
        self.Invited = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Invited = params.get("Invited")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationInvitationsResponse(AbstractModel):
    """ListOrganizationInvitations返回参数结构体

    """

    def __init__(self):
        """
        :param Invitations: 邀请信息列表\n        :type Invitations: list of OrgInvitation\n        :param TotalCount: 总数目\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Invitations = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Invitations") is not None:
            self.Invitations = []
            for item in params.get("Invitations"):
                obj = OrgInvitation()
                obj._deserialize(item)
                self.Invitations.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListOrganizationMembersRequest(AbstractModel):
    """ListOrganizationMembers请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        """
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
        


class ListOrganizationMembersResponse(AbstractModel):
    """ListOrganizationMembers返回参数结构体

    """

    def __init__(self):
        """
        :param Members: 成员列表\n        :type Members: list of OrgMember\n        :param TotalCount: 总数目\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Members = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListOrganizationNodeMembersRequest(AbstractModel):
    """ListOrganizationNodeMembers请求参数结构体

    """

    def __init__(self):
        """
        :param NodeId: 企业组织单元ID\n        :type NodeId: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限制数目\n        :type Limit: int\n        """
        self.NodeId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationNodeMembersResponse(AbstractModel):
    """ListOrganizationNodeMembers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数目\n        :type TotalCount: int\n        :param Members: 成员列表\n        :type Members: list of OrgMember\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Members = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.RequestId = params.get("RequestId")


class ListOrganizationNodesRequest(AbstractModel):
    """ListOrganizationNodes请求参数结构体

    """


class ListOrganizationNodesResponse(AbstractModel):
    """ListOrganizationNodes返回参数结构体

    """

    def __init__(self):
        """
        :param Nodes: 企业组织单元列表\n        :type Nodes: list of OrgNode\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Nodes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = OrgNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.RequestId = params.get("RequestId")


class MoveOrganizationMembersToNodeRequest(AbstractModel):
    """MoveOrganizationMembersToNode请求参数结构体

    """

    def __init__(self):
        """
        :param NodeId: 组织单元ID\n        :type NodeId: int\n        :param Uins: 成员UIN列表\n        :type Uins: list of int non-negative\n        """
        self.NodeId = None
        self.Uins = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationMembersToNodeResponse(AbstractModel):
    """MoveOrganizationMembersToNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrgInvitation(AbstractModel):
    """企业组织邀请

    """

    def __init__(self):
        """
        :param Id: 邀请ID\n        :type Id: int\n        :param Uin: 被邀请UIN\n        :type Uin: int\n        :param HostUin: 创建者UIN\n        :type HostUin: int\n        :param HostName: 创建者名称\n        :type HostName: str\n        :param HostMail: 创建者邮箱\n        :type HostMail: str\n        :param Status: 邀请状态。-1：已过期，0：正常，1：已接受，2：已失效，3：已取消\n        :type Status: int\n        :param Name: 名称\n        :type Name: str\n        :param Remark: 备注\n        :type Remark: str\n        :param OrgType: 企业组织类型\n        :type OrgType: int\n        :param InviteTime: 邀请时间\n        :type InviteTime: str\n        :param ExpireTime: 过期时间\n        :type ExpireTime: str\n        """
        self.Id = None
        self.Uin = None
        self.HostUin = None
        self.HostName = None
        self.HostMail = None
        self.Status = None
        self.Name = None
        self.Remark = None
        self.OrgType = None
        self.InviteTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uin = params.get("Uin")
        self.HostUin = params.get("HostUin")
        self.HostName = params.get("HostName")
        self.HostMail = params.get("HostMail")
        self.Status = params.get("Status")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.OrgType = params.get("OrgType")
        self.InviteTime = params.get("InviteTime")
        self.ExpireTime = params.get("ExpireTime")
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
        """
        :param Uin: UIN\n        :type Uin: int\n        :param Name: 名称\n        :type Name: str\n        :param Remark: 备注\n        :type Remark: str\n        :param JoinTime: 加入时间\n        :type JoinTime: str\n        """
        self.Uin = None
        self.Name = None
        self.Remark = None
        self.JoinTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.JoinTime = params.get("JoinTime")
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
        """
        :param NodeId: 组织单元ID\n        :type NodeId: int\n        :param Name: 名称\n        :type Name: str\n        :param ParentNodeId: 父单元ID\n        :type ParentNodeId: int\n        :param MemberCount: 成员数量\n        :type MemberCount: int\n        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None
        self.MemberCount = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")
        self.MemberCount = params.get("MemberCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuitOrganizationRequest(AbstractModel):
    """QuitOrganization请求参数结构体

    """

    def __init__(self):
        """
        :param OrgId: 企业组织ID\n        :type OrgId: int\n        """
        self.OrgId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuitOrganizationResponse(AbstractModel):
    """QuitOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendOrganizationInvitationRequest(AbstractModel):
    """SendOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param InviteUin: 被邀请账户UIN\n        :type InviteUin: int\n        :param Name: 名称\n        :type Name: str\n        :param Remark: 备注\n        :type Remark: str\n        """
        self.InviteUin = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.InviteUin = params.get("InviteUin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendOrganizationInvitationResponse(AbstractModel):
    """SendOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOrganizationMemberRequest(AbstractModel):
    """UpdateOrganizationMember请求参数结构体

    """

    def __init__(self):
        """
        :param MemberUin: 成员UIN\n        :type MemberUin: int\n        :param Name: 名称\n        :type Name: str\n        :param Remark: 备注\n        :type Remark: str\n        """
        self.MemberUin = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationMemberResponse(AbstractModel):
    """UpdateOrganizationMember返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode请求参数结构体

    """

    def __init__(self):
        """
        :param NodeId: 企业组织单元ID\n        :type NodeId: int\n        :param Name: 名称\n        :type Name: str\n        :param ParentNodeId: 父单元ID\n        :type ParentNodeId: int\n        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")