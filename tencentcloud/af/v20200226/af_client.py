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
from tencentcloud.af.v20200226 import models


class AfClient(AbstractClient):
    _apiVersion = '2020-02-26'
    _endpoint = 'af.tencentcloudapi.com'
    _service = 'af'


    def DescribeAntiFraud(self, request):
        """该接口未在使用，后端地址已无法访问，经查近60天日志无正常业务访问记录，申请预下线。

        天御反欺诈服务，主要应用于银行、证券、保险、消费金融等金融行业客户，通过腾讯的大数据风控能力，
        可以准确识别恶意用户信息，解决客户在支付、活动、理财，风控等业务环节遇到的欺诈威胁，降低企业
        的损失。

        :param request: Request instance for DescribeAntiFraud.
        :type request: :class:`tencentcloud.af.v20200226.models.DescribeAntiFraudRequest`
        :rtype: :class:`tencentcloud.af.v20200226.models.DescribeAntiFraudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiFraud", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiFraudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAntiFraud(self, request):
        """反欺诈评分接口

        :param request: Request instance for GetAntiFraud.
        :type request: :class:`tencentcloud.af.v20200226.models.GetAntiFraudRequest`
        :rtype: :class:`tencentcloud.af.v20200226.models.GetAntiFraudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAntiFraud", params, headers=headers)
            response = json.loads(body)
            model = models.GetAntiFraudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryAntiFraud(self, request):
        """天御反欺诈服务，主要应用于银行、证券、保险、消费金融等金融行业客户，通过腾讯的大数据风控能力，
        可以准确识别恶意用户信息，解决客户在支付、活动、理财，风控等业务环节遇到的欺诈威胁，降低企业
        的损失。

        :param request: Request instance for QueryAntiFraud.
        :type request: :class:`tencentcloud.af.v20200226.models.QueryAntiFraudRequest`
        :rtype: :class:`tencentcloud.af.v20200226.models.QueryAntiFraudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAntiFraud", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAntiFraudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))