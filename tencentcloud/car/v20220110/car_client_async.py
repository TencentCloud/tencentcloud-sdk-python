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
from tencentcloud.car.v20220110 import models
from typing import Dict


class CarClient(AbstractClient):
    _apiVersion = '2022-01-10'
    _endpoint = 'car.tencentcloudapi.com'
    _service = 'car'

    async def ApplyConcurrent(
            self,
            request: models.ApplyConcurrentRequest,
            opts: Dict = None,
    ) -> models.ApplyConcurrentResponse:
        """
        本接口用于申请并发。接口超时时间：20秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyConcurrent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyConcurrentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSession(
            self,
            request: models.CreateSessionRequest,
            opts: Dict = None,
    ) -> models.CreateSessionResponse:
        """
        本接口用于创建会话。接口超时时间：5秒。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroySession(
            self,
            request: models.DestroySessionRequest,
            opts: Dict = None,
    ) -> models.DestroySessionResponse:
        """
        销毁会话。如果该会话开启了云端推流，那么销毁会话时会结束云端推流。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroySession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroySessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishStream(
            self,
            request: models.StartPublishStreamRequest,
            opts: Dict = None,
    ) -> models.StartPublishStreamResponse:
        """
        开始云端推流。云端推流 codec 根据客户端（SDK）能力来自动选择，默认优先顺序为 H265、H264、VP8、VP9。
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishStreamWithURL(
            self,
            request: models.StartPublishStreamWithURLRequest,
            opts: Dict = None,
    ) -> models.StartPublishStreamWithURLResponse:
        """
        开始云端推流到指定URL。云端推流 codec 根据客户端（SDK）能力来自动选择，默认优先顺序为 H265、H264、VP8、VP9。该推流方式需要单独计费，详细计费方式请查看[指定地址推流费用说明](https://cloud.tencent.com/document/product/1547/72168#98ac188a-d122-4caf-88be-05268ecefdf6)
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishStreamWithURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishStreamWithURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopPublishStream(
            self,
            request: models.StopPublishStreamRequest,
            opts: Dict = None,
    ) -> models.StopPublishStreamResponse:
        """
        停止云端推流
        """
        
        kwargs = {}
        kwargs["action"] = "StopPublishStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopPublishStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)