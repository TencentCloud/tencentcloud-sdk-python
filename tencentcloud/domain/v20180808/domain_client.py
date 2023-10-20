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
        """创建赎回订单。

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


    def DeleteCustomDnsHost(self, request):
        """删除自定义DNS Host

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


    def DescribeCustomDnsHostSet(self, request):
        """查询自定义DNS Host

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


    def ModifyCustomDnsHost(self, request):
        """修改自定义DNS Host

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
        """本接口 ( ModifyDomainDNSBatch) 用于批量域名 DNS 修改 。

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
        """同步自定义DNS Host

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