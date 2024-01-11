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
from tencentcloud.tdid.v20210519 import models


class TdidClient(AbstractClient):
    _apiVersion = '2021-05-19'
    _endpoint = 'tdid.tencentcloudapi.com'
    _service = 'tdid'


    def CheckNewPurchase(self, request):
        """检查用户套餐购买状态

        :param request: Request instance for CheckNewPurchase.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CheckNewPurchaseRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CheckNewPurchaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckNewPurchase", params, headers=headers)
            response = json.loads(body)
            model = models.CheckNewPurchaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDidByHost(self, request):
        """自动生成公私钥对托管在DID平台，并注册DID标识

        :param request: Request instance for CreateTDidByHost.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByHostRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDidByHost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidByHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDidByPubKey(self, request):
        """使用导入的公钥文件注册DID标识

        :param request: Request instance for CreateTDidByPubKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPubKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPubKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDidByPubKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidByPubKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeactivateTDid(self, request):
        """更新DID标识的禁用状态

        :param request: Request instance for DeactivateTDid.
        :type request: :class:`tencentcloud.tdid.v20210519.models.DeactivateTDidRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.DeactivateTDidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeactivateTDid", params, headers=headers)
            response = json.loads(body)
            model = models.DeactivateTDidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCredentialState(self, request):
        """获取凭证链上状态信息

        :param request: Request instance for GetCredentialState.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialStateRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialState", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTDidDocument(self, request):
        """获取DID标识的文档

        :param request: Request instance for GetTDidDocument.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetTDidDocumentRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetTDidDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTDidDocument", params, headers=headers)
            response = json.loads(body)
            model = models.GetTDidDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IssueCredential(self, request):
        """颁发可验证凭证

        :param request: Request instance for IssueCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.IssueCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.IssueCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IssueCredential", params, headers=headers)
            response = json.loads(body)
            model = models.IssueCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCredentialState(self, request):
        """更新凭证的链上状态

        :param request: Request instance for UpdateCredentialState.
        :type request: :class:`tencentcloud.tdid.v20210519.models.UpdateCredentialStateRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.UpdateCredentialStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCredentialState", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCredentialStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyCredentials(self, request):
        """验证已签名的可验证凭证

        :param request: Request instance for VerifyCredentials.
        :type request: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialsRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))