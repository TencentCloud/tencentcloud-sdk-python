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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.organization.v20181225 import models


class OrganizationClient(AbstractClient):
    _apiVersion = '2018-12-25'
    _endpoint = 'organization.tencentcloudapi.com'
    _service = 'organization'


    def AcceptOrganizationInvitation(self, request):
        r"""接受加入企业组织邀请

        :param request: Request instance for AcceptOrganizationInvitation.
        :type request: :class:`tencentcloud.organization.v20181225.models.AcceptOrganizationInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.AcceptOrganizationInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptOrganizationInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptOrganizationInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOrganizationNode(self, request):
        r"""添加企业组织单元

        :param request: Request instance for AddOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20181225.models.AddOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.AddOrganizationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganizationNode", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelOrganizationInvitation(self, request):
        r"""取消企业组织邀请

        :param request: Request instance for CancelOrganizationInvitation.
        :type request: :class:`tencentcloud.organization.v20181225.models.CancelOrganizationInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.CancelOrganizationInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelOrganizationInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.CancelOrganizationInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganization(self, request):
        r"""创建企业组织

        :param request: Request instance for CreateOrganization.
        :type request: :class:`tencentcloud.organization.v20181225.models.CreateOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.CreateOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganization(self, request):
        r"""删除企业组织

        :param request: Request instance for DeleteOrganization.
        :type request: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMemberFromNode(self, request):
        r"""删除企业组织成员

        :param request: Request instance for DeleteOrganizationMemberFromNode.
        :type request: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationMemberFromNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationMemberFromNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMemberFromNode", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMemberFromNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMembers(self, request):
        r"""批量删除企业组织成员

        :param request: Request instance for DeleteOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationNodes(self, request):
        r"""批量删除企业组织单元

        :param request: Request instance for DeleteOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.DeleteOrganizationNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DenyOrganizationInvitation(self, request):
        r"""拒绝企业组织邀请

        :param request: Request instance for DenyOrganizationInvitation.
        :type request: :class:`tencentcloud.organization.v20181225.models.DenyOrganizationInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.DenyOrganizationInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DenyOrganizationInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.DenyOrganizationInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOrganization(self, request):
        r"""获取企业组织信息

        :param request: Request instance for GetOrganization.
        :type request: :class:`tencentcloud.organization.v20181225.models.GetOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.GetOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.GetOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOrganizationMember(self, request):
        r"""获取企业组织成员

        :param request: Request instance for GetOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20181225.models.GetOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.GetOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.GetOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationInvitations(self, request):
        r"""获取邀请信息列表

        :param request: Request instance for ListOrganizationInvitations.
        :type request: :class:`tencentcloud.organization.v20181225.models.ListOrganizationInvitationsRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.ListOrganizationInvitationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationInvitations", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationInvitationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationMembers(self, request):
        r"""获取企业组织成员列表

        :param request: Request instance for ListOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20181225.models.ListOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.ListOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationMembers", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationNodeMembers(self, request):
        r"""获取企业组织单元成员列表

        :param request: Request instance for ListOrganizationNodeMembers.
        :type request: :class:`tencentcloud.organization.v20181225.models.ListOrganizationNodeMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.ListOrganizationNodeMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationNodeMembers", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationNodeMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationNodes(self, request):
        r"""获取企业组织单元列表

        :param request: Request instance for ListOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20181225.models.ListOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.ListOrganizationNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationNodes", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MoveOrganizationMembersToNode(self, request):
        r"""移动成员到指定企业组织单元

        :param request: Request instance for MoveOrganizationMembersToNode.
        :type request: :class:`tencentcloud.organization.v20181225.models.MoveOrganizationMembersToNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.MoveOrganizationMembersToNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MoveOrganizationMembersToNode", params, headers=headers)
            response = json.loads(body)
            model = models.MoveOrganizationMembersToNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QuitOrganization(self, request):
        r"""退出企业组织

        :param request: Request instance for QuitOrganization.
        :type request: :class:`tencentcloud.organization.v20181225.models.QuitOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.QuitOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QuitOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.QuitOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendOrganizationInvitation(self, request):
        r"""发送企业组织邀请

        :param request: Request instance for SendOrganizationInvitation.
        :type request: :class:`tencentcloud.organization.v20181225.models.SendOrganizationInvitationRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.SendOrganizationInvitationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendOrganizationInvitation", params, headers=headers)
            response = json.loads(body)
            model = models.SendOrganizationInvitationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationMember(self, request):
        r"""更新企业成员信息

        :param request: Request instance for UpdateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20181225.models.UpdateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.UpdateOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationNode(self, request):
        r"""更新企业组织单元

        :param request: Request instance for UpdateOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20181225.models.UpdateOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20181225.models.UpdateOrganizationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationNode", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))