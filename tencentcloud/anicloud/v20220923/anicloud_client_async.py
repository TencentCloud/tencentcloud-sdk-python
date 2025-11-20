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
from tencentcloud.anicloud.v20220923 import models
from typing import Dict


class AnicloudClient(AbstractClient):
    _apiVersion = '2022-09-23'
    _endpoint = 'anicloud.tencentcloudapi.com'
    _service = 'anicloud'

    async def CheckAppidExist(
            self,
            request: models.CheckAppidExistRequest,
            opts: Dict = None,
    ) -> models.CheckAppidExistResponse:
        """
        查看appid是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAppidExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAppidExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryResource(
            self,
            request: models.QueryResourceRequest,
            opts: Dict = None,
    ) -> models.QueryResourceResponse:
        """
        查询购买资源
        """
        
        kwargs = {}
        kwargs["action"] = "QueryResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryResourceInfo(
            self,
            request: models.QueryResourceInfoRequest,
            opts: Dict = None,
    ) -> models.QueryResourceInfoResponse:
        """
        查询资源信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryResourceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryResourceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)