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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ba.v20200720 import models
from typing import Dict


class BaClient(AbstractClient):
    _apiVersion = '2020-07-20'
    _endpoint = 'ba.tencentcloudapi.com'
    _service = 'ba'

    async def CreateWeappQRUrl(
            self,
            request: models.CreateWeappQRUrlRequest,
            opts: Dict = None,
    ) -> models.CreateWeappQRUrlResponse:
        """
        创建渠道备案小程序二维码
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWeappQRUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWeappQRUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGetAuthInfo(
            self,
            request: models.DescribeGetAuthInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeGetAuthInfoResponse:
        """
        获取实名认证信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGetAuthInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGetAuthInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncIcpOrderWebInfo(
            self,
            request: models.SyncIcpOrderWebInfoRequest,
            opts: Dict = None,
    ) -> models.SyncIcpOrderWebInfoResponse:
        """
        将备案ICP订单下的一个网站信息 同步给订单下其他网站，需要被同步的网站被检查通过(isCheck:true)；
        只有指定的网站信息字段能被同步
        """
        
        kwargs = {}
        kwargs["action"] = "SyncIcpOrderWebInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncIcpOrderWebInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)