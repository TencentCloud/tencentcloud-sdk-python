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


    def AddLabel(self, request):
        """下线已有内测接口，待上线正式版本的接口

        DID添加标签

        :param request: Request instance for AddLabel.
        :type request: :class:`tencentcloud.tdid.v20210519.models.AddLabelRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.AddLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLabel", params, headers=headers)
            response = json.loads(body)
            model = models.AddLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckChain(self, request):
        """该接口不再使用

        检查区块链信息

        :param request: Request instance for CheckChain.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CheckChainRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CheckChainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckChain", params, headers=headers)
            response = json.loads(body)
            model = models.CheckChainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCredential(self, request):
        """该接口不再使用

        创建凭证

        :param request: Request instance for CreateCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSelectiveCredential(self, request):
        """该接口不再使用

        创建选择性批露凭证

        :param request: Request instance for CreateSelectiveCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateSelectiveCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateSelectiveCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSelectiveCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSelectiveCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDid(self, request):
        """该接口不再使用

        创建机构DID

        :param request: Request instance for CreateTDid.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDid", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDidByPrivateKey(self, request):
        """该接口不再使用

        新建DID根据私钥生成Tdid

        :param request: Request instance for CreateTDidByPrivateKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPrivateKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPrivateKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDidByPrivateKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidByPrivateKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDidByPublicKey(self, request):
        """该接口不再使用

         新建DID根据公钥生成Tdid

        :param request: Request instance for CreateTDidByPublicKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPublicKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDidByPublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidByPublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAgencyTDid(self, request):
        """该接口已废弃

        本机构DID详情

        :param request: Request instance for GetAgencyTDid.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetAgencyTDidRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetAgencyTDidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAgencyTDid", params, headers=headers)
            response = json.loads(body)
            model = models.GetAgencyTDidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAuthorityIssuer(self, request):
        """该接口不再使用

        获取权威机构信息

        :param request: Request instance for GetAuthorityIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetAuthorityIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetAuthorityIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAuthorityIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.GetAuthorityIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetConsortiumClusterList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        获取联盟bcos网络列表

        :param request: Request instance for GetConsortiumClusterList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumClusterListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetConsortiumClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.GetConsortiumClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetConsortiumList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        获取联盟列表

        :param request: Request instance for GetConsortiumList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetConsortiumList", params, headers=headers)
            response = json.loads(body)
            model = models.GetConsortiumListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCptInfo(self, request):
        """该接口不再使用

        凭证模版详情

        :param request: Request instance for GetCptInfo.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCptInfoRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCptInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCptInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetCptInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCredentialCptRank(self, request):
        """下线已有内测接口，待上线正式版本的接口

        凭证颁发按机构排行

        :param request: Request instance for GetCredentialCptRank.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialCptRankRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialCptRankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialCptRank", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialCptRankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCredentialStatus(self, request):
        """该接口不再使用

        获取凭证链上状态信息

        :param request: Request instance for GetCredentialStatus.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialStatusRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidDocument(self, request):
        """该接口不再使用

        查看DID文档

        :param request: Request instance for GetDidDocument.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidDocumentRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidDocument", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterCpt(self, request):
        """该接口不再使用

        凭证模版新建

        :param request: Request instance for RegisterCpt.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RegisterCptRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RegisterCptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterCpt", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterCptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCredentialStatus(self, request):
        """该接口不再使用

        设置凭证链上状态

        :param request: Request instance for SetCredentialStatus.
        :type request: :class:`tencentcloud.tdid.v20210519.models.SetCredentialStatusRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.SetCredentialStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCredentialStatus", params, headers=headers)
            response = json.loads(body)
            model = models.SetCredentialStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyCredential(self, request):
        """该接口不再使用

        验证凭证

        :param request: Request instance for VerifyCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyCredential", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))