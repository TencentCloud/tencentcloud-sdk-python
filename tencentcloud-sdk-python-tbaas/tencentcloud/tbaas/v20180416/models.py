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


class ApplyUserCertRequest(AbstractModel):
    """ApplyUserCert请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：cert_mng
        :type Module: str
        :param Operation: 操作名，固定字段：cert_apply_for_user
        :type Operation: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param GroupName: 申请证书的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param UserIdentity: 用户证书标识，用于标识用户证书，要求由纯小写字母组成，长度小于10
        :type UserIdentity: str
        :param Applicant: 证书申请实体，使用腾讯云账号实名认证的名称
        :type Applicant: str
        :param IdentityNum: 证件号码。如果腾讯云账号对应的实名认证类型为企业认证，填入“0”；如果腾讯云账号对应的实名认证类型为个人认证，填入个人身份证号码
        :type IdentityNum: str
        :param CsrData: csr p10证书文件。需要用户根据文档生成证书的CSR文件
        :type CsrData: str
        :param Notes: 证书备注信息
        :type Notes: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupName = None
        self.UserIdentity = None
        self.Applicant = None
        self.IdentityNum = None
        self.CsrData = None
        self.Notes = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        self.UserIdentity = params.get("UserIdentity")
        self.Applicant = params.get("Applicant")
        self.IdentityNum = params.get("IdentityNum")
        self.CsrData = params.get("CsrData")
        self.Notes = params.get("Notes")


class ApplyUserCertResponse(AbstractModel):
    """ApplyUserCert返回参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书ID
        :type CertId: int
        :param CertDn: 证书DN
        :type CertDn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertId = None
        self.CertDn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertDn = params.get("CertDn")
        self.RequestId = params.get("RequestId")


class BcosBlockObj(AbstractModel):
    """Bcos区块对象

    """

    def __init__(self):
        """
        :param BlockHash: 区块哈希
        :type BlockHash: str
        :param BlockNumber: 区块高度
        :type BlockNumber: int
        :param BlockTimestamp: 区块时间戳
        :type BlockTimestamp: str
        :param Sealer: 打包节点ID
        :type Sealer: str
        :param SealerIndex: 打包节点索引
        :type SealerIndex: int
        :param CreateTime: 记录保存时间
        :type CreateTime: str
        :param TransCount: 交易数量
        :type TransCount: int
        :param ModifyTime: 记录修改时间
        :type ModifyTime: str
        """
        self.BlockHash = None
        self.BlockNumber = None
        self.BlockTimestamp = None
        self.Sealer = None
        self.SealerIndex = None
        self.CreateTime = None
        self.TransCount = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.BlockHash = params.get("BlockHash")
        self.BlockNumber = params.get("BlockNumber")
        self.BlockTimestamp = params.get("BlockTimestamp")
        self.Sealer = params.get("Sealer")
        self.SealerIndex = params.get("SealerIndex")
        self.CreateTime = params.get("CreateTime")
        self.TransCount = params.get("TransCount")
        self.ModifyTime = params.get("ModifyTime")


class BcosTransInfo(AbstractModel):
    """Bcos交易信息对象

    """

    def __init__(self):
        """
        :param BlockNumber: 所属区块高度
        :type BlockNumber: int
        :param BlockTimestamp: 区块时间戳
        :type BlockTimestamp: str
        :param TransHash: 交易哈希
        :type TransHash: str
        :param TransFrom: 交易发起者
        :type TransFrom: str
        :param TransTo: 交易接收者
        :type TransTo: str
        :param CreateTime: 落库时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.BlockNumber = None
        self.BlockTimestamp = None
        self.TransHash = None
        self.TransFrom = None
        self.TransTo = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.BlockNumber = params.get("BlockNumber")
        self.BlockTimestamp = params.get("BlockTimestamp")
        self.TransHash = params.get("TransHash")
        self.TransFrom = params.get("TransFrom")
        self.TransTo = params.get("TransTo")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")


class Block(AbstractModel):
    """区块对象

    """

    def __init__(self):
        """
        :param BlockNum: 区块编号
        :type BlockNum: int
        :param DataHash: 区块Hash数值
        :type DataHash: str
        :param BlockId: 区块ID，与区块编号一致
        :type BlockId: int
        :param PreHash: 前一个区块Hash（未使用）,与区块Hash数值一致
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


class BlockByNumberHandlerRequest(AbstractModel):
    """BlockByNumberHandler请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：block
        :type Module: str
        :param Operation: 操作名，固定字段：block_by_number
        :type Operation: str
        :param GroupPk: 当前群组编号
        :type GroupPk: str
        :param BlockNumber: 区块高度
        :type BlockNumber: int
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.BlockNumber = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.BlockNumber = params.get("BlockNumber")


class BlockByNumberHandlerResponse(AbstractModel):
    """BlockByNumberHandler返回参数结构体

    """

    def __init__(self):
        """
        :param BlockJson: 返回区块json字符串
        :type BlockJson: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlockJson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlockJson = params.get("BlockJson")
        self.RequestId = params.get("RequestId")


class DeployDynamicContractHandlerRequest(AbstractModel):
    """DeployDynamicContractHandler请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：contract
        :type Module: str
        :param Operation: 操作名，固定字段：deploy_by_dynamic_contract
        :type Operation: str
        :param GroupPk: 群组编号
        :type GroupPk: str
        :param ContractName: 合约名称
        :type ContractName: str
        :param AbiInfo: 合约编译后的abi
        :type AbiInfo: str
        :param ByteCodeBin: 合约编译后的binary
        :type ByteCodeBin: str
        :param ConstructorParams: 构造函数入参
        :type ConstructorParams: list of str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.ContractName = None
        self.AbiInfo = None
        self.ByteCodeBin = None
        self.ConstructorParams = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.ContractName = params.get("ContractName")
        self.AbiInfo = params.get("AbiInfo")
        self.ByteCodeBin = params.get("ByteCodeBin")
        self.ConstructorParams = params.get("ConstructorParams")


class DeployDynamicContractHandlerResponse(AbstractModel):
    """DeployDynamicContractHandler返回参数结构体

    """

    def __init__(self):
        """
        :param ContractAddress: 部署成功返回的合约地址
        :type ContractAddress: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContractAddress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ContractAddress = params.get("ContractAddress")
        self.RequestId = params.get("RequestId")


class DownloadUserCertRequest(AbstractModel):
    """DownloadUserCert请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：cert_mng
        :type Module: str
        :param Operation: 操作名，固定字段：cert_download_for_user
        :type Operation: str
        :param CertId: 证书ID，可以在证书详情页面获取
        :type CertId: int
        :param CertDn: 证书DN，可以在证书详情页面获取
        :type CertDn: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param GroupName: 下载证书的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        """
        self.Module = None
        self.Operation = None
        self.CertId = None
        self.CertDn = None
        self.ClusterId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.CertId = params.get("CertId")
        self.CertDn = params.get("CertDn")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")


class DownloadUserCertResponse(AbstractModel):
    """DownloadUserCert返回参数结构体

    """

    def __init__(self):
        """
        :param CertName: 证书名称
        :type CertName: str
        :param CertCtx: 证书内容
        :type CertCtx: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertName = None
        self.CertCtx = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertCtx = params.get("CertCtx")
        self.RequestId = params.get("RequestId")


class EndorserGroup(AbstractModel):
    """背书组织及其节点列表

    """

    def __init__(self):
        """
        :param EndorserGroupName: 背书组织名称
        :type EndorserGroupName: str
        :param EndorserPeerList: 背书节点列表
        :type EndorserPeerList: list of str
        """
        self.EndorserGroupName = None
        self.EndorserPeerList = None


    def _deserialize(self, params):
        self.EndorserGroupName = params.get("EndorserGroupName")
        self.EndorserPeerList = params.get("EndorserPeerList")


class GetBlockListHandlerRequest(AbstractModel):
    """GetBlockListHandler请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：block
        :type Module: str
        :param Operation: 操作名，固定字段：get_block_list
        :type Operation: str
        :param Offset: 记录偏移数
        :type Offset: int
        :param Limit: 每页记录数
        :type Limit: int
        :param GroupPk: 当前群组编号
        :type GroupPk: str
        :param BlockHash: 区块哈希
        :type BlockHash: str
        """
        self.Module = None
        self.Operation = None
        self.Offset = None
        self.Limit = None
        self.GroupPk = None
        self.BlockHash = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupPk = params.get("GroupPk")
        self.BlockHash = params.get("BlockHash")


class GetBlockListHandlerResponse(AbstractModel):
    """GetBlockListHandler返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param GroupPk: 当前群组编号
        :type GroupPk: str
        :param List: 返回数据列表
        :type List: list of BcosBlockObj
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GroupPk = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.GroupPk = params.get("GroupPk")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BcosBlockObj()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


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


class GetBlockTransactionListForUserRequest(AbstractModel):
    """GetBlockTransactionListForUser请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：block_transaction_list_for_user
        :type Operation: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param GroupName: 参与交易的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param BlockId: 区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID
        :type BlockId: int
        :param Offset: 查询的交易列表起始偏移地址
        :type Offset: int
        :param Limit: 查询的交易列表数量
        :type Limit: int
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupName = None
        self.ChannelName = None
        self.BlockId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        self.ChannelName = params.get("ChannelName")
        self.BlockId = params.get("BlockId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetBlockTransactionListForUserResponse(AbstractModel):
    """GetBlockTransactionListForUser返回参数结构体

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
        :param JoinChannelCount: 当前组织加入的通道数量
        :type JoinChannelCount: int
        :param TotalPeerCount: 网络节点总数量
        :type TotalPeerCount: int
        :param MyPeerCount: 当前组织创建的节点数量
        :type MyPeerCount: int
        :param OrderCount: 其他组织创建的节点数量
        :type OrderCount: int
        :param TotalGroupCount: 网络组织总数量
        :type TotalGroupCount: int
        :param MyGroupCount: 当前组织创建的组织数量
        :type MyGroupCount: int
        :param TotalChaincodeCount: 网络智能合约总数量
        :type TotalChaincodeCount: int
        :param RecentChaincodeCount: 最近7天发起的智能合约数量
        :type RecentChaincodeCount: int
        :param MyChaincodeCount: 当前组织发起的智能合约数量
        :type MyChaincodeCount: int
        :param TotalCertCount: 当前组织的证书总数量
        :type TotalCertCount: int
        :param TlsCertCount: 颁发给当前组织的证书数量
        :type TlsCertCount: int
        :param PeerCertCount: 网络背书节点证书数量
        :type PeerCertCount: int
        :param ClientCertCount: 当前组织业务证书数量
        :type ClientCertCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalChannelCount = None
        self.MyChannelCount = None
        self.JoinChannelCount = None
        self.TotalPeerCount = None
        self.MyPeerCount = None
        self.OrderCount = None
        self.TotalGroupCount = None
        self.MyGroupCount = None
        self.TotalChaincodeCount = None
        self.RecentChaincodeCount = None
        self.MyChaincodeCount = None
        self.TotalCertCount = None
        self.TlsCertCount = None
        self.PeerCertCount = None
        self.ClientCertCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalChannelCount = params.get("TotalChannelCount")
        self.MyChannelCount = params.get("MyChannelCount")
        self.JoinChannelCount = params.get("JoinChannelCount")
        self.TotalPeerCount = params.get("TotalPeerCount")
        self.MyPeerCount = params.get("MyPeerCount")
        self.OrderCount = params.get("OrderCount")
        self.TotalGroupCount = params.get("TotalGroupCount")
        self.MyGroupCount = params.get("MyGroupCount")
        self.TotalChaincodeCount = params.get("TotalChaincodeCount")
        self.RecentChaincodeCount = params.get("RecentChaincodeCount")
        self.MyChaincodeCount = params.get("MyChaincodeCount")
        self.TotalCertCount = params.get("TotalCertCount")
        self.TlsCertCount = params.get("TlsCertCount")
        self.PeerCertCount = params.get("PeerCertCount")
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


class GetTransByHashHandlerRequest(AbstractModel):
    """GetTransByHashHandler请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：get_trans_by_hash
        :type Operation: str
        :param GroupPk: 群组编号
        :type GroupPk: str
        :param TransHash: 交易哈希
        :type TransHash: str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.TransHash = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.TransHash = params.get("TransHash")


class GetTransByHashHandlerResponse(AbstractModel):
    """GetTransByHashHandler返回参数结构体

    """

    def __init__(self):
        """
        :param TransactionJson: 交易信息json字符串
        :type TransactionJson: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TransactionJson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionJson = params.get("TransactionJson")
        self.RequestId = params.get("RequestId")


class GetTransListHandlerRequest(AbstractModel):
    """GetTransListHandler请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：get_trans_list
        :type Operation: str
        :param Offset: 记录偏移量
        :type Offset: int
        :param Limit: 每页记录数
        :type Limit: int
        :param GroupPk: 群组编号
        :type GroupPk: str
        :param TransHash: 交易哈希
        :type TransHash: str
        """
        self.Module = None
        self.Operation = None
        self.Offset = None
        self.Limit = None
        self.GroupPk = None
        self.TransHash = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupPk = params.get("GroupPk")
        self.TransHash = params.get("TransHash")


class GetTransListHandlerResponse(AbstractModel):
    """GetTransListHandler返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param GroupPk: 当前群组编号
        :type GroupPk: str
        :param List: 返回数据列表
        :type List: list of BcosTransInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GroupPk = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.GroupPk = params.get("GroupPk")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BcosTransInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class GetTransactionDetailForUserRequest(AbstractModel):
    """GetTransactionDetailForUser请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：transaction_detail_for_user
        :type Operation: str
        :param ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param GroupName: 参与交易的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param BlockId: 区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID
        :type BlockId: int
        :param TransactionId: 交易ID，需要查询的详情的交易ID
        :type TransactionId: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupName = None
        self.ChannelName = None
        self.BlockId = None
        self.TransactionId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        self.ChannelName = params.get("ChannelName")
        self.BlockId = params.get("BlockId")
        self.TransactionId = params.get("TransactionId")


class GetTransactionDetailForUserResponse(AbstractModel):
    """GetTransactionDetailForUser返回参数结构体

    """

    def __init__(self):
        """
        :param TransactionId: 交易ID
        :type TransactionId: str
        :param TransactionHash: 交易hash
        :type TransactionHash: str
        :param CreateOrgName: 创建交易的组织名
        :type CreateOrgName: str
        :param TransactionType: 交易类型（普通交易和配置交易）
        :type TransactionType: str
        :param TransactionStatus: 交易状态
        :type TransactionStatus: str
        :param CreateTime: 交易创建时间
        :type CreateTime: str
        :param TransactionData: 交易数据
        :type TransactionData: str
        :param BlockId: 交易所在区块号
        :type BlockId: int
        :param BlockHash: 交易所在区块哈希
        :type BlockHash: str
        :param BlockHeight: 交易所在区块高度
        :type BlockHeight: int
        :param ChannelName: 通道名称
        :type ChannelName: str
        :param ContractName: 交易所在合约名称
        :type ContractName: str
        :param EndorserOrgList: 背书组织列表
        :type EndorserOrgList: list of EndorserGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TransactionId = None
        self.TransactionHash = None
        self.CreateOrgName = None
        self.TransactionType = None
        self.TransactionStatus = None
        self.CreateTime = None
        self.TransactionData = None
        self.BlockId = None
        self.BlockHash = None
        self.BlockHeight = None
        self.ChannelName = None
        self.ContractName = None
        self.EndorserOrgList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.TransactionHash = params.get("TransactionHash")
        self.CreateOrgName = params.get("CreateOrgName")
        self.TransactionType = params.get("TransactionType")
        self.TransactionStatus = params.get("TransactionStatus")
        self.CreateTime = params.get("CreateTime")
        self.TransactionData = params.get("TransactionData")
        self.BlockId = params.get("BlockId")
        self.BlockHash = params.get("BlockHash")
        self.BlockHeight = params.get("BlockHeight")
        self.ChannelName = params.get("ChannelName")
        self.ContractName = params.get("ContractName")
        if params.get("EndorserOrgList") is not None:
            self.EndorserOrgList = []
            for item in params.get("EndorserOrgList"):
                obj = EndorserGroup()
                obj._deserialize(item)
                self.EndorserOrgList.append(obj)
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


class SendTransactionHandlerRequest(AbstractModel):
    """SendTransactionHandler请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：send_transaction
        :type Operation: str
        :param GroupPk: 群组编号
        :type GroupPk: str
        :param ContractId: 合约编号
        :type ContractId: int
        :param FuncName: 合约方法名
        :type FuncName: str
        :param FuncParam: 合约方法入参
        :type FuncParam: list of str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.ContractId = None
        self.FuncName = None
        self.FuncParam = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.ContractId = params.get("ContractId")
        self.FuncName = params.get("FuncName")
        self.FuncParam = params.get("FuncParam")


class SendTransactionHandlerResponse(AbstractModel):
    """SendTransactionHandler返回参数结构体

    """

    def __init__(self):
        """
        :param TransactionRsp: 交易结果json字符串
        :type TransactionRsp: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TransactionRsp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionRsp = params.get("TransactionRsp")
        self.RequestId = params.get("RequestId")


class SrvInvokeRequest(AbstractModel):
    """SrvInvoke请求参数结构体

    """

    def __init__(self):
        """
        :param Service: 服务类型，iss或者dam
        :type Service: str
        :param Method: 服务接口，要调用的方法函数名
        :type Method: str
        :param Param: 用户自定义json字符串
        :type Param: str
        """
        self.Service = None
        self.Method = None
        self.Param = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.Method = params.get("Method")
        self.Param = params.get("Param")


class SrvInvokeResponse(AbstractModel):
    """SrvInvoke返回参数结构体

    """

    def __init__(self):
        """
        :param RetCode: 返回码
        :type RetCode: int
        :param RetMsg: 返回消息
        :type RetMsg: str
        :param Data: 返回数据
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RetCode = None
        self.RetMsg = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")
        self.RetMsg = params.get("RetMsg")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TransByDynamicContractHandlerRequest(AbstractModel):
    """TransByDynamicContractHandler请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，固定字段：transaction
        :type Module: str
        :param Operation: 操作名，固定字段：trans_by_dynamic_contract
        :type Operation: str
        :param GroupPk: 群组编号
        :type GroupPk: str
        :param ContractAddress: 合约地址（合约部署成功，可得到合约地址）
        :type ContractAddress: str
        :param ContractName: 合约名
        :type ContractName: str
        :param AbiInfo: 合约编译后的abi
        :type AbiInfo: str
        :param FuncName: 合约被调用方法名
        :type FuncName: str
        :param FuncParam: 合约被调用方法的入参
        :type FuncParam: list of str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.ContractAddress = None
        self.ContractName = None
        self.AbiInfo = None
        self.FuncName = None
        self.FuncParam = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.ContractAddress = params.get("ContractAddress")
        self.ContractName = params.get("ContractName")
        self.AbiInfo = params.get("AbiInfo")
        self.FuncName = params.get("FuncName")
        self.FuncParam = params.get("FuncParam")


class TransByDynamicContractHandlerResponse(AbstractModel):
    """TransByDynamicContractHandler返回参数结构体

    """

    def __init__(self):
        """
        :param TransactionRsp: 交易结果json字符串
        :type TransactionRsp: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TransactionRsp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionRsp = params.get("TransactionRsp")
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