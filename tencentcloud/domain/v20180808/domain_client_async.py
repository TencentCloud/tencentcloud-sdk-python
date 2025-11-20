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
from tencentcloud.domain.v20180808 import models
from typing import Dict


class DomainClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'domain.tencentcloudapi.com'
    _service = 'domain'

    async def BatchModifyDomainInfo(
            self,
            request: models.BatchModifyDomainInfoRequest,
            opts: Dict = None,
    ) -> models.BatchModifyDomainInfoResponse:
        """
        本接口 ( BatchModifyDomainInfo ) 用于批量域名信息修改 。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyDomainInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyDomainInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BidDetailPage(
            self,
            request: models.BidDetailPageRequest,
            opts: Dict = None,
    ) -> models.BidDetailPageResponse:
        """
        该接口用于用户详情页出价请求
        """
        
        kwargs = {}
        kwargs["action"] = "BidDetailPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BidDetailPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BidPreDomains(
            self,
            request: models.BidPreDomainsRequest,
            opts: Dict = None,
    ) -> models.BidPreDomainsResponse:
        """
        用户合作商预释放出价
        """
        
        kwargs = {}
        kwargs["action"] = "BidPreDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BidPreDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BiddingPreRelease(
            self,
            request: models.BiddingPreReleaseRequest,
            opts: Dict = None,
    ) -> models.BiddingPreReleaseResponse:
        """
        用于出价界面出价请求
        """
        
        kwargs = {}
        kwargs["action"] = "BiddingPreRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BiddingPreReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBatchStatus(
            self,
            request: models.CheckBatchStatusRequest,
            opts: Dict = None,
    ) -> models.CheckBatchStatusResponse:
        """
        本接口 ( CheckBatchStatus ) 用于查询批量操作日志状态 。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBatchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBatchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDomain(
            self,
            request: models.CheckDomainRequest,
            opts: Dict = None,
    ) -> models.CheckDomainResponse:
        """
        检查域名是否可以注册。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomDnsHost(
            self,
            request: models.CreateCustomDnsHostRequest,
            opts: Dict = None,
    ) -> models.CreateCustomDnsHostResponse:
        """
        创建自定义DNS Host
        域名在“正常状态”下可创建，域名如果“未实名”则无法创建，账户如果未实名则无法创建。
        默认每个域名 自定义DNS Host 数量不超过10个
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomDnsHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomDnsHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainBatch(
            self,
            request: models.CreateDomainBatchRequest,
            opts: Dict = None,
    ) -> models.CreateDomainBatchResponse:
        """
        本接口 ( CreateDomainBatch ) 用于批量域名注册 。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainRedemption(
            self,
            request: models.CreateDomainRedemptionRequest,
            opts: Dict = None,
    ) -> models.CreateDomainRedemptionResponse:
        """
        创建赎回订单。需要域名状态为：RedemptionPending：赎回期
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainRedemption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainRedemptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePhoneEmail(
            self,
            request: models.CreatePhoneEmailRequest,
            opts: Dict = None,
    ) -> models.CreatePhoneEmailResponse:
        """
        此接口用于创建有效的手机、邮箱
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePhoneEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePhoneEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTemplate(
            self,
            request: models.CreateTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTemplateResponse:
        """
        本接口 ( CreateTemplate ) 用于添加域名信息模板 。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBidding(
            self,
            request: models.DeleteBiddingRequest,
            opts: Dict = None,
    ) -> models.DeleteBiddingResponse:
        """
        删除记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBidding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBiddingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomDnsHost(
            self,
            request: models.DeleteCustomDnsHostRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomDnsHostResponse:
        """
        删除自定义DNS Host
        仅能删除域名在“正常状态”下，已经创建过的自定义Host，域名如果“未实名”或账户未实名，则无法操作
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomDnsHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomDnsHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePhoneEmail(
            self,
            request: models.DeletePhoneEmailRequest,
            opts: Dict = None,
    ) -> models.DeletePhoneEmailResponse:
        """
        此接口用于删除已验证的手机邮箱
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePhoneEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePhoneEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReservedPreDomainInfo(
            self,
            request: models.DeleteReservedPreDomainInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteReservedPreDomainInfoResponse:
        """
        用于清除多余的预定域名信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReservedPreDomainInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReservedPreDomainInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTemplate(
            self,
            request: models.DeleteTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteTemplateResponse:
        """
        本接口 ( DeleteTemplate ) 用于删除信息模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuctionList(
            self,
            request: models.DescribeAuctionListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuctionListResponse:
        """
        用户控制台获取竞价列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuctionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuctionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchOperationLogDetails(
            self,
            request: models.DescribeBatchOperationLogDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchOperationLogDetailsResponse:
        """
        本接口 ( DescribeBatchOperationLogDetails ) 用于获取批量操作日志详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchOperationLogDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchOperationLogDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchOperationLogs(
            self,
            request: models.DescribeBatchOperationLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchOperationLogsResponse:
        """
        本接口 ( DescribeBatchOperationLogs ) 用于获取批量操作日志 。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchOperationLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchOperationLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBiddingAppointDetail(
            self,
            request: models.DescribeBiddingAppointDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBiddingAppointDetailResponse:
        """
        我预约的域名-预约详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBiddingAppointDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBiddingAppointDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBiddingAppointList(
            self,
            request: models.DescribeBiddingAppointListRequest,
            opts: Dict = None,
    ) -> models.DescribeBiddingAppointListResponse:
        """
        我预定的域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBiddingAppointList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBiddingAppointListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBiddingDetail(
            self,
            request: models.DescribeBiddingDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBiddingDetailResponse:
        """
        我竞价的域名-竞价详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBiddingDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBiddingDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBiddingList(
            self,
            request: models.DescribeBiddingListRequest,
            opts: Dict = None,
    ) -> models.DescribeBiddingListResponse:
        """
        我竞价的域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBiddingList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBiddingListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBiddingSuccessfulDetail(
            self,
            request: models.DescribeBiddingSuccessfulDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBiddingSuccessfulDetailResponse:
        """
        我得标的域名-得标详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBiddingSuccessfulDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBiddingSuccessfulDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBiddingSuccessfulList(
            self,
            request: models.DescribeBiddingSuccessfulListRequest,
            opts: Dict = None,
    ) -> models.DescribeBiddingSuccessfulListResponse:
        """
        我得标的域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBiddingSuccessfulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBiddingSuccessfulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomDnsHostSet(
            self,
            request: models.DescribeCustomDnsHostSetRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomDnsHostSetResponse:
        """
        查询自定义DNS Host
        当前域名在任意状态下均可获取(根据域名当前状态，不一定能获取到具体数据)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomDnsHostSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomDnsHostSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainBaseInfo(
            self,
            request: models.DescribeDomainBaseInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainBaseInfoResponse:
        """
        本接口 (  DescribeDomainBaseInfo) 获取域名基本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainBaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainBaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainNameList(
            self,
            request: models.DescribeDomainNameListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainNameListResponse:
        """
        本接口 (  DescribeDomainNameList ) 我的域名列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainNameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainNameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainPriceList(
            self,
            request: models.DescribeDomainPriceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainPriceListResponse:
        """
        按照域名后缀获取对应的价格列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainPriceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainPriceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainSimpleInfo(
            self,
            request: models.DescribeDomainSimpleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainSimpleInfoResponse:
        """
        获取域名实名信息详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainSimpleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainSimpleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePayWaitDetail(
            self,
            request: models.DescribePayWaitDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePayWaitDetailResponse:
        """
        等待支付详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePayWaitDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePayWaitDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePhoneEmailList(
            self,
            request: models.DescribePhoneEmailListRequest,
            opts: Dict = None,
    ) -> models.DescribePhoneEmailListResponse:
        """
        本接口用于获取已验证的手机邮箱列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePhoneEmailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePhoneEmailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreAuctionList(
            self,
            request: models.DescribePreAuctionListRequest,
            opts: Dict = None,
    ) -> models.DescribePreAuctionListResponse:
        """
        用于预释放竞价列表数据查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreAuctionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreAuctionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreDomainList(
            self,
            request: models.DescribePreDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribePreDomainListResponse:
        """
        用户服务商提前获取预释放域名数据，查询数据根据结束时间进行倒序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreReleaseList(
            self,
            request: models.DescribePreReleaseListRequest,
            opts: Dict = None,
    ) -> models.DescribePreReleaseListResponse:
        """
        接口用于预释放页面查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreReleaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreReleaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedBidInfo(
            self,
            request: models.DescribeReservedBidInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedBidInfoResponse:
        """
        接口用于获取合作商竞价过程中竞价详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedBidInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedBidInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedPreDomainInfo(
            self,
            request: models.DescribeReservedPreDomainInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedPreDomainInfoResponse:
        """
        合作商用于查询预约预释放状态信息内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedPreDomainInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedPreDomainInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplate(
            self,
            request: models.DescribeTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateResponse:
        """
        本接口 (DescribeTemplate) 用于获取模板信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateList(
            self,
            request: models.DescribeTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateListResponse:
        """
        本接口 (DescribeTemplateList) 用于获取信息模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTldList(
            self,
            request: models.DescribeTldListRequest,
            opts: Dict = None,
    ) -> models.DescribeTldListResponse:
        """
        用于获取域名注册当前支持注册的后缀
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTldList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTldListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnPreDomainDetail(
            self,
            request: models.DescribeUnPreDomainDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeUnPreDomainDetailResponse:
        """
        查询预释放未预约域名详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnPreDomainDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnPreDomainDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomDnsHost(
            self,
            request: models.ModifyCustomDnsHostRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomDnsHostResponse:
        """
        修改自定义DNS Host
        域名在“正常状态”下可修改已经存在的自定义DNS Host，域名如果“未实名”则无法修改，账户如果未实名则无法修改。 默认每个域名 自定义DNS Host 数量不超过10个
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomDnsHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomDnsHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainDNSBatch(
            self,
            request: models.ModifyDomainDNSBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainDNSBatchResponse:
        """
        本接口 ( ModifyDomainDNSBatch) 用于批量域名 DNS 修改 。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainDNSBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainDNSBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainOwnerBatch(
            self,
            request: models.ModifyDomainOwnerBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainOwnerBatchResponse:
        """
        本接口 ( ModifyDomainOwnerBatch) 用于域名批量账号间转移 。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainOwnerBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainOwnerBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIntlCustomDnsHost(
            self,
            request: models.ModifyIntlCustomDnsHostRequest,
            opts: Dict = None,
    ) -> models.ModifyIntlCustomDnsHostResponse:
        """
        国际站-修改DNS Host
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIntlCustomDnsHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIntlCustomDnsHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTemplate(
            self,
            request: models.ModifyTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyTemplateResponse:
        """
        修改模板信息,仅能修改模板未通过审核的，即[模板详情](https://cloud.tencent.com/document/product/242/50018)中：AuditStatus不为Approved状态的
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDomainBatch(
            self,
            request: models.RenewDomainBatchRequest,
            opts: Dict = None,
    ) -> models.RenewDomainBatchResponse:
        """
        本接口 ( RenewDomainBatch ) 用于批量续费域名 。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReservedPreDomains(
            self,
            request: models.ReservedPreDomainsRequest,
            opts: Dict = None,
    ) -> models.ReservedPreDomainsResponse:
        """
        用于合作商对预释放域名进行预留。
        """
        
        kwargs = {}
        kwargs["action"] = "ReservedPreDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReservedPreDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendPhoneEmailCode(
            self,
            request: models.SendPhoneEmailCodeRequest,
            opts: Dict = None,
    ) -> models.SendPhoneEmailCodeResponse:
        """
        此接口用于发送手机邮箱验证码。
        """
        
        kwargs = {}
        kwargs["action"] = "SendPhoneEmailCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendPhoneEmailCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDomainAutoRenew(
            self,
            request: models.SetDomainAutoRenewRequest,
            opts: Dict = None,
    ) -> models.SetDomainAutoRenewResponse:
        """
        本接口 ( SetDomainAutoRenew ) 用于设置域名自动续费。
        当前操作暂不受域名状态限制
        """
        
        kwargs = {}
        kwargs["action"] = "SetDomainAutoRenew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDomainAutoRenewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncCustomDnsHost(
            self,
            request: models.SyncCustomDnsHostRequest,
            opts: Dict = None,
    ) -> models.SyncCustomDnsHostResponse:
        """
        同步自定义DNS Host，将域名已经设置的host配置数据从注册局同步下来
        """
        
        kwargs = {}
        kwargs["action"] = "SyncCustomDnsHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncCustomDnsHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferInDomainBatch(
            self,
            request: models.TransferInDomainBatchRequest,
            opts: Dict = None,
    ) -> models.TransferInDomainBatchResponse:
        """
        本接口 ( TransferInDomainBatch ) 用于批量转入域名 。
        """
        
        kwargs = {}
        kwargs["action"] = "TransferInDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferInDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferProhibitionBatch(
            self,
            request: models.TransferProhibitionBatchRequest,
            opts: Dict = None,
    ) -> models.TransferProhibitionBatchResponse:
        """
        本接口 ( TransferProhibitionBatch ) 用于批量禁止域名转移 。
        """
        
        kwargs = {}
        kwargs["action"] = "TransferProhibitionBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferProhibitionBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProhibitionBatch(
            self,
            request: models.UpdateProhibitionBatchRequest,
            opts: Dict = None,
    ) -> models.UpdateProhibitionBatchResponse:
        """
        本接口 ( UpdateProhibitionBatch ) 用于批量禁止更新锁。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProhibitionBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProhibitionBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadImage(
            self,
            request: models.UploadImageRequest,
            opts: Dict = None,
    ) -> models.UploadImageResponse:
        """
        本接口 ( UploadImage ) 用于证件图片上传 。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)