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


class CreateCredentialRequest(AbstractModel):
    """CreateCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionArg: 参数集合，详见示例
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.FunctionArg`
        :param TransactionArg: 参数集合，详见示例
        :type TransactionArg: :class:`tencentcloud.tdid.v20210519.models.TransactionArg`
        :param VersionCredential: 版本
        :type VersionCredential: str
        """
        self.FunctionArg = None
        self.TransactionArg = None
        self.VersionCredential = None


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self.FunctionArg = FunctionArg()
            self.FunctionArg._deserialize(params.get("FunctionArg"))
        if params.get("TransactionArg") is not None:
            self.TransactionArg = TransactionArg()
            self.TransactionArg._deserialize(params.get("TransactionArg"))
        self.VersionCredential = params.get("VersionCredential")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCredentialResponse(AbstractModel):
    """CreateCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param CredentialData: Credential的具体信息
        :type CredentialData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CredentialData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CredentialData = params.get("CredentialData")
        self.RequestId = params.get("RequestId")


class CreateSelectiveCredentialRequest(AbstractModel):
    """CreateSelectiveCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionArg: 参数集合
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        :param PolicyId: 批露策略id
        :type PolicyId: int
        """
        self.FunctionArg = None
        self.PolicyId = None


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self.FunctionArg = VerifyFunctionArg()
            self.FunctionArg._deserialize(params.get("FunctionArg"))
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSelectiveCredentialResponse(AbstractModel):
    """CreateSelectiveCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param CredentialData: 凭证字符串
        :type CredentialData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CredentialData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CredentialData = params.get("CredentialData")
        self.RequestId = params.get("RequestId")


class CreateTDidRequest(AbstractModel):
    """CreateTDid请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 群组ID
        :type GroupId: int
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param Relegation: 部署机构为1，否则为0
        :type Relegation: int
        """
        self.GroupId = None
        self.ClusterId = None
        self.Relegation = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.Relegation = params.get("Relegation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidResponse(AbstractModel):
    """CreateTDid返回参数结构体

    """

    def __init__(self):
        r"""
        :param Did: TDID
        :type Did: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Did = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.RequestId = params.get("RequestId")


class FunctionArg(AbstractModel):
    """创建凭证入参的FunctionArg

    """

    def __init__(self):
        r"""
        :param CptId: CPT ID
        :type CptId: int
        :param Issuer: 签发者 did
        :type Issuer: str
        :param ExpirationDate: 过期时间
        :type ExpirationDate: str
        :param ClaimJson: 声明
        :type ClaimJson: str
        """
        self.CptId = None
        self.Issuer = None
        self.ExpirationDate = None
        self.ClaimJson = None


    def _deserialize(self, params):
        self.CptId = params.get("CptId")
        self.Issuer = params.get("Issuer")
        self.ExpirationDate = params.get("ExpirationDate")
        self.ClaimJson = params.get("ClaimJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Proof(AbstractModel):
    """验证凭证签名

    """

    def __init__(self):
        r"""
        :param Created: 创建时间
        :type Created: int
        :param Creator: 创建着did
        :type Creator: str
        :param SaltJson: salt值
        :type SaltJson: str
        :param SignatureValue: 签名
        :type SignatureValue: str
        :param Type: type类型
        :type Type: str
        """
        self.Created = None
        self.Creator = None
        self.SaltJson = None
        self.SignatureValue = None
        self.Type = None


    def _deserialize(self, params):
        self.Created = params.get("Created")
        self.Creator = params.get("Creator")
        self.SaltJson = params.get("SaltJson")
        self.SignatureValue = params.get("SignatureValue")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionArg(AbstractModel):
    """创建凭证第二个

    """

    def __init__(self):
        r"""
        :param InvokerTDid: 凭证did
        :type InvokerTDid: str
        """
        self.InvokerTDid = None


    def _deserialize(self, params):
        self.InvokerTDid = params.get("InvokerTDid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialRequest(AbstractModel):
    """VerifyCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionArg: 参数集合
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        """
        self.FunctionArg = None


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self.FunctionArg = VerifyFunctionArg()
            self.FunctionArg._deserialize(params.get("FunctionArg"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialResponse(AbstractModel):
    """VerifyCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 是否验证成功
        :type Result: bool
        :param VerifyCode: 验证返回码
        :type VerifyCode: int
        :param VerifyMessage: 验证消息
        :type VerifyMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.VerifyCode = None
        self.VerifyMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.VerifyCode = params.get("VerifyCode")
        self.VerifyMessage = params.get("VerifyMessage")
        self.RequestId = params.get("RequestId")


class VerifyFunctionArg(AbstractModel):
    """验证凭证参数值

    """

    def __init__(self):
        r"""
        :param CptId: CPT ID
        :type CptId: int
        :param Issuer: issuer did
        :type Issuer: str
        :param ExpirationDate: 过期时间
        :type ExpirationDate: int
        :param ClaimJson: 声明
        :type ClaimJson: str
        :param IssuanceDate: 颁发时间
        :type IssuanceDate: int
        :param Context: context值
        :type Context: str
        :param Id: id值
        :type Id: str
        :param Proof: 签名值
        :type Proof: :class:`tencentcloud.tdid.v20210519.models.Proof`
        :param Type: type值
        :type Type: list of str
        """
        self.CptId = None
        self.Issuer = None
        self.ExpirationDate = None
        self.ClaimJson = None
        self.IssuanceDate = None
        self.Context = None
        self.Id = None
        self.Proof = None
        self.Type = None


    def _deserialize(self, params):
        self.CptId = params.get("CptId")
        self.Issuer = params.get("Issuer")
        self.ExpirationDate = params.get("ExpirationDate")
        self.ClaimJson = params.get("ClaimJson")
        self.IssuanceDate = params.get("IssuanceDate")
        self.Context = params.get("Context")
        self.Id = params.get("Id")
        if params.get("Proof") is not None:
            self.Proof = Proof()
            self.Proof._deserialize(params.get("Proof"))
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        