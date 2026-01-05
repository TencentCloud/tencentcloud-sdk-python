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
from tencentcloud.wimgs.v20251106 import models
from typing import Dict


class WimgsClient(AbstractClient):
    _apiVersion = '2025-11-06'
    _endpoint = 'wimgs.tencentcloudapi.com'
    _service = 'wimgs'

    async def SearchByText(
            self,
            request: models.SearchByTextRequest,
            opts: Dict = None,
    ) -> models.SearchByTextResponse:
        """
        文搜图接口，本服务将针对您输入的搜索关键词，检索并以JSON形式返回相关图片的标题、宽高、缩略图、内容来源url等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchByText"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchByTextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)