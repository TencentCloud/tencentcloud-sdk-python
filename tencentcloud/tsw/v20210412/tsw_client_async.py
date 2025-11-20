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
from tencentcloud.tsw.v20210412 import models
from typing import Dict


class TswClient(AbstractClient):
    _apiVersion = '2021-04-12'
    _endpoint = 'tsw.tencentcloudapi.com'
    _service = 'tsw'

    async def DescribeComponentAlertObject(
            self,
            request: models.DescribeComponentAlertObjectRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentAlertObjectResponse:
        """
        获取告警对象-组件告警
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponentAlertObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentAlertObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceAlertObject(
            self,
            request: models.DescribeServiceAlertObjectRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceAlertObjectResponse:
        """
        获取告警对象-服务告警表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceAlertObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceAlertObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeToken(
            self,
            request: models.DescribeTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenResponse:
        """
        查询token
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)