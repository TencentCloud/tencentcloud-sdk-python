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
from tencentcloud.sms.v20190711 import models
from typing import Dict


class SmsClient(AbstractClient):
    _apiVersion = '2019-07-11'
    _endpoint = 'sms.tencentcloudapi.com'
    _service = 'sms'

    async def AddSmsSign(
            self,
            request: models.AddSmsSignRequest,
            opts: Dict = None,
    ) -> models.AddSmsSignResponse:
        """
        本接口 (AddSmsSign) 用于添加短信签名。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>添加短信签名前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39022">腾讯云短信签名审核标准。</a></li><li>个人认证用户不支持使用 API 申请短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 申请短信签名。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "AddSmsSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSmsSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddSmsTemplate(
            self,
            request: models.AddSmsTemplateRequest,
            opts: Dict = None,
    ) -> models.AddSmsTemplateResponse:
        """
        本接口 (AddSmsTemplate) 用于创建短信模板。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>申请短信模板前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39023">腾讯云短信正文模板审核标准。</a></li><li>个人认证用户不支持使用 API 申请短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 申请短信正文模板。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "AddSmsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSmsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CallbackStatusStatistics(
            self,
            request: models.CallbackStatusStatisticsRequest,
            opts: Dict = None,
    ) -> models.CallbackStatusStatisticsResponse:
        """
        本接口 (CallbackStatusStatistics) 用于统计用户回执的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "CallbackStatusStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallbackStatusStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmsSign(
            self,
            request: models.DeleteSmsSignRequest,
            opts: Dict = None,
    ) -> models.DeleteSmsSignResponse:
        """
        本接口 (DeleteSmsSign) 用于删除短信签名。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 删除短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 删除短信签名。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmsSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmsSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmsTemplate(
            self,
            request: models.DeleteSmsTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSmsTemplateResponse:
        """
        本接口 (DeleteSmsTemplate) 用于删除短信模板。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 删除短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 删除短信正文模板。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmsSignList(
            self,
            request: models.DescribeSmsSignListRequest,
            opts: Dict = None,
    ) -> models.DescribeSmsSignListResponse:
        """
        本接口 (DescribeSmsSignList) 用于查询短信签名状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 查询短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 查询短信签名。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmsSignList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmsSignListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmsTemplateList(
            self,
            request: models.DescribeSmsTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeSmsTemplateListResponse:
        """
        本接口 (DescribeSmsTemplateList) 用于查询短信模板状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 查询短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 查询短信正文模板。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmsTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmsTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmsSign(
            self,
            request: models.ModifySmsSignRequest,
            opts: Dict = None,
    ) -> models.ModifySmsSignResponse:
        """
        本接口 (ModifySmsSign) 用于修改短信签名。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>修改短信签名前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39022">腾讯云短信签名审核标准。</a></li><li>个人认证用户不支持使用 API 修改短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 修改短信签名。</li><li>修改短信签名，仅当签名为<b>待审核</b>或<b>已拒绝</b>状态时，才能进行修改，<b>已审核通过</b>的签名不支持修改。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmsSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmsSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmsTemplate(
            self,
            request: models.ModifySmsTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySmsTemplateResponse:
        """
        本接口 (ModifySmsTemplate) 用于修改短信模板。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>修改短信正文模板前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39023">腾讯云短信正文模板审核标准。</a></li><li>个人认证用户不支持使用 API 修改短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 修改短信正文模板。</li><li>修改短信模板，仅当正文模板为<b>待审核</b>或<b>已拒绝</b>状态时，才能进行修改，<b>已审核通过</b>的正文模板不支持修改。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsReplyStatus(
            self,
            request: models.PullSmsReplyStatusRequest,
            opts: Dict = None,
    ) -> models.PullSmsReplyStatusResponse:
        """
        本接口 (PullSmsReplyStatus) 用于拉取短信回复状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>此接口需要联系  <a href="https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81">腾讯云短信小助手</a> 开通。接口拉取的状态数据为队列模式，同一号码一次下发的状态数据仅能拉取一次。</li><li>上行回复也支持 <a href="https://cloud.tencent.com/document/product/382/42907">配置回复回调</a> 的方式获取。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsReplyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsReplyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsReplyStatusByPhoneNumber(
            self,
            request: models.PullSmsReplyStatusByPhoneNumberRequest,
            opts: Dict = None,
    ) -> models.PullSmsReplyStatusByPhoneNumberResponse:
        """
        本接口 (PullSmsReplyStatusByPhoneNumber) 用于拉取单个号码短信回复状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>上行回复也支持 <a href="https://cloud.tencent.com/document/product/382/42907">配置回复回调</a> 的方式获取。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsReplyStatusByPhoneNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsReplyStatusByPhoneNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsSendStatus(
            self,
            request: models.PullSmsSendStatusRequest,
            opts: Dict = None,
    ) -> models.PullSmsSendStatusResponse:
        """
        本接口 (PullSmsSendStatus) 用于拉取短信下发状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>此接口需要联系  <a href="https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81">腾讯云短信小助手</a> 开通。接口拉取的状态数据为队列模式，同一号码一次下发的状态数据仅能拉取一次。</li><li>下发状态也支持 <a href="https://cloud.tencent.com/document/product/382/37809#sendingstatus">配置回调</a> 的方式获取。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsSendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsSendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsSendStatusByPhoneNumber(
            self,
            request: models.PullSmsSendStatusByPhoneNumberRequest,
            opts: Dict = None,
    ) -> models.PullSmsSendStatusByPhoneNumberResponse:
        """
        本接口 (PullSmsSendStatusByPhoneNumber) 用于拉取单个号码短信下发状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>下发状态也支持 <a href="https://cloud.tencent.com/document/product/382/37809#sendingstatus">配置回调</a> 的方式获取。</li></ul></blockquote>
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsSendStatusByPhoneNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsSendStatusByPhoneNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendSms(
            self,
            request: models.SendSmsRequest,
            opts: Dict = None,
    ) -> models.SendSmsResponse:
        """
        本接口 (SendSms) 用于发送验证码、通知类短信和营销短信。支持国内短信与国际/港澳台短信。
        """
        
        kwargs = {}
        kwargs["action"] = "SendSms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendSmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendStatusStatistics(
            self,
            request: models.SendStatusStatisticsRequest,
            opts: Dict = None,
    ) -> models.SendStatusStatisticsResponse:
        """
        本接口 (SendStatusStatistics) 用于统计用户发送短信的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "SendStatusStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendStatusStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SmsPackagesStatistics(
            self,
            request: models.SmsPackagesStatisticsRequest,
            opts: Dict = None,
    ) -> models.SmsPackagesStatisticsResponse:
        """
        本接口 (SmsPackagesStatistics) 用于统计用户套餐包数据。
        """
        
        kwargs = {}
        kwargs["action"] = "SmsPackagesStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SmsPackagesStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)