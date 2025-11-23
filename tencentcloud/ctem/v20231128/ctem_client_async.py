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
from tencentcloud.ctem.v20231128 import models
from typing import Dict


class CtemClient(AbstractClient):
    _apiVersion = '2023-11-28'
    _endpoint = 'ctem.tencentcloudapi.com'
    _service = 'ctem'

    async def CreateApp(
            self,
            request: models.CreateAppRequest,
            opts: Dict = None,
    ) -> models.CreateAppResponse:
        """
        添加APP资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAsset(
            self,
            request: models.CreateAssetRequest,
            opts: Dict = None,
    ) -> models.CreateAssetResponse:
        """
        添加主机资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomer(
            self,
            request: models.CreateCustomerRequest,
            opts: Dict = None,
    ) -> models.CreateCustomerResponse:
        """
        创建企业
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomain(
            self,
            request: models.CreateDomainRequest,
            opts: Dict = None,
    ) -> models.CreateDomainResponse:
        """
        添加主域名数据
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnterprise(
            self,
            request: models.CreateEnterpriseRequest,
            opts: Dict = None,
    ) -> models.CreateEnterpriseResponse:
        """
        添加企业架构资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnterprise"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnterpriseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHttp(
            self,
            request: models.CreateHttpRequest,
            opts: Dict = None,
    ) -> models.CreateHttpResponse:
        """
        添加网站资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHttp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHttpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJobRecord(
            self,
            request: models.CreateJobRecordRequest,
            opts: Dict = None,
    ) -> models.CreateJobRecordResponse:
        """
        启动测绘
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJobRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJobRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateManage(
            self,
            request: models.CreateManageRequest,
            opts: Dict = None,
    ) -> models.CreateManageResponse:
        """
        添加后台数据
        """
        
        kwargs = {}
        kwargs["action"] = "CreateManage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateManageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePort(
            self,
            request: models.CreatePortRequest,
            opts: Dict = None,
    ) -> models.CreatePortResponse:
        """
        添加端口服务资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSeeds(
            self,
            request: models.CreateSeedsRequest,
            opts: Dict = None,
    ) -> models.CreateSeedsResponse:
        """
        创建种子
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSeeds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSeedsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubDomain(
            self,
            request: models.CreateSubDomainRequest,
            opts: Dict = None,
    ) -> models.CreateSubDomainResponse:
        """
        添加子域名数据
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSuspiciousAsset(
            self,
            request: models.CreateSuspiciousAssetRequest,
            opts: Dict = None,
    ) -> models.CreateSuspiciousAssetResponse:
        """
        添加影子资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSuspiciousAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSuspiciousAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWechatApplet(
            self,
            request: models.CreateWechatAppletRequest,
            opts: Dict = None,
    ) -> models.CreateWechatAppletResponse:
        """
        添加微信小程序资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWechatApplet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWechatAppletResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWechatOfficialAccount(
            self,
            request: models.CreateWechatOfficialAccountRequest,
            opts: Dict = None,
    ) -> models.CreateWechatOfficialAccountResponse:
        """
        添加微信公众号资产
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWechatOfficialAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWechatOfficialAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApps(
            self,
            request: models.DeleteAppsRequest,
            opts: Dict = None,
    ) -> models.DeleteAppsResponse:
        """
        删除APP数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAssets(
            self,
            request: models.DeleteAssetsRequest,
            opts: Dict = None,
    ) -> models.DeleteAssetsResponse:
        """
        删除主机资产数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomains(
            self,
            request: models.DeleteDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainsResponse:
        """
        删除主域名数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnterprises(
            self,
            request: models.DeleteEnterprisesRequest,
            opts: Dict = None,
    ) -> models.DeleteEnterprisesResponse:
        """
        删除企业架构数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnterprises"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnterprisesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHttps(
            self,
            request: models.DeleteHttpsRequest,
            opts: Dict = None,
    ) -> models.DeleteHttpsResponse:
        """
        删除网站资产数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHttps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHttpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteManages(
            self,
            request: models.DeleteManagesRequest,
            opts: Dict = None,
    ) -> models.DeleteManagesResponse:
        """
        删除后台数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteManages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteManagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePorts(
            self,
            request: models.DeletePortsRequest,
            opts: Dict = None,
    ) -> models.DeletePortsResponse:
        """
        删除端口数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSeeds(
            self,
            request: models.DeleteSeedsRequest,
            opts: Dict = None,
    ) -> models.DeleteSeedsResponse:
        """
        删除种子
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSeeds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSeedsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubDomains(
            self,
            request: models.DeleteSubDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteSubDomainsResponse:
        """
        删除子域名数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSuspiciousAssets(
            self,
            request: models.DeleteSuspiciousAssetsRequest,
            opts: Dict = None,
    ) -> models.DeleteSuspiciousAssetsResponse:
        """
        删除影子资产数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSuspiciousAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSuspiciousAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWechatApplets(
            self,
            request: models.DeleteWechatAppletsRequest,
            opts: Dict = None,
    ) -> models.DeleteWechatAppletsResponse:
        """
        删除微信小程序数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWechatApplets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWechatAppletsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWechatOfficialAccounts(
            self,
            request: models.DeleteWechatOfficialAccountsRequest,
            opts: Dict = None,
    ) -> models.DeleteWechatOfficialAccountsResponse:
        """
        删除微信公众号数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWechatOfficialAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWechatOfficialAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiSecs(
            self,
            request: models.DescribeApiSecsRequest,
            opts: Dict = None,
    ) -> models.DescribeApiSecsResponse:
        """
        查看API安全数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiSecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiSecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApps(
            self,
            request: models.DescribeAppsRequest,
            opts: Dict = None,
    ) -> models.DescribeAppsResponse:
        """
        查看移动端资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssets(
            self,
            request: models.DescribeAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetsResponse:
        """
        查看主机资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigs(
            self,
            request: models.DescribeConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigsResponse:
        """
        查看目录爆破数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomers(
            self,
            request: models.DescribeCustomersRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomersResponse:
        """
        查看企业列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDarkWebs(
            self,
            request: models.DescribeDarkWebsRequest,
            opts: Dict = None,
    ) -> models.DescribeDarkWebsResponse:
        """
        查看暗网数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDarkWebs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDarkWebsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        查看主域名数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnterprises(
            self,
            request: models.DescribeEnterprisesRequest,
            opts: Dict = None,
    ) -> models.DescribeEnterprisesResponse:
        """
        查看企业架构数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnterprises"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnterprisesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFakeApps(
            self,
            request: models.DescribeFakeAppsRequest,
            opts: Dict = None,
    ) -> models.DescribeFakeAppsResponse:
        """
        查询仿冒应用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFakeApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFakeAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFakeMiniPrograms(
            self,
            request: models.DescribeFakeMiniProgramsRequest,
            opts: Dict = None,
    ) -> models.DescribeFakeMiniProgramsResponse:
        """
        查询仿冒小程序
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFakeMiniPrograms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFakeMiniProgramsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFakeWebsites(
            self,
            request: models.DescribeFakeWebsitesRequest,
            opts: Dict = None,
    ) -> models.DescribeFakeWebsitesResponse:
        """
        查询仿冒网站
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFakeWebsites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFakeWebsitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFakeWechatOfficials(
            self,
            request: models.DescribeFakeWechatOfficialsRequest,
            opts: Dict = None,
    ) -> models.DescribeFakeWechatOfficialsResponse:
        """
        查询仿冒公众号
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFakeWechatOfficials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFakeWechatOfficialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGithubs(
            self,
            request: models.DescribeGithubsRequest,
            opts: Dict = None,
    ) -> models.DescribeGithubsResponse:
        """
        查看Github泄露数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGithubs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGithubsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHttps(
            self,
            request: models.DescribeHttpsRequest,
            opts: Dict = None,
    ) -> models.DescribeHttpsResponse:
        """
        查看http数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHttps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHttpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobRecordDetails(
            self,
            request: models.DescribeJobRecordDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobRecordDetailsResponse:
        """
        查看链路详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobRecordDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobRecordDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobRecords(
            self,
            request: models.DescribeJobRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobRecordsResponse:
        """
        查看任务运行记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLeakageCodes(
            self,
            request: models.DescribeLeakageCodesRequest,
            opts: Dict = None,
    ) -> models.DescribeLeakageCodesResponse:
        """
        获取代码泄露数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLeakageCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLeakageCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLeakageDatas(
            self,
            request: models.DescribeLeakageDatasRequest,
            opts: Dict = None,
    ) -> models.DescribeLeakageDatasResponse:
        """
        获取数据泄露事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLeakageDatas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLeakageDatasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLeakageEmails(
            self,
            request: models.DescribeLeakageEmailsRequest,
            opts: Dict = None,
    ) -> models.DescribeLeakageEmailsResponse:
        """
        获取邮箱泄露数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLeakageEmails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLeakageEmailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeManages(
            self,
            request: models.DescribeManagesRequest,
            opts: Dict = None,
    ) -> models.DescribeManagesResponse:
        """
        查看后台管理数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeManages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeManagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetDisks(
            self,
            request: models.DescribeNetDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeNetDisksResponse:
        """
        查看网盘泄露数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePorts(
            self,
            request: models.DescribePortsRequest,
            opts: Dict = None,
    ) -> models.DescribePortsResponse:
        """
        查看端口数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSeeds(
            self,
            request: models.DescribeSeedsRequest,
            opts: Dict = None,
    ) -> models.DescribeSeedsResponse:
        """
        查看种子列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSeeds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSeedsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSensitiveInfos(
            self,
            request: models.DescribeSensitiveInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeSensitiveInfosResponse:
        """
        查看敏感信息泄露数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSensitiveInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSensitiveInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubDomains(
            self,
            request: models.DescribeSubDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubDomainsResponse:
        """
        查看子域名数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSuspiciousAssets(
            self,
            request: models.DescribeSuspiciousAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSuspiciousAssetsResponse:
        """
        查看影子资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSuspiciousAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSuspiciousAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVuls(
            self,
            request: models.DescribeVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeVulsResponse:
        """
        查看漏洞数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeakPasswords(
            self,
            request: models.DescribeWeakPasswordsRequest,
            opts: Dict = None,
    ) -> models.DescribeWeakPasswordsResponse:
        """
        查看弱口令数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeakPasswords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeakPasswordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWechatApplets(
            self,
            request: models.DescribeWechatAppletsRequest,
            opts: Dict = None,
    ) -> models.DescribeWechatAppletsResponse:
        """
        查看微信小程序
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWechatApplets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWechatAppletsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWechatOfficialAccounts(
            self,
            request: models.DescribeWechatOfficialAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeWechatOfficialAccountsResponse:
        """
        查看公众号数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWechatOfficialAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWechatOfficialAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnoreData(
            self,
            request: models.IgnoreDataRequest,
            opts: Dict = None,
    ) -> models.IgnoreDataResponse:
        """
        忽略数据
        """
        
        kwargs = {}
        kwargs["action"] = "IgnoreData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnoreDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomer(
            self,
            request: models.ModifyCustomerRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomerResponse:
        """
        编辑企业
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLabel(
            self,
            request: models.ModifyLabelRequest,
            opts: Dict = None,
    ) -> models.ModifyLabelResponse:
        """
        修改标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySeedStatus(
            self,
            request: models.ModifySeedStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySeedStatusResponse:
        """
        修改种子状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySeedStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySeedStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopJobRecord(
            self,
            request: models.StopJobRecordRequest,
            opts: Dict = None,
    ) -> models.StopJobRecordResponse:
        """
        停止扫描
        """
        
        kwargs = {}
        kwargs["action"] = "StopJobRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopJobRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)