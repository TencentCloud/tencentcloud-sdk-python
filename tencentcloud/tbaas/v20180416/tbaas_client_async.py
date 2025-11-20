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
from tencentcloud.tbaas.v20180416 import models
from typing import Dict


class TbaasClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'tbaas.tencentcloudapi.com'
    _service = 'tbaas'

    async def ApplyChainMakerBatchUserCert(
            self,
            request: models.ApplyChainMakerBatchUserCertRequest,
            opts: Dict = None,
    ) -> models.ApplyChainMakerBatchUserCertResponse:
        """
        批量申请长安链用户签名证书
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyChainMakerBatchUserCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyChainMakerBatchUserCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyUserCert(
            self,
            request: models.ApplyUserCertRequest,
            opts: Dict = None,
    ) -> models.ApplyUserCertResponse:
        """
        申请用户证书
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyUserCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyUserCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFabricBlock(
            self,
            request: models.DescribeFabricBlockRequest,
            opts: Dict = None,
    ) -> models.DescribeFabricBlockResponse:
        """
        获取Fabric某区块的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFabricBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFabricBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFabricTransaction(
            self,
            request: models.DescribeFabricTransactionRequest,
            opts: Dict = None,
    ) -> models.DescribeFabricTransactionResponse:
        """
        获取Fabric交易的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFabricTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFabricTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadUserCert(
            self,
            request: models.DownloadUserCertRequest,
            opts: Dict = None,
    ) -> models.DownloadUserCertResponse:
        """
        下载用户证书
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadUserCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadUserCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetBlockList(
            self,
            request: models.GetBlockListRequest,
            opts: Dict = None,
    ) -> models.GetBlockListResponse:
        """
        查看当前网络下的所有区块列表，分页展示
        """
        
        kwargs = {}
        kwargs["action"] = "GetBlockList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetBlockListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetBlockTransactionListForUser(
            self,
            request: models.GetBlockTransactionListForUserRequest,
            opts: Dict = None,
    ) -> models.GetBlockTransactionListForUserResponse:
        """
        获取区块内交易列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetBlockTransactionListForUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetBlockTransactionListForUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetClusterSummary(
            self,
            request: models.GetClusterSummaryRequest,
            opts: Dict = None,
    ) -> models.GetClusterSummaryResponse:
        """
        获取区块链网络概要
        """
        
        kwargs = {}
        kwargs["action"] = "GetClusterSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetClusterSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetInvokeTx(
            self,
            request: models.GetInvokeTxRequest,
            opts: Dict = None,
    ) -> models.GetInvokeTxResponse:
        """
        Invoke异步调用结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "GetInvokeTx"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetInvokeTxResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLatestTransactionList(
            self,
            request: models.GetLatestTransactionListRequest,
            opts: Dict = None,
    ) -> models.GetLatestTransactionListResponse:
        """
        获取fabric最新交易列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetLatestTransactionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLatestTransactionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTransactionDetailForUser(
            self,
            request: models.GetTransactionDetailForUserRequest,
            opts: Dict = None,
    ) -> models.GetTransactionDetailForUserResponse:
        """
        获取交易的详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetTransactionDetailForUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTransactionDetailForUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Invoke(
            self,
            request: models.InvokeRequest,
            opts: Dict = None,
    ) -> models.InvokeResponse:
        """
        新增交易
        """
        
        kwargs = {}
        kwargs["action"] = "Invoke"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeChainMakerContract(
            self,
            request: models.InvokeChainMakerContractRequest,
            opts: Dict = None,
    ) -> models.InvokeChainMakerContractResponse:
        """
        调用长安链合约执行交易
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeChainMakerContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeChainMakerContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeChainMakerDemoContract(
            self,
            request: models.InvokeChainMakerDemoContractRequest,
            opts: Dict = None,
    ) -> models.InvokeChainMakerDemoContractResponse:
        """
        调用长安链体验网络合约执行交易
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeChainMakerDemoContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeChainMakerDemoContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeFabricChaincode(
            self,
            request: models.InvokeFabricChaincodeRequest,
            opts: Dict = None,
    ) -> models.InvokeFabricChaincodeResponse:
        """
        调用Fabric用户合约执行交易
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeFabricChaincode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeFabricChaincodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Query(
            self,
            request: models.QueryRequest,
            opts: Dict = None,
    ) -> models.QueryResponse:
        """
        查询交易
        """
        
        kwargs = {}
        kwargs["action"] = "Query"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChainMakerBlockTransaction(
            self,
            request: models.QueryChainMakerBlockTransactionRequest,
            opts: Dict = None,
    ) -> models.QueryChainMakerBlockTransactionResponse:
        """
        查询长安链指定高度区块的交易
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChainMakerBlockTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChainMakerBlockTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChainMakerContract(
            self,
            request: models.QueryChainMakerContractRequest,
            opts: Dict = None,
    ) -> models.QueryChainMakerContractResponse:
        """
        调用长安链合约查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChainMakerContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChainMakerContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChainMakerDemoBlockTransaction(
            self,
            request: models.QueryChainMakerDemoBlockTransactionRequest,
            opts: Dict = None,
    ) -> models.QueryChainMakerDemoBlockTransactionResponse:
        """
        查询长安链体验网络指定高度区块的交易
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChainMakerDemoBlockTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChainMakerDemoBlockTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChainMakerDemoContract(
            self,
            request: models.QueryChainMakerDemoContractRequest,
            opts: Dict = None,
    ) -> models.QueryChainMakerDemoContractResponse:
        """
        调用长安链体验网络合约查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChainMakerDemoContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChainMakerDemoContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChainMakerDemoTransaction(
            self,
            request: models.QueryChainMakerDemoTransactionRequest,
            opts: Dict = None,
    ) -> models.QueryChainMakerDemoTransactionResponse:
        """
        通过交易ID查询长安链体验网络交易
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChainMakerDemoTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChainMakerDemoTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChainMakerTransaction(
            self,
            request: models.QueryChainMakerTransactionRequest,
            opts: Dict = None,
    ) -> models.QueryChainMakerTransactionResponse:
        """
        通过交易ID查询长安链交易
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChainMakerTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChainMakerTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFabricChaincode(
            self,
            request: models.QueryFabricChaincodeRequest,
            opts: Dict = None,
    ) -> models.QueryFabricChaincodeResponse:
        """
        调用Fabric用户合约查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFabricChaincode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFabricChaincodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SrvInvoke(
            self,
            request: models.SrvInvokeRequest,
            opts: Dict = None,
    ) -> models.SrvInvokeResponse:
        """
        trustsql服务统一接口
        """
        
        kwargs = {}
        kwargs["action"] = "SrvInvoke"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SrvInvokeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)