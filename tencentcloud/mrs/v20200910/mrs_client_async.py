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
from tencentcloud.mrs.v20200910 import models
from typing import Dict


class MrsClient(AbstractClient):
    _apiVersion = '2020-09-10'
    _endpoint = 'mrs.tencentcloudapi.com'
    _service = 'mrs'

    async def DrugInstructionObject(
            self,
            request: models.DrugInstructionObjectRequest,
            opts: Dict = None,
    ) -> models.DrugInstructionObjectResponse:
        """
        药品说明书PDF文件结构化
        """
        
        kwargs = {}
        kwargs["action"] = "DrugInstructionObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DrugInstructionObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageMask(
            self,
            request: models.ImageMaskRequest,
            opts: Dict = None,
    ) -> models.ImageMaskResponse:
        """
        医疗报告图片脱敏接口
        """
        
        kwargs = {}
        kwargs["action"] = "ImageMask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageMaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageMaskAsync(
            self,
            request: models.ImageMaskAsyncRequest,
            opts: Dict = None,
    ) -> models.ImageMaskAsyncResponse:
        """
        图片脱敏-异步接口
        短时间大批量调用（例如>100上传/10分钟），如果遇到错误码“FalledOperation.AsyncQueueFullError”，请于数分钟后再次尝试提交。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageMaskAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageMaskAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageMaskAsyncGetResult(
            self,
            request: models.ImageMaskAsyncGetResultRequest,
            opts: Dict = None,
    ) -> models.ImageMaskAsyncGetResultResponse:
        """
        图片脱敏-异步获取结果接口
        请于上传请求后24小时内获取结果。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageMaskAsyncGetResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageMaskAsyncGetResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageToClass(
            self,
            request: models.ImageToClassRequest,
            opts: Dict = None,
    ) -> models.ImageToClassResponse:
        """
        图片分类
        """
        
        kwargs = {}
        kwargs["action"] = "ImageToClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageToClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageToObject(
            self,
            request: models.ImageToObjectRequest,
            opts: Dict = None,
    ) -> models.ImageToObjectResponse:
        """
        图片转结构化对象
        """
        
        kwargs = {}
        kwargs["action"] = "ImageToObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageToObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextToClass(
            self,
            request: models.TextToClassRequest,
            opts: Dict = None,
    ) -> models.TextToClassResponse:
        """
        文本分类

        适用场景：经过腾讯医疗专用 OCR 从图片识别之后的文本，并且需要加上每个字符的坐标信息，才可以调用此接口。通过其它 OCR 识别的文本可能不适配。医院的 XML 格式文本也不适配，XML 文件需要经过特殊转换才能直接调用此接口。单次调用传入的文本不宜超过 2000 字。如有需要调用此接口，建议先咨询产品团队。
        """
        
        kwargs = {}
        kwargs["action"] = "TextToClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextToObject(
            self,
            request: models.TextToObjectRequest,
            opts: Dict = None,
    ) -> models.TextToObjectResponse:
        """
        文本转结构化对象。

        适用场景：经过腾讯医疗专用 OCR 从图片识别之后的文本，可以调用此接口。通过其它 OCR 识别的文本可能不适配。医院的 XML 格式文本也不适配，XML 文件需要经过特殊转换才能直接调用此接口。单次调用传入的文本不宜超过 2000 字。
        """
        
        kwargs = {}
        kwargs["action"] = "TextToObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TurnPDFToObject(
            self,
            request: models.TurnPDFToObjectRequest,
            opts: Dict = None,
    ) -> models.TurnPDFToObjectResponse:
        """
        将PDF格式的体检报告文件结构化，解析关键信息。
        注意：该接口是按照体检报告 PDF 页面数量统计次数，不是按照 PDF 文件数量统计次数。通过该接口传入的报告必须是体检报告，非体检报告可能无法正确解析。
        """
        
        kwargs = {}
        kwargs["action"] = "TurnPDFToObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TurnPDFToObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TurnPDFToObjectAsync(
            self,
            request: models.TurnPDFToObjectAsyncRequest,
            opts: Dict = None,
    ) -> models.TurnPDFToObjectAsyncResponse:
        """
        体检报告PDF文件结构化-异步接口
        """
        
        kwargs = {}
        kwargs["action"] = "TurnPDFToObjectAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TurnPDFToObjectAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TurnPDFToObjectAsyncGetResult(
            self,
            request: models.TurnPDFToObjectAsyncGetResultRequest,
            opts: Dict = None,
    ) -> models.TurnPDFToObjectAsyncGetResultResponse:
        """
        体检报告PDF文件结构化异步获取结果接口
        """
        
        kwargs = {}
        kwargs["action"] = "TurnPDFToObjectAsyncGetResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TurnPDFToObjectAsyncGetResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)