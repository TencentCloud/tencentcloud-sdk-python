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


class CRDLArg(AbstractModel):
    """颁发凭证的数据参数

    """

    def __init__(self):
        r"""
        :param _CPTId: CPT ID
        :type CPTId: int
        :param _Issuer: 签发者 did
        :type Issuer: str
        :param _ExpirationDate: 过期时间
        :type ExpirationDate: str
        :param _ClaimJson: 声明
        :type ClaimJson: str
        :param _Type: 凭证类型
        :type Type: list of str
        :param _Parties: 多方签名的用户did
        :type Parties: list of str
        """
        self._CPTId = None
        self._Issuer = None
        self._ExpirationDate = None
        self._ClaimJson = None
        self._Type = None
        self._Parties = None

    @property
    def CPTId(self):
        return self._CPTId

    @CPTId.setter
    def CPTId(self, CPTId):
        self._CPTId = CPTId

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def ClaimJson(self):
        return self._ClaimJson

    @ClaimJson.setter
    def ClaimJson(self, ClaimJson):
        self._ClaimJson = ClaimJson

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Parties(self):
        return self._Parties

    @Parties.setter
    def Parties(self, Parties):
        self._Parties = Parties


    def _deserialize(self, params):
        self._CPTId = params.get("CPTId")
        self._Issuer = params.get("Issuer")
        self._ExpirationDate = params.get("ExpirationDate")
        self._ClaimJson = params.get("ClaimJson")
        self._Type = params.get("Type")
        self._Parties = params.get("Parties")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChainTransaction(AbstractModel):
    """链上交易信息

    """

    def __init__(self):
        r"""
        :param _TransactionHash: 交易哈希
        :type TransactionHash: str
        """
        self._TransactionHash = None

    @property
    def TransactionHash(self):
        return self._TransactionHash

    @TransactionHash.setter
    def TransactionHash(self, TransactionHash):
        self._TransactionHash = TransactionHash


    def _deserialize(self, params):
        self._TransactionHash = params.get("TransactionHash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckNewPurchaseRequest(AbstractModel):
    """CheckNewPurchase请求参数结构体

    """


class CheckNewPurchaseResponse(AbstractModel):
    """CheckNewPurchase返回参数结构体

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


class CreateTDidByHostRequest(AbstractModel):
    """CreateTDidByHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DAPId: DID应用ID
        :type DAPId: int
        :param _CustomAttribute: 自定义DID文档json属性
        :type CustomAttribute: str
        """
        self._DAPId = None
        self._CustomAttribute = None

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId

    @property
    def CustomAttribute(self):
        return self._CustomAttribute

    @CustomAttribute.setter
    def CustomAttribute(self, CustomAttribute):
        self._CustomAttribute = CustomAttribute


    def _deserialize(self, params):
        self._DAPId = params.get("DAPId")
        self._CustomAttribute = params.get("CustomAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByHostResponse(AbstractModel):
    """CreateTDidByHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: DID标识
        :type Did: str
        :param _Transaction: 链上交易信息
        :type Transaction: :class:`tencentcloud.tdid.v20210519.models.ChainTransaction`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Did = None
        self._Transaction = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        if params.get("Transaction") is not None:
            self._Transaction = ChainTransaction()
            self._Transaction._deserialize(params.get("Transaction"))
        self._RequestId = params.get("RequestId")


class CreateTDidByPubKeyRequest(AbstractModel):
    """CreateTDidByPubKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DAPId: DID应用id
        :type DAPId: int
        :param _PublicKey: pem格式的认证公钥
        :type PublicKey: str
        :param _CustomAttribute: 自定义DID初始化属性json字符串
        :type CustomAttribute: str
        :param _IgnoreExisted: 0:did存在返回错误，1:did存在返回该did，默认:0
        :type IgnoreExisted: int
        """
        self._DAPId = None
        self._PublicKey = None
        self._CustomAttribute = None
        self._IgnoreExisted = None

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def CustomAttribute(self):
        return self._CustomAttribute

    @CustomAttribute.setter
    def CustomAttribute(self, CustomAttribute):
        self._CustomAttribute = CustomAttribute

    @property
    def IgnoreExisted(self):
        return self._IgnoreExisted

    @IgnoreExisted.setter
    def IgnoreExisted(self, IgnoreExisted):
        self._IgnoreExisted = IgnoreExisted


    def _deserialize(self, params):
        self._DAPId = params.get("DAPId")
        self._PublicKey = params.get("PublicKey")
        self._CustomAttribute = params.get("CustomAttribute")
        self._IgnoreExisted = params.get("IgnoreExisted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPubKeyResponse(AbstractModel):
    """CreateTDidByPubKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: did标识
        :type Did: str
        :param _Transaction: 链上交易信息
        :type Transaction: :class:`tencentcloud.tdid.v20210519.models.ChainTransaction`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Did = None
        self._Transaction = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        if params.get("Transaction") is not None:
            self._Transaction = ChainTransaction()
            self._Transaction._deserialize(params.get("Transaction"))
        self._RequestId = params.get("RequestId")


class CredentialState(AbstractModel):
    """凭证链上状态信息

    """

    def __init__(self):
        r"""
        :param _Id: 凭证唯一id
        :type Id: str
        :param _Status: 凭证状态（0：吊销；1：有效）
        :type Status: int
        :param _Issuer: 凭证颁发者Did
        :type Issuer: str
        :param _VCDigest: VC摘要，对应凭证Proof的vcDigest字段
        :type VCDigest: str
        :param _TXDigest: 交易摘要，对应凭证Proof的txDigest字段 
        :type TXDigest: str
        :param _IssueTime: 颁布凭证的UTC时间戳
        :type IssueTime: int
        :param _ExpireTime: 凭证过期的UTC时间戳
        :type ExpireTime: int
        :param _CPTId: 凭证模板id
        :type CPTId: int
        :param _Signature: 凭证签名
        :type Signature: str
        :param _MetaDigest: 元数据摘要
        :type MetaDigest: str
        """
        self._Id = None
        self._Status = None
        self._Issuer = None
        self._VCDigest = None
        self._TXDigest = None
        self._IssueTime = None
        self._ExpireTime = None
        self._CPTId = None
        self._Signature = None
        self._MetaDigest = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def VCDigest(self):
        return self._VCDigest

    @VCDigest.setter
    def VCDigest(self, VCDigest):
        self._VCDigest = VCDigest

    @property
    def TXDigest(self):
        return self._TXDigest

    @TXDigest.setter
    def TXDigest(self, TXDigest):
        self._TXDigest = TXDigest

    @property
    def IssueTime(self):
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, IssueTime):
        self._IssueTime = IssueTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CPTId(self):
        return self._CPTId

    @CPTId.setter
    def CPTId(self, CPTId):
        self._CPTId = CPTId

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def MetaDigest(self):
        return self._MetaDigest

    @MetaDigest.setter
    def MetaDigest(self, MetaDigest):
        self._MetaDigest = MetaDigest


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Issuer = params.get("Issuer")
        self._VCDigest = params.get("VCDigest")
        self._TXDigest = params.get("TXDigest")
        self._IssueTime = params.get("IssueTime")
        self._ExpireTime = params.get("ExpireTime")
        self._CPTId = params.get("CPTId")
        self._Signature = params.get("Signature")
        self._MetaDigest = params.get("MetaDigest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateTDidRequest(AbstractModel):
    """DeactivateTDid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: DID标识符
        :type Did: str
        :param _OperateCredential: 设置DID禁用状态的临时凭证内容，通过创建凭证接口(CreateCredential)生成并签名，凭证类型为：OperateCredential, 为安全起见凭证过期时间不适合太长，建议设置为1分钟内
        :type OperateCredential: str
        :param _DAPId: DID应用Id
        :type DAPId: int
        :param _Deactivated: 是否禁用
        :type Deactivated: str
        """
        self._Did = None
        self._OperateCredential = None
        self._DAPId = None
        self._Deactivated = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def OperateCredential(self):
        return self._OperateCredential

    @OperateCredential.setter
    def OperateCredential(self, OperateCredential):
        self._OperateCredential = OperateCredential

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId

    @property
    def Deactivated(self):
        return self._Deactivated

    @Deactivated.setter
    def Deactivated(self, Deactivated):
        self._Deactivated = Deactivated


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._OperateCredential = params.get("OperateCredential")
        self._DAPId = params.get("DAPId")
        self._Deactivated = params.get("Deactivated")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateTDidResponse(AbstractModel):
    """DeactivateTDid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Transaction: 上链交易信息
        :type Transaction: :class:`tencentcloud.tdid.v20210519.models.ChainTransaction`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Transaction = None
        self._RequestId = None

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Transaction") is not None:
            self._Transaction = ChainTransaction()
            self._Transaction._deserialize(params.get("Transaction"))
        self._RequestId = params.get("RequestId")


class GetCredentialStateRequest(AbstractModel):
    """GetCredentialState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialId: 凭证唯一Id
        :type CredentialId: str
        :param _DAPId: 用户应用Id
        :type DAPId: int
        """
        self._CredentialId = None
        self._DAPId = None

    @property
    def CredentialId(self):
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId


    def _deserialize(self, params):
        self._CredentialId = params.get("CredentialId")
        self._DAPId = params.get("DAPId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialStateResponse(AbstractModel):
    """GetCredentialState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialState: 凭证状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CredentialState: :class:`tencentcloud.tdid.v20210519.models.CredentialState`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CredentialState = None
        self._RequestId = None

    @property
    def CredentialState(self):
        return self._CredentialState

    @CredentialState.setter
    def CredentialState(self, CredentialState):
        self._CredentialState = CredentialState

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CredentialState") is not None:
            self._CredentialState = CredentialState()
            self._CredentialState._deserialize(params.get("CredentialState"))
        self._RequestId = params.get("RequestId")


class GetTDidDocumentRequest(AbstractModel):
    """GetTDidDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: DID标识
        :type Did: str
        :param _DAPId: DID应用ID
        :type DAPId: int
        """
        self._Did = None
        self._DAPId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._DAPId = params.get("DAPId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTDidDocumentResponse(AbstractModel):
    """GetTDidDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: DID文档内容
        :type Document: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Document = None
        self._RequestId = None

    @property
    def Document(self):
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Document = params.get("Document")
        self._RequestId = params.get("RequestId")


class IssueCredentialRequest(AbstractModel):
    """IssueCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CRDLArg: 参数集合，详见示例
        :type CRDLArg: :class:`tencentcloud.tdid.v20210519.models.CRDLArg`
        :param _UnSigned: 是否未签名
        :type UnSigned: bool
        :param _DAPId: DID应用id
        :type DAPId: int
        """
        self._CRDLArg = None
        self._UnSigned = None
        self._DAPId = None

    @property
    def CRDLArg(self):
        return self._CRDLArg

    @CRDLArg.setter
    def CRDLArg(self, CRDLArg):
        self._CRDLArg = CRDLArg

    @property
    def UnSigned(self):
        return self._UnSigned

    @UnSigned.setter
    def UnSigned(self, UnSigned):
        self._UnSigned = UnSigned

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId


    def _deserialize(self, params):
        if params.get("CRDLArg") is not None:
            self._CRDLArg = CRDLArg()
            self._CRDLArg._deserialize(params.get("CRDLArg"))
        self._UnSigned = params.get("UnSigned")
        self._DAPId = params.get("DAPId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueCredentialResponse(AbstractModel):
    """IssueCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialData: 可验证凭证内容
        :type CredentialData: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CredentialData = None
        self._RequestId = None

    @property
    def CredentialData(self):
        return self._CredentialData

    @CredentialData.setter
    def CredentialData(self, CredentialData):
        self._CredentialData = CredentialData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CredentialData = params.get("CredentialData")
        self._RequestId = params.get("RequestId")


class UpdateCredentialStateRequest(AbstractModel):
    """UpdateCredentialState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DAPId: DID应用Id
        :type DAPId: int
        :param _OperateCredential: 更新VC状态的临时凭证内容，通过创建凭证接口(CreateCredential)生成并签名，凭证类型为：OperateCredential, 为安全起见凭证过期时间不适合太长，建议设置为1分钟内
        :type OperateCredential: str
        """
        self._DAPId = None
        self._OperateCredential = None

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId

    @property
    def OperateCredential(self):
        return self._OperateCredential

    @OperateCredential.setter
    def OperateCredential(self, OperateCredential):
        self._OperateCredential = OperateCredential


    def _deserialize(self, params):
        self._DAPId = params.get("DAPId")
        self._OperateCredential = params.get("OperateCredential")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCredentialStateResponse(AbstractModel):
    """UpdateCredentialState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 更新是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class VerifyCredentialsRequest(AbstractModel):
    """VerifyCredentials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyType: 0:仅验证签名，1:验证签名和链上状态，2, 仅验证链上状态，默认为0, 3.验证DID和凭证状态以及签名，4. 验证历史凭证有效性
        :type VerifyType: int
        :param _CredentialData: 凭证内容
        :type CredentialData: str
        :param _DAPId: DID应用id
        :type DAPId: int
        """
        self._VerifyType = None
        self._CredentialData = None
        self._DAPId = None

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def CredentialData(self):
        return self._CredentialData

    @CredentialData.setter
    def CredentialData(self, CredentialData):
        self._CredentialData = CredentialData

    @property
    def DAPId(self):
        return self._DAPId

    @DAPId.setter
    def DAPId(self, DAPId):
        self._DAPId = DAPId


    def _deserialize(self, params):
        self._VerifyType = params.get("VerifyType")
        self._CredentialData = params.get("CredentialData")
        self._DAPId = params.get("DAPId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialsResponse(AbstractModel):
    """VerifyCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否验证成功
        :type Result: bool
        :param _VerifyCode: 验证返回码
        :type VerifyCode: int
        :param _VerifyMessage: 验证结果信息
        :type VerifyMessage: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._VerifyCode = None
        self._VerifyMessage = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def VerifyCode(self):
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode

    @property
    def VerifyMessage(self):
        return self._VerifyMessage

    @VerifyMessage.setter
    def VerifyMessage(self, VerifyMessage):
        self._VerifyMessage = VerifyMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._VerifyCode = params.get("VerifyCode")
        self._VerifyMessage = params.get("VerifyMessage")
        self._RequestId = params.get("RequestId")