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
from tencentcloud.rkp.v20191209 import models


class RkpClient(AbstractClient):
    _apiVersion = '2019-12-09'
    _endpoint = 'rkp.tencentcloudapi.com'


    def GetOpenId(self, request):
        """根据DevicceToken查询OpenID。

        :param request: Request instance for GetOpenId.
        :type request: :class:`tencentcloud.rkp.v20191209.models.GetOpenIdRequest`
        :rtype: :class:`tencentcloud.rkp.v20191209.models.GetOpenIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetOpenId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetOpenIdResponse()
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


    def GetToken(self, request):
        """获取token接口。

        :param request: Request instance for GetToken.
        :type request: :class:`tencentcloud.rkp.v20191209.models.GetTokenRequest`
        :rtype: :class:`tencentcloud.rkp.v20191209.models.GetTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTokenResponse()
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


    def QueryDevAndRisk(self, request):
        """腾讯天御设备风险查询接口，输入由客户应用自主采集的设备信息， 通过腾讯大数据风控能力，可以准确根据输入设备信息，还原设备库中的设备ID，并且识别设备的风险，解决客户业务过程中的设备风险，降低企业损失。

        :param request: Request instance for QueryDevAndRisk.
        :type request: :class:`tencentcloud.rkp.v20191209.models.QueryDevAndRiskRequest`
        :rtype: :class:`tencentcloud.rkp.v20191209.models.QueryDevAndRiskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryDevAndRisk", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryDevAndRiskResponse()
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