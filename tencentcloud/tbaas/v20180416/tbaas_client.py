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
from tencentcloud.tbaas.v20180416 import models


class TbaasClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'tbaas.tencentcloudapi.com'
    _service = 'tbaas'


    def ApplyChainMakerBatchUserCert(self, request):
        """批量申请长安链用户签名证书

        :param request: Request instance for ApplyChainMakerBatchUserCert.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.ApplyChainMakerBatchUserCertRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ApplyChainMakerBatchUserCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyChainMakerBatchUserCert", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyChainMakerBatchUserCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyUserCert(self, request):
        """申请用户证书

        :param request: Request instance for ApplyUserCert.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.ApplyUserCertRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ApplyUserCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyUserCert", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyUserCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateChaincodeAndInstallForUser(self, request):
        """创建并安装合约

        :param request: Request instance for CreateChaincodeAndInstallForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.CreateChaincodeAndInstallForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.CreateChaincodeAndInstallForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChaincodeAndInstallForUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChaincodeAndInstallForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadUserCert(self, request):
        """下载用户证书

        :param request: Request instance for DownloadUserCert.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DownloadUserCertRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DownloadUserCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadUserCert", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadUserCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetBlockList(self, request):
        """查看当前网络下的所有区块列表，分页展示

        :param request: Request instance for GetBlockList.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBlockList", params, headers=headers)
            response = json.loads(body)
            model = models.GetBlockListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetBlockTransactionListForUser(self, request):
        """获取区块内的交易列表

        :param request: Request instance for GetBlockTransactionListForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBlockTransactionListForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBlockTransactionListForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBlockTransactionListForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetBlockTransactionListForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetChaincodeCompileLogForUser(self, request):
        """获取合约编译日志

        :param request: Request instance for GetChaincodeCompileLogForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeCompileLogForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeCompileLogForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChaincodeCompileLogForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetChaincodeCompileLogForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetChaincodeInitializeResultForUser(self, request):
        """实例化结果查询

        :param request: Request instance for GetChaincodeInitializeResultForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeInitializeResultForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeInitializeResultForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChaincodeInitializeResultForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetChaincodeInitializeResultForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetChaincodeLogForUser(self, request):
        """获取合约容器日志

        :param request: Request instance for GetChaincodeLogForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeLogForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeLogForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChaincodeLogForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetChaincodeLogForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetChannelListForUser(self, request):
        """获取通道列表

        :param request: Request instance for GetChannelListForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChannelListForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChannelListForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChannelListForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetChannelListForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetClusterListForUser(self, request):
        """获取该用户的网络列表。网络信息中包含组织信息，但仅包含该用户所在组织的信息。

        :param request: Request instance for GetClusterListForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetClusterListForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetClusterListForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetClusterListForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetClusterListForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetClusterSummary(self, request):
        """获取区块链网络概要

        :param request: Request instance for GetClusterSummary.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetClusterSummaryRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetClusterSummary", params, headers=headers)
            response = json.loads(body)
            model = models.GetClusterSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetInvokeTx(self, request):
        """Invoke异步调用结果查询

        :param request: Request instance for GetInvokeTx.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetInvokeTxRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetInvokeTxResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInvokeTx", params, headers=headers)
            response = json.loads(body)
            model = models.GetInvokeTxResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetLatesdTransactionList(self, request):
        """获取最新交易列表（已废弃）

        :param request: Request instance for GetLatesdTransactionList.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetLatesdTransactionListRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetLatesdTransactionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLatesdTransactionList", params, headers=headers)
            response = json.loads(body)
            model = models.GetLatesdTransactionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetLatestTransactionList(self, request):
        """获取fabric最新交易列表

        :param request: Request instance for GetLatestTransactionList.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetLatestTransactionListRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetLatestTransactionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLatestTransactionList", params, headers=headers)
            response = json.loads(body)
            model = models.GetLatestTransactionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPeerLogForUser(self, request):
        """获取节点日志

        :param request: Request instance for GetPeerLogForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetPeerLogForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetPeerLogForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPeerLogForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetPeerLogForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetTransactionDetailForUser(self, request):
        """获取交易详情

        :param request: Request instance for GetTransactionDetailForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetTransactionDetailForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetTransactionDetailForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTransactionDetailForUser", params, headers=headers)
            response = json.loads(body)
            model = models.GetTransactionDetailForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InitializeChaincodeForUser(self, request):
        """实例化合约

        :param request: Request instance for InitializeChaincodeForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InitializeChaincodeForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InitializeChaincodeForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitializeChaincodeForUser", params, headers=headers)
            response = json.loads(body)
            model = models.InitializeChaincodeForUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Invoke(self, request):
        """新增交易

        :param request: Request instance for Invoke.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Invoke", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InvokeChainMakerContract(self, request):
        """调用长安链合约执行交易

        :param request: Request instance for InvokeChainMakerContract.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeChainMakerContractRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeChainMakerContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeChainMakerContract", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeChainMakerContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InvokeChainMakerDemoContract(self, request):
        """调用长安链体验网络合约执行交易

        :param request: Request instance for InvokeChainMakerDemoContract.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeChainMakerDemoContractRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeChainMakerDemoContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeChainMakerDemoContract", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeChainMakerDemoContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Query(self, request):
        """查询交易

        :param request: Request instance for Query.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Query", params, headers=headers)
            response = json.loads(body)
            model = models.QueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryChainMakerBlockTransaction(self, request):
        """查询长安链指定高度区块的交易

        :param request: Request instance for QueryChainMakerBlockTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerBlockTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerBlockTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerBlockTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChainMakerBlockTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryChainMakerContract(self, request):
        """调用长安链合约查询

        :param request: Request instance for QueryChainMakerContract.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerContractRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerContract", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChainMakerContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryChainMakerDemoBlockTransaction(self, request):
        """查询长安链体验网络指定高度区块的交易

        :param request: Request instance for QueryChainMakerDemoBlockTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerDemoBlockTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerDemoBlockTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerDemoBlockTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChainMakerDemoBlockTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryChainMakerDemoContract(self, request):
        """调用长安链体验网络合约查询

        :param request: Request instance for QueryChainMakerDemoContract.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerDemoContractRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerDemoContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerDemoContract", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChainMakerDemoContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryChainMakerDemoTransaction(self, request):
        """通过交易ID查询长安链体验网络交易

        :param request: Request instance for QueryChainMakerDemoTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerDemoTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerDemoTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerDemoTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChainMakerDemoTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryChainMakerTransaction(self, request):
        """通过交易ID查询长安链交易

        :param request: Request instance for QueryChainMakerTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChainMakerTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SrvInvoke(self, request):
        """trustsql服务统一接口

        :param request: Request instance for SrvInvoke.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.SrvInvokeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.SrvInvokeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SrvInvoke", params, headers=headers)
            response = json.loads(body)
            model = models.SrvInvokeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)