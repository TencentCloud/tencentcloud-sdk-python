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
from tencentcloud.ca.v20230228 import models
from typing import Dict


class CaClient(AbstractClient):
    _apiVersion = '2023-02-28'
    _endpoint = 'ca.tencentcloudapi.com'
    _service = 'ca'

    async def CreateVerifyReport(
            self,
            request: models.CreateVerifyReportRequest,
            opts: Dict = None,
    ) -> models.CreateVerifyReportResponse:
        """
        创建签名验证报告任务，此接口为异步盖章接口，盖章时效24小时。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVerifyReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVerifyReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVerifyReport(
            self,
            request: models.DescribeVerifyReportRequest,
            opts: Dict = None,
    ) -> models.DescribeVerifyReportResponse:
        """
        下载验签报告url，url有效期默认12小时
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVerifyReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVerifyReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFile(
            self,
            request: models.UploadFileRequest,
            opts: Dict = None,
    ) -> models.UploadFileResponse:
        """
        文件上传接口
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)