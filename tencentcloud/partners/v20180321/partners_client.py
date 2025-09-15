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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.partners.v20180321 import models


class PartnersClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'partners.tencentcloudapi.com'
    _service = 'partners'


    def AgentPayDeals(self, request):
        r"""代理商支付订单接口，支持自付/代付

        :param request: Request instance for AgentPayDeals.
        :type request: :class:`tencentcloud.partners.v20180321.models.AgentPayDealsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.AgentPayDealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AgentPayDeals", params, headers=headers)
            response = json.loads(body)
            model = models.AgentPayDealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AgentTransferMoney(self, request):
        r"""为合作伙伴提供转账给客户能力。仅支持合作伙伴为自己名下客户转账。

        :param request: Request instance for AgentTransferMoney.
        :type request: :class:`tencentcloud.partners.v20180321.models.AgentTransferMoneyRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.AgentTransferMoneyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AgentTransferMoney", params, headers=headers)
            response = json.loads(body)
            model = models.AgentTransferMoneyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignClientsToSales(self, request):
        r"""为代客or申请中代客分派跟进人（业务员），入参可从以下API获取
        - 代客列表获取API： [DescribeAgentAuditedClients](https://cloud.tencent.com/document/product/563/19184)
        - 申请中代客列表获取API：[DescribeAgentClients](https://cloud.tencent.com/document/product/563/16046)
        - 业务员列表获取API：[DescribeSalesmans](https://cloud.tencent.com/document/product/563/35196) <br><br>

        :param request: Request instance for AssignClientsToSales.
        :type request: :class:`tencentcloud.partners.v20180321.models.AssignClientsToSalesRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.AssignClientsToSalesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignClientsToSales", params, headers=headers)
            response = json.loads(body)
            model = models.AssignClientsToSalesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AuditApplyClient(self, request):
        r"""代理商可以审核其名下申请中代客

        :param request: Request instance for AuditApplyClient.
        :type request: :class:`tencentcloud.partners.v20180321.models.AuditApplyClientRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.AuditApplyClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuditApplyClient", params, headers=headers)
            response = json.loads(body)
            model = models.AuditApplyClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePayRelationForClient(self, request):
        r"""合作伙伴为客户创建强代付关系

        :param request: Request instance for CreatePayRelationForClient.
        :type request: :class:`tencentcloud.partners.v20180321.models.CreatePayRelationForClientRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.CreatePayRelationForClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePayRelationForClient", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePayRelationForClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentAuditedClients(self, request):
        r"""查询已审核客户列表

        :param request: Request instance for DescribeAgentAuditedClients.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentAuditedClientsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentAuditedClientsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentAuditedClients", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentAuditedClientsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentBills(self, request):
        r"""代理商可查询自己及名下代客所有业务明细

        :param request: Request instance for DescribeAgentBills.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentBillsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentBillsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentBills", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentBillsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentClientGrade(self, request):
        r"""传入代客uin，查客户级别，客户审核状态，客户实名认证状态

        :param request: Request instance for DescribeAgentClientGrade.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientGradeRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientGradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentClientGrade", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentClientGradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentClients(self, request):
        r"""代理商可查询自己名下待审核客户列表

        :param request: Request instance for DescribeAgentClients.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentClients", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentClientsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentDealsByCache(self, request):
        r"""供代理商拉取全量预付费普通客户订单
        （对应控制台：客户订单-预付费-普通订单）

        :param request: Request instance for DescribeAgentDealsByCache.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsByCacheRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsByCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDealsByCache", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentDealsByCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentDealsPriceDetailByDealName(self, request):
        r"""供代理商使用名下有效普通代客的预付费子订单号查询订单费用详情

        :param request: Request instance for DescribeAgentDealsPriceDetailByDealName.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsPriceDetailByDealNameRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsPriceDetailByDealNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDealsPriceDetailByDealName", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentDealsPriceDetailByDealNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentPayDealsV2(self, request):
        r"""查询最近15天内的代理商代付订单

        :param request: Request instance for DescribeAgentPayDealsV2.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentPayDealsV2Request`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentPayDealsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentPayDealsV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentPayDealsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentRelateBigDealIds(self, request):
        r"""根据大订单号查询关联申请合并支付的其他订单号

        :param request: Request instance for DescribeAgentRelateBigDealIds.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentRelateBigDealIdsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentRelateBigDealIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentRelateBigDealIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentRelateBigDealIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentSelfPayDealsV2(self, request):
        r"""查询代理商名下指定代客最近15天内的自付订单（预付费）

        :param request: Request instance for DescribeAgentSelfPayDealsV2.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentSelfPayDealsV2Request`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentSelfPayDealsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentSelfPayDealsV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentSelfPayDealsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientBalanceNew(self, request):
        r"""为合作伙伴提供查询客户余额能力。调用者必须是合作伙伴，只能查询自己名下客户余额

        :param request: Request instance for DescribeClientBalanceNew.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeClientBalanceNewRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeClientBalanceNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientBalanceNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientBalanceNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientJoinIncreaseList(self, request):
        r"""查询合作伙伴名下客户的参与增量激励考核信息列表

        :param request: Request instance for DescribeClientJoinIncreaseList.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeClientJoinIncreaseListRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeClientJoinIncreaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientJoinIncreaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientJoinIncreaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientSwitchTraTaskInfo(self, request):
        r"""查询客户的交易类型切换任务的信息，查询成功则获取当前用户的切换链接，查询失败则返回失败的原因

        :param request: Request instance for DescribeClientSwitchTraTaskInfo.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeClientSwitchTraTaskInfoRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeClientSwitchTraTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientSwitchTraTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientSwitchTraTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRebateInfos(self, request):
        r"""【该接口已下线，请切换使用升级版本DescribeRebateInfosNew】代理商可查询自己名下全部返佣信息

        :param request: Request instance for DescribeRebateInfos.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeRebateInfosRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeRebateInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRebateInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRebateInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRebateInfosNew(self, request):
        r"""代理商可查询自己名下全部返佣信息

        :param request: Request instance for DescribeRebateInfosNew.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeRebateInfosNewRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeRebateInfosNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRebateInfosNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRebateInfosNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSalesmans(self, request):
        r"""代理商查询名下业务员列表信息

        :param request: Request instance for DescribeSalesmans.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeSalesmansRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeSalesmansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSalesmans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSalesmansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnbindClientList(self, request):
        r"""代理商名下客户解绑记录查询接口

        :param request: Request instance for DescribeUnbindClientList.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeUnbindClientListRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeUnbindClientListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnbindClientList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnbindClientListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClientRemark(self, request):
        r"""代理商可以对名下客户添加备注、修改备注

        :param request: Request instance for ModifyClientRemark.
        :type request: :class:`tencentcloud.partners.v20180321.models.ModifyClientRemarkRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.ModifyClientRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClientRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClientRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemovePayRelationForClient(self, request):
        r"""合作伙伴为客户消除强代付关系

        :param request: Request instance for RemovePayRelationForClient.
        :type request: :class:`tencentcloud.partners.v20180321.models.RemovePayRelationForClientRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.RemovePayRelationForClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemovePayRelationForClient", params, headers=headers)
            response = json.loads(body)
            model = models.RemovePayRelationForClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))