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
from tencentcloud.af.v20200226 import models
from typing import Dict


class AfClient(AbstractClient):
    _apiVersion = '2020-02-26'
    _endpoint = 'af.tencentcloudapi.com'
    _service = 'af'

    async def DescribeAntiFraud(
            self,
            request: models.DescribeAntiFraudRequest,
            opts: Dict = None,
    ) -> models.DescribeAntiFraudResponse:
        """
        该接口未在使用，后端地址已无法访问，经查近60天日志无正常业务访问记录，申请预下线。

        天御反欺诈服务，主要应用于银行、证券、保险、消费金融等金融行业客户，通过腾讯的大数据风控能力，
        可以准确识别恶意用户信息，解决客户在支付、活动、理财，风控等业务环节遇到的欺诈威胁，降低企业
        的损失。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAntiFraud"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAntiFraudResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAntiFraud(
            self,
            request: models.GetAntiFraudRequest,
            opts: Dict = None,
    ) -> models.GetAntiFraudResponse:
        """
        反欺诈评分接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetAntiFraud"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAntiFraudResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAntiFraud(
            self,
            request: models.QueryAntiFraudRequest,
            opts: Dict = None,
    ) -> models.QueryAntiFraudResponse:
        """
        天御反欺诈服务，主要应用于银行、证券、保险、消费金融等金融行业客户，通过腾讯的大数据风控能力，
        可以准确识别恶意用户信息，解决客户在支付、活动、理财，风控等业务环节遇到的欺诈威胁，降低企业
        的损失。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAntiFraud"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAntiFraudResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)