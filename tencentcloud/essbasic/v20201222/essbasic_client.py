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
from tencentcloud.essbasic.v20201222 import models


class EssbasicClient(AbstractClient):
    _apiVersion = '2020-12-22'
    _endpoint = 'essbasic.tencentcloudapi.com'
    _service = 'essbasic'


    def ArchiveFlow(self, request):
        """此接口（ArchiveFlow）用于流程的归档。

        注意：归档后的流程不可再进行发送、签署、拒签、撤回等一系列操作。

        :param request: Request instance for ArchiveFlow.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.ArchiveFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.ArchiveFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ArchiveFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ArchiveFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelFlow(self, request):
        """此接口（CancelFlow）用于撤销正在进行中的流程。

        注：已归档流程不可完成撤销动作。

        :param request: Request instance for CancelFlow.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CancelFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CancelFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CancelFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckBankCard2EVerification(self, request):
        """该接口为第三方平台向电子签平台验证银行卡二要素

        :param request: Request instance for CheckBankCard2EVerification.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCard2EVerificationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCard2EVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBankCard2EVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBankCard2EVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckBankCard3EVerification(self, request):
        """该接口为第三方平台向电子签平台验证银行卡三要素

        :param request: Request instance for CheckBankCard3EVerification.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCard3EVerificationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCard3EVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBankCard3EVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBankCard3EVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckBankCard4EVerification(self, request):
        """该接口为第三方平台向电子签平台验证银行卡四要素

        :param request: Request instance for CheckBankCard4EVerification.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCard4EVerificationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCard4EVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBankCard4EVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBankCard4EVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckBankCardVerification(self, request):
        """该接口为第三方平台向电子签平台验证银行卡二/三/四要素
        银行卡二要素(同CheckBankCard2EVerification): bank_card + name
        银行卡三要素(同CheckBankCard3EVerification): bank_card + name + id_card_number
        银行卡四要素(同CheckBankCard4EVerification): bank_card + name + id_card_number + mobile

        :param request: Request instance for CheckBankCardVerification.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCardVerificationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckBankCardVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBankCardVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBankCardVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckFaceIdentify(self, request):
        """该接口为第三方平台向电子签平台检测慧眼或腾讯电子签小程序人脸核身结果

        :param request: Request instance for CheckFaceIdentify.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckFaceIdentifyRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckFaceIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFaceIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFaceIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckIdCardVerification(self, request):
        """该接口为第三方平台向电子签平台验证姓名和身份证信息

        :param request: Request instance for CheckIdCardVerification.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckIdCardVerificationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckIdCardVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIdCardVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIdCardVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckMobileAndName(self, request):
        """该接口为第三方平台向电子签平台验证手机号二要素

        :param request: Request instance for CheckMobileAndName.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckMobileAndNameRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckMobileAndNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckMobileAndName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckMobileAndNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckMobileVerification(self, request):
        """该接口为第三方平台向电子签平台验证手机号三要素

        :param request: Request instance for CheckMobileVerification.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckMobileVerificationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckMobileVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckMobileVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckMobileVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckVerifyCodeMatchFlowId(self, request):
        """此接口用于确认验证码是否正确

        :param request: Request instance for CheckVerifyCodeMatchFlowId.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CheckVerifyCodeMatchFlowIdRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CheckVerifyCodeMatchFlowIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckVerifyCodeMatchFlowId", params, headers=headers)
            response = json.loads(body)
            model = models.CheckVerifyCodeMatchFlowIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFaceIdSign(self, request):
        """该接口为第三方平台向电子签平台获取慧眼慧眼API签名

        :param request: Request instance for CreateFaceIdSign.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateFaceIdSignRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateFaceIdSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFaceIdSign", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFaceIdSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFlowByFiles(self, request):
        """此接口（CreateFlowByFiles）用于通过PDF文件创建签署流程。

        注意：调用此接口前，请先调用多文件上传接口 (UploadFiles)，提前上传合同文件。

        :param request: Request instance for CreateFlowByFiles.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateFlowByFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateFlowByFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowByFiles", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlowByFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateH5FaceIdUrl(self, request):
        """该接口为第三方平台向电子签平台获取慧眼H5人脸核身Url

        :param request: Request instance for CreateH5FaceIdUrl.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateH5FaceIdUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateH5FaceIdUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateH5FaceIdUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateH5FaceIdUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePreviewSignUrl(self, request):
        """此接口（CreatePreviewSignUrl）用于生成生成预览签署URL。

        注：调用此接口前，请确保您已提前调用了发送流程接口（SendFlow）指定相关签署方。

        :param request: Request instance for CreatePreviewSignUrl.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreatePreviewSignUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreatePreviewSignUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePreviewSignUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePreviewSignUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSeal(self, request):
        """此接口（CreateSeal）用于创建个人/企业印章。

        注意：使用FileId参数指定印章，需先调用多文件上传 (UploadFiles) 上传印章图片。

        :param request: Request instance for CreateSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSeal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServerFlowSign(self, request):
        """此接口（CreateServerFlowSign）用于静默签署文件。

        注：
        1、此接口为白名单接口，调用前请提前与客服经理或邮件至e-contract@tencent.com进行联系。
        2、仅合同发起者可使用流程静默签署能力。

        :param request: Request instance for CreateServerFlowSign.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateServerFlowSignRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateServerFlowSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServerFlowSign", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServerFlowSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSignUrl(self, request):
        """此接口（CreateSignUrl）用于生成指定用户的签署URL。

        注：调用此接口前，请确保您已提前调用了发送流程接口（SendFlow）指定相关签署方。

        :param request: Request instance for CreateSignUrl.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateSignUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateSignUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSignUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubOrganization(self, request):
        """此接口（CreateSubOrganization）用于在腾讯电子签内注册子机构。

        :param request: Request instance for CreateSubOrganization.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateSubOrganizationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateSubOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubOrganizationAndSeal(self, request):
        """此接口（CreateSubOrganizationAndSeal）用于注册子机构，同时系统将为该子企业自动生成一个默认电子印章图片。

        注意：
        1. 在后续的签署流程中，若未指定签署使用的印章ID，则默认调用自动生成的印章图片进行签署。
        2. 此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。

        :param request: Request instance for CreateSubOrganizationAndSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateSubOrganizationAndSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateSubOrganizationAndSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubOrganizationAndSeal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubOrganizationAndSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUser(self, request):
        """此接口（CreateUser）用于注册腾讯电子签个人用户。

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUserAndSeal(self, request):
        """第三方应用可通过此接口（CreateUserAndSeal）注册腾讯电子签实名个人用户，同时系统将为该用户自动生成一个默认电子签名图片。

        注意：
        1. 在后续的签署流程中，若未指定签署使用的印章ID，则默认调用自动生成的签名图片进行签署。
        2. 此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。

        :param request: Request instance for CreateUserAndSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.CreateUserAndSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.CreateUserAndSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserAndSeal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserAndSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSeal(self, request):
        """此接口 (DeleteSeal) 用于删除指定ID的印章。

        注意：默认印章不支持删除

        :param request: Request instance for DeleteSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DeleteSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DeleteSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSeal", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCatalogApprovers(self, request):
        """第三方应用可通过此接口（DescribeCatalogApprovers）查询指定目录的参与者列表

        :param request: Request instance for DescribeCatalogApprovers.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeCatalogApproversRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeCatalogApproversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCatalogApprovers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCatalogApproversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCatalogSignComponents(self, request):
        """第三方应用可通过此接口（DescribeCatalogSignComponents）拉取目录签署区

        :param request: Request instance for DescribeCatalogSignComponents.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeCatalogSignComponentsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeCatalogSignComponentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCatalogSignComponents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCatalogSignComponentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomFlowIds(self, request):
        """此接口（DescribeCustomFlowIds）用于通过自定义流程id来查询对应的电子签流程id

        :param request: Request instance for DescribeCustomFlowIds.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeCustomFlowIdsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeCustomFlowIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomFlowIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomFlowIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomFlowIdsByFlowId(self, request):
        """此接口（DescribeCustomFlowIdsByFlowId）用于根据流程id反查自定义流程id

        :param request: Request instance for DescribeCustomFlowIdsByFlowId.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeCustomFlowIdsByFlowIdRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeCustomFlowIdsByFlowIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomFlowIdsByFlowId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomFlowIdsByFlowIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFaceIdPhotos(self, request):
        """该接口为第三方平台向电子签平台获取慧眼人脸核身照片

        :param request: Request instance for DescribeFaceIdPhotos.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeFaceIdPhotosRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeFaceIdPhotosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFaceIdPhotos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFaceIdPhotosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFaceIdResults(self, request):
        """该接口为第三方平台向电子签平台获取慧眼人脸核身结果

        :param request: Request instance for DescribeFaceIdResults.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeFaceIdResultsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeFaceIdResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFaceIdResults", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFaceIdResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileIdsByCustomIds(self, request):
        """根据用户自定义id查询文件id

        :param request: Request instance for DescribeFileIdsByCustomIds.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeFileIdsByCustomIdsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeFileIdsByCustomIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileIdsByCustomIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileIdsByCustomIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileUrls(self, request):
        """此接口（DescribeFileUrls）用于获取签署文件下载的URL。

        :param request: Request instance for DescribeFileUrls.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeFileUrlsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeFileUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileUrls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlow(self, request):
        """通过此接口（DescribeFlow）可查询签署流程的详细信息。

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowApprovers(self, request):
        """第三方应用可通过此接口（DescribeFlowApprovers）查询流程参与者信息。

        :param request: Request instance for DescribeFlowApprovers.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeFlowApproversRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeFlowApproversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowApprovers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowApproversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowFiles(self, request):
        """查询流程文件

        :param request: Request instance for DescribeFlowFiles.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeFlowFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeFlowFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSeals(self, request):
        """此接口（DescribeSeals）用于查询指定ID的印章信息。

        :param request: Request instance for DescribeSeals.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeSealsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeSealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSeals", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubOrganizations(self, request):
        """此接口（DescribeSubOrganizations）用于查询子机构信息。

        注：此接口仅可查询您所属机构应用号创建的子机构信息，不可跨应用/跨机构查询。

        :param request: Request instance for DescribeSubOrganizations.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeSubOrganizationsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeSubOrganizationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubOrganizations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubOrganizationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsers(self, request):
        """此接口（DescribeUsers）用于查询应用号下的个人用户信息。

        注：此接口仅可查询您所属机构应用号创建的个人用户信息，不可跨应用/跨机构查询。

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DescribeUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyFlowFile(self, request):
        """通过此接口（DestroyFlowFile）可删除指定流程中的合同文件。

        注：调用此接口前，请确保此流程已属于归档状态。您可通过查询流程信息接口（DescribeFlow）进行查询。

        :param request: Request instance for DestroyFlowFile.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.DestroyFlowFileRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.DestroyFlowFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyFlowFile", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyFlowFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateOrganizationSeal(self, request):
        """生成企业电子印章

        :param request: Request instance for GenerateOrganizationSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.GenerateOrganizationSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.GenerateOrganizationSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateOrganizationSeal", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateOrganizationSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateUserSeal(self, request):
        """此接口（GenerateUserSeal）用于生成个人签名图片。

        注意：
        1. 个人签名由用户注册时预留的姓名信息生成，不支持自定义签名内容。
        2. 个人用户仅支持拥有一个系统生成的电子签名。

        :param request: Request instance for GenerateUserSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.GenerateUserSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.GenerateUserSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateUserSeal", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateUserSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyOrganizationDefaultSeal(self, request):
        """此接口 (ModifyOrganizationDefaultSeal) 用于重新指定企业默认印章。

        :param request: Request instance for ModifyOrganizationDefaultSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.ModifyOrganizationDefaultSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.ModifyOrganizationDefaultSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrganizationDefaultSeal", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOrganizationDefaultSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySeal(self, request):
        """此接口（ModifySeal）用于修改指定印章ID的印章图片和名称。

        注：印章类型暂不支持修改，如需调整，请联系客服经理或通过创建印章接口（CreateSeal）进行创建新印章。

        :param request: Request instance for ModifySeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.ModifySealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.ModifySealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySeal", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubOrganizationInfo(self, request):
        """此接口（ModifySubOrganizationInfo）用于更新子机构信息。

        注：若修改子机构名称或更新机构证件照片，需要重新通过子机构实名接口（VerifySubOrganization）进行重新实名。

        :param request: Request instance for ModifySubOrganizationInfo.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.ModifySubOrganizationInfoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.ModifySubOrganizationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubOrganizationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubOrganizationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUser(self, request):
        """此接口（ModifyUser）用于更新个人用户信息。

        注：若修改用户姓名，需要重新通过个人用户实名接口（VerifyUser）进行重新实名。

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUserDefaultSeal(self, request):
        """此接口 (ModifyUserDefaultSeal) 用于重新指定个人默认印章。

        :param request: Request instance for ModifyUserDefaultSeal.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.ModifyUserDefaultSealRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.ModifyUserDefaultSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserDefaultSeal", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserDefaultSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RejectFlow(self, request):
        """此接口（RejectFlow）用于用户拒绝签署合同流程。

        :param request: Request instance for RejectFlow.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.RejectFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.RejectFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectFlow", params, headers=headers)
            response = json.loads(body)
            model = models.RejectFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendFlow(self, request):
        """此接口（SendFlow）用于指定签署者及签署内容，后续可通过生成签署接口（CreateSignUrl）获取签署url。

        :param request: Request instance for SendFlow.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.SendFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.SendFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendFlow", params, headers=headers)
            response = json.loads(body)
            model = models.SendFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendFlowUrl(self, request):
        """发送流程并获取签署URL

        :param request: Request instance for SendFlowUrl.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.SendFlowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.SendFlowUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendFlowUrl", params, headers=headers)
            response = json.loads(body)
            model = models.SendFlowUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendSignInnerVerifyCode(self, request):
        """此接口用于发送签署验证码

        :param request: Request instance for SendSignInnerVerifyCode.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.SendSignInnerVerifyCodeRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.SendSignInnerVerifyCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendSignInnerVerifyCode", params, headers=headers)
            response = json.loads(body)
            model = models.SendSignInnerVerifyCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SignFlow(self, request):
        """此接口（SignFlow）可用于对流程文件进行签署。

        :param request: Request instance for SignFlow.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.SignFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.SignFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SignFlow", params, headers=headers)
            response = json.loads(body)
            model = models.SignFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadFiles(self, request):
        """此接口（UploadFiles）用于文件上传。

        :param request: Request instance for UploadFiles.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.UploadFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.UploadFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFiles", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VerifySubOrganization(self, request):
        """此接口（VerifySubOrganization）用于通过子机构的实名认证。

        注：此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。

        :param request: Request instance for VerifySubOrganization.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.VerifySubOrganizationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.VerifySubOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifySubOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.VerifySubOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VerifyUser(self, request):
        """第三方应用可通过此接口（VerifyUser）将腾讯电子签个人用户的实名认证状态设为通过。

        注：此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。

        :param request: Request instance for VerifyUser.
        :type request: :class:`tencentcloud.essbasic.v20201222.models.VerifyUserRequest`
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.VerifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)