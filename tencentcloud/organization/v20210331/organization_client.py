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


    def BindOrganizationMemberAuthAccount(self, request):
        """绑定组织成员和子账号的授权关系

        :param request: Request instance for BindOrganizationMemberAuthAccount.
        :type request: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.BindOrganizationMemberAuthAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindOrganizationMemberAuthAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindOrganizationMemberAuthAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOrganizationMember(self, request):
        """创建组织成员

        :param request: Request instance for CreateOrganizationMember.
        :type request: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.CreateOrganizationMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateOrganizationMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOrganizationMemberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrganization(self, request):
        """获取企业组织信息

        :param request: Request instance for DescribeOrganization.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOrganization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrganizationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrganizationMembers(self, request):
        """获取企业组织成员列表

        :param request: Request instance for DescribeOrganizationMembers.
        :type request: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersRequest`
        :rtype: :class:`tencentcloud.organization.v20210331.models.DescribeOrganizationMembersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOrganizationMembers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrganizationMembersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)