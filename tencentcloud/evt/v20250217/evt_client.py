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
from tencentcloud.evt.v20250217 import models


class EvtClient(AbstractClient):
    _apiVersion = '2025-02-17'
    _endpoint = 'evt.tencentcloudapi.com'
    _service = 'evt'


    def CompleteApproval(self, request):
        r"""执行审批

        :param request: Request instance for CompleteApproval.
        :type request: :class:`tencentcloud.evt.v20250217.models.CompleteApprovalRequest`
        :rtype: :class:`tencentcloud.evt.v20250217.models.CompleteApprovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteApproval", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteApprovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoleUser(self, request):
        r"""创建人员

        :param request: Request instance for CreateRoleUser.
        :type request: :class:`tencentcloud.evt.v20250217.models.CreateRoleUserRequest`
        :rtype: :class:`tencentcloud.evt.v20250217.models.CreateRoleUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoleUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoleUser(self, request):
        r"""删除自定义用户

        :param request: Request instance for DeleteRoleUser.
        :type request: :class:`tencentcloud.evt.v20250217.models.DeleteRoleUserRequest`
        :rtype: :class:`tencentcloud.evt.v20250217.models.DeleteRoleUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoleUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutMessage(self, request):
        r"""推送事件数据

        :param request: Request instance for PutMessage.
        :type request: :class:`tencentcloud.evt.v20250217.models.PutMessageRequest`
        :rtype: :class:`tencentcloud.evt.v20250217.models.PutMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutMessage", params, headers=headers)
            response = json.loads(body)
            model = models.PutMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))