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
from tencentcloud.ai3d.v20250513 import models
from typing import Dict


class Ai3dClient(AbstractClient):
    _apiVersion = '2025-05-13'
    _endpoint = 'ai3d.tencentcloudapi.com'
    _service = 'ai3d'

    async def QueryHunyuanTo3DProJob(
            self,
            request: models.QueryHunyuanTo3DProJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuanTo3DProJobResponse:
        """
        混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供3个并发，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuanTo3DProJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuanTo3DProJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryHunyuanTo3DRapidJob(
            self,
            request: models.QueryHunyuanTo3DRapidJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuanTo3DRapidJobResponse:
        """
        混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuanTo3DRapidJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuanTo3DRapidJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHunyuanTo3DProJob(
            self,
            request: models.SubmitHunyuanTo3DProJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanTo3DProJobResponse:
        """
        混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供3个并发，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanTo3DProJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanTo3DProJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHunyuanTo3DRapidJob(
            self,
            request: models.SubmitHunyuanTo3DRapidJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanTo3DRapidJobResponse:
        """
        混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanTo3DRapidJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanTo3DRapidJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)