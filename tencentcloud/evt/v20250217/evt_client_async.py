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
from tencentcloud.evt.v20250217 import models
from typing import Dict


class EvtClient(AbstractClient):
    _apiVersion = '2025-02-17'
    _endpoint = 'evt.tencentcloudapi.com'
    _service = 'evt'

    async def CompleteApproval(
            self,
            request: models.CompleteApprovalRequest,
            opts: Dict = None,
    ) -> models.CompleteApprovalResponse:
        """
        执行审批
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteApproval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteApprovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoleUser(
            self,
            request: models.CreateRoleUserRequest,
            opts: Dict = None,
    ) -> models.CreateRoleUserResponse:
        """
        创建人员
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoleUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoleUser(
            self,
            request: models.DeleteRoleUserRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleUserResponse:
        """
        删除自定义用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoleUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutMessage(
            self,
            request: models.PutMessageRequest,
            opts: Dict = None,
    ) -> models.PutMessageResponse:
        """
        推送事件数据
        """
        
        kwargs = {}
        kwargs["action"] = "PutMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)