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
from tencentcloud.tdid.v20210519 import models
from typing import Dict


class TdidClient(AbstractClient):
    _apiVersion = '2021-05-19'
    _endpoint = 'tdid.tencentcloudapi.com'
    _service = 'tdid'

    async def CreateDisclosedCredential(
            self,
            request: models.CreateDisclosedCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateDisclosedCredentialResponse:
        """
        根据披露策略创建选择性披露凭证
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisclosedCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisclosedCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePresentation(
            self,
            request: models.CreatePresentationRequest,
            opts: Dict = None,
    ) -> models.CreatePresentationResponse:
        """
        创建凭证持有人的可验证表达
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePresentation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePresentationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDidByHost(
            self,
            request: models.CreateTDidByHostRequest,
            opts: Dict = None,
    ) -> models.CreateTDidByHostResponse:
        """
        自动生成公私钥对托管在DID平台，并注册DID标识
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDidByHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDidByHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDidByPubKey(
            self,
            request: models.CreateTDidByPubKeyRequest,
            opts: Dict = None,
    ) -> models.CreateTDidByPubKeyResponse:
        """
        使用导入的公钥文件注册DID标识
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDidByPubKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDidByPubKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeactivateTDid(
            self,
            request: models.DeactivateTDidRequest,
            opts: Dict = None,
    ) -> models.DeactivateTDidResponse:
        """
        更新DID标识的禁用状态
        """
        
        kwargs = {}
        kwargs["action"] = "DeactivateTDid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeactivateTDidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAppSummary(
            self,
            request: models.GetAppSummaryRequest,
            opts: Dict = None,
    ) -> models.GetAppSummaryResponse:
        """
        获取某个应用关键指标统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "GetAppSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAppSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCredentialState(
            self,
            request: models.GetCredentialStateRequest,
            opts: Dict = None,
    ) -> models.GetCredentialStateResponse:
        """
        获取凭证链上状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetCredentialState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCredentialStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOverSummary(
            self,
            request: models.GetOverSummaryRequest,
            opts: Dict = None,
    ) -> models.GetOverSummaryResponse:
        """
        获取某个应用关键指标统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "GetOverSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOverSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTDidByObjectId(
            self,
            request: models.GetTDidByObjectIdRequest,
            opts: Dict = None,
    ) -> models.GetTDidByObjectIdResponse:
        """
        通过业务层绑定的对象ID获取DID标识
        """
        
        kwargs = {}
        kwargs["action"] = "GetTDidByObjectId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTDidByObjectIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTDidDocument(
            self,
            request: models.GetTDidDocumentRequest,
            opts: Dict = None,
    ) -> models.GetTDidDocumentResponse:
        """
        获取DID标识的文档
        """
        
        kwargs = {}
        kwargs["action"] = "GetTDidDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTDidDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTDidPubKey(
            self,
            request: models.GetTDidPubKeyRequest,
            opts: Dict = None,
    ) -> models.GetTDidPubKeyResponse:
        """
        查询DID标识的认证公钥
        """
        
        kwargs = {}
        kwargs["action"] = "GetTDidPubKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTDidPubKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IssueCredential(
            self,
            request: models.IssueCredentialRequest,
            opts: Dict = None,
    ) -> models.IssueCredentialResponse:
        """
        颁发可验证凭证
        """
        
        kwargs = {}
        kwargs["action"] = "IssueCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IssueCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAuthorityInfo(
            self,
            request: models.QueryAuthorityInfoRequest,
            opts: Dict = None,
    ) -> models.QueryAuthorityInfoResponse:
        """
        查询权威机构信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAuthorityInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAuthorityInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCPT(
            self,
            request: models.QueryCPTRequest,
            opts: Dict = None,
    ) -> models.QueryCPTResponse:
        """
        查询凭证模板内容
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCPT"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCPTResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTDidAttribute(
            self,
            request: models.SetTDidAttributeRequest,
            opts: Dict = None,
    ) -> models.SetTDidAttributeResponse:
        """
        设置DID文档的自定义属性
        """
        
        kwargs = {}
        kwargs["action"] = "SetTDidAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTDidAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCredentialState(
            self,
            request: models.UpdateCredentialStateRequest,
            opts: Dict = None,
    ) -> models.UpdateCredentialStateResponse:
        """
        1. 首次更新凭证状态基于不同场景参数有所差异，分以下两种场景：
        (1)  颁发凭证的DID是本腾讯云账号创建
        (2) 颁发凭证的DID是非本腾讯云账号创建(此调用方式也适用于场景1)
        2. 首次更新过凭证状态后，凭证状态已绑定该账号的链上用户，后续更新凭证状态只需参数CredentialStatus即可, OperateCredential和OriginCredential参数均不需要
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCredentialState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCredentialStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyCredentials(
            self,
            request: models.VerifyCredentialsRequest,
            opts: Dict = None,
    ) -> models.VerifyCredentialsResponse:
        """
        验证已签名的可验证凭证
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyCredentials"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyCredentialsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyPresentation(
            self,
            request: models.VerifyPresentationRequest,
            opts: Dict = None,
    ) -> models.VerifyPresentationResponse:
        """
        验证可验证表达的内容
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyPresentation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyPresentationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)