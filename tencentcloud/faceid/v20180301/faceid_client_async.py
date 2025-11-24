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
from tencentcloud.faceid.v20180301 import models
from typing import Dict


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.tencentcloudapi.com'
    _service = 'faceid'

    async def BankCard2EVerification(
            self,
            request: models.BankCard2EVerificationRequest,
            opts: Dict = None,
    ) -> models.BankCard2EVerificationResponse:
        """
        本接口用于校验姓名和银行卡号的真实性和一致性。
        """
        
        kwargs = {}
        kwargs["action"] = "BankCard2EVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCard2EVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankCard4EVerification(
            self,
            request: models.BankCard4EVerificationRequest,
            opts: Dict = None,
    ) -> models.BankCard4EVerificationResponse:
        """
        本接口用于输入银行卡号、姓名、开户证件号、开户手机号，校验信息的真实性和一致性。
        """
        
        kwargs = {}
        kwargs["action"] = "BankCard4EVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCard4EVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankCardVerification(
            self,
            request: models.BankCardVerificationRequest,
            opts: Dict = None,
    ) -> models.BankCardVerificationResponse:
        """
        本接口用于银行卡号、姓名、开户证件号信息的真实性和一致性。
        """
        
        kwargs = {}
        kwargs["action"] = "BankCardVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCardVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBankCardInformation(
            self,
            request: models.CheckBankCardInformationRequest,
            opts: Dict = None,
    ) -> models.CheckBankCardInformationResponse:
        """
        银行卡基础信息查询
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBankCardInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBankCardInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckEidTokenStatus(
            self,
            request: models.CheckEidTokenStatusRequest,
            opts: Dict = None,
    ) -> models.CheckEidTokenStatusResponse:
        """
        用于轮询E证通H5场景EidToken验证状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckEidTokenStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckEidTokenStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIdCardInformation(
            self,
            request: models.CheckIdCardInformationRequest,
            opts: Dict = None,
    ) -> models.CheckIdCardInformationResponse:
        """
        传入身份证人像面照片，识别身份证照片上的信息，并将姓名、身份证号、身份证人像照片与权威库的证件照进行比对，是否属于同一个人，从而验证身份证信息的真实性。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIdCardInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIdCardInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIdNameDate(
            self,
            request: models.CheckIdNameDateRequest,
            opts: Dict = None,
    ) -> models.CheckIdNameDateResponse:
        """
        本接口用于校验姓名、身份证号、身份证有效期的真实性和一致性。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIdNameDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIdNameDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckPhoneAndName(
            self,
            request: models.CheckPhoneAndNameRequest,
            opts: Dict = None,
    ) -> models.CheckPhoneAndNameResponse:
        """
        手机号二要素核验接口用于校验手机号和姓名的真实性和一致性，支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckPhoneAndName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckPhoneAndNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectAIFakeFaces(
            self,
            request: models.DetectAIFakeFacesRequest,
            opts: Dict = None,
    ) -> models.DetectAIFakeFacesResponse:
        """
        基于多模态的AI大模型算法，提供对人脸图片、视频的防攻击检测能力，可针对性有效识别高仿真的AIGC换脸、高清翻拍、批量黑产攻击、水印等攻击痕迹，增强对图片和视频的防伪安全能力。
        """
        
        kwargs = {}
        kwargs["action"] = "DetectAIFakeFaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectAIFakeFacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectAuth(
            self,
            request: models.DetectAuthRequest,
            opts: Dict = None,
    ) -> models.DetectAuthResponse:
        """
        每次调用人脸核身SaaS化服务前，需先调用本接口获取BizToken，用来串联核身流程，在验证完成后，用于获取验证结果信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DetectAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EncryptedPhoneVerification(
            self,
            request: models.EncryptedPhoneVerificationRequest,
            opts: Dict = None,
    ) -> models.EncryptedPhoneVerificationResponse:
        """
        本接口用于校验手机号、姓名和身份证号的真实性和一致性，入参支持明文、MD5和SHA256加密传输。
        """
        
        kwargs = {}
        kwargs["action"] = "EncryptedPhoneVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EncryptedPhoneVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetActionSequence(
            self,
            request: models.GetActionSequenceRequest,
            opts: Dict = None,
    ) -> models.GetActionSequenceResponse:
        """
        使用动作活体检测模式前，需调用本接口获取动作顺序。
        """
        
        kwargs = {}
        kwargs["action"] = "GetActionSequence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetActionSequenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDetectInfo(
            self,
            request: models.GetDetectInfoRequest,
            opts: Dict = None,
    ) -> models.GetDetectInfoResponse:
        """
        完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\*24\*3,600秒）可多次拉取。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDetectInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDetectInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDetectInfoEnhanced(
            self,
            request: models.GetDetectInfoEnhancedRequest,
            opts: Dict = None,
    ) -> models.GetDetectInfoEnhancedResponse:
        """
        完成验证后，用BizToken调用本接口获取结果信息，BizToken生成后三天内（3\*24\*3,600秒）可多次拉取。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDetectInfoEnhanced"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDetectInfoEnhancedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEidResult(
            self,
            request: models.GetEidResultRequest,
            opts: Dict = None,
    ) -> models.GetEidResultResponse:
        """
        完成验证后，用EidToken调用本接口获取结果信息，EidToken生成后三天内（3\*24\*3,600秒）可多次拉取。
        """
        
        kwargs = {}
        kwargs["action"] = "GetEidResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEidResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEidToken(
            self,
            request: models.GetEidTokenRequest,
            opts: Dict = None,
    ) -> models.GetEidTokenResponse:
        """
        每次调用E证通服务前，需先调用本接口获取EidToken，用来串联E证通流程，在验证完成后，用于获取E证通结果信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetEidToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEidTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFaceIdResult(
            self,
            request: models.GetFaceIdResultRequest,
            opts: Dict = None,
    ) -> models.GetFaceIdResultResponse:
        """
        完成验证后，用FaceIdToken调用本接口获取结果信息，FaceIdToken生成后三天内（3\*24\*3,600秒）可多次拉取。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFaceIdResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFaceIdResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFaceIdRiskInfo(
            self,
            request: models.GetFaceIdRiskInfoRequest,
            opts: Dict = None,
    ) -> models.GetFaceIdRiskInfoResponse:
        """
        完成验证后，用FaceIdToken调用本接口获取设备风险相关信息，FaceIdToken生成后三天内（3\*24\*3,600秒）可多次拉取。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFaceIdRiskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFaceIdRiskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFaceIdToken(
            self,
            request: models.GetFaceIdTokenRequest,
            opts: Dict = None,
    ) -> models.GetFaceIdTokenResponse:
        """
        每次调用人脸核身SDK服务前，需先调用本接口获取SDKToken，用来串联核身流程，在验证完成后，用于获取验证结果信息，该token仅能核身一次。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFaceIdToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFaceIdTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFaceidRiskInfoToken(
            self,
            request: models.GetFaceidRiskInfoTokenRequest,
            opts: Dict = None,
    ) -> models.GetFaceidRiskInfoTokenResponse:
        """
        每次调用人脸核身SDK服务前，需先调用本接口获取SDKToken，用来串联核身流程，在验证完成后，用于获取风险结果信息，该Token仅能核身一次。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFaceidRiskInfoToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFaceidRiskInfoTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLiveCode(
            self,
            request: models.GetLiveCodeRequest,
            opts: Dict = None,
    ) -> models.GetLiveCodeResponse:
        """
        使用数字活体检测模式前，需调用本接口获取数字验证码。
        """
        
        kwargs = {}
        kwargs["action"] = "GetLiveCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLiveCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWeChatBillDetails(
            self,
            request: models.GetWeChatBillDetailsRequest,
            opts: Dict = None,
    ) -> models.GetWeChatBillDetailsResponse:
        """
        查询微信渠道服务（微信小程序、微信原生H5、微信普通H5）的账单明细及计费状态。
        """
        
        kwargs = {}
        kwargs["action"] = "GetWeChatBillDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWeChatBillDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IdCardOCRVerification(
            self,
            request: models.IdCardOCRVerificationRequest,
            opts: Dict = None,
    ) -> models.IdCardOCRVerificationResponse:
        """
        本接口用于校验姓名和身份证号的真实性和一致性，您可以通过输入姓名和身份证号或传入身份证人像面照片提供所需验证信息。
        """
        
        kwargs = {}
        kwargs["action"] = "IdCardOCRVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IdCardOCRVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IdCardVerification(
            self,
            request: models.IdCardVerificationRequest,
            opts: Dict = None,
    ) -> models.IdCardVerificationResponse:
        """
        传入姓名和身份证号，校验两者的真实性和一致性。
        """
        
        kwargs = {}
        kwargs["action"] = "IdCardVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IdCardVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageRecognition(
            self,
            request: models.ImageRecognitionRequest,
            opts: Dict = None,
    ) -> models.ImageRecognitionResponse:
        """
        传入照片和身份信息，判断该照片与权威库的证件照是否属于同一个人（该接口已停止接入，新客户请使用<a href="https://cloud.tencent.com/document/product/1007/102203">照片人脸核身（V2.0）</a>接口）。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageRecognition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageRecognitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageRecognitionV2(
            self,
            request: models.ImageRecognitionV2Request,
            opts: Dict = None,
    ) -> models.ImageRecognitionV2Response:
        """
        传入照片和身份信息，判断该照片与权威库的证件照是否属于同一个人。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageRecognitionV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageRecognitionV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LivenessCompare(
            self,
            request: models.LivenessCompareRequest,
            opts: Dict = None,
    ) -> models.LivenessCompareResponse:
        """
        传入视频和照片，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与上传照片是否属于同一个人。
        """
        
        kwargs = {}
        kwargs["action"] = "LivenessCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LivenessCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LivenessRecognition(
            self,
            request: models.LivenessRecognitionRequest,
            opts: Dict = None,
    ) -> models.LivenessRecognitionResponse:
        """
        传入视频和身份信息，先判断视频中是否为真人，判断为真人后，再判断该视频中的人与权威库的证件照是否属于同一个人。
        """
        
        kwargs = {}
        kwargs["action"] = "LivenessRecognition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LivenessRecognitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MinorsVerification(
            self,
            request: models.MinorsVerificationRequest,
            opts: Dict = None,
    ) -> models.MinorsVerificationResponse:
        """
        通过传入手机号或姓名和身份证号，结合权威数据源和腾讯健康守护可信模型，判断该信息是否真实且年满18周岁。腾讯健康守护可信模型覆盖了上十亿手机库源，覆盖率高、准确率高，如果不在库中的手机号，还可以通过姓名+身份证进行兜底验证。
        """
        
        kwargs = {}
        kwargs["action"] = "MinorsVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MinorsVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MobileNetworkTimeVerification(
            self,
            request: models.MobileNetworkTimeVerificationRequest,
            opts: Dict = None,
    ) -> models.MobileNetworkTimeVerificationResponse:
        """
        本接口用于查询手机号在网时长，输入手机号进行查询。
        """
        
        kwargs = {}
        kwargs["action"] = "MobileNetworkTimeVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MobileNetworkTimeVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MobileStatus(
            self,
            request: models.MobileStatusRequest,
            opts: Dict = None,
    ) -> models.MobileStatusResponse:
        """
        本接口用于验证手机号的状态，您可以输入手机号进行查询。
        """
        
        kwargs = {}
        kwargs["action"] = "MobileStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MobileStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseNfcData(
            self,
            request: models.ParseNfcDataRequest,
            opts: Dict = None,
    ) -> models.ParseNfcDataResponse:
        """
        解析SDK获取到的证件NFC数据，接口传入SDK返回的ReqId，返回证件信息（个别字段为特定证件类型特有）。SDK生成的ReqId五分钟内有效，重复查询仅收一次费。支持身份证类证件（二代身份证、港澳居住证、台湾居住证、外国人永居证）以及旅行类证件（港澳通行证、台湾通行证、台胞证、回乡证）的NFC识别及核验。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseNfcData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseNfcDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PhoneVerification(
            self,
            request: models.PhoneVerificationRequest,
            opts: Dict = None,
    ) -> models.PhoneVerificationResponse:
        """
        本接口用于校验手机号、姓名和身份证号的真实性和一致性。支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。
        """
        
        kwargs = {}
        kwargs["action"] = "PhoneVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PhoneVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PhoneVerificationCMCC(
            self,
            request: models.PhoneVerificationCMCCRequest,
            opts: Dict = None,
    ) -> models.PhoneVerificationCMCCResponse:
        """
        本接口用于校验中国移动手机号、姓名和身份证号的真实性和一致性。中国移动支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。
        """
        
        kwargs = {}
        kwargs["action"] = "PhoneVerificationCMCC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PhoneVerificationCMCCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PhoneVerificationCTCC(
            self,
            request: models.PhoneVerificationCTCCRequest,
            opts: Dict = None,
    ) -> models.PhoneVerificationCTCCResponse:
        """
        本接口用于校验中国电信手机号、姓名和身份证号的真实性和一致性。中国电信支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。
        """
        
        kwargs = {}
        kwargs["action"] = "PhoneVerificationCTCC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PhoneVerificationCTCCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PhoneVerificationCUCC(
            self,
            request: models.PhoneVerificationCUCCRequest,
            opts: Dict = None,
    ) -> models.PhoneVerificationCUCCResponse:
        """
        本接口用于校验中国联通手机号、姓名和身份证号的真实性和一致性。中国联通支持的手机号段详情请查阅<a href="https://cloud.tencent.com/document/product/1007/46063">运营商类</a>文档。
        """
        
        kwargs = {}
        kwargs["action"] = "PhoneVerificationCUCC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PhoneVerificationCUCCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)