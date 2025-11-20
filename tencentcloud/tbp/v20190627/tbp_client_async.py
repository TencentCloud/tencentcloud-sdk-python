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
from tencentcloud.tbp.v20190627 import models
from typing import Dict


class TbpClient(AbstractClient):
    _apiVersion = '2019-06-27'
    _endpoint = 'tbp.tencentcloudapi.com'
    _service = 'tbp'

    async def TextProcess(
            self,
            request: models.TextProcessRequest,
            opts: Dict = None,
    ) -> models.TextProcessResponse:
        """
        接收调用侧的文本输入，返回应答文本。
        """
        
        kwargs = {}
        kwargs["action"] = "TextProcess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextProcessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextReset(
            self,
            request: models.TextResetRequest,
            opts: Dict = None,
    ) -> models.TextResetResponse:
        """
        会话重置接口。
        """
        
        kwargs = {}
        kwargs["action"] = "TextReset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextResetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)