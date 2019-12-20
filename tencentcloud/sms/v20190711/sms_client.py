# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.sms.v20190711 import models


class SmsClient(AbstractClient):
    _apiVersion = '2019-07-11'
    _endpoint = 'sms.tencentcloudapi.com'


    def CallbackStatusStatistics(self, request):
        """统计用户回执的数据。

        :param request: Request instance for CallbackStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CallbackStatusStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallbackStatusStatisticsResponse()
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


    def PullSmsReplyStatus(self, request):
        """拉取短信回复状态。

        :param request: Request instance for PullSmsReplyStatus.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsReplyStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsReplyStatusResponse()
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


    def PullSmsReplyStatusByPhoneNumber(self, request):
        """拉取单个号码短信回复状态。

        :param request: Request instance for PullSmsReplyStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsReplyStatusByPhoneNumber", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsReplyStatusByPhoneNumberResponse()
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


    def PullSmsSendStatus(self, request):
        """拉取短信下发状态。

        :param request: Request instance for PullSmsSendStatus.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsSendStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsSendStatusResponse()
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


    def PullSmsSendStatusByPhoneNumber(self, request):
        """拉取单个号码短信下发状态。

        :param request: Request instance for PullSmsSendStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullSmsSendStatusByPhoneNumber", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullSmsSendStatusByPhoneNumberResponse()
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


    def SendSms(self, request):
        """短信发送接口，用户给用户发短信验证码、通知类短信或营销短信。


        :param request: Request instance for SendSms.
        :type request: :class:`tencentcloud.sms.v20190711.models.SendSmsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SendSmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendSms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendSmsResponse()
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


    def SendStatusStatistics(self, request):
        """统计用户发送短信的数据。

        :param request: Request instance for SendStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.SendStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SendStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendStatusStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendStatusStatisticsResponse()
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


    def SmsPackagesStatistics(self, request):
        """用户套餐包信息统计。

        :param request: Request instance for SmsPackagesStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.SmsPackagesStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SmsPackagesStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SmsPackagesStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SmsPackagesStatisticsResponse()
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