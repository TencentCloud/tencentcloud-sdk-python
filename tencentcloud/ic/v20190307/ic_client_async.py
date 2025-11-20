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
from tencentcloud.ic.v20190307 import models
from typing import Dict


class IcClient(AbstractClient):
    _apiVersion = '2019-03-07'
    _endpoint = 'ic.tencentcloudapi.com'
    _service = 'ic'

    async def DescribeApp(
            self,
            request: models.DescribeAppRequest,
            opts: Dict = None,
    ) -> models.DescribeAppResponse:
        """
        根据应用id查询物联卡应用详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCard(
            self,
            request: models.DescribeCardRequest,
            opts: Dict = None,
    ) -> models.DescribeCardResponse:
        """
        查询卡片详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCards(
            self,
            request: models.DescribeCardsRequest,
            opts: Dict = None,
    ) -> models.DescribeCardsResponse:
        """
        查询卡片列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCardsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSms(
            self,
            request: models.DescribeSmsRequest,
            opts: Dict = None,
    ) -> models.DescribeSmsResponse:
        """
        查询短信列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserCardRemark(
            self,
            request: models.ModifyUserCardRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyUserCardRemarkResponse:
        """
        编辑卡片备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserCardRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserCardRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PayForExtendData(
            self,
            request: models.PayForExtendDataRequest,
            opts: Dict = None,
    ) -> models.PayForExtendDataResponse:
        """
        购买套外流量包
        """
        
        kwargs = {}
        kwargs["action"] = "PayForExtendData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PayForExtendDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewCards(
            self,
            request: models.RenewCardsRequest,
            opts: Dict = None,
    ) -> models.RenewCardsResponse:
        """
        批量为卡片续费，此接口建议调用至少间隔10s,如果出现返回deal lock failed相关的错误，请过10s再重试。
        续费的必要条件：
        1、单次续费的卡片不可以超过 100张。
        2、接口只支持在控制台购买的卡片进行续费
        3、销户和未激活的卡片不支持续费。
        4、每张物联网卡，续费总周期不能超过24个月
        """
        
        kwargs = {}
        kwargs["action"] = "RenewCards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewCardsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendMultiSms(
            self,
            request: models.SendMultiSmsRequest,
            opts: Dict = None,
    ) -> models.SendMultiSmsResponse:
        """
        群发短信
        """
        
        kwargs = {}
        kwargs["action"] = "SendMultiSms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendMultiSmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendSms(
            self,
            request: models.SendSmsRequest,
            opts: Dict = None,
    ) -> models.SendSmsResponse:
        """
        发送短信息接口
        """
        
        kwargs = {}
        kwargs["action"] = "SendSms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendSmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)