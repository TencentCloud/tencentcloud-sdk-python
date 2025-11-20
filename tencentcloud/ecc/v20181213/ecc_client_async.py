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
from tencentcloud.ecc.v20181213 import models
from typing import Dict


class EccClient(AbstractClient):
    _apiVersion = '2018-12-13'
    _endpoint = 'ecc.tencentcloudapi.com'
    _service = 'ecc'

    async def CorrectMultiImage(
            self,
            request: models.CorrectMultiImageRequest,
            opts: Dict = None,
    ) -> models.CorrectMultiImageResponse:
        """
        https://ecc.tencentcloudapi.com/?Action=CorrectMultiImage
        多图像识别批改接口
        """
        
        kwargs = {}
        kwargs["action"] = "CorrectMultiImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CorrectMultiImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTask(
            self,
            request: models.DescribeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResponse:
        """
        异步任务结果查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ECC(
            self,
            request: models.ECCRequest,
            opts: Dict = None,
    ) -> models.ECCResponse:
        """
        纯文本英语作文批改
        """
        
        kwargs = {}
        kwargs["action"] = "ECC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ECCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EHOCR(
            self,
            request: models.EHOCRRequest,
            opts: Dict = None,
    ) -> models.EHOCRResponse:
        """
        https://ecc.tencentcloudapi.com/?Action=EHOCR
        图像识别批改接口
        """
        
        kwargs = {}
        kwargs["action"] = "EHOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EHOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)