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
from tencentcloud.captcha.v20190722 import models


class CaptchaClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'captcha.tencentcloudapi.com'
    _service = 'captcha'


    def DescribeCaptchaAppIdInfo(self, request):
        """查询安全验证码应用APPId信息

        :param request: Request instance for DescribeCaptchaAppIdInfo.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaAppIdInfoRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaAppIdInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaAppIdInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaData(self, request):
        """安全验证码分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3  分钟级查询

        :param request: Request instance for DescribeCaptchaData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaDataSum(self, request):
        """安全验证码查询请求数据概况，例如：按照时间段查询数据  昨日请求量、昨日恶意比例、昨日验证量、昨日通过量、昨日恶意拦截量……

        :param request: Request instance for DescribeCaptchaDataSum.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataSumRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataSumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaDataSum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaDataSumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaMiniData(self, request):
        """安全验证码小程序插件分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3 小时级查询（五小时左右延迟）

        :param request: Request instance for DescribeCaptchaMiniData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaMiniData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaMiniDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaMiniDataSum(self, request):
        """安全验证码小程序插件查询请求数据概况

        :param request: Request instance for DescribeCaptchaMiniDataSum.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataSumRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataSumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaMiniDataSum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaMiniDataSumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaMiniOperData(self, request):
        """安全验证码小程序插件用户操作数据查询

        :param request: Request instance for DescribeCaptchaMiniOperData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniOperDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniOperDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaMiniOperData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaMiniOperDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaMiniResult(self, request):
        """核查验证码票据结果(小程序插件)

        :param request: Request instance for DescribeCaptchaMiniResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaMiniResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaMiniResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaMiniRiskResult(self, request):
        """核查验证码小程序插件票据接入风控结果(已停用)

        :param request: Request instance for DescribeCaptchaMiniRiskResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniRiskResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniRiskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaMiniRiskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaMiniRiskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaOperData(self, request):
        """安全验证码用户操作数据查询，验证码加载耗时type = 1 、拦截情况type = 2、 一周通过平均尝试次数 type = 3、尝试次数分布 type = 4

        :param request: Request instance for DescribeCaptchaOperData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaOperDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaOperDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaOperData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaOperDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaResult(self, request):
        """核查验证码票据结果(Web及APP)

        :param request: Request instance for DescribeCaptchaResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaTicketData(self, request):
        """安全验证码用户操作票据数据查询

        :param request: Request instance for DescribeCaptchaTicketData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaTicketDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaTicketDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaTicketData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaTicketDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaUserAllAppId(self, request):
        """安全验证码获取用户注册所有APPId和应用名称

        :param request: Request instance for DescribeCaptchaUserAllAppId.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaUserAllAppIdRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaUserAllAppIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaUserAllAppId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaUserAllAppIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRequestStatistics(self, request):
        """查询单个CaptchaAppID验证的统计数据，包括：请求量、验证量、验证通过量、验证拦截量。

        :param request: Request instance for GetRequestStatistics.
        :type request: :class:`tencentcloud.captcha.v20190722.models.GetRequestStatisticsRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.GetRequestStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRequestStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetRequestStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTicketStatistics(self, request):
        """查询单个CaptchaAppID票据校验数据，包括：票据校验量、票据校验通过量、票据校验拦截量。

        :param request: Request instance for GetTicketStatistics.
        :type request: :class:`tencentcloud.captcha.v20190722.models.GetTicketStatisticsRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.GetTicketStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTicketStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetTicketStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTotalRequestStatistics(self, request):
        """查询全部验证的统计数据，包括：总请求量、总验证量、总验证通过量、总验证拦截量等数据。

        :param request: Request instance for GetTotalRequestStatistics.
        :type request: :class:`tencentcloud.captcha.v20190722.models.GetTotalRequestStatisticsRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.GetTotalRequestStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTotalRequestStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetTotalRequestStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTotalTicketStatistics(self, request):
        """查询全部票据校验的统计数据，包括：总票据校验量、总票据校验通过量、总票据校验拦截量。

        :param request: Request instance for GetTotalTicketStatistics.
        :type request: :class:`tencentcloud.captcha.v20190722.models.GetTotalTicketStatisticsRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.GetTotalTicketStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTotalTicketStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.GetTotalTicketStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCaptchaAppIdInfo(self, request):
        """更新验证码应用APPId信息

        :param request: Request instance for UpdateCaptchaAppIdInfo.
        :type request: :class:`tencentcloud.captcha.v20190722.models.UpdateCaptchaAppIdInfoRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.UpdateCaptchaAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCaptchaAppIdInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCaptchaAppIdInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))