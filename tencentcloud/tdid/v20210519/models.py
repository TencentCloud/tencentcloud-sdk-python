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


class AddLabelRequest(AbstractModel):
    """AddLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param LabelId: 标签ID
        :type LabelId: int
        :param Did: tdid
        :type Did: str
        """
        self.LabelId = None
        self.Did = None


    def _deserialize(self, params):
        self.LabelId = params.get("LabelId")
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLabelResponse(AbstractModel):
    """AddLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Authority(AbstractModel):
    """权威机构

    """

    def __init__(self):
        r"""
        :param Id: 权威机构ID
        :type Id: int
        :param DidId: Did的ID
        :type DidId: int
        :param Did: DID具体信息
        :type Did: str
        :param Name: 机构名称
        :type Name: str
        :param Status: 权威认证 1:已认证，2:未认证
        :type Status: int
        :param DidServiceId: DID服务ID
        :type DidServiceId: int
        :param ContractAppId: 应用ID
        :type ContractAppId: int
        :param Remark: 备注
        :type Remark: str
        :param RegisterTime: 注册时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisterTime: str
        :param RecognizeTime: 认证时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognizeTime: str
        :param CreateTime: 生成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param AppName: 合约名称
        :type AppName: str
        :param LabelName: 链上标签
        :type LabelName: str
        """
        self.Id = None
        self.DidId = None
        self.Did = None
        self.Name = None
        self.Status = None
        self.DidServiceId = None
        self.ContractAppId = None
        self.Remark = None
        self.RegisterTime = None
        self.RecognizeTime = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClusterId = None
        self.GroupId = None
        self.AppName = None
        self.LabelName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DidId = params.get("DidId")
        self.Did = params.get("Did")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.DidServiceId = params.get("DidServiceId")
        self.ContractAppId = params.get("ContractAppId")
        self.Remark = params.get("Remark")
        self.RegisterTime = params.get("RegisterTime")
        self.RecognizeTime = params.get("RecognizeTime")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.AppName = params.get("AppName")
        self.LabelName = params.get("LabelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BcosClusterItem(AbstractModel):
    """bcos网络信息

    """

    def __init__(self):
        r"""
        :param ChainId: 网络索引id
        :type ChainId: int
        :param ChainName: 网络名称
        :type ChainName: str
        :param AgencyCount: 机构数量
        :type AgencyCount: int
        :param ConsortiumId: 联盟id
        :type ConsortiumId: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param ChainStatus: 网络状态
        :type ChainStatus: int
        :param ResourceId: 资源 id
        :type ResourceId: str
        :param ClusterId: 集群id
        :type ClusterId: str
        :param ConsortiumName: 组织名称
        :type ConsortiumName: str
        :param AgencyId: 机构id
        :type AgencyId: int
        :param AutoRenewFlag: 续费状态
        :type AutoRenewFlag: int
        :param TotalNetworkNode: 网络模式
        :type TotalNetworkNode: int
        :param TotalCreateNode: 创建节点数
        :type TotalCreateNode: int
        :param TotalGroups: 总群组数量
        :type TotalGroups: int
        """
        self.ChainId = None
        self.ChainName = None
        self.AgencyCount = None
        self.ConsortiumId = None
        self.CreateTime = None
        self.ExpireTime = None
        self.ChainStatus = None
        self.ResourceId = None
        self.ClusterId = None
        self.ConsortiumName = None
        self.AgencyId = None
        self.AutoRenewFlag = None
        self.TotalNetworkNode = None
        self.TotalCreateNode = None
        self.TotalGroups = None


    def _deserialize(self, params):
        self.ChainId = params.get("ChainId")
        self.ChainName = params.get("ChainName")
        self.AgencyCount = params.get("AgencyCount")
        self.ConsortiumId = params.get("ConsortiumId")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChainStatus = params.get("ChainStatus")
        self.ResourceId = params.get("ResourceId")
        self.ClusterId = params.get("ClusterId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.AgencyId = params.get("AgencyId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.TotalNetworkNode = params.get("TotalNetworkNode")
        self.TotalCreateNode = params.get("TotalCreateNode")
        self.TotalGroups = params.get("TotalGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorityIssuerRequest(AbstractModel):
    """CancelAuthorityIssuer请求参数结构体

    """

    def __init__(self):
        r"""
        :param Did: did具体信息
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorityIssuerResponse(AbstractModel):
    """CancelAuthorityIssuer返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckChainRequest(AbstractModel):
    """CheckChain请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 群组ID
        :type GroupId: int
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param AgencyName: did服务机构名称
        :type AgencyName: str
        """
        self.GroupId = None
        self.ClusterId = None
        self.AgencyName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.AgencyName = params.get("AgencyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckChainResponse(AbstractModel):
    """CheckChain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoleType: 1为盟主，0为非盟主
        :type RoleType: int
        :param ChainId: 链ID
        :type ChainId: str
        :param AppName: 应用名称
        :type AppName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoleType = None
        self.ChainId = None
        self.AppName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleType = params.get("RoleType")
        self.ChainId = params.get("ChainId")
        self.AppName = params.get("AppName")
        self.RequestId = params.get("RequestId")


class CheckDidDeployRequest(AbstractModel):
    """CheckDidDeploy请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDidDeployResponse(AbstractModel):
    """CheckDidDeploy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Task: 服务信息
        :type Task: :class:`tencentcloud.tdid.v20210519.models.Task`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Task = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.RequestId = params.get("RequestId")


class ConsortiumItem(AbstractModel):
    """联盟信息

    """

    def __init__(self):
        r"""
        :param Id: 联盟id
        :type Id: int
        :param Name: 联盟名称
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Contract(AbstractModel):
    """部署合约

    """

    def __init__(self):
        r"""
        :param ApplyName: 应用名
        :type ApplyName: str
        :param Enable: 合约状态 true:已启用 false:未启用
        :type Enable: bool
        :param Hash: 合约CNS地址
        :type Hash: str
        :param HashShow: 合约CNS地址脱敏
        :type HashShow: str
        :param WeId: 部署机构DID
        :type WeId: str
        :param DeployName: 部署机构名称
        :type DeployName: str
        :param GroupId: 部署群组
        :type GroupId: str
        :param CreateTime: 部署时间
        :type CreateTime: str
        """
        self.ApplyName = None
        self.Enable = None
        self.Hash = None
        self.HashShow = None
        self.WeId = None
        self.DeployName = None
        self.GroupId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ApplyName = params.get("ApplyName")
        self.Enable = params.get("Enable")
        self.Hash = params.get("Hash")
        self.HashShow = params.get("HashShow")
        self.WeId = params.get("WeId")
        self.DeployName = params.get("DeployName")
        self.GroupId = params.get("GroupId")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CptIssueRank(AbstractModel):
    """模板颁发量排名

    """

    def __init__(self):
        r"""
        :param CptName: 模板名称
        :type CptName: str
        :param Rank: 名次
        :type Rank: int
        :param Count: 颁发量
        :type Count: int
        :param ApplyName: 应用名称
        :type ApplyName: str
        :param ApplyId: 应用ID
        :type ApplyId: int
        """
        self.CptName = None
        self.Rank = None
        self.Count = None
        self.ApplyName = None
        self.ApplyId = None


    def _deserialize(self, params):
        self.CptName = params.get("CptName")
        self.Rank = params.get("Rank")
        self.Count = params.get("Count")
        self.ApplyName = params.get("ApplyName")
        self.ApplyId = params.get("ApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CptListData(AbstractModel):
    """cpt集合数据

    """

    def __init__(self):
        r"""
        :param Id: ID信息
        :type Id: int
        :param Name: 模版名称
        :type Name: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param ServiceId: 服务ID
        :type ServiceId: int
        :param ContractAppId: 合约应用ID
        :type ContractAppId: int
        :param CptId: 凭证模板ID
        :type CptId: int
        :param CptType: 模板类型，1: 系统模板，2: 用户模板，3:普通模板
        :type CptType: int
        :param Description: 凭证模版描述
        :type Description: str
        :param CptJson: 凭证模板Json
        :type CptJson: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreatorDid: 创建者DID
        :type CreatorDid: str
        :param AppName: 应用名称
        :type AppName: str
        """
        self.Id = None
        self.Name = None
        self.ClusterId = None
        self.GroupId = None
        self.ServiceId = None
        self.ContractAppId = None
        self.CptId = None
        self.CptType = None
        self.Description = None
        self.CptJson = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CreatorDid = None
        self.AppName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ServiceId = params.get("ServiceId")
        self.ContractAppId = params.get("ContractAppId")
        self.CptId = params.get("CptId")
        self.CptType = params.get("CptType")
        self.Description = params.get("Description")
        self.CptJson = params.get("CptJson")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CreatorDid = params.get("CreatorDid")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param UnSigned: 是否未签名
        :type UnSigned: bool
        """
        self.FunctionArg = None
        self.TransactionArg = None
        self.VersionCredential = None
        self.UnSigned = None


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self.FunctionArg = FunctionArg()
            self.FunctionArg._deserialize(params.get("FunctionArg"))
        if params.get("TransactionArg") is not None:
            self.TransactionArg = TransactionArg()
            self.TransactionArg._deserialize(params.get("TransactionArg"))
        self.VersionCredential = params.get("VersionCredential")
        self.UnSigned = params.get("UnSigned")
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


class CreateDidServiceRequest(AbstractModel):
    """CreateDidService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConsortiumName: 联盟名称
        :type ConsortiumName: str
        :param ConsortiumId: 联盟ID
        :type ConsortiumId: int
        :param GroupId: 群组ID
        :type GroupId: int
        :param AgencyName: 机构名称
        :type AgencyName: str
        :param AppName: 应用名称
        :type AppName: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupName: 群组名称
        :type GroupName: str
        """
        self.ConsortiumName = None
        self.ConsortiumId = None
        self.GroupId = None
        self.AgencyName = None
        self.AppName = None
        self.ClusterId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.ConsortiumName = params.get("ConsortiumName")
        self.ConsortiumId = params.get("ConsortiumId")
        self.GroupId = params.get("GroupId")
        self.AgencyName = params.get("AgencyName")
        self.AppName = params.get("AppName")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDidServiceResponse(AbstractModel):
    """CreateDidService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Task: 服务信息
        :type Task: :class:`tencentcloud.tdid.v20210519.models.Task`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Task = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.RequestId = params.get("RequestId")


class CreateLabelRequest(AbstractModel):
    """CreateLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param LabelName: 标签名称
        :type LabelName: str
        :param ClusterId: 网络Id
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        """
        self.LabelName = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.LabelName = params.get("LabelName")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLabelResponse(AbstractModel):
    """CreateLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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


class CreateTDidByPrivateKeyRequest(AbstractModel):
    """CreateTDidByPrivateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param PrivateKey: 私钥
        :type PrivateKey: str
        """
        self.ClusterId = None
        self.GroupId = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPrivateKeyResponse(AbstractModel):
    """CreateTDidByPrivateKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Did: did的具体信息
        :type Did: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Did = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.RequestId = params.get("RequestId")


class CreateTDidByPublicKeyRequest(AbstractModel):
    """CreateTDidByPublicKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param PublicKey: 身份公钥
        :type PublicKey: str
        :param EncryptPubKey: 加密公钥
        :type EncryptPubKey: str
        """
        self.ClusterId = None
        self.GroupId = None
        self.PublicKey = None
        self.EncryptPubKey = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.PublicKey = params.get("PublicKey")
        self.EncryptPubKey = params.get("EncryptPubKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPublicKeyResponse(AbstractModel):
    """CreateTDidByPublicKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Did: did具体信息
        :type Did: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Did = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
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


class CredentialStatus(AbstractModel):
    """凭证链上状态信息

    """

    def __init__(self):
        r"""
        :param CredentialId: 凭证唯一id
        :type CredentialId: str
        :param Status: 凭证状态（0：吊销；1：有效）
        :type Status: int
        :param Issuer: 凭证颁发者Did
        :type Issuer: str
        :param Digest: 凭证摘要
注意：此字段可能返回 null，表示取不到有效值。
        :type Digest: str
        :param Signature: 凭证签名
注意：此字段可能返回 null，表示取不到有效值。
        :type Signature: str
        :param TimeStamp: 更新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        """
        self.CredentialId = None
        self.Status = None
        self.Issuer = None
        self.Digest = None
        self.Signature = None
        self.TimeStamp = None


    def _deserialize(self, params):
        self.CredentialId = params.get("CredentialId")
        self.Status = params.get("Status")
        self.Issuer = params.get("Issuer")
        self.Digest = params.get("Digest")
        self.Signature = params.get("Signature")
        self.TimeStamp = params.get("TimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployByNameRequest(AbstractModel):
    """DeployByName请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationName: 应用名称
        :type ApplicationName: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        """
        self.ApplicationName = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployByNameResponse(AbstractModel):
    """DeployByName返回参数结构体

    """

    def __init__(self):
        r"""
        :param Hash: 哈希值
        :type Hash: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Hash = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        self.RequestId = params.get("RequestId")


class DidCluster(AbstractModel):
    """did区块链网络信息

    """

    def __init__(self):
        r"""
        :param ChainId: 链ID
        :type ChainId: int
        :param ChainName: 链名称
        :type ChainName: str
        :param AgencyCount: 组织数量
        :type AgencyCount: int
        :param ConsortiumId: 联盟ID
        :type ConsortiumId: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param ChainStatus: 网络状态
        :type ChainStatus: int
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param ConsortiumName: 联盟名称
        :type ConsortiumName: str
        :param AgencyId: 组织ID
        :type AgencyId: int
        :param AutoRenewFlag: 自动续费
        :type AutoRenewFlag: int
        :param TotalNetworkNode: 网络节点总数
        :type TotalNetworkNode: int
        :param TotalCreateNode: 本机构节点数
        :type TotalCreateNode: int
        :param TotalGroups: 总群组数
        :type TotalGroups: int
        :param DidCount: DID总数
        :type DidCount: int
        """
        self.ChainId = None
        self.ChainName = None
        self.AgencyCount = None
        self.ConsortiumId = None
        self.CreateTime = None
        self.ExpireTime = None
        self.ChainStatus = None
        self.ResourceId = None
        self.ClusterId = None
        self.ConsortiumName = None
        self.AgencyId = None
        self.AutoRenewFlag = None
        self.TotalNetworkNode = None
        self.TotalCreateNode = None
        self.TotalGroups = None
        self.DidCount = None


    def _deserialize(self, params):
        self.ChainId = params.get("ChainId")
        self.ChainName = params.get("ChainName")
        self.AgencyCount = params.get("AgencyCount")
        self.ConsortiumId = params.get("ConsortiumId")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChainStatus = params.get("ChainStatus")
        self.ResourceId = params.get("ResourceId")
        self.ClusterId = params.get("ClusterId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.AgencyId = params.get("AgencyId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.TotalNetworkNode = params.get("TotalNetworkNode")
        self.TotalCreateNode = params.get("TotalCreateNode")
        self.TotalGroups = params.get("TotalGroups")
        self.DidCount = params.get("DidCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DidData(AbstractModel):
    """DID列表

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: int
        :param GroupId: 群组ID
        :type GroupId: int
        :param AppName: 应用名称
        :type AppName: str
        :param Did: did号码
        :type Did: str
        :param Remark: 备注
        :type Remark: str
        :param AuthorityState: 权威机构认证状态 1未注册 2 未认证 3 已认证
        :type AuthorityState: int
        :param LabelName: DID标签名称
        :type LabelName: str
        :param CreatedAt: DID创建时间
        :type CreatedAt: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param AllianceName: 联盟名称
        :type AllianceName: str
        :param LabelId: DID标签id
        :type LabelId: int
        """
        self.ServiceId = None
        self.GroupId = None
        self.AppName = None
        self.Did = None
        self.Remark = None
        self.AuthorityState = None
        self.LabelName = None
        self.CreatedAt = None
        self.ClusterId = None
        self.AllianceName = None
        self.LabelId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.GroupId = params.get("GroupId")
        self.AppName = params.get("AppName")
        self.Did = params.get("Did")
        self.Remark = params.get("Remark")
        self.AuthorityState = params.get("AuthorityState")
        self.LabelName = params.get("LabelName")
        self.CreatedAt = params.get("CreatedAt")
        self.ClusterId = params.get("ClusterId")
        self.AllianceName = params.get("AllianceName")
        self.LabelId = params.get("LabelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DidServiceInfo(AbstractModel):
    """DID服务基本信息

    """

    def __init__(self):
        r"""
        :param Id: DID服务索引
        :type Id: int
        :param Appid: 应用ID
        :type Appid: int
        :param Uin: 账号唯一标识
        :type Uin: str
        :param ConsortiumId: 联盟id
        :type ConsortiumId: int
        :param ConsortiumName: 联盟名称
        :type ConsortiumName: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param ChainId: 链ID
        :type ChainId: str
        :param RoleType: 1为盟主，0为非盟主
        :type RoleType: int
        :param AgencyDid: 机构DID
        :type AgencyDid: str
        :param CreateOrg: 机构名称
        :type CreateOrg: str
        :param Endpoint: 端点
        :type Endpoint: str
        :param CreateTime: 生成时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param GroupName: 群组名称
        :type GroupName: str
        """
        self.Id = None
        self.Appid = None
        self.Uin = None
        self.ConsortiumId = None
        self.ConsortiumName = None
        self.ClusterId = None
        self.GroupId = None
        self.ChainId = None
        self.RoleType = None
        self.AgencyDid = None
        self.CreateOrg = None
        self.Endpoint = None
        self.CreateTime = None
        self.UpdateTime = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Appid = params.get("Appid")
        self.Uin = params.get("Uin")
        self.ConsortiumId = params.get("ConsortiumId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ChainId = params.get("ChainId")
        self.RoleType = params.get("RoleType")
        self.AgencyDid = params.get("AgencyDid")
        self.CreateOrg = params.get("CreateOrg")
        self.Endpoint = params.get("Endpoint")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownCptRequest(AbstractModel):
    """DownCpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param CptIndex: Cpt索引
        :type CptIndex: int
        """
        self.CptIndex = None


    def _deserialize(self, params):
        self.CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownCptResponse(AbstractModel):
    """DownCpt返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableHashRequest(AbstractModel):
    """EnableHash请求参数结构体

    """

    def __init__(self):
        r"""
        :param Hash: 合约CNS地址
        :type Hash: str
        """
        self.Hash = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableHashResponse(AbstractModel):
    """EnableHash返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        


class GetAgencyTDidRequest(AbstractModel):
    """GetAgencyTDid请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 网络ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAgencyTDidResponse(AbstractModel):
    """GetAgencyTDid返回参数结构体

    """

    def __init__(self):
        r"""
        :param Prefix: 固定前缀
        :type Prefix: str
        :param Identity: did详情
        :type Identity: list of Identity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Prefix = None
        self.Identity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Prefix = params.get("Prefix")
        if params.get("Identity") is not None:
            self.Identity = []
            for item in params.get("Identity"):
                obj = Identity()
                obj._deserialize(item)
                self.Identity.append(obj)
        self.RequestId = params.get("RequestId")


class GetAuthoritiesListRequest(AbstractModel):
    """GetAuthoritiesList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 页码，从1开始
        :type PageNumber: int
        :param PageSize: 每页大小
        :type PageSize: int
        :param Did: Did信息
        :type Did: str
        :param Status: 权威认证 1:已认证，2:未认证
        :type Status: int
        """
        self.PageNumber = None
        self.PageSize = None
        self.Did = None
        self.Status = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.Did = params.get("Did")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthoritiesListResponse(AbstractModel):
    """GetAuthoritiesList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultList: 数据集合
        :type ResultList: list of Authority
        :param AllCount: 总数
        :type AllCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultList") is not None:
            self.ResultList = []
            for item in params.get("ResultList"):
                obj = Authority()
                obj._deserialize(item)
                self.ResultList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetAuthorityIssuerRequest(AbstractModel):
    """GetAuthorityIssuer请求参数结构体

    """

    def __init__(self):
        r"""
        :param Did: tdid
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthorityIssuerResponse(AbstractModel):
    """GetAuthorityIssuer返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param ClusterId: 区块链网络id
        :type ClusterId: str
        :param GroupId: 区块链群组id
        :type GroupId: int
        :param Did: 权威机构did
        :type Did: str
        :param Remark: 机构备注信息
        :type Remark: str
        :param RegisterTime: 注册时间
        :type RegisterTime: str
        :param RecognizeTime: 认证时间
        :type RecognizeTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.ClusterId = None
        self.GroupId = None
        self.Did = None
        self.Remark = None
        self.RegisterTime = None
        self.RecognizeTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.Did = params.get("Did")
        self.Remark = params.get("Remark")
        self.RegisterTime = params.get("RegisterTime")
        self.RecognizeTime = params.get("RecognizeTime")
        self.RequestId = params.get("RequestId")


class GetConsortiumClusterListRequest(AbstractModel):
    """GetConsortiumClusterList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConsortiumId: 联盟id
        :type ConsortiumId: int
        """
        self.ConsortiumId = None


    def _deserialize(self, params):
        self.ConsortiumId = params.get("ConsortiumId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetConsortiumClusterListResponse(AbstractModel):
    """GetConsortiumClusterList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterList: 网络列表
        :type ClusterList: list of BcosClusterItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = BcosClusterItem()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.RequestId = params.get("RequestId")


class GetConsortiumListRequest(AbstractModel):
    """GetConsortiumList请求参数结构体

    """


class GetConsortiumListResponse(AbstractModel):
    """GetConsortiumList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ConsortiumList: 联盟列表
        :type ConsortiumList: list of ConsortiumItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConsortiumList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConsortiumList") is not None:
            self.ConsortiumList = []
            for item in params.get("ConsortiumList"):
                obj = ConsortiumItem()
                obj._deserialize(item)
                self.ConsortiumList.append(obj)
        self.RequestId = params.get("RequestId")


class GetCptInfoRequest(AbstractModel):
    """GetCptInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CptIndex: Cpt索引
        :type CptIndex: int
        """
        self.CptIndex = None


    def _deserialize(self, params):
        self.CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCptInfoResponse(AbstractModel):
    """GetCptInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CptJsonData: CptJsonData的具体信息
        :type CptJsonData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CptJsonData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CptJsonData = params.get("CptJsonData")
        self.RequestId = params.get("RequestId")


class GetCptListRequest(AbstractModel):
    """GetCptList请求参数结构体

    """

    def __init__(self):
        r"""
        :param DisplayStart: 起始位置
        :type DisplayStart: int
        :param DisplayLength: 长度
        :type DisplayLength: int
        :param CptType: 模板类型，0: 所有模板，1: 系统模板，2: 用户模板，3:普通模板
        :type CptType: int
        """
        self.DisplayStart = None
        self.DisplayLength = None
        self.CptType = None


    def _deserialize(self, params):
        self.DisplayStart = params.get("DisplayStart")
        self.DisplayLength = params.get("DisplayLength")
        self.CptType = params.get("CptType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCptListResponse(AbstractModel):
    """GetCptList返回参数结构体

    """

    def __init__(self):
        r"""
        :param CptDataList: cpt数据集合
        :type CptDataList: list of CptListData
        :param AllCount: 凭证模板总数
        :type AllCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CptDataList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CptDataList") is not None:
            self.CptDataList = []
            for item in params.get("CptDataList"):
                obj = CptListData()
                obj._deserialize(item)
                self.CptDataList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetCredentialCptRankRequest(AbstractModel):
    """GetCredentialCptRank请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间（支持到天 2021-4-23）
        :type StartTime: str
        :param EndTime: 结束时间（支持到天 2021-4-23）
        :type EndTime: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialCptRankResponse(AbstractModel):
    """GetCredentialCptRank返回参数结构体

    """

    def __init__(self):
        r"""
        :param RankIssueResult: Rank集合
        :type RankIssueResult: list of CptIssueRank
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RankIssueResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RankIssueResult") is not None:
            self.RankIssueResult = []
            for item in params.get("RankIssueResult"):
                obj = CptIssueRank()
                obj._deserialize(item)
                self.RankIssueResult.append(obj)
        self.RequestId = params.get("RequestId")


class GetCredentialIssueRankRequest(AbstractModel):
    """GetCredentialIssueRank请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间（支持到天 2021-4-23）
        :type StartTime: str
        :param EndTime: 结束时间（支持到天 2021-4-23）
        :type EndTime: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialIssueRankResponse(AbstractModel):
    """GetCredentialIssueRank返回参数结构体

    """

    def __init__(self):
        r"""
        :param RankIssueResult: Rank集合
        :type RankIssueResult: list of CptIssueRank
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RankIssueResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RankIssueResult") is not None:
            self.RankIssueResult = []
            for item in params.get("RankIssueResult"):
                obj = CptIssueRank()
                obj._deserialize(item)
                self.RankIssueResult.append(obj)
        self.RequestId = params.get("RequestId")


class GetCredentialIssueTrendRequest(AbstractModel):
    """GetCredentialIssueTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间（支持到天 2021-4-23）
        :type StartTime: str
        :param EndTime: 结束时间（支持到天 2021-4-23）
        :type EndTime: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialIssueTrendResponse(AbstractModel):
    """GetCredentialIssueTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Trend: Trend集合
        :type Trend: list of Trend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Trend = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trend") is not None:
            self.Trend = []
            for item in params.get("Trend"):
                obj = Trend()
                obj._deserialize(item)
                self.Trend.append(obj)
        self.RequestId = params.get("RequestId")


class GetCredentialStatusRequest(AbstractModel):
    """GetCredentialStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param CredentialId: 凭证id
        :type CredentialId: str
        """
        self.CredentialId = None


    def _deserialize(self, params):
        self.CredentialId = params.get("CredentialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialStatusResponse(AbstractModel):
    """GetCredentialStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param CredentialStatus: 凭证状态信息
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CredentialStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self.CredentialStatus = CredentialStatus()
            self.CredentialStatus._deserialize(params.get("CredentialStatus"))
        self.RequestId = params.get("RequestId")


class GetDataPanelRequest(AbstractModel):
    """GetDataPanel请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 网络ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDataPanelResponse(AbstractModel):
    """GetDataPanel返回参数结构体

    """

    def __init__(self):
        r"""
        :param BlockNetworkCount: 区块链网络数量
        :type BlockNetworkCount: int
        :param BlockNetworkName: 区块链网络名称
        :type BlockNetworkName: str
        :param BlockHeight: 当前区块高度
        :type BlockHeight: int
        :param BlockNetworkType: 区块链网络类型
        :type BlockNetworkType: int
        :param DidCount: did数量
        :type DidCount: int
        :param CptCount: 凭证模版数量
        :type CptCount: int
        :param CertificatedAuthCount: 已认证权威机构数量
        :type CertificatedAuthCount: int
        :param IssueCptCount: 颁发凭证数量
        :type IssueCptCount: int
        :param NewDidCount: 本周新增DID数量
        :type NewDidCount: int
        :param BcosCount: BCOS网络类型数量
        :type BcosCount: int
        :param FabricCount: Fabric网络类型数量
        :type FabricCount: int
        :param ChainMakerCount: 长安链网络类型数量
        :type ChainMakerCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlockNetworkCount = None
        self.BlockNetworkName = None
        self.BlockHeight = None
        self.BlockNetworkType = None
        self.DidCount = None
        self.CptCount = None
        self.CertificatedAuthCount = None
        self.IssueCptCount = None
        self.NewDidCount = None
        self.BcosCount = None
        self.FabricCount = None
        self.ChainMakerCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlockNetworkCount = params.get("BlockNetworkCount")
        self.BlockNetworkName = params.get("BlockNetworkName")
        self.BlockHeight = params.get("BlockHeight")
        self.BlockNetworkType = params.get("BlockNetworkType")
        self.DidCount = params.get("DidCount")
        self.CptCount = params.get("CptCount")
        self.CertificatedAuthCount = params.get("CertificatedAuthCount")
        self.IssueCptCount = params.get("IssueCptCount")
        self.NewDidCount = params.get("NewDidCount")
        self.BcosCount = params.get("BcosCount")
        self.FabricCount = params.get("FabricCount")
        self.ChainMakerCount = params.get("ChainMakerCount")
        self.RequestId = params.get("RequestId")


class GetDeployInfoRequest(AbstractModel):
    """GetDeployInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Hash: 合约CNS地址
        :type Hash: str
        """
        self.Hash = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeployInfoResponse(AbstractModel):
    """GetDeployInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Hash: 合约CNS地址
        :type Hash: str
        :param GroupId: 合约主群组ID
        :type GroupId: str
        :param DeployDid: 部署机构DID
        :type DeployDid: str
        :param SdkVersion: TDID SDK版本
        :type SdkVersion: str
        :param ContractVersion: TDID 合约版本
        :type ContractVersion: str
        :param BlockVersion: 区块链节点版本
        :type BlockVersion: str
        :param BlockIp: 区块链节点IP
        :type BlockIp: str
        :param DidAddress: DID合约地址
        :type DidAddress: str
        :param CptAddress: CPT合约地址
        :type CptAddress: str
        :param AuthorityAddress: Authority Issuer地址
        :type AuthorityAddress: str
        :param EvidenceAddress: Evidence合约地址
        :type EvidenceAddress: str
        :param SpecificAddress: Specific Issuer合约地址
        :type SpecificAddress: str
        :param ChainId: 链ID
        :type ChainId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Hash = None
        self.GroupId = None
        self.DeployDid = None
        self.SdkVersion = None
        self.ContractVersion = None
        self.BlockVersion = None
        self.BlockIp = None
        self.DidAddress = None
        self.CptAddress = None
        self.AuthorityAddress = None
        self.EvidenceAddress = None
        self.SpecificAddress = None
        self.ChainId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        self.GroupId = params.get("GroupId")
        self.DeployDid = params.get("DeployDid")
        self.SdkVersion = params.get("SdkVersion")
        self.ContractVersion = params.get("ContractVersion")
        self.BlockVersion = params.get("BlockVersion")
        self.BlockIp = params.get("BlockIp")
        self.DidAddress = params.get("DidAddress")
        self.CptAddress = params.get("CptAddress")
        self.AuthorityAddress = params.get("AuthorityAddress")
        self.EvidenceAddress = params.get("EvidenceAddress")
        self.SpecificAddress = params.get("SpecificAddress")
        self.ChainId = params.get("ChainId")
        self.RequestId = params.get("RequestId")


class GetDeployListRequest(AbstractModel):
    """GetDeployList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param DisplayStart: 起始位置
        :type DisplayStart: int
        :param DisplayLength: 长度
        :type DisplayLength: int
        """
        self.ClusterId = None
        self.GroupId = None
        self.DisplayStart = None
        self.DisplayLength = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.DisplayStart = params.get("DisplayStart")
        self.DisplayLength = params.get("DisplayLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeployListResponse(AbstractModel):
    """GetDeployList返回参数结构体

    """

    def __init__(self):
        r"""
        :param AllCount: 合约总数
        :type AllCount: int
        :param Result: 合约部署列表
        :type Result: list of Contract
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllCount = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllCount = params.get("AllCount")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Contract()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class GetDidClusterDetailRequest(AbstractModel):
    """GetDidClusterDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: DID网络ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidClusterDetailResponse(AbstractModel):
    """GetDidClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param ConsortiumName: 组织名称
        :type ConsortiumName: str
        :param ChainAgency: 区块链组织名称
        :type ChainAgency: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.ConsortiumName = None
        self.ChainAgency = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.ChainAgency = params.get("ChainAgency")
        self.RequestId = params.get("RequestId")


class GetDidClusterListRequest(AbstractModel):
    """GetDidClusterList请求参数结构体

    """


class GetDidClusterListResponse(AbstractModel):
    """GetDidClusterList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DidClusterList: DID网络列表
        :type DidClusterList: list of DidCluster
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DidClusterList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DidClusterList") is not None:
            self.DidClusterList = []
            for item in params.get("DidClusterList"):
                obj = DidCluster()
                obj._deserialize(item)
                self.DidClusterList.append(obj)
        self.RequestId = params.get("RequestId")


class GetDidDetailRequest(AbstractModel):
    """GetDidDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Did: DID号码的具体信息
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidDetailResponse(AbstractModel):
    """GetDidDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Did: DID名称
        :type Did: str
        :param Remark: 备注
        :type Remark: str
        :param PublicKey: 公钥
        :type PublicKey: str
        :param AuthorityState: 权威认证
        :type AuthorityState: int
        :param ConsortiumId: 联盟ID
        :type ConsortiumId: int
        :param ConsortiumName: 联盟名称
        :type ConsortiumName: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param ResChainId: bcos资源ID
        :type ResChainId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Did = None
        self.Remark = None
        self.PublicKey = None
        self.AuthorityState = None
        self.ConsortiumId = None
        self.ConsortiumName = None
        self.GroupId = None
        self.ClusterId = None
        self.ResChainId = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.Remark = params.get("Remark")
        self.PublicKey = params.get("PublicKey")
        self.AuthorityState = params.get("AuthorityState")
        self.ConsortiumId = params.get("ConsortiumId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.ResChainId = params.get("ResChainId")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class GetDidDocumentRequest(AbstractModel):
    """GetDidDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param Did: tdid
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidDocumentResponse(AbstractModel):
    """GetDidDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Document: DID文档
        :type Document: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Document = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Document = params.get("Document")
        self.RequestId = params.get("RequestId")


class GetDidListRequest(AbstractModel):
    """GetDidList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 每页大小
        :type PageSize: int
        :param PageNumber: 页码，从1开始
        :type PageNumber: int
        :param Did: Did信息
        :type Did: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        """
        self.PageSize = None
        self.PageNumber = None
        self.Did = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.Did = params.get("Did")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidListResponse(AbstractModel):
    """GetDidList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataList: 数据列表
        :type DataList: list of DidData
        :param AllCount: 数据总条数
        :type AllCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = DidData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetDidRegisterTrendRequest(AbstractModel):
    """GetDidRegisterTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间（支持到天 2021-4-23）
        :type StartTime: str
        :param EndTime: 结束时间（支持到天 2021-4-23）
        :type EndTime: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidRegisterTrendResponse(AbstractModel):
    """GetDidRegisterTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Trend: Trend集合
        :type Trend: list of Trend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Trend = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trend") is not None:
            self.Trend = []
            for item in params.get("Trend"):
                obj = Trend()
                obj._deserialize(item)
                self.Trend.append(obj)
        self.RequestId = params.get("RequestId")


class GetDidServiceDetailRequest(AbstractModel):
    """GetDidServiceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: DID服务ID
        :type ServiceId: int
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidServiceDetailResponse(AbstractModel):
    """GetDidServiceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param DidService: did服务信息
        :type DidService: :class:`tencentcloud.tdid.v20210519.models.DidServiceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DidService = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DidService") is not None:
            self.DidService = DidServiceInfo()
            self.DidService._deserialize(params.get("DidService"))
        self.RequestId = params.get("RequestId")


class GetDidServiceListRequest(AbstractModel):
    """GetDidServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 1: 以网络维度输出, 0: 以服务维度输出
        :type Type: int
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidServiceListResponse(AbstractModel):
    """GetDidServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DidServiceList: DID服务列表
        :type DidServiceList: list of DidServiceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DidServiceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DidServiceList") is not None:
            self.DidServiceList = []
            for item in params.get("DidServiceList"):
                obj = DidServiceInfo()
                obj._deserialize(item)
                self.DidServiceList.append(obj)
        self.RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 0为未部署DID服务的群组，1为已部署DID服务的群组
        :type Status: int
        :param ClusterId: 网络ID
        :type ClusterId: str
        """
        self.Status = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 群组数据集合
        :type Result: list of Group
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Group()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class GetLabelListRequest(AbstractModel):
    """GetLabelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 每页大小
        :type PageSize: int
        :param PageNumber: 页码，从1开始
        :type PageNumber: int
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        """
        self.PageSize = None
        self.PageNumber = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLabelListResponse(AbstractModel):
    """GetLabelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 数据集合
        :type Result: list of Label
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Label()
                obj._deserialize(item)
                self.Result.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GetPolicyListRequest(AbstractModel):
    """GetPolicyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param DisplayStart: 起始位置
        :type DisplayStart: int
        :param DisplayLength: 长度
        :type DisplayLength: int
        """
        self.DisplayStart = None
        self.DisplayLength = None


    def _deserialize(self, params):
        self.DisplayStart = params.get("DisplayStart")
        self.DisplayLength = params.get("DisplayLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyListResponse(AbstractModel):
    """GetPolicyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyDataList: 策略Policy管理列表
        :type PolicyDataList: list of Policy
        :param AllCount: 总数
        :type AllCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyDataList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyDataList") is not None:
            self.PolicyDataList = []
            for item in params.get("PolicyDataList"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicyDataList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param Did: did的具体号码
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Did: DID的具体信息
        :type Did: str
        :param PublicKey: 公钥
        :type PublicKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Did = None
        self.PublicKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.PublicKey = params.get("PublicKey")
        self.RequestId = params.get("RequestId")


class Group(AbstractModel):
    """群组

    """

    def __init__(self):
        r"""
        :param GroupId: 群组ID
        :type GroupId: int
        :param NodeCount: 节点数量
        :type NodeCount: int
        :param NodeCountOfAgency: 所属机构节点数量
        :type NodeCountOfAgency: int
        :param Description: 群组描述
        :type Description: str
        :param RoleType: 参与角色，盟主或非盟主
        :type RoleType: int
        :param ChainId: 链id
        :type ChainId: str
        """
        self.GroupId = None
        self.NodeCount = None
        self.NodeCountOfAgency = None
        self.Description = None
        self.RoleType = None
        self.ChainId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.NodeCount = params.get("NodeCount")
        self.NodeCountOfAgency = params.get("NodeCountOfAgency")
        self.Description = params.get("Description")
        self.RoleType = params.get("RoleType")
        self.ChainId = params.get("ChainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identity(AbstractModel):
    """did详情

    """

    def __init__(self):
        r"""
        :param AccountIdentifier: 账户标识符
        :type AccountIdentifier: str
        :param ChainID: 链ID
        :type ChainID: str
        :param Did: 完整tdid
        :type Did: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param GroupName: 群组名称
        :type GroupName: str
        """
        self.AccountIdentifier = None
        self.ChainID = None
        self.Did = None
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.AccountIdentifier = params.get("AccountIdentifier")
        self.ChainID = params.get("ChainID")
        self.Did = params.get("Did")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param LabelId: 标签ID
        :type LabelId: int
        :param LabelName: 标签名称
        :type LabelName: str
        :param DidCount: did数量
        :type DidCount: int
        :param Did: 创建者did
        :type Did: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param GroupId: 群组ID
        :type GroupId: int
        """
        self.LabelId = None
        self.LabelName = None
        self.DidCount = None
        self.Did = None
        self.ClusterId = None
        self.CreateTime = None
        self.GroupId = None


    def _deserialize(self, params):
        self.LabelId = params.get("LabelId")
        self.LabelName = params.get("LabelName")
        self.DidCount = params.get("DidCount")
        self.Did = params.get("Did")
        self.ClusterId = params.get("ClusterId")
        self.CreateTime = params.get("CreateTime")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """策略管理

    """

    def __init__(self):
        r"""
        :param Id: 披露策略索引
        :type Id: int
        :param Name: 披露策略名称
        :type Name: str
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param ServiceId: 服务ID
        :type ServiceId: int
        :param ContractAppId: 合约应用ID
        :type ContractAppId: int
        :param PolicyId: 披露策略ID
        :type PolicyId: int
        :param CptId: 凭证模板ID
        :type CptId: int
        :param PolicyJson: 策略Json
        :type PolicyJson: str
        :param CreateTime: 生成时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreatorDid: 创建者DID
        :type CreatorDid: str
        :param AppName: 应用名称
        :type AppName: str
        :param CptIndex: 模板索引
        :type CptIndex: int
        """
        self.Id = None
        self.Name = None
        self.ClusterId = None
        self.GroupId = None
        self.ServiceId = None
        self.ContractAppId = None
        self.PolicyId = None
        self.CptId = None
        self.PolicyJson = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CreatorDid = None
        self.AppName = None
        self.CptIndex = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ServiceId = params.get("ServiceId")
        self.ContractAppId = params.get("ContractAppId")
        self.PolicyId = params.get("PolicyId")
        self.CptId = params.get("CptId")
        self.PolicyJson = params.get("PolicyJson")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CreatorDid = params.get("CreatorDid")
        self.AppName = params.get("AppName")
        self.CptIndex = params.get("CptIndex")
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
        


class QueryPolicyRequest(AbstractModel):
    """QueryPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyIndex: policy索引
        :type PolicyIndex: int
        """
        self.PolicyIndex = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPolicyResponse(AbstractModel):
    """QueryPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 披露策略索引
        :type Id: int
        :param PolicyId: 披露策略ID
        :type PolicyId: int
        :param CptId: 凭证模板ID
        :type CptId: int
        :param PolicyData: 披露策略的具体信息
        :type PolicyData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.PolicyId = None
        self.CptId = None
        self.PolicyData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.CptId = params.get("CptId")
        self.PolicyData = params.get("PolicyData")
        self.RequestId = params.get("RequestId")


class RecognizeAuthorityIssuerRequest(AbstractModel):
    """RecognizeAuthorityIssuer请求参数结构体

    """

    def __init__(self):
        r"""
        :param Did: did具体信息
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeAuthorityIssuerResponse(AbstractModel):
    """RecognizeAuthorityIssuer返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterClaimPolicyRequest(AbstractModel):
    """RegisterClaimPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param CptIndex: Cpt索引
        :type CptIndex: int
        :param Policy: 披露策略
        :type Policy: str
        """
        self.CptIndex = None
        self.Policy = None


    def _deserialize(self, params):
        self.CptIndex = params.get("CptIndex")
        self.Policy = params.get("Policy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterClaimPolicyResponse(AbstractModel):
    """RegisterClaimPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 披露策略索引
        :type Id: int
        :param PolicyId: 披露策略ID
        :type PolicyId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class RegisterCptRequest(AbstractModel):
    """RegisterCpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 群组ID
        :type GroupId: int
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param CptJson: CptJson的具体信息
        :type CptJson: str
        :param CptId: cptId 不填默认自增
        :type CptId: int
        """
        self.GroupId = None
        self.ClusterId = None
        self.CptJson = None
        self.CptId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.CptJson = params.get("CptJson")
        self.CptId = params.get("CptId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCptResponse(AbstractModel):
    """RegisterCpt返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 凭证模板索引
        :type Id: int
        :param CptId: 凭证模板id
        :type CptId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.CptId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CptId = params.get("CptId")
        self.RequestId = params.get("RequestId")


class RegisterIssuerRequest(AbstractModel):
    """RegisterIssuer请求参数结构体

    """

    def __init__(self):
        r"""
        :param Did: tdid
        :type Did: str
        :param Name: 权威机构名称
        :type Name: str
        :param Description: 备注
        :type Description: str
        """
        self.Did = None
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterIssuerResponse(AbstractModel):
    """RegisterIssuer返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveHashRequest(AbstractModel):
    """RemoveHash请求参数结构体

    """

    def __init__(self):
        r"""
        :param Hash: 合约CNS地址
        :type Hash: str
        """
        self.Hash = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveHashResponse(AbstractModel):
    """RemoveHash返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetCredentialStatusRequest(AbstractModel):
    """SetCredentialStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param CredentialStatus: 凭证状态
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        """
        self.CredentialStatus = None


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self.CredentialStatus = CredentialStatus()
            self.CredentialStatus._deserialize(params.get("CredentialStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCredentialStatusResponse(AbstractModel):
    """SetCredentialStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Task(AbstractModel):
    """CreateDidService、CheckDidDeploy出参

    """

    def __init__(self):
        r"""
        :param Id: 任务ID
        :type Id: int
        :param AppId: 应用ID
        :type AppId: int
        :param ClusterId: 网络ID
        :type ClusterId: str
        :param GroupId: 群组ID
        :type GroupId: int
        :param ServiceId: 服务ID
        :type ServiceId: int
        :param Status: 0: 部署中，1:部署成功，其他失败
        :type Status: int
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param ErrorMsg: 错误提示
        :type ErrorMsg: str
        :param CreateTime: 生成时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.AppId = None
        self.ClusterId = None
        self.GroupId = None
        self.ServiceId = None
        self.Status = None
        self.ErrorCode = None
        self.ErrorMsg = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ServiceId = params.get("ServiceId")
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
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
        


class Trend(AbstractModel):
    """趋势

    """

    def __init__(self):
        r"""
        :param Time: 时间点
        :type Time: str
        :param Count: 数量
        :type Count: int
        """
        self.Time = None
        self.Count = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Count = params.get("Count")
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
        