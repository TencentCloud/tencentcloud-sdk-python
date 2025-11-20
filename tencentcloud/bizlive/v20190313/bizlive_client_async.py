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
from tencentcloud.bizlive.v20190313 import models
from typing import Dict


class BizliveClient(AbstractClient):
    _apiVersion = '2019-03-13'
    _endpoint = 'bizlive.tencentcloudapi.com'
    _service = 'bizlive'

    async def CreateSession(
            self,
            request: models.CreateSessionRequest,
            opts: Dict = None,
    ) -> models.CreateSessionResponse:
        """
        创建会话
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamPlayInfoList(
            self,
            request: models.DescribeStreamPlayInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamPlayInfoListResponse:
        """
        查询播放数据，支持按流名称查询详细播放数据，也可按播放域名查询详细总数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamPlayInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamPlayInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkers(
            self,
            request: models.DescribeWorkersRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkersResponse:
        """
        查询空闲机器数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidLiveStream(
            self,
            request: models.ForbidLiveStreamRequest,
            opts: Dict = None,
    ) -> models.ForbidLiveStreamResponse:
        """
        禁止某条流的推送，可以预设某个时刻将流恢复。
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterIM(
            self,
            request: models.RegisterIMRequest,
            opts: Dict = None,
    ) -> models.RegisterIMResponse:
        """
        注册聊天室
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterIM"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterIMResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopGame(
            self,
            request: models.StopGameRequest,
            opts: Dict = None,
    ) -> models.StopGameResponse:
        """
        强制退出游戏
        """
        
        kwargs = {}
        kwargs["action"] = "StopGame"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopGameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)