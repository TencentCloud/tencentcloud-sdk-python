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
from tencentcloud.captcha.v20190722 import models
from typing import Dict


class CaptchaClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'captcha.tencentcloudapi.com'
    _service = 'captcha'

    async def DescribeCaptchaAppIdInfo(
            self,
            request: models.DescribeCaptchaAppIdInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaAppIdInfoResponse:
        """
        查询安全验证码应用APPId信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaAppIdInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaAppIdInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaData(
            self,
            request: models.DescribeCaptchaDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaDataResponse:
        """
        安全验证码分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3  分钟级查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaDataSum(
            self,
            request: models.DescribeCaptchaDataSumRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaDataSumResponse:
        """
        安全验证码查询请求数据概况，例如：按照时间段查询数据  昨日请求量、昨日恶意比例、昨日验证量、昨日通过量、昨日恶意拦截量……
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaDataSum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaDataSumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaMiniData(
            self,
            request: models.DescribeCaptchaMiniDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaMiniDataResponse:
        """
        安全验证码小程序插件分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3 小时级查询（五小时左右延迟）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaMiniData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaMiniDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaMiniDataSum(
            self,
            request: models.DescribeCaptchaMiniDataSumRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaMiniDataSumResponse:
        """
        安全验证码小程序插件查询请求数据概况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaMiniDataSum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaMiniDataSumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaMiniOperData(
            self,
            request: models.DescribeCaptchaMiniOperDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaMiniOperDataResponse:
        """
        安全验证码小程序插件用户操作数据查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaMiniOperData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaMiniOperDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaMiniResult(
            self,
            request: models.DescribeCaptchaMiniResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaMiniResultResponse:
        """
        核查验证码票据结果(小程序插件)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaMiniResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaMiniResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaMiniRiskResult(
            self,
            request: models.DescribeCaptchaMiniRiskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaMiniRiskResultResponse:
        """
        核查验证码小程序插件票据接入风控结果(已停用)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaMiniRiskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaMiniRiskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaOperData(
            self,
            request: models.DescribeCaptchaOperDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaOperDataResponse:
        """
        安全验证码用户操作数据查询，验证码加载耗时type = 1 、拦截情况type = 2、 一周通过平均尝试次数 type = 3、尝试次数分布 type = 4
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaOperData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaOperDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaRceResult(
            self,
            request: models.DescribeCaptchaRceResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaRceResultResponse:
        """
        Rce融合验证核查验证码票据结果(Web及APP)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaRceResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaRceResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaResult(
            self,
            request: models.DescribeCaptchaResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaResultResponse:
        """
        核查验证码票据结果(Web及APP)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaTicketData(
            self,
            request: models.DescribeCaptchaTicketDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaTicketDataResponse:
        """
        安全验证码用户操作票据数据查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaTicketData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaTicketDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaUserAllAppId(
            self,
            request: models.DescribeCaptchaUserAllAppIdRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaUserAllAppIdResponse:
        """
        安全验证码获取用户注册所有APPId和应用名称
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaUserAllAppId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaUserAllAppIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRequestStatistics(
            self,
            request: models.GetRequestStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetRequestStatisticsResponse:
        """
        查询单个CaptchaAppID验证的统计数据，包括：请求量、验证量、验证通过量、验证拦截量。
        """
        
        kwargs = {}
        kwargs["action"] = "GetRequestStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRequestStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTicketStatistics(
            self,
            request: models.GetTicketStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetTicketStatisticsResponse:
        """
        查询单个CaptchaAppID票据校验数据，包括：票据校验量、票据校验通过量、票据校验拦截量。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTicketStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTicketStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTotalRequestStatistics(
            self,
            request: models.GetTotalRequestStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetTotalRequestStatisticsResponse:
        """
        查询全部验证的统计数据，包括：总请求量、总验证量、总验证通过量、总验证拦截量等数据。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTotalRequestStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTotalRequestStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTotalTicketStatistics(
            self,
            request: models.GetTotalTicketStatisticsRequest,
            opts: Dict = None,
    ) -> models.GetTotalTicketStatisticsResponse:
        """
        查询全部票据校验的统计数据，包括：总票据校验量、总票据校验通过量、总票据校验拦截量。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTotalTicketStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTotalTicketStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCaptchaAppIdInfo(
            self,
            request: models.UpdateCaptchaAppIdInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateCaptchaAppIdInfoResponse:
        """
        更新验证码应用APPId信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCaptchaAppIdInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCaptchaAppIdInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)