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
from tencentcloud.tsw.v20200924 import models
from typing import Dict


class TswClient(AbstractClient):
    _apiVersion = '2020-09-24'
    _endpoint = 'tsw.tencentcloudapi.com'
    _service = 'tsw'

    async def DescribeAgentShell(
            self,
            request: models.DescribeAgentShellRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentShellResponse:
        """
        获取服务接入信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentShell"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentShellResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)