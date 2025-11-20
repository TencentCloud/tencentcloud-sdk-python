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
from tencentcloud.soe.v20180724 import models
from typing import Dict


class SoeClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'soe.tencentcloudapi.com'
    _service = 'soe'

    async def InitOralProcess(
            self,
            request: models.InitOralProcessRequest,
            opts: Dict = None,
    ) -> models.InitOralProcessResponse:
        """
        初始化发音评估过程，每一轮评估前进行调用。语音输入模式分为流式模式和非流式模式，流式模式支持数据分片传输，可以加快评估响应速度。评估模式分为词模式和句子模式，词模式会标注每个音节的详细信息；句子模式会有完整度和流利度的评估。
        """
        
        kwargs = {}
        kwargs["action"] = "InitOralProcess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitOralProcessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KeywordEvaluate(
            self,
            request: models.KeywordEvaluateRequest,
            opts: Dict = None,
    ) -> models.KeywordEvaluateResponse:
        """
        指定主题关键词词汇评估，分析语音与关键词的切合程度，可指定多个关键词，支持中文英文同时评测。分片传输时，尽量保证纯异步调用，即不等待上一个分片的传输结果边录边传，这样可以尽可能早的提供音频数据。音频源目前仅支持16k采样率16bit单声道编码方式，如有不一致可能导致评估不准确或失败。
        """
        
        kwargs = {}
        kwargs["action"] = "KeywordEvaluate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KeywordEvaluateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransmitOralProcess(
            self,
            request: models.TransmitOralProcessRequest,
            opts: Dict = None,
    ) -> models.TransmitOralProcessResponse:
        """
        本接口可用于中英文发音评测数据传输。在使用本接口时需要注意：传输音频数据，必须在完成发音评估初始化接口之后调用，且SessonId要与初始化接口保持一致。分片传输时，尽量保证SeqId顺序传输（请确认SeqId由1开始）。音频源目前仅支持16k采样率16bit单声道编码方式，如有不一致可能导致评估不准确或失败。
        """
        
        kwargs = {}
        kwargs["action"] = "TransmitOralProcess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransmitOralProcessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransmitOralProcessWithInit(
            self,
            request: models.TransmitOralProcessWithInitRequest,
            opts: Dict = None,
    ) -> models.TransmitOralProcessWithInitResponse:
        """
        本接口可用于中英文发音评测。在使用本接口时需要注意：初始化并传输音频数据，分片传输时，尽量保证SeqId顺序传输（请确认SeqId由1开始）。音频源目前仅支持16k采样率16bit单声道编码方式，如有不一致可能导致评估不准确或失败。
        """
        
        kwargs = {}
        kwargs["action"] = "TransmitOralProcessWithInit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransmitOralProcessWithInitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)