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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SignUserCsrList(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type SignUserCrtList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignUserCrtList = None
        self._RequestId = None

    @property
    def SignUserCrtList(self):
        return self._SignUserCrtList

    @SignUserCrtList.setter
    def SignUserCrtList(self, SignUserCrtList):
        self._SignUserCrtList = SignUserCrtList

    @property
    def RequestId(self):
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def UserIdentity(self):
        return self._UserIdentity

    @UserIdentity.setter
    def UserIdentity(self, UserIdentity):
        self._UserIdentity = UserIdentity

    @property
    def Applicant(self):
        return self._Applicant

    @Applicant.setter
    def Applicant(self, Applicant):
        self._Applicant = Applicant

    @property
    def IdentityNum(self):
        return self._IdentityNum

    @IdentityNum.setter
    def IdentityNum(self, IdentityNum):
        self._IdentityNum = IdentityNum

    @property
    def CsrData(self):
        return self._CsrData

    @CsrData.setter
    def CsrData(self, CsrData):
        self._CsrData = CsrData

    @property
    def Notes(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertId = None
        self._CertDn = None
        self._RequestId = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertDn(self):
        return self._CertDn

    @CertDn.setter
    def CertDn(self, CertDn):
        self._CertDn = CertDn

    @property
    def RequestId(self):
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
        return self._BlockNum

    @BlockNum.setter
    def BlockNum(self, BlockNum):
        self._BlockNum = BlockNum

    @property
    def DataHash(self):
        return self._DataHash

    @DataHash.setter
    def DataHash(self, DataHash):
        self._DataHash = DataHash

    @property
    def BlockId(self):
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def PreHash(self):
        return self._PreHash

    @PreHash.setter
    def PreHash(self, PreHash):
        self._PreHash = PreHash

    @property
    def TxCount(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeMessage: str
        :param _TxId: 交易ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TxId: str
        :param _GasUsed: Gas使用量
注意：此字段可能返回 null，表示取不到有效值。
        :type GasUsed: int
        :param _Message: 合约返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Result: 合约函数返回，base64编码
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeMessage(self):
        return self._CodeMessage

    @CodeMessage.setter
    def CodeMessage(self, CodeMessage):
        self._CodeMessage = CodeMessage

    @property
    def TxId(self):
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def GasUsed(self):
        return self._GasUsed

    @GasUsed.setter
    def GasUsed(self, GasUsed):
        self._GasUsed = GasUsed

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Result(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeMessage: str
        :param _TxId: 交易ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TxId: str
        :param _GasUsed: Gas使用量
注意：此字段可能返回 null，表示取不到有效值。
        :type GasUsed: int
        :param _BlockHeight: 区块高度
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockHeight: int
        :param _ContractEvent: 合约执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractEvent: str
        :param _Message: 合约返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Timestamp: 交易时间，单位是秒
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeMessage(self):
        return self._CodeMessage

    @CodeMessage.setter
    def CodeMessage(self, CodeMessage):
        self._CodeMessage = CodeMessage

    @property
    def TxId(self):
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def GasUsed(self):
        return self._GasUsed

    @GasUsed.setter
    def GasUsed(self, GasUsed):
        self._GasUsed = GasUsed

    @property
    def BlockHeight(self):
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def ContractEvent(self):
        return self._ContractEvent

    @ContractEvent.setter
    def ContractEvent(self, ContractEvent):
        self._ContractEvent = ContractEvent

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Timestamp(self):
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
        


class ChannelDetailForUser(AbstractModel):
    """通道详情信息

    """

    def __init__(self):
        r"""
        :param _ChannelName: 通道名称
        :type ChannelName: str
        :param _PeerList: 当前组织加入通道的节点列表
        :type PeerList: list of PeerDetailForUser
        """
        self._ChannelName = None
        self._PeerList = None

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def PeerList(self):
        return self._PeerList

    @PeerList.setter
    def PeerList(self, PeerList):
        self._PeerList = PeerList


    def _deserialize(self, params):
        self._ChannelName = params.get("ChannelName")
        if params.get("PeerList") is not None:
            self._PeerList = []
            for item in params.get("PeerList"):
                obj = PeerDetailForUser()
                obj._deserialize(item)
                self._PeerList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterDetailForUser(AbstractModel):
    """网络详情信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID
        :type ClusterId: str
        :param _GroupList: 组织列表
        :type GroupList: list of GroupDetailForUser
        :param _ClusterName: 网络名称
        :type ClusterName: str
        """
        self._ClusterId = None
        self._GroupList = None
        self._ClusterName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = GroupDetailForUser()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChaincodeAndInstallForUserRequest(AbstractModel):
    """CreateChaincodeAndInstallForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：chaincode_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：chaincode_create_and_install_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 调用合约的组织名称，可以在组织管理列表中获取当前组织的名称
        :type GroupName: str
        :param _PeerName: 合约安装节点名称，可以在通道详情中获取该通道上的节点名称
        :type PeerName: str
        :param _ChaincodeName: 智能合约名称，格式说明：以小写字母开头，由2-12位数字或小写字母组成
        :type ChaincodeName: str
        :param _ChaincodeVersion: 智能合约版本，格式说明：由1-12位数字、小写字母、特殊符号(“.”)组成，如v1.0
        :type ChaincodeVersion: str
        :param _ChaincodeFileType: 智能合约代码文件类型，支持类型：
1. "go"：.go合约文件
2. "gozip"：go合约工程zip包，要求压缩目录为代码根目录
3. "javazip"：java合约工程zip包，要求压缩目录为代码根目录
4. "nodezip"：nodejs合约工程zip包，要求压缩目录为代码根目录
        :type ChaincodeFileType: str
        :param _Chaincode: 合约内容，合约文件或压缩包内容的base64编码，大小要求小于等于5M
        :type Chaincode: str
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._PeerName = None
        self._ChaincodeName = None
        self._ChaincodeVersion = None
        self._ChaincodeFileType = None
        self._Chaincode = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def PeerName(self):
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def ChaincodeName(self):
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChaincodeVersion(self):
        return self._ChaincodeVersion

    @ChaincodeVersion.setter
    def ChaincodeVersion(self, ChaincodeVersion):
        self._ChaincodeVersion = ChaincodeVersion

    @property
    def ChaincodeFileType(self):
        return self._ChaincodeFileType

    @ChaincodeFileType.setter
    def ChaincodeFileType(self, ChaincodeFileType):
        self._ChaincodeFileType = ChaincodeFileType

    @property
    def Chaincode(self):
        return self._Chaincode

    @Chaincode.setter
    def Chaincode(self, Chaincode):
        self._Chaincode = Chaincode


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._PeerName = params.get("PeerName")
        self._ChaincodeName = params.get("ChaincodeName")
        self._ChaincodeVersion = params.get("ChaincodeVersion")
        self._ChaincodeFileType = params.get("ChaincodeFileType")
        self._Chaincode = params.get("Chaincode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChaincodeAndInstallForUserResponse(AbstractModel):
    """CreateChaincodeAndInstallForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertDn(self):
        return self._CertDn

    @CertDn.setter
    def CertDn(self, CertDn):
        self._CertDn = CertDn

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertName = None
        self._CertCtx = None
        self._RequestId = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertCtx(self):
        return self._CertCtx

    @CertCtx.setter
    def CertCtx(self, CertCtx):
        self._CertCtx = CertCtx

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertCtx = params.get("CertCtx")
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
        return self._EndorserGroupName

    @EndorserGroupName.setter
    def EndorserGroupName(self, EndorserGroupName):
        self._EndorserGroupName = EndorserGroupName

    @property
    def EndorserPeerList(self):
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlockList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlockList(self):
        return self._BlockList

    @BlockList.setter
    def BlockList(self, BlockList):
        self._BlockList = BlockList

    @property
    def RequestId(self):
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def BlockId(self):
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TransactionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TransactionList(self):
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def RequestId(self):
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


class GetChaincodeCompileLogForUserRequest(AbstractModel):
    """GetChaincodeCompileLogForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：chaincode_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：chaincode_compile_log_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 调用合约的组织名称
        :type GroupName: str
        :param _ChaincodeName: 业务所属智能合约名称
        :type ChaincodeName: str
        :param _ChaincodeVersion: 业务所属智能合约版本
        :type ChaincodeVersion: str
        :param _PeerName: 合约安装节点名称，可以在通道详情中获取该通道上的节点名称
        :type PeerName: str
        :param _Limit: 返回数据项数，本接口默认取值：10
        :type Limit: int
        :param _Offset: 返回数据起始偏移，本接口默认取值：0
        :type Offset: int
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._ChaincodeName = None
        self._ChaincodeVersion = None
        self._PeerName = None
        self._Limit = None
        self._Offset = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChaincodeName(self):
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChaincodeVersion(self):
        return self._ChaincodeVersion

    @ChaincodeVersion.setter
    def ChaincodeVersion(self, ChaincodeVersion):
        self._ChaincodeVersion = ChaincodeVersion

    @property
    def PeerName(self):
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._ChaincodeName = params.get("ChaincodeName")
        self._ChaincodeVersion = params.get("ChaincodeVersion")
        self._PeerName = params.get("PeerName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetChaincodeCompileLogForUserResponse(AbstractModel):
    """GetChaincodeCompileLogForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 日志总行数，上限2000条日志
        :type TotalCount: int
        :param _CompileLogList: 日志列表
        :type CompileLogList: list of LogDetailForUser
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CompileLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CompileLogList(self):
        return self._CompileLogList

    @CompileLogList.setter
    def CompileLogList(self, CompileLogList):
        self._CompileLogList = CompileLogList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CompileLogList") is not None:
            self._CompileLogList = []
            for item in params.get("CompileLogList"):
                obj = LogDetailForUser()
                obj._deserialize(item)
                self._CompileLogList.append(obj)
        self._RequestId = params.get("RequestId")


class GetChaincodeInitializeResultForUserRequest(AbstractModel):
    """GetChaincodeInitializeResultForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：chaincode_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：chaincode_init_result_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 调用合约的组织名称
        :type GroupName: str
        :param _ChannelName: 业务所属通道名称
        :type ChannelName: str
        :param _ChaincodeName: 业务所属合约名称
        :type ChaincodeName: str
        :param _ChaincodeVersion: 业务所属智能合约版本
        :type ChaincodeVersion: str
        :param _TaskId: 实例化任务ID
        :type TaskId: int
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._ChannelName = None
        self._ChaincodeName = None
        self._ChaincodeVersion = None
        self._TaskId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChaincodeName(self):
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChaincodeVersion(self):
        return self._ChaincodeVersion

    @ChaincodeVersion.setter
    def ChaincodeVersion(self, ChaincodeVersion):
        self._ChaincodeVersion = ChaincodeVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._ChannelName = params.get("ChannelName")
        self._ChaincodeName = params.get("ChaincodeName")
        self._ChaincodeVersion = params.get("ChaincodeVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetChaincodeInitializeResultForUserResponse(AbstractModel):
    """GetChaincodeInitializeResultForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InitResult: 实例化结果：0，实例化中；1，实例化成功；2，实例化失败
        :type InitResult: int
        :param _InitMessage: 实例化信息
        :type InitMessage: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InitResult = None
        self._InitMessage = None
        self._RequestId = None

    @property
    def InitResult(self):
        return self._InitResult

    @InitResult.setter
    def InitResult(self, InitResult):
        self._InitResult = InitResult

    @property
    def InitMessage(self):
        return self._InitMessage

    @InitMessage.setter
    def InitMessage(self, InitMessage):
        self._InitMessage = InitMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InitResult = params.get("InitResult")
        self._InitMessage = params.get("InitMessage")
        self._RequestId = params.get("RequestId")


class GetChaincodeLogForUserRequest(AbstractModel):
    """GetChaincodeLogForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：chaincode_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：chaincode_log_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 调用合约的组织名称
        :type GroupName: str
        :param _ChaincodeName: 业务所属智能合约名称
        :type ChaincodeName: str
        :param _ChaincodeVersion: 业务所属智能合约版本
        :type ChaincodeVersion: str
        :param _PeerName: 合约安装节点名称，可以在通道详情中获取该通道上的节点名称
        :type PeerName: str
        :param _BeginTime: 日志开始时间，如"2020-11-24 19:49:25"
        :type BeginTime: str
        :param _RowNum: 返回日志行数的最大值，系统设定该参数最大为1000，且一行日志的最大字节数是500，即最大返回50万个字节数的日志数据
        :type RowNum: int
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._ChaincodeName = None
        self._ChaincodeVersion = None
        self._PeerName = None
        self._BeginTime = None
        self._RowNum = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChaincodeName(self):
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChaincodeVersion(self):
        return self._ChaincodeVersion

    @ChaincodeVersion.setter
    def ChaincodeVersion(self, ChaincodeVersion):
        self._ChaincodeVersion = ChaincodeVersion

    @property
    def PeerName(self):
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def RowNum(self):
        return self._RowNum

    @RowNum.setter
    def RowNum(self, RowNum):
        self._RowNum = RowNum


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._ChaincodeName = params.get("ChaincodeName")
        self._ChaincodeVersion = params.get("ChaincodeVersion")
        self._PeerName = params.get("PeerName")
        self._BeginTime = params.get("BeginTime")
        self._RowNum = params.get("RowNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetChaincodeLogForUserResponse(AbstractModel):
    """GetChaincodeLogForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回日志总行数，不会超过入参的RowNum
        :type TotalCount: int
        :param _ChaincodeLogList: 日志列表
        :type ChaincodeLogList: list of LogDetailForUser
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ChaincodeLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ChaincodeLogList(self):
        return self._ChaincodeLogList

    @ChaincodeLogList.setter
    def ChaincodeLogList(self, ChaincodeLogList):
        self._ChaincodeLogList = ChaincodeLogList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ChaincodeLogList") is not None:
            self._ChaincodeLogList = []
            for item in params.get("ChaincodeLogList"):
                obj = LogDetailForUser()
                obj._deserialize(item)
                self._ChaincodeLogList.append(obj)
        self._RequestId = params.get("RequestId")


class GetChannelListForUserRequest(AbstractModel):
    """GetChannelListForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：channel_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：channel_list_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 组织名称
        :type GroupName: str
        :param _Limit: 返回数据项数，本接口默认取值：10，上限取值：20
        :type Limit: int
        :param _Offset: 返回数据起始偏移，本接口默认取值：0
        :type Offset: int
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._Limit = None
        self._Offset = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetChannelListForUserResponse(AbstractModel):
    """GetChannelListForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 通道总数量
        :type TotalCount: int
        :param _ChannelList: 通道列表
        :type ChannelList: list of ChannelDetailForUser
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ChannelList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ChannelList(self):
        return self._ChannelList

    @ChannelList.setter
    def ChannelList(self, ChannelList):
        self._ChannelList = ChannelList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ChannelList") is not None:
            self._ChannelList = []
            for item in params.get("ChannelList"):
                obj = ChannelDetailForUser()
                obj._deserialize(item)
                self._ChannelList.append(obj)
        self._RequestId = params.get("RequestId")


class GetClusterListForUserRequest(AbstractModel):
    """GetClusterListForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：cluster_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：cluster_list_for_user
        :type Operation: str
        :param _Limit: 返回数据项数，本接口默认取值：10，上限取值：20
        :type Limit: int
        :param _Offset: 返回数据起始偏移，本接口默认取值：0
        :type Offset: int
        """
        self._Module = None
        self._Operation = None
        self._Limit = None
        self._Offset = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetClusterListForUserResponse(AbstractModel):
    """GetClusterListForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 网络总数量
        :type TotalCount: int
        :param _ClusterList: 网络列表
        :type ClusterList: list of ClusterDetailForUser
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterList(self):
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterDetailForUser()
                obj._deserialize(item)
                self._ClusterList.append(obj)
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._TotalChannelCount

    @TotalChannelCount.setter
    def TotalChannelCount(self, TotalChannelCount):
        self._TotalChannelCount = TotalChannelCount

    @property
    def MyChannelCount(self):
        return self._MyChannelCount

    @MyChannelCount.setter
    def MyChannelCount(self, MyChannelCount):
        self._MyChannelCount = MyChannelCount

    @property
    def JoinChannelCount(self):
        return self._JoinChannelCount

    @JoinChannelCount.setter
    def JoinChannelCount(self, JoinChannelCount):
        self._JoinChannelCount = JoinChannelCount

    @property
    def TotalPeerCount(self):
        return self._TotalPeerCount

    @TotalPeerCount.setter
    def TotalPeerCount(self, TotalPeerCount):
        self._TotalPeerCount = TotalPeerCount

    @property
    def MyPeerCount(self):
        return self._MyPeerCount

    @MyPeerCount.setter
    def MyPeerCount(self, MyPeerCount):
        self._MyPeerCount = MyPeerCount

    @property
    def OrderCount(self):
        return self._OrderCount

    @OrderCount.setter
    def OrderCount(self, OrderCount):
        self._OrderCount = OrderCount

    @property
    def TotalGroupCount(self):
        return self._TotalGroupCount

    @TotalGroupCount.setter
    def TotalGroupCount(self, TotalGroupCount):
        self._TotalGroupCount = TotalGroupCount

    @property
    def MyGroupCount(self):
        return self._MyGroupCount

    @MyGroupCount.setter
    def MyGroupCount(self, MyGroupCount):
        self._MyGroupCount = MyGroupCount

    @property
    def TotalChaincodeCount(self):
        return self._TotalChaincodeCount

    @TotalChaincodeCount.setter
    def TotalChaincodeCount(self, TotalChaincodeCount):
        self._TotalChaincodeCount = TotalChaincodeCount

    @property
    def RecentChaincodeCount(self):
        return self._RecentChaincodeCount

    @RecentChaincodeCount.setter
    def RecentChaincodeCount(self, RecentChaincodeCount):
        self._RecentChaincodeCount = RecentChaincodeCount

    @property
    def MyChaincodeCount(self):
        return self._MyChaincodeCount

    @MyChaincodeCount.setter
    def MyChaincodeCount(self, MyChaincodeCount):
        self._MyChaincodeCount = MyChaincodeCount

    @property
    def TotalCertCount(self):
        return self._TotalCertCount

    @TotalCertCount.setter
    def TotalCertCount(self, TotalCertCount):
        self._TotalCertCount = TotalCertCount

    @property
    def TlsCertCount(self):
        return self._TlsCertCount

    @TlsCertCount.setter
    def TlsCertCount(self, TlsCertCount):
        self._TlsCertCount = TlsCertCount

    @property
    def PeerCertCount(self):
        return self._PeerCertCount

    @PeerCertCount.setter
    def PeerCertCount(self, PeerCertCount):
        self._PeerCertCount = PeerCertCount

    @property
    def ClientCertCount(self):
        return self._ClientCertCount

    @ClientCertCount.setter
    def ClientCertCount(self, ClientCertCount):
        self._ClientCertCount = ClientCertCount

    @property
    def RequestId(self):
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def PeerName(self):
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def PeerGroup(self):
        return self._PeerGroup

    @PeerGroup.setter
    def PeerGroup(self, PeerGroup):
        self._PeerGroup = PeerGroup

    @property
    def TxId(self):
        return self._TxId

    @TxId.setter
    def TxId(self, TxId):
        self._TxId = TxId

    @property
    def GroupName(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TxValidationCode = None
        self._TxValidationMsg = None
        self._BlockId = None
        self._RequestId = None

    @property
    def TxValidationCode(self):
        return self._TxValidationCode

    @TxValidationCode.setter
    def TxValidationCode(self, TxValidationCode):
        self._TxValidationCode = TxValidationCode

    @property
    def TxValidationMsg(self):
        return self._TxValidationMsg

    @TxValidationMsg.setter
    def TxValidationMsg(self, TxValidationMsg):
        self._TxValidationMsg = TxValidationMsg

    @property
    def BlockId(self):
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def RequestId(self):
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def LatestBlockNumber(self):
        return self._LatestBlockNumber

    @LatestBlockNumber.setter
    def LatestBlockNumber(self, LatestBlockNumber):
        self._LatestBlockNumber = LatestBlockNumber

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TransactionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TransactionList(self):
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def RequestId(self):
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def LatestBlockNumber(self):
        return self._LatestBlockNumber

    @LatestBlockNumber.setter
    def LatestBlockNumber(self, LatestBlockNumber):
        self._LatestBlockNumber = LatestBlockNumber

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TransactionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TransactionList(self):
        return self._TransactionList

    @TransactionList.setter
    def TransactionList(self, TransactionList):
        self._TransactionList = TransactionList

    @property
    def RequestId(self):
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


class GetPeerLogForUserRequest(AbstractModel):
    """GetPeerLogForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：peer_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：peer_log_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 调用合约的组织名称
        :type GroupName: str
        :param _PeerName: 节点名称
        :type PeerName: str
        :param _BeginTime: 日志开始时间，如"2020-11-24 19:49:25"
        :type BeginTime: str
        :param _RowNum: 返回日志行数的最大值，系统设定该参数最大为1000，且一行日志的最大字节数是500，即最大返回50万个字节数的日志数据
        :type RowNum: int
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._PeerName = None
        self._BeginTime = None
        self._RowNum = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def PeerName(self):
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def RowNum(self):
        return self._RowNum

    @RowNum.setter
    def RowNum(self, RowNum):
        self._RowNum = RowNum


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._PeerName = params.get("PeerName")
        self._BeginTime = params.get("BeginTime")
        self._RowNum = params.get("RowNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPeerLogForUserResponse(AbstractModel):
    """GetPeerLogForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回日志总行数，不会超过入参的RowNum
        :type TotalCount: int
        :param _PeerLogList: 日志列表
        :type PeerLogList: list of LogDetailForUser
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PeerLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PeerLogList(self):
        return self._PeerLogList

    @PeerLogList.setter
    def PeerLogList(self, PeerLogList):
        self._PeerLogList = PeerLogList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PeerLogList") is not None:
            self._PeerLogList = []
            for item in params.get("PeerLogList"):
                obj = LogDetailForUser()
                obj._deserialize(item)
                self._PeerLogList.append(obj)
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def BlockId(self):
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def TransactionId(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionHash(self):
        return self._TransactionHash

    @TransactionHash.setter
    def TransactionHash(self, TransactionHash):
        self._TransactionHash = TransactionHash

    @property
    def CreateOrgName(self):
        return self._CreateOrgName

    @CreateOrgName.setter
    def CreateOrgName(self, CreateOrgName):
        self._CreateOrgName = CreateOrgName

    @property
    def TransactionType(self):
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def TransactionStatus(self):
        return self._TransactionStatus

    @TransactionStatus.setter
    def TransactionStatus(self, TransactionStatus):
        self._TransactionStatus = TransactionStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TransactionData(self):
        return self._TransactionData

    @TransactionData.setter
    def TransactionData(self, TransactionData):
        self._TransactionData = TransactionData

    @property
    def BlockId(self):
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def BlockHash(self):
        return self._BlockHash

    @BlockHash.setter
    def BlockHash(self, BlockHash):
        self._BlockHash = BlockHash

    @property
    def BlockHeight(self):
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ContractName(self):
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def EndorserOrgList(self):
        return self._EndorserOrgList

    @EndorserOrgList.setter
    def EndorserOrgList(self, EndorserOrgList):
        self._EndorserOrgList = EndorserOrgList

    @property
    def RequestId(self):
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


class GroupDetailForUser(AbstractModel):
    """组织详情信息

    """

    def __init__(self):
        r"""
        :param _GroupName: 组织名称
        :type GroupName: str
        :param _GroupMSPId: 组织MSP Identity
        :type GroupMSPId: str
        """
        self._GroupName = None
        self._GroupMSPId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupMSPId(self):
        return self._GroupMSPId

    @GroupMSPId.setter
    def GroupMSPId(self, GroupMSPId):
        self._GroupMSPId = GroupMSPId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupMSPId = params.get("GroupMSPId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeChaincodeForUserRequest(AbstractModel):
    """InitializeChaincodeForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：chaincode_mng
        :type Module: str
        :param _Operation: 操作名，本接口取值：chaincode_init_for_user
        :type Operation: str
        :param _ClusterId: 区块链网络ID，可在区块链网络详情或列表中获取
        :type ClusterId: str
        :param _GroupName: 调用合约的组织名称
        :type GroupName: str
        :param _ChaincodeName: 业务所属智能合约名称
        :type ChaincodeName: str
        :param _ChaincodeVersion: 业务所属智能合约版本
        :type ChaincodeVersion: str
        :param _ChannelName: 业务所属通道名称
        :type ChannelName: str
        :param _PeerName: 合约实例化节点名称，可以在通道详情中获取该通道上的节点名称
        :type PeerName: str
        :param _Args: 实例化的函数参数列表
        :type Args: list of str
        """
        self._Module = None
        self._Operation = None
        self._ClusterId = None
        self._GroupName = None
        self._ChaincodeName = None
        self._ChaincodeVersion = None
        self._ChannelName = None
        self._PeerName = None
        self._Args = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ChaincodeName(self):
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChaincodeVersion(self):
        return self._ChaincodeVersion

    @ChaincodeVersion.setter
    def ChaincodeVersion(self, ChaincodeVersion):
        self._ChaincodeVersion = ChaincodeVersion

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def PeerName(self):
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        self._ChaincodeName = params.get("ChaincodeName")
        self._ChaincodeVersion = params.get("ChaincodeVersion")
        self._ChannelName = params.get("ChannelName")
        self._PeerName = params.get("PeerName")
        self._Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitializeChaincodeForUserResponse(AbstractModel):
    """InitializeChaincodeForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 实例化任务ID，用于查询实例化结果
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam

    @property
    def AsyncFlag(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
        return self._FuncParam

    @FuncParam.setter
    def FuncParam(self, FuncParam):
        self._FuncParam = FuncParam

    @property
    def AsyncFlag(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerContractResult()
            self._Result._deserialize(params.get("Result"))
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChaincodeName(self):
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Peers(self):
        return self._Peers

    @Peers.setter
    def Peers(self, Peers):
        self._Peers = Peers

    @property
    def FuncName(self):
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def AsyncFlag(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Txid = None
        self._Events = None
        self._RequestId = None

    @property
    def Txid(self):
        return self._Txid

    @Txid.setter
    def Txid(self, Txid):
        self._Txid = Txid

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Txid = params.get("Txid")
        self._Events = params.get("Events")
        self._RequestId = params.get("RequestId")


class LogDetailForUser(AbstractModel):
    """日志详情信息

    """

    def __init__(self):
        r"""
        :param _LineNumber: 日志行号
        :type LineNumber: int
        :param _LogMessage: 日志详情
        :type LogMessage: str
        """
        self._LineNumber = None
        self._LogMessage = None

    @property
    def LineNumber(self):
        return self._LineNumber

    @LineNumber.setter
    def LineNumber(self, LineNumber):
        self._LineNumber = LineNumber

    @property
    def LogMessage(self):
        return self._LogMessage

    @LogMessage.setter
    def LogMessage(self, LogMessage):
        self._LogMessage = LogMessage


    def _deserialize(self, params):
        self._LineNumber = params.get("LineNumber")
        self._LogMessage = params.get("LogMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeerDetailForUser(AbstractModel):
    """节点详情信息

    """

    def __init__(self):
        r"""
        :param _PeerName: 节点名称
        :type PeerName: str
        """
        self._PeerName = None

    @property
    def PeerName(self):
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName


    def _deserialize(self, params):
        self._PeerName = params.get("PeerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        return self._PeerName

    @PeerName.setter
    def PeerName(self, PeerName):
        self._PeerName = PeerName

    @property
    def OrgName(self):
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def BlockHeight(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of ChainMakerTransactionResult
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        :param _TxCount: 交易数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TxCount: int
        :param _BlockTimestamp: 区块时间戳，单位是秒
        :type BlockTimestamp: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._BlockHeight = None
        self._TxCount = None
        self._BlockTimestamp = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def BlockHeight(self):
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def TxCount(self):
        return self._TxCount

    @TxCount.setter
    def TxCount(self, TxCount):
        self._TxCount = TxCount

    @property
    def BlockTimestamp(self):
        return self._BlockTimestamp

    @BlockTimestamp.setter
    def BlockTimestamp(self, BlockTimestamp):
        self._BlockTimestamp = BlockTimestamp

    @property
    def RequestId(self):
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def BlockHeight(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of ChainMakerTransactionResult
        :param _BlockHeight: 区块高度
        :type BlockHeight: int
        :param _TxCount: 交易数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TxCount: int
        :param _BlockTimestamp: 区块时间戳，单位是秒
        :type BlockTimestamp: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._BlockHeight = None
        self._TxCount = None
        self._BlockTimestamp = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def BlockHeight(self):
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def TxCount(self):
        return self._TxCount

    @TxCount.setter
    def TxCount(self, TxCount):
        self._TxCount = TxCount

    @property
    def BlockTimestamp(self):
        return self._BlockTimestamp

    @BlockTimestamp.setter
    def BlockTimestamp(self, BlockTimestamp):
        self._BlockTimestamp = BlockTimestamp

    @property
    def RequestId(self):
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ContractName(self):
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def FuncName(self):
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def FuncParam(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerContractResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def TxID(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerTransactionResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def TxID(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tbaas.v20180416.models.ChainMakerTransactionResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ChainMakerTransactionResult()
            self._Result._deserialize(params.get("Result"))
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
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ChaincodeName(self):
        return self._ChaincodeName

    @ChaincodeName.setter
    def ChaincodeName(self, ChaincodeName):
        self._ChaincodeName = ChaincodeName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Peers(self):
        return self._Peers

    @Peers.setter
    def Peers(self, Peers):
        self._Peers = Peers

    @property
    def FuncName(self):
        return self._FuncName

    @FuncName.setter
    def FuncName(self, FuncName):
        self._FuncName = FuncName

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Args(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._CertMark

    @CertMark.setter
    def CertMark(self, CertMark):
        self._CertMark = CertMark

    @property
    def SignCsrContent(self):
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
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Param(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RetCode = None
        self._RetMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RetCode = params.get("RetCode")
        self._RetMsg = params.get("RetMsg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


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
        return self._TransactionId

    @TransactionId.setter
    def TransactionId(self, TransactionId):
        self._TransactionId = TransactionId

    @property
    def TransactionHash(self):
        return self._TransactionHash

    @TransactionHash.setter
    def TransactionHash(self, TransactionHash):
        self._TransactionHash = TransactionHash

    @property
    def CreateOrgName(self):
        return self._CreateOrgName

    @CreateOrgName.setter
    def CreateOrgName(self, CreateOrgName):
        self._CreateOrgName = CreateOrgName

    @property
    def BlockId(self):
        return self._BlockId

    @BlockId.setter
    def BlockId(self, BlockId):
        self._BlockId = BlockId

    @property
    def TransactionType(self):
        return self._TransactionType

    @TransactionType.setter
    def TransactionType(self, TransactionType):
        self._TransactionType = TransactionType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BlockHeight(self):
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def TransactionStatus(self):
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
        