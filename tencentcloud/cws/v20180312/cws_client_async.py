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
from tencentcloud.cws.v20180312 import models
from typing import Dict


class CwsClient(AbstractClient):
    _apiVersion = '2018-03-12'
    _endpoint = 'cws.tencentcloudapi.com'
    _service = 'cws'

    async def CreateMonitors(
            self,
            request: models.CreateMonitorsRequest,
            opts: Dict = None,
    ) -> models.CreateMonitorsResponse:
        """
        本接口（CreateMonitors）用于新增一个或多个站点的监测任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMonitors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMonitorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSites(
            self,
            request: models.CreateSitesRequest,
            opts: Dict = None,
    ) -> models.CreateSitesResponse:
        """
        本接口（CreateSites）用于新增一个或多个站点。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSitesScans(
            self,
            request: models.CreateSitesScansRequest,
            opts: Dict = None,
    ) -> models.CreateSitesScansResponse:
        """
        本接口（CreateSitesScans）用于新增一个或多个站点的单次扫描任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSitesScans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSitesScansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulsMisinformation(
            self,
            request: models.CreateVulsMisinformationRequest,
            opts: Dict = None,
    ) -> models.CreateVulsMisinformationResponse:
        """
        本接口（CreateVulsMisinformation）可以用于新增一个或多个漏洞误报信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulsMisinformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulsMisinformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulsReport(
            self,
            request: models.CreateVulsReportRequest,
            opts: Dict = None,
    ) -> models.CreateVulsReportResponse:
        """
        本接口 (CreateVulsReport) 用于生成漏洞报告并返回下载链接。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulsReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulsReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMonitors(
            self,
            request: models.DeleteMonitorsRequest,
            opts: Dict = None,
    ) -> models.DeleteMonitorsResponse:
        """
        本接口 (DeleteMonitors) 用于删除用户监控任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMonitors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMonitorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSites(
            self,
            request: models.DeleteSitesRequest,
            opts: Dict = None,
    ) -> models.DeleteSitesResponse:
        """
        本接口 (DeleteSites) 用于删除站点。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfig(
            self,
            request: models.DescribeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigResponse:
        """
        本接口 (DescribeConfig) 用于查询用户配置的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitors(
            self,
            request: models.DescribeMonitorsRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorsResponse:
        """
        本接口 (DescribeMonitors) 用于查询一个或多个监控任务的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSiteQuota(
            self,
            request: models.DescribeSiteQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeSiteQuotaResponse:
        """
        本接口 (DescribeSiteQuota) 用于查询用户购买的扫描次数总数和已使用数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSiteQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSiteQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSites(
            self,
            request: models.DescribeSitesRequest,
            opts: Dict = None,
    ) -> models.DescribeSitesResponse:
        """
        本接口 (DescribeSites) 用于查询一个或多个站点的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSitesVerification(
            self,
            request: models.DescribeSitesVerificationRequest,
            opts: Dict = None,
    ) -> models.DescribeSitesVerificationResponse:
        """
        本接口 (DescribeSitesVerification) 用于查询一个或多个待验证站点的验证信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSitesVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSitesVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVuls(
            self,
            request: models.DescribeVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeVulsResponse:
        """
        本接口 (DescribeVuls) 用于查询一个或多个漏洞的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulsNumber(
            self,
            request: models.DescribeVulsNumberRequest,
            opts: Dict = None,
    ) -> models.DescribeVulsNumberResponse:
        """
        本接口 (DescribeVulsNumber) 用于查询用户网站的漏洞总计数量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulsNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulsNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulsNumberTimeline(
            self,
            request: models.DescribeVulsNumberTimelineRequest,
            opts: Dict = None,
    ) -> models.DescribeVulsNumberTimelineResponse:
        """
        本接口 (DescribeVulsNumberTimeline) 用于查询漏洞数随时间变化统计信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulsNumberTimeline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulsNumberTimelineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfigAttribute(
            self,
            request: models.ModifyConfigAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigAttributeResponse:
        """
        本接口 (ModifyConfigAttribute) 用于修改用户配置的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfigAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMonitorAttribute(
            self,
            request: models.ModifyMonitorAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyMonitorAttributeResponse:
        """
        本接口 (ModifyMonitorAttribute) 用于修改监测任务的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMonitorAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMonitorAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySiteAttribute(
            self,
            request: models.ModifySiteAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySiteAttributeResponse:
        """
        本接口 (ModifySiteAttribute) 用于修改站点的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySiteAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySiteAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifySites(
            self,
            request: models.VerifySitesRequest,
            opts: Dict = None,
    ) -> models.VerifySitesResponse:
        """
        本接口 (VerifySites) 用于验证一个或多个待验证站点。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifySites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifySitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)