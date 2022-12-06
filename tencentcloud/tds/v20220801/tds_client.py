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
from tencentcloud.tds.v20220801 import models


class TdsClient(AbstractClient):
    _apiVersion = '2022-08-01'
    _endpoint = 'tds.tencentcloudapi.com'
    _service = 'tds'


    def DescribeFraudBase(self, request):
        """查询设备风险

        :param request: Request instance for DescribeFraudBase.
        :type request: :class:`tencentcloud.tds.v20220801.models.DescribeFraudBaseRequest`
        :rtype: :class:`tencentcloud.tds.v20220801.models.DescribeFraudBaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFraudBase", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFraudBaseResponse()
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


    def DescribeFraudPremium(self, request):
        """查询设备标识及风险

        :param request: Request instance for DescribeFraudPremium.
        :type request: :class:`tencentcloud.tds.v20220801.models.DescribeFraudPremiumRequest`
        :rtype: :class:`tencentcloud.tds.v20220801.models.DescribeFraudPremiumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFraudPremium", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFraudPremiumResponse()
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


    def DescribeFraudUltimate(self, request):
        """查询设备标识及风险（旗舰版）

        :param request: Request instance for DescribeFraudUltimate.
        :type request: :class:`tencentcloud.tds.v20220801.models.DescribeFraudUltimateRequest`
        :rtype: :class:`tencentcloud.tds.v20220801.models.DescribeFraudUltimateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFraudUltimate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFraudUltimateResponse()
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


    def DescribeTrustedID(self, request):
        """查询设备标识

        :param request: Request instance for DescribeTrustedID.
        :type request: :class:`tencentcloud.tds.v20220801.models.DescribeTrustedIDRequest`
        :rtype: :class:`tencentcloud.tds.v20220801.models.DescribeTrustedIDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrustedID", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrustedIDResponse()
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