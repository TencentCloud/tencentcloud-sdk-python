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
from tencentcloud.wss.v20180426 import models
from typing import Dict


class WssClient(AbstractClient):
    _apiVersion = '2018-04-26'
    _endpoint = 'wss.tencentcloudapi.com'
    _service = 'wss'

    async def DeleteCert(
            self,
            request: models.DeleteCertRequest,
            opts: Dict = None,
    ) -> models.DeleteCertResponse:
        """
        本接口（DeleteCert）用于删除证书。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertList(
            self,
            request: models.DescribeCertListRequest,
            opts: Dict = None,
    ) -> models.DescribeCertListResponse:
        """
        本接口(DescribeCertList)用于获取证书列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadCert(
            self,
            request: models.UploadCertRequest,
            opts: Dict = None,
    ) -> models.UploadCertResponse:
        """
        本接口（UploadCert）用于上传证书。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)