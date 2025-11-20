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
from tencentcloud.bpaas.v20181217 import models
from typing import Dict


class BpaasClient(AbstractClient):
    _apiVersion = '2018-12-17'
    _endpoint = 'bpaas.tencentcloudapi.com'
    _service = 'bpaas'

    async def GetBpaasApproveDetail(
            self,
            request: models.GetBpaasApproveDetailRequest,
            opts: Dict = None,
    ) -> models.GetBpaasApproveDetailResponse:
        """
        查看审批详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetBpaasApproveDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetBpaasApproveDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OutApproveBpaasApplication(
            self,
            request: models.OutApproveBpaasApplicationRequest,
            opts: Dict = None,
    ) -> models.OutApproveBpaasApplicationResponse:
        """
        外部审批申请单
        """
        
        kwargs = {}
        kwargs["action"] = "OutApproveBpaasApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OutApproveBpaasApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)