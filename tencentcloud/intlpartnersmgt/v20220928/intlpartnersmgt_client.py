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
from tencentcloud.intlpartnersmgt.v20220928 import models


class IntlpartnersmgtClient(AbstractClient):
    _apiVersion = '2022-09-28'
    _endpoint = 'intlpartnersmgt.tencentcloudapi.com'
    _service = 'intlpartnersmgt'


    def AllocateCustomerCredit(self, request):
        """合作伙伴可以为关联客户设置信用额度，包括调高额度、降低额度、设置额度为0
        1、信用额度长期有效，不会定期清0；
        2、可用信用额度为0，会触发客户停服，请谨慎操作；
        3、如需限制客户新购，但不影响已购产品使用，可与渠道经理申请客户欠费不停服特权后，设置可用信用额度为0；
        4、设置的额度，为当前可用信用额度的增量，最大不能超过合作伙伴可分配的剩余额度，设置负数代表回收额度，可用信用额度最低设置为0。

        :param request: Request instance for AllocateCustomerCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCustomerCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.AllocateCustomerCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateCustomerCredit", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateCustomerCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccount(self, request):
        """在合作伙伴平台，创建腾讯云账号，子客户注册完成后，自动与合作伙伴账号绑定。

        注意事项：<br>
        1、创建腾讯云账号，输入的邮箱、手机号，需要合作伙伴做有效性验证。<br>
        2、客户首次登录需要补充个人信息

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetCountryCodes(self, request):
        """获取国家和地区的代码

        :param request: Request instance for GetCountryCodes.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.GetCountryCodesRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.GetCountryCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCountryCodes", params, headers=headers)
            response = json.loads(body)
            model = models.GetCountryCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCreditAllocationHistory(self, request):
        """查询单个客户的全部历史分配记录

        :param request: Request instance for QueryCreditAllocationHistory.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditAllocationHistoryRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditAllocationHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCreditAllocationHistory", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCreditAllocationHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCreditByUinList(self, request):
        """查询用户列表信用

        :param request: Request instance for QueryCreditByUinList.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditByUinListRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCreditByUinListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCreditByUinList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCreditByUinListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCustomersCredit(self, request):
        """合作伙伴可以查询关联客户的信用额度，以及客户的基础信息

        :param request: Request instance for QueryCustomersCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomersCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryCustomersCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCustomersCredit", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCustomersCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryDirectCustomersCredit(self, request):
        """查询直接子客信用

        :param request: Request instance for QueryDirectCustomersCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryDirectCustomersCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryDirectCustomersCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDirectCustomersCredit", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDirectCustomersCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryPartnerCredit(self, request):
        """查询合作伙伴自己的总信用额度、可用信用额度、已使用信用额度，单位为美元

        :param request: Request instance for QueryPartnerCredit.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPartnerCreditRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryPartnerCreditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPartnerCredit", params, headers=headers)
            response = json.loads(body)
            model = models.QueryPartnerCreditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryVoucherAmountByUin(self, request):
        """根据客户uin查询代金券额度

        :param request: Request instance for QueryVoucherAmountByUin.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherAmountByUinRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherAmountByUinResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVoucherAmountByUin", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVoucherAmountByUinResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryVoucherListByUin(self, request):
        """根据客户uin查询代金券列表

        :param request: Request instance for QueryVoucherListByUin.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherListByUinRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherListByUinResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVoucherListByUin", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVoucherListByUinResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryVoucherPool(self, request):
        """查询代金券额度池

        :param request: Request instance for QueryVoucherPool.
        :type request: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherPoolRequest`
        :rtype: :class:`tencentcloud.intlpartnersmgt.v20220928.models.QueryVoucherPoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVoucherPool", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVoucherPoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)