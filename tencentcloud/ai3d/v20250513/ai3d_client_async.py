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

    async def Convert3DFormat(
            self,
            request: models.Convert3DFormatRequest,
            opts: Dict = None,
    ) -> models.Convert3DFormatResponse:
        """
        输入3D模型文件后，可进行3D模型文件格式转换。
        """
        
        kwargs = {}
        kwargs["action"] = "Convert3DFormat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Convert3DFormatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHunyuanTo3DUVJob(
            self,
            request: models.DescribeHunyuanTo3DUVJobRequest,
            opts: Dict = None,
    ) -> models.DescribeHunyuanTo3DUVJobResponse:
        """
        查询组件拆分任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHunyuanTo3DUVJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHunyuanTo3DUVJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReduceFaceJob(
            self,
            request: models.DescribeReduceFaceJobRequest,
            opts: Dict = None,
    ) -> models.DescribeReduceFaceJobResponse:
        """
        混元生3D接口，采用 Polygon 1.5模型，输入3D 高模后，可生成布线规整，较低面数的3D 模型。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReduceFaceJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReduceFaceJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTextureTo3DJob(
            self,
            request: models.DescribeTextureTo3DJobRequest,
            opts: Dict = None,
    ) -> models.DescribeTextureTo3DJobResponse:
        """
        混元生3D接口，输入单几何模型和参考图或文字描述后，可生成对应的纹理贴图。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTextureTo3DJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTextureTo3DJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryHunyuan3DPartJob(
            self,
            request: models.QueryHunyuan3DPartJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuan3DPartJobResponse:
        """
        查询组件生成任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuan3DPartJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuan3DPartJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        
    async def SubmitHunyuan3DPartJob(
            self,
            request: models.SubmitHunyuan3DPartJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuan3DPartJobResponse:
        """
        输入3D模型文件后，根据模型结构自动进行组件识别生成。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuan3DPartJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuan3DPartJobResponse
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
        
    async def SubmitHunyuanTo3DUVJob(
            self,
            request: models.SubmitHunyuanTo3DUVJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanTo3DUVJobResponse:
        """
        输入模型后，可根据模型纹理进行UV展开，输出对应UV贴图。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanTo3DUVJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanTo3DUVJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitReduceFaceJob(
            self,
            request: models.SubmitReduceFaceJobRequest,
            opts: Dict = None,
    ) -> models.SubmitReduceFaceJobResponse:
        """
        混元生3D接口，采用 Polygon 1.5模型，输入3D 高模后，可生成布线规整，较低面数的3D 模型。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitReduceFaceJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitReduceFaceJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTextureTo3DJob(
            self,
            request: models.SubmitTextureTo3DJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTextureTo3DJobResponse:
        """
        混元生3D接口，输入单几何模型和参考图或文字描述后，可生成对应的纹理贴图。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTextureTo3DJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTextureTo3DJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)