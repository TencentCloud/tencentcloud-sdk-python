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
            body = self.call("DescribeCaptchaAppIdInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaAppIdInfoResponse()
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


    def DescribeCaptchaData(self, request):
        """安全验证码分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3  分钟级查询

        :param request: Request instance for DescribeCaptchaData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaDataResponse()
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


    def DescribeCaptchaDataSum(self, request):
        """安全验证码查询请求数据概况，例如：按照时间段查询数据  昨日请求量、昨日恶意比例、昨日验证量、昨日通过量、昨日恶意拦截量……

        :param request: Request instance for DescribeCaptchaDataSum.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataSumRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataSumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaDataSum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaDataSumResponse()
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


    def DescribeCaptchaMiniData(self, request):
        """安全验证码小程序插件分类查询数据接口，请求量type=0、通过量type=1、验证量type=2、拦截量type=3 小时级查询（五小时左右延迟）

        :param request: Request instance for DescribeCaptchaMiniData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaMiniData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaMiniDataResponse()
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


    def DescribeCaptchaMiniDataSum(self, request):
        """安全验证码小程序插件查询请求数据概况

        :param request: Request instance for DescribeCaptchaMiniDataSum.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataSumRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniDataSumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaMiniDataSum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaMiniDataSumResponse()
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


    def DescribeCaptchaMiniOperData(self, request):
        """安全验证码小程序插件用户操作数据查询

        :param request: Request instance for DescribeCaptchaMiniOperData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniOperDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniOperDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaMiniOperData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaMiniOperDataResponse()
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


    def DescribeCaptchaMiniResult(self, request):
        """核查验证码小程序插件票据结果

        :param request: Request instance for DescribeCaptchaMiniResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaMiniResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaMiniResultResponse()
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


    def DescribeCaptchaMiniRiskResult(self, request):
        """核查验证码小程序插件票据接入风控结果(Beta)

        :param request: Request instance for DescribeCaptchaMiniRiskResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniRiskResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaMiniRiskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaMiniRiskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaMiniRiskResultResponse()
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


    def DescribeCaptchaOperData(self, request):
        """安全验证码用户操作数据查询，验证码加载耗时type = 1 、拦截情况type = 2、 一周通过平均尝试次数 type = 3、尝试次数分布 type = 4

        :param request: Request instance for DescribeCaptchaOperData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaOperDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaOperDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaOperData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaOperDataResponse()
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


    def DescribeCaptchaResult(self, request):
        """核查验证码票据结果

        :param request: Request instance for DescribeCaptchaResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaResultResponse()
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


    def DescribeCaptchaTicketData(self, request):
        """安全验证码用户操作票据数据查询

        :param request: Request instance for DescribeCaptchaTicketData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaTicketDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaTicketDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaTicketData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaTicketDataResponse()
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


    def DescribeCaptchaUserAllAppId(self, request):
        """安全验证码获取用户注册所有APPId和应用名称

        :param request: Request instance for DescribeCaptchaUserAllAppId.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaUserAllAppIdRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaUserAllAppIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaUserAllAppId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaUserAllAppIdResponse()
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


    def UpdateCaptchaAppIdInfo(self, request):
        """更新验证码应用APPId信息

        :param request: Request instance for UpdateCaptchaAppIdInfo.
        :type request: :class:`tencentcloud.captcha.v20190722.models.UpdateCaptchaAppIdInfoRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.UpdateCaptchaAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCaptchaAppIdInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCaptchaAppIdInfoResponse()
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