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
        r"""
        :param _Id: 邀请ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptOrganizationInvitationResponse(AbstractModel):
    """AcceptOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ParentNodeId: 父组织单元ID
        :type ParentNodeId: int
        :param _Name: 组织单元名字
        :type Name: str
        """
        self._ParentNodeId = None
        self._Name = None

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


    def _deserialize(self, params):
        self._ParentNodeId = params.get("ParentNodeId")
        self._Name = params.get("Name")
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
        :param _NodeId: 组织单元ID
        :type NodeId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CancelOrganizationInvitationRequest(AbstractModel):
    """CancelOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 邀请ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationInvitationResponse(AbstractModel):
    """CancelOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateOrganizationRequest(AbstractModel):
    """CreateOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgType: 组织类型（目前固定为1）
        :type OrgType: int
        """
        self._OrgType = None

    @property
    def OrgType(self):
        return self._OrgType

    @OrgType.setter
    def OrgType(self, OrgType):
        self._OrgType = OrgType


    def _deserialize(self, params):
        self._OrgType = params.get("OrgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationResponse(AbstractModel):
    """CreateOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID
        :type OrgId: int
        :param _Nickname: 创建者昵称
        :type Nickname: str
        :param _Mail: 创建者邮箱
        :type Mail: str
        :param _OrgType: 组织类型
        :type OrgType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgId = None
        self._Nickname = None
        self._Mail = None
        self._OrgType = None
        self._RequestId = None

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def OrgType(self):
        return self._OrgType

    @OrgType.setter
    def OrgType(self, OrgType):
        self._OrgType = OrgType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._Nickname = params.get("Nickname")
        self._Mail = params.get("Mail")
        self._OrgType = params.get("OrgType")
        self._RequestId = params.get("RequestId")


class DeleteOrganizationMemberFromNodeRequest(AbstractModel):
    """DeleteOrganizationMemberFromNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 被删除成员UIN
        :type MemberUin: int
        :param _NodeId: 组织单元ID
        :type NodeId: int
        """
        self._MemberUin = None
        self._NodeId = None

    @property
    def MemberUin(self):
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMemberFromNodeResponse(AbstractModel):
    """DeleteOrganizationMemberFromNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Uins: 被删除成员的UIN列表
        :type Uins: list of int non-negative
        """
        self._Uins = None

    @property
    def Uins(self):
        return self._Uins

    @Uins.setter
    def Uins(self, Uins):
        self._Uins = Uins


    def _deserialize(self, params):
        self._Uins = params.get("Uins")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _NodeIds: 组织单元ID列表
        :type NodeIds: list of int non-negative
        """
        self._NodeIds = None

    @property
    def NodeIds(self):
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds


    def _deserialize(self, params):
        self._NodeIds = params.get("NodeIds")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DenyOrganizationInvitationRequest(AbstractModel):
    """DenyOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 邀请ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DenyOrganizationInvitationResponse(AbstractModel):
    """DenyOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class GetOrganizationMemberRequest(AbstractModel):
    """GetOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 组织成员UIN
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
        


class GetOrganizationMemberResponse(AbstractModel):
    """GetOrganizationMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 组织成员UIN
        :type Uin: int
        :param _Name: 组织成员名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        :param _JoinTime: 加入时间
        :type JoinTime: str
        :param _NodeId: 组织单元ID
        :type NodeId: int
        :param _NodeName: 组织单元名称
        :type NodeName: str
        :param _ParentNodeId: 父组织单元ID
        :type ParentNodeId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._Name = None
        self._Remark = None
        self._JoinTime = None
        self._NodeId = None
        self._NodeName = None
        self._ParentNodeId = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
    def JoinTime(self):
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime

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
    def ParentNodeId(self):
        return self._ParentNodeId

    @ParentNodeId.setter
    def ParentNodeId(self, ParentNodeId):
        self._ParentNodeId = ParentNodeId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._JoinTime = params.get("JoinTime")
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        self._ParentNodeId = params.get("ParentNodeId")
        self._RequestId = params.get("RequestId")


class GetOrganizationRequest(AbstractModel):
    """GetOrganization请求参数结构体

    """


class GetOrganizationResponse(AbstractModel):
    """GetOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID
        :type OrgId: int
        :param _HostUin: 创建者UIN
        :type HostUin: int
        :param _Nickname: 创建者昵称
        :type Nickname: str
        :param _Mail: 创建者邮箱
        :type Mail: str
        :param _OrgType: 企业组织类型
        :type OrgType: int
        :param _IsEmpty: 是否为空
        :type IsEmpty: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgId = None
        self._HostUin = None
        self._Nickname = None
        self._Mail = None
        self._OrgType = None
        self._IsEmpty = None
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
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def OrgType(self):
        return self._OrgType

    @OrgType.setter
    def OrgType(self, OrgType):
        self._OrgType = OrgType

    @property
    def IsEmpty(self):
        return self._IsEmpty

    @IsEmpty.setter
    def IsEmpty(self, IsEmpty):
        self._IsEmpty = IsEmpty

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._HostUin = params.get("HostUin")
        self._Nickname = params.get("Nickname")
        self._Mail = params.get("Mail")
        self._OrgType = params.get("OrgType")
        self._IsEmpty = params.get("IsEmpty")
        self._RequestId = params.get("RequestId")


class ListOrganizationInvitationsRequest(AbstractModel):
    """ListOrganizationInvitations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Invited: 是否被邀请。1：被邀请，0：发出的邀请
        :type Invited: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        """
        self._Invited = None
        self._Offset = None
        self._Limit = None

    @property
    def Invited(self):
        return self._Invited

    @Invited.setter
    def Invited(self, Invited):
        self._Invited = Invited

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


    def _deserialize(self, params):
        self._Invited = params.get("Invited")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationInvitationsResponse(AbstractModel):
    """ListOrganizationInvitations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Invitations: 邀请信息列表
        :type Invitations: list of OrgInvitation
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Invitations = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Invitations(self):
        return self._Invitations

    @Invitations.setter
    def Invitations(self, Invitations):
        self._Invitations = Invitations

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
        if params.get("Invitations") is not None:
            self._Invitations = []
            for item in params.get("Invitations"):
                obj = OrgInvitation()
                obj._deserialize(item)
                self._Invitations.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListOrganizationMembersRequest(AbstractModel):
    """ListOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationMembersResponse(AbstractModel):
    """ListOrganizationMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Members: 成员列表
        :type Members: list of OrgMember
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Members = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Members(self):
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

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
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self._Members.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListOrganizationNodeMembersRequest(AbstractModel):
    """ListOrganizationNodeMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 企业组织单元ID
        :type NodeId: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        """
        self._NodeId = None
        self._Offset = None
        self._Limit = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

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


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationNodeMembersResponse(AbstractModel):
    """ListOrganizationNodeMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _Members: 成员列表
        :type Members: list of OrgMember
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Members = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Members(self):
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self._Members.append(obj)
        self._RequestId = params.get("RequestId")


class ListOrganizationNodesRequest(AbstractModel):
    """ListOrganizationNodes请求参数结构体

    """


class ListOrganizationNodesResponse(AbstractModel):
    """ListOrganizationNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Nodes: 企业组织单元列表
        :type Nodes: list of OrgNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Nodes = None
        self._RequestId = None

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = OrgNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._RequestId = params.get("RequestId")


class MoveOrganizationMembersToNodeRequest(AbstractModel):
    """MoveOrganizationMembersToNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 组织单元ID
        :type NodeId: int
        :param _Uins: 成员UIN列表
        :type Uins: list of int non-negative
        """
        self._NodeId = None
        self._Uins = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Uins(self):
        return self._Uins

    @Uins.setter
    def Uins(self, Uins):
        self._Uins = Uins


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationMembersToNodeResponse(AbstractModel):
    """MoveOrganizationMembersToNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class OrgInvitation(AbstractModel):
    """企业组织邀请

    """

    def __init__(self):
        r"""
        :param _Id: 邀请ID
        :type Id: int
        :param _Uin: 被邀请UIN
        :type Uin: int
        :param _HostUin: 创建者UIN
        :type HostUin: int
        :param _HostName: 创建者名称
        :type HostName: str
        :param _HostMail: 创建者邮箱
        :type HostMail: str
        :param _Status: 邀请状态。-1：已过期，0：正常，1：已接受，2：已失效，3：已取消
        :type Status: int
        :param _Name: 名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        :param _OrgType: 企业组织类型
        :type OrgType: int
        :param _InviteTime: 邀请时间
        :type InviteTime: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        """
        self._Id = None
        self._Uin = None
        self._HostUin = None
        self._HostName = None
        self._HostMail = None
        self._Status = None
        self._Name = None
        self._Remark = None
        self._OrgType = None
        self._InviteTime = None
        self._ExpireTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def HostUin(self):
        return self._HostUin

    @HostUin.setter
    def HostUin(self, HostUin):
        self._HostUin = HostUin

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def HostMail(self):
        return self._HostMail

    @HostMail.setter
    def HostMail(self, HostMail):
        self._HostMail = HostMail

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def OrgType(self):
        return self._OrgType

    @OrgType.setter
    def OrgType(self, OrgType):
        self._OrgType = OrgType

    @property
    def InviteTime(self):
        return self._InviteTime

    @InviteTime.setter
    def InviteTime(self, InviteTime):
        self._InviteTime = InviteTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Uin = params.get("Uin")
        self._HostUin = params.get("HostUin")
        self._HostName = params.get("HostName")
        self._HostMail = params.get("HostMail")
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._OrgType = params.get("OrgType")
        self._InviteTime = params.get("InviteTime")
        self._ExpireTime = params.get("ExpireTime")
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
        :param _Uin: UIN
        :type Uin: int
        :param _Name: 名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        :param _JoinTime: 加入时间
        :type JoinTime: str
        """
        self._Uin = None
        self._Name = None
        self._Remark = None
        self._JoinTime = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
    def JoinTime(self):
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._JoinTime = params.get("JoinTime")
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
        :param _NodeId: 组织单元ID
        :type NodeId: int
        :param _Name: 名称
        :type Name: str
        :param _ParentNodeId: 父单元ID
        :type ParentNodeId: int
        :param _MemberCount: 成员数量
        :type MemberCount: int
        """
        self._NodeId = None
        self._Name = None
        self._ParentNodeId = None
        self._MemberCount = None

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
    def MemberCount(self):
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._ParentNodeId = params.get("ParentNodeId")
        self._MemberCount = params.get("MemberCount")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class SendOrganizationInvitationRequest(AbstractModel):
    """SendOrganizationInvitation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InviteUin: 被邀请账户UIN
        :type InviteUin: int
        :param _Name: 名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._InviteUin = None
        self._Name = None
        self._Remark = None

    @property
    def InviteUin(self):
        return self._InviteUin

    @InviteUin.setter
    def InviteUin(self, InviteUin):
        self._InviteUin = InviteUin

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
        self._InviteUin = params.get("InviteUin")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendOrganizationInvitationResponse(AbstractModel):
    """SendOrganizationInvitation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _MemberUin: 成员UIN
        :type MemberUin: int
        :param _Name: 名称
        :type Name: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._MemberUin = None
        self._Name = None
        self._Remark = None

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


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _NodeId: 企业组织单元ID
        :type NodeId: int
        :param _Name: 名称
        :type Name: str
        :param _ParentNodeId: 父单元ID
        :type ParentNodeId: int
        """
        self._NodeId = None
        self._Name = None
        self._ParentNodeId = None

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


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._ParentNodeId = params.get("ParentNodeId")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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