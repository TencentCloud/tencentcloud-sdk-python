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
from tencentcloud.bma.v20221115 import models
from typing import Dict


class BmaClient(AbstractClient):
    _apiVersion = '2022-11-15'
    _endpoint = 'bma.tencentcloudapi.com'
    _service = 'bma'

    async def CreateBPBrand(
            self,
            request: models.CreateBPBrandRequest,
            opts: Dict = None,
    ) -> models.CreateBPBrandResponse:
        """
        添加品牌
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPBrand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPBrandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPFakeAPP(
            self,
            request: models.CreateBPFakeAPPRequest,
            opts: Dict = None,
    ) -> models.CreateBPFakeAPPResponse:
        """
        仿冒应用举报
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPFakeAPP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPFakeAPPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPFakeAPPList(
            self,
            request: models.CreateBPFakeAPPListRequest,
            opts: Dict = None,
    ) -> models.CreateBPFakeAPPListResponse:
        """
        批量仿冒应用举报
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPFakeAPPList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPFakeAPPListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPFakeURL(
            self,
            request: models.CreateBPFakeURLRequest,
            opts: Dict = None,
    ) -> models.CreateBPFakeURLResponse:
        """
        仿冒网址举报
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPFakeURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPFakeURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPFakeURLs(
            self,
            request: models.CreateBPFakeURLsRequest,
            opts: Dict = None,
    ) -> models.CreateBPFakeURLsResponse:
        """
        批量仿冒网址举报
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPFakeURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPFakeURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPWhiteList(
            self,
            request: models.CreateBPWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateBPWhiteListResponse:
        """
        添加白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBPWhiteList(
            self,
            request: models.DeleteBPWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteBPWhiteListResponse:
        """
        删除白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBPWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBPWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPBrands(
            self,
            request: models.DescribeBPBrandsRequest,
            opts: Dict = None,
    ) -> models.DescribeBPBrandsResponse:
        """
        查询品牌列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPBrands"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPBrandsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPFakeAPPList(
            self,
            request: models.DescribeBPFakeAPPListRequest,
            opts: Dict = None,
    ) -> models.DescribeBPFakeAPPListResponse:
        """
        查询仿冒应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPFakeAPPList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPFakeAPPListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPFakeURLs(
            self,
            request: models.DescribeBPFakeURLsRequest,
            opts: Dict = None,
    ) -> models.DescribeBPFakeURLsResponse:
        """
        查询仿冒网址列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPFakeURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPFakeURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPWhiteLists(
            self,
            request: models.DescribeBPWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DescribeBPWhiteListsResponse:
        """
        查询白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)