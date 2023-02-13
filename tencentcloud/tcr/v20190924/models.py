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


class AccessVpc(AbstractModel):
    """内网接入信息

    """

    def __init__(self):
        r"""
        :param VpcId: Vpc的Id
        :type VpcId: str
        :param SubnetId: 子网Id
        :type SubnetId: str
        :param Status: 内网接入状态
        :type Status: str
        :param AccessIp: 内网接入Ip
        :type AccessIp: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.AccessIp = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.AccessIp = params.get("AccessIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoDelStrategyInfo(AbstractModel):
    """自动删除策略信息

    """

    def __init__(self):
        r"""
        :param Username: 用户名
        :type Username: str
        :param RepoName: 仓库名
        :type RepoName: str
        :param Type: 类型
        :type Type: str
        :param Value: 策略值
        :type Value: int
        :param Valid: Valid
        :type Valid: int
        :param CreationTime: 创建时间
        :type CreationTime: str
        """
        self.Username = None
        self.RepoName = None
        self.Type = None
        self.Value = None
        self.Valid = None
        self.CreationTime = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.RepoName = params.get("RepoName")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        self.Valid = params.get("Valid")
        self.CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoDelStrategyInfoResp(AbstractModel):
    """获取自动删除策略

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数目
        :type TotalCount: int
        :param StrategyInfo: 自动删除策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyInfo: list of AutoDelStrategyInfo
        """
        self.TotalCount = None
        self.StrategyInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("StrategyInfo") is not None:
            self.StrategyInfo = []
            for item in params.get("StrategyInfo"):
                obj = AutoDelStrategyInfo()
                obj._deserialize(item)
                self.StrategyInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteImagePersonalRequest(AbstractModel):
    """BatchDeleteImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Tags: Tag列表
        :type Tags: list of str
        """
        self.RepoName = None
        self.Tags = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteImagePersonalResponse(AbstractModel):
    """BatchDeleteImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchDeleteRepositoryPersonalRequest(AbstractModel):
    """BatchDeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoNames: 仓库名称数组
        :type RepoNames: list of str
        """
        self.RepoNames = None


    def _deserialize(self, params):
        self.RepoNames = params.get("RepoNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteRepositoryPersonalResponse(AbstractModel):
    """BatchDeleteRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CVEWhitelistItem(AbstractModel):
    """命名空间漏洞白名单列表

    """

    def __init__(self):
        r"""
        :param CVEID: 漏洞白名单 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CVEID: str
        """
        self.CVEID = None


    def _deserialize(self, params):
        self.CVEID = params.get("CVEID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameRequest(AbstractModel):
    """CheckInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryName: 待创建的实例名称
        :type RegistryName: str
        """
        self.RegistryName = None


    def _deserialize(self, params):
        self.RegistryName = params.get("RegistryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceNameResponse(AbstractModel):
    """CheckInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsValidated: 检查结果，true为合法，false为非法
        :type IsValidated: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsValidated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValidated = params.get("IsValidated")
        self.RequestId = params.get("RequestId")


class CheckInstanceRequest(AbstractModel):
    """CheckInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 待检测的实例Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstanceResponse(AbstractModel):
    """CheckInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsValidated: 检查结果，true为合法，false为非法
        :type IsValidated: bool
        :param RegionId: 实例所在的RegionId
        :type RegionId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsValidated = None
        self.RegionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValidated = params.get("IsValidated")
        self.RegionId = params.get("RegionId")
        self.RequestId = params.get("RequestId")


class CreateApplicationTriggerPersonalRequest(AbstractModel):
    """CreateApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 触发器关联的镜像仓库，library/test格式
        :type RepoName: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发
        :type InvokeMethod: str
        :param ClusterId: 应用所在TKE集群ID
        :type ClusterId: str
        :param Namespace: 应用所在TKE集群命名空间
        :type Namespace: str
        :param WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param WorkloadName: 应用所在TKE集群工作负载名称
        :type WorkloadName: str
        :param ContainerName: 应用所在TKE集群工作负载下容器名称
        :type ContainerName: str
        :param ClusterRegion: 应用所在TKE集群地域
        :type ClusterRegion: int
        :param InvokeExpr: 触发方式对应的表达式
        :type InvokeExpr: str
        """
        self.RepoName = None
        self.TriggerName = None
        self.InvokeMethod = None
        self.ClusterId = None
        self.Namespace = None
        self.WorkloadType = None
        self.WorkloadName = None
        self.ContainerName = None
        self.ClusterRegion = None
        self.InvokeExpr = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeMethod = params.get("InvokeMethod")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.WorkloadType = params.get("WorkloadType")
        self.WorkloadName = params.get("WorkloadName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")
        self.InvokeExpr = params.get("InvokeExpr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationTriggerPersonalResponse(AbstractModel):
    """CreateApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateImageAccelerationServiceRequest(AbstractModel):
    """CreateImageAccelerationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param VpcId: 创建CFS的归属的VPCID
        :type VpcId: str
        :param SubnetId: 创建CFS的归属的子网ID
        :type SubnetId: str
        :param StorageType: 创建CFS的存储类型，其中 SD 为标准型存储， HP为性能存储。
        :type StorageType: str
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param Zone: 可用区名称，例如ap-beijing-1，请参考 概览 文档中的地域与可用区列表
        :type Zone: str
        :param TagSpecification: 云标签描述
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        """
        self.RegistryId = None
        self.VpcId = None
        self.SubnetId = None
        self.StorageType = None
        self.PGroupId = None
        self.Zone = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.StorageType = params.get("StorageType")
        self.PGroupId = params.get("PGroupId")
        self.Zone = params.get("Zone")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageAccelerationServiceResponse(AbstractModel):
    """CreateImageAccelerationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateImageLifecyclePersonalRequest(AbstractModel):
    """CreateImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Type: keep_last_days:保留最近几天的数据;keep_last_nums:保留最近多少个
        :type Type: str
        :param Val: 策略值
        :type Val: int
        """
        self.RepoName = None
        self.Type = None
        self.Val = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Type = params.get("Type")
        self.Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageLifecyclePersonalResponse(AbstractModel):
    """CreateImageLifecyclePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateImmutableTagRulesRequest(AbstractModel):
    """CreateImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param NamespaceName: 命名空间
        :type NamespaceName: str
        :param Rule: 规则
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Rule = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        if params.get("Rule") is not None:
            self.Rule = ImmutableTagRule()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImmutableTagRulesResponse(AbstractModel):
    """CreateImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceCustomizedDomainRequest(AbstractModel):
    """CreateInstanceCustomizedDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param DomainName: 自定义域名
        :type DomainName: str
        :param CertificateId: 证书ID
        :type CertificateId: str
        """
        self.RegistryId = None
        self.DomainName = None
        self.CertificateId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.DomainName = params.get("DomainName")
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceCustomizedDomainResponse(AbstractModel):
    """CreateInstanceCustomizedDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryName: 企业版实例名称
        :type RegistryName: str
        :param RegistryType: 企业版实例类型（basic 基础版；standard 标准版；premium 高级版）
        :type RegistryType: str
        :param TagSpecification: 云标签描述
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param RegistryChargeType: 实例计费类型，0表示按量计费，1表示预付费，默认为按量计费
        :type RegistryChargeType: int
        :param RegistryChargePrepaid: 预付费自动续费标识和购买时长
        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`
        :param SyncTag: 是否同步TCR云标签至生成的COS Bucket
        :type SyncTag: bool
        """
        self.RegistryName = None
        self.RegistryType = None
        self.TagSpecification = None
        self.RegistryChargeType = None
        self.RegistryChargePrepaid = None
        self.SyncTag = None


    def _deserialize(self, params):
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        self.RegistryChargeType = params.get("RegistryChargeType")
        if params.get("RegistryChargePrepaid") is not None:
            self.RegistryChargePrepaid = RegistryChargePrepaid()
            self.RegistryChargePrepaid._deserialize(params.get("RegistryChargePrepaid"))
        self.SyncTag = params.get("SyncTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 企业版实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param TokenType: 访问凭证类型，longterm 为长期访问凭证，temp 为临时访问凭证，默认是临时访问凭证，有效期1小时
        :type TokenType: str
        :param Desc: 长期访问凭证描述信息
        :type Desc: str
        """
        self.RegistryId = None
        self.TokenType = None
        self.Desc = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenType = params.get("TokenType")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceTokenResponse(AbstractModel):
    """CreateInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Username: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param Token: 访问凭证
        :type Token: str
        :param ExpTime: 访问凭证过期时间戳，是一个时间戳数字，无单位
        :type ExpTime: int
        :param TokenId: 长期凭证的TokenId，短期凭证没有TokenId
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Username = None
        self.Token = None
        self.ExpTime = None
        self.TokenId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Token = params.get("Token")
        self.ExpTime = params.get("ExpTime")
        self.TokenId = params.get("TokenId")
        self.RequestId = params.get("RequestId")


class CreateInternalEndpointDnsRequest(AbstractModel):
    """CreateInternalEndpointDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: tcr实例id
        :type InstanceId: str
        :param VpcId: 私有网络id
        :type VpcId: str
        :param EniLBIp: tcr内网访问链路ip
        :type EniLBIp: str
        :param UsePublicDomain: true：为默认域名，公网域名一致
false: 使用vpc域名
默认为vpc域名
        :type UsePublicDomain: bool
        :param RegionName: 解析地域，需要保证和vpc处于同一地域，如果不填则默认为主实例地域
        :type RegionName: str
        :param RegionId: 请求的地域ID，用于实例复制地域
        :type RegionId: int
        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.UsePublicDomain = None
        self.RegionName = None
        self.RegionId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.EniLBIp = params.get("EniLBIp")
        self.UsePublicDomain = params.get("UsePublicDomain")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInternalEndpointDnsResponse(AbstractModel):
    """CreateInternalEndpointDns返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMultipleSecurityPolicyRequest(AbstractModel):
    """CreateMultipleSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param SecurityGroupPolicySet: 安全组策略
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self.RegistryId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultipleSecurityPolicyResponse(AbstractModel):
    """CreateMultipleSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateNamespacePersonalRequest(AbstractModel):
    """CreateNamespacePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespacePersonalResponse(AbstractModel):
    """CreateNamespacePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称（长度2-30个字符，只能包含小写字母、数字及分隔符("."、"_"、"-")，且不能以分隔符开头、结尾或连续）
        :type NamespaceName: str
        :param IsPublic: 是否公开，true为公开，fale为私有
        :type IsPublic: bool
        :param TagSpecification: 云标签描述
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param IsAutoScan: 自动扫描级别，true为自动，false为手动
        :type IsAutoScan: bool
        :param IsPreventVUL: 安全阻断级别，true为自动，false为手动
        :type IsPreventVUL: bool
        :param Severity: 阻断漏洞等级，目前仅支持low、medium、high
        :type Severity: str
        :param CVEWhitelistItems: 漏洞白名单列表
        :type CVEWhitelistItems: list of CVEWhitelistItem
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None
        self.TagSpecification = None
        self.IsAutoScan = None
        self.IsPreventVUL = None
        self.Severity = None
        self.CVEWhitelistItems = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        self.IsAutoScan = params.get("IsAutoScan")
        self.IsPreventVUL = params.get("IsPreventVUL")
        self.Severity = params.get("Severity")
        if params.get("CVEWhitelistItems") is not None:
            self.CVEWhitelistItems = []
            for item in params.get("CVEWhitelistItems"):
                obj = CVEWhitelistItem()
                obj._deserialize(item)
                self.CVEWhitelistItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateReplicationInstanceRequest(AbstractModel):
    """CreateReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param ReplicationRegionId: 复制实例地域ID
        :type ReplicationRegionId: int
        :param ReplicationRegionName: 复制实例地域名称
        :type ReplicationRegionName: str
        :param SyncTag: 是否同步TCR云标签至生成的COS Bucket
        :type SyncTag: bool
        """
        self.RegistryId = None
        self.ReplicationRegionId = None
        self.ReplicationRegionName = None
        self.SyncTag = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ReplicationRegionName = params.get("ReplicationRegionName")
        self.SyncTag = params.get("SyncTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplicationInstanceResponse(AbstractModel):
    """CreateReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReplicationRegistryId: 企业版复制实例Id
        :type ReplicationRegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReplicationRegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.RequestId = params.get("RequestId")


class CreateRepositoryPersonalRequest(AbstractModel):
    """CreateRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Public: 是否公共,1:公共,0:私有
        :type Public: int
        :param Description: 仓库描述
        :type Description: str
        """
        self.RepoName = None
        self.Public = None
        self.Description = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Public = params.get("Public")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRepositoryPersonalResponse(AbstractModel):
    """CreateRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 仓库名称
        :type RepositoryName: str
        :param BriefDescription: 仓库简短描述
        :type BriefDescription: str
        :param Description: 仓库详细描述
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param CidrBlock: 192.168.0.0/24
        :type CidrBlock: str
        :param Description: 备注
        :type Description: str
        """
        self.RegistryId = None
        self.CidrBlock = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.CidrBlock = params.get("CidrBlock")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateSignaturePolicyRequest(AbstractModel):
    """CreateSignaturePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param Name: 策略名称
        :type Name: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param KmsId: KMS 密钥
        :type KmsId: str
        :param KmsRegion: KMS 密钥所属地域
        :type KmsRegion: str
        :param Domain: 用户自定义域名，为空时使用 TCR 实例默认域名生成签名
        :type Domain: str
        :param Disabled: 禁用加签策略，默认为 false
        :type Disabled: bool
        """
        self.RegistryId = None
        self.Name = None
        self.NamespaceName = None
        self.KmsId = None
        self.KmsRegion = None
        self.Domain = None
        self.Disabled = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Name = params.get("Name")
        self.NamespaceName = params.get("NamespaceName")
        self.KmsId = params.get("KmsId")
        self.KmsRegion = params.get("KmsRegion")
        self.Domain = params.get("Domain")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignaturePolicyResponse(AbstractModel):
    """CreateSignaturePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSignatureRequest(AbstractModel):
    """CreateSignature请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 仓库名称
        :type RepositoryName: str
        :param ImageVersion: Tag名称
        :type ImageVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignatureResponse(AbstractModel):
    """CreateSignature返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRetentionExecutionRequest(AbstractModel):
    """CreateTagRetentionExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param RetentionId: 版本保留规则Id
        :type RetentionId: int
        :param DryRun: 是否模拟执行，默认值为false，即非模拟执行
        :type DryRun: bool
        """
        self.RegistryId = None
        self.RetentionId = None
        self.DryRun = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionExecutionResponse(AbstractModel):
    """CreateTagRetentionExecution返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRetentionRuleRequest(AbstractModel):
    """CreateTagRetentionRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param NamespaceId: 命名空间的Id
        :type NamespaceId: int
        :param RetentionRule: 保留策略
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param CronSetting: 执行周期，当前只能选择： manual;daily;weekly;monthly
        :type CronSetting: str
        :param Disabled: 是否禁用规则，默认值为false
        :type Disabled: bool
        """
        self.RegistryId = None
        self.NamespaceId = None
        self.RetentionRule = None
        self.CronSetting = None
        self.Disabled = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self.RetentionRule = RetentionRule()
            self.RetentionRule._deserialize(params.get("RetentionRule"))
        self.CronSetting = params.get("CronSetting")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagRetentionRuleResponse(AbstractModel):
    """CreateTagRetentionRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUserPersonalRequest(AbstractModel):
    """CreateUserPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Password: 用户密码，密码必须为8到16位
        :type Password: str
        """
        self.Password = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserPersonalResponse(AbstractModel):
    """CreateUserPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param Trigger: 触发器参数
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWebhookTriggerResponse(AbstractModel):
    """CreateWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param Trigger: 新建的触发器
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Trigger = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.RequestId = params.get("RequestId")


class CustomizedDomainInfo(AbstractModel):
    """自定义域名信息

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param CertId: 证书ID
        :type CertId: str
        :param DomainName: 域名名称
        :type DomainName: str
        :param Status: 域名创建状态（SUCCESS, FAILURE, CREATING, DELETING）
        :type Status: str
        """
        self.RegistryId = None
        self.CertId = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.CertId = params.get("CertId")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationTriggerPersonalRequest(AbstractModel):
    """DeleteApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param TriggerName: 触发器名称
        :type TriggerName: str
        """
        self.TriggerName = None


    def _deserialize(self, params):
        self.TriggerName = params.get("TriggerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationTriggerPersonalResponse(AbstractModel):
    """DeleteApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageAccelerateServiceRequest(AbstractModel):
    """DeleteImageAccelerateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageAccelerateServiceResponse(AbstractModel):
    """DeleteImageAccelerateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal请求参数结构体

    """


class DeleteImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageLifecyclePersonalRequest(AbstractModel):
    """DeleteImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageLifecyclePersonalResponse(AbstractModel):
    """DeleteImageLifecyclePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImagePersonalRequest(AbstractModel):
    """DeleteImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Tag: Tag名
        :type Tag: str
        """
        self.RepoName = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagePersonalResponse(AbstractModel):
    """DeleteImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param ImageVersion: 镜像版本
        :type ImageVersion: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.RepositoryName = None
        self.ImageVersion = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        self.NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImmutableTagRulesRequest(AbstractModel):
    """DeleteImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param NamespaceName: 命名空间
        :type NamespaceName: str
        :param RuleId: 规则 Id
        :type RuleId: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RuleId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImmutableTagRulesResponse(AbstractModel):
    """DeleteImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceCustomizedDomainRequest(AbstractModel):
    """DeleteInstanceCustomizedDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param DomainName: 自定义域名
        :type DomainName: str
        :param CertificateId: 证书ID
        :type CertificateId: str
        """
        self.RegistryId = None
        self.DomainName = None
        self.CertificateId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.DomainName = params.get("DomainName")
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceCustomizedDomainResponse(AbstractModel):
    """DeleteInstanceCustomizedDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例id
        :type RegistryId: str
        :param DeleteBucket: 是否删除存储桶，默认为false
        :type DeleteBucket: bool
        :param DryRun: 是否dryRun模式，缺省值：false
        :type DryRun: bool
        """
        self.RegistryId = None
        self.DeleteBucket = None
        self.DryRun = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.DeleteBucket = params.get("DeleteBucket")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 ID
        :type RegistryId: str
        :param TokenId: 访问凭证 ID
        :type TokenId: str
        """
        self.RegistryId = None
        self.TokenId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenId = params.get("TokenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceTokenResponse(AbstractModel):
    """DeleteInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInternalEndpointDnsRequest(AbstractModel):
    """DeleteInternalEndpointDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: tcr实例id
        :type InstanceId: str
        :param VpcId: 私有网络id
        :type VpcId: str
        :param EniLBIp: tcr内网访问链路ip
        :type EniLBIp: str
        :param UsePublicDomain: true：使用默认域名
false:  使用带有vpc的域名
        :type UsePublicDomain: bool
        :param RegionName: 解析地域，需要保证和vpc处于同一地域，如果不填则默认为主实例地域
        :type RegionName: str
        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.UsePublicDomain = None
        self.RegionName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.EniLBIp = params.get("EniLBIp")
        self.UsePublicDomain = params.get("UsePublicDomain")
        self.RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInternalEndpointDnsResponse(AbstractModel):
    """DeleteInternalEndpointDns返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMultipleSecurityPolicyRequest(AbstractModel):
    """DeleteMultipleSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param SecurityGroupPolicySet: 安全组策略
        :type SecurityGroupPolicySet: list of SecurityPolicy
        """
        self.RegistryId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = []
            for item in params.get("SecurityGroupPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityGroupPolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMultipleSecurityPolicyResponse(AbstractModel):
    """DeleteMultipleSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DeleteNamespacePersonalRequest(AbstractModel):
    """DeleteNamespacePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespacePersonalResponse(AbstractModel):
    """DeleteNamespacePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReplicationInstanceRequest(AbstractModel):
    """DeleteReplicationInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例id
        :type RegistryId: str
        :param ReplicationRegistryId: 复制实例ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: 复制实例地域Id
        :type ReplicationRegionId: int
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReplicationInstanceResponse(AbstractModel):
    """DeleteReplicationInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryPersonalRequest(AbstractModel):
    """DeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryPersonalResponse(AbstractModel):
    """DeleteRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param RepositoryName: 镜像仓库的名称
        :type RepositoryName: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryTagsRequest(AbstractModel):
    """DeleteRepositoryTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 仓库名称
        :type RepositoryName: str
        :param Tags: Tag列表，单次请求Tag数量最大为20
        :type Tags: list of str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.Tags = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryTagsResponse(AbstractModel):
    """DeleteRepositoryTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param PolicyIndex: 白名单Id
        :type PolicyIndex: int
        :param PolicyVersion: 白名单版本
        :type PolicyVersion: str
        """
        self.RegistryId = None
        self.PolicyIndex = None
        self.PolicyVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.PolicyIndex = params.get("PolicyIndex")
        self.PolicyVersion = params.get("PolicyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DeleteSignaturePolicyRequest(AbstractModel):
    """DeleteSignaturePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSignaturePolicyResponse(AbstractModel):
    """DeleteSignaturePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagRetentionRuleRequest(AbstractModel):
    """DeleteTagRetentionRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param RetentionId: 版本保留规则的Id
        :type RetentionId: int
        """
        self.RegistryId = None
        self.RetentionId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagRetentionRuleResponse(AbstractModel):
    """DeleteTagRetentionRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Id: 触发器 Id
        :type Id: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWebhookTriggerResponse(AbstractModel):
    """DeleteWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeApplicationTriggerLogPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerLogPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param Order: 升序或降序
        :type Order: str
        :param OrderBy: 按某列排序
        :type OrderBy: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerLogPersonalResp(AbstractModel):
    """查询应用更新触发器触发日志返回值

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回总数
        :type TotalCount: int
        :param LogInfo: 触发日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogInfo: list of TriggerLogResp
        """
        self.TotalCount = None
        self.LogInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LogInfo") is not None:
            self.LogInfo = []
            for item in params.get("LogInfo"):
                obj = TriggerLogResp()
                obj._deserialize(item)
                self.LogInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerLogPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerLogPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 触发日志返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeApplicationTriggerLogPersonalResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationTriggerPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        """
        self.RepoName = None
        self.TriggerName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerPersonalResp(AbstractModel):
    """拉取触发器列表返回值

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回条目总数
        :type TotalCount: int
        :param TriggerInfo: 触发器列表
        :type TriggerInfo: list of TriggerResp
        """
        self.TotalCount = None
        self.TriggerInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TriggerInfo") is not None:
            self.TriggerInfo = []
            for item in params.get("TriggerInfo"):
                obj = TriggerResp()
                obj._deserialize(item)
                self.TriggerInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationTriggerPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 触发器列表返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeApplicationTriggerPersonalResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeChartDownloadInfoRequest(AbstractModel):
    """DescribeChartDownloadInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间
        :type NamespaceName: str
        :param ChartName: Chart包的名称
        :type ChartName: str
        :param ChartVersion: Chart包的版本
        :type ChartVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.ChartName = None
        self.ChartVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.ChartName = params.get("ChartName")
        self.ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChartDownloadInfoResponse(AbstractModel):
    """DescribeChartDownloadInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param PreSignedDownloadURL: 用于下载的url的预签名地址
        :type PreSignedDownloadURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PreSignedDownloadURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedDownloadURL = params.get("PreSignedDownloadURL")
        self.RequestId = params.get("RequestId")


class DescribeExternalEndpointStatusRequest(AbstractModel):
    """DescribeExternalEndpointStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalEndpointStatusResponse(AbstractModel):
    """DescribeExternalEndpointStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 开启公网访问状态，开启中（Opening）、已开启（Opened）、关闭（Closed）
        :type Status: str
        :param Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Reason = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.RequestId = params.get("RequestId")


class DescribeFavorRepositoryPersonalRequest(AbstractModel):
    """DescribeFavorRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Limit: 分页Limit
        :type Limit: int
        :param Offset: Offset用于分页
        :type Offset: int
        """
        self.RepoName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFavorRepositoryPersonalResponse(AbstractModel):
    """DescribeFavorRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 个人收藏仓库列表返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.FavorResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = FavorResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeGCJobsRequest(AbstractModel):
    """DescribeGCJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGCJobsResponse(AbstractModel):
    """DescribeGCJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Jobs: GC Job 列表
        :type Jobs: list of GCJobInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Jobs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self.Jobs = []
            for item in params.get("Jobs"):
                obj = GCJobInfo()
                obj._deserialize(item)
                self.Jobs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageAccelerateServiceRequest(AbstractModel):
    """DescribeImageAccelerateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageAccelerateServiceResponse(AbstractModel):
    """DescribeImageAccelerateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 镜像加速状态
        :type Status: str
        :param CFSVIP: CFS的VIP
        :type CFSVIP: str
        :param IsEnable: 是否开通
        :type IsEnable: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.CFSVIP = None
        self.IsEnable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.CFSVIP = params.get("CFSVIP")
        self.IsEnable = params.get("IsEnable")
        self.RequestId = params.get("RequestId")


class DescribeImageFilterPersonalRequest(AbstractModel):
    """DescribeImageFilterPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Tag: Tag名
        :type Tag: str
        """
        self.RepoName = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageFilterPersonalResponse(AbstractModel):
    """DescribeImageFilterPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回tag镜像内容相同的tag列表
        :type Data: :class:`tencentcloud.tcr.v20190924.models.SameImagesResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SameImagesResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal请求参数结构体

    """


class DescribeImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 全局自动删除策略信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AutoDelStrategyInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageLifecyclePersonalRequest(AbstractModel):
    """DescribeImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageLifecyclePersonalResponse(AbstractModel):
    """DescribeImageLifecyclePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 自动删除策略信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AutoDelStrategyInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageManifestsRequest(AbstractModel):
    """DescribeImageManifests请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param ImageVersion: 镜像版本
        :type ImageVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageManifestsResponse(AbstractModel):
    """DescribeImageManifests返回参数结构体

    """

    def __init__(self):
        r"""
        :param Manifest: 镜像的Manifest信息
        :type Manifest: str
        :param Config: 镜像的配置信息
        :type Config: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Manifest = None
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Manifest = params.get("Manifest")
        self.Config = params.get("Config")
        self.RequestId = params.get("RequestId")


class DescribeImagePersonalRequest(AbstractModel):
    """DescribeImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param Tag: tag名称，可根据输入搜索
        :type Tag: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagePersonalResponse(AbstractModel):
    """DescribeImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 镜像tag信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.TagInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TagInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param ImageVersion: 指定镜像版本进行查找，当前为模糊搜索
        :type ImageVersion: str
        :param Limit: 每页个数，用于分页，默认20
        :type Limit: int
        :param Offset: 页数，默认值为1
        :type Offset: int
        :param Digest: 指定镜像 Digest 进行查找
        :type Digest: str
        :param ExactMatch: 指定是否为精准匹配，true为精准匹配，不填为模糊匹配
        :type ExactMatch: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None
        self.Limit = None
        self.Offset = None
        self.Digest = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Digest = params.get("Digest")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageInfoList: 容器镜像信息列表
        :type ImageInfoList: list of TcrImageInfo
        :param TotalCount: 容器镜像总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self.ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = TcrImageInfo()
                obj._deserialize(item)
                self.ImageInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImmutableTagRulesRequest(AbstractModel):
    """DescribeImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImmutableTagRulesResponse(AbstractModel):
    """DescribeImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Rules: 规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ImmutableTagRule
        :param EmptyNs: 未创建规则的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type EmptyNs: list of str
        :param Total: 规则总量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.EmptyNs = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ImmutableTagRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.EmptyNs = params.get("EmptyNs")
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeInstanceAllNamespacesRequest(AbstractModel):
    """DescribeInstanceAllNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 每页个数
        :type Limit: int
        :param Offset: 起始偏移位置
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAllNamespacesResponse(AbstractModel):
    """DescribeInstanceAllNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstanceAllRequest(AbstractModel):
    """DescribeInstanceAll请求参数结构体

    """

    def __init__(self):
        r"""
        :param Registryids: 实例ID列表(为空时，
表示获取账号下所有实例)
        :type Registryids: list of str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param AllRegion: 获取所有地域的实例，默认为False
        :type AllRegion: bool
        """
        self.Registryids = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.AllRegion = None


    def _deserialize(self, params):
        self.Registryids = params.get("Registryids")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AllRegion = params.get("AllRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAllResponse(AbstractModel):
    """DescribeInstanceAll返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总实例个数
        :type TotalCount: int
        :param Registries: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Registries: list of Registry
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Registries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self.Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self.Registries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceCustomizedDomainRequest(AbstractModel):
    """DescribeInstanceCustomizedDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param Limit: 分页Limit
        :type Limit: int
        :param Offset: 分页Offset
        :type Offset: int
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceCustomizedDomainResponse(AbstractModel):
    """DescribeInstanceCustomizedDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainInfoList: 域名信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainInfoList: list of CustomizedDomainInfo
        :param TotalCount: 总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfoList") is not None:
            self.DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = CustomizedDomainInfo()
                obj._deserialize(item)
                self.DomainInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceStatusRequest(AbstractModel):
    """DescribeInstanceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryIds: 实例ID的数组
        :type RegistryIds: list of str
        """
        self.RegistryIds = None


    def _deserialize(self, params):
        self.RegistryIds = params.get("RegistryIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceStatusResponse(AbstractModel):
    """DescribeInstanceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryStatusSet: 实例的状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryStatusSet: list of RegistryStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegistryStatusSet") is not None:
            self.RegistryStatusSet = []
            for item in params.get("RegistryStatusSet"):
                obj = RegistryStatus()
                obj._deserialize(item)
                self.RegistryStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTokenRequest(AbstractModel):
    """DescribeInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 ID
        :type RegistryId: str
        :param Limit: 分页单页数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTokenResponse(AbstractModel):
    """DescribeInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 长期访问凭证总数
        :type TotalCount: int
        :param Tokens: 长期访问凭证列表
        :type Tokens: list of TcrInstanceToken
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tokens = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tokens") is not None:
            self.Tokens = []
            for item in params.get("Tokens"):
                obj = TcrInstanceToken()
                obj._deserialize(item)
                self.Tokens.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Registryids: 实例ID列表(为空时，
表示获取账号下所有实例)
        :type Registryids: list of str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param AllRegion: 获取所有地域的实例，默认为False
        :type AllRegion: bool
        """
        self.Registryids = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.AllRegion = None


    def _deserialize(self, params):
        self.Registryids = params.get("Registryids")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AllRegion = params.get("AllRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总实例个数
        :type TotalCount: int
        :param Registries: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Registries: list of Registry
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Registries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self.Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self.Registries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternalEndpointDnsStatusRequest(AbstractModel):
    """DescribeInternalEndpointDnsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param VpcSet: vpc列表
        :type VpcSet: list of VpcAndDomainInfo
        """
        self.VpcSet = None


    def _deserialize(self, params):
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcAndDomainInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInternalEndpointDnsStatusResponse(AbstractModel):
    """DescribeInternalEndpointDnsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param VpcSet: vpc私有域名解析状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcSet: list of VpcPrivateDomainStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcPrivateDomainStatus()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternalEndpointsRequest(AbstractModel):
    """DescribeInternalEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInternalEndpointsResponse(AbstractModel):
    """DescribeInternalEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccessVpcSet: 内网接入信息的列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessVpcSet: list of AccessVpc
        :param TotalCount: 内网接入总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessVpcSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessVpcSet") is not None:
            self.AccessVpcSet = []
            for item in params.get("AccessVpcSet"):
                obj = AccessVpc()
                obj._deserialize(item)
                self.AccessVpcSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNamespacePersonalRequest(AbstractModel):
    """DescribeNamespacePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间，支持模糊查询
        :type Namespace: str
        :param Limit: 单页数量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.Namespace = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacePersonalResponse(AbstractModel):
    """DescribeNamespacePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 用户命名空间返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = NamespaceInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 指定命名空间，不填写默认查询所有命名空间
        :type NamespaceName: str
        :param Limit: 每页个数
        :type Limit: int
        :param Offset: 页面偏移（第几页）
        :type Offset: int
        :param All: 列出所有命名空间
        :type All: bool
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param KmsSignPolicy: 仅查询启用了 KMS 镜像签名的空间
        :type KmsSignPolicy: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Limit = None
        self.Offset = None
        self.All = None
        self.Filters = None
        self.KmsSignPolicy = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.All = params.get("All")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.KmsSignPolicy = params.get("KmsSignPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceList: 命名空间列表信息
        :type NamespaceList: list of TcrNamespaceInfo
        :param TotalCount: 总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NamespaceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NamespaceList") is not None:
            self.NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TcrNamespaceInfo()
                obj._deserialize(item)
                self.NamespaceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的总数
        :type TotalCount: int
        :param Regions: 地域信息列表
        :type Regions: list of Region
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Regions") is not None:
            self.Regions = []
            for item in params.get("Regions"):
                obj = Region()
                obj._deserialize(item)
                self.Regions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstanceCreateTasksRequest(AbstractModel):
    """DescribeReplicationInstanceCreateTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReplicationRegistryId: 同步实例Id，见实例返回列表中的同步实例ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: 同步实例的地域ID，见实例返回列表中地域ID
        :type ReplicationRegionId: int
        """
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None


    def _deserialize(self, params):
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceCreateTasksResponse(AbstractModel):
    """DescribeReplicationInstanceCreateTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskDetail: 任务详情
        :type TaskDetail: list of TaskDetail
        :param Status: 整体任务状态
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskDetail = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskDetail") is not None:
            self.TaskDetail = []
            for item in params.get("TaskDetail"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.TaskDetail.append(obj)
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstanceSyncStatusRequest(AbstractModel):
    """DescribeReplicationInstanceSyncStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例Id
        :type RegistryId: str
        :param ReplicationRegistryId: 复制实例Id
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: 复制实例的地域Id
        :type ReplicationRegionId: int
        :param ShowReplicationLog: 是否显示同步日志
        :type ShowReplicationLog: bool
        :param Offset: 日志页号, 默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认5，最大为20
        :type Limit: int
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None
        self.ShowReplicationLog = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ShowReplicationLog = params.get("ShowReplicationLog")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstanceSyncStatusResponse(AbstractModel):
    """DescribeReplicationInstanceSyncStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReplicationStatus: 同步状态
        :type ReplicationStatus: str
        :param ReplicationTime: 同步完成时间
        :type ReplicationTime: str
        :param ReplicationLog: 同步日志
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicationLog: :class:`tencentcloud.tcr.v20190924.models.ReplicationLog`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReplicationStatus = None
        self.ReplicationTime = None
        self.ReplicationLog = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationStatus = params.get("ReplicationStatus")
        self.ReplicationTime = params.get("ReplicationTime")
        if params.get("ReplicationLog") is not None:
            self.ReplicationLog = ReplicationLog()
            self.ReplicationLog._deserialize(params.get("ReplicationLog"))
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstancesRequest(AbstractModel):
    """DescribeReplicationInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        """
        self.RegistryId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationInstancesResponse(AbstractModel):
    """DescribeReplicationInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总实例个数
        :type TotalCount: int
        :param ReplicationRegistries: 同步实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicationRegistries: list of ReplicationRegistry
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReplicationRegistries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReplicationRegistries") is not None:
            self.ReplicationRegistries = []
            for item in params.get("ReplicationRegistries"):
                obj = ReplicationRegistry()
                obj._deserialize(item)
                self.ReplicationRegistries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRepositoriesRequest(AbstractModel):
    """DescribeRepositories请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 指定命名空间，不填写默认为查询所有命名空间下镜像仓库
        :type NamespaceName: str
        :param RepositoryName: 指定镜像仓库，不填写默认查询指定命名空间下所有镜像仓库
        :type RepositoryName: str
        :param Offset: 页数，用于分页
        :type Offset: int
        :param Limit: 每页个数，用于分页
        :type Limit: int
        :param SortBy: 基于字段排序，支持的值有-creation_time,-name, -update_time
        :type SortBy: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.Offset = None
        self.Limit = None
        self.SortBy = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories返回参数结构体

    """

    def __init__(self):
        r"""
        :param RepositoryList: 仓库信息列表
        :type RepositoryList: list of TcrRepositoryInfo
        :param TotalCount: 总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RepositoryList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RepositoryList") is not None:
            self.RepositoryList = []
            for item in params.get("RepositoryList"):
                obj = TcrRepositoryInfo()
                obj._deserialize(item)
                self.RepositoryList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRepositoryFilterPersonalRequest(AbstractModel):
    """DescribeRepositoryFilterPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 搜索镜像名
        :type RepoName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20，最大100
        :type Limit: int
        :param Public: 筛选条件：1表示public，0表示private
        :type Public: int
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Public = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Public = params.get("Public")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryFilterPersonalResponse(AbstractModel):
    """DescribeRepositoryFilterPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.SearchUserRepositoryResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SearchUserRepositoryResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRepositoryOwnerPersonalRequest(AbstractModel):
    """DescribeRepositoryOwnerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.Offset = None
        self.Limit = None
        self.RepoName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryOwnerPersonalResponse(AbstractModel):
    """DescribeRepositoryOwnerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepoInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRepositoryPersonalRequest(AbstractModel):
    """DescribeRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名字
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryPersonalResponse(AbstractModel):
    """DescribeRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepositoryInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepositoryInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityPoliciesRequest(AbstractModel):
    """DescribeSecurityPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例的Id
        :type RegistryId: str
        """
        self.RegistryId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPoliciesResponse(AbstractModel):
    """DescribeSecurityPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityPolicySet: 实例安全策略组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityPolicySet: list of SecurityPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityPolicySet") is not None:
            self.SecurityPolicySet = []
            for item in params.get("SecurityPolicySet"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self.SecurityPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionRequest(AbstractModel):
    """DescribeTagRetentionExecution请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param RetentionId: 规则Id
        :type RetentionId: int
        :param Limit: 分页PageSize
        :type Limit: int
        :param Offset: 分页Page
        :type Offset: int
        """
        self.RegistryId = None
        self.RetentionId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionResponse(AbstractModel):
    """DescribeTagRetentionExecution返回参数结构体

    """

    def __init__(self):
        r"""
        :param RetentionExecutionList: 版本保留执行记录列表
        :type RetentionExecutionList: list of RetentionExecution
        :param TotalCount: 版本保留执行记录总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RetentionExecutionList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RetentionExecutionList") is not None:
            self.RetentionExecutionList = []
            for item in params.get("RetentionExecutionList"):
                obj = RetentionExecution()
                obj._deserialize(item)
                self.RetentionExecutionList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTagRetentionExecutionTaskRequest(AbstractModel):
    """DescribeTagRetentionExecutionTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param RetentionId: 规则Id
        :type RetentionId: int
        :param ExecutionId: 规则执行Id
        :type ExecutionId: int
        :param Offset: 分页Page
        :type Offset: int
        :param Limit: 分页PageSize
        :type Limit: int
        """
        self.RegistryId = None
        self.RetentionId = None
        self.ExecutionId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RetentionId = params.get("RetentionId")
        self.ExecutionId = params.get("ExecutionId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionExecutionTaskResponse(AbstractModel):
    """DescribeTagRetentionExecutionTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RetentionTaskList: 版本保留执行任务列表
        :type RetentionTaskList: list of RetentionTask
        :param TotalCount: 版本保留执行任务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RetentionTaskList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RetentionTaskList") is not None:
            self.RetentionTaskList = []
            for item in params.get("RetentionTaskList"):
                obj = RetentionTask()
                obj._deserialize(item)
                self.RetentionTaskList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTagRetentionRulesRequest(AbstractModel):
    """DescribeTagRetentionRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param Limit: 分页PageSize
        :type Limit: int
        :param Offset: 分页Page
        :type Offset: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagRetentionRulesResponse(AbstractModel):
    """DescribeTagRetentionRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RetentionPolicyList: 版本保留策略列表
        :type RetentionPolicyList: list of RetentionPolicy
        :param TotalCount: 版本保留策略总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RetentionPolicyList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RetentionPolicyList") is not None:
            self.RetentionPolicyList = []
            for item in params.get("RetentionPolicyList"):
                obj = RetentionPolicy()
                obj._deserialize(item)
                self.RetentionPolicyList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUserQuotaPersonalRequest(AbstractModel):
    """DescribeUserQuotaPersonal请求参数结构体

    """


class DescribeUserQuotaPersonalResponse(AbstractModel):
    """DescribeUserQuotaPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 配额返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RespLimit`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RespLimit()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerLogRequest(AbstractModel):
    """DescribeWebhookTriggerLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Id: 触发器 Id
        :type Id: int
        :param Limit: 分页单页数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerLogResponse(AbstractModel):
    """DescribeWebhookTriggerLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param Logs: 日志列表
        :type Logs: list of WebhookTriggerLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Logs") is not None:
            self.Logs = []
            for item in params.get("Logs"):
                obj = WebhookTriggerLog()
                obj._deserialize(item)
                self.Logs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerRequest(AbstractModel):
    """DescribeWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Limit: 分页单页数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebhookTriggerResponse(AbstractModel):
    """DescribeWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 触发器总数
        :type TotalCount: int
        :param Triggers: 触发器列表
        :type Triggers: list of WebhookTrigger
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Triggers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = WebhookTrigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadHelmChartRequest(AbstractModel):
    """DownloadHelmChart请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param ChartName: Helm chart名称
        :type ChartName: str
        :param ChartVersion: Helm chart版本
        :type ChartVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.ChartName = None
        self.ChartVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.ChartName = params.get("ChartName")
        self.ChartVersion = params.get("ChartVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadHelmChartResponse(AbstractModel):
    """DownloadHelmChart返回参数结构体

    """

    def __init__(self):
        r"""
        :param TmpToken: 临时token
        :type TmpToken: str
        :param TmpSecretId: 临时的secretId
        :type TmpSecretId: str
        :param TmpSecretKey: 临时的secretKey
        :type TmpSecretKey: str
        :param Bucket: 存储桶信息
        :type Bucket: str
        :param Region: 实例ID
        :type Region: str
        :param Path: chart信息
        :type Path: str
        :param StartTime: 开始时间时间戳
        :type StartTime: int
        :param ExpiredTime: token过期时间时间戳
        :type ExpiredTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TmpToken = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.Bucket = None
        self.Region = None
        self.Path = None
        self.StartTime = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TmpToken = params.get("TmpToken")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class DupImageTagResp(AbstractModel):
    """复制镜像tag返回值

    """

    def __init__(self):
        r"""
        :param Digest: 镜像Digest值
        :type Digest: str
        """
        self.Digest = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateImagePersonalRequest(AbstractModel):
    """DuplicateImagePersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param SrcImage: 源镜像名称，不包含domain。例如： tencentyun/foo:v1
        :type SrcImage: str
        :param DestImage: 目的镜像名称，不包含domain。例如： tencentyun/foo:latest
        :type DestImage: str
        """
        self.SrcImage = None
        self.DestImage = None


    def _deserialize(self, params):
        self.SrcImage = params.get("SrcImage")
        self.DestImage = params.get("DestImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateImagePersonalResponse(AbstractModel):
    """DuplicateImagePersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 复制镜像返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DupImageTagResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DupImageTagResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class FavorResp(AbstractModel):
    """用于获取收藏仓库的响应

    """

    def __init__(self):
        r"""
        :param TotalCount: 收藏仓库的总数
        :type TotalCount: int
        :param RepoInfo: 仓库信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoInfo: list of Favors
        """
        self.TotalCount = None
        self.RepoInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = Favors()
                obj._deserialize(item)
                self.RepoInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Favors(AbstractModel):
    """仓库收藏

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名字
        :type RepoName: str
        :param RepoType: 仓库类型
        :type RepoType: str
        :param PullCount: Pull总共的次数
注意：此字段可能返回 null，表示取不到有效值。
        :type PullCount: int
        :param FavorCount: 仓库收藏次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FavorCount: int
        :param Public: 仓库是否公开
注意：此字段可能返回 null，表示取不到有效值。
        :type Public: int
        :param IsQcloudOfficial: 是否为官方所有
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloudOfficial: bool
        :param TagCount: 仓库Tag的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TagCount: int
        :param Logo: Logo
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param Region: 地域
        :type Region: str
        :param RegionId: 地域的Id
        :type RegionId: int
        """
        self.RepoName = None
        self.RepoType = None
        self.PullCount = None
        self.FavorCount = None
        self.Public = None
        self.IsQcloudOfficial = None
        self.TagCount = None
        self.Logo = None
        self.Region = None
        self.RegionId = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.PullCount = params.get("PullCount")
        self.FavorCount = params.get("FavorCount")
        self.Public = params.get("Public")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        self.TagCount = params.get("TagCount")
        self.Logo = params.get("Logo")
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GCJobInfo(AbstractModel):
    """GC 执行信息

    """

    def __init__(self):
        r"""
        :param ID: 作业 ID
        :type ID: int
        :param JobStatus: 作业状态
        :type JobStatus: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Schedule: 调度信息
        :type Schedule: :class:`tencentcloud.tcr.v20190924.models.Schedule`
        """
        self.ID = None
        self.JobStatus = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Schedule = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.JobStatus = params.get("JobStatus")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Schedule") is not None:
            self.Schedule = Schedule()
            self.Schedule._deserialize(params.get("Schedule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """Header KV

    """

    def __init__(self):
        r"""
        :param Key: Header Key
        :type Key: str
        :param Values: Header Values
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImmutableTagRule(AbstractModel):
    """镜像 tag 不可变规则

    """

    def __init__(self):
        r"""
        :param RepositoryPattern: 仓库匹配规则
        :type RepositoryPattern: str
        :param TagPattern: Tag 匹配规则
        :type TagPattern: str
        :param RepositoryDecoration: repoMatches或repoExcludes
        :type RepositoryDecoration: str
        :param TagDecoration: matches或excludes
        :type TagDecoration: str
        :param Disabled: 禁用规则
        :type Disabled: bool
        :param RuleId: 规则 Id
        :type RuleId: int
        :param NsName: 命名空间
        :type NsName: str
        """
        self.RepositoryPattern = None
        self.TagPattern = None
        self.RepositoryDecoration = None
        self.TagDecoration = None
        self.Disabled = None
        self.RuleId = None
        self.NsName = None


    def _deserialize(self, params):
        self.RepositoryPattern = params.get("RepositoryPattern")
        self.TagPattern = params.get("TagPattern")
        self.RepositoryDecoration = params.get("RepositoryDecoration")
        self.TagDecoration = params.get("TagDecoration")
        self.Disabled = params.get("Disabled")
        self.RuleId = params.get("RuleId")
        self.NsName = params.get("NsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueString(AbstractModel):
    """通用参数字符串键值对

    """

    def __init__(self):
        r"""
        :param Key: 键
        :type Key: str
        :param Value: 值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Limit(AbstractModel):
    """共享镜像仓库用户配额

    """

    def __init__(self):
        r"""
        :param Username: 用户名
        :type Username: str
        :param Type: 配额的类型
        :type Type: str
        :param Value: 配置的值
        :type Value: int
        """
        self.Username = None
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointRequest(AbstractModel):
    """ManageExternalEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Operation: 操作（Create/Delete）
        :type Operation: str
        """
        self.RegistryId = None
        self.Operation = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageExternalEndpointResponse(AbstractModel):
    """ManageExternalEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ManageImageLifecycleGlobalPersonalRequest(AbstractModel):
    """ManageImageLifecycleGlobalPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: global_keep_last_days:全局保留最近几天的数据;global_keep_last_nums:全局保留最近多少个
        :type Type: str
        :param Val: 策略值
        :type Val: int
        """
        self.Type = None
        self.Val = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageImageLifecycleGlobalPersonalResponse(AbstractModel):
    """ManageImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ManageInternalEndpointRequest(AbstractModel):
    """ManageInternalEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Operation: Create/Delete
        :type Operation: str
        :param VpcId: 需要接入的用户vpcid
        :type VpcId: str
        :param SubnetId: 需要接入的用户子网id
        :type SubnetId: str
        :param RegionId: 请求的地域ID，用于实例复制地域
        :type RegionId: int
        :param RegionName: 请求的地域名称，用于实例复制地域
        :type RegionName: str
        """
        self.RegistryId = None
        self.Operation = None
        self.VpcId = None
        self.SubnetId = None
        self.RegionId = None
        self.RegionName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Operation = params.get("Operation")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageInternalEndpointResponse(AbstractModel):
    """ManageInternalEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ManageReplicationRequest(AbstractModel):
    """ManageReplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param SourceRegistryId: 复制源实例ID
        :type SourceRegistryId: str
        :param DestinationRegistryId: 复制目标实例ID
        :type DestinationRegistryId: str
        :param Rule: 同步规则
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ReplicationRule`
        :param Description: 规则描述
        :type Description: str
        :param DestinationRegionId: 目标实例的地域ID，如广州是1
        :type DestinationRegionId: int
        :param PeerReplicationOption: 开启跨主账号实例同步配置项
        :type PeerReplicationOption: :class:`tencentcloud.tcr.v20190924.models.PeerReplicationOption`
        """
        self.SourceRegistryId = None
        self.DestinationRegistryId = None
        self.Rule = None
        self.Description = None
        self.DestinationRegionId = None
        self.PeerReplicationOption = None


    def _deserialize(self, params):
        self.SourceRegistryId = params.get("SourceRegistryId")
        self.DestinationRegistryId = params.get("DestinationRegistryId")
        if params.get("Rule") is not None:
            self.Rule = ReplicationRule()
            self.Rule._deserialize(params.get("Rule"))
        self.Description = params.get("Description")
        self.DestinationRegionId = params.get("DestinationRegionId")
        if params.get("PeerReplicationOption") is not None:
            self.PeerReplicationOption = PeerReplicationOption()
            self.PeerReplicationOption._deserialize(params.get("PeerReplicationOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageReplicationResponse(AbstractModel):
    """ManageReplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationTriggerPersonalRequest(AbstractModel):
    """ModifyApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 触发器关联的镜像仓库，library/test格式
        :type RepoName: str
        :param TriggerName: 触发器名称，必填参数
        :type TriggerName: str
        :param InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发
        :type InvokeMethod: str
        :param InvokeExpr: 触发方式对应的表达式
        :type InvokeExpr: str
        :param ClusterId: 应用所在TKE集群ID
        :type ClusterId: str
        :param Namespace: 应用所在TKE集群命名空间
        :type Namespace: str
        :param WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param WorkloadName: 应用所在TKE集群工作负载名称
        :type WorkloadName: str
        :param ContainerName: 应用所在TKE集群工作负载下容器名称
        :type ContainerName: str
        :param ClusterRegion: 应用所在TKE集群地域数字ID，如1（广州）、16（成都）
        :type ClusterRegion: int
        :param NewTriggerName: 新触发器名称
        :type NewTriggerName: str
        """
        self.RepoName = None
        self.TriggerName = None
        self.InvokeMethod = None
        self.InvokeExpr = None
        self.ClusterId = None
        self.Namespace = None
        self.WorkloadType = None
        self.WorkloadName = None
        self.ContainerName = None
        self.ClusterRegion = None
        self.NewTriggerName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeMethod = params.get("InvokeMethod")
        self.InvokeExpr = params.get("InvokeExpr")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.WorkloadType = params.get("WorkloadType")
        self.WorkloadName = params.get("WorkloadName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")
        self.NewTriggerName = params.get("NewTriggerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationTriggerPersonalResponse(AbstractModel):
    """ModifyApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImmutableTagRulesRequest(AbstractModel):
    """ModifyImmutableTagRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param NamespaceName: 命名空间
        :type NamespaceName: str
        :param RuleId: 规则 Id
        :type RuleId: int
        :param Rule: 规则
        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RuleId = None
        self.Rule = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RuleId = params.get("RuleId")
        if params.get("Rule") is not None:
            self.Rule = ImmutableTagRule()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImmutableTagRulesResponse(AbstractModel):
    """ModifyImmutableTagRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param RegistryType: 实例的规格
        :type RegistryType: str
        """
        self.RegistryId = None
        self.RegistryType = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RegistryType = params.get("RegistryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceTokenRequest(AbstractModel):
    """ModifyInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param TokenId: 实例长期访问凭证 ID
        :type TokenId: str
        :param RegistryId: 实例 ID
        :type RegistryId: str
        :param Enable: 启用或禁用实例长期访问凭证
        :type Enable: bool
        :param Desc: 访问凭证描述
        :type Desc: str
        :param ModifyFlag: 1为修改描述 2为操作启动禁用，默认值为2
        :type ModifyFlag: int
        """
        self.TokenId = None
        self.RegistryId = None
        self.Enable = None
        self.Desc = None
        self.ModifyFlag = None


    def _deserialize(self, params):
        self.TokenId = params.get("TokenId")
        self.RegistryId = params.get("RegistryId")
        self.Enable = params.get("Enable")
        self.Desc = params.get("Desc")
        self.ModifyFlag = params.get("ModifyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTokenResponse(AbstractModel):
    """ModifyInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param IsPublic: 访问级别，True为公开，False为私有
        :type IsPublic: bool
        :param IsAutoScan: 扫描级别，True为自动，False为手动
        :type IsAutoScan: bool
        :param IsPreventVUL: 阻断开关，True为开放，False为关闭
        :type IsPreventVUL: bool
        :param Severity: 阻断漏洞等级，目前仅支持 low、medium、high
        :type Severity: str
        :param CVEWhitelistItems: 漏洞白名单列表
        :type CVEWhitelistItems: list of CVEWhitelistItem
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None
        self.IsAutoScan = None
        self.IsPreventVUL = None
        self.Severity = None
        self.CVEWhitelistItems = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")
        self.IsAutoScan = params.get("IsAutoScan")
        self.IsPreventVUL = params.get("IsPreventVUL")
        self.Severity = params.get("Severity")
        if params.get("CVEWhitelistItems") is not None:
            self.CVEWhitelistItems = []
            for item in params.get("CVEWhitelistItems"):
                obj = CVEWhitelistItem()
                obj._deserialize(item)
                self.CVEWhitelistItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryAccessPersonalRequest(AbstractModel):
    """ModifyRepositoryAccessPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Public: 默认值为0, 1公共，0私有
        :type Public: int
        """
        self.RepoName = None
        self.Public = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Public = params.get("Public")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryAccessPersonalResponse(AbstractModel):
    """ModifyRepositoryAccessPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryInfoPersonalRequest(AbstractModel):
    """ModifyRepositoryInfoPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Description: 仓库描述
        :type Description: str
        """
        self.RepoName = None
        self.Description = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryInfoPersonalResponse(AbstractModel):
    """ModifyRepositoryInfoPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryRequest(AbstractModel):
    """ModifyRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param BriefDescription: 仓库简短描述
        :type BriefDescription: str
        :param Description: 仓库详细描述
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRepositoryResponse(AbstractModel):
    """ModifyRepository返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例的Id
        :type RegistryId: str
        :param PolicyIndex: PolicyId
        :type PolicyIndex: int
        :param CidrBlock: 192.168.0.0/24 白名单Ip
        :type CidrBlock: str
        :param Description: 备注
        :type Description: str
        """
        self.RegistryId = None
        self.PolicyIndex = None
        self.CidrBlock = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.PolicyIndex = params.get("PolicyIndex")
        self.CidrBlock = params.get("CidrBlock")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ModifyTagRetentionRuleRequest(AbstractModel):
    """ModifyTagRetentionRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例iD
        :type RegistryId: str
        :param NamespaceId: 命名空间的Id，必须填写原有的命名空间id
        :type NamespaceId: int
        :param RetentionRule: 保留策略
        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`
        :param CronSetting: 执行周期，必须填写为原来的设置
        :type CronSetting: str
        :param RetentionId: 规则Id
        :type RetentionId: int
        :param Disabled: 是否禁用规则
        :type Disabled: bool
        """
        self.RegistryId = None
        self.NamespaceId = None
        self.RetentionRule = None
        self.CronSetting = None
        self.RetentionId = None
        self.Disabled = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceId = params.get("NamespaceId")
        if params.get("RetentionRule") is not None:
            self.RetentionRule = RetentionRule()
            self.RetentionRule._deserialize(params.get("RetentionRule"))
        self.CronSetting = params.get("CronSetting")
        self.RetentionId = params.get("RetentionId")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTagRetentionRuleResponse(AbstractModel):
    """ModifyTagRetentionRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserPasswordPersonalRequest(AbstractModel):
    """ModifyUserPasswordPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Password: 更新后的密码
        :type Password: str
        """
        self.Password = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserPasswordPersonalResponse(AbstractModel):
    """ModifyUserPasswordPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Trigger: 触发器参数
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebhookTriggerResponse(AbstractModel):
    """ModifyWebhookTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NamespaceInfo(AbstractModel):
    """命名空间信息

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间
        :type Namespace: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param RepoCount: 命名空间下仓库数量
        :type RepoCount: int
        """
        self.Namespace = None
        self.CreationTime = None
        self.RepoCount = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.CreationTime = params.get("CreationTime")
        self.RepoCount = params.get("RepoCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfoResp(AbstractModel):
    """获取命名空间信息返回

    """

    def __init__(self):
        r"""
        :param NamespaceCount: 命名空间数量
        :type NamespaceCount: int
        :param NamespaceInfo: 命名空间信息
        :type NamespaceInfo: list of NamespaceInfo
        """
        self.NamespaceCount = None
        self.NamespaceInfo = None


    def _deserialize(self, params):
        self.NamespaceCount = params.get("NamespaceCount")
        if params.get("NamespaceInfo") is not None:
            self.NamespaceInfo = []
            for item in params.get("NamespaceInfo"):
                obj = NamespaceInfo()
                obj._deserialize(item)
                self.NamespaceInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceIsExistsResp(AbstractModel):
    """NamespaceIsExists返回类型

    """

    def __init__(self):
        r"""
        :param IsExist: 命名空间是否存在
        :type IsExist: bool
        :param IsPreserved: 是否为保留命名空间
        :type IsPreserved: bool
        """
        self.IsExist = None
        self.IsPreserved = None


    def _deserialize(self, params):
        self.IsExist = params.get("IsExist")
        self.IsPreserved = params.get("IsPreserved")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeerReplicationOption(AbstractModel):
    """跨主账号实例同步参数

    """

    def __init__(self):
        r"""
        :param PeerRegistryUin: 待同步实例的uin
        :type PeerRegistryUin: str
        :param PeerRegistryToken: 待同步实例的访问永久Token
        :type PeerRegistryToken: str
        :param EnablePeerReplication: 是否开启跨主账号实例同步
        :type EnablePeerReplication: bool
        """
        self.PeerRegistryUin = None
        self.PeerRegistryToken = None
        self.EnablePeerReplication = None


    def _deserialize(self, params):
        self.PeerRegistryUin = params.get("PeerRegistryUin")
        self.PeerRegistryToken = params.get("PeerRegistryToken")
        self.EnablePeerReplication = params.get("EnablePeerReplication")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param Alias: gz
        :type Alias: str
        :param RegionId: 1
        :type RegionId: int
        :param RegionName: ap-guangzhou
        :type RegionName: str
        :param Status: alluser
        :type Status: str
        :param Remark: remark
        :type Remark: str
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param Id: id
        :type Id: int
        """
        self.Alias = None
        self.RegionId = None
        self.RegionName = None
        self.Status = None
        self.Remark = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.Id = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Registry(AbstractModel):
    """实例信息结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param RegistryName: 实例名称
        :type RegistryName: str
        :param RegistryType: 实例规格
        :type RegistryType: str
        :param Status: 实例状态
        :type Status: str
        :param PublicDomain: 实例的公共访问地址
        :type PublicDomain: str
        :param CreatedAt: 实例创建时间
        :type CreatedAt: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param RegionId: 地域Id
        :type RegionId: int
        :param EnableAnonymous: 是否支持匿名
        :type EnableAnonymous: bool
        :param TokenValidTime: Token有效时间
        :type TokenValidTime: int
        :param InternalEndpoint: 实例内部访问地址
        :type InternalEndpoint: str
        :param TagSpecification: 实例云标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param ExpiredAt: 实例过期时间（预付费）
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredAt: str
        :param PayMod: 实例付费类型，0表示后付费，1表示预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMod: int
        :param RenewFlag: 预付费续费标识，0表示手动续费，1表示自动续费，2不续费并且不通知
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        """
        self.RegistryId = None
        self.RegistryName = None
        self.RegistryType = None
        self.Status = None
        self.PublicDomain = None
        self.CreatedAt = None
        self.RegionName = None
        self.RegionId = None
        self.EnableAnonymous = None
        self.TokenValidTime = None
        self.InternalEndpoint = None
        self.TagSpecification = None
        self.ExpiredAt = None
        self.PayMod = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")
        self.Status = params.get("Status")
        self.PublicDomain = params.get("PublicDomain")
        self.CreatedAt = params.get("CreatedAt")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.EnableAnonymous = params.get("EnableAnonymous")
        self.TokenValidTime = params.get("TokenValidTime")
        self.InternalEndpoint = params.get("InternalEndpoint")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        self.ExpiredAt = params.get("ExpiredAt")
        self.PayMod = params.get("PayMod")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryChargePrepaid(AbstractModel):
    """实例预付费模式

    """

    def __init__(self):
        r"""
        :param Period: 购买实例的时长，单位：月
        :type Period: int
        :param RenewFlag: 自动续费标识，0：手动续费，1：自动续费，2：不续费并且不通知
        :type RenewFlag: int
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryCondition(AbstractModel):
    """实例创建过程

    """

    def __init__(self):
        r"""
        :param Type: 实例创建过程类型
        :type Type: str
        :param Status: 实例创建过程状态
        :type Status: str
        :param Reason: 转换到该过程的简明原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self.Type = None
        self.Status = None
        self.Reason = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegistryStatus(AbstractModel):
    """实例状态

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例的Id
        :type RegistryId: str
        :param Status: 实例的状态
        :type Status: str
        :param Conditions: 附加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of RegistryCondition
        """
        self.RegistryId = None
        self.Status = None
        self.Conditions = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Status = params.get("Status")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RegistryCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param RegistryChargePrepaid: 预付费自动续费标识和购买时长,0：手动续费，1：自动续费，2：不续费并且不通知;单位为月
        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`
        :param Flag: 0 续费， 1按量转包年包月
        :type Flag: int
        """
        self.RegistryId = None
        self.RegistryChargePrepaid = None
        self.Flag = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("RegistryChargePrepaid") is not None:
            self.RegistryChargePrepaid = RegistryChargePrepaid()
            self.RegistryChargePrepaid._deserialize(params.get("RegistryChargePrepaid"))
        self.Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegistryId: 企业版实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ReplicationFilter(AbstractModel):
    """同步规则过滤器

    """

    def __init__(self):
        r"""
        :param Type: 类型（name、tag和resource）
        :type Type: str
        :param Value: 默认为空
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationLog(AbstractModel):
    """同步日志

    """

    def __init__(self):
        r"""
        :param ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param Source: 源资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param Destination: 目的资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Destination: str
        :param Status: 同步状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.ResourceType = None
        self.Source = None
        self.Destination = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.Source = params.get("Source")
        self.Destination = params.get("Destination")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRegistry(AbstractModel):
    """企业版复制实例

    """

    def __init__(self):
        r"""
        :param RegistryId: 主实例ID
        :type RegistryId: str
        :param ReplicationRegistryId: 复制实例ID
        :type ReplicationRegistryId: str
        :param ReplicationRegionId: 复制实例的地域ID
        :type ReplicationRegionId: int
        :param ReplicationRegionName: 复制实例的地域名称
        :type ReplicationRegionName: str
        :param Status: 复制实例的状态
        :type Status: str
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        """
        self.RegistryId = None
        self.ReplicationRegistryId = None
        self.ReplicationRegionId = None
        self.ReplicationRegionName = None
        self.Status = None
        self.CreatedAt = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
        self.ReplicationRegionName = params.get("ReplicationRegionName")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicationRule(AbstractModel):
    """同步规则

    """

    def __init__(self):
        r"""
        :param Name: 同步规则名称
        :type Name: str
        :param DestNamespace: 目标命名空间
        :type DestNamespace: str
        :param Override: 是否覆盖
        :type Override: bool
        :param Filters: 同步过滤条件
        :type Filters: list of ReplicationFilter
        """
        self.Name = None
        self.DestNamespace = None
        self.Override = None
        self.Filters = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DestNamespace = params.get("DestNamespace")
        self.Override = params.get("Override")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ReplicationFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepoInfo(AbstractModel):
    """仓库的信息

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        :param RepoType: 仓库类型
        :type RepoType: str
        :param TagCount: Tag数量
        :type TagCount: int
        :param Public: 是否为公开
        :type Public: int
        :param IsUserFavor: 是否为用户收藏
        :type IsUserFavor: bool
        :param IsQcloudOfficial: 是否为腾讯云官方仓库
        :type IsQcloudOfficial: bool
        :param FavorCount: 被收藏的个数
        :type FavorCount: int
        :param PullCount: 拉取的数量
        :type PullCount: int
        :param Description: 描述
        :type Description: str
        :param CreationTime: 仓库创建时间
        :type CreationTime: str
        :param UpdateTime: 仓库更新时间
        :type UpdateTime: str
        """
        self.RepoName = None
        self.RepoType = None
        self.TagCount = None
        self.Public = None
        self.IsUserFavor = None
        self.IsQcloudOfficial = None
        self.FavorCount = None
        self.PullCount = None
        self.Description = None
        self.CreationTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.TagCount = params.get("TagCount")
        self.Public = params.get("Public")
        self.IsUserFavor = params.get("IsUserFavor")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        self.FavorCount = params.get("FavorCount")
        self.PullCount = params.get("PullCount")
        self.Description = params.get("Description")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepoInfoResp(AbstractModel):
    """仓库信息的返回信息

    """

    def __init__(self):
        r"""
        :param TotalCount: 仓库总数
        :type TotalCount: int
        :param RepoInfo: 仓库信息列表
        :type RepoInfo: list of RepoInfo
        :param Server: Server信息
        :type Server: str
        """
        self.TotalCount = None
        self.RepoInfo = None
        self.Server = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self.RepoInfo.append(obj)
        self.Server = params.get("Server")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepoIsExistResp(AbstractModel):
    """仓库是否存在的返回值

    """

    def __init__(self):
        r"""
        :param IsExist: 仓库是否存在
        :type IsExist: bool
        """
        self.IsExist = None


    def _deserialize(self, params):
        self.IsExist = params.get("IsExist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepositoryInfoResp(AbstractModel):
    """查询共享版仓库信息返回

    """

    def __init__(self):
        r"""
        :param RepoName: 镜像仓库名字
        :type RepoName: str
        :param RepoType: 镜像仓库类型
        :type RepoType: str
        :param Server: 镜像仓库服务地址
        :type Server: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param Description: 镜像仓库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Public: 是否为公有镜像
        :type Public: int
        :param PullCount: 下载次数
        :type PullCount: int
        :param FavorCount: 收藏次数
        :type FavorCount: int
        :param IsUserFavor: 是否为用户收藏
        :type IsUserFavor: bool
        :param IsQcloudOfficial: 是否为腾讯云官方镜像
        :type IsQcloudOfficial: bool
        """
        self.RepoName = None
        self.RepoType = None
        self.Server = None
        self.CreationTime = None
        self.Description = None
        self.Public = None
        self.PullCount = None
        self.FavorCount = None
        self.IsUserFavor = None
        self.IsQcloudOfficial = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.Server = params.get("Server")
        self.CreationTime = params.get("CreationTime")
        self.Description = params.get("Description")
        self.Public = params.get("Public")
        self.PullCount = params.get("PullCount")
        self.FavorCount = params.get("FavorCount")
        self.IsUserFavor = params.get("IsUserFavor")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RespLimit(AbstractModel):
    """用户配额返回值

    """

    def __init__(self):
        r"""
        :param LimitInfo: 配额信息
        :type LimitInfo: list of Limit
        """
        self.LimitInfo = None


    def _deserialize(self, params):
        if params.get("LimitInfo") is not None:
            self.LimitInfo = []
            for item in params.get("LimitInfo"):
                obj = Limit()
                obj._deserialize(item)
                self.LimitInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionExecution(AbstractModel):
    """版本保留规则执行

    """

    def __init__(self):
        r"""
        :param ExecutionId: 执行Id
        :type ExecutionId: int
        :param RetentionId: 所属规则id
        :type RetentionId: int
        :param StartTime: 执行的开始时间
        :type StartTime: str
        :param EndTime: 执行的结束时间
        :type EndTime: str
        :param Status: 执行的状态，Failed, Succeed, Stopped, InProgress
        :type Status: str
        """
        self.ExecutionId = None
        self.RetentionId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.ExecutionId = params.get("ExecutionId")
        self.RetentionId = params.get("RetentionId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionPolicy(AbstractModel):
    """版本保留策略

    """

    def __init__(self):
        r"""
        :param RetentionId: 版本保留策略Id
        :type RetentionId: int
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param RetentionRuleList: 规则列表
        :type RetentionRuleList: list of RetentionRule
        :param CronSetting: 定期执行方式
        :type CronSetting: str
        :param Disabled: 是否启用规则
        :type Disabled: bool
        :param NextExecutionTime: 基于当前时间根据cronSetting后下一次任务要执行的时间，仅做参考使用
        :type NextExecutionTime: str
        """
        self.RetentionId = None
        self.NamespaceName = None
        self.RetentionRuleList = None
        self.CronSetting = None
        self.Disabled = None
        self.NextExecutionTime = None


    def _deserialize(self, params):
        self.RetentionId = params.get("RetentionId")
        self.NamespaceName = params.get("NamespaceName")
        if params.get("RetentionRuleList") is not None:
            self.RetentionRuleList = []
            for item in params.get("RetentionRuleList"):
                obj = RetentionRule()
                obj._deserialize(item)
                self.RetentionRuleList.append(obj)
        self.CronSetting = params.get("CronSetting")
        self.Disabled = params.get("Disabled")
        self.NextExecutionTime = params.get("NextExecutionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionRule(AbstractModel):
    """版本保留规则

    """

    def __init__(self):
        r"""
        :param Key: 支持的策略，可选值为latestPushedK（保留最新推送多少个版本）nDaysSinceLastPush（保留近天内推送）
        :type Key: str
        :param Value: 规则设置下的对应值
        :type Value: int
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetentionTask(AbstractModel):
    """版本保留执行的规则

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: int
        :param ExecutionId: 所属的规则执行Id
        :type ExecutionId: int
        :param StartTime: 任务开始时间
        :type StartTime: str
        :param EndTime: 任务结束时间
        :type EndTime: str
        :param Status: 任务的执行状态，Failed, Succeed, Stopped, InProgress
        :type Status: str
        :param Total: 总tag数
        :type Total: int
        :param Retained: 保留tag数
        :type Retained: int
        :param Repository: 应用的仓库
        :type Repository: str
        """
        self.TaskId = None
        self.ExecutionId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Total = None
        self.Retained = None
        self.Repository = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ExecutionId = params.get("ExecutionId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Total = params.get("Total")
        self.Retained = params.get("Retained")
        self.Repository = params.get("Repository")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SameImagesResp(AbstractModel):
    """指定tag镜像内容相同的tag列表

    """

    def __init__(self):
        r"""
        :param SameImages: tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SameImages: list of str
        """
        self.SameImages = None


    def _deserialize(self, params):
        self.SameImages = params.get("SameImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Schedule(AbstractModel):
    """作业调度信息

    """

    def __init__(self):
        r"""
        :param Type: 类型：Hourly, Daily, Weekly, Custom, Manual, Dryrun, None
        :type Type: str
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
        


class SearchUserRepositoryResp(AbstractModel):
    """获取满足输入搜索条件的用户镜像仓库

    """

    def __init__(self):
        r"""
        :param TotalCount: 总个数
        :type TotalCount: int
        :param RepoInfo: 仓库列表
        :type RepoInfo: list of RepoInfo
        :param Server: Server
        :type Server: str
        :param PrivilegeFiltered: PrivilegeFiltered
        :type PrivilegeFiltered: bool
        """
        self.TotalCount = None
        self.RepoInfo = None
        self.Server = None
        self.PrivilegeFiltered = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self.RepoInfo.append(obj)
        self.Server = params.get("Server")
        self.PrivilegeFiltered = params.get("PrivilegeFiltered")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicy(AbstractModel):
    """安全策略

    """

    def __init__(self):
        r"""
        :param PolicyIndex: 策略索引
        :type PolicyIndex: int
        :param Description: 备注
        :type Description: str
        :param CidrBlock: 运行访问的公网IP地址端
        :type CidrBlock: str
        :param PolicyVersion: 安全策略的版本
        :type PolicyVersion: str
        """
        self.PolicyIndex = None
        self.Description = None
        self.CidrBlock = None
        self.PolicyVersion = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Description = params.get("Description")
        self.CidrBlock = params.get("CidrBlock")
        self.PolicyVersion = params.get("PolicyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """云标签Tag

    """

    def __init__(self):
        r"""
        :param Key: 云标签的key
        :type Key: str
        :param Value: 云标签的值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """镜像tag信息

    """

    def __init__(self):
        r"""
        :param TagName: Tag名称
        :type TagName: str
        :param TagId: 制品的 ID
        :type TagId: str
        :param ImageId: docker image 可以看到的id
        :type ImageId: str
        :param Size: 大小
        :type Size: str
        :param CreationTime: 制品的创建时间
        :type CreationTime: str
        :param DurationDays: 制品创建至今时间长度
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationDays: str
        :param Author: 标注的制品作者
        :type Author: str
        :param Architecture: 标注的制品平台
        :type Architecture: str
        :param DockerVersion: 创建制品的 Docker 版本
        :type DockerVersion: str
        :param OS: 标注的制品操作系统
        :type OS: str
        :param SizeByte: 制品大小
        :type SizeByte: int
        :param Id: 序号
        :type Id: int
        :param UpdateTime: 数据更新时间
        :type UpdateTime: str
        :param PushTime: 制品更新时间
        :type PushTime: str
        :param Kind: 制品类型
        :type Kind: str
        """
        self.TagName = None
        self.TagId = None
        self.ImageId = None
        self.Size = None
        self.CreationTime = None
        self.DurationDays = None
        self.Author = None
        self.Architecture = None
        self.DockerVersion = None
        self.OS = None
        self.SizeByte = None
        self.Id = None
        self.UpdateTime = None
        self.PushTime = None
        self.Kind = None


    def _deserialize(self, params):
        self.TagName = params.get("TagName")
        self.TagId = params.get("TagId")
        self.ImageId = params.get("ImageId")
        self.Size = params.get("Size")
        self.CreationTime = params.get("CreationTime")
        self.DurationDays = params.get("DurationDays")
        self.Author = params.get("Author")
        self.Architecture = params.get("Architecture")
        self.DockerVersion = params.get("DockerVersion")
        self.OS = params.get("OS")
        self.SizeByte = params.get("SizeByte")
        self.Id = params.get("Id")
        self.UpdateTime = params.get("UpdateTime")
        self.PushTime = params.get("PushTime")
        self.Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfoResp(AbstractModel):
    """Tag列表的返回值

    """

    def __init__(self):
        r"""
        :param TagCount: Tag的总数
        :type TagCount: int
        :param TagInfo: TagInfo列表
        :type TagInfo: list of TagInfo
        :param Server: Server
        :type Server: str
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.TagCount = None
        self.TagInfo = None
        self.Server = None
        self.RepoName = None


    def _deserialize(self, params):
        self.TagCount = params.get("TagCount")
        if params.get("TagInfo") is not None:
            self.TagInfo = []
            for item in params.get("TagInfo"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagInfo.append(obj)
        self.Server = params.get("Server")
        self.RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """云标签

    """

    def __init__(self):
        r"""
        :param ResourceType: 默认值为instance
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param Tags: 云标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """任务详情

    """

    def __init__(self):
        r"""
        :param TaskName: 任务
        :type TaskName: str
        :param TaskUUID: 任务UUID
        :type TaskUUID: str
        :param TaskStatus: 任务状态
        :type TaskStatus: str
        :param TaskMessage: 任务的状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMessage: str
        :param CreatedTime: 任务开始时间
        :type CreatedTime: str
        :param FinishedTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedTime: str
        """
        self.TaskName = None
        self.TaskUUID = None
        self.TaskStatus = None
        self.TaskMessage = None
        self.CreatedTime = None
        self.FinishedTime = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskUUID = params.get("TaskUUID")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskMessage = params.get("TaskMessage")
        self.CreatedTime = params.get("CreatedTime")
        self.FinishedTime = params.get("FinishedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrImageInfo(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        r"""
        :param Digest: 哈希值
        :type Digest: str
        :param Size: 镜像体积（单位：字节）
        :type Size: int
        :param ImageVersion: Tag名称
        :type ImageVersion: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Kind: 制品类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param KmsSignature: KMS 签名信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsSignature: str
        """
        self.Digest = None
        self.Size = None
        self.ImageVersion = None
        self.UpdateTime = None
        self.Kind = None
        self.KmsSignature = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")
        self.Size = params.get("Size")
        self.ImageVersion = params.get("ImageVersion")
        self.UpdateTime = params.get("UpdateTime")
        self.Kind = params.get("Kind")
        self.KmsSignature = params.get("KmsSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrInstanceToken(AbstractModel):
    """实例登录令牌

    """

    def __init__(self):
        r"""
        :param Id: 令牌ID
        :type Id: str
        :param Desc: 令牌描述
        :type Desc: str
        :param RegistryId: 令牌所属实例ID
        :type RegistryId: str
        :param Enabled: 令牌启用状态
        :type Enabled: bool
        :param CreatedAt: 令牌创建时间
        :type CreatedAt: str
        :param ExpiredAt: 令牌过期时间戳
        :type ExpiredAt: int
        """
        self.Id = None
        self.Desc = None
        self.RegistryId = None
        self.Enabled = None
        self.CreatedAt = None
        self.ExpiredAt = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        self.RegistryId = params.get("RegistryId")
        self.Enabled = params.get("Enabled")
        self.CreatedAt = params.get("CreatedAt")
        self.ExpiredAt = params.get("ExpiredAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrNamespaceInfo(AbstractModel):
    """Tcr 命名空间的描述

    """

    def __init__(self):
        r"""
        :param Name: 命名空间名称
        :type Name: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param Public: 访问级别
        :type Public: bool
        :param NamespaceId: 命名空间的Id
        :type NamespaceId: int
        :param TagSpecification: 实例云标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`
        :param Metadata: 命名空间元数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: list of KeyValueString
        :param CVEWhitelistItems: 漏洞白名单列表
        :type CVEWhitelistItems: list of CVEWhitelistItem
        :param AutoScan: 扫描级别，true为自动，false为手动
        :type AutoScan: bool
        :param PreventVUL: 安全阻断级别，true为开启，false为关闭
        :type PreventVUL: bool
        :param Severity: 阻断漏洞等级，目前仅支持low、medium、high, 为""时表示没有设置
        :type Severity: str
        """
        self.Name = None
        self.CreationTime = None
        self.Public = None
        self.NamespaceId = None
        self.TagSpecification = None
        self.Metadata = None
        self.CVEWhitelistItems = None
        self.AutoScan = None
        self.PreventVUL = None
        self.Severity = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.NamespaceId = params.get("NamespaceId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        if params.get("Metadata") is not None:
            self.Metadata = []
            for item in params.get("Metadata"):
                obj = KeyValueString()
                obj._deserialize(item)
                self.Metadata.append(obj)
        if params.get("CVEWhitelistItems") is not None:
            self.CVEWhitelistItems = []
            for item in params.get("CVEWhitelistItems"):
                obj = CVEWhitelistItem()
                obj._deserialize(item)
                self.CVEWhitelistItems.append(obj)
        self.AutoScan = params.get("AutoScan")
        self.PreventVUL = params.get("PreventVUL")
        self.Severity = params.get("Severity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrRepositoryInfo(AbstractModel):
    """Tcr镜像仓库信息

    """

    def __init__(self):
        r"""
        :param Name: 仓库名称
        :type Name: str
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param CreationTime: 创建时间，格式"2006-01-02 15:04:05.999999999 -0700 MST"
        :type CreationTime: str
        :param Public: 是否公开
        :type Public: bool
        :param Description: 仓库详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param BriefDescription: 简单描述
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefDescription: str
        :param UpdateTime: 更新时间，格式"2006-01-02 15:04:05.999999999 -0700 MST"
        :type UpdateTime: str
        """
        self.Name = None
        self.Namespace = None
        self.CreationTime = None
        self.Public = None
        self.Description = None
        self.BriefDescription = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.Description = params.get("Description")
        self.BriefDescription = params.get("BriefDescription")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInvokeCondition(AbstractModel):
    """触发器触发条件

    """

    def __init__(self):
        r"""
        :param InvokeMethod: 触发方式
        :type InvokeMethod: str
        :param InvokeExpr: 触发表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeExpr: str
        """
        self.InvokeMethod = None
        self.InvokeExpr = None


    def _deserialize(self, params):
        self.InvokeMethod = params.get("InvokeMethod")
        self.InvokeExpr = params.get("InvokeExpr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInvokePara(AbstractModel):
    """触发器触发参数

    """

    def __init__(self):
        r"""
        :param AppId: AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param ClusterId: TKE集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Namespace: TKE集群命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param ServiceName: TKE集群工作负载名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param ContainerName: TKE集群工作负载中容器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param ClusterRegion: TKE集群地域数字ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterRegion: int
        """
        self.AppId = None
        self.ClusterId = None
        self.Namespace = None
        self.ServiceName = None
        self.ContainerName = None
        self.ClusterRegion = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.ServiceName = params.get("ServiceName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInvokeResult(AbstractModel):
    """触发器触发结果

    """

    def __init__(self):
        r"""
        :param ReturnCode: 请求TKE返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: int
        :param ReturnMsg: 请求TKE返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        """
        self.ReturnCode = None
        self.ReturnMsg = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerLogResp(AbstractModel):
    """触发器日志

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param TagName: Tag名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param InvokeSource: 触发方式
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param InvokeTime: 触发时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeTime: str
        :param InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param InvokePara: 触发参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`
        :param InvokeResult: 触发结果
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeResult: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeResult`
        """
        self.RepoName = None
        self.TagName = None
        self.TriggerName = None
        self.InvokeSource = None
        self.InvokeAction = None
        self.InvokeTime = None
        self.InvokeCondition = None
        self.InvokePara = None
        self.InvokeResult = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeSource = params.get("InvokeSource")
        self.InvokeAction = params.get("InvokeAction")
        self.InvokeTime = params.get("InvokeTime")
        if params.get("InvokeCondition") is not None:
            self.InvokeCondition = TriggerInvokeCondition()
            self.InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self.InvokePara = TriggerInvokePara()
            self.InvokePara._deserialize(params.get("InvokePara"))
        if params.get("InvokeResult") is not None:
            self.InvokeResult = TriggerInvokeResult()
            self.InvokeResult._deserialize(params.get("InvokeResult"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerResp(AbstractModel):
    """触发器返回值

    """

    def __init__(self):
        r"""
        :param TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param InvokeSource: 触发来源
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param InvokePara: 触发器参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`
        """
        self.TriggerName = None
        self.InvokeSource = None
        self.InvokeAction = None
        self.CreateTime = None
        self.UpdateTime = None
        self.InvokeCondition = None
        self.InvokePara = None


    def _deserialize(self, params):
        self.TriggerName = params.get("TriggerName")
        self.InvokeSource = params.get("InvokeSource")
        self.InvokeAction = params.get("InvokeAction")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("InvokeCondition") is not None:
            self.InvokeCondition = TriggerInvokeCondition()
            self.InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self.InvokePara = TriggerInvokePara()
            self.InvokePara._deserialize(params.get("InvokePara"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValidateNamespaceExistPersonalRequest(AbstractModel):
    """ValidateNamespaceExistPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValidateNamespaceExistPersonalResponse(AbstractModel):
    """ValidateNamespaceExistPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 验证命名空间是否存在返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceIsExistsResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = NamespaceIsExistsResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ValidateRepositoryExistPersonalRequest(AbstractModel):
    """ValidateRepositoryExistPersonal请求参数结构体

    """

    def __init__(self):
        r"""
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValidateRepositoryExistPersonalResponse(AbstractModel):
    """ValidateRepositoryExistPersonal返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 验证个人版仓库是否存在返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoIsExistResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepoIsExistResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class VpcAndDomainInfo(AbstractModel):
    """vpc和domain信息

    """

    def __init__(self):
        r"""
        :param InstanceId: tcr实例id
        :type InstanceId: str
        :param VpcId: 私有网络id
        :type VpcId: str
        :param EniLBIp: tcr内网访问链路ip
        :type EniLBIp: str
        :param UsePublicDomain: true：use instance name as subdomain
false: use instancename+"-vpc" as subdomain
        :type UsePublicDomain: bool
        :param RegionName: 解析地域，需要保证和vpc处于同一地域，如果不填则默认为主实例地域
        :type RegionName: str
        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.UsePublicDomain = None
        self.RegionName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.EniLBIp = params.get("EniLBIp")
        self.UsePublicDomain = params.get("UsePublicDomain")
        self.RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcPrivateDomainStatus(AbstractModel):
    """vpc私有域名解析状态

    """

    def __init__(self):
        r"""
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param VpcId: unique vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param Status: ENABLE代表已经开启，DISABLE代表未开启，ERROR代表查询出错
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.Region = None
        self.VpcId = None
        self.Status = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTarget(AbstractModel):
    """触发器目标

    """

    def __init__(self):
        r"""
        :param Address: 目标地址
        :type Address: str
        :param Headers: 自定义 Headers
        :type Headers: list of Header
        """
        self.Address = None
        self.Headers = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTrigger(AbstractModel):
    """Webhook 触发器

    """

    def __init__(self):
        r"""
        :param Name: 触发器名称
        :type Name: str
        :param Targets: 触发器目标
        :type Targets: list of WebhookTarget
        :param EventTypes: 触发动作
        :type EventTypes: list of str
        :param Condition: 触发规则
        :type Condition: str
        :param Enabled: 启用触发器
        :type Enabled: bool
        :param Id: 触发器Id
        :type Id: int
        :param Description: 触发器描述
        :type Description: str
        :param NamespaceId: 触发器所属命名空间 Id
        :type NamespaceId: int
        """
        self.Name = None
        self.Targets = None
        self.EventTypes = None
        self.Condition = None
        self.Enabled = None
        self.Id = None
        self.Description = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = WebhookTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EventTypes = params.get("EventTypes")
        self.Condition = params.get("Condition")
        self.Enabled = params.get("Enabled")
        self.Id = params.get("Id")
        self.Description = params.get("Description")
        self.NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookTriggerLog(AbstractModel):
    """触发器日志

    """

    def __init__(self):
        r"""
        :param Id: 日志 Id
        :type Id: int
        :param TriggerId: 触发器 Id
        :type TriggerId: int
        :param EventType: 事件类型
        :type EventType: str
        :param NotifyType: 通知类型
        :type NotifyType: str
        :param Detail: 详情
        :type Detail: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Status: 状态
        :type Status: str
        """
        self.Id = None
        self.TriggerId = None
        self.EventType = None
        self.NotifyType = None
        self.Detail = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TriggerId = params.get("TriggerId")
        self.EventType = params.get("EventType")
        self.NotifyType = params.get("NotifyType")
        self.Detail = params.get("Detail")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        