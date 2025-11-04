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
from tencentcloud.sms.v20210111 import models


class SmsClient(AbstractClient):
    _apiVersion = '2021-01-11'
    _endpoint = 'sms.tencentcloudapi.com'
    _service = 'sms'


    def AddSmsSign(self, request):
        r"""本接口 (AddSmsSign) 用于添加短信签名。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>添加短信签名前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39022">腾讯云短信签名审核标准。</a></li><li>个人认证用户不支持使用 API 申请短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 申请短信签名。</li></ul></blockquote>

        :param request: Request instance for AddSmsSign.
        :type request: :class:`tencentcloud.sms.v20210111.models.AddSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.AddSmsSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSmsSign", params, headers=headers)
            response = json.loads(body)
            model = models.AddSmsSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddSmsTemplate(self, request):
        r"""本接口 (AddSmsTemplate) 用于创建短信模板。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>申请短信模板前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39023">腾讯云短信正文模板审核标准。</a></li><li>个人认证用户不支持使用 API 申请短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 申请短信正文模板。</li></ul></blockquote>

        :param request: Request instance for AddSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20210111.models.AddSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.AddSmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.AddSmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CallbackStatusStatistics(self, request):
        r"""本接口 (CallbackStatusStatistics) 用于统计用户回执的数据。

        :param request: Request instance for CallbackStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20210111.models.CallbackStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.CallbackStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallbackStatusStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.CallbackStatusStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSmsSign(self, request):
        r"""本接口 (DeleteSmsSign) 用于删除短信签名。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 删除短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 删除短信签名。</li></ul></blockquote>

        :param request: Request instance for DeleteSmsSign.
        :type request: :class:`tencentcloud.sms.v20210111.models.DeleteSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DeleteSmsSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSmsSign", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSmsSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSmsTemplate(self, request):
        r"""本接口 (DeleteSmsTemplate) 用于删除短信模板。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 删除短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 删除短信正文模板。</li></ul></blockquote>

        :param request: Request instance for DeleteSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20210111.models.DeleteSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DeleteSmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePhoneNumberInfo(self, request):
        r"""本接口 (DescribePhoneNumberInfo) 用于提供电话号码的信息查询，包括国家（或地区）码、规范的 E.164 格式号码等。
        - 例如：查询号码 +86018501234444，可以得到国家码 86、规范的 E.164 号码 +8618501234444 等信息。

        :param request: Request instance for DescribePhoneNumberInfo.
        :type request: :class:`tencentcloud.sms.v20210111.models.DescribePhoneNumberInfoRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DescribePhoneNumberInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePhoneNumberInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePhoneNumberInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmsSignList(self, request):
        r"""本接口 (DescribeSmsSignList) 用于查询短信签名状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 查询短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 查询短信签名。</li></ul></blockquote>

        :param request: Request instance for DescribeSmsSignList.
        :type request: :class:`tencentcloud.sms.v20210111.models.DescribeSmsSignListRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DescribeSmsSignListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsSignList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsSignListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmsTemplateList(self, request):
        r"""本接口 (DescribeSmsTemplateList) 用于查询短信模板状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>个人认证用户不支持使用 API 查询短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 查询短信正文模板。</li></ul></blockquote>

        :param request: Request instance for DescribeSmsTemplateList.
        :type request: :class:`tencentcloud.sms.v20210111.models.DescribeSmsTemplateListRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DescribeSmsTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySmsSign(self, request):
        r"""本接口 (ModifySmsSign) 用于修改短信签名。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>修改短信签名前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39022">腾讯云短信签名审核标准。</a></li><li>个人认证用户不支持使用 API 修改短信签名，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 修改短信签名。</li><li>修改短信签名，仅当签名为<b>待审核</b>或<b>已拒绝</b>状态时，才能进行修改，<b>已审核通过</b>的签名不支持修改。</li></ul></blockquote>

        :param request: Request instance for ModifySmsSign.
        :type request: :class:`tencentcloud.sms.v20210111.models.ModifySmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.ModifySmsSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySmsSign", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySmsSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySmsTemplate(self, request):
        r"""本接口 (ModifySmsTemplate) 用于修改短信模板。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>修改短信正文模板前，请先认真参阅 <a href="https://cloud.tencent.com/document/product/382/39023">腾讯云短信正文模板审核标准。</a></li><li>个人认证用户不支持使用 API 修改短信正文模板，请参阅了解 <a href="https://cloud.tencent.com/document/product/378/3629">实名认证基本介绍</a>，如果为个人认证请登录 <a href="https://console.cloud.tencent.com/smsv2">控制台</a> 修改短信正文模板。</li><li>修改短信模板，仅当正文模板为<b>待审核</b>或<b>已拒绝</b>状态时，才能进行修改，<b>已审核通过</b>的正文模板不支持修改。</li></ul></blockquote>

        :param request: Request instance for ModifySmsTemplate.
        :type request: :class:`tencentcloud.sms.v20210111.models.ModifySmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.ModifySmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullSmsReplyStatus(self, request):
        r"""本接口 (PullSmsReplyStatus) 用于拉取短信回复状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>此接口需要联系  <a href="https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81">腾讯云短信小助手</a> 开通。接口拉取的状态数据为队列模式，同一号码一次下发的状态数据仅能拉取一次。</li><li>上行回复也支持 <a href="https://cloud.tencent.com/document/product/382/42907">配置回复回调</a> 的方式获取。</li></ul></blockquote>

        :param request: Request instance for PullSmsReplyStatus.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsReplyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsReplyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullSmsReplyStatusByPhoneNumber(self, request):
        r"""本接口 (PullSmsReplyStatusByPhoneNumber) 用于拉取单个号码短信回复状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>上行回复也支持 <a href="https://cloud.tencent.com/document/product/382/42907">配置回复回调</a> 的方式获取。</li></ul></blockquote>

        :param request: Request instance for PullSmsReplyStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsReplyStatusByPhoneNumber", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsReplyStatusByPhoneNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullSmsSendStatus(self, request):
        r"""本接口 (PullSmsSendStatus) 用于拉取短信下发状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>此接口需要联系  <a href="https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81">腾讯云短信小助手</a> 开通。接口拉取的状态数据为队列模式，同一号码一次下发的状态数据仅能拉取一次。</li><li>下发状态也支持 <a href="https://cloud.tencent.com/document/product/382/37809#sendingstatus">配置回调</a> 的方式获取。</li></ul></blockquote>

        :param request: Request instance for PullSmsSendStatus.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsSendStatus", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsSendStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PullSmsSendStatusByPhoneNumber(self, request):
        r"""本接口 (PullSmsSendStatusByPhoneNumber) 用于拉取单个号码短信下发状态。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>下发状态也支持 <a href="https://cloud.tencent.com/document/product/382/37809#sendingstatus">配置回调</a> 的方式获取。</li></ul></blockquote>

        :param request: Request instance for PullSmsSendStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsSendStatusByPhoneNumber", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsSendStatusByPhoneNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportConversion(self, request):
        r"""本接口 (ReportConversion) 用于短信转化率上报。将已接收到短信的流水号上报到腾讯云短信服务。
        <blockquote class="d-mod-explain"><div class="d-mod-title d-explain-title" style="line-height: normal;"><i class="d-icon-explain"></i>说明：</div><p></p><ul><li>该接口当前以白名单方式对外开放，如有需要请联系  <a href="https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81">腾讯云短信小助手</a> 开通。</li></ul></blockquote>

        :param request: Request instance for ReportConversion.
        :type request: :class:`tencentcloud.sms.v20210111.models.ReportConversionRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.ReportConversionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportConversion", params, headers=headers)
            response = json.loads(body)
            model = models.ReportConversionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendSms(self, request):
        r"""本接口 (SendSms) 用于发送验证码、通知类短信和营销短信。支持国内短信与国际/港澳台短信。
        - 当前接口属于 2021-01-11 版本，如果您仍在使用 [2019-07-11 版本](https://cloud.tencent.com/document/product/382/38778)，建议您使用当前最新版本的接口，版本差异可参考[版本描述](https://cloud.tencent.com/document/product/382/63195#.E7.89.88.E6.9C.AC.E6.8F.8F.E8.BF.B0)。

        :param request: Request instance for SendSms.
        :type request: :class:`tencentcloud.sms.v20210111.models.SendSmsRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.SendSmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendSms", params, headers=headers)
            response = json.loads(body)
            model = models.SendSmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendStatusStatistics(self, request):
        r"""本接口 (SendStatusStatistics) 用于统计用户发送短信的数据。

        :param request: Request instance for SendStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20210111.models.SendStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.SendStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendStatusStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.SendStatusStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SmsPackagesStatistics(self, request):
        r"""本接口 (SmsPackagesStatistics) 用于统计用户套餐包数据。

        :param request: Request instance for SmsPackagesStatistics.
        :type request: :class:`tencentcloud.sms.v20210111.models.SmsPackagesStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.SmsPackagesStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SmsPackagesStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.SmsPackagesStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))