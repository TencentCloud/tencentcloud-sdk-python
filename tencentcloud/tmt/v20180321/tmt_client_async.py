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
from tencentcloud.tmt.v20180321 import models
from typing import Dict


class TmtClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'tmt.tencentcloudapi.com'
    _service = 'tmt'

    async def FileTranslate(
            self,
            request: models.FileTranslateRequest,
            opts: Dict = None,
    ) -> models.FileTranslateResponse:
        """
        提交文档原文内容，输出任务ID， 支持原文为单一语种文档（如出现多语言文档，仅支持以选定的源语言相关内容翻译）,文件格式有pdf、docx、pptx、xlsx，支持的文本格式有txt、xml、html、markdown、properties。任务翻译数据可保存7天，7天后不再返回任务数据。请注意保存。
        """
        
        kwargs = {}
        kwargs["action"] = "FileTranslate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FileTranslateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFileTranslate(
            self,
            request: models.GetFileTranslateRequest,
            opts: Dict = None,
    ) -> models.GetFileTranslateResponse:
        """
        在调用文档翻译请求接口后，有回调和轮询两种方式获取识别结果。
        •当采用回调方式时，翻译完成后会将结果通过 POST 请求的形式通知到用户在请求时填写的回调 URL，具体请参见[文件翻译回调说明](https://cloud.tencent.com/document/product/551/91138)。
        • 当采用轮询方式时，需要主动提交任务ID来轮询识别结果，共有任务成功、等待、执行中和失败四种结果，具体信息请参见参数说明。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFileTranslate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFileTranslateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageTranslate(
            self,
            request: models.ImageTranslateRequest,
            opts: Dict = None,
    ) -> models.ImageTranslateResponse:
        """
        提供13种语言的图片翻译服务，可自动识别图片中的文本内容并翻译成目标语言，识别后的文本按行翻译，后续会提供可按段落翻译的版本。<br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageTranslate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageTranslateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageTranslateLLM(
            self,
            request: models.ImageTranslateLLMRequest,
            opts: Dict = None,
    ) -> models.ImageTranslateLLMResponse:
        """
        提供18种语言的图片翻译服务，可自动识别图片中的文本内容并翻译成目标语言，识别后的文本按行翻译，后续会提供可按段落翻译的版本。

        - 输入图片格式：png、jpg、jpeg等常用图片格式，不支持gif动图。
        - 输出图片格式：jpg。

        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageTranslateLLM"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageTranslateLLMResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LanguageDetect(
            self,
            request: models.LanguageDetectRequest,
            opts: Dict = None,
    ) -> models.LanguageDetectResponse:
        """
        可自动识别文本内容的语言种类，轻量高效，无需额外实现判断方式，使面向客户的服务体验更佳。 <br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。
        """
        
        kwargs = {}
        kwargs["action"] = "LanguageDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LanguageDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SpeechTranslate(
            self,
            request: models.SpeechTranslateRequest,
            opts: Dict = None,
    ) -> models.SpeechTranslateResponse:
        """
        本接口提供上传音频，将音频进行语音识别并翻译成文本的服务，目前开放中英互译的语音翻译服务。
        待识别和翻译的音频文件可以是 pcm、mp3和speex 格式，其中支持流式传输的只有pcm格式，pcm采样率要求16kHz、位深16bit、单声道，音频内语音清晰。<br/>
        如果采用流式传输的方式，要求每个分片时长200ms~500ms；如果采用非流式的传输方式，要求音频时长不超过8s。注意最后一个分片的IsEnd参数设置为1。<br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源部分。
        """
        
        kwargs = {}
        kwargs["action"] = "SpeechTranslate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SpeechTranslateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextTranslate(
            self,
            request: models.TextTranslateRequest,
            opts: Dict = None,
    ) -> models.TextTranslateResponse:
        """
        腾讯翻译为合作伙伴提供文本翻译、文档翻译、交互翻译、AI同传等多种机器翻译服务，具有toB多行业解决方案。作为WMT世界机器翻译大赛冠军，翻译准确度值得信赖，其中，交互翻译能力是业界领先技术；腾讯同传是AI同传业界标杆。<br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。
        """
        
        kwargs = {}
        kwargs["action"] = "TextTranslate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextTranslateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextTranslateBatch(
            self,
            request: models.TextTranslateBatchRequest,
            opts: Dict = None,
    ) -> models.TextTranslateBatchResponse:
        """
        批量翻译文本的接口
        """
        
        kwargs = {}
        kwargs["action"] = "TextTranslateBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextTranslateBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)