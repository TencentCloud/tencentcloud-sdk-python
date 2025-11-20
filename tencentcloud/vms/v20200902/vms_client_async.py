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
from tencentcloud.vms.v20200902 import models
from typing import Dict


class VmsClient(AbstractClient):
    _apiVersion = '2020-09-02'
    _endpoint = 'vms.tencentcloudapi.com'
    _service = 'vms'

    async def SendCodeVoice(
            self,
            request: models.SendCodeVoiceRequest,
            opts: Dict = None,
    ) -> models.SendCodeVoiceResponse:
        """
        给用户发语音验证码（仅支持数字）。
        """
        
        kwargs = {}
        kwargs["action"] = "SendCodeVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendCodeVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendTtsVoice(
            self,
            request: models.SendTtsVoiceRequest,
            opts: Dict = None,
    ) -> models.SendTtsVoiceResponse:
        """
        给用户发送指定模板的语音通知。
        """
        
        kwargs = {}
        kwargs["action"] = "SendTtsVoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendTtsVoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)