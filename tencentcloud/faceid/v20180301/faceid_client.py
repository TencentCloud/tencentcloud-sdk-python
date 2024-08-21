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
            headers = request.headers
            body = self.call("BankCard2EVerification", params, headers=headers)
            response = json.loads(body)
            model = models.BankCard2EVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BankCard4EVerification(self, request):
        """本接口用于输入银行卡号、姓名、开户证件号、开户手机号，校验信息的真实性和一致性。

        :param request: Request instance for BankCard4EVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BankCard4EVerification", params, headers=headers)
            response = json.loads(body)
            model = models.BankCard4EVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BankCardVerification(self, request):
        """本接口用于银行卡号、姓名、开户证件号信息的真实性和一致性。

        :param request: Request instance for BankCardVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BankCardVerification", params, headers=headers)
            response = json.loads(body)
            model = models.BankCardVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBankCardInformation(self, request):
        """银行卡基础信息查询

        :param request: Request instance for CheckBankCardInformation.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckBankCardInformationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckBankCardInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBankCardInformation", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBankCardInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckEidTokenStatus(self, request):
        """用于轮询E证通H5场景EidToken验证状态。

        :param request: Request instance for CheckEidTokenStatus.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckEidTokenStatusRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckEidTokenStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckEidTokenStatus", params, headers=headers)
            response = json.loads(body)
            model = models.CheckEidTokenStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIdCardInformation(self, request):
        """传入身份证人像面照片，识别身份证照片上的信息，并将姓名、身份证号、身份证人像照片与权威库的证件照进行比对，是否属于同一个人，从而验证身份证信息的真实性。

        :param request: Request instance for CheckIdCardInformation.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckIdCardInformationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckIdCardInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIdCardInformation", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIdCardInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIdNameDate(self, request):
        """本接口用于校验姓名、身份证号、身份证有效期的真实性和一致性。

        :param request: Request instance for CheckIdNameDate.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckIdNameDateRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckIdNameDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIdNameDate", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIdNameDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckPhoneAndName(self, request):
        """手机号二要素核验接口用于校验手机号和姓名的真实性和一致性，支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。

        :param request: Request instance for CheckPhoneAndName.
        :type request: :class:`tencentcloud.faceid.v20180301.models.CheckPhoneAndNameRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.CheckPhoneAndNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckPhoneAndName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckPhoneAndNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectAIFakeFaces(self, request):
        """基于多模态的AI大模型算法，提供对人脸图片、视频的防攻击检测能力，可针对性有效识别高仿真的AIGC换脸、高清翻拍、批量黑产攻击、水印等攻击痕迹，增强对图片和视频的防伪安全能力。

        :param request: Request instance for DetectAIFakeFaces.
        :type request: :class:`tencentcloud.faceid.v20180301.models.DetectAIFakeFacesRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DetectAIFakeFacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectAIFakeFaces", params, headers=headers)
            response = json.loads(body)
            model = models.DetectAIFakeFacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectAuth(self, request):
        """每次调用人脸核身SaaS化服务前，需先调用本接口获取BizToken，用来串联核身流程，在验证完成后，用于获取验证结果信息。

        :param request: Request instance for DetectAuth.
        :type request: :class:`tencentcloud.faceid.v20180301.models.DetectAuthRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DetectAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectAuth", params, headers=headers)
            response = json.loads(body)
            model = models.DetectAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EncryptedPhoneVerification(self, request):
        """本接口用于校验手机号、姓名和身份证号的真实性和一致性，入参支持明文、MD5和SHA256加密传输。

        :param request: Request instance for EncryptedPhoneVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.EncryptedPhoneVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.EncryptedPhoneVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EncryptedPhoneVerification", params, headers=headers)
            response = json.loads(body)
            model = models.EncryptedPhoneVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetActionSequence(self, request):
        """使用动作活体检测模式前，需调用本接口获取动作顺序。

        :param request: Request instance for GetActionSequence.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetActionSequenceRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetActionSequenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetActionSequence", params, headers=headers)
            response = json.loads(body)
            model = models.GetActionSequenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDetectInfo(self, request):
        """完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetDetectInfo.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDetectInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetDetectInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDetectInfoEnhanced(self, request):
        """完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetDetectInfoEnhanced.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoEnhancedRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoEnhancedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDetectInfoEnhanced", params, headers=headers)
            response = json.loads(body)
            model = models.GetDetectInfoEnhancedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEidResult(self, request):
        """完成验证后，用EidToken调用本接口获取结果信息，EidToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetEidResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetEidResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetEidResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEidResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetEidResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEidToken(self, request):
        """每次调用E证通服务前，需先调用本接口获取EidToken，用来串联E证通流程，在验证完成后，用于获取E证通结果信息。

        :param request: Request instance for GetEidToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetEidTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetEidTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEidToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetEidTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFaceIdResult(self, request):
        """完成验证后，用FaceIdToken调用本接口获取结果信息，FaceIdToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetFaceIdResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFaceIdResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetFaceIdResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFaceIdRiskInfo(self, request):
        """完成验证后，用FaceIdToken调用本接口获取设备风险相关信息，FaceIdToken生成后三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetFaceIdRiskInfo.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdRiskInfoRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdRiskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFaceIdRiskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetFaceIdRiskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFaceIdToken(self, request):
        """每次调用人脸核身SDK服务前，需先调用本接口获取SDKToken，用来串联核身流程，在验证完成后，用于获取验证结果信息，该token仅能核身一次。

        :param request: Request instance for GetFaceIdToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceIdTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFaceIdToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetFaceIdTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFaceidRiskInfoToken(self, request):
        """每次调用人脸核身SDK服务前，需先调用本接口获取SDKToken，用来串联核身流程，在验证完成后，用于获取风险结果信息，该Token仅能核身一次。

        :param request: Request instance for GetFaceidRiskInfoToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetFaceidRiskInfoTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetFaceidRiskInfoTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFaceidRiskInfoToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetFaceidRiskInfoTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLiveCode(self, request):
        """使用数字活体检测模式前，需调用本接口获取数字验证码。

        :param request: Request instance for GetLiveCode.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetLiveCodeRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetLiveCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLiveCode", params, headers=headers)
            response = json.loads(body)
            model = models.GetLiveCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWeChatBillDetails(self, request):
        """查询微信渠道服务（微信小程序、微信原生H5、微信普通H5）的账单明细及计费状态。

        :param request: Request instance for GetWeChatBillDetails.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetWeChatBillDetailsRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetWeChatBillDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWeChatBillDetails", params, headers=headers)
            response = json.loads(body)
            model = models.GetWeChatBillDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IdCardOCRVerification(self, request):
        """本接口用于校验姓名和身份证号的真实性和一致性，您可以通过输入姓名和身份证号或传入身份证人像面照片提供所需验证信息。

        :param request: Request instance for IdCardOCRVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdCardOCRVerification", params, headers=headers)
            response = json.loads(body)
            model = models.IdCardOCRVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IdCardVerification(self, request):
        """传入姓名和身份证号，校验两者的真实性和一致性。

        :param request: Request instance for IdCardVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdCardVerification", params, headers=headers)
            response = json.loads(body)
            model = models.IdCardVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageRecognition(self, request):
        """传入照片和身份信息，判断该照片与权威库的证件照是否属于同一个人（该接口已停止接入，新客户请使用<a href="https://cloud.tencent.com/document/product/1007/102203">照片人脸核身（V2.0）</a>接口）。

        :param request: Request instance for ImageRecognition.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageRecognition", params, headers=headers)
            response = json.loads(body)
            model = models.ImageRecognitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageRecognitionV2(self, request):
        """传入照片和身份信息，判断该照片与权威库的证件照是否属于同一个人。

        :param request: Request instance for ImageRecognitionV2.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionV2Request`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageRecognitionV2", params, headers=headers)
            response = json.loads(body)
            model = models.ImageRecognitionV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Liveness(self, request):
        """活体检测

        :param request: Request instance for Liveness.
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Liveness", params, headers=headers)
            response = json.loads(body)
            model = models.LivenessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LivenessCompare(self, request):
        """传入视频和照片，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与上传照片是否属于同一个人。

        :param request: Request instance for LivenessCompare.
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LivenessCompare", params, headers=headers)
            response = json.loads(body)
            model = models.LivenessCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LivenessRecognition(self, request):
        """传入视频和身份信息，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与权威库的证件照是否属于同一个人。

        :param request: Request instance for LivenessRecognition.
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessRecognitionRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessRecognitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LivenessRecognition", params, headers=headers)
            response = json.loads(body)
            model = models.LivenessRecognitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MinorsVerification(self, request):
        """通过传入手机号或姓名和身份证号，结合权威数据源和腾讯健康守护可信模型，判断该信息是否真实且年满18周岁。腾讯健康守护可信模型覆盖了上十亿手机库源，覆盖率高、准确率高，如果不在库中的手机号，还可以通过姓名+身份证进行兜底验证。

        :param request: Request instance for MinorsVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MinorsVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MinorsVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MinorsVerification", params, headers=headers)
            response = json.loads(body)
            model = models.MinorsVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MobileNetworkTimeVerification(self, request):
        """本接口用于查询手机号在网时长，输入手机号进行查询。

        :param request: Request instance for MobileNetworkTimeVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MobileNetworkTimeVerification", params, headers=headers)
            response = json.loads(body)
            model = models.MobileNetworkTimeVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MobileStatus(self, request):
        """本接口用于验证手机号的状态，您可以输入手机号进行查询。

        :param request: Request instance for MobileStatus.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileStatusRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MobileStatus", params, headers=headers)
            response = json.loads(body)
            model = models.MobileStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseNfcData(self, request):
        """解析SDK获取到的证件NFC数据，接口传入SDK返回的ReqId，返回证件信息（个别字段为特定证件类型特有）。SDK生成的ReqId五分钟内有效，重复查询仅收一次费。支持身份证类证件（二代身份证、港澳居住证、台湾居住证、外国人永居证）以及旅行类证件（港澳通行证、台湾通行证、台胞证、回乡证）的NFC识别及核验。

        :param request: Request instance for ParseNfcData.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ParseNfcDataRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ParseNfcDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseNfcData", params, headers=headers)
            response = json.loads(body)
            model = models.ParseNfcDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PhoneVerification(self, request):
        """本接口用于校验手机号、姓名和身份证号的真实性和一致性。支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。

        :param request: Request instance for PhoneVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PhoneVerification", params, headers=headers)
            response = json.loads(body)
            model = models.PhoneVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PhoneVerificationCMCC(self, request):
        """本接口用于校验中国移动手机号、姓名和身份证号的真实性和一致性。中国移动支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。

        :param request: Request instance for PhoneVerificationCMCC.
        :type request: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationCMCCRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationCMCCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PhoneVerificationCMCC", params, headers=headers)
            response = json.loads(body)
            model = models.PhoneVerificationCMCCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PhoneVerificationCTCC(self, request):
        """本接口用于校验中国电信手机号、姓名和身份证号的真实性和一致性。中国电信支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。

        :param request: Request instance for PhoneVerificationCTCC.
        :type request: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationCTCCRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationCTCCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PhoneVerificationCTCC", params, headers=headers)
            response = json.loads(body)
            model = models.PhoneVerificationCTCCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PhoneVerificationCUCC(self, request):
        """本接口用于校验中国联通手机号、姓名和身份证号的真实性和一致性。中国联通支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。

        :param request: Request instance for PhoneVerificationCUCC.
        :type request: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationCUCCRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationCUCCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PhoneVerificationCUCC", params, headers=headers)
            response = json.loads(body)
            model = models.PhoneVerificationCUCCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))