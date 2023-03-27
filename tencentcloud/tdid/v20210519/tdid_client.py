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
                raise TencentCloudSDKException(e.message, e.message)


    def CancelAuthorityIssuer(self, request):
        """下线已有内测接口，待上线正式版本的接口

        撤消权威机构认证

        :param request: Request instance for CancelAuthorityIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CancelAuthorityIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CancelAuthorityIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAuthorityIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAuthorityIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckChain(self, request):
        """检查区块链信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def CheckDidDeploy(self, request):
        """下线已有内测接口，待上线正式版本的接口

        检查部署情况

        :param request: Request instance for CheckDidDeploy.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CheckDidDeployRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CheckDidDeployResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDidDeploy", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDidDeployResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCredential(self, request):
        """创建凭证

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDidService(self, request):
        """下线已有内测接口，待上线正式版本的接口

        创建DID服务

        :param request: Request instance for CreateDidService.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateDidServiceRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateDidServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDidService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDidServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLabel(self, request):
        """下线已有内测接口，待上线正式版本的接口

        新建标签

        :param request: Request instance for CreateLabel.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateLabelRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLabel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLabelResponse()
            model._deserialize(response["Response"])
            return model
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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTDid(self, request):
        """创建机构DID

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTDidByPrivateKey(self, request):
        """新建DID根据私钥生成Tdid

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTDidByPublicKey(self, request):
        """新建DID根据公钥生成Tdid

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeployByName(self, request):
        """下线已有内测接口，待上线正式版本的接口

        通过Name部署TDID合约

        :param request: Request instance for DeployByName.
        :type request: :class:`tencentcloud.tdid.v20210519.models.DeployByNameRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.DeployByNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployByName", params, headers=headers)
            response = json.loads(body)
            model = models.DeployByNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownCpt(self, request):
        """下线已有内测接口，待上线正式版本的接口

        凭证模版下载

        :param request: Request instance for DownCpt.
        :type request: :class:`tencentcloud.tdid.v20210519.models.DownCptRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.DownCptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownCpt", params, headers=headers)
            response = json.loads(body)
            model = models.DownCptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableHash(self, request):
        """下线已有内测接口，待上线正式版本的接口

        启用合约

        :param request: Request instance for EnableHash.
        :type request: :class:`tencentcloud.tdid.v20210519.models.EnableHashRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.EnableHashResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableHash", params, headers=headers)
            response = json.loads(body)
            model = models.EnableHashResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def GetAuthoritiesList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        权威机构列表

        :param request: Request instance for GetAuthoritiesList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetAuthoritiesListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetAuthoritiesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAuthoritiesList", params, headers=headers)
            response = json.loads(body)
            model = models.GetAuthoritiesListResponse()
            model._deserialize(response["Response"])
            return model
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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def GetCptInfo(self, request):
        """凭证模版详情

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
                raise TencentCloudSDKException(e.message, e.message)


    def GetCptList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        凭证模版列表

        :param request: Request instance for GetCptList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCptListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCptListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCptList", params, headers=headers)
            response = json.loads(body)
            model = models.GetCptListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def GetCredentialIssueRank(self, request):
        """下线已有内测接口，待上线正式版本的接口

        凭证颁发按机构排行

        :param request: Request instance for GetCredentialIssueRank.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueRankRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueRankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialIssueRank", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialIssueRankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetCredentialIssueTrend(self, request):
        """下线已有内测接口，待上线正式版本的接口

        凭证颁发趋势

        :param request: Request instance for GetCredentialIssueTrend.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueTrendRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialIssueTrend", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialIssueTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetCredentialStatus(self, request):
        """获取凭证链上状态信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def GetDataPanel(self, request):
        """下线已有内测接口，待上线正式版本的接口

        概览

        :param request: Request instance for GetDataPanel.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDataPanelRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDataPanelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDataPanel", params, headers=headers)
            response = json.loads(body)
            model = models.GetDataPanelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDeployInfo(self, request):
        """下线已有内测接口，待上线正式版本的接口

        合约部署详情

        :param request: Request instance for GetDeployInfo.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDeployInfoRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDeployInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeployInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeployInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDeployList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        合约部署列表

        :param request: Request instance for GetDeployList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDeployListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDeployListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeployList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeployListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDidClusterDetail(self, request):
        """下线已有内测接口，待上线正式版本的接口

        获取DID区块链网络详情

        :param request: Request instance for GetDidClusterDetail.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterDetailRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDidClusterList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        获取用户的DID网络列表

        :param request: Request instance for GetDidClusterList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDidDetail(self, request):
        """下线已有内测接口，待上线正式版本的接口

        DID详情

        :param request: Request instance for GetDidDetail.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidDetailRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidDetailResponse()
            model._deserialize(response["Response"])
            return model
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
                raise TencentCloudSDKException(e.message, e.message)


    def GetDidList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        DID列表

        :param request: Request instance for GetDidList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDidRegisterTrend(self, request):
        """下线已有内测接口，待上线正式版本的接口

        DID注册趋势

        :param request: Request instance for GetDidRegisterTrend.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidRegisterTrendRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidRegisterTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidRegisterTrend", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidRegisterTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDidServiceDetail(self, request):
        """下线已有内测接口，待上线正式版本的接口

        获取DID服务详情

        :param request: Request instance for GetDidServiceDetail.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceDetailRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidServiceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidServiceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDidServiceList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        获取DID服务列表

        :param request: Request instance for GetDidServiceList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetGroupList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        主群组配置列表

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetLabelList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        标签列表

        :param request: Request instance for GetLabelList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetLabelListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetLabelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabelList", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPolicyList(self, request):
        """下线已有内测接口，待上线正式版本的接口

        披露策略Policy管理列表

        :param request: Request instance for GetPolicyList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetPolicyListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.GetPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPublicKey(self, request):
        """下线已有内测接口，待上线正式版本的接口

        查看公钥

        :param request: Request instance for GetPublicKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetPublicKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetPublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.GetPublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryPolicy(self, request):
        """下线已有内测接口，待上线正式版本的接口

        披露策略Policy查看

        :param request: Request instance for QueryPolicy.
        :type request: :class:`tencentcloud.tdid.v20210519.models.QueryPolicyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.QueryPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.QueryPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecognizeAuthorityIssuer(self, request):
        """下线已有内测接口，待上线正式版本的接口

        认证权威机构

        :param request: Request instance for RecognizeAuthorityIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RecognizeAuthorityIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RecognizeAuthorityIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeAuthorityIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeAuthorityIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterClaimPolicy(self, request):
        """下线已有内测接口，待上线正式版本的接口

        披露策略Policy注册

        :param request: Request instance for RegisterClaimPolicy.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RegisterClaimPolicyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RegisterClaimPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterClaimPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterClaimPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterCpt(self, request):
        """凭证模版新建

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
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterIssuer(self, request):
        """下线已有内测接口，待上线正式版本的接口

        注册为权威机构

        :param request: Request instance for RegisterIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RegisterIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RegisterIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveHash(self, request):
        """下线已有内测接口，待上线正式版本的接口

        删除合约

        :param request: Request instance for RemoveHash.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RemoveHashRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RemoveHashResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveHash", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveHashResponse()
            model._deserialize(response["Response"])
            return model
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
                raise TencentCloudSDKException(e.message, e.message)


    def VerifyCredential(self, request):
        """验证凭证

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
                raise TencentCloudSDKException(e.message, e.message)