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
from tencentcloud.icr.v20211014 import models
from typing import Dict


class IcrClient(AbstractClient):
    _apiVersion = '2021-10-14'
    _endpoint = 'icr.tencentcloudapi.com'
    _service = 'icr'

    async def GetIndustryV1HomeMembers(
            self,
            request: models.GetIndustryV1HomeMembersRequest,
            opts: Dict = None,
    ) -> models.GetIndustryV1HomeMembersResponse:
        """
        获取成员列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetIndustryV1HomeMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetIndustryV1HomeMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)