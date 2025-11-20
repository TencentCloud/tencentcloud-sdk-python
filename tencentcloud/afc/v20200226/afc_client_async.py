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
from tencentcloud.afc.v20200226 import models
from typing import Dict


class AfcClient(AbstractClient):
    _apiVersion = '2020-02-26'
    _endpoint = 'afc.tencentcloudapi.com'
    _service = 'afc'

    async def GetAntiFraudVip(
            self,
            request: models.GetAntiFraudVipRequest,
            opts: Dict = None,
    ) -> models.GetAntiFraudVipResponse:
        """
        反欺诈VIP评分接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetAntiFraudVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAntiFraudVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAntiFraudVip(
            self,
            request: models.QueryAntiFraudVipRequest,
            opts: Dict = None,
    ) -> models.QueryAntiFraudVipResponse:
        """
        天御反欺诈服务，主要应用于银行、证券、保险、P2P等金融行业客户，通过腾讯的大数据风控能力，
        可以准确识别恶意用户信息，解决客户在支付、活动、理财，风控等业务环节遇到的欺诈威胁，降低企业
        的损失。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAntiFraudVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAntiFraudVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransportGeneralInterface(
            self,
            request: models.TransportGeneralInterfaceRequest,
            opts: Dict = None,
    ) -> models.TransportGeneralInterfaceResponse:
        """
        天御信鸽取数平台接口
        """
        
        kwargs = {}
        kwargs["action"] = "TransportGeneralInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransportGeneralInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)