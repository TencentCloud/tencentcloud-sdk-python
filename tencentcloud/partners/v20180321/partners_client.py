# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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