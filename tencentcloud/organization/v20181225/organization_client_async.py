# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.organization.v20181225 import models
from typing import Dict


class OrganizationClient(AbstractClient):
    _apiVersion = '2018-12-25'
    _endpoint = 'organization.tencentcloudapi.com'
    _service = 'organization'

    async def AcceptOrganizationInvitation(
            self,
            request: models.AcceptOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.AcceptOrganizationInvitationResponse:
        """
        接受加入企业组织邀请
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOrganizationNode(
            self,
            request: models.AddOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.AddOrganizationNodeResponse:
        """
        添加企业组织单元
        """
        
        kwargs = {}
        kwargs["action"] = "AddOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelOrganizationInvitation(
            self,
            request: models.CancelOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.CancelOrganizationInvitationResponse:
        """
        取消企业组织邀请
        """
        
        kwargs = {}
        kwargs["action"] = "CancelOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrganization(
            self,
            request: models.CreateOrganizationRequest,
            opts: Dict = None,
    ) -> models.CreateOrganizationResponse:
        """
        创建企业组织
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganization(
            self,
            request: models.DeleteOrganizationRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationResponse:
        """
        删除企业组织
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMemberFromNode(
            self,
            request: models.DeleteOrganizationMemberFromNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMemberFromNodeResponse:
        """
        删除企业组织成员
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMemberFromNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMemberFromNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationMembers(
            self,
            request: models.DeleteOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationMembersResponse:
        """
        批量删除企业组织成员
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOrganizationNodes(
            self,
            request: models.DeleteOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.DeleteOrganizationNodesResponse:
        """
        批量删除企业组织单元
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DenyOrganizationInvitation(
            self,
            request: models.DenyOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.DenyOrganizationInvitationResponse:
        """
        拒绝企业组织邀请
        """
        
        kwargs = {}
        kwargs["action"] = "DenyOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DenyOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOrganization(
            self,
            request: models.GetOrganizationRequest,
            opts: Dict = None,
    ) -> models.GetOrganizationResponse:
        """
        获取企业组织信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOrganizationMember(
            self,
            request: models.GetOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.GetOrganizationMemberResponse:
        """
        获取企业组织成员
        """
        
        kwargs = {}
        kwargs["action"] = "GetOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationInvitations(
            self,
            request: models.ListOrganizationInvitationsRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationInvitationsResponse:
        """
        获取邀请信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationInvitations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationInvitationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationMembers(
            self,
            request: models.ListOrganizationMembersRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationMembersResponse:
        """
        获取企业组织成员列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationNodeMembers(
            self,
            request: models.ListOrganizationNodeMembersRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationNodeMembersResponse:
        """
        获取企业组织单元成员列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationNodeMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationNodeMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOrganizationNodes(
            self,
            request: models.ListOrganizationNodesRequest,
            opts: Dict = None,
    ) -> models.ListOrganizationNodesResponse:
        """
        获取企业组织单元列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOrganizationNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOrganizationNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveOrganizationMembersToNode(
            self,
            request: models.MoveOrganizationMembersToNodeRequest,
            opts: Dict = None,
    ) -> models.MoveOrganizationMembersToNodeResponse:
        """
        移动成员到指定企业组织单元
        """
        
        kwargs = {}
        kwargs["action"] = "MoveOrganizationMembersToNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveOrganizationMembersToNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuitOrganization(
            self,
            request: models.QuitOrganizationRequest,
            opts: Dict = None,
    ) -> models.QuitOrganizationResponse:
        """
        退出企业组织
        """
        
        kwargs = {}
        kwargs["action"] = "QuitOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuitOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendOrganizationInvitation(
            self,
            request: models.SendOrganizationInvitationRequest,
            opts: Dict = None,
    ) -> models.SendOrganizationInvitationResponse:
        """
        发送企业组织邀请
        """
        
        kwargs = {}
        kwargs["action"] = "SendOrganizationInvitation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendOrganizationInvitationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationMember(
            self,
            request: models.UpdateOrganizationMemberRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationMemberResponse:
        """
        更新企业成员信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOrganizationNode(
            self,
            request: models.UpdateOrganizationNodeRequest,
            opts: Dict = None,
    ) -> models.UpdateOrganizationNodeResponse:
        """
        更新企业组织单元
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOrganizationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOrganizationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)