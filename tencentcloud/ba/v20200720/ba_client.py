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
from tencentcloud.ba.v20200720 import models


class BaClient(AbstractClient):
    _apiVersion = '2020-07-20'
    _endpoint = 'ba.tencentcloudapi.com'
    _service = 'ba'


    def CreateWeappQRUrl(self, request):
        """创建渠道备案小程序二维码

        :param request: Request instance for CreateWeappQRUrl.
        :type request: :class:`tencentcloud.ba.v20200720.models.CreateWeappQRUrlRequest`
        :rtype: :class:`tencentcloud.ba.v20200720.models.CreateWeappQRUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWeappQRUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWeappQRUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGetAuthInfo(self, request):
        """获取实名认证信息

        :param request: Request instance for DescribeGetAuthInfo.
        :type request: :class:`tencentcloud.ba.v20200720.models.DescribeGetAuthInfoRequest`
        :rtype: :class:`tencentcloud.ba.v20200720.models.DescribeGetAuthInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGetAuthInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGetAuthInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncIcpOrderWebInfo(self, request):
        """将备案ICP订单下的一个网站信息 同步给订单下其他网站，需要被同步的网站被检查通过(isCheck:true)；
        只有指定的网站信息字段能被同步

        :param request: Request instance for SyncIcpOrderWebInfo.
        :type request: :class:`tencentcloud.ba.v20200720.models.SyncIcpOrderWebInfoRequest`
        :rtype: :class:`tencentcloud.ba.v20200720.models.SyncIcpOrderWebInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncIcpOrderWebInfo", params, headers=headers)
            response = json.loads(body)
            model = models.SyncIcpOrderWebInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))