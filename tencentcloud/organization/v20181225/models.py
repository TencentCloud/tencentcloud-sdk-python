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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AcceptOrganizationInvitationRequest(AbstractModel):
    """AcceptOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 邀请ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AcceptOrganizationInvitationResponse(AbstractModel):
    """AcceptOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode请求参数结构体

    """

    def __init__(self):
        """
        :param ParentNodeId: 父组织单元ID
        :type ParentNodeId: int
        :param Name: 组织单元名字
        :type Name: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddOrganizationNodeResponse(AbstractModel):
    """AddOrganizationNode返回参数结构体

    """

    def __init__(self):
        """
        :param NodeId: 组织单元ID
        :type NodeId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelOrganizationInvitationRequest(AbstractModel):
    """CancelOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 邀请ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelOrganizationInvitationResponse(AbstractModel):
    """CancelOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateOrganizationRequest(AbstractModel):
    """CreateOrganization请求参数结构体

    """

    def __init__(self):
        """
        :param OrgType: 组织类型（目前固定为1）
        :type OrgType: int
        """
        self.OrgType = None


    def _deserialize(self, params):
        self.OrgType = params.get("OrgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateOrganizationResponse(AbstractModel):
    """CreateOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param OrgId: 企业组织ID
        :type OrgId: int
        :param Nickname: 创建者昵称
        :type Nickname: str
        :param Mail: 创建者邮箱
        :type Mail: str
        :param OrgType: 组织类型
        :type OrgType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMemberFromNodeRequest(AbstractModel):
    """DeleteOrganizationMemberFromNode请求参数结构体

    """

    def __init__(self):
        """
        :param MemberUin: 被删除成员UIN
        :type MemberUin: int
        :param NodeId: 组织单元ID
        :type NodeId: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMemberFromNodeResponse(AbstractModel):
    """DeleteOrganizationMemberFromNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers请求参数结构体

    """

    def __init__(self):
        """
        :param Uins: 被删除成员的UIN列表
        :type Uins: list of int non-negative
        """
        self.Uins = None


    def _deserialize(self, params):
        self.Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationMembersResponse(AbstractModel):
    """DeleteOrganizationMembers返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes请求参数结构体

    """

    def __init__(self):
        """
        :param NodeIds: 组织单元ID列表
        :type NodeIds: list of int non-negative
        """
        self.NodeIds = None


    def _deserialize(self, params):
        self.NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationNodesResponse(AbstractModel):
    """DeleteOrganizationNodes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteOrganizationRequest(AbstractModel):
    """DeleteOrganization请求参数结构体

    """


class DeleteOrganizationResponse(AbstractModel):
    """DeleteOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DenyOrganizationInvitationRequest(AbstractModel):
    """DenyOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 邀请ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DenyOrganizationInvitationResponse(AbstractModel):
    """DenyOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetOrganizationMemberRequest(AbstractModel):
    """GetOrganizationMember请求参数结构体

    """

    def __init__(self):
        """
        :param MemberUin: 组织成员UIN
        :type MemberUin: int
        """
        self.MemberUin = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetOrganizationMemberResponse(AbstractModel):
    """GetOrganizationMember返回参数结构体

    """

    def __init__(self):
        """
        :param Uin: 组织成员UIN
        :type Uin: int
        :param Name: 组织成员名称
        :type Name: str
        :param Remark: 备注
        :type Remark: str
        :param JoinTime: 加入时间
        :type JoinTime: str
        :param NodeId: 组织单元ID
        :type NodeId: int
        :param NodeName: 组织单元名称
        :type NodeName: str
        :param ParentNodeId: 父组织单元ID
        :type ParentNodeId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetOrganizationRequest(AbstractModel):
    """GetOrganization请求参数结构体

    """


class GetOrganizationResponse(AbstractModel):
    """GetOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param OrgId: 企业组织ID
        :type OrgId: int
        :param HostUin: 创建者UIN
        :type HostUin: int
        :param Nickname: 创建者昵称
        :type Nickname: str
        :param Mail: 创建者邮箱
        :type Mail: str
        :param OrgType: 企业组织类型
        :type OrgType: int
        :param IsEmpty: 是否为空
        :type IsEmpty: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationInvitationsRequest(AbstractModel):
    """ListOrganizationInvitations请求参数结构体

    """

    def __init__(self):
        """
        :param Invited: 是否被邀请。1：被邀请，0：发出的邀请
        :type Invited: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationInvitationsResponse(AbstractModel):
    """ListOrganizationInvitations返回参数结构体

    """

    def __init__(self):
        """
        :param Invitations: 邀请信息列表
        :type Invitations: list of OrgInvitation
        :param TotalCount: 总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationMembersRequest(AbstractModel):
    """ListOrganizationMembers请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationMembersResponse(AbstractModel):
    """ListOrganizationMembers返回参数结构体

    """

    def __init__(self):
        """
        :param Members: 成员列表
        :type Members: list of OrgMember
        :param TotalCount: 总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationNodeMembersRequest(AbstractModel):
    """ListOrganizationNodeMembers请求参数结构体

    """

    def __init__(self):
        """
        :param NodeId: 企业组织单元ID
        :type NodeId: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationNodeMembersResponse(AbstractModel):
    """ListOrganizationNodeMembers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数目
        :type TotalCount: int
        :param Members: 成员列表
        :type Members: list of OrgMember
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListOrganizationNodesRequest(AbstractModel):
    """ListOrganizationNodes请求参数结构体

    """


class ListOrganizationNodesResponse(AbstractModel):
    """ListOrganizationNodes返回参数结构体

    """

    def __init__(self):
        """
        :param Nodes: 企业组织单元列表
        :type Nodes: list of OrgNode
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MoveOrganizationMembersToNodeRequest(AbstractModel):
    """MoveOrganizationMembersToNode请求参数结构体

    """

    def __init__(self):
        """
        :param NodeId: 组织单元ID
        :type NodeId: int
        :param Uins: 成员UIN列表
        :type Uins: list of int non-negative
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MoveOrganizationMembersToNodeResponse(AbstractModel):
    """MoveOrganizationMembersToNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OrgInvitation(AbstractModel):
    """企业组织邀请

    """

    def __init__(self):
        """
        :param Id: 邀请ID
        :type Id: int
        :param Uin: 被邀请UIN
        :type Uin: int
        :param HostUin: 创建者UIN
        :type HostUin: int
        :param HostName: 创建者名称
        :type HostName: str
        :param HostMail: 创建者邮箱
        :type HostMail: str
        :param Status: 邀请状态。-1：已过期，0：正常，1：已接受，2：已失效，3：已取消
        :type Status: int
        :param Name: 名称
        :type Name: str
        :param Remark: 备注
        :type Remark: str
        :param OrgType: 企业组织类型
        :type OrgType: int
        :param InviteTime: 邀请时间
        :type InviteTime: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OrgMember(AbstractModel):
    """企业组织成员

    """

    def __init__(self):
        """
        :param Uin: UIN
        :type Uin: int
        :param Name: 名称
        :type Name: str
        :param Remark: 备注
        :type Remark: str
        :param JoinTime: 加入时间
        :type JoinTime: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OrgNode(AbstractModel):
    """企业组织单元

    """

    def __init__(self):
        """
        :param NodeId: 组织单元ID
        :type NodeId: int
        :param Name: 名称
        :type Name: str
        :param ParentNodeId: 父单元ID
        :type ParentNodeId: int
        :param MemberCount: 成员数量
        :type MemberCount: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QuitOrganizationRequest(AbstractModel):
    """QuitOrganization请求参数结构体

    """

    def __init__(self):
        """
        :param OrgId: 企业组织ID
        :type OrgId: int
        """
        self.OrgId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QuitOrganizationResponse(AbstractModel):
    """QuitOrganization返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendOrganizationInvitationRequest(AbstractModel):
    """SendOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        """
        :param InviteUin: 被邀请账户UIN
        :type InviteUin: int
        :param Name: 名称
        :type Name: str
        :param Remark: 备注
        :type Remark: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendOrganizationInvitationResponse(AbstractModel):
    """SendOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationMemberRequest(AbstractModel):
    """UpdateOrganizationMember请求参数结构体

    """

    def __init__(self):
        """
        :param MemberUin: 成员UIN
        :type MemberUin: int
        :param Name: 名称
        :type Name: str
        :param Remark: 备注
        :type Remark: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationMemberResponse(AbstractModel):
    """UpdateOrganizationMember返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode请求参数结构体

    """

    def __init__(self):
        """
        :param NodeId: 企业组织单元ID
        :type NodeId: int
        :param Name: 名称
        :type Name: str
        :param ParentNodeId: 父单元ID
        :type ParentNodeId: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateOrganizationNodeResponse(AbstractModel):
    """UpdateOrganizationNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        