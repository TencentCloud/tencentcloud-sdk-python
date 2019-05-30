# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class Block(AbstractModel):
    """区块对象

    """

    def __init__(self):
        """
        :param BlockNum: 区块编号
        :type BlockNum: int
        :param DataHash: 区块Hash数值
        :type DataHash: str
        :param BlockId: 区块ID，与区块编号一直
        :type BlockId: int
        :param PreHash: 前一个区块Hash（未使用）,与区块Hash数值一直
        :type PreHash: str
        :param TxCount: 区块内的交易数量
        :type TxCount: int
        """
        self.BlockNum = None
        self.DataHash = None
        self.BlockId = None
        self.PreHash = None
        self.TxCount = None


    def _deserialize(self, params):
        self.BlockNum = params.get("BlockNum")
        self.DataHash = params.get("DataHash")
        self.BlockId = params.get("BlockId")
        self.PreHash = params.get("PreHash")
        self.TxCount = params.get("TxCount")


class GetBlockListRequest(AbstractModel):
    """GetBlockList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名称，固定字段：block
        :type Module: str
        :param Operation: 操作名称，固定字段：block_list
        :type Operation: str
        :param ChannelId: 通道ID，固定字段：0
        :type ChannelId: int
        :param GroupId: 组织ID，固定字段：0
        :type GroupId: int
        :param ChannelName: 需要查询的通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param GroupName: 调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param Offset: 需要获取的起始交易偏移
        :type Offset: int
        :param Limit: 需要获取的交易数量
        :type Limit: int
        """
        self.Module = None
        self.Operation = None
        self.ChannelId = None
        self.GroupId = None
        self.ChannelName = None
        self.GroupName = None
        self.ClusterId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ChannelId = params.get("ChannelId")
        self.GroupId = params.get("GroupId")
        self.ChannelName = params.get("ChannelName")
        self.GroupName = params.get("GroupName")
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetBlockListResponse(AbstractModel):
    """GetBlockList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 区块数量
        :type TotalCount: int
        :param BlockList: 区块列表
        :type BlockList: list of Block
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BlockList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BlockList") is not None:
            self.BlockList = []
            for item in params.get("BlockList"):
                obj = Block()
                obj._deserialize(item)
                self.BlockList.append(obj)
        self.RequestId = params.get("RequestId")


class GetClusterSummaryRequest(AbstractModel):
    """GetClusterSummary请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名称，固定字段：cluster_mng
        :type Module: str
        :param Operation: 操作名称，固定字段：cluster_summary
        :type Operation: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param GroupId: 组织ID，固定字段：0
        :type GroupId: int
        :param GroupName: 调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")


class GetClusterSummaryResponse(AbstractModel):
    """GetClusterSummary返回参数结构体

    """

    def __init__(self):
        """
        :param TotalChannelCount: 网络通道总数量
        :type TotalChannelCount: int
        :param MyChannelCount: 当前组织创建的通道数量
        :type MyChannelCount: int
        :param OtherChannelCount: 其组织创建的通道数量
        :type OtherChannelCount: int
        :param JoinChannelCount: 当前组织加入的通道数量
        :type JoinChannelCount: int
        :param NoneChannelCount: 与当前组织无关的通道数量
        :type NoneChannelCount: int
        :param TotalPeerCount: 网络节点总数量
        :type TotalPeerCount: int
        :param MyPeerCount: 当前组织创建的节点数量
        :type MyPeerCount: int
        :param OtherPeerCount: 其他组织创建的节点数量
        :type OtherPeerCount: int
        :param TotalGroupCount: 网络组织总数量
        :type TotalGroupCount: int
        :param MyGroupCount: 当前组织创建的组织数量
        :type MyGroupCount: int
        :param OtherGroupCount: 其他组织创建的组织数量
        :type OtherGroupCount: int
        :param TotalChaincodeCount: 网络智能合约总数量
        :type TotalChaincodeCount: int
        :param RecentChaincodeCount: 最近7天发起的智能合约数量
        :type RecentChaincodeCount: int
        :param MyChaincodeCount: 当前组织发起的智能合约数量
        :type MyChaincodeCount: int
        :param OtherChaincodeCount: 其组织发起的智能合约数量
        :type OtherChaincodeCount: int
        :param TotalCertCount: 当前组织的证书总数量
        :type TotalCertCount: int
        :param TlsCertCount: 颁发给当前组织的证书数量
        :type TlsCertCount: int
        :param PeerCertCount: 网络背书节点证书数量
        :type PeerCertCount: int
        :param OrderCertCount: 网络排序节点证书数量
        :type OrderCertCount: int
        :param ClientCertCount: 当前组织业务证书数量
        :type ClientCertCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalChannelCount = None
        self.MyChannelCount = None
        self.OtherChannelCount = None
        self.JoinChannelCount = None
        self.NoneChannelCount = None
        self.TotalPeerCount = None
        self.MyPeerCount = None
        self.OtherPeerCount = None
        self.TotalGroupCount = None
        self.MyGroupCount = None
        self.OtherGroupCount = None
        self.TotalChaincodeCount = None
        self.RecentChaincodeCount = None
        self.MyChaincodeCount = None
        self.OtherChaincodeCount = None
        self.TotalCertCount = None
        self.TlsCertCount = None
        self.PeerCertCount = None
        self.OrderCertCount = None
        self.ClientCertCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalChannelCount = params.get("TotalChannelCount")
        self.MyChannelCount = params.get("MyChannelCount")
        self.OtherChannelCount = params.get("OtherChannelCount")
        self.JoinChannelCount = params.get("JoinChannelCount")
        self.NoneChannelCount = params.get("NoneChannelCount")
        self.TotalPeerCount = params.get("TotalPeerCount")
        self.MyPeerCount = params.get("MyPeerCount")
        self.OtherPeerCount = params.get("OtherPeerCount")
        self.TotalGroupCount = params.get("TotalGroupCount")
        self.MyGroupCount = params.get("MyGroupCount")
        self.OtherGroupCount = params.get("OtherGroupCount")
        self.TotalChaincodeCount = params.get("TotalChaincodeCount")
        self.RecentChaincodeCount = params.get("RecentChaincodeCount")
        self.MyChaincodeCount = params.get("MyChaincodeCount")
        self.OtherChaincodeCount = params.get("OtherChaincodeCount")
        self.TotalCertCount = params.get("TotalCertCount")
        self.TlsCertCount = params.get("TlsCertCount")
        self.PeerCertCount = params.get("PeerCertCount")
        self.OrderCertCount = params.get("OrderCertCount")
        self.ClientCertCount = params.get("ClientCertCount")
        self.RequestId = params.get("RequestId")


class GetInvokeTxRequest(AbstractModel):
    """GetInvokeTx请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：query_txid
        :type Operation: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param PeerName: 执行该查询交易的节点名称，可以在通道详情中获取该通道上的节点名称极其所属组织名称
        :type PeerName: str
        :param PeerGroup: 执行该查询交易的节点所属组织名称，可以在通道详情中获取该通道上的节点名称极其所属组织名称
        :type PeerGroup: str
        :param TxId: 交易ID
        :type TxId: str
        :param GroupName: 调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChannelName = None
        self.PeerName = None
        self.PeerGroup = None
        self.TxId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.ChannelName = params.get("ChannelName")
        self.PeerName = params.get("PeerName")
        self.PeerGroup = params.get("PeerGroup")
        self.TxId = params.get("TxId")
        self.GroupName = params.get("GroupName")


class GetInvokeTxResponse(AbstractModel):
    """GetInvokeTx返回参数结构体

    """

    def __init__(self):
        """
        :param TxValidationCode: 交易执行状态码
        :type TxValidationCode: int
        :param TxValidationMsg: 交易执行消息
        :type TxValidationMsg: str
        :param BlockId: 交易所在区块ID
        :type BlockId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxValidationCode = None
        self.TxValidationMsg = None
        self.BlockId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxValidationCode = params.get("TxValidationCode")
        self.TxValidationMsg = params.get("TxValidationMsg")
        self.BlockId = params.get("BlockId")
        self.RequestId = params.get("RequestId")


class GetLatesdTransactionListRequest(AbstractModel):
    """GetLatesdTransactionList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名称，固定字段：transaction
        :type Module: str
        :param Operation: 操作名称，固定字段：latest_transaction_list
        :type Operation: str
        :param GroupId: 组织ID，固定字段：0
        :type GroupId: int
        :param ChannelId: 通道ID，固定字段：0
        :type ChannelId: int
        :param LatestBlockNumber: 获取的最新交易的区块数量，取值范围1~5
        :type LatestBlockNumber: int
        :param GroupName: 调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param ChannelName: 需要查询的通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param Offset: 需要获取的起始交易偏移
        :type Offset: int
        :param Limit: 需要获取的交易数量
        :type Limit: int
        """
        self.Module = None
        self.Operation = None
        self.GroupId = None
        self.ChannelId = None
        self.LatestBlockNumber = None
        self.GroupName = None
        self.ChannelName = None
        self.ClusterId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupId = params.get("GroupId")
        self.ChannelId = params.get("ChannelId")
        self.LatestBlockNumber = params.get("LatestBlockNumber")
        self.GroupName = params.get("GroupName")
        self.ChannelName = params.get("ChannelName")
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetLatesdTransactionListResponse(AbstractModel):
    """GetLatesdTransactionList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 交易总数量
        :type TotalCount: int
        :param TransactionList: 交易列表
        :type TransactionList: list of TransactionItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TransactionList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TransactionList") is not None:
            self.TransactionList = []
            for item in params.get("TransactionList"):
                obj = TransactionItem()
                obj._deserialize(item)
                self.TransactionList.append(obj)
        self.RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：invoke
        :type Operation: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param ChaincodeName: 业务所属智能合约名称，可在智能合约详情或列表中获取
        :type ChaincodeName: str
        :param ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param Peers: 对该笔交易进行背书的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称极其所属组织名称
        :type Peers: list of PeerSet
        :param FuncName: 该笔交易需要调用的智能合约中的函数名称
        :type FuncName: str
        :param GroupName: 调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param Args: 被调用的函数参数列表
        :type Args: list of str
        :param AsyncFlag: 同步调用标识，可选参数，值为0或者不传表示使用同步方法调用，调用后会等待交易执行后再返回执行结果；值为1时表示使用异步方式调用Invoke，执行后会立即返回交易对应的Txid，后续需要通过GetInvokeTx这个API查询该交易的执行结果。（对于逻辑较为简单的交易，可以使用同步模式；对于逻辑较为复杂的交易，建议使用异步模式，否则容易导致API因等待时间过长，返回等待超时）
        :type AsyncFlag: int
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChaincodeName = None
        self.ChannelName = None
        self.Peers = None
        self.FuncName = None
        self.GroupName = None
        self.Args = None
        self.AsyncFlag = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.ChaincodeName = params.get("ChaincodeName")
        self.ChannelName = params.get("ChannelName")
        if params.get("Peers") is not None:
            self.Peers = []
            for item in params.get("Peers"):
                obj = PeerSet()
                obj._deserialize(item)
                self.Peers.append(obj)
        self.FuncName = params.get("FuncName")
        self.GroupName = params.get("GroupName")
        self.Args = params.get("Args")
        self.AsyncFlag = params.get("AsyncFlag")


class InvokeResponse(AbstractModel):
    """Invoke返回参数结构体

    """

    def __init__(self):
        """
        :param Txid: 交易ID
        :type Txid: str
        :param Events: 交易执行结果
        :type Events: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Txid = None
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Txid = params.get("Txid")
        self.Events = params.get("Events")
        self.RequestId = params.get("RequestId")


class PeerSet(AbstractModel):
    """PeerSet

    """

    def __init__(self):
        """
        :param PeerName: 节点名称
        :type PeerName: str
        :param OrgName: 组织名称
        :type OrgName: str
        """
        self.PeerName = None
        self.OrgName = None


    def _deserialize(self, params):
        self.PeerName = params.get("PeerName")
        self.OrgName = params.get("OrgName")


class QueryRequest(AbstractModel):
    """Query请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：query
        :type Operation: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param ChaincodeName: 业务所属智能合约名称，可在智能合约详情或列表中获取
        :type ChaincodeName: str
        :param ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param Peers: 执行该查询交易的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称极其所属组织名称
        :type Peers: list of PeerSet
        :param FuncName: 该笔交易查询需要调用的智能合约中的函数名称
        :type FuncName: str
        :param GroupName: 调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param Args: 被调用的函数参数列表
        :type Args: list of str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChaincodeName = None
        self.ChannelName = None
        self.Peers = None
        self.FuncName = None
        self.GroupName = None
        self.Args = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.ChaincodeName = params.get("ChaincodeName")
        self.ChannelName = params.get("ChannelName")
        if params.get("Peers") is not None:
            self.Peers = []
            for item in params.get("Peers"):
                obj = PeerSet()
                obj._deserialize(item)
                self.Peers.append(obj)
        self.FuncName = params.get("FuncName")
        self.GroupName = params.get("GroupName")
        self.Args = params.get("Args")


class QueryResponse(AbstractModel):
    """Query返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 查询结果数据
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TransactionItem(AbstractModel):
    """交易列表项信息

    """

    def __init__(self):
        """
        :param TransactionId: 交易ID
        :type TransactionId: str
        :param TransactionHash: 交易hash
        :type TransactionHash: str
        :param CreateOrgName: 创建交易的组织名
        :type CreateOrgName: str
        :param BlockId: 交易所在区块号
        :type BlockId: int
        :param TransactionType: 交易类型（普通交易和配置交易）
        :type TransactionType: str
        :param CreateTime: 交易创建时间
        :type CreateTime: str
        :param BlockHeight: 交易所在区块高度
        :type BlockHeight: int
        :param TransactionStatus: 交易状态
        :type TransactionStatus: str
        """
        self.TransactionId = None
        self.TransactionHash = None
        self.CreateOrgName = None
        self.BlockId = None
        self.TransactionType = None
        self.CreateTime = None
        self.BlockHeight = None
        self.TransactionStatus = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.TransactionHash = params.get("TransactionHash")
        self.CreateOrgName = params.get("CreateOrgName")
        self.BlockId = params.get("BlockId")
        self.TransactionType = params.get("TransactionType")
        self.CreateTime = params.get("CreateTime")
        self.BlockHeight = params.get("BlockHeight")
        self.TransactionStatus = params.get("TransactionStatus")