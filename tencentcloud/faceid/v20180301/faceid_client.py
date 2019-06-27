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
from tencentcloud.faceid.v20180301 import models


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.tencentcloudapi.com'


    def BankCard2EVerification(self, request):
        """银行卡二要素核验

        :param request: 调用BankCard2EVerification所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCard2EVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCard2EVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCard2EVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCard2EVerificationResponse()
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


    def BankCard4EVerification(self, request):
        """银行卡四要素核验

        :param request: 调用BankCard4EVerification所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCard4EVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCard4EVerificationResponse()
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


    def BankCardVerification(self, request):
        """银行卡核验

        :param request: 调用BankCardVerification所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCardVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCardVerificationResponse()
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


    def DetectAuth(self, request):
        """每次调用人脸核身SaaS化服务前，需先调用本接口获取BizToken，用来串联核身流程，在验证完成后，用于获取验证结果信息。

        :param request: 调用DetectAuth所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.DetectAuthRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DetectAuthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectAuth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectAuthResponse()
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


    def GetActionSequence(self, request):
        """使用动作活体检测模式前，需调用本接口获取动作顺序。

        :param request: 调用GetActionSequence所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetActionSequenceRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetActionSequenceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetActionSequence", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetActionSequenceResponse()
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


    def GetDetectInfo(self, request):
        """完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: 调用GetDetectInfo所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDetectInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDetectInfoResponse()
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


    def GetLiveCode(self, request):
        """使用数字活体检测模式前，需调用本接口获取数字验证码。

        :param request: 调用GetLiveCode所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetLiveCodeRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetLiveCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLiveCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLiveCodeResponse()
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


    def IdCardVerification(self, request):
        """传入姓名和身份证号，校验两者的真实性和一致性。

        :param request: 调用IdCardVerification所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IdCardVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IdCardVerificationResponse()
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


    def ImageRecognition(self, request):
        """传入照片和身份信息，判断该照片与公安权威库的证件照是否属于同一个人。

        :param request: 调用ImageRecognition所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageRecognition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageRecognitionResponse()
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


    def Liveness(self, request):
        """活体检测

        :param request: 调用Liveness所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Liveness", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LivenessResponse()
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


    def LivenessCompare(self, request):
        """传入视频和照片，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与上传照片是否属于同一个人。

        :param request: 调用LivenessCompare所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LivenessCompare", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LivenessCompareResponse()
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


    def LivenessRecognition(self, request):
        """传入视频和身份信息，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与公安权威库的证件照是否属于同一个人。

        :param request: 调用LivenessRecognition所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessRecognitionRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessRecognitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LivenessRecognition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LivenessRecognitionResponse()
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