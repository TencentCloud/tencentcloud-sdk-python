# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.domain.v20180808 import models


class DomainClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'domain.tencentcloudapi.com'
    _service = 'domain'


    def BatchModifyDomainInfo(self, request):
        """本接口 ( BatchModifyDomainInfo ) 用于批量域名信息修改 。

        :param request: Request instance for BatchModifyDomainInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.BatchModifyDomainInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.BatchModifyDomainInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyDomainInfo", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyDomainInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BidDetailPage(self, request):
        """该接口用于用户详情页出价请求

        :param request: Request instance for BidDetailPage.
        :type request: :class:`tencentcloud.domain.v20180808.models.BidDetailPageRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.BidDetailPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BidDetailPage", params, headers=headers)
            response = json.loads(body)
            model = models.BidDetailPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BidPreDomains(self, request):
        """用户合作商预释放出价

        :param request: Request instance for BidPreDomains.
        :type request: :class:`tencentcloud.domain.v20180808.models.BidPreDomainsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.BidPreDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BidPreDomains", params, headers=headers)
            response = json.loads(body)
            model = models.BidPreDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BiddingPreRelease(self, request):
        """用于出价界面出价请求

        :param request: Request instance for BiddingPreRelease.
        :type request: :class:`tencentcloud.domain.v20180808.models.BiddingPreReleaseRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.BiddingPreReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BiddingPreRelease", params, headers=headers)
            response = json.loads(body)
            model = models.BiddingPreReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBatchStatus(self, request):
        """本接口 ( CheckBatchStatus ) 用于查询批量操作日志状态 。

        :param request: Request instance for CheckBatchStatus.
        :type request: :class:`tencentcloud.domain.v20180808.models.CheckBatchStatusRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CheckBatchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBatchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBatchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDomain(self, request):
        """检查域名是否可以注册。

        :param request: Request instance for CheckDomain.
        :type request: :class:`tencentcloud.domain.v20180808.models.CheckDomainRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CheckDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomDnsHost(self, request):
        """创建自定义DNS Host
        域名在“正常状态”下可创建，域名如果“未实名”则无法创建，账户如果未实名则无法创建。
        默认每个域名 自定义DNS Host 数量不超过10个

        :param request: Request instance for CreateCustomDnsHost.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateCustomDnsHostRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateCustomDnsHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomDnsHost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomDnsHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainBatch(self, request):
        """本接口 ( CreateDomainBatch ) 用于批量域名注册 。

        :param request: Request instance for CreateDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainRedemption(self, request):
        """创建赎回订单。需要域名状态为：RedemptionPending：赎回期

        :param request: Request instance for CreateDomainRedemption.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateDomainRedemptionRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateDomainRedemptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainRedemption", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainRedemptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePhoneEmail(self, request):
        """此接口用于创建有效的手机、邮箱

        :param request: Request instance for CreatePhoneEmail.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreatePhoneEmailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreatePhoneEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePhoneEmail", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePhoneEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTemplate(self, request):
        """本接口 ( CreateTemplate ) 用于添加域名信息模板 。

        :param request: Request instance for CreateTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBidding(self, request):
        """删除记录。

        :param request: Request instance for DeleteBidding.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeleteBiddingRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeleteBiddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBidding", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBiddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomDnsHost(self, request):
        """删除自定义DNS Host
        仅能删除域名在“正常状态”下，已经创建过的自定义Host，域名如果“未实名”或账户未实名，则无法操作

        :param request: Request instance for DeleteCustomDnsHost.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeleteCustomDnsHostRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeleteCustomDnsHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomDnsHost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomDnsHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePhoneEmail(self, request):
        """此接口用于删除已验证的手机邮箱

        :param request: Request instance for DeletePhoneEmail.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeletePhoneEmailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeletePhoneEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePhoneEmail", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePhoneEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReservedPreDomainInfo(self, request):
        """用于清除多余的预定域名信息

        :param request: Request instance for DeleteReservedPreDomainInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeleteReservedPreDomainInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeleteReservedPreDomainInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReservedPreDomainInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReservedPreDomainInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTemplate(self, request):
        """本接口 ( DeleteTemplate ) 用于删除信息模板。

        :param request: Request instance for DeleteTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeleteTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeleteTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuctionList(self, request):
        """用户控制台获取竞价列表

        :param request: Request instance for DescribeAuctionList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeAuctionListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeAuctionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuctionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuctionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchOperationLogDetails(self, request):
        """本接口 ( DescribeBatchOperationLogDetails ) 用于获取批量操作日志详情。

        :param request: Request instance for DescribeBatchOperationLogDetails.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogDetailsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchOperationLogDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchOperationLogDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchOperationLogs(self, request):
        """本接口 ( DescribeBatchOperationLogs ) 用于获取批量操作日志 。

        :param request: Request instance for DescribeBatchOperationLogs.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchOperationLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchOperationLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBiddingAppointDetail(self, request):
        """我预约的域名-预约详情。

        :param request: Request instance for DescribeBiddingAppointDetail.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingAppointDetailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingAppointDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBiddingAppointDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBiddingAppointDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBiddingAppointList(self, request):
        """我预定的域名。

        :param request: Request instance for DescribeBiddingAppointList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingAppointListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingAppointListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBiddingAppointList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBiddingAppointListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBiddingDetail(self, request):
        """我竞价的域名-竞价详情。

        :param request: Request instance for DescribeBiddingDetail.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingDetailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBiddingDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBiddingDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBiddingList(self, request):
        """我竞价的域名。

        :param request: Request instance for DescribeBiddingList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBiddingList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBiddingListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBiddingSuccessfulDetail(self, request):
        """我得标的域名-得标详情。

        :param request: Request instance for DescribeBiddingSuccessfulDetail.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingSuccessfulDetailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingSuccessfulDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBiddingSuccessfulDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBiddingSuccessfulDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBiddingSuccessfulList(self, request):
        """我得标的域名。

        :param request: Request instance for DescribeBiddingSuccessfulList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingSuccessfulListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBiddingSuccessfulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBiddingSuccessfulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBiddingSuccessfulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomDnsHostSet(self, request):
        """查询自定义DNS Host
        当前域名在任意状态下均可获取(根据域名当前状态，不一定能获取到具体数据)

        :param request: Request instance for DescribeCustomDnsHostSet.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeCustomDnsHostSetRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeCustomDnsHostSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomDnsHostSet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomDnsHostSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainBaseInfo(self, request):
        """本接口 (  DescribeDomainBaseInfo) 获取域名基本信息。

        :param request: Request instance for DescribeDomainBaseInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainBaseInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainBaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainBaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainBaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainNameList(self, request):
        """本接口 (  DescribeDomainNameList ) 我的域名列表。

        :param request: Request instance for DescribeDomainNameList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainNameListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainNameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainNameList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainNameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainPriceList(self, request):
        """按照域名后缀获取对应的价格列表

        :param request: Request instance for DescribeDomainPriceList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainPriceListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainPriceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainPriceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainPriceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainSimpleInfo(self, request):
        """获取域名实名信息详情

        :param request: Request instance for DescribeDomainSimpleInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainSimpleInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainSimpleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainSimpleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainSimpleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePayWaitDetail(self, request):
        """等待支付详情接口

        :param request: Request instance for DescribePayWaitDetail.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribePayWaitDetailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribePayWaitDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePayWaitDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePayWaitDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePhoneEmailList(self, request):
        """本接口用于获取已验证的手机邮箱列表

        :param request: Request instance for DescribePhoneEmailList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribePhoneEmailListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribePhoneEmailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePhoneEmailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePhoneEmailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreAuctionList(self, request):
        """用于预释放竞价列表数据查询

        :param request: Request instance for DescribePreAuctionList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribePreAuctionListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribePreAuctionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreAuctionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreAuctionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreDomainList(self, request):
        """用户服务商提前获取预释放域名数据，查询数据根据结束时间进行倒序。

        :param request: Request instance for DescribePreDomainList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribePreDomainListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribePreDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreReleaseList(self, request):
        """接口用于预释放页面查询

        :param request: Request instance for DescribePreReleaseList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribePreReleaseListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribePreReleaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreReleaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreReleaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReservedBidInfo(self, request):
        """接口用于获取合作商竞价过程中竞价详情数据

        :param request: Request instance for DescribeReservedBidInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeReservedBidInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeReservedBidInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReservedBidInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReservedBidInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReservedPreDomainInfo(self, request):
        """合作商用于查询预约预释放状态信息内容

        :param request: Request instance for DescribeReservedPreDomainInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeReservedPreDomainInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeReservedPreDomainInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReservedPreDomainInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReservedPreDomainInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplate(self, request):
        """本接口 (DescribeTemplate) 用于获取模板信息。

        :param request: Request instance for DescribeTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateList(self, request):
        """本接口 (DescribeTemplateList) 用于获取信息模板列表。

        :param request: Request instance for DescribeTemplateList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTldList(self, request):
        """用于获取域名注册当前支持注册的后缀

        :param request: Request instance for DescribeTldList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeTldListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeTldListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTldList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTldListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnPreDomainDetail(self, request):
        """查询预释放未预约域名详情接口

        :param request: Request instance for DescribeUnPreDomainDetail.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeUnPreDomainDetailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeUnPreDomainDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnPreDomainDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnPreDomainDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomDnsHost(self, request):
        """修改自定义DNS Host
        域名在“正常状态”下可修改已经存在的自定义DNS Host，域名如果“未实名”则无法修改，账户如果未实名则无法修改。 默认每个域名 自定义DNS Host 数量不超过10个

        :param request: Request instance for ModifyCustomDnsHost.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyCustomDnsHostRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyCustomDnsHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomDnsHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomDnsHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainDNSBatch(self, request):
        """本接口 ( ModifyDomainDNSBatch) 用于批量域名 DNS 修改 。

        :param request: Request instance for ModifyDomainDNSBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyDomainDNSBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyDomainDNSBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainDNSBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainDNSBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainOwnerBatch(self, request):
        """本接口 ( ModifyDomainOwnerBatch) 用于域名批量账号间转移 。

        :param request: Request instance for ModifyDomainOwnerBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyDomainOwnerBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyDomainOwnerBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainOwnerBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainOwnerBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIntlCustomDnsHost(self, request):
        """国际站-修改DNS Host

        :param request: Request instance for ModifyIntlCustomDnsHost.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyIntlCustomDnsHostRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyIntlCustomDnsHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIntlCustomDnsHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIntlCustomDnsHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTemplate(self, request):
        """修改模板信息

        :param request: Request instance for ModifyTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDomainBatch(self, request):
        """本接口 ( RenewDomainBatch ) 用于批量续费域名 。

        :param request: Request instance for RenewDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.RenewDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.RenewDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReservedPreDomains(self, request):
        """用于合作商对预释放域名进行预留。

        :param request: Request instance for ReservedPreDomains.
        :type request: :class:`tencentcloud.domain.v20180808.models.ReservedPreDomainsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ReservedPreDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReservedPreDomains", params, headers=headers)
            response = json.loads(body)
            model = models.ReservedPreDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendPhoneEmailCode(self, request):
        """此接口用于发送手机邮箱验证码。

        :param request: Request instance for SendPhoneEmailCode.
        :type request: :class:`tencentcloud.domain.v20180808.models.SendPhoneEmailCodeRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.SendPhoneEmailCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendPhoneEmailCode", params, headers=headers)
            response = json.loads(body)
            model = models.SendPhoneEmailCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetDomainAutoRenew(self, request):
        """本接口 ( SetDomainAutoRenew ) 用于设置域名自动续费。
        当前操作暂不受域名状态限制

        :param request: Request instance for SetDomainAutoRenew.
        :type request: :class:`tencentcloud.domain.v20180808.models.SetDomainAutoRenewRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.SetDomainAutoRenewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDomainAutoRenew", params, headers=headers)
            response = json.loads(body)
            model = models.SetDomainAutoRenewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncCustomDnsHost(self, request):
        """同步自定义DNS Host，将域名已经设置的host配置数据从注册局同步下来

        :param request: Request instance for SyncCustomDnsHost.
        :type request: :class:`tencentcloud.domain.v20180808.models.SyncCustomDnsHostRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.SyncCustomDnsHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncCustomDnsHost", params, headers=headers)
            response = json.loads(body)
            model = models.SyncCustomDnsHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransferInDomainBatch(self, request):
        """本接口 ( TransferInDomainBatch ) 用于批量转入域名 。

        :param request: Request instance for TransferInDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.TransferInDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.TransferInDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransferInDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.TransferInDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransferProhibitionBatch(self, request):
        """本接口 ( TransferProhibitionBatch ) 用于批量禁止域名转移 。

        :param request: Request instance for TransferProhibitionBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.TransferProhibitionBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.TransferProhibitionBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransferProhibitionBatch", params, headers=headers)
            response = json.loads(body)
            model = models.TransferProhibitionBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProhibitionBatch(self, request):
        """本接口 ( UpdateProhibitionBatch ) 用于批量禁止更新锁。

        :param request: Request instance for UpdateProhibitionBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.UpdateProhibitionBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.UpdateProhibitionBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProhibitionBatch", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProhibitionBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadImage(self, request):
        """本接口 ( UploadImage ) 用于证件图片上传 。

        :param request: Request instance for UploadImage.
        :type request: :class:`tencentcloud.domain.v20180808.models.UploadImageRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.UploadImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadImage", params, headers=headers)
            response = json.loads(body)
            model = models.UploadImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))