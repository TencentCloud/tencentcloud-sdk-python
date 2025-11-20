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
from tencentcloud.yunsou.v20191115 import models
from typing import Dict


class YunsouClient(AbstractClient):
    _apiVersion = '2019-11-15'
    _endpoint = 'yunsou.tencentcloudapi.com'
    _service = 'yunsou'

    async def DataManipulation(
            self,
            request: models.DataManipulationRequest,
            opts: Dict = None,
    ) -> models.DataManipulationResponse:
        """
        上传云搜数据的API接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DataManipulation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DataManipulationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DataSearch(
            self,
            request: models.DataSearchRequest,
            opts: Dict = None,
    ) -> models.DataSearchResponse:
        """
        用于检索云搜中的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DataSearch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DataSearchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)