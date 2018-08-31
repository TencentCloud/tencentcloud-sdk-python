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


class GetInvokeTxRequest(AbstractModel):
    """GetInvokeTx请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param ClusterId: cluster标识
        :type ClusterId: str
        :param ChannelName: 通道名称
        :type ChannelName: str
        :param PeerName: 节点名称
        :type PeerName: str
        :param PeerGroup: 节点所属组织名称
        :type PeerGroup: str
        :param TxId: 事务ID
        :type TxId: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChannelName = None
        self.PeerName = None
        self.PeerGroup = None
        self.TxId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.ChannelName = params.get("ChannelName")
        self.PeerName = params.get("PeerName")
        self.PeerGroup = params.get("PeerGroup")
        self.TxId = params.get("TxId")


class GetInvokeTxResponse(AbstractModel):
    """GetInvokeTx返回参数结构体

    """

    def __init__(self):
        """
        :param TxValidationCode: 状态码
        :type TxValidationCode: int
        :param TxValidationMsg: 消息
        :type TxValidationMsg: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TxValidationCode = None
        self.TxValidationMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxValidationCode = params.get("TxValidationCode")
        self.TxValidationMsg = params.get("TxValidationMsg")
        self.RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param ClusterId: cluster标识
        :type ClusterId: str
        :param ChaincodeName: 合约名称
        :type ChaincodeName: str
        :param ChannelName: 通道名称
        :type ChannelName: str
        :param Peers: 使用的节点名称及对应组织名称
        :type Peers: list of PeerSet
        :param FuncName: 函数名
        :type FuncName: str
        :param Args: 函数参数列表
        :type Args: list of str
        :param AsyncFlag: 同步调用标识
        :type AsyncFlag: int
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChaincodeName = None
        self.ChannelName = None
        self.Peers = None
        self.FuncName = None
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
        self.Args = params.get("Args")
        self.AsyncFlag = params.get("AsyncFlag")


class InvokeResponse(AbstractModel):
    """Invoke返回参数结构体

    """

    def __init__(self):
        """
        :param Txid: 交易编号
        :type Txid: str
        :param Events: 返回内容
        :type Events: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param ClusterId: cluster标识
        :type ClusterId: str
        :param ChaincodeName: 合约名称
        :type ChaincodeName: str
        :param ChannelName: 通道名称
        :type ChannelName: str
        :param Peers: 使用的节点名称及对应组织名称
        :type Peers: list of PeerSet
        :param FuncName: 函数名
        :type FuncName: str
        :param Args: 函数参数列表
        :type Args: list of str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChaincodeName = None
        self.ChannelName = None
        self.Peers = None
        self.FuncName = None
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
        self.Args = params.get("Args")


class QueryResponse(AbstractModel):
    """Query返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 查询结果数据
        :type Data: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")