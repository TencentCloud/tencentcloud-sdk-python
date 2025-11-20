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
from tencentcloud.sslpod.v20190605 import models
from typing import Dict


class SslpodClient(AbstractClient):
    _apiVersion = '2019-06-05'
    _endpoint = 'sslpod.tencentcloudapi.com'
    _service = 'sslpod'

    async def CreateDomain(
            self,
            request: models.CreateDomainRequest,
            opts: Dict = None,
    ) -> models.CreateDomainResponse:
        """
        通过域名端口添加监控
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomain(
            self,
            request: models.DeleteDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainResponse:
        """
        通过域名ID删除监控的域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDashboard(
            self,
            request: models.DescribeDashboardRequest,
            opts: Dict = None,
    ) -> models.DescribeDashboardResponse:
        """
        获取仪表盘数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainCerts(
            self,
            request: models.DescribeDomainCertsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainCertsResponse:
        """
        获取域名关联证书
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainCerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainCertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainTags(
            self,
            request: models.DescribeDomainTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainTagsResponse:
        """
        获取账号下所有tag
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        通过searchType搜索已经添加的域名
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNoticeInfo(
            self,
            request: models.DescribeNoticeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeNoticeInfoResponse:
        """
        获取通知额度信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNoticeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNoticeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainTags(
            self,
            request: models.ModifyDomainTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainTagsResponse:
        """
        修改域名tag
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshDomain(
            self,
            request: models.RefreshDomainRequest,
            opts: Dict = None,
    ) -> models.RefreshDomainResponse:
        """
        强制重新检测域名
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResolveDomain(
            self,
            request: models.ResolveDomainRequest,
            opts: Dict = None,
    ) -> models.ResolveDomainResponse:
        """
        解析域名获得多个IP地址
        """
        
        kwargs = {}
        kwargs["action"] = "ResolveDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResolveDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)