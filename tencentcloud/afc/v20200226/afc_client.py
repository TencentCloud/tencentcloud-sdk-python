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
from tencentcloud.afc.v20200226 import models


class AfcClient(AbstractClient):
    _apiVersion = '2020-02-26'
    _endpoint = 'afc.tencentcloudapi.com'
    _service = 'afc'


    def GetAntiFraudVip(self, request):
        r"""反欺诈VIP评分接口

        :param request: Request instance for GetAntiFraudVip.
        :type request: :class:`tencentcloud.afc.v20200226.models.GetAntiFraudVipRequest`
        :rtype: :class:`tencentcloud.afc.v20200226.models.GetAntiFraudVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAntiFraudVip", params, headers=headers)
            response = json.loads(body)
            model = models.GetAntiFraudVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryAntiFraudVip(self, request):
        r"""天御反欺诈服务，主要应用于银行、证券、保险、P2P等金融行业客户，通过腾讯的大数据风控能力，
        可以准确识别恶意用户信息，解决客户在支付、活动、理财，风控等业务环节遇到的欺诈威胁，降低企业
        的损失。

        :param request: Request instance for QueryAntiFraudVip.
        :type request: :class:`tencentcloud.afc.v20200226.models.QueryAntiFraudVipRequest`
        :rtype: :class:`tencentcloud.afc.v20200226.models.QueryAntiFraudVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAntiFraudVip", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAntiFraudVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransportGeneralInterface(self, request):
        r"""天御信鸽取数平台接口

        :param request: Request instance for TransportGeneralInterface.
        :type request: :class:`tencentcloud.afc.v20200226.models.TransportGeneralInterfaceRequest`
        :rtype: :class:`tencentcloud.afc.v20200226.models.TransportGeneralInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransportGeneralInterface", params, headers=headers)
            response = json.loads(body)
            model = models.TransportGeneralInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))