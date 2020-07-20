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
from tencentcloud.taf.v20200210 import models


class TafClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'taf.tencentcloudapi.com'


    def DetectFraudKOL(self, request):
        """DetectFraudKOL

        :param request: Request instance for DetectFraudKOL.
        :type request: :class:`tencentcloud.taf.v20200210.models.DetectFraudKOLRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.DetectFraudKOLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectFraudKOL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectFraudKOLResponse()
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


    def EnhanceTaDegree(self, request):
        """流量反欺诈-虚假TA识别

        :param request: Request instance for EnhanceTaDegree.
        :type request: :class:`tencentcloud.taf.v20200210.models.EnhanceTaDegreeRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.EnhanceTaDegreeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnhanceTaDegree", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnhanceTaDegreeResponse()
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


    def RecognizeCustomizedAudience(self, request):
        """流量反欺诈-流量验准定制版

        :param request: Request instance for RecognizeCustomizedAudience.
        :type request: :class:`tencentcloud.taf.v20200210.models.RecognizeCustomizedAudienceRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.RecognizeCustomizedAudienceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecognizeCustomizedAudience", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizeCustomizedAudienceResponse()
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


    def RecognizePreciseTargetAudience(self, request):
        """流量反欺诈-流量验准高级版

        :param request: Request instance for RecognizePreciseTargetAudience.
        :type request: :class:`tencentcloud.taf.v20200210.models.RecognizePreciseTargetAudienceRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.RecognizePreciseTargetAudienceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecognizePreciseTargetAudience", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizePreciseTargetAudienceResponse()
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


    def RecognizeTargetAudience(self, request):
        """流量反欺诈-流量验准

        :param request: Request instance for RecognizeTargetAudience.
        :type request: :class:`tencentcloud.taf.v20200210.models.RecognizeTargetAudienceRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.RecognizeTargetAudienceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecognizeTargetAudience", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizeTargetAudienceResponse()
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


    def SendTrafficSecuritySmsMessage(self, request):
        """SendTrafficSecuritySmsMessage

        :param request: Request instance for SendTrafficSecuritySmsMessage.
        :type request: :class:`tencentcloud.taf.v20200210.models.SendTrafficSecuritySmsMessageRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.SendTrafficSecuritySmsMessageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendTrafficSecuritySmsMessage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendTrafficSecuritySmsMessageResponse()
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