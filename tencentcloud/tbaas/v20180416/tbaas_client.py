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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFabricBlock(self, request):
        """获取Fabric某区块的详细信息

        :param request: Request instance for DescribeFabricBlock.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricBlockRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFabricBlock", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFabricBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFabricTransaction(self, request):
        """获取Fabric交易的详细信息

        :param request: Request instance for DescribeFabricTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DescribeFabricTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFabricTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFabricTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetBlockTransactionListForUser(self, request):
        """获取区块内交易列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTransactionDetailForUser(self, request):
        """获取交易的详情

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InvokeFabricChaincode(self, request):
        """调用Fabric用户合约执行交易

        :param request: Request instance for InvokeFabricChaincode.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeFabricChaincodeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeFabricChaincodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeFabricChaincode", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeFabricChaincodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryFabricChaincode(self, request):
        """调用Fabric用户合约查询

        :param request: Request instance for QueryFabricChaincode.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryFabricChaincodeRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryFabricChaincodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFabricChaincode", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFabricChaincodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))