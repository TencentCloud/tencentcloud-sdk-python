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


class CheckChainRequest(AbstractModel):
    """CheckChain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: int
        :param _ClusterId: 网络ID
        :type ClusterId: str
        :param _AgencyName: did服务机构名称
        :type AgencyName: str
        """
        self._GroupId = None
        self._ClusterId = None
        self._AgencyName = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AgencyName(self):
        return self._AgencyName

    @AgencyName.setter
    def AgencyName(self, AgencyName):
        self._AgencyName = AgencyName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ClusterId = params.get("ClusterId")
        self._AgencyName = params.get("AgencyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckChainResponse(AbstractModel):
    """CheckChain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleType: 1为盟主，0为非盟主
        :type RoleType: int
        :param _ChainId: 链ID
        :type ChainId: str
        :param _AppName: 应用名称
        :type AppName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleType = None
        self._ChainId = None
        self._AppName = None
        self._RequestId = None

    @property
    def RoleType(self):
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleType = params.get("RoleType")
        self._ChainId = params.get("ChainId")
        self._AppName = params.get("AppName")
        self._RequestId = params.get("RequestId")


class CreateCredentialRequest(AbstractModel):
    """CreateCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionArg: 参数集合，详见示例
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.FunctionArg`
        :param _TransactionArg: 参数集合，详见示例
        :type TransactionArg: :class:`tencentcloud.tdid.v20210519.models.TransactionArg`
        :param _VersionCredential: 版本
        :type VersionCredential: str
        :param _UnSigned: 是否未签名
        :type UnSigned: bool
        """
        self._FunctionArg = None
        self._TransactionArg = None
        self._VersionCredential = None
        self._UnSigned = None

    @property
    def FunctionArg(self):
        return self._FunctionArg

    @FunctionArg.setter
    def FunctionArg(self, FunctionArg):
        self._FunctionArg = FunctionArg

    @property
    def TransactionArg(self):
        return self._TransactionArg

    @TransactionArg.setter
    def TransactionArg(self, TransactionArg):
        self._TransactionArg = TransactionArg

    @property
    def VersionCredential(self):
        return self._VersionCredential

    @VersionCredential.setter
    def VersionCredential(self, VersionCredential):
        self._VersionCredential = VersionCredential

    @property
    def UnSigned(self):
        return self._UnSigned

    @UnSigned.setter
    def UnSigned(self, UnSigned):
        self._UnSigned = UnSigned


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self._FunctionArg = FunctionArg()
            self._FunctionArg._deserialize(params.get("FunctionArg"))
        if params.get("TransactionArg") is not None:
            self._TransactionArg = TransactionArg()
            self._TransactionArg._deserialize(params.get("TransactionArg"))
        self._VersionCredential = params.get("VersionCredential")
        self._UnSigned = params.get("UnSigned")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCredentialResponse(AbstractModel):
    """CreateCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialData: Credential的具体信息
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


class CreateSelectiveCredentialRequest(AbstractModel):
    """CreateSelectiveCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionArg: 参数集合
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        :param _PolicyId: 批露策略id
        :type PolicyId: int
        """
        self._FunctionArg = None
        self._PolicyId = None

    @property
    def FunctionArg(self):
        return self._FunctionArg

    @FunctionArg.setter
    def FunctionArg(self, FunctionArg):
        self._FunctionArg = FunctionArg

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self._FunctionArg = VerifyFunctionArg()
            self._FunctionArg._deserialize(params.get("FunctionArg"))
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSelectiveCredentialResponse(AbstractModel):
    """CreateSelectiveCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialData: 凭证字符串
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


class CreateTDidByPrivateKeyRequest(AbstractModel):
    """CreateTDidByPrivateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID
        :type ClusterId: str
        :param _GroupId: 群组ID
        :type GroupId: int
        :param _PrivateKey: 私钥
        :type PrivateKey: str
        """
        self._ClusterId = None
        self._GroupId = None
        self._PrivateKey = None

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
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPrivateKeyResponse(AbstractModel):
    """CreateTDidByPrivateKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: did的具体信息
        :type Did: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Did = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._RequestId = params.get("RequestId")


class CreateTDidByPublicKeyRequest(AbstractModel):
    """CreateTDidByPublicKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 网络ID
        :type ClusterId: str
        :param _GroupId: 群组ID
        :type GroupId: int
        :param _PublicKey: 身份公钥
        :type PublicKey: str
        :param _EncryptPubKey: 加密公钥
        :type EncryptPubKey: str
        """
        self._ClusterId = None
        self._GroupId = None
        self._PublicKey = None
        self._EncryptPubKey = None

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
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def EncryptPubKey(self):
        return self._EncryptPubKey

    @EncryptPubKey.setter
    def EncryptPubKey(self, EncryptPubKey):
        self._EncryptPubKey = EncryptPubKey


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._PublicKey = params.get("PublicKey")
        self._EncryptPubKey = params.get("EncryptPubKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPublicKeyResponse(AbstractModel):
    """CreateTDidByPublicKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: did具体信息
        :type Did: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Did = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._RequestId = params.get("RequestId")


class CreateTDidRequest(AbstractModel):
    """CreateTDid请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: int
        :param _ClusterId: 网络ID
        :type ClusterId: str
        :param _Relegation: 部署机构为1，否则为0
        :type Relegation: int
        """
        self._GroupId = None
        self._ClusterId = None
        self._Relegation = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Relegation(self):
        return self._Relegation

    @Relegation.setter
    def Relegation(self, Relegation):
        self._Relegation = Relegation


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ClusterId = params.get("ClusterId")
        self._Relegation = params.get("Relegation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidResponse(AbstractModel):
    """CreateTDid返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: TDID
        :type Did: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Did = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._RequestId = params.get("RequestId")


class CredentialStatus(AbstractModel):
    """凭证链上状态信息

    """

    def __init__(self):
        r"""
        :param _CredentialId: 凭证唯一id
        :type CredentialId: str
        :param _Status: 凭证状态（0：吊销；1：有效）
        :type Status: int
        :param _Issuer: 凭证颁发者Did
        :type Issuer: str
        :param _Digest: 凭证摘要
注意：此字段可能返回 null，表示取不到有效值。
        :type Digest: str
        :param _Signature: 凭证签名
注意：此字段可能返回 null，表示取不到有效值。
        :type Signature: str
        :param _TimeStamp: 更新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        """
        self._CredentialId = None
        self._Status = None
        self._Issuer = None
        self._Digest = None
        self._Signature = None
        self._TimeStamp = None

    @property
    def CredentialId(self):
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId

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
    def Digest(self):
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp


    def _deserialize(self, params):
        self._CredentialId = params.get("CredentialId")
        self._Status = params.get("Status")
        self._Issuer = params.get("Issuer")
        self._Digest = params.get("Digest")
        self._Signature = params.get("Signature")
        self._TimeStamp = params.get("TimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionArg(AbstractModel):
    """创建凭证入参的FunctionArg

    """

    def __init__(self):
        r"""
        :param _CptId: CPT ID
        :type CptId: int
        :param _Issuer: 签发者 did
        :type Issuer: str
        :param _ExpirationDate: 过期时间
        :type ExpirationDate: str
        :param _ClaimJson: 声明
        :type ClaimJson: str
        """
        self._CptId = None
        self._Issuer = None
        self._ExpirationDate = None
        self._ClaimJson = None

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

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


    def _deserialize(self, params):
        self._CptId = params.get("CptId")
        self._Issuer = params.get("Issuer")
        self._ExpirationDate = params.get("ExpirationDate")
        self._ClaimJson = params.get("ClaimJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthorityIssuerRequest(AbstractModel):
    """GetAuthorityIssuer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: tdid
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthorityIssuerResponse(AbstractModel):
    """GetAuthorityIssuer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _ClusterId: 区块链网络id
        :type ClusterId: str
        :param _GroupId: 区块链群组id
        :type GroupId: int
        :param _Did: 权威机构did
        :type Did: str
        :param _Remark: 机构备注信息
        :type Remark: str
        :param _RegisterTime: 注册时间
        :type RegisterTime: str
        :param _RecognizeTime: 认证时间
        :type RecognizeTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._ClusterId = None
        self._GroupId = None
        self._Did = None
        self._Remark = None
        self._RegisterTime = None
        self._RecognizeTime = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RegisterTime(self):
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def RecognizeTime(self):
        return self._RecognizeTime

    @RecognizeTime.setter
    def RecognizeTime(self, RecognizeTime):
        self._RecognizeTime = RecognizeTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._Did = params.get("Did")
        self._Remark = params.get("Remark")
        self._RegisterTime = params.get("RegisterTime")
        self._RecognizeTime = params.get("RecognizeTime")
        self._RequestId = params.get("RequestId")


class GetCptInfoRequest(AbstractModel):
    """GetCptInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CptIndex: Cpt索引
        :type CptIndex: int
        """
        self._CptIndex = None

    @property
    def CptIndex(self):
        return self._CptIndex

    @CptIndex.setter
    def CptIndex(self, CptIndex):
        self._CptIndex = CptIndex


    def _deserialize(self, params):
        self._CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCptInfoResponse(AbstractModel):
    """GetCptInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CptJsonData: CptJsonData的具体信息
        :type CptJsonData: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CptJsonData = None
        self._RequestId = None

    @property
    def CptJsonData(self):
        return self._CptJsonData

    @CptJsonData.setter
    def CptJsonData(self, CptJsonData):
        self._CptJsonData = CptJsonData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CptJsonData = params.get("CptJsonData")
        self._RequestId = params.get("RequestId")


class GetCredentialStatusRequest(AbstractModel):
    """GetCredentialStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialId: 凭证id
        :type CredentialId: str
        """
        self._CredentialId = None

    @property
    def CredentialId(self):
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId


    def _deserialize(self, params):
        self._CredentialId = params.get("CredentialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialStatusResponse(AbstractModel):
    """GetCredentialStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialStatus: 凭证状态信息
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CredentialStatus = None
        self._RequestId = None

    @property
    def CredentialStatus(self):
        return self._CredentialStatus

    @CredentialStatus.setter
    def CredentialStatus(self, CredentialStatus):
        self._CredentialStatus = CredentialStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self._CredentialStatus = CredentialStatus()
            self._CredentialStatus._deserialize(params.get("CredentialStatus"))
        self._RequestId = params.get("RequestId")


class GetDidDocumentRequest(AbstractModel):
    """GetDidDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Did: tdid
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidDocumentResponse(AbstractModel):
    """GetDidDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Document: DID文档
        :type Document: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Document = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
        self._Name = params.get("Name")
        self._Document = params.get("Document")
        self._RequestId = params.get("RequestId")


class Proof(AbstractModel):
    """验证凭证签名

    """

    def __init__(self):
        r"""
        :param _Created: 创建时间
        :type Created: int
        :param _Creator: 创建着did
        :type Creator: str
        :param _SaltJson: salt值
        :type SaltJson: str
        :param _SignatureValue: 签名
        :type SignatureValue: str
        :param _Type: type类型
        :type Type: str
        """
        self._Created = None
        self._Creator = None
        self._SaltJson = None
        self._SignatureValue = None
        self._Type = None

    @property
    def Created(self):
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def SaltJson(self):
        return self._SaltJson

    @SaltJson.setter
    def SaltJson(self, SaltJson):
        self._SaltJson = SaltJson

    @property
    def SignatureValue(self):
        return self._SignatureValue

    @SignatureValue.setter
    def SignatureValue(self, SignatureValue):
        self._SignatureValue = SignatureValue

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Created = params.get("Created")
        self._Creator = params.get("Creator")
        self._SaltJson = params.get("SaltJson")
        self._SignatureValue = params.get("SignatureValue")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCptRequest(AbstractModel):
    """RegisterCpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: int
        :param _ClusterId: 网络ID
        :type ClusterId: str
        :param _CptJson: CptJson的具体信息
        :type CptJson: str
        :param _CptId: cptId 不填默认自增
        :type CptId: int
        """
        self._GroupId = None
        self._ClusterId = None
        self._CptJson = None
        self._CptId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CptJson(self):
        return self._CptJson

    @CptJson.setter
    def CptJson(self, CptJson):
        self._CptJson = CptJson

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ClusterId = params.get("ClusterId")
        self._CptJson = params.get("CptJson")
        self._CptId = params.get("CptId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCptResponse(AbstractModel):
    """RegisterCpt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 凭证模板索引
        :type Id: int
        :param _CptId: 凭证模板id
        :type CptId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._CptId = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CptId = params.get("CptId")
        self._RequestId = params.get("RequestId")


class SetCredentialStatusRequest(AbstractModel):
    """SetCredentialStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CredentialStatus: 凭证状态
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        """
        self._CredentialStatus = None

    @property
    def CredentialStatus(self):
        return self._CredentialStatus

    @CredentialStatus.setter
    def CredentialStatus(self, CredentialStatus):
        self._CredentialStatus = CredentialStatus


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self._CredentialStatus = CredentialStatus()
            self._CredentialStatus._deserialize(params.get("CredentialStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCredentialStatusResponse(AbstractModel):
    """SetCredentialStatus返回参数结构体

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


class TransactionArg(AbstractModel):
    """创建凭证第二个

    """

    def __init__(self):
        r"""
        :param _InvokerTDid: 凭证did
        :type InvokerTDid: str
        """
        self._InvokerTDid = None

    @property
    def InvokerTDid(self):
        return self._InvokerTDid

    @InvokerTDid.setter
    def InvokerTDid(self, InvokerTDid):
        self._InvokerTDid = InvokerTDid


    def _deserialize(self, params):
        self._InvokerTDid = params.get("InvokerTDid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialRequest(AbstractModel):
    """VerifyCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FunctionArg: 参数集合
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        """
        self._FunctionArg = None

    @property
    def FunctionArg(self):
        return self._FunctionArg

    @FunctionArg.setter
    def FunctionArg(self, FunctionArg):
        self._FunctionArg = FunctionArg


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self._FunctionArg = VerifyFunctionArg()
            self._FunctionArg._deserialize(params.get("FunctionArg"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialResponse(AbstractModel):
    """VerifyCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否验证成功
        :type Result: bool
        :param _VerifyCode: 验证返回码
        :type VerifyCode: int
        :param _VerifyMessage: 验证消息
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


class VerifyFunctionArg(AbstractModel):
    """验证凭证参数值

    """

    def __init__(self):
        r"""
        :param _CptId: CPT ID
        :type CptId: int
        :param _Issuer: issuer did
        :type Issuer: str
        :param _ExpirationDate: 过期时间
        :type ExpirationDate: int
        :param _ClaimJson: 声明
        :type ClaimJson: str
        :param _IssuanceDate: 颁发时间
        :type IssuanceDate: int
        :param _Context: context值
        :type Context: str
        :param _Id: id值
        :type Id: str
        :param _Proof: 签名值
        :type Proof: :class:`tencentcloud.tdid.v20210519.models.Proof`
        :param _Type: type值
        :type Type: list of str
        """
        self._CptId = None
        self._Issuer = None
        self._ExpirationDate = None
        self._ClaimJson = None
        self._IssuanceDate = None
        self._Context = None
        self._Id = None
        self._Proof = None
        self._Type = None

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

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
    def IssuanceDate(self):
        return self._IssuanceDate

    @IssuanceDate.setter
    def IssuanceDate(self, IssuanceDate):
        self._IssuanceDate = IssuanceDate

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Proof(self):
        return self._Proof

    @Proof.setter
    def Proof(self, Proof):
        self._Proof = Proof

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._CptId = params.get("CptId")
        self._Issuer = params.get("Issuer")
        self._ExpirationDate = params.get("ExpirationDate")
        self._ClaimJson = params.get("ClaimJson")
        self._IssuanceDate = params.get("IssuanceDate")
        self._Context = params.get("Context")
        self._Id = params.get("Id")
        if params.get("Proof") is not None:
            self._Proof = Proof()
            self._Proof._deserialize(params.get("Proof"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        