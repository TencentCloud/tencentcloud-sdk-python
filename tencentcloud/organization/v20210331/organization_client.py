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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.organization.v20210331 import models


class OrganizationClient(AbstractClient):
    _apiVersion = '2021-03-31'
    _endpoint = 'organization.tencentcloudapi.com'
    _service = 'organization'


    def AddOrganizationMemberEmail(self, request):
        """添加组织成员邮箱

        :param request: Request instance for AddOrganizationMemberEmail.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddOrganizationMemberEmailRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddOrganizationMemberEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOrganizationMemberEmail", params, headers=headers)
            response = json.loads(body)
            model = models.AddOrganizationMemberEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOrganizationNode(self, request):
        """添加企业组织节点

        :param request: Request instance for AddOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.AddOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.AddOrganizationNodeResponse`

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


    def BindOrganizationMemberAuthAccount(self, request):
        """绑定组织成员和组织管理员子账号的授权关系

        :param request: Request instance for BindOrganizationMemberAuthAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindOrganizationMemberAuthAccount", params, headers=headers)
            response = json.loads(body)
            model = models.BindOrganizationMemberAuthAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelOrganizationMemberAuthAccount(self, request):
        """取消组织成员和组织管理员子账号的授权关系

        :param request: Request instance for CancelOrganizationMemberAuthAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.CancelOrganizationMemberAuthAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CancelOrganizationMemberAuthAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelOrganizationMemberAuthAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CancelOrganizationMemberAuthAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMember(self, request):
        """创建组织成员

        :param request: Request instance for CreateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMember", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMemberAuthIdentity(self, request):
        """添加组织成员访问授权

        :param request: Request instance for CreateOrganizationMemberAuthIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberAuthIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberAuthIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMemberAuthIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberAuthIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrganizationMemberPolicy(self, request):
        """创建组织成员访问授权策略

        :param request: Request instance for CreateOrganizationMemberPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrganizationMemberPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrganizationMemberPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMemberAuthIdentity(self, request):
        """删除组织成员访问授权

        :param request: Request instance for DeleteOrganizationMemberAuthIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMemberAuthIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMemberAuthIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMemberAuthIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMemberAuthIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationMembers(self, request):
        """批量删除企业组织成员

        :param request: Request instance for DeleteOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersResponse`

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


    def DeleteOrganizationMembersPolicy(self, request):
        """删除组织成员访问策略

        :param request: Request instance for DeleteOrganizationMembersPolicy.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersPolicyRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationMembersPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOrganizationMembersPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOrganizationMembersPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOrganizationNodes(self, request):
        """批量删除企业组织节点

        :param request: Request instance for DeleteOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DeleteOrganizationNodesResponse`

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


    def DescribeOrganization(self, request):
        """获取企业组织信息

        :param request: Request instance for DescribeOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationAuthNode(self, request):
        """获取已设置管理员的互信主体关系列表

        :param request: Request instance for DescribeOrganizationAuthNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationAuthNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationAuthNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationAuthNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationAuthNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationFinancialByMember(self, request):
        """以成员维度获取组织财务信息

        :param request: Request instance for DescribeOrganizationFinancialByMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationFinancialByMember", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationFinancialByMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationFinancialByMonth(self, request):
        """以月维度获取组织财务信息趋势

        :param request: Request instance for DescribeOrganizationFinancialByMonth.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMonthRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByMonthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationFinancialByMonth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationFinancialByMonthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationFinancialByProduct(self, request):
        """以产品维度获取组织财务信息

        :param request: Request instance for DescribeOrganizationFinancialByProduct.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByProductRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationFinancialByProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationFinancialByProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationFinancialByProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberAuthAccounts(self, request):
        """获取组织成员被绑定授权关系的子账号列表

        :param request: Request instance for DescribeOrganizationMemberAuthAccounts.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthAccountsRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberAuthAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberAuthAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberAuthIdentities(self, request):
        """获取组织成员可被管理的身份列表

        :param request: Request instance for DescribeOrganizationMemberAuthIdentities.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthIdentitiesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberAuthIdentitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberAuthIdentities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberAuthIdentitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberEmailBind(self, request):
        """查询成员邮箱绑定详细信息

        :param request: Request instance for DescribeOrganizationMemberEmailBind.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberEmailBindRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberEmailBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberEmailBind", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberEmailBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMemberPolicies(self, request):
        """获取组织成员的授权策略列表

        :param request: Request instance for DescribeOrganizationMemberPolicies.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberPoliciesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMemberPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMemberPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMemberPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationMembers(self, request):
        """获取企业组织成员列表

        :param request: Request instance for DescribeOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationNodes(self, request):
        """获取组织节点列表

        :param request: Request instance for DescribeOrganizationNodes.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationNodesRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListOrganizationIdentity(self, request):
        """获取组织成员访问身份列表

        :param request: Request instance for ListOrganizationIdentity.
        :type request: :class:`tencentcloud.organization.v20210331.models.ListOrganizationIdentityRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.ListOrganizationIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListOrganizationIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.ListOrganizationIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MoveOrganizationNodeMembers(self, request):
        """移动成员到指定企业组织节点

        :param request: Request instance for MoveOrganizationNodeMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.MoveOrganizationNodeMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.MoveOrganizationNodeMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MoveOrganizationNodeMembers", params, headers=headers)
            response = json.loads(body)
            model = models.MoveOrganizationNodeMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationMember(self, request):
        """更新组织成员信息

        :param request: Request instance for UpdateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberResponse`

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


    def UpdateOrganizationMemberEmailBind(self, request):
        """修改绑定成员邮箱

        :param request: Request instance for UpdateOrganizationMemberEmailBind.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberEmailBindRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationMemberEmailBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateOrganizationMemberEmailBind", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateOrganizationMemberEmailBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateOrganizationNode(self, request):
        """更新企业组织节点

        :param request: Request instance for UpdateOrganizationNode.
        :type request: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationNodeRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.UpdateOrganizationNodeResponse`

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