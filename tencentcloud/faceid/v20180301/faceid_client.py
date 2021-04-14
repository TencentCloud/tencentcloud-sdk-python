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
    _service = 'faceid'


    def BankCard2EVerification(self, request):
        """本接口用于校验姓名和银行卡号的真实性和一致性。

        :param request: Request instance for BankCard2EVerification.
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
        """本接口用于输入银行卡号、姓名、开户证件号、开户手机号，校验信息的真实性和一致性。

        :param request: Request instance for BankCard4EVerification.
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
        """本接口用于银行卡号、姓名、开户证件号信息的真实性和一致性。

        :param request: Request instance for BankCardVerification.
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


    def CheckBankCardInformation(self, request):
        """银行卡基础信息查询

        :param request: Request instance for CheckBankCardInformation.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckBankCardInformationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckBankCardInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckBankCardInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckBankCardInformationResponse()
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


    def CheckIdCardInformation(self, request):
        """传入身份证人像面照片，识别身份证照片上的信息，并将姓名、身份证号、身份证人像照片与公安权威库的证件照进行比对，是否属于同一个人，从而验证身份证信息的真实性。

        :param request: Request instance for CheckIdCardInformation.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckIdCardInformationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckIdCardInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckIdCardInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckIdCardInformationResponse()
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


    def CheckPhoneAndName(self, request):
        """手机号二要素核验接口用于校验手机号和姓名的真实性和一致性，支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。

        :param request: Request instance for CheckPhoneAndName.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckPhoneAndNameRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckPhoneAndNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckPhoneAndName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckPhoneAndNameResponse()
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

        :param request: Request instance for DetectAuth.
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

        :param request: Request instance for GetActionSequence.
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

        :param request: Request instance for GetDetectInfo.
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


    def GetDetectInfoEnhanced(self, request):
        """完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetDetectInfoEnhanced.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoEnhancedRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoEnhancedResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDetectInfoEnhanced", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDetectInfoEnhancedResponse()
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


    def GetEidResult(self, request):
        """完成验证后，用EidToken调用本接口获取结果信息，EidToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetEidResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetEidResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetEidResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetEidResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetEidResultResponse()
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


    def GetEidToken(self, request):
        """每次调用E证通小程序服务前，需先调用本接口获取EidToken，用来串联核身流程，在验证完成后，用于获取验证结果信息。

        :param request: Request instance for GetEidToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetEidTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetEidTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetEidToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetEidTokenResponse()
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


    def GetFaceIdResult(self, request):
        """完成验证后，用FaceIdToken调用本接口获取结果信息，FaceIdToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetFaceIdResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFaceIdResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFaceIdResultResponse()
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


    def GetFaceIdToken(self, request):
        """每次调用人脸核身SDK服务前，需先调用本接口获取SDKToken，用来串联核身流程，在验证完成后，用于获取验证结果信息，该token仅能核身一次。

        :param request: Request instance for GetFaceIdToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFaceIdToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFaceIdTokenResponse()
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

        :param request: Request instance for GetLiveCode.
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


    def GetRealNameAuthResult(self, request):
        """获取微信实名认证结果

        :param request: Request instance for GetRealNameAuthResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetRealNameAuthResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetRealNameAuthResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRealNameAuthResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRealNameAuthResultResponse()
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


    def GetRealNameAuthToken(self, request):
        """该接口仅限微信公众号中使用，传入姓名和身份证号获取回调URL，在微信公众号中打开验证姓名和身份证号与微信实名的信息是否一致。

        :param request: Request instance for GetRealNameAuthToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetRealNameAuthTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetRealNameAuthTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRealNameAuthToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRealNameAuthTokenResponse()
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


    def IdCardOCRVerification(self, request):
        """本接口用于校验姓名和身份证号的真实性和一致性，您可以通过输入姓名和身份证号或传入身份证人像面照片提供所需验证信息。

        :param request: Request instance for IdCardOCRVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IdCardOCRVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IdCardOCRVerificationResponse()
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

        :param request: Request instance for IdCardVerification.
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

        :param request: Request instance for ImageRecognition.
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

        :param request: Request instance for Liveness.
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

        :param request: Request instance for LivenessCompare.
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

        :param request: Request instance for LivenessRecognition.
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


    def MinorsVerification(self, request):
        """未成年人守护接口是通过传入手机号或姓名和身份证号，结合权威数据源和腾讯健康守护可信模型，判断该信息是否真实且年满18周岁。腾讯健康守护可信模型覆盖了上十亿手机库源，覆盖率高、准确率高，如果不在库中的手机号，还可以通过姓名+身份证进行兜底验证。

        :param request: Request instance for MinorsVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MinorsVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MinorsVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MinorsVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MinorsVerificationResponse()
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


    def MobileNetworkTimeVerification(self, request):
        """本接口用于查询手机号在网时长，输入手机号进行查询。

        :param request: Request instance for MobileNetworkTimeVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MobileNetworkTimeVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MobileNetworkTimeVerificationResponse()
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


    def MobileStatus(self, request):
        """本接口用于验证手机号的状态，您可以输入手机号进行查询。

        :param request: Request instance for MobileStatus.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileStatusRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MobileStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MobileStatusResponse()
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


    def PhoneVerification(self, request):
        """本接口用于校验手机号、姓名和身份证号的真实性和一致性。支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。

        :param request: Request instance for PhoneVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PhoneVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PhoneVerificationResponse()
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