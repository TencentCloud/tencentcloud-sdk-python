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
from tencentcloud.mall.v20230518 import models
from typing import Dict


class MallClient(AbstractClient):
    _apiVersion = '2023-05-18'
    _endpoint = 'mall.tencentcloudapi.com'
    _service = 'mall'

    async def DescribeDrawResourceList(
            self,
            request: models.DescribeDrawResourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDrawResourceListResponse:
        """
        依据客户的Uin查询开通的资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDrawResourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDrawResourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)