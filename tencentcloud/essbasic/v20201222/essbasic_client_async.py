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
from tencentcloud.essbasic.v20201222 import models
from typing import Dict


class EssbasicClient(AbstractClient):
    _apiVersion = '2020-12-22'
    _endpoint = 'essbasic.tencentcloudapi.com'
    _service = 'essbasic'

    async def ArchiveFlow(
            self,
            request: models.ArchiveFlowRequest,
            opts: Dict = None,
    ) -> models.ArchiveFlowResponse:
        """
        此接口（ArchiveFlow）用于流程的归档。

        注意：归档后的流程不可再进行发送、签署、拒签、撤回等一系列操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ArchiveFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ArchiveFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelFlow(
            self,
            request: models.CancelFlowRequest,
            opts: Dict = None,
    ) -> models.CancelFlowResponse:
        """
        此接口（CancelFlow）用于撤销正在进行中的流程。

        注：已归档流程不可完成撤销动作。
        """
        
        kwargs = {}
        kwargs["action"] = "CancelFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBankCard2EVerification(
            self,
            request: models.CheckBankCard2EVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckBankCard2EVerificationResponse:
        """
        该接口为第三方平台向电子签平台验证银行卡二要素
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBankCard2EVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBankCard2EVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBankCard3EVerification(
            self,
            request: models.CheckBankCard3EVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckBankCard3EVerificationResponse:
        """
        该接口为第三方平台向电子签平台验证银行卡三要素
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBankCard3EVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBankCard3EVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBankCard4EVerification(
            self,
            request: models.CheckBankCard4EVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckBankCard4EVerificationResponse:
        """
        该接口为第三方平台向电子签平台验证银行卡四要素
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBankCard4EVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBankCard4EVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBankCardVerification(
            self,
            request: models.CheckBankCardVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckBankCardVerificationResponse:
        """
        该接口为第三方平台向电子签平台验证银行卡二/三/四要素
        银行卡二要素(同CheckBankCard2EVerification): bank_card + name
        银行卡三要素(同CheckBankCard3EVerification): bank_card + name + id_card_number
        银行卡四要素(同CheckBankCard4EVerification): bank_card + name + id_card_number + mobile
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBankCardVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBankCardVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFaceIdentify(
            self,
            request: models.CheckFaceIdentifyRequest,
            opts: Dict = None,
    ) -> models.CheckFaceIdentifyResponse:
        """
        该接口为第三方平台向电子签平台检测慧眼或腾讯电子签小程序人脸核身结果
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFaceIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFaceIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIdCardVerification(
            self,
            request: models.CheckIdCardVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckIdCardVerificationResponse:
        """
        该接口为第三方平台向电子签平台验证姓名和身份证信息
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIdCardVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIdCardVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckMobileAndName(
            self,
            request: models.CheckMobileAndNameRequest,
            opts: Dict = None,
    ) -> models.CheckMobileAndNameResponse:
        """
        该接口为第三方平台向电子签平台验证手机号二要素
        """
        
        kwargs = {}
        kwargs["action"] = "CheckMobileAndName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckMobileAndNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckMobileVerification(
            self,
            request: models.CheckMobileVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckMobileVerificationResponse:
        """
        该接口为第三方平台向电子签平台验证手机号三要素
        """
        
        kwargs = {}
        kwargs["action"] = "CheckMobileVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckMobileVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckVerifyCodeMatchFlowId(
            self,
            request: models.CheckVerifyCodeMatchFlowIdRequest,
            opts: Dict = None,
    ) -> models.CheckVerifyCodeMatchFlowIdResponse:
        """
        此接口用于确认验证码是否正确
        """
        
        kwargs = {}
        kwargs["action"] = "CheckVerifyCodeMatchFlowId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckVerifyCodeMatchFlowIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFaceIdSign(
            self,
            request: models.CreateFaceIdSignRequest,
            opts: Dict = None,
    ) -> models.CreateFaceIdSignResponse:
        """
        该接口为第三方平台向电子签平台获取慧眼慧眼API签名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFaceIdSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFaceIdSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFlowByFiles(
            self,
            request: models.CreateFlowByFilesRequest,
            opts: Dict = None,
    ) -> models.CreateFlowByFilesResponse:
        """
        此接口（CreateFlowByFiles）用于通过PDF文件创建签署流程。

        注意：调用此接口前，请先调用多文件上传接口 (UploadFiles)，提前上传合同文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlowByFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlowByFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateH5FaceIdUrl(
            self,
            request: models.CreateH5FaceIdUrlRequest,
            opts: Dict = None,
    ) -> models.CreateH5FaceIdUrlResponse:
        """
        该接口为第三方平台向电子签平台获取慧眼H5人脸核身Url
        """
        
        kwargs = {}
        kwargs["action"] = "CreateH5FaceIdUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateH5FaceIdUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePreviewSignUrl(
            self,
            request: models.CreatePreviewSignUrlRequest,
            opts: Dict = None,
    ) -> models.CreatePreviewSignUrlResponse:
        """
        此接口（CreatePreviewSignUrl）用于生成生成预览签署URL。

        注：调用此接口前，请确保您已提前调用了发送流程接口（SendFlow）指定相关签署方。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePreviewSignUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePreviewSignUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSeal(
            self,
            request: models.CreateSealRequest,
            opts: Dict = None,
    ) -> models.CreateSealResponse:
        """
        此接口（CreateSeal）用于创建个人/企业印章。

        注意：使用FileId参数指定印章，需先调用多文件上传 (UploadFiles) 上传印章图片。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServerFlowSign(
            self,
            request: models.CreateServerFlowSignRequest,
            opts: Dict = None,
    ) -> models.CreateServerFlowSignResponse:
        """
        此接口（CreateServerFlowSign）用于静默签署文件。

        注：
        1、此接口为白名单接口，调用前请提前与客服经理或邮件至e-contract@tencent.com进行联系。
        2、仅合同发起者可使用流程静默签署能力。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServerFlowSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServerFlowSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSignUrl(
            self,
            request: models.CreateSignUrlRequest,
            opts: Dict = None,
    ) -> models.CreateSignUrlResponse:
        """
        此接口（CreateSignUrl）用于生成指定用户的签署URL。

        注：调用此接口前，请确保您已提前调用了发送流程接口（SendFlow）指定相关签署方。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSignUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSignUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubOrganization(
            self,
            request: models.CreateSubOrganizationRequest,
            opts: Dict = None,
    ) -> models.CreateSubOrganizationResponse:
        """
        此接口（CreateSubOrganization）用于在腾讯电子签内注册子机构。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubOrganizationAndSeal(
            self,
            request: models.CreateSubOrganizationAndSealRequest,
            opts: Dict = None,
    ) -> models.CreateSubOrganizationAndSealResponse:
        """
        此接口（CreateSubOrganizationAndSeal）用于注册子机构，同时系统将为该子企业自动生成一个默认电子印章图片。

        注意：
        1. 在后续的签署流程中，若未指定签署使用的印章ID，则默认调用自动生成的印章图片进行签署。
        2. 此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubOrganizationAndSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubOrganizationAndSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        此接口（CreateUser）用于注册腾讯电子签个人用户。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserAndSeal(
            self,
            request: models.CreateUserAndSealRequest,
            opts: Dict = None,
    ) -> models.CreateUserAndSealResponse:
        """
        第三方应用可通过此接口（CreateUserAndSeal）注册腾讯电子签实名个人用户，同时系统将为该用户自动生成一个默认电子签名图片。

        注意：
        1. 在后续的签署流程中，若未指定签署使用的印章ID，则默认调用自动生成的签名图片进行签署。
        2. 此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserAndSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserAndSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSeal(
            self,
            request: models.DeleteSealRequest,
            opts: Dict = None,
    ) -> models.DeleteSealResponse:
        """
        此接口 (DeleteSeal) 用于删除指定ID的印章。

        注意：默认印章不支持删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCatalogApprovers(
            self,
            request: models.DescribeCatalogApproversRequest,
            opts: Dict = None,
    ) -> models.DescribeCatalogApproversResponse:
        """
        第三方应用可通过此接口（DescribeCatalogApprovers）查询指定目录的参与者列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCatalogApprovers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCatalogApproversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCatalogSignComponents(
            self,
            request: models.DescribeCatalogSignComponentsRequest,
            opts: Dict = None,
    ) -> models.DescribeCatalogSignComponentsResponse:
        """
        第三方应用可通过此接口（DescribeCatalogSignComponents）拉取目录签署区
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCatalogSignComponents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCatalogSignComponentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomFlowIds(
            self,
            request: models.DescribeCustomFlowIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomFlowIdsResponse:
        """
        此接口（DescribeCustomFlowIds）用于通过自定义流程id来查询对应的电子签流程id
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomFlowIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomFlowIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomFlowIdsByFlowId(
            self,
            request: models.DescribeCustomFlowIdsByFlowIdRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomFlowIdsByFlowIdResponse:
        """
        此接口（DescribeCustomFlowIdsByFlowId）用于根据流程id反查自定义流程id
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomFlowIdsByFlowId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomFlowIdsByFlowIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFaceIdPhotos(
            self,
            request: models.DescribeFaceIdPhotosRequest,
            opts: Dict = None,
    ) -> models.DescribeFaceIdPhotosResponse:
        """
        该接口为第三方平台向电子签平台获取慧眼人脸核身照片
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFaceIdPhotos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFaceIdPhotosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFaceIdResults(
            self,
            request: models.DescribeFaceIdResultsRequest,
            opts: Dict = None,
    ) -> models.DescribeFaceIdResultsResponse:
        """
        该接口为第三方平台向电子签平台获取慧眼人脸核身结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFaceIdResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFaceIdResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileIdsByCustomIds(
            self,
            request: models.DescribeFileIdsByCustomIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileIdsByCustomIdsResponse:
        """
        根据用户自定义id查询文件id
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileIdsByCustomIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileIdsByCustomIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileUrls(
            self,
            request: models.DescribeFileUrlsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileUrlsResponse:
        """
        此接口（DescribeFileUrls）用于获取签署文件下载的URL。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileUrls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileUrlsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlow(
            self,
            request: models.DescribeFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowResponse:
        """
        通过此接口（DescribeFlow）可查询签署流程的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowApprovers(
            self,
            request: models.DescribeFlowApproversRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowApproversResponse:
        """
        第三方应用可通过此接口（DescribeFlowApprovers）查询流程参与者信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowApprovers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowApproversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowFiles(
            self,
            request: models.DescribeFlowFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowFilesResponse:
        """
        查询流程文件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSeals(
            self,
            request: models.DescribeSealsRequest,
            opts: Dict = None,
    ) -> models.DescribeSealsResponse:
        """
        此接口（DescribeSeals）用于查询指定ID的印章信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSeals"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSealsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubOrganizations(
            self,
            request: models.DescribeSubOrganizationsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubOrganizationsResponse:
        """
        此接口（DescribeSubOrganizations）用于查询子机构信息。

        注：此接口仅可查询您所属机构应用号创建的子机构信息，不可跨应用/跨机构查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubOrganizations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubOrganizationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsers(
            self,
            request: models.DescribeUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersResponse:
        """
        此接口（DescribeUsers）用于查询应用号下的个人用户信息。

        注：此接口仅可查询您所属机构应用号创建的个人用户信息，不可跨应用/跨机构查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyFlowFile(
            self,
            request: models.DestroyFlowFileRequest,
            opts: Dict = None,
    ) -> models.DestroyFlowFileResponse:
        """
        通过此接口（DestroyFlowFile）可删除指定流程中的合同文件。

        注：调用此接口前，请确保此流程已属于归档状态。您可通过查询流程信息接口（DescribeFlow）进行查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyFlowFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyFlowFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateOrganizationSeal(
            self,
            request: models.GenerateOrganizationSealRequest,
            opts: Dict = None,
    ) -> models.GenerateOrganizationSealResponse:
        """
        生成企业电子印章
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateOrganizationSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateOrganizationSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateUserSeal(
            self,
            request: models.GenerateUserSealRequest,
            opts: Dict = None,
    ) -> models.GenerateUserSealResponse:
        """
        此接口（GenerateUserSeal）用于生成个人签名图片。

        注意：
        1. 个人签名由用户注册时预留的姓名信息生成，不支持自定义签名内容。
        2. 个人用户仅支持拥有一个系统生成的电子签名。
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateUserSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateUserSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOrganizationDefaultSeal(
            self,
            request: models.ModifyOrganizationDefaultSealRequest,
            opts: Dict = None,
    ) -> models.ModifyOrganizationDefaultSealResponse:
        """
        此接口 (ModifyOrganizationDefaultSeal) 用于重新指定企业默认印章。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOrganizationDefaultSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOrganizationDefaultSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySeal(
            self,
            request: models.ModifySealRequest,
            opts: Dict = None,
    ) -> models.ModifySealResponse:
        """
        此接口（ModifySeal）用于修改指定印章ID的印章图片和名称。

        注：印章类型暂不支持修改，如需调整，请联系客服经理或通过创建印章接口（CreateSeal）进行创建新印章。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubOrganizationInfo(
            self,
            request: models.ModifySubOrganizationInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySubOrganizationInfoResponse:
        """
        此接口（ModifySubOrganizationInfo）用于更新子机构信息。

        注：若修改子机构名称或更新机构证件照片，需要重新通过子机构实名接口（VerifySubOrganization）进行重新实名。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubOrganizationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubOrganizationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        此接口（ModifyUser）用于更新个人用户信息。

        注：若修改用户姓名，需要重新通过个人用户实名接口（VerifyUser）进行重新实名。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserDefaultSeal(
            self,
            request: models.ModifyUserDefaultSealRequest,
            opts: Dict = None,
    ) -> models.ModifyUserDefaultSealResponse:
        """
        此接口 (ModifyUserDefaultSeal) 用于重新指定个人默认印章。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserDefaultSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserDefaultSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectFlow(
            self,
            request: models.RejectFlowRequest,
            opts: Dict = None,
    ) -> models.RejectFlowResponse:
        """
        此接口（RejectFlow）用于用户拒绝签署合同流程。
        """
        
        kwargs = {}
        kwargs["action"] = "RejectFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendFlow(
            self,
            request: models.SendFlowRequest,
            opts: Dict = None,
    ) -> models.SendFlowResponse:
        """
        此接口（SendFlow）用于指定签署者及签署内容，后续可通过生成签署接口（CreateSignUrl）获取签署url。
        """
        
        kwargs = {}
        kwargs["action"] = "SendFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendFlowUrl(
            self,
            request: models.SendFlowUrlRequest,
            opts: Dict = None,
    ) -> models.SendFlowUrlResponse:
        """
        发送流程并获取签署URL
        """
        
        kwargs = {}
        kwargs["action"] = "SendFlowUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendFlowUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendSignInnerVerifyCode(
            self,
            request: models.SendSignInnerVerifyCodeRequest,
            opts: Dict = None,
    ) -> models.SendSignInnerVerifyCodeResponse:
        """
        此接口用于发送签署验证码
        """
        
        kwargs = {}
        kwargs["action"] = "SendSignInnerVerifyCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendSignInnerVerifyCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SignFlow(
            self,
            request: models.SignFlowRequest,
            opts: Dict = None,
    ) -> models.SignFlowResponse:
        """
        此接口（SignFlow）可用于对流程文件进行签署。
        """
        
        kwargs = {}
        kwargs["action"] = "SignFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SignFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFiles(
            self,
            request: models.UploadFilesRequest,
            opts: Dict = None,
    ) -> models.UploadFilesResponse:
        """
        此接口（UploadFiles）用于文件上传。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifySubOrganization(
            self,
            request: models.VerifySubOrganizationRequest,
            opts: Dict = None,
    ) -> models.VerifySubOrganizationResponse:
        """
        此接口（VerifySubOrganization）用于通过子机构的实名认证。

        注：此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifySubOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifySubOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyUser(
            self,
            request: models.VerifyUserRequest,
            opts: Dict = None,
    ) -> models.VerifyUserResponse:
        """
        第三方应用可通过此接口（VerifyUser）将腾讯电子签个人用户的实名认证状态设为通过。

        注：此接口为白名单接口，如您需要使用此能力，请提前与客户经理沟通或邮件至e-contract@tencent.com与我们联系。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)