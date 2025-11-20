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
from tencentcloud.bsca.v20210811 import models
from typing import Dict


class BscaClient(AbstractClient):
    _apiVersion = '2021-08-11'
    _endpoint = 'bsca.tencentcloudapi.com'
    _service = 'bsca'

    async def DescribeKBComponent(
            self,
            request: models.DescribeKBComponentRequest,
            opts: Dict = None,
    ) -> models.DescribeKBComponentResponse:
        """
        本接口(DescribeKBComponent)用于在知识库中查询开源组件信息。本接口根据用户输入的PURL在知识库中寻找对应的开源组件，其中Name为必填字段。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBComponentVersionList(
            self,
            request: models.DescribeKBComponentVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeKBComponentVersionListResponse:
        """
        查询特定组件的版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBComponentVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBComponentVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBComponentVulnerability(
            self,
            request: models.DescribeKBComponentVulnerabilityRequest,
            opts: Dict = None,
    ) -> models.DescribeKBComponentVulnerabilityResponse:
        """
        本接口(DescribeKBComponentVulnerability)用于在知识库中查询开源组件的漏洞信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBComponentVulnerability"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBComponentVulnerabilityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBLicense(
            self,
            request: models.DescribeKBLicenseRequest,
            opts: Dict = None,
    ) -> models.DescribeKBLicenseResponse:
        """
        本接口(DescribeKBLicense)用于在知识库中查询许可证信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBVulnerability(
            self,
            request: models.DescribeKBVulnerabilityRequest,
            opts: Dict = None,
    ) -> models.DescribeKBVulnerabilityResponse:
        """
        本接口(DescribeKBVulnerability)用于在知识库中查询漏洞详细信息，支持根据CVE、Vul ID、CNVD ID、CNNVD ID查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBVulnerability"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBVulnerabilityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MatchKBPURLList(
            self,
            request: models.MatchKBPURLListRequest,
            opts: Dict = None,
    ) -> models.MatchKBPURLListResponse:
        """
        本接口(MatchKBPURLList)用于在知识库中匹配与特征对应的开源组件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "MatchKBPURLList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MatchKBPURLListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchKBComponent(
            self,
            request: models.SearchKBComponentRequest,
            opts: Dict = None,
    ) -> models.SearchKBComponentResponse:
        """
        根据输入的组件名、组件类型搜索相应的组件，返回符合条件的组件列表
        """
        
        kwargs = {}
        kwargs["action"] = "SearchKBComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchKBComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)