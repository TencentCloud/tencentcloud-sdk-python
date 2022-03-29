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


    def CreateCredential(self, request):
        """创建凭证

        :param request: Request instance for CreateCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateCredentialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCredential", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCredentialResponse()
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


    def CreateSelectiveCredential(self, request):
        """创建选择性批露凭证

        :param request: Request instance for CreateSelectiveCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateSelectiveCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateSelectiveCredentialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSelectiveCredential", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSelectiveCredentialResponse()
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


    def CreateTDid(self, request):
        """创建机构DID

        :param request: Request instance for CreateTDid.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTDid", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTDidResponse()
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


    def CreateTDidByPublicKey(self, request):
        """新建DID根据公钥生成Tdid

        :param request: Request instance for CreateTDidByPublicKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPublicKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPublicKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTDidByPublicKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTDidByPublicKeyResponse()
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


    def GetAuthorityIssuer(self, request):
        """获取权威机构信息

        :param request: Request instance for GetAuthorityIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetAuthorityIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetAuthorityIssuerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAuthorityIssuer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAuthorityIssuerResponse()
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


    def GetDidDocument(self, request):
        """查看DID文档

        :param request: Request instance for GetDidDocument.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidDocumentRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidDocumentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDidDocument", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDidDocumentResponse()
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


    def SetCredentialStatus(self, request):
        """设置凭证链上状态

        :param request: Request instance for SetCredentialStatus.
        :type request: :class:`tencentcloud.tdid.v20210519.models.SetCredentialStatusRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.SetCredentialStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetCredentialStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetCredentialStatusResponse()
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


    def VerifyCredential(self, request):
        """验证凭证

        :param request: Request instance for VerifyCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyCredential", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyCredentialResponse()
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