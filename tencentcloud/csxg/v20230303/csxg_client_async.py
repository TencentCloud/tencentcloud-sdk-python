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
from tencentcloud.csxg.v20230303 import models
from typing import Dict


class CsxgClient(AbstractClient):
    _apiVersion = '2023-03-03'
    _endpoint = 'csxg.tencentcloudapi.com'
    _service = 'csxg'

    async def Create5GInstance(
            self,
            request: models.Create5GInstanceRequest,
            opts: Dict = None,
    ) -> models.Create5GInstanceResponse:
        """
        创建5G入云服务接口
        """
        
        kwargs = {}
        kwargs["action"] = "Create5GInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Create5GInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Delete5GInstance(
            self,
            request: models.Delete5GInstanceRequest,
            opts: Dict = None,
    ) -> models.Delete5GInstanceResponse:
        """
        删除5G入云服务
        """
        
        kwargs = {}
        kwargs["action"] = "Delete5GInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Delete5GInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Describe5GAPNs(
            self,
            request: models.Describe5GAPNsRequest,
            opts: Dict = None,
    ) -> models.Describe5GAPNsResponse:
        """
        查询APN信息
        """
        
        kwargs = {}
        kwargs["action"] = "Describe5GAPNs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Describe5GAPNsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Describe5GInstances(
            self,
            request: models.Describe5GInstancesRequest,
            opts: Dict = None,
    ) -> models.Describe5GInstancesResponse:
        """
        查询5G入云服务
        """
        
        kwargs = {}
        kwargs["action"] = "Describe5GInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Describe5GInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Modify5GInstanceAttribute(
            self,
            request: models.Modify5GInstanceAttributeRequest,
            opts: Dict = None,
    ) -> models.Modify5GInstanceAttributeResponse:
        """
        修改5G入云服务
        """
        
        kwargs = {}
        kwargs["action"] = "Modify5GInstanceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.Modify5GInstanceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)