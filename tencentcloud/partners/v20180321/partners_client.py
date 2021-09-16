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
from tencentcloud.partners.v20180321 import models


class PartnersClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'partners.tencentcloudapi.com'
    _service = 'partners'


    def AgentPayDeals(self, request):
        """代理商支付订单接口，支持自付/代付

        :param request: Request instance for AgentPayDeals.
        :type request: :class:`tencentcloud.partners.v20180321.models.AgentPayDealsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.AgentPayDealsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AgentPayDeals", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AgentPayDealsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AgentTransferMoney(self, request):
        """为合作伙伴提供转账给客户能力。仅支持合作伙伴为自己名下客户转账。

        :param request: Request instance for AgentTransferMoney.
        :type request: :class:`tencentcloud.partners.v20180321.models.AgentTransferMoneyRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.AgentTransferMoneyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AgentTransferMoney", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AgentTransferMoneyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AuditApplyClient(self, request):
        """代理商可以审核其名下申请中代客

        :param request: Request instance for AuditApplyClient.
        :type request: :class:`tencentcloud.partners.v20180321.models.AuditApplyClientRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.AuditApplyClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AuditApplyClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AuditApplyClientResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePayRelationForClient(self, request):
        """合作伙伴为客户创建强代付关系

        :param request: Request instance for CreatePayRelationForClient.
        :type request: :class:`tencentcloud.partners.v20180321.models.CreatePayRelationForClientRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.CreatePayRelationForClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePayRelationForClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePayRelationForClientResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentAuditedClients(self, request):
        """查询已审核客户列表

        :param request: Request instance for DescribeAgentAuditedClients.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentAuditedClientsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentAuditedClientsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentAuditedClients", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentAuditedClientsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentBills(self, request):
        """代理商可查询自己及名下代客所有业务明细

        :param request: Request instance for DescribeAgentBills.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentBillsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentBillsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentBills", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentBillsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentClientGrade(self, request):
        """传入代客uin，查客户级别，客户审核状态，客户实名认证状态

        :param request: Request instance for DescribeAgentClientGrade.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientGradeRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientGradeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentClientGrade", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentClientGradeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentClients(self, request):
        """代理商可查询自己名下待审核客户列表

        :param request: Request instance for DescribeAgentClients.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentClientsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentClients", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentClientsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentDealsByCache(self, request):
        """供超大型代理商（代客数量>=3000 ）拉取缓存的全量客户订单。

        :param request: Request instance for DescribeAgentDealsByCache.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsByCacheRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsByCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentDealsByCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentDealsByCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentDealsCache(self, request):
        """【该接口将逐步下线，请切换使用升级版本DescribeAgentDealsByCache】供超大型代理商（代客数量>=3000 ）拉取缓存的全量客户订单。

        :param request: Request instance for DescribeAgentDealsCache.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsCacheRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentDealsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentDealsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentDealsCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentPayDeals(self, request):
        """【该接口将逐步下线，请切换使用升级版本DescribeAgentPayDealsV2】可以查询代理商代付的所有订单

        :param request: Request instance for DescribeAgentPayDeals.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentPayDealsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentPayDealsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentPayDeals", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentPayDealsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentPayDealsV2(self, request):
        """可以查询代理商代付的所有订单

        :param request: Request instance for DescribeAgentPayDealsV2.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentPayDealsV2Request`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentPayDealsV2Response`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentPayDealsV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentPayDealsV2Response()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentSelfPayDeals(self, request):
        """【该接口将逐步下线，请切换使用升级版本DescribeAgentSelfPayDealsV2】可以查询代理商下指定客户的自付订单

        :param request: Request instance for DescribeAgentSelfPayDeals.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentSelfPayDealsRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentSelfPayDealsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentSelfPayDeals", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentSelfPayDealsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentSelfPayDealsV2(self, request):
        """可以查询代理商下指定客户的自付订单

        :param request: Request instance for DescribeAgentSelfPayDealsV2.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeAgentSelfPayDealsV2Request`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeAgentSelfPayDealsV2Response`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentSelfPayDealsV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentSelfPayDealsV2Response()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClientBalance(self, request):
        """【该接口将逐步下线，请切换使用升级版本DescribeClientBalanceNew】为合作伙伴提供查询客户余额能力。调用者必须是合作伙伴，只能查询自己名下客户余额.

        :param request: Request instance for DescribeClientBalance.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeClientBalanceRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeClientBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClientBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClientBalanceNew(self, request):
        """为合作伙伴提供查询客户余额能力。调用者必须是合作伙伴，只能查询自己名下客户余额

        :param request: Request instance for DescribeClientBalanceNew.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeClientBalanceNewRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeClientBalanceNewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClientBalanceNew", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientBalanceNewResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRebateInfos(self, request):
        """代理商可查询自己名下全部返佣信息

        :param request: Request instance for DescribeRebateInfos.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeRebateInfosRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeRebateInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRebateInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRebateInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSalesmans(self, request):
        """代理商查询名下业务员列表信息

        :param request: Request instance for DescribeSalesmans.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeSalesmansRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeSalesmansResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSalesmans", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSalesmansResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUnbindClientList(self, request):
        """代理商名下客户解绑记录查询接口

        :param request: Request instance for DescribeUnbindClientList.
        :type request: :class:`tencentcloud.partners.v20180321.models.DescribeUnbindClientListRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.DescribeUnbindClientListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnbindClientList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnbindClientListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClientRemark(self, request):
        """代理商可以对名下客户添加备注、修改备注

        :param request: Request instance for ModifyClientRemark.
        :type request: :class:`tencentcloud.partners.v20180321.models.ModifyClientRemarkRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.ModifyClientRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClientRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClientRemarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemovePayRelationForClient(self, request):
        """合作伙伴为客户消除强代付关系

        :param request: Request instance for RemovePayRelationForClient.
        :type request: :class:`tencentcloud.partners.v20180321.models.RemovePayRelationForClientRequest`
        :rtype: :class:`tencentcloud.partners.v20180321.models.RemovePayRelationForClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemovePayRelationForClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemovePayRelationForClientResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)