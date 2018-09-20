# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def AgentPayDeals(self, request):
        """代理商支付订单接口，支持自付/代付

        :param request: 调用AgentPayDeals所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AgentTransferMoney(self, request):
        """为合作伙伴提供转账给客户能力。仅支持合作伙伴为自己名下客户转账。

        :param request: 调用AgentTransferMoney所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AuditApplyClient(self, request):
        """代理商可以审核其名下申请中代客

        :param request: 调用AuditApplyClient所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentAuditedClients(self, request):
        """查询已审核客户列表

        :param request: 调用DescribeAgentAuditedClients所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentBills(self, request):
        """代理商可查询自己及名下代客所有业务明细

        :param request: 调用DescribeAgentBills所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentClients(self, request):
        """代理商可查询自己名下待审核客户列表

        :param request: 调用DescribeAgentClients所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClientBalance(self, request):
        """为合作伙伴提供查询客户余额能力。调用者必须是合作伙伴，只能查询自己名下客户余额

        :param request: 调用DescribeClientBalance所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRebateInfos(self, request):
        """代理商可查询自己名下全部返佣信息

        :param request: 调用DescribeRebateInfos所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClientRemark(self, request):
        """代理商可以对名下客户添加备注、修改备注

        :param request: 调用ModifyClientRemark所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)