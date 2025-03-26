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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class ApplyChainMakerBatchUserCertRequest(AbstractModel):
    """ApplyChainMakerBatchUserCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _SignUserCsrList: 证书标识和证书请求文件，可参考TBaaS证书生成相关文档生成证书请求文件
        :type SignUserCsrList: list of SignCertCsr
        """
        self._ClusterId = None
        self._SignUserCsrList = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SignUserCsrList(self):
        """证书标识和证书请求文件，可参考TBaaS证书生成相关文档生成证书请求文件
        :rtype: list of SignCertCsr
        """
        return self._SignUserCsrList

    @SignUserCsrList.setter
    def SignUserCsrList(self, SignUserCsrList):
        self._SignUserCsrList = SignUserCsrList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("SignUserCsrList") is not None:
            self._SignUserCsrList = []
            for item in params.get("SignUserCsrList"):
                obj = SignCertCsr()
                obj._deserialize(item)
                self._SignUserCsrList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyChainMakerBatchUserCertResponse(AbstractModel):
    """ApplyChainMakerBatchUserCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignUserCrtList: 成功生成的用户证书的base64编码字符串列表，与SignUserCsrList一一对应
        :type SignUserCrtList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignUserCrtList = None
        self._RequestId = None

    @property
    def SignUserCrtList(self):
        """成功生成的用户证书的base64编码字符串列表，与SignUserCsrList一一对应
        :rtype: list of str
        """
        return self._SignUserCrtList

    @SignUserCrtList.setter
    def SignUserCrtList(self, SignUserCrtList):
        self._SignUserCrtList = SignUserCrtList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignUserCrtList = params.get("SignUserCrtList")
        self._RequestId = params.get("RequestId")


class ApplyUserCertRequest(AbstractModel):
    """ApplyUserCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定字段：cert_mng
        :type Module: str
        :param _Operation: 操作名，固定字段：cert_apply_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 申请证书的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _UserIdentity: 用户证书标识，用于标识用户证书，要求由纯小写字母组成，长度小于10
        :type UserIdentity: str
        :param _Applicant: 证书申请实体，使用腾讯云账号实名认证的名称
        :type Applicant: str
        :param _IdentityNum: 证件号码。如果腾讯云账号对应的实名认证类型为企业认证，填入“0”；如果腾讯云账号对应的实名认证类型为个人认证，填入个人身份证号码
        :type IdentityNum: str
        :param _CsrData: csr p10证书文件。需要用户根据文档生成证书的CSR文件
        :type CsrData: str
        :param _Notes: 证书备注信息
        :type Notes: str
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._UserIdentity = None
        self._Applicant = None
        self._IdentityNum = None
        self._CsrData = None
        self._Notes = None

    @property
    def Module(self):
        """模块名，固定字段：cert_mng
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名，固定字段：cert_apply_for_user
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        """申请证书的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def UserIdentity(self):
        """用户证书标识，用于标识用户证书，要求由纯小写字母组成，长度小于10
        :rtype: str
        """
        return self._UserIdentity

    @UserIdentity.setter
    def UserIdentity(self, UserIdentity):
        self._UserIdentity = UserIdentity

    @property
    def Applicant(self):
        """证书申请实体，使用腾讯云账号实名认证的名称
        :rtype: str
        """
        return self._Applicant

    @Applicant.setter
    def Applicant(self, Applicant):
        self._Applicant = Applicant

    @property
    def IdentityNum(self):
        """证件号码。如果腾讯云账号对应的实名认证类型为企业认证，填入“0”；如果腾讯云账号对应的实名认证类型为个人认证，填入个人身份证号码
        :rtype: str
        """
        return self._IdentityNum

    @IdentityNum.setter
    def IdentityNum(self, IdentityNum):
        self._IdentityNum = IdentityNum

    @property
    def CsrData(self):
        """csr p10证书文件。需要用户根据文档生成证书的CSR文件
        :rtype: str
        """
        return self._CsrData

    @CsrData.setter
    def CsrData(self, CsrData):
        self._CsrData = CsrData

    @property
    def Notes(self):
        """证书备注信息
        :rtype: str
        """
        return self._Notes

    @Notes.setter
    def Notes(self, Notes):
        self._Notes = Notes


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._UserIdentity = params.get("UserIdentity")
        self._Applicant = params.get("Applicant")
        self._IdentityNum = params.get("IdentityNum")
        self._CsrData = params.get("CsrData")
        self._Notes = params.get("Notes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyUserCertResponse(AbstractModel):
    """ApplyUserCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID
        :type CertId: int
        :param _CertDn: 证书DN
        :type CertDn: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertId = None
        self._CertDn = None
        self._RequestId = None

    @property
    def CertId(self):
        """证书ID
        :rtype: int
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertDn(self):
        """证书DN
        :rtype: str
        """
        return self._CertDn

    @CertDn.setter
    def CertDn(self, CertDn):
        self._CertDn = CertDn

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertDn = params.get("CertDn")
        self._RequestId = params.get("RequestId")


class Block(AbstractModel):
    """区块对象

    """

    def __init__(self):
        r"""
        :param _BlockNum: 区块编号
        :type BlockNum: int
        :param _DataHash: 区块数据Hash数值
        :type DataHash: str
        :param _BlockId: 区块ID，与区块编号一致
        :type BlockId: int
        :param _PreHash: 前一个区块Hash
        :type PreHash: str
        :param _TxCount: 区块内的交易数量
        :type TxCount: int
        """
        self._BlockNum = None
        self._DataHash = None
        self._BlockId = None
        self._PreHash = None
        self._TxCount = None

    @property
    def BlockNum(self):
        """区块编号
        :rtype: int
        """
        return self._BlockNum

    @BlockNum.setter
    def BlockNum(self, BlockNum):
        self._BlockNum = BlockNum

    @property
    def DataHash(self):
        """区块数据Hash数值
        :rtype: str
        """
        return self._DataHash

    @DataHash.setter
    def DataHash(self, DataHash):
        self._DataHash = DataHash

    @property
    def BlockId(self):
        """区块ID，与区块编号一致
        :rtype: int
        """
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def PreHash(self):
        """前一个区块Hash
        :rtype: str
        """
        return self._PreHash

    @PreHash.setter
    def PreHash(self, PreHash):
        self._PreHash = PreHash

    @property
    def TxCount(self):
        """区块内的交易数量
        :rtype: int
        """
        return self._TxCount

    @TxCount.setter
    def TxCount(self, TxCount):
        self._TxCount = TxCount


    def _deserialize(self, params):
        self._BlockNum = params.get("BlockNum")
        self._DataHash = params.get("DataHash")
        self._BlockId = params.get("BlockId")
        self._PreHash = params.get("PreHash")
        self._TxCount = params.get("TxCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChainMakerContractResult(AbstractModel):
    """长安链合约执行结果

    """

    def __init__(self):
        r"""
        :param _Code: 交易结果码
        :type Code: int
        :param _CodeMessage: 交易结果码含义
        :type CodeMessage: str
        :param _TxId: 交易ID
        :type TxId: str
        :param _GasUsed: Gas使用量
        :type GasUsed: int
        :param _Message: 合约返回消息
        :type Message: str
        :param _Result: 合约函数返回，base64编码
        :type Result: str
        """
        self._Code = None
        self._CodeMessage = None
        self._TxId = None
        self._GasUsed = None
        self._Message = None
        self._Result = None

    @property
    def Code(self):
        """交易结果码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeMessage(self):
        """交易结果码含义
        :rtype: str
        """
        return self._CodeMessage

    @CodeMessage.setter
    def CodeMessage(self, CodeMessage):
        self._CodeMessage = CodeMessage

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def GasUsed(self):
        """Gas使用量
        :rtype: int
        """
        return self._GasUsed

    @GasUsed.setter
    def GasUsed(self, GasUsed):
        self._GasUsed = GasUsed

    @property
    def Message(self):
        """合约返回消息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Result(self):
        """合约函数返回，base64编码
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._CodeMessage = params.get("CodeMessage")
        self._TxId = params.get("TxId")
        self._GasUsed = params.get("GasUsed")
        self._Message = params.get("Message")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChainMakerTransactionResult(AbstractModel):
    """长安链交易查询结果

    """

    def __init__(self):
        r"""
        :param _Code: 交易结果码
        :type Code: int
        :param _CodeMessage: 交易结果码含义
        :type CodeMessage: str
        :param _TxId: 交易ID
        :type TxId: str
        :param _GasUsed: Gas使用量
        :type GasUsed: int
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        :param _ContractEvent: 合约执行结果
        :type ContractEvent: str
        :param _Message: 合约返回信息
        :type Message: str
        :param _Timestamp: 交易时间，单位是秒
        :type Timestamp: int
        """
        self._Code = None
        self._CodeMessage = None
        self._TxId = None
        self._GasUsed = None
        self._BlockHeight = None
        self._ContractEvent = None
        self._Message = None
        self._Timestamp = None

    @property
    def Code(self):
        """交易结果码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeMessage(self):
        """交易结果码含义
        :rtype: str
        """
        return self._CodeMessage

    @CodeMessage.setter
    def CodeMessage(self, CodeMessage):
        self._CodeMessage = CodeMessage

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def GasUsed(self):
        """Gas使用量
        :rtype: int
        """
        return self._GasUsed

    @GasUsed.setter
    def GasUsed(self, GasUsed):
        self._GasUsed = GasUsed

    @property
    def BlockHeight(self):
        """区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def ContractEvent(self):
        """合约执行结果
        :rtype: str
        """
        return self._ContractEvent

    @ContractEvent.setter
    def ContractEvent(self, ContractEvent):
        self._ContractEvent = ContractEvent

    @property
    def Message(self):
        """合约返回信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Timestamp(self):
        """交易时间，单位是秒
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._CodeMessage = params.get("CodeMessage")
        self._TxId = params.get("TxId")
        self._GasUsed = params.get("GasUsed")
        self._BlockHeight = params.get("BlockHeight")
        self._ContractEvent = params.get("ContractEvent")
        self._Message = params.get("Message")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFabricBlockRequest(AbstractModel):
    """DescribeFabricBlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChannelId: 通道ID，可在通道列表或通道详情获取
        :type ChannelId: str
        :param _BlockHeight: 区块高度，从0开始
        :type BlockHeight: int
        """
        self._ClusterId = None
        self._ChannelId = None
        self._BlockHeight = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChannelId(self):
        """通道ID，可在通道列表或通道详情获取
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def BlockHeight(self):
        """区块高度，从0开始
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChannelId = params.get("ChannelId")
        self._BlockHeight = params.get("BlockHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFabricBlockResponse(AbstractModel):
    """DescribeFabricBlock返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        :param _BlockHash: 区块Hash
        :type BlockHash: str
        :param _PreBlockHash: 前置区块Hash
        :type PreBlockHash: str
        :param _TxCount: 区块中交易数量
        :type TxCount: int
        :param _TransactionList: 区块中交易列表
        :type TransactionList: list of Transaction
        :param _CreateTimestamp: 创建时间戳
        :type CreateTimestamp: str
        :param _ProposerOrg: 提案组织
        :type ProposerOrg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlockHeight = None
        self._BlockHash = None
        self._PreBlockHash = None
        self._TxCount = None
        self._TransactionList = None
        self._CreateTimestamp = None
        self._ProposerOrg = None
        self._RequestId = None

    @property
    def BlockHeight(self):
        """区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def BlockHash(self):
        """区块Hash
        :rtype: str
        """
        return self._BlockHash

    @BlockHash.setter
    def BlockHash(self, BlockHash):
        self._BlockHash = BlockHash

    @property
    def PreBlockHash(self):
        """前置区块Hash
        :rtype: str
        """
        return self._PreBlockHash

    @PreBlockHash.setter
    def PreBlockHash(self, PreBlockHash):
        self._PreBlockHash = PreBlockHash

    @property
    def TxCount(self):
        """区块中交易数量
        :rtype: int
        """
        return self._TxCount

    @TxCount.setter
    def TxCount(self, TxCount):
        self._TxCount = TxCount

    @property
    def TransactionList(self):
        """区块中交易列表
        :rtype: list of Transaction
        """
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def CreateTimestamp(self):
        """创建时间戳
        :rtype: str
        """
        return self._CreateTimestamp

    @CreateTimestamp.setter
    def CreateTimestamp(self, CreateTimestamp):
        self._CreateTimestamp = CreateTimestamp

    @property
    def ProposerOrg(self):
        """提案组织
        :rtype: str
        """
        return self._ProposerOrg

    @ProposerOrg.setter
    def ProposerOrg(self, ProposerOrg):
        self._ProposerOrg = ProposerOrg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlockHeight = params.get("BlockHeight")
        self._BlockHash = params.get("BlockHash")
        self._PreBlockHash = params.get("PreBlockHash")
        self._TxCount = params.get("TxCount")
        if params.get("TransactionList") is not None:
            self._TransactionList = []
            for item in params.get("TransactionList"):
                obj = Transaction()
                obj._deserialize(item)
                self._TransactionList.append(obj)
        self._CreateTimestamp = params.get("CreateTimestamp")
        self._ProposerOrg = params.get("ProposerOrg")
        self._RequestId = params.get("RequestId")


class DescribeFabricTransactionRequest(AbstractModel):
    """DescribeFabricTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChannelId: 通道ID，可在通道列表或通道详情获取
        :type ChannelId: str
        :param _TxId: 交易ID
        :type TxId: str
        """
        self._ClusterId = None
        self._ChannelId = None
        self._TxId = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChannelId(self):
        """通道ID，可在通道列表或通道详情获取
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChannelId = params.get("ChannelId")
        self._TxId = params.get("TxId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFabricTransactionResponse(AbstractModel):
    """DescribeFabricTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TxId: 交易ID
        :type TxId: str
        :param _TxHash: 交易Hash
        :type TxHash: str
        :param _TxStatus: 交易状态
        :type TxStatus: str
        :param _JoinOrgList: 参与的组织列表
        :type JoinOrgList: list of str
        :param _Sender: 交易发送者
        :type Sender: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        :param _ChaincodeName: 交易所属合约
        :type ChaincodeName: str
        :param _TransactionData: 交易数据，base64编码，解码后为json化的字符串
        :type TransactionData: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TxId = None
        self._TxHash = None
        self._TxStatus = None
        self._JoinOrgList = None
        self._Sender = None
        self._CreateTime = None
        self._BlockHeight = None
        self._ChaincodeName = None
        self._TransactionData = None
        self._RequestId = None

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def TxHash(self):
        """交易Hash
        :rtype: str
        """
        return self._TxHash

    @TxHash.setter
    def TxHash(self, TxHash):
        self._TxHash = TxHash

    @property
    def TxStatus(self):
        """交易状态
        :rtype: str
        """
        return self._TxStatus

    @TxStatus.setter
    def TxStatus(self, TxStatus):
        self._TxStatus = TxStatus

    @property
    def JoinOrgList(self):
        """参与的组织列表
        :rtype: list of str
        """
        return self._JoinOrgList

    @JoinOrgList.setter
    def JoinOrgList(self, JoinOrgList):
        self._JoinOrgList = JoinOrgList

    @property
    def Sender(self):
        """交易发送者
        :rtype: str
        """
        return self._Sender

    @Sender.setter
    def Sender(self, Sender):
        self._Sender = Sender

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BlockHeight(self):
        """区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def ChaincodeName(self):
        """交易所属合约
        :rtype: str
        """
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def TransactionData(self):
        """交易数据，base64编码，解码后为json化的字符串
        :rtype: str
        """
        return self._TransactionData

    @TransactionData.setter
    def TransactionData(self, TransactionData):
        self._TransactionData = TransactionData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TxId = params.get("TxId")
        self._TxHash = params.get("TxHash")
        self._TxStatus = params.get("TxStatus")
        self._JoinOrgList = params.get("JoinOrgList")
        self._Sender = params.get("Sender")
        self._CreateTime = params.get("CreateTime")
        self._BlockHeight = params.get("BlockHeight")
        self._ChaincodeName = params.get("ChaincodeName")
        self._TransactionData = params.get("TransactionData")
        self._RequestId = params.get("RequestId")


class DownloadUserCertRequest(AbstractModel):
    """DownloadUserCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定字段：cert_mng
        :type Module: str
        :param _Operation: 操作名，固定字段：cert_download_for_user
        :type Operation: str
        :param _CertId: 证书ID，可以在证书详情页面获取
        :type CertId: int
        :param _CertDn: 证书DN，可以在证书详情页面获取
        :type CertDn: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 下载证书的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        """
        self._Module = None
        self._Operation = None
        self._CertId = None
        self._CertDn = None
        self._ClusterId = None
        self._GroupName = None

    @property
    def Module(self):
        """模块名，固定字段：cert_mng
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名，固定字段：cert_download_for_user
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def CertId(self):
        """证书ID，可以在证书详情页面获取
        :rtype: int
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertDn(self):
        """证书DN，可以在证书详情页面获取
        :rtype: str
        """
        return self._CertDn

    @CertDn.setter
    def CertDn(self, CertDn):
        self._CertDn = CertDn

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        """下载证书的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._CertId = params.get("CertId")
        self._CertDn = params.get("CertDn")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadUserCertResponse(AbstractModel):
    """DownloadUserCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertName: 证书名称
        :type CertName: str
        :param _CertCtx: 证书内容
        :type CertCtx: str
        :param _Cert: 证书内容
        :type Cert: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertName = None
        self._CertCtx = None
        self._Cert = None
        self._RequestId = None

    @property
    def CertName(self):
        """证书名称
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertCtx(self):
        warnings.warn("parameter `CertCtx` is deprecated", DeprecationWarning) 

        """证书内容
        :rtype: str
        """
        return self._CertCtx

    @CertCtx.setter
    def CertCtx(self, CertCtx):
        warnings.warn("parameter `CertCtx` is deprecated", DeprecationWarning) 

        self._CertCtx = CertCtx

    @property
    def Cert(self):
        """证书内容
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertCtx = params.get("CertCtx")
        self._Cert = params.get("Cert")
        self._RequestId = params.get("RequestId")


class EndorserGroup(AbstractModel):
    """背书组织及其节点列表

    """

    def __init__(self):
        r"""
        :param _EndorserGroupName: 背书组织名称
        :type EndorserGroupName: str
        :param _EndorserPeerList: 背书节点列表
        :type EndorserPeerList: list of str
        """
        self._EndorserGroupName = None
        self._EndorserPeerList = None

    @property
    def EndorserGroupName(self):
        """背书组织名称
        :rtype: str
        """
        return self._EndorserGroupName

    @EndorserGroupName.setter
    def EndorserGroupName(self, EndorserGroupName):
        self._EndorserGroupName = EndorserGroupName

    @property
    def EndorserPeerList(self):
        """背书节点列表
        :rtype: list of str
        """
        return self._EndorserPeerList

    @EndorserPeerList.setter
    def EndorserPeerList(self, EndorserPeerList):
        self._EndorserPeerList = EndorserPeerList


    def _deserialize(self, params):
        self._EndorserGroupName = params.get("EndorserGroupName")
        self._EndorserPeerList = params.get("EndorserPeerList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBlockListRequest(AbstractModel):
    """GetBlockList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名称，固定字段：block
        :type Module: str
        :param _Operation: 操作名称，固定字段：block_list
        :type Operation: str
        :param _ChannelId: 通道ID，固定字段：0
        :type ChannelId: int
        :param _GroupId: 组织ID，固定字段：0
        :type GroupId: int
        :param _ChannelName: 需要查询的通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _GroupName: 调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _Offset: 需要获取的起始交易偏移
        :type Offset: int
        :param _Limit: 需要获取的交易数量
        :type Limit: int
        """
        self._Module = None
        self._Operation = None
        self._ChannelId = None
        self._GroupId = None
        self._ChannelName = None
        self._GroupName = None
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def Module(self):
        """模块名称，固定字段：block
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名称，固定字段：block_list
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ChannelId(self):
        """通道ID，固定字段：0
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def GroupId(self):
        """组织ID，固定字段：0
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ChannelName(self):
        """需要查询的通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def GroupName(self):
        """调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """需要获取的起始交易偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """需要获取的交易数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ChannelId = params.get("ChannelId")
        self._GroupId = params.get("GroupId")
        self._ChannelName = params.get("ChannelName")
        self._GroupName = params.get("GroupName")
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBlockListResponse(AbstractModel):
    """GetBlockList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 区块数量
        :type TotalCount: int
        :param _BlockList: 区块列表
        :type BlockList: list of Block
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlockList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """区块数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlockList(self):
        """区块列表
        :rtype: list of Block
        """
        return self._BlockList

    @BlockList.setter
    def BlockList(self, BlockList):
        self._BlockList = BlockList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BlockList") is not None:
            self._BlockList = []
            for item in params.get("BlockList"):
                obj = Block()
                obj._deserialize(item)
                self._BlockList.append(obj)
        self._RequestId = params.get("RequestId")


class GetBlockTransactionListForUserRequest(AbstractModel):
    """GetBlockTransactionListForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定字段：transaction
        :type Module: str
        :param _Operation: 操作名，固定字段：block_transaction_list_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 参与交易的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _BlockId: 区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID
        :type BlockId: int
        :param _Offset: 查询的交易列表起始偏移地址
        :type Offset: int
        :param _Limit: 查询的交易列表数量
        :type Limit: int
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._ChannelName = None
        self._BlockId = None
        self._Offset = None
        self._Limit = None

    @property
    def Module(self):
        """模块名，固定字段：transaction
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名，固定字段：block_transaction_list_for_user
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        """参与交易的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        """业务所属通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def BlockId(self):
        """区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID
        :rtype: int
        """
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def Offset(self):
        """查询的交易列表起始偏移地址
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询的交易列表数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._ChannelName = params.get("ChannelName")
        self._BlockId = params.get("BlockId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBlockTransactionListForUserResponse(AbstractModel):
    """GetBlockTransactionListForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 交易总数量
        :type TotalCount: int
        :param _TransactionList: 交易列表
        :type TransactionList: list of TransactionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TransactionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """交易总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TransactionList(self):
        """交易列表
        :rtype: list of TransactionItem
        """
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TransactionList") is not None:
            self._TransactionList = []
            for item in params.get("TransactionList"):
                obj = TransactionItem()
                obj._deserialize(item)
                self._TransactionList.append(obj)
        self._RequestId = params.get("RequestId")


class GetClusterSummaryRequest(AbstractModel):
    """GetClusterSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名称，固定字段：cluster_mng
        :type Module: str
        :param _Operation: 操作名称，固定字段：cluster_summary
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupId: 组织ID，固定字段：0
        :type GroupId: int
        :param _GroupName: 调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupId = None
        self._GroupName = None

    @property
    def Module(self):
        """模块名称，固定字段：cluster_mng
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名称，固定字段：cluster_summary
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        """组织ID，固定字段：0
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetClusterSummaryResponse(AbstractModel):
    """GetClusterSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalChannelCount: 网络通道总数量
        :type TotalChannelCount: int
        :param _MyChannelCount: 当前组织创建的通道数量
        :type MyChannelCount: int
        :param _JoinChannelCount: 当前组织加入的通道数量
        :type JoinChannelCount: int
        :param _TotalPeerCount: 网络节点总数量
        :type TotalPeerCount: int
        :param _MyPeerCount: 当前组织创建的节点数量
        :type MyPeerCount: int
        :param _OrderCount: 其他组织创建的节点数量
        :type OrderCount: int
        :param _TotalGroupCount: 网络组织总数量
        :type TotalGroupCount: int
        :param _MyGroupCount: 当前组织创建的组织数量
        :type MyGroupCount: int
        :param _TotalChaincodeCount: 网络智能合约总数量
        :type TotalChaincodeCount: int
        :param _RecentChaincodeCount: 最近7天发起的智能合约数量
        :type RecentChaincodeCount: int
        :param _MyChaincodeCount: 当前组织发起的智能合约数量
        :type MyChaincodeCount: int
        :param _TotalCertCount: 当前组织的证书总数量
        :type TotalCertCount: int
        :param _TlsCertCount: 颁发给当前组织的证书数量
        :type TlsCertCount: int
        :param _PeerCertCount: 网络背书节点证书数量
        :type PeerCertCount: int
        :param _ClientCertCount: 当前组织业务证书数量
        :type ClientCertCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalChannelCount = None
        self._MyChannelCount = None
        self._JoinChannelCount = None
        self._TotalPeerCount = None
        self._MyPeerCount = None
        self._OrderCount = None
        self._TotalGroupCount = None
        self._MyGroupCount = None
        self._TotalChaincodeCount = None
        self._RecentChaincodeCount = None
        self._MyChaincodeCount = None
        self._TotalCertCount = None
        self._TlsCertCount = None
        self._PeerCertCount = None
        self._ClientCertCount = None
        self._RequestId = None

    @property
    def TotalChannelCount(self):
        """网络通道总数量
        :rtype: int
        """
        return self._TotalChannelCount

    @TotalChannelCount.setter
    def TotalChannelCount(self, TotalChannelCount):
        self._TotalChannelCount = TotalChannelCount

    @property
    def MyChannelCount(self):
        """当前组织创建的通道数量
        :rtype: int
        """
        return self._MyChannelCount

    @MyChannelCount.setter
    def MyChannelCount(self, MyChannelCount):
        self._MyChannelCount = MyChannelCount

    @property
    def JoinChannelCount(self):
        """当前组织加入的通道数量
        :rtype: int
        """
        return self._JoinChannelCount

    @JoinChannelCount.setter
    def JoinChannelCount(self, JoinChannelCount):
        self._JoinChannelCount = JoinChannelCount

    @property
    def TotalPeerCount(self):
        """网络节点总数量
        :rtype: int
        """
        return self._TotalPeerCount

    @TotalPeerCount.setter
    def TotalPeerCount(self, TotalPeerCount):
        self._TotalPeerCount = TotalPeerCount

    @property
    def MyPeerCount(self):
        """当前组织创建的节点数量
        :rtype: int
        """
        return self._MyPeerCount

    @MyPeerCount.setter
    def MyPeerCount(self, MyPeerCount):
        self._MyPeerCount = MyPeerCount

    @property
    def OrderCount(self):
        """其他组织创建的节点数量
        :rtype: int
        """
        return self._OrderCount

    @OrderCount.setter
    def OrderCount(self, OrderCount):
        self._OrderCount = OrderCount

    @property
    def TotalGroupCount(self):
        """网络组织总数量
        :rtype: int
        """
        return self._TotalGroupCount

    @TotalGroupCount.setter
    def TotalGroupCount(self, TotalGroupCount):
        self._TotalGroupCount = TotalGroupCount

    @property
    def MyGroupCount(self):
        """当前组织创建的组织数量
        :rtype: int
        """
        return self._MyGroupCount

    @MyGroupCount.setter
    def MyGroupCount(self, MyGroupCount):
        self._MyGroupCount = MyGroupCount

    @property
    def TotalChaincodeCount(self):
        """网络智能合约总数量
        :rtype: int
        """
        return self._TotalChaincodeCount

    @TotalChaincodeCount.setter
    def TotalChaincodeCount(self, TotalChaincodeCount):
        self._TotalChaincodeCount = TotalChaincodeCount

    @property
    def RecentChaincodeCount(self):
        """最近7天发起的智能合约数量
        :rtype: int
        """
        return self._RecentChaincodeCount

    @RecentChaincodeCount.setter
    def RecentChaincodeCount(self, RecentChaincodeCount):
        self._RecentChaincodeCount = RecentChaincodeCount

    @property
    def MyChaincodeCount(self):
        """当前组织发起的智能合约数量
        :rtype: int
        """
        return self._MyChaincodeCount

    @MyChaincodeCount.setter
    def MyChaincodeCount(self, MyChaincodeCount):
        self._MyChaincodeCount = MyChaincodeCount

    @property
    def TotalCertCount(self):
        """当前组织的证书总数量
        :rtype: int
        """
        return self._TotalCertCount

    @TotalCertCount.setter
    def TotalCertCount(self, TotalCertCount):
        self._TotalCertCount = TotalCertCount

    @property
    def TlsCertCount(self):
        """颁发给当前组织的证书数量
        :rtype: int
        """
        return self._TlsCertCount

    @TlsCertCount.setter
    def TlsCertCount(self, TlsCertCount):
        self._TlsCertCount = TlsCertCount

    @property
    def PeerCertCount(self):
        """网络背书节点证书数量
        :rtype: int
        """
        return self._PeerCertCount

    @PeerCertCount.setter
    def PeerCertCount(self, PeerCertCount):
        self._PeerCertCount = PeerCertCount

    @property
    def ClientCertCount(self):
        """当前组织业务证书数量
        :rtype: int
        """
        return self._ClientCertCount

    @ClientCertCount.setter
    def ClientCertCount(self, ClientCertCount):
        self._ClientCertCount = ClientCertCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalChannelCount = params.get("TotalChannelCount")
        self._MyChannelCount = params.get("MyChannelCount")
        self._JoinChannelCount = params.get("JoinChannelCount")
        self._TotalPeerCount = params.get("TotalPeerCount")
        self._MyPeerCount = params.get("MyPeerCount")
        self._OrderCount = params.get("OrderCount")
        self._TotalGroupCount = params.get("TotalGroupCount")
        self._MyGroupCount = params.get("MyGroupCount")
        self._TotalChaincodeCount = params.get("TotalChaincodeCount")
        self._RecentChaincodeCount = params.get("RecentChaincodeCount")
        self._MyChaincodeCount = params.get("MyChaincodeCount")
        self._TotalCertCount = params.get("TotalCertCount")
        self._TlsCertCount = params.get("TlsCertCount")
        self._PeerCertCount = params.get("PeerCertCount")
        self._ClientCertCount = params.get("ClientCertCount")
        self._RequestId = params.get("RequestId")


class GetInvokeTxRequest(AbstractModel):
    """GetInvokeTx请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定字段：transaction
        :type Module: str
        :param _Operation: 操作名，固定字段：query_txid
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _PeerName: 执行该查询交易的节点名称，可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :type PeerName: str
        :param _PeerGroup: 执行该查询交易的节点所属组织名称，可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :type PeerGroup: str
        :param _TxId: 交易ID
        :type TxId: str
        :param _GroupName: 调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._ChannelName = None
        self._PeerName = None
        self._PeerGroup = None
        self._TxId = None
        self._GroupName = None

    @property
    def Module(self):
        """模块名，固定字段：transaction
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名，固定字段：query_txid
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChannelName(self):
        """业务所属通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def PeerName(self):
        """执行该查询交易的节点名称，可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :rtype: str
        """
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def PeerGroup(self):
        """执行该查询交易的节点所属组织名称，可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :rtype: str
        """
        return self._PeerGroup

    @PeerGroup.setter
    def PeerGroup(self, PeerGroup):
        self._PeerGroup = PeerGroup

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def GroupName(self):
        """调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._ChannelName = params.get("ChannelName")
        self._PeerName = params.get("PeerName")
        self._PeerGroup = params.get("PeerGroup")
        self._TxId = params.get("TxId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetInvokeTxResponse(AbstractModel):
    """GetInvokeTx返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TxValidationCode: 交易执行状态码
        :type TxValidationCode: int
        :param _TxValidationMsg: 交易执行消息
        :type TxValidationMsg: str
        :param _BlockId: 交易所在区块ID
        :type BlockId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TxValidationCode = None
        self._TxValidationMsg = None
        self._BlockId = None
        self._RequestId = None

    @property
    def TxValidationCode(self):
        """交易执行状态码
        :rtype: int
        """
        return self._TxValidationCode

    @TxValidationCode.setter
    def TxValidationCode(self, TxValidationCode):
        self._TxValidationCode = TxValidationCode

    @property
    def TxValidationMsg(self):
        """交易执行消息
        :rtype: str
        """
        return self._TxValidationMsg

    @TxValidationMsg.setter
    def TxValidationMsg(self, TxValidationMsg):
        self._TxValidationMsg = TxValidationMsg

    @property
    def BlockId(self):
        """交易所在区块ID
        :rtype: int
        """
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TxValidationCode = params.get("TxValidationCode")
        self._TxValidationMsg = params.get("TxValidationMsg")
        self._BlockId = params.get("BlockId")
        self._RequestId = params.get("RequestId")


class GetLatesdTransactionListRequest(AbstractModel):
    """GetLatesdTransactionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名称，固定字段：transaction
        :type Module: str
        :param _Operation: 操作名称，固定字段：latest_transaction_list
        :type Operation: str
        :param _GroupId: 组织ID，固定字段：0
        :type GroupId: int
        :param _ChannelId: 通道ID，固定字段：0
        :type ChannelId: int
        :param _LatestBlockNumber: 获取的最新交易的区块数量，取值范围1~5
        :type LatestBlockNumber: int
        :param _GroupName: 调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _ChannelName: 需要查询的通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _Offset: 需要获取的起始交易偏移
        :type Offset: int
        :param _Limit: 需要获取的交易数量
        :type Limit: int
        """
        self._Module = None
        self._Operation = None
        self._GroupId = None
        self._ChannelId = None
        self._LatestBlockNumber = None
        self._GroupName = None
        self._ChannelName = None
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def Module(self):
        """模块名称，固定字段：transaction
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名称，固定字段：latest_transaction_list
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def GroupId(self):
        """组织ID，固定字段：0
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ChannelId(self):
        """通道ID，固定字段：0
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def LatestBlockNumber(self):
        """获取的最新交易的区块数量，取值范围1~5
        :rtype: int
        """
        return self._LatestBlockNumber

    @LatestBlockNumber.setter
    def LatestBlockNumber(self, LatestBlockNumber):
        self._LatestBlockNumber = LatestBlockNumber

    @property
    def GroupName(self):
        """调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        """需要查询的通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """需要获取的起始交易偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """需要获取的交易数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._GroupId = params.get("GroupId")
        self._ChannelId = params.get("ChannelId")
        self._LatestBlockNumber = params.get("LatestBlockNumber")
        self._GroupName = params.get("GroupName")
        self._ChannelName = params.get("ChannelName")
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLatesdTransactionListResponse(AbstractModel):
    """GetLatesdTransactionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 交易总数量
        :type TotalCount: int
        :param _TransactionList: 交易列表
        :type TransactionList: list of TransactionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TransactionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """交易总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TransactionList(self):
        """交易列表
        :rtype: list of TransactionItem
        """
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TransactionList") is not None:
            self._TransactionList = []
            for item in params.get("TransactionList"):
                obj = TransactionItem()
                obj._deserialize(item)
                self._TransactionList.append(obj)
        self._RequestId = params.get("RequestId")


class GetLatestTransactionListRequest(AbstractModel):
    """GetLatestTransactionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名称，固定字段：transaction
        :type Module: str
        :param _Operation: 操作名称，固定字段：latest_transaction_list
        :type Operation: str
        :param _GroupId: 组织ID，固定字段：0
        :type GroupId: int
        :param _ChannelId: 通道ID，固定字段：0
        :type ChannelId: int
        :param _LatestBlockNumber: 获取的最新交易的区块数量，取值范围1~5
        :type LatestBlockNumber: int
        :param _GroupName: 调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _ChannelName: 需要查询的通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _Offset: 需要获取的起始交易偏移
        :type Offset: int
        :param _Limit: 需要获取的交易数量
        :type Limit: int
        """
        self._Module = None
        self._Operation = None
        self._GroupId = None
        self._ChannelId = None
        self._LatestBlockNumber = None
        self._GroupName = None
        self._ChannelName = None
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def Module(self):
        """模块名称，固定字段：transaction
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名称，固定字段：latest_transaction_list
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def GroupId(self):
        """组织ID，固定字段：0
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ChannelId(self):
        """通道ID，固定字段：0
        :rtype: int
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def LatestBlockNumber(self):
        """获取的最新交易的区块数量，取值范围1~5
        :rtype: int
        """
        return self._LatestBlockNumber

    @LatestBlockNumber.setter
    def LatestBlockNumber(self, LatestBlockNumber):
        self._LatestBlockNumber = LatestBlockNumber

    @property
    def GroupName(self):
        """调用接口的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        """需要查询的通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """需要获取的起始交易偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """需要获取的交易数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._GroupId = params.get("GroupId")
        self._ChannelId = params.get("ChannelId")
        self._LatestBlockNumber = params.get("LatestBlockNumber")
        self._GroupName = params.get("GroupName")
        self._ChannelName = params.get("ChannelName")
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLatestTransactionListResponse(AbstractModel):
    """GetLatestTransactionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 交易总数量
        :type TotalCount: int
        :param _TransactionList: 交易列表
        :type TransactionList: list of TransactionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TransactionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """交易总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TransactionList(self):
        """交易列表
        :rtype: list of TransactionItem
        """
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TransactionList") is not None:
            self._TransactionList = []
            for item in params.get("TransactionList"):
                obj = TransactionItem()
                obj._deserialize(item)
                self._TransactionList.append(obj)
        self._RequestId = params.get("RequestId")


class GetTransactionDetailForUserRequest(AbstractModel):
    """GetTransactionDetailForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定字段：transaction
        :type Module: str
        :param _Operation: 操作名，固定字段：transaction_detail_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 参与交易的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _BlockId: 区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID
        :type BlockId: int
        :param _TransactionId: 交易ID，需要查询的详情的交易ID
        :type TransactionId: str
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._ChannelName = None
        self._BlockId = None
        self._TransactionId = None

    @property
    def Module(self):
        """模块名，固定字段：transaction
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名，固定字段：transaction_detail_for_user
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        """参与交易的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        """业务所属通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def BlockId(self):
        """区块ID，通过GetInvokeTx接口可以获取交易所在的区块ID
        :rtype: int
        """
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def TransactionId(self):
        """交易ID，需要查询的详情的交易ID
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._ChannelName = params.get("ChannelName")
        self._BlockId = params.get("BlockId")
        self._TransactionId = params.get("TransactionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTransactionDetailForUserResponse(AbstractModel):
    """GetTransactionDetailForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TransactionId: 交易ID
        :type TransactionId: str
        :param _TransactionHash: 交易hash
        :type TransactionHash: str
        :param _CreateOrgName: 创建交易的组织名
        :type CreateOrgName: str
        :param _TransactionType: 交易类型（普通交易和配置交易）
        :type TransactionType: str
        :param _TransactionStatus: 交易状态
        :type TransactionStatus: str
        :param _CreateTime: 交易创建时间
        :type CreateTime: str
        :param _TransactionData: 交易数据
        :type TransactionData: str
        :param _BlockId: 交易所在区块号
        :type BlockId: int
        :param _BlockHash: 交易所在区块哈希
        :type BlockHash: str
        :param _BlockHeight: 交易所在区块高度
        :type BlockHeight: int
        :param _ChannelName: 通道名称
        :type ChannelName: str
        :param _ContractName: 交易所在合约名称
        :type ContractName: str
        :param _EndorserOrgList: 背书组织列表
        :type EndorserOrgList: list of EndorserGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TransactionId = None
        self._TransactionHash = None
        self._CreateOrgName = None
        self._TransactionType = None
        self._TransactionStatus = None
        self._CreateTime = None
        self._TransactionData = None
        self._BlockId = None
        self._BlockHash = None
        self._BlockHeight = None
        self._ChannelName = None
        self._ContractName = None
        self._EndorserOrgList = None
        self._RequestId = None

    @property
    def TransactionId(self):
        """交易ID
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionHash(self):
        """交易hash
        :rtype: str
        """
        return self._TransactionHash

    @TransactionHash.setter
    def TransactionHash(self, TransactionHash):
        self._TransactionHash = TransactionHash

    @property
    def CreateOrgName(self):
        """创建交易的组织名
        :rtype: str
        """
        return self._CreateOrgName

    @CreateOrgName.setter
    def CreateOrgName(self, CreateOrgName):
        self._CreateOrgName = CreateOrgName

    @property
    def TransactionType(self):
        """交易类型（普通交易和配置交易）
        :rtype: str
        """
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def TransactionStatus(self):
        """交易状态
        :rtype: str
        """
        return self._TransactionStatus

    @TransactionStatus.setter
    def TransactionStatus(self, TransactionStatus):
        self._TransactionStatus = TransactionStatus

    @property
    def CreateTime(self):
        """交易创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TransactionData(self):
        """交易数据
        :rtype: str
        """
        return self._TransactionData

    @TransactionData.setter
    def TransactionData(self, TransactionData):
        self._TransactionData = TransactionData

    @property
    def BlockId(self):
        """交易所在区块号
        :rtype: int
        """
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def BlockHash(self):
        """交易所在区块哈希
        :rtype: str
        """
        return self._BlockHash

    @BlockHash.setter
    def BlockHash(self, BlockHash):
        self._BlockHash = BlockHash

    @property
    def BlockHeight(self):
        """交易所在区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def ChannelName(self):
        """通道名称
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ContractName(self):
        """交易所在合约名称
        :rtype: str
        """
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def EndorserOrgList(self):
        """背书组织列表
        :rtype: list of EndorserGroup
        """
        return self._EndorserOrgList

    @EndorserOrgList.setter
    def EndorserOrgList(self, EndorserOrgList):
        self._EndorserOrgList = EndorserOrgList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TransactionId = params.get("TransactionId")
        self._TransactionHash = params.get("TransactionHash")
        self._CreateOrgName = params.get("CreateOrgName")
        self._TransactionType = params.get("TransactionType")
        self._TransactionStatus = params.get("TransactionStatus")
        self._CreateTime = params.get("CreateTime")
        self._TransactionData = params.get("TransactionData")
        self._BlockId = params.get("BlockId")
        self._BlockHash = params.get("BlockHash")
        self._BlockHeight = params.get("BlockHeight")
        self._ChannelName = params.get("ChannelName")
        self._ContractName = params.get("ContractName")
        if params.get("EndorserOrgList") is not None:
            self._EndorserOrgList = []
            for item in params.get("EndorserOrgList"):
                obj = EndorserGroup()
                obj._deserialize(item)
                self._EndorserOrgList.append(obj)
        self._RequestId = params.get("RequestId")


class InvokeChainMakerContractRequest(AbstractModel):
    """InvokeChainMakerContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _ContractName: 合约名称，可在合约管理中获取
        :type ContractName: str
        :param _FuncName: 合约方法名
        :type FuncName: str
        :param _FuncParam: 合约方法入参，json格式字符串，key/value都是string类型的map
        :type FuncParam: str
        :param _AsyncFlag: 是否异步执行，1为是，否则为0；如果异步执行，可使用返回值中的交易TxID查询执行结果
        :type AsyncFlag: int
        """
        self._ClusterId = None
        self._ChainId = None
        self._ContractName = None
        self._FuncName = None
        self._FuncParam = None
        self._AsyncFlag = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        """合约名称，可在合约管理中获取
        :rtype: str
        """
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        """合约方法名
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        """合约方法入参，json格式字符串，key/value都是string类型的map
        :rtype: str
        """
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam

    @property
    def AsyncFlag(self):
        """是否异步执行，1为是，否则为0；如果异步执行，可使用返回值中的交易TxID查询执行结果
        :rtype: int
        """
        return self._AsyncFlag

    @AsyncFlag.setter
    def AsyncFlag(self, AsyncFlag):
        self._AsyncFlag = AsyncFlag


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._ContractName = params.get("ContractName")
        self._FuncName = params.get("FuncName")
        self._FuncParam = params.get("FuncParam")
        self._AsyncFlag = params.get("AsyncFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeChainMakerContractResponse(AbstractModel):
    """InvokeChainMakerContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 交易结果
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """交易结果
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerContractResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InvokeChainMakerDemoContractRequest(AbstractModel):
    """InvokeChainMakerDemoContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _ContractName: 合约名称，可在合约管理中获取
        :type ContractName: str
        :param _FuncName: 合约方法名
        :type FuncName: str
        :param _FuncParam: 合约方法入参，json格式字符串，key/value都是string类型的map
        :type FuncParam: str
        :param _AsyncFlag: 是否异步执行，1为是，否则为0；如果异步执行，可使用返回值中的交易TxID查询执行结果
        :type AsyncFlag: int
        """
        self._ClusterId = None
        self._ChainId = None
        self._ContractName = None
        self._FuncName = None
        self._FuncParam = None
        self._AsyncFlag = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        """合约名称，可在合约管理中获取
        :rtype: str
        """
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        """合约方法名
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        """合约方法入参，json格式字符串，key/value都是string类型的map
        :rtype: str
        """
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam

    @property
    def AsyncFlag(self):
        """是否异步执行，1为是，否则为0；如果异步执行，可使用返回值中的交易TxID查询执行结果
        :rtype: int
        """
        return self._AsyncFlag

    @AsyncFlag.setter
    def AsyncFlag(self, AsyncFlag):
        self._AsyncFlag = AsyncFlag


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._ContractName = params.get("ContractName")
        self._FuncName = params.get("FuncName")
        self._FuncParam = params.get("FuncParam")
        self._AsyncFlag = params.get("AsyncFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeChainMakerDemoContractResponse(AbstractModel):
    """InvokeChainMakerDemoContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 交易结果
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """交易结果
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerContractResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InvokeFabricChaincodeRequest(AbstractModel):
    """InvokeFabricChaincode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情获取
        :type ClusterId: str
        :param _ChannelId: 通道ID，可在通道列表或通道详情获取
        :type ChannelId: str
        :param _ChaincodeName: 合约名称，可在合约列表或合约详情获取
        :type ChaincodeName: str
        :param _FuncName: 合约方法
        :type FuncName: str
        :param _FuncParam: 合约方法入参
        :type FuncParam: list of str
        :param _WithAsyncResult: 是否异步执行，如果异步执行，可使用返回值中的交易TxID查询执行结果
        :type WithAsyncResult: bool
        """
        self._ClusterId = None
        self._ChannelId = None
        self._ChaincodeName = None
        self._FuncName = None
        self._FuncParam = None
        self._WithAsyncResult = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChannelId(self):
        """通道ID，可在通道列表或通道详情获取
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChaincodeName(self):
        """合约名称，可在合约列表或合约详情获取
        :rtype: str
        """
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def FuncName(self):
        """合约方法
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        """合约方法入参
        :rtype: list of str
        """
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam

    @property
    def WithAsyncResult(self):
        """是否异步执行，如果异步执行，可使用返回值中的交易TxID查询执行结果
        :rtype: bool
        """
        return self._WithAsyncResult

    @WithAsyncResult.setter
    def WithAsyncResult(self, WithAsyncResult):
        self._WithAsyncResult = WithAsyncResult


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChannelId = params.get("ChannelId")
        self._ChaincodeName = params.get("ChaincodeName")
        self._FuncName = params.get("FuncName")
        self._FuncParam = params.get("FuncParam")
        self._WithAsyncResult = params.get("WithAsyncResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFabricChaincodeResponse(AbstractModel):
    """InvokeFabricChaincode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TxId: 交易ID
        :type TxId: str
        :param _TxStatus: 交易状态
        :type TxStatus: str
        :param _TxResult: 交易结果
        :type TxResult: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TxId = None
        self._TxStatus = None
        self._TxResult = None
        self._RequestId = None

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def TxStatus(self):
        """交易状态
        :rtype: str
        """
        return self._TxStatus

    @TxStatus.setter
    def TxStatus(self, TxStatus):
        self._TxStatus = TxStatus

    @property
    def TxResult(self):
        """交易结果
        :rtype: str
        """
        return self._TxResult

    @TxResult.setter
    def TxResult(self, TxResult):
        self._TxResult = TxResult

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TxId = params.get("TxId")
        self._TxStatus = params.get("TxStatus")
        self._TxResult = params.get("TxResult")
        self._RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定字段：transaction
        :type Module: str
        :param _Operation: 操作名，固定字段：invoke
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChaincodeName: 业务所属智能合约名称，可在智能合约详情或列表中获取
        :type ChaincodeName: str
        :param _ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _Peers: 对该笔交易进行背书的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :type Peers: list of PeerSet
        :param _FuncName: 该笔交易需要调用的智能合约中的函数名称
        :type FuncName: str
        :param _GroupName: 调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _Args: 被调用的函数参数列表，参数列表大小总和要求小于2M
        :type Args: list of str
        :param _AsyncFlag: 同步调用标识，可选参数，值为0或者不传表示使用同步方法调用，调用后会等待交易执行后再返回执行结果；值为1时表示使用异步方式调用Invoke，执行后会立即返回交易对应的Txid，后续需要通过GetInvokeTx这个API查询该交易的执行结果。（对于逻辑较为简单的交易，可以使用同步模式；对于逻辑较为复杂的交易，建议使用异步模式，否则容易导致API因等待时间过长，返回等待超时）
        :type AsyncFlag: int
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._ChaincodeName = None
        self._ChannelName = None
        self._Peers = None
        self._FuncName = None
        self._GroupName = None
        self._Args = None
        self._AsyncFlag = None

    @property
    def Module(self):
        """模块名，固定字段：transaction
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名，固定字段：invoke
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChaincodeName(self):
        """业务所属智能合约名称，可在智能合约详情或列表中获取
        :rtype: str
        """
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChannelName(self):
        """业务所属通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Peers(self):
        """对该笔交易进行背书的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :rtype: list of PeerSet
        """
        return self._Peers

    @Peers.setter
    def Peers(self, Peers):
        self._Peers = Peers

    @property
    def FuncName(self):
        """该笔交易需要调用的智能合约中的函数名称
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def GroupName(self):
        """调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Args(self):
        """被调用的函数参数列表，参数列表大小总和要求小于2M
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def AsyncFlag(self):
        """同步调用标识，可选参数，值为0或者不传表示使用同步方法调用，调用后会等待交易执行后再返回执行结果；值为1时表示使用异步方式调用Invoke，执行后会立即返回交易对应的Txid，后续需要通过GetInvokeTx这个API查询该交易的执行结果。（对于逻辑较为简单的交易，可以使用同步模式；对于逻辑较为复杂的交易，建议使用异步模式，否则容易导致API因等待时间过长，返回等待超时）
        :rtype: int
        """
        return self._AsyncFlag

    @AsyncFlag.setter
    def AsyncFlag(self, AsyncFlag):
        self._AsyncFlag = AsyncFlag


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._ChaincodeName = params.get("ChaincodeName")
        self._ChannelName = params.get("ChannelName")
        if params.get("Peers") is not None:
            self._Peers = []
            for item in params.get("Peers"):
                obj = PeerSet()
                obj._deserialize(item)
                self._Peers.append(obj)
        self._FuncName = params.get("FuncName")
        self._GroupName = params.get("GroupName")
        self._Args = params.get("Args")
        self._AsyncFlag = params.get("AsyncFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeResponse(AbstractModel):
    """Invoke返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Txid: 交易ID
        :type Txid: str
        :param _Events: 交易执行结果
        :type Events: str
        :param _TxId: 交易ID
        :type TxId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Txid = None
        self._Events = None
        self._TxId = None
        self._RequestId = None

    @property
    def Txid(self):
        warnings.warn("parameter `Txid` is deprecated", DeprecationWarning) 

        """交易ID
        :rtype: str
        """
        return self._Txid

    @Txid.setter
    def Txid(self, Txid):
        warnings.warn("parameter `Txid` is deprecated", DeprecationWarning) 

        self._Txid = Txid

    @property
    def Events(self):
        """交易执行结果
        :rtype: str
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Txid = params.get("Txid")
        self._Events = params.get("Events")
        self._TxId = params.get("TxId")
        self._RequestId = params.get("RequestId")


class PeerSet(AbstractModel):
    """PeerSet

    """

    def __init__(self):
        r"""
        :param _PeerName: 节点名称
        :type PeerName: str
        :param _OrgName: 组织名称
        :type OrgName: str
        """
        self._PeerName = None
        self._OrgName = None

    @property
    def PeerName(self):
        """节点名称
        :rtype: str
        """
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def OrgName(self):
        """组织名称
        :rtype: str
        """
        return self._OrgName

    @OrgName.setter
    def OrgName(self, OrgName):
        self._OrgName = OrgName


    def _deserialize(self, params):
        self._PeerName = params.get("PeerName")
        self._OrgName = params.get("OrgName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChainMakerBlockTransactionRequest(AbstractModel):
    """QueryChainMakerBlockTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        """
        self._ClusterId = None
        self._ChainId = None
        self._BlockHeight = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def BlockHeight(self):
        """区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._BlockHeight = params.get("BlockHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChainMakerBlockTransactionResponse(AbstractModel):
    """QueryChainMakerBlockTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 区块交易
        :type Result: list of ChainMakerTransactionResult
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        :param _TxCount: 交易数量
        :type TxCount: int
        :param _BlockTimestamp: 区块时间戳，单位是秒
        :type BlockTimestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._BlockHeight = None
        self._TxCount = None
        self._BlockTimestamp = None
        self._RequestId = None

    @property
    def Result(self):
        """区块交易
        :rtype: list of ChainMakerTransactionResult
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def BlockHeight(self):
        """区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def TxCount(self):
        """交易数量
        :rtype: int
        """
        return self._TxCount

    @TxCount.setter
    def TxCount(self, TxCount):
        self._TxCount = TxCount

    @property
    def BlockTimestamp(self):
        """区块时间戳，单位是秒
        :rtype: int
        """
        return self._BlockTimestamp

    @BlockTimestamp.setter
    def BlockTimestamp(self, BlockTimestamp):
        self._BlockTimestamp = BlockTimestamp

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ChainMakerTransactionResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._BlockHeight = params.get("BlockHeight")
        self._TxCount = params.get("TxCount")
        self._BlockTimestamp = params.get("BlockTimestamp")
        self._RequestId = params.get("RequestId")


class QueryChainMakerContractRequest(AbstractModel):
    """QueryChainMakerContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _ContractName: 合约名称，可在合约管理中获取
        :type ContractName: str
        :param _FuncName: 合约方法名
        :type FuncName: str
        :param _FuncParam: 合约方法入参，json格式字符串，key/value都是string类型的map
        :type FuncParam: str
        """
        self._ClusterId = None
        self._ChainId = None
        self._ContractName = None
        self._FuncName = None
        self._FuncParam = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        """合约名称，可在合约管理中获取
        :rtype: str
        """
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        """合约方法名
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        """合约方法入参，json格式字符串，key/value都是string类型的map
        :rtype: str
        """
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._ContractName = params.get("ContractName")
        self._FuncName = params.get("FuncName")
        self._FuncParam = params.get("FuncParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChainMakerContractResponse(AbstractModel):
    """QueryChainMakerContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 交易结果
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """交易结果
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerContractResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class QueryChainMakerDemoBlockTransactionRequest(AbstractModel):
    """QueryChainMakerDemoBlockTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        """
        self._ClusterId = None
        self._ChainId = None
        self._BlockHeight = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def BlockHeight(self):
        """区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._BlockHeight = params.get("BlockHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChainMakerDemoBlockTransactionResponse(AbstractModel):
    """QueryChainMakerDemoBlockTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 区块交易
        :type Result: list of ChainMakerTransactionResult
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        :param _TxCount: 交易数量
        :type TxCount: int
        :param _BlockTimestamp: 区块时间戳，单位是秒
        :type BlockTimestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._BlockHeight = None
        self._TxCount = None
        self._BlockTimestamp = None
        self._RequestId = None

    @property
    def Result(self):
        """区块交易
        :rtype: list of ChainMakerTransactionResult
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def BlockHeight(self):
        """区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def TxCount(self):
        """交易数量
        :rtype: int
        """
        return self._TxCount

    @TxCount.setter
    def TxCount(self, TxCount):
        self._TxCount = TxCount

    @property
    def BlockTimestamp(self):
        """区块时间戳，单位是秒
        :rtype: int
        """
        return self._BlockTimestamp

    @BlockTimestamp.setter
    def BlockTimestamp(self, BlockTimestamp):
        self._BlockTimestamp = BlockTimestamp

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ChainMakerTransactionResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._BlockHeight = params.get("BlockHeight")
        self._TxCount = params.get("TxCount")
        self._BlockTimestamp = params.get("BlockTimestamp")
        self._RequestId = params.get("RequestId")


class QueryChainMakerDemoContractRequest(AbstractModel):
    """QueryChainMakerDemoContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _ContractName: 合约名称，可在合约管理中获取
        :type ContractName: str
        :param _FuncName: 合约方法名
        :type FuncName: str
        :param _FuncParam: 合约方法入参，json格式字符串，key/value都是string类型的map
        :type FuncParam: str
        """
        self._ClusterId = None
        self._ChainId = None
        self._ContractName = None
        self._FuncName = None
        self._FuncParam = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        """合约名称，可在合约管理中获取
        :rtype: str
        """
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        """合约方法名
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        """合约方法入参，json格式字符串，key/value都是string类型的map
        :rtype: str
        """
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._ContractName = params.get("ContractName")
        self._FuncName = params.get("FuncName")
        self._FuncParam = params.get("FuncParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChainMakerDemoContractResponse(AbstractModel):
    """QueryChainMakerDemoContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 交易结果
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """交易结果
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerContractResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class QueryChainMakerDemoTransactionRequest(AbstractModel):
    """QueryChainMakerDemoTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _TxID: 交易ID，通过调用合约的返回值获取
        :type TxID: str
        """
        self._ClusterId = None
        self._ChainId = None
        self._TxID = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def TxID(self):
        """交易ID，通过调用合约的返回值获取
        :rtype: str
        """
        return self._TxID

    @TxID.setter
    def TxID(self, TxID):
        self._TxID = TxID


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._TxID = params.get("TxID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChainMakerDemoTransactionResponse(AbstractModel):
    """QueryChainMakerDemoTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 交易结果
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerTransactionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """交易结果
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerTransactionResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerTransactionResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class QueryChainMakerTransactionRequest(AbstractModel):
    """QueryChainMakerTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChainId: 业务链ID，可在网络概览页获取
        :type ChainId: str
        :param _TxID: 交易ID，通过调用合约的返回值获取
        :type TxID: str
        """
        self._ClusterId = None
        self._ChainId = None
        self._TxID = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        """业务链ID，可在网络概览页获取
        :rtype: str
        """
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def TxID(self):
        """交易ID，通过调用合约的返回值获取
        :rtype: str
        """
        return self._TxID

    @TxID.setter
    def TxID(self, TxID):
        self._TxID = TxID


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChainId = params.get("ChainId")
        self._TxID = params.get("TxID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChainMakerTransactionResponse(AbstractModel):
    """QueryChainMakerTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 交易结果
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerTransactionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """交易结果
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerTransactionResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerTransactionResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class QueryFabricChaincodeRequest(AbstractModel):
    """QueryFabricChaincode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID，可在区块链网络详情获取
        :type ClusterId: str
        :param _ChannelId: 通道ID，可在通道列表或通道详情获取
        :type ChannelId: str
        :param _ChaincodeName: 合约名称，可在合约列表或合约详情获取
        :type ChaincodeName: str
        :param _FuncName: 合约方法
        :type FuncName: str
        :param _FuncParam: 合约方法入参
        :type FuncParam: list of str
        """
        self._ClusterId = None
        self._ChannelId = None
        self._ChaincodeName = None
        self._FuncName = None
        self._FuncParam = None

    @property
    def ClusterId(self):
        """网络ID，可在区块链网络详情获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChannelId(self):
        """通道ID，可在通道列表或通道详情获取
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChaincodeName(self):
        """合约名称，可在合约列表或合约详情获取
        :rtype: str
        """
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def FuncName(self):
        """合约方法
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        """合约方法入参
        :rtype: list of str
        """
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ChannelId = params.get("ChannelId")
        self._ChaincodeName = params.get("ChaincodeName")
        self._FuncName = params.get("FuncName")
        self._FuncParam = params.get("FuncParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFabricChaincodeResponse(AbstractModel):
    """QueryFabricChaincode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TxId: 交易ID
        :type TxId: str
        :param _TxStatus: 交易状态
        :type TxStatus: str
        :param _TxResult: 交易结果
        :type TxResult: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TxId = None
        self._TxStatus = None
        self._TxResult = None
        self._RequestId = None

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def TxStatus(self):
        """交易状态
        :rtype: str
        """
        return self._TxStatus

    @TxStatus.setter
    def TxStatus(self, TxStatus):
        self._TxStatus = TxStatus

    @property
    def TxResult(self):
        """交易结果
        :rtype: str
        """
        return self._TxResult

    @TxResult.setter
    def TxResult(self, TxResult):
        self._TxResult = TxResult

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TxId = params.get("TxId")
        self._TxStatus = params.get("TxStatus")
        self._TxResult = params.get("TxResult")
        self._RequestId = params.get("RequestId")


class QueryRequest(AbstractModel):
    """Query请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，固定字段：transaction
        :type Module: str
        :param _Operation: 操作名，固定字段：query
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _ChaincodeName: 业务所属智能合约名称，可在智能合约详情或列表中获取
        :type ChaincodeName: str
        :param _ChannelName: 业务所属通道名称，可在通道详情或列表中获取
        :type ChannelName: str
        :param _Peers: 执行该查询交易的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :type Peers: list of PeerSet
        :param _FuncName: 该笔交易查询需要调用的智能合约中的函数名称
        :type FuncName: str
        :param _GroupName: 调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _Args: 被调用的函数参数列表
        :type Args: list of str
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._ChaincodeName = None
        self._ChannelName = None
        self._Peers = None
        self._FuncName = None
        self._GroupName = None
        self._Args = None

    @property
    def Module(self):
        """模块名，固定字段：transaction
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        """操作名，固定字段：query
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        """区块链网络ID，可在区块链网络详情或列表中获取
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChaincodeName(self):
        """业务所属智能合约名称，可在智能合约详情或列表中获取
        :rtype: str
        """
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChannelName(self):
        """业务所属通道名称，可在通道详情或列表中获取
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Peers(self):
        """执行该查询交易的节点列表（包括节点名称和节点所属组织名称，详见数据结构一节），可以在通道详情中获取该通道上的节点名称及其所属组织名称
        :rtype: list of PeerSet
        """
        return self._Peers

    @Peers.setter
    def Peers(self, Peers):
        self._Peers = Peers

    @property
    def FuncName(self):
        """该笔交易查询需要调用的智能合约中的函数名称
        :rtype: str
        """
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def GroupName(self):
        """调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Args(self):
        """被调用的函数参数列表
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._ChaincodeName = params.get("ChaincodeName")
        self._ChannelName = params.get("ChannelName")
        if params.get("Peers") is not None:
            self._Peers = []
            for item in params.get("Peers"):
                obj = PeerSet()
                obj._deserialize(item)
                self._Peers.append(obj)
        self._FuncName = params.get("FuncName")
        self._GroupName = params.get("GroupName")
        self._Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResponse(AbstractModel):
    """Query返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询结果数据
        :type Data: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """查询结果数据
        :rtype: list of str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class SignCertCsr(AbstractModel):
    """用于申请用户签名证书的结构体

    """

    def __init__(self):
        r"""
        :param _CertMark: 用户签名证书的标识，会存在于用户申请的证书中
        :type CertMark: str
        :param _SignCsrContent: 用户申请签名证书所需要的证书请求文件的base64编码
        :type SignCsrContent: str
        """
        self._CertMark = None
        self._SignCsrContent = None

    @property
    def CertMark(self):
        """用户签名证书的标识，会存在于用户申请的证书中
        :rtype: str
        """
        return self._CertMark

    @CertMark.setter
    def CertMark(self, CertMark):
        self._CertMark = CertMark

    @property
    def SignCsrContent(self):
        """用户申请签名证书所需要的证书请求文件的base64编码
        :rtype: str
        """
        return self._SignCsrContent

    @SignCsrContent.setter
    def SignCsrContent(self, SignCsrContent):
        self._SignCsrContent = SignCsrContent


    def _deserialize(self, params):
        self._CertMark = params.get("CertMark")
        self._SignCsrContent = params.get("SignCsrContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrvInvokeRequest(AbstractModel):
    """SrvInvoke请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 服务类型，iss或者dam
        :type Service: str
        :param _Method: 服务接口，要调用的方法函数名
        :type Method: str
        :param _Param: 用户自定义json字符串
        :type Param: str
        """
        self._Service = None
        self._Method = None
        self._Param = None

    @property
    def Service(self):
        """服务类型，iss或者dam
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Method(self):
        """服务接口，要调用的方法函数名
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Param(self):
        """用户自定义json字符串
        :rtype: str
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._Method = params.get("Method")
        self._Param = params.get("Param")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrvInvokeResponse(AbstractModel):
    """SrvInvoke返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RetCode: 返回码
        :type RetCode: int
        :param _RetMsg: 返回消息
        :type RetMsg: str
        :param _Data: 返回数据
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RetCode = None
        self._RetMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def RetCode(self):
        """返回码
        :rtype: int
        """
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def RetMsg(self):
        """返回消息
        :rtype: str
        """
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def Data(self):
        """返回数据
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RetCode = params.get("RetCode")
        self._RetMsg = params.get("RetMsg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class Transaction(AbstractModel):
    """交易显示概述信息

    """

    def __init__(self):
        r"""
        :param _TxId: 交易ID
        :type TxId: str
        :param _ChaincodeName: 合约名称
        :type ChaincodeName: str
        :param _Sender: 交易发送者
        :type Sender: str
        :param _CreateTime: 交易创建时间
        :type CreateTime: str
        :param _BlockHeight: 交易所在区块高度
        :type BlockHeight: int
        :param _TxIndex: 交易在区块中的序号
        :type TxIndex: int
        """
        self._TxId = None
        self._ChaincodeName = None
        self._Sender = None
        self._CreateTime = None
        self._BlockHeight = None
        self._TxIndex = None

    @property
    def TxId(self):
        """交易ID
        :rtype: str
        """
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def ChaincodeName(self):
        """合约名称
        :rtype: str
        """
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def Sender(self):
        """交易发送者
        :rtype: str
        """
        return self._Sender

    @Sender.setter
    def Sender(self, Sender):
        self._Sender = Sender

    @property
    def CreateTime(self):
        """交易创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BlockHeight(self):
        """交易所在区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def TxIndex(self):
        """交易在区块中的序号
        :rtype: int
        """
        return self._TxIndex

    @TxIndex.setter
    def TxIndex(self, TxIndex):
        self._TxIndex = TxIndex


    def _deserialize(self, params):
        self._TxId = params.get("TxId")
        self._ChaincodeName = params.get("ChaincodeName")
        self._Sender = params.get("Sender")
        self._CreateTime = params.get("CreateTime")
        self._BlockHeight = params.get("BlockHeight")
        self._TxIndex = params.get("TxIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionItem(AbstractModel):
    """交易列表项信息

    """

    def __init__(self):
        r"""
        :param _TransactionId: 交易ID
        :type TransactionId: str
        :param _TransactionHash: 交易hash
        :type TransactionHash: str
        :param _CreateOrgName: 创建交易的组织名
        :type CreateOrgName: str
        :param _BlockId: 交易所在区块号
        :type BlockId: int
        :param _TransactionType: 交易类型（普通交易和配置交易）
        :type TransactionType: str
        :param _CreateTime: 交易创建时间
        :type CreateTime: str
        :param _BlockHeight: 交易所在区块高度
        :type BlockHeight: int
        :param _TransactionStatus: 交易状态
        :type TransactionStatus: str
        """
        self._TransactionId = None
        self._TransactionHash = None
        self._CreateOrgName = None
        self._BlockId = None
        self._TransactionType = None
        self._CreateTime = None
        self._BlockHeight = None
        self._TransactionStatus = None

    @property
    def TransactionId(self):
        """交易ID
        :rtype: str
        """
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionHash(self):
        """交易hash
        :rtype: str
        """
        return self._TransactionHash

    @TransactionHash.setter
    def TransactionHash(self, TransactionHash):
        self._TransactionHash = TransactionHash

    @property
    def CreateOrgName(self):
        """创建交易的组织名
        :rtype: str
        """
        return self._CreateOrgName

    @CreateOrgName.setter
    def CreateOrgName(self, CreateOrgName):
        self._CreateOrgName = CreateOrgName

    @property
    def BlockId(self):
        """交易所在区块号
        :rtype: int
        """
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def TransactionType(self):
        """交易类型（普通交易和配置交易）
        :rtype: str
        """
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def CreateTime(self):
        """交易创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BlockHeight(self):
        """交易所在区块高度
        :rtype: int
        """
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def TransactionStatus(self):
        """交易状态
        :rtype: str
        """
        return self._TransactionStatus

    @TransactionStatus.setter
    def TransactionStatus(self, TransactionStatus):
        self._TransactionStatus = TransactionStatus


    def _deserialize(self, params):
        self._TransactionId = params.get("TransactionId")
        self._TransactionHash = params.get("TransactionHash")
        self._CreateOrgName = params.get("CreateOrgName")
        self._BlockId = params.get("BlockId")
        self._TransactionType = params.get("TransactionType")
        self._CreateTime = params.get("CreateTime")
        self._BlockHeight = params.get("BlockHeight")
        self._TransactionStatus = params.get("TransactionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        