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
from tencentcloud.ig.v20210518 import models
from typing import Dict


class IgClient(AbstractClient):
    _apiVersion = '2021-05-18'
    _endpoint = 'ig.tencentcloudapi.com'
    _service = 'ig'

    async def DescribeIgOrderList(
            self,
            request: models.DescribeIgOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeIgOrderListResponse:
        """
        查询智能导诊订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)