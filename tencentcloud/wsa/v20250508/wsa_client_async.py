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
from tencentcloud.wsa.v20250508 import models
from typing import Dict


class WsaClient(AbstractClient):
    _apiVersion = '2025-05-08'
    _endpoint = 'wsa.tencentcloudapi.com'
    _service = 'wsa'

    async def SearchPro(
            self,
            request: models.SearchProRequest,
            opts: Dict = None,
    ) -> models.SearchProResponse:
        """
        联网搜索API，以JSON形式向客户提供搜索结果数据，包含标题、摘要、内容来源url等信息
        """
        
        kwargs = {}
        kwargs["action"] = "SearchPro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)