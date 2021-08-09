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
        """
        :param VpcId: Vpc的Id\n        :type VpcId: str\n        :param SubnetId: 子网Id\n        :type SubnetId: str\n        :param Status: 内网接入状态\n        :type Status: str\n        :param AccessIp: 内网接入Ip\n        :type AccessIp: str\n        """
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
        """
        :param Username: 用户名\n        :type Username: str\n        :param RepoName: 仓库名\n        :type RepoName: str\n        :param Type: 类型\n        :type Type: str\n        :param Value: 策略值\n        :type Value: int\n        :param Valid: Valid\n        :type Valid: int\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        """
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
        """
        :param TotalCount: 总数目\n        :type TotalCount: int\n        :param StrategyInfo: 自动删除策略列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type StrategyInfo: list of AutoDelStrategyInfo\n        """
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
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Tags: Tag列表\n        :type Tags: list of str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchDeleteRepositoryPersonalRequest(AbstractModel):
    """BatchDeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoNames: 仓库名称数组\n        :type RepoNames: list of str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckInstanceNameRequest(AbstractModel):
    """CheckInstanceName请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryName: 待创建的实例名称\n        :type RegistryName: str\n        """
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
        """
        :param IsValidated: 检查结果，true为合法，false为非法\n        :type IsValidated: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IsValidated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValidated = params.get("IsValidated")
        self.RequestId = params.get("RequestId")


class CheckInstanceRequest(AbstractModel):
    """CheckInstance请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 待检测的实例Id\n        :type RegistryId: str\n        """
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
        """
        :param IsValidated: 检查结果，true为合法，false为非法\n        :type IsValidated: bool\n        :param RegionId: 实例所在的RegionId\n        :type RegionId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 触发器关联的镜像仓库，library/test格式\n        :type RepoName: str\n        :param TriggerName: 触发器名称\n        :type TriggerName: str\n        :param InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发\n        :type InvokeMethod: str\n        :param ClusterId: 应用所在TKE集群ID\n        :type ClusterId: str\n        :param Namespace: 应用所在TKE集群命名空间\n        :type Namespace: str\n        :param WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。\n        :type WorkloadType: str\n        :param WorkloadName: 应用所在TKE集群工作负载名称\n        :type WorkloadName: str\n        :param ContainerName: 应用所在TKE集群工作负载下容器名称\n        :type ContainerName: str\n        :param ClusterRegion: 应用所在TKE集群地域\n        :type ClusterRegion: int\n        :param InvokeExpr: 触发方式对应的表达式\n        :type InvokeExpr: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateImageLifecyclePersonalRequest(AbstractModel):
    """CreateImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Type: keep_last_days:保留最近几天的数据;keep_last_nums:保留最近多少个\n        :type Type: str\n        :param Val: 策略值\n        :type Val: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateImmutableTagRulesRequest(AbstractModel):
    """CreateImmutableTagRules请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 Id\n        :type RegistryId: str\n        :param NamespaceName: 命名空间\n        :type NamespaceName: str\n        :param Rule: 规则\n        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryName: 企业版实例名称\n        :type RegistryName: str\n        :param RegistryType: 企业版实例类型（basic 基础版；standard 标准版；premium 高级版）\n        :type RegistryType: str\n        :param TagSpecification: 云标签描述\n        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`\n        :param RegistryChargeType: 实例计费类型，0表示按量计费，1表示预付费，默认为按量计费\n        :type RegistryChargeType: int\n        """
        self.RegistryName = None
        self.RegistryType = None
        self.TagSpecification = None
        self.RegistryChargeType = None


    def _deserialize(self, params):
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = TagSpecification()
            self.TagSpecification._deserialize(params.get("TagSpecification"))
        self.RegistryChargeType = params.get("RegistryChargeType")
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
        """
        :param RegistryId: 企业版实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param TokenType: 访问凭证类型，longterm 为长期访问凭证，temp 为临时访问凭证，默认是临时访问凭证，有效期1小时\n        :type TokenType: str\n        :param Desc: 长期访问凭证描述信息\n        :type Desc: str\n        """
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
        """
        :param Username: 用户名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Username: str\n        :param Token: 访问凭证\n        :type Token: str\n        :param ExpTime: 访问凭证过期时间戳\n        :type ExpTime: int\n        :param TokenId: 长期凭证的TokenId，短期凭证没有TokenId
注意：此字段可能返回 null，表示取不到有效值。\n        :type TokenId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param InstanceId: tcr实例id\n        :type InstanceId: str\n        :param VpcId: 私有网络id\n        :type VpcId: str\n        :param EniLBIp: tcr内网访问链路ip\n        :type EniLBIp: str\n        :param UsePublicDomain: true：为默认域名，公网域名一致
false: 使用vpc域名
默认为vpc域名\n        :type UsePublicDomain: bool\n        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.UsePublicDomain = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.EniLBIp = params.get("EniLBIp")
        self.UsePublicDomain = params.get("UsePublicDomain")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMultipleSecurityPolicyRequest(AbstractModel):
    """CreateMultipleSecurityPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param SecurityGroupPolicySet: 安全组策略\n        :type SecurityGroupPolicySet: list of SecurityPolicy\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateNamespacePersonalRequest(AbstractModel):
    """CreateNamespacePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称\n        :type Namespace: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间的名称\n        :type NamespaceName: str\n        :param IsPublic: 是否公开，true为公开，fale为私有\n        :type IsPublic: bool\n        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateReplicationInstanceRequest(AbstractModel):
    """CreateReplicationInstance请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param ReplicationRegionId: 复制实例地域ID\n        :type ReplicationRegionId: int\n        """
        self.RegistryId = None
        self.ReplicationRegionId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.ReplicationRegionId = params.get("ReplicationRegionId")
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
        """
        :param ReplicationRegistryId: 企业版复制实例Id\n        :type ReplicationRegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReplicationRegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationRegistryId = params.get("ReplicationRegistryId")
        self.RequestId = params.get("RequestId")


class CreateRepositoryPersonalRequest(AbstractModel):
    """CreateRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Public: 是否公共,1:公共,0:私有\n        :type Public: int\n        :param Description: 仓库描述\n        :type Description: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param RepositoryName: 仓库名称\n        :type RepositoryName: str\n        :param BriefDescription: 仓库简短描述\n        :type BriefDescription: str\n        :param Description: 仓库详细描述\n        :type Description: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param CidrBlock: 192.168.0.0/24\n        :type CidrBlock: str\n        :param Description: 备注\n        :type Description: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateTagRetentionExecutionRequest(AbstractModel):
    """CreateTagRetentionExecution请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param RetentionId: 版本保留规则Id\n        :type RetentionId: int\n        :param DryRun: 是否模拟执行\n        :type DryRun: bool\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRetentionRuleRequest(AbstractModel):
    """CreateTagRetentionRule请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param NamespaceId: 命名空间的Id\n        :type NamespaceId: int\n        :param RetentionRule: 保留策略\n        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`\n        :param CronSetting: 执行周期，当前只能选择： manual;daily;weekly;monthly\n        :type CronSetting: str\n        :param Disabled: 是否禁用规则\n        :type Disabled: bool\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUserPersonalRequest(AbstractModel):
    """CreateUserPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Password: 用户密码\n        :type Password: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 Id\n        :type RegistryId: str\n        :param Trigger: 触发器参数\n        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`\n        :param Namespace: 命名空间\n        :type Namespace: str\n        """
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
        """
        :param Trigger: 新建的触发器\n        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Trigger = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.RequestId = params.get("RequestId")


class DeleteApplicationTriggerPersonalRequest(AbstractModel):
    """DeleteApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param TriggerName: 触发器名称\n        :type TriggerName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageLifecyclePersonalRequest(AbstractModel):
    """DeleteImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImagePersonalRequest(AbstractModel):
    """DeleteImagePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Tag: Tag名\n        :type Tag: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RepositoryName: 镜像仓库名称\n        :type RepositoryName: str\n        :param ImageVersion: 镜像版本\n        :type ImageVersion: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImmutableTagRulesRequest(AbstractModel):
    """DeleteImmutableTagRules请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 Id\n        :type RegistryId: str\n        :param NamespaceName: 命名空间\n        :type NamespaceName: str\n        :param RuleId: 规则 Id\n        :type RuleId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例id\n        :type RegistryId: str\n        :param DeleteBucket: 是否删除存储桶，默认为false\n        :type DeleteBucket: bool\n        """
        self.RegistryId = None
        self.DeleteBucket = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.DeleteBucket = params.get("DeleteBucket")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 ID\n        :type RegistryId: str\n        :param TokenId: 访问凭证 ID\n        :type TokenId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInternalEndpointDnsRequest(AbstractModel):
    """DeleteInternalEndpointDns请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: tcr实例id\n        :type InstanceId: str\n        :param VpcId: 私有网络id\n        :type VpcId: str\n        :param EniLBIp: tcr内网访问链路ip\n        :type EniLBIp: str\n        :param UsePublicDomain: true：use instance name as subdomain
false: use instancename+"-vpc" as subdomain\n        :type UsePublicDomain: bool\n        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.UsePublicDomain = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.EniLBIp = params.get("EniLBIp")
        self.UsePublicDomain = params.get("UsePublicDomain")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMultipleSecurityPolicyRequest(AbstractModel):
    """DeleteMultipleSecurityPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param SecurityGroupPolicySet: 安全组策略\n        :type SecurityGroupPolicySet: list of SecurityPolicy\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DeleteNamespacePersonalRequest(AbstractModel):
    """DeleteNamespacePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称\n        :type Namespace: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间的名称\n        :type NamespaceName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryPersonalRequest(AbstractModel):
    """DeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param NamespaceName: 命名空间的名称\n        :type NamespaceName: str\n        :param RepositoryName: 仓库名称的名称\n        :type RepositoryName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param PolicyIndex: 白名单Id\n        :type PolicyIndex: int\n        :param PolicyVersion: 白名单版本\n        :type PolicyVersion: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class DeleteTagRetentionRuleRequest(AbstractModel):
    """DeleteTagRetentionRule请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param RetentionId: 版本保留规则的Id\n        :type RetentionId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param Namespace: 命名空间\n        :type Namespace: str\n        :param Id: 触发器 Id\n        :type Id: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeApplicationTriggerLogPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerLogPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回最大数量，默认 20, 最大值 100\n        :type Limit: int\n        :param Order: 升序或降序\n        :type Order: str\n        :param OrderBy: 按某列排序\n        :type OrderBy: str\n        """
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
        """
        :param TotalCount: 返回总数\n        :type TotalCount: int\n        :param LogInfo: 触发日志列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogInfo: list of TriggerLogResp\n        """
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
        """
        :param Data: 触发日志返回值\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param TriggerName: 触发器名称\n        :type TriggerName: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回最大数量，默认 20, 最大值 100\n        :type Limit: int\n        """
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
        """
        :param TotalCount: 返回条目总数\n        :type TotalCount: int\n        :param TriggerInfo: 触发器列表\n        :type TriggerInfo: list of TriggerResp\n        """
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
        """
        :param Data: 触发器列表返回值\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间\n        :type NamespaceName: str\n        :param ChartName: Chart包的名称\n        :type ChartName: str\n        :param ChartVersion: Chart包的版本\n        :type ChartVersion: str\n        """
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
        """
        :param PreSignedDownloadURL: 用于下载的url的预签名地址\n        :type PreSignedDownloadURL: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PreSignedDownloadURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedDownloadURL = params.get("PreSignedDownloadURL")
        self.RequestId = params.get("RequestId")


class DescribeExternalEndpointStatusRequest(AbstractModel):
    """DescribeExternalEndpointStatus请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        """
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
        """
        :param Status: 开启公网访问状态，开启中（Opening）、已开启（Opened）、关闭（Closed）\n        :type Status: str\n        :param Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reason: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Limit: 分页Limit\n        :type Limit: int\n        :param Offset: Offset用于分页\n        :type Offset: int\n        """
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
        """
        :param Data: 个人收藏仓库列表返回信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.FavorResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = FavorResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageFilterPersonalRequest(AbstractModel):
    """DescribeImageFilterPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Tag: Tag名\n        :type Tag: str\n        """
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
        """
        :param Data: payload\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.SameImagesResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Data: 全局自动删除策略信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        """
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
        """
        :param Data: 自动删除策略信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param RepositoryName: 镜像仓库名称\n        :type RepositoryName: str\n        :param ImageVersion: 镜像版本\n        :type ImageVersion: str\n        """
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
        """
        :param Manifest: 镜像的Manifest信息\n        :type Manifest: str\n        :param Config: 镜像的配置信息\n        :type Config: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回最大数量，默认 20, 最大值 100\n        :type Limit: int\n        :param Tag: tag名称，可根据输入搜索\n        :type Tag: str\n        """
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
        """
        :param Data: 镜像tag信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.TagInfoResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param RepositoryName: 镜像仓库名称\n        :type RepositoryName: str\n        :param ImageVersion: 指定镜像版本进行查找，当前为模糊搜索\n        :type ImageVersion: str\n        :param Limit: 每页个数，用于分页，默认20\n        :type Limit: int\n        :param Offset: 页数，默认值为1\n        :type Offset: int\n        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        """
        :param ImageInfoList: 容器镜像信息列表\n        :type ImageInfoList: list of TcrImageInfo\n        :param TotalCount: 容器镜像总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例 Id\n        :type RegistryId: str\n        """
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
        """
        :param Rules: 规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rules: list of ImmutableTagRule\n        :param EmptyNs: 未创建规则的命名空间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EmptyNs: list of str\n        :param Total: 规则总量\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeInstanceStatusRequest(AbstractModel):
    """DescribeInstanceStatus请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryIds: 实例ID的数组\n        :type RegistryIds: list of str\n        """
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
        """
        :param RegistryStatusSet: 实例的状态列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegistryStatusSet: list of RegistryStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例 ID\n        :type RegistryId: str\n        :param Limit: 分页单页数量\n        :type Limit: int\n        :param Offset: 分页偏移量\n        :type Offset: int\n        """
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
        """
        :param TotalCount: 长期访问凭证总数\n        :type TotalCount: int\n        :param Tokens: 长期访问凭证列表\n        :type Tokens: list of TcrInstanceToken\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Registryids: 实例ID列表(为空时，
表示获取账号下所有实例)\n        :type Registryids: list of str\n        :param Offset: 偏移量,默认0\n        :type Offset: int\n        :param Limit: 最大输出条数，默认20，最大为100\n        :type Limit: int\n        :param Filters: 过滤条件\n        :type Filters: list of Filter\n        :param AllRegion: 获取所有地域的实例，默认为False\n        :type AllRegion: bool\n        """
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
        """
        :param TotalCount: 总实例个数\n        :type TotalCount: int\n        :param Registries: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Registries: list of Registry\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param VpcSet: vpc列表\n        :type VpcSet: list of VpcAndDomainInfo\n        """
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
        """
        :param VpcSet: vpc私有域名解析状态列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcSet: list of VpcPrivateDomainStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        """
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
        """
        :param AccessVpcSet: 内网接入信息的列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessVpcSet: list of AccessVpc\n        :param TotalCount: 内网接入总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Namespace: 命名空间，支持模糊查询\n        :type Namespace: str\n        :param Limit: 单页数量\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        """
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
        """
        :param Data: 用户命名空间返回信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceInfoResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param NamespaceName: 指定命名空间，不填写默认查询所有命名空间\n        :type NamespaceName: str\n        :param Limit: 每页个数\n        :type Limit: int\n        :param Offset: 页偏移\n        :type Offset: int\n        """
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
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param NamespaceList: 命名空间列表信息\n        :type NamespaceList: list of TcrNamespaceInfo\n        :param TotalCount: 总个数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeReplicationInstanceCreateTasksRequest(AbstractModel):
    """DescribeReplicationInstanceCreateTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ReplicationRegistryId: 同步实例Id\n        :type ReplicationRegistryId: str\n        :param ReplicationRegionId: 同步实例的地域ID\n        :type ReplicationRegionId: int\n        """
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
        """
        :param TaskDetail: 任务详情\n        :type TaskDetail: list of TaskDetail\n        :param Status: 整体任务状态\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 主实例Id\n        :type RegistryId: str\n        :param ReplicationRegistryId: 复制实例Id\n        :type ReplicationRegistryId: str\n        :param ReplicationRegionId: 复制实例的地域Id\n        :type ReplicationRegionId: int\n        """
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
        


class DescribeReplicationInstanceSyncStatusResponse(AbstractModel):
    """DescribeReplicationInstanceSyncStatus返回参数结构体

    """

    def __init__(self):
        """
        :param ReplicationStatus: 同步状态\n        :type ReplicationStatus: str\n        :param ReplicationTime: 同步完成时间\n        :type ReplicationTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReplicationStatus = None
        self.ReplicationTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplicationStatus = params.get("ReplicationStatus")
        self.ReplicationTime = params.get("ReplicationTime")
        self.RequestId = params.get("RequestId")


class DescribeReplicationInstancesRequest(AbstractModel):
    """DescribeReplicationInstances请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param Offset: 偏移量,默认0\n        :type Offset: int\n        :param Limit: 最大输出条数，默认20，最大为100\n        :type Limit: int\n        """
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
        """
        :param TotalCount: 总实例个数\n        :type TotalCount: int\n        :param ReplicationRegistries: 同步实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReplicationRegistries: list of ReplicationRegistry\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param NamespaceName: 指定命名空间，不填写默认为查询所有命名空间下镜像仓库\n        :type NamespaceName: str\n        :param RepositoryName: 指定镜像仓库，不填写默认查询指定命名空间下所有镜像仓库\n        :type RepositoryName: str\n        :param Offset: 页数，用于分页\n        :type Offset: int\n        :param Limit: 每页个数，用于分页\n        :type Limit: int\n        :param SortBy: 基于字段排序，支持的值有-creation_time,-name, -update_time\n        :type SortBy: str\n        """
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
        """
        :param RepositoryList: 仓库信息列表\n        :type RepositoryList: list of TcrRepositoryInfo\n        :param TotalCount: 总个数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 搜索镜像名\n        :type RepoName: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回最大数量，默认 20，最大100\n        :type Limit: int\n        :param Public: 筛选条件：1表示public，0表示private\n        :type Public: int\n        :param Namespace: 命名空间\n        :type Namespace: str\n        """
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
        """
        :param Data: 仓库信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.SearchUserRepositoryResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回最大数量，默认 20, 最大值 100\n        :type Limit: int\n        :param RepoName: 仓库名称\n        :type RepoName: str\n        """
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
        """
        :param Data: 仓库信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoInfoResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 仓库名字\n        :type RepoName: str\n        """
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
        """
        :param Data: 仓库信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepositoryInfoResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例的Id\n        :type RegistryId: str\n        """
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
        """
        :param SecurityPolicySet: 实例安全策略组
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityPolicySet: list of SecurityPolicy\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param RetentionId: 规则Id\n        :type RetentionId: int\n        :param Limit: 分页PageSize\n        :type Limit: int\n        :param Offset: 分页Page\n        :type Offset: int\n        """
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
        """
        :param RetentionExecutionList: 版本保留执行记录列表\n        :type RetentionExecutionList: list of RetentionExecution\n        :param TotalCount: 版本保留执行记录总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param RetentionId: 规则Id\n        :type RetentionId: int\n        :param ExecutionId: 规则执行Id\n        :type ExecutionId: int\n        :param Offset: 分页Page\n        :type Offset: int\n        :param Limit: 分页PageSize\n        :type Limit: int\n        """
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
        """
        :param RetentionTaskList: 版本保留执行任务列表\n        :type RetentionTaskList: list of RetentionTask\n        :param TotalCount: 版本保留执行任务总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param NamespaceName: 命名空间的名称\n        :type NamespaceName: str\n        :param Limit: 分页PageSize\n        :type Limit: int\n        :param Offset: 分页Page\n        :type Offset: int\n        """
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
        """
        :param RetentionPolicyList: 版本保留策略列表\n        :type RetentionPolicyList: list of RetentionPolicy\n        :param TotalCount: 版本保留策略总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Data: 配额返回信息\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.RespLimit`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例 Id\n        :type RegistryId: str\n        :param Namespace: 命名空间\n        :type Namespace: str\n        :param Id: 触发器 Id\n        :type Id: int\n        :param Limit: 分页单页数量\n        :type Limit: int\n        :param Offset: 分页偏移量\n        :type Offset: int\n        """
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
        """
        :param TotalCount: 总数\n        :type TotalCount: int\n        :param Logs: 日志列表\n        :type Logs: list of WebhookTriggerLog\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param Limit: 分页单页数量\n        :type Limit: int\n        :param Offset: 分页偏移量\n        :type Offset: int\n        :param Namespace: 命名空间\n        :type Namespace: str\n        """
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
        """
        :param TotalCount: 触发器总数\n        :type TotalCount: int\n        :param Triggers: 触发器列表\n        :type Triggers: list of WebhookTrigger\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param ChartName: Helm chart名称\n        :type ChartName: str\n        :param ChartVersion: Helm chart版本\n        :type ChartVersion: str\n        """
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
        """
        :param TmpToken: 临时token\n        :type TmpToken: str\n        :param TmpSecretId: 临时的secretId\n        :type TmpSecretId: str\n        :param TmpSecretKey: 临时的secretKey\n        :type TmpSecretKey: str\n        :param Bucket: 存储桶信息\n        :type Bucket: str\n        :param Region: 实例ID\n        :type Region: str\n        :param Path: chart信息\n        :type Path: str\n        :param StartTime: 开始时间时间戳\n        :type StartTime: int\n        :param ExpiredTime: token过期时间时间戳\n        :type ExpiredTime: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Digest: 镜像Digest值\n        :type Digest: str\n        """
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
        """
        :param SrcImage: 源镜像名称，不包含domain。例如： tencentyun/foo:v1\n        :type SrcImage: str\n        :param DestImage: 目的镜像名称，不包含domain。例如： tencentyun/foo:latest\n        :type DestImage: str\n        """
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
        """
        :param Data: 复制镜像返回值\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.DupImageTagResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TotalCount: 收藏仓库的总数\n        :type TotalCount: int\n        :param RepoInfo: 仓库信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepoInfo: list of Favors\n        """
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
        """
        :param RepoName: 仓库名字\n        :type RepoName: str\n        :param RepoType: 仓库类型\n        :type RepoType: str\n        :param PullCount: Pull总共的次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PullCount: int\n        :param FavorCount: 仓库收藏次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type FavorCount: int\n        :param Public: 仓库是否公开
注意：此字段可能返回 null，表示取不到有效值。\n        :type Public: int\n        :param IsQcloudOfficial: 是否为官方所有
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsQcloudOfficial: bool\n        :param TagCount: 仓库Tag的数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagCount: int\n        :param Logo: Logo
注意：此字段可能返回 null，表示取不到有效值。\n        :type Logo: str\n        :param Region: 地域\n        :type Region: str\n        :param RegionId: 地域的Id\n        :type RegionId: int\n        """
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
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。\n        :type Name: str\n        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。\n        :type Values: list of str\n        """
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
        


class Header(AbstractModel):
    """Header KV

    """

    def __init__(self):
        """
        :param Key: Header Key\n        :type Key: str\n        :param Values: Header Values\n        :type Values: list of str\n        """
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
        """
        :param RepositoryPattern: 仓库匹配规则\n        :type RepositoryPattern: str\n        :param TagPattern: Tag 匹配规则\n        :type TagPattern: str\n        :param RepositoryDecoration: repoMatches或repoExcludes\n        :type RepositoryDecoration: str\n        :param TagDecoration: matches或excludes\n        :type TagDecoration: str\n        :param Disabled: 禁用规则\n        :type Disabled: bool\n        :param RuleId: 规则 Id\n        :type RuleId: int\n        :param NsName: 命名空间\n        :type NsName: str\n        """
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
        


class Limit(AbstractModel):
    """共享镜像仓库用户配额

    """

    def __init__(self):
        """
        :param Username: 用户名\n        :type Username: str\n        :param Type: 配额的类型\n        :type Type: str\n        :param Value: 配置的值\n        :type Value: int\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param Operation: 操作（Create/Delete）\n        :type Operation: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ManageImageLifecycleGlobalPersonalRequest(AbstractModel):
    """ManageImageLifecycleGlobalPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Type: global_keep_last_days:全局保留最近几天的数据;global_keep_last_nums:全局保留最近多少个\n        :type Type: str\n        :param Val: 策略值\n        :type Val: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ManageInternalEndpointRequest(AbstractModel):
    """ManageInternalEndpoint请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param Operation: Create/Delete\n        :type Operation: str\n        :param VpcId: 需要接入的用户vpcid\n        :type VpcId: str\n        :param SubnetId: 需要接入的用户子网id\n        :type SubnetId: str\n        :param RegionId: 请求的地域ID\n        :type RegionId: int\n        """
        self.RegistryId = None
        self.Operation = None
        self.VpcId = None
        self.SubnetId = None
        self.RegionId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Operation = params.get("Operation")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.RegionId = params.get("RegionId")
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ManageReplicationRequest(AbstractModel):
    """ManageReplication请求参数结构体

    """

    def __init__(self):
        """
        :param SourceRegistryId: 复制源实例ID\n        :type SourceRegistryId: str\n        :param DestinationRegistryId: 复制目标实例ID\n        :type DestinationRegistryId: str\n        :param Rule: 同步规则\n        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ReplicationRule`\n        :param Description: 规则描述\n        :type Description: str\n        :param DestinationRegionId: 目标实例的地域ID，如广州是1\n        :type DestinationRegionId: int\n        :param PeerReplicationOption: 开启跨主账号实例同步配置项\n        :type PeerReplicationOption: :class:`tencentcloud.tcr.v20190924.models.PeerReplicationOption`\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationTriggerPersonalRequest(AbstractModel):
    """ModifyApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 触发器关联的镜像仓库，library/test格式\n        :type RepoName: str\n        :param TriggerName: 触发器名称\n        :type TriggerName: str\n        :param InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发\n        :type InvokeMethod: str\n        :param InvokeExpr: 触发方式对应的表达式\n        :type InvokeExpr: str\n        :param ClusterId: 应用所在TKE集群ID\n        :type ClusterId: str\n        :param Namespace: 应用所在TKE集群命名空间\n        :type Namespace: str\n        :param WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。\n        :type WorkloadType: str\n        :param WorkloadName: 应用所在TKE集群工作负载名称\n        :type WorkloadName: str\n        :param ContainerName: 应用所在TKE集群工作负载下容器名称\n        :type ContainerName: str\n        :param ClusterRegion: 应用所在TKE集群地域数字ID，如1（广州）、16（成都）\n        :type ClusterRegion: int\n        :param NewTriggerName: 新触发器名称\n        :type NewTriggerName: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImmutableTagRulesRequest(AbstractModel):
    """ModifyImmutableTagRules请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 Id\n        :type RegistryId: str\n        :param NamespaceName: 命名空间\n        :type NamespaceName: str\n        :param RuleId: 规则 Id\n        :type RuleId: int\n        :param Rule: 规则\n        :type Rule: :class:`tencentcloud.tcr.v20190924.models.ImmutableTagRule`\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceTokenRequest(AbstractModel):
    """ModifyInstanceToken请求参数结构体

    """

    def __init__(self):
        """
        :param TokenId: 实例长期访问凭证 ID\n        :type TokenId: str\n        :param RegistryId: 实例 ID\n        :type RegistryId: str\n        :param Enable: 启用或禁用实例长期访问凭证\n        :type Enable: bool\n        :param Desc: 访问凭证描述\n        :type Desc: str\n        :param ModifyFlag: 1为修改描述 2为启动禁用，不填写默认为修改启动禁用\n        :type ModifyFlag: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param IsPublic: 访问级别，True为公开，False为私有\n        :type IsPublic: bool\n        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryAccessPersonalRequest(AbstractModel):
    """ModifyRepositoryAccessPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Public: 默认值为0\n        :type Public: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryInfoPersonalRequest(AbstractModel):
    """ModifyRepositoryInfoPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param Description: 仓库描述\n        :type Description: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryRequest(AbstractModel):
    """ModifyRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param RepositoryName: 镜像仓库名称\n        :type RepositoryName: str\n        :param BriefDescription: 仓库简短描述\n        :type BriefDescription: str\n        :param Description: 仓库详细描述\n        :type Description: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例的Id\n        :type RegistryId: str\n        :param PolicyIndex: PolicyId\n        :type PolicyIndex: int\n        :param CidrBlock: 192.168.0.0/24 白名单Ip\n        :type CidrBlock: str\n        :param Description: 备注\n        :type Description: str\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ModifyTagRetentionRuleRequest(AbstractModel):
    """ModifyTagRetentionRule请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 主实例iD\n        :type RegistryId: str\n        :param NamespaceId: 命名空间的Id，必须填写原有的命名空间id\n        :type NamespaceId: int\n        :param RetentionRule: 保留策略\n        :type RetentionRule: :class:`tencentcloud.tcr.v20190924.models.RetentionRule`\n        :param CronSetting: 执行周期，必须填写为原来的设置\n        :type CronSetting: str\n        :param RetentionId: 规则Id\n        :type RetentionId: int\n        :param Disabled: 是否禁用规则\n        :type Disabled: bool\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserPasswordPersonalRequest(AbstractModel):
    """ModifyUserPasswordPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Password: 更新后的密码\n        :type Password: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param Trigger: 触发器参数\n        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`\n        :param Namespace: 命名空间\n        :type Namespace: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NamespaceInfo(AbstractModel):
    """命名空间信息

    """

    def __init__(self):
        """
        :param Namespace: 命名空间\n        :type Namespace: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param RepoCount: 命名空间下仓库数量\n        :type RepoCount: int\n        """
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
        """
        :param NamespaceCount: 命名空间数量\n        :type NamespaceCount: int\n        :param NamespaceInfo: 命名空间信息\n        :type NamespaceInfo: list of NamespaceInfo\n        """
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
        """
        :param IsExist: 命名空间是否存在\n        :type IsExist: bool\n        :param IsPreserved: 是否为保留命名空间\n        :type IsPreserved: bool\n        """
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
        """
        :param PeerRegistryUin: 待同步实例的uin\n        :type PeerRegistryUin: str\n        :param PeerRegistryToken: 待同步实例的访问永久Token\n        :type PeerRegistryToken: str\n        :param EnablePeerReplication: 是否开启跨主账号实例同步\n        :type EnablePeerReplication: bool\n        """
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
        


class Registry(AbstractModel):
    """实例信息结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID\n        :type RegistryId: str\n        :param RegistryName: 实例名称\n        :type RegistryName: str\n        :param RegistryType: 实例规格\n        :type RegistryType: str\n        :param Status: 实例状态\n        :type Status: str\n        :param PublicDomain: 实例的公共访问地址\n        :type PublicDomain: str\n        :param CreatedAt: 实例创建时间\n        :type CreatedAt: str\n        :param RegionName: 地域名称\n        :type RegionName: str\n        :param RegionId: 地域Id\n        :type RegionId: int\n        :param EnableAnonymous: 是否支持匿名\n        :type EnableAnonymous: bool\n        :param TokenValidTime: Token有效时间\n        :type TokenValidTime: int\n        :param InternalEndpoint: 实例内部访问地址\n        :type InternalEndpoint: str\n        :param TagSpecification: 实例云标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSpecification: :class:`tencentcloud.tcr.v20190924.models.TagSpecification`\n        :param ExpiredAt: 实例过期时间（预付费）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpiredAt: str\n        :param PayMod: 实例付费类型，0表示后付费，1表示预付费
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayMod: int\n        :param RenewFlag: 预付费续费标识，0表示手动续费，1表示自动续费，2不续费并且不通知
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewFlag: int\n        """
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
        """
        :param Period: 购买实例的时长，单位：月\n        :type Period: int\n        :param RenewFlag: 自动续费标识，0：手动续费，1：自动续费，2：不续费并且不通知\n        :type RenewFlag: int\n        """
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
        """
        :param Type: 实例创建过程类型\n        :type Type: str\n        :param Status: 实例创建过程状态\n        :type Status: str\n        :param Reason: 转换到该过程的简明原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reason: str\n        """
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
        """
        :param RegistryId: 实例的Id\n        :type RegistryId: str\n        :param Status: 实例的状态\n        :type Status: str\n        :param Conditions: 附加状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Conditions: list of RegistryCondition\n        """
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
        """
        :param RegistryId: 实例Id\n        :type RegistryId: str\n        :param RegistryChargePrepaid: 预付费自动续费标识和购买时长\n        :type RegistryChargePrepaid: :class:`tencentcloud.tcr.v20190924.models.RegistryChargePrepaid`\n        :param Flag: 0 续费， 1按量转包年包月\n        :type Flag: int\n        """
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
        """
        :param RegistryId: 企业版实例Id\n        :type RegistryId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class ReplicationFilter(AbstractModel):
    """同步规则过滤器

    """

    def __init__(self):
        """
        :param Type: 类型（name、tag和resource）\n        :type Type: str\n        :param Value: 默认为空\n        :type Value: str\n        """
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
        


class ReplicationRegistry(AbstractModel):
    """企业版复制实例

    """

    def __init__(self):
        """
        :param RegistryId: 主实例ID\n        :type RegistryId: str\n        :param ReplicationRegistryId: 复制实例ID\n        :type ReplicationRegistryId: str\n        :param ReplicationRegionId: 复制实例的地域ID\n        :type ReplicationRegionId: int\n        :param ReplicationRegionName: 复制实例的地域名称\n        :type ReplicationRegionName: str\n        :param Status: 复制实例的状态\n        :type Status: str\n        :param CreatedAt: 创建时间\n        :type CreatedAt: str\n        """
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
        """
        :param Name: 同步规则名称\n        :type Name: str\n        :param DestNamespace: 目标命名空间\n        :type DestNamespace: str\n        :param Override: 是否覆盖\n        :type Override: bool\n        :param Filters: 同步过滤条件\n        :type Filters: list of ReplicationFilter\n        """
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
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        :param RepoType: 仓库类型\n        :type RepoType: str\n        :param TagCount: Tag数量\n        :type TagCount: int\n        :param Public: 是否为公开\n        :type Public: int\n        :param IsUserFavor: 是否为用户收藏\n        :type IsUserFavor: bool\n        :param IsQcloudOfficial: 是否为腾讯云官方仓库\n        :type IsQcloudOfficial: bool\n        :param FavorCount: 被收藏的个数\n        :type FavorCount: int\n        :param PullCount: 拉取的数量\n        :type PullCount: int\n        :param Description: 描述\n        :type Description: str\n        :param CreationTime: 仓库创建时间\n        :type CreationTime: str\n        :param UpdateTime: 仓库更新时间\n        :type UpdateTime: str\n        """
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
        """
        :param TotalCount: 仓库总数\n        :type TotalCount: int\n        :param RepoInfo: 仓库信息列表\n        :type RepoInfo: list of RepoInfo\n        :param Server: Server信息\n        :type Server: str\n        """
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
        """
        :param IsExist: 仓库是否存在\n        :type IsExist: bool\n        """
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
        """
        :param RepoName: 镜像仓库名字\n        :type RepoName: str\n        :param RepoType: 镜像仓库类型\n        :type RepoType: str\n        :param Server: 镜像仓库服务地址\n        :type Server: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param Description: 镜像仓库描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param Public: 是否为公有镜像\n        :type Public: int\n        :param PullCount: 下载次数\n        :type PullCount: int\n        :param FavorCount: 收藏次数\n        :type FavorCount: int\n        :param IsUserFavor: 是否为用户收藏\n        :type IsUserFavor: bool\n        :param IsQcloudOfficial: 是否为腾讯云官方镜像\n        :type IsQcloudOfficial: bool\n        """
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
        """
        :param LimitInfo: 配额信息\n        :type LimitInfo: list of Limit\n        """
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
        """
        :param ExecutionId: 执行Id\n        :type ExecutionId: int\n        :param RetentionId: 所属规则id\n        :type RetentionId: int\n        :param StartTime: 执行的开始时间\n        :type StartTime: str\n        :param EndTime: 执行的结束时间\n        :type EndTime: str\n        :param Status: 执行的状态，Failed, Succeed, Stopped, InProgress\n        :type Status: str\n        """
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
        """
        :param RetentionId: 版本保留策略Id\n        :type RetentionId: int\n        :param NamespaceName: 命名空间的名称\n        :type NamespaceName: str\n        :param RetentionRuleList: 规则列表\n        :type RetentionRuleList: list of RetentionRule\n        :param CronSetting: 定期执行方式\n        :type CronSetting: str\n        :param Disabled: 是否启用规则\n        :type Disabled: bool\n        :param NextExecutionTime: 基于当前时间根据cronSetting后下一次任务要执行的时间，仅做参考使用\n        :type NextExecutionTime: str\n        """
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
        """
        :param Key: 支持的策略，可选值为latestPushedK（保留最新推送多少个版本）nDaysSinceLastPush（保留近天内推送）\n        :type Key: str\n        :param Value: 规则设置下的对应值\n        :type Value: int\n        """
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
        """
        :param TaskId: 任务Id\n        :type TaskId: int\n        :param ExecutionId: 所属的规则执行Id\n        :type ExecutionId: int\n        :param StartTime: 任务开始时间\n        :type StartTime: str\n        :param EndTime: 任务结束时间\n        :type EndTime: str\n        :param Status: 任务的执行状态，Failed, Succeed, Stopped, InProgress\n        :type Status: str\n        :param Total: 总tag数\n        :type Total: int\n        :param Retained: 保留tag数\n        :type Retained: int\n        :param Repository: 应用的仓库\n        :type Repository: str\n        """
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
        """
        :param SameImages: tag列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SameImages: list of str\n        """
        self.SameImages = None


    def _deserialize(self, params):
        self.SameImages = params.get("SameImages")
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
        """
        :param TotalCount: 总个数\n        :type TotalCount: int\n        :param RepoInfo: 仓库列表\n        :type RepoInfo: list of RepoInfo\n        :param Server: Server\n        :type Server: str\n        :param PrivilegeFiltered: PrivilegeFiltered\n        :type PrivilegeFiltered: bool\n        """
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
        """
        :param PolicyIndex: 策略索引\n        :type PolicyIndex: int\n        :param Description: 备注\n        :type Description: str\n        :param CidrBlock: 运行访问的公网IP地址端\n        :type CidrBlock: str\n        :param PolicyVersion: 安全策略的版本\n        :type PolicyVersion: str\n        """
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
        """
        :param Key: 云标签的key\n        :type Key: str\n        :param Value: 云标签的值\n        :type Value: str\n        """
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
        """
        :param TagName: Tag名称\n        :type TagName: str\n        :param TagId: 镜像Id\n        :type TagId: str\n        :param ImageId: docker image 可以看到的id\n        :type ImageId: str\n        :param Size: 大小\n        :type Size: str\n        :param CreationTime: 镜像的创建时间\n        :type CreationTime: str\n        :param DurationDays: 镜像创建至今时间长度
注意：此字段可能返回 null，表示取不到有效值。\n        :type DurationDays: str\n        :param Author: 镜像的作者\n        :type Author: str\n        :param Architecture: 次镜像建议运行的系统架构\n        :type Architecture: str\n        :param DockerVersion: 创建此镜像的docker版本\n        :type DockerVersion: str\n        :param OS: 此镜像建议运行系统\n        :type OS: str\n        :param SizeByte: SizeByte\n        :type SizeByte: int\n        :param Id: Id\n        :type Id: int\n        :param UpdateTime: 数据更新时间\n        :type UpdateTime: str\n        :param PushTime: 镜像更新时间\n        :type PushTime: str\n        """
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
        """
        :param TagCount: Tag的总数\n        :type TagCount: int\n        :param TagInfo: TagInfo列表\n        :type TagInfo: list of TagInfo\n        :param Server: Server\n        :type Server: str\n        :param RepoName: 仓库名称\n        :type RepoName: str\n        """
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
        """
        :param ResourceType: 默认值为instance
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceType: str\n        :param Tags: 云标签数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        """
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
        """
        :param TaskName: 任务\n        :type TaskName: str\n        :param TaskUUID: 任务UUID\n        :type TaskUUID: str\n        :param TaskStatus: 任务状态\n        :type TaskStatus: str\n        :param TaskMessage: 任务的状态信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskMessage: str\n        :param CreatedTime: 任务开始时间\n        :type CreatedTime: str\n        :param FinishedTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type FinishedTime: str\n        """
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
        """
        :param Digest: 哈希值\n        :type Digest: str\n        :param Size: 镜像大小\n        :type Size: int\n        :param ImageVersion: Tag名称\n        :type ImageVersion: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        """
        self.Digest = None
        self.Size = None
        self.ImageVersion = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")
        self.Size = params.get("Size")
        self.ImageVersion = params.get("ImageVersion")
        self.UpdateTime = params.get("UpdateTime")
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
        """
        :param Id: 令牌ID\n        :type Id: str\n        :param Desc: 令牌描述\n        :type Desc: str\n        :param RegistryId: 令牌所属实例ID\n        :type RegistryId: str\n        :param Enabled: 令牌启用状态\n        :type Enabled: bool\n        :param CreatedAt: 令牌创建时间\n        :type CreatedAt: str\n        :param ExpiredAt: 令牌过期时间戳\n        :type ExpiredAt: int\n        """
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
        """
        :param Name: 命名空间名称\n        :type Name: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param Public: 访问级别\n        :type Public: bool\n        :param NamespaceId: 命名空间的Id\n        :type NamespaceId: int\n        """
        self.Name = None
        self.CreationTime = None
        self.Public = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.NamespaceId = params.get("NamespaceId")
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
        """
        :param Name: 仓库名称\n        :type Name: str\n        :param Namespace: 命名空间名称\n        :type Namespace: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param Public: 是否公开\n        :type Public: bool\n        :param Description: 仓库详细描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param BriefDescription: 简单描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type BriefDescription: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        """
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
        """
        :param InvokeMethod: 触发方式\n        :type InvokeMethod: str\n        :param InvokeExpr: 触发表达式
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeExpr: str\n        """
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
        """
        :param AppId: AppId
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: str\n        :param ClusterId: TKE集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param Namespace: TKE集群命名空间
注意：此字段可能返回 null，表示取不到有效值。\n        :type Namespace: str\n        :param ServiceName: TKE集群工作负载名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        :param ContainerName: TKE集群工作负载中容器名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerName: str\n        :param ClusterRegion: TKE集群地域数字ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterRegion: int\n        """
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
        """
        :param ReturnCode: 请求TKE返回值
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReturnCode: int\n        :param ReturnMsg: 请求TKE返回信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReturnMsg: str\n        """
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
        """
        :param RepoName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepoName: str\n        :param TagName: Tag名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagName: str\n        :param TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TriggerName: str\n        :param InvokeSource: 触发方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeSource: str\n        :param InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeAction: str\n        :param InvokeTime: 触发时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeTime: str\n        :param InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`\n        :param InvokePara: 触发参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`\n        :param InvokeResult: 触发结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeResult: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeResult`\n        """
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
        """
        :param TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TriggerName: str\n        :param InvokeSource: 触发来源
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeSource: str\n        :param InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeAction: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`\n        :param InvokePara: 触发器参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`\n        """
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
        """
        :param Namespace: 命名空间名称\n        :type Namespace: str\n        """
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
        """
        :param Data: 命名空间是否存在\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceIsExistsResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RepoName: 仓库名称\n        :type RepoName: str\n        """
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
        """
        :param Data: 仓库是否存在\n        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoIsExistResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param InstanceId: tcr实例id\n        :type InstanceId: str\n        :param VpcId: 私有网络id\n        :type VpcId: str\n        :param EniLBIp: tcr内网访问链路ip\n        :type EniLBIp: str\n        :param UsePublicDomain: true：use instance name as subdomain
false: use instancename+"-vpc" as subdomain\n        :type UsePublicDomain: bool\n        """
        self.InstanceId = None
        self.VpcId = None
        self.EniLBIp = None
        self.UsePublicDomain = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.EniLBIp = params.get("EniLBIp")
        self.UsePublicDomain = params.get("UsePublicDomain")
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
        """
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param VpcId: unique vpc id
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param Status: ENABLE代表已经开启，DISABLE代表未开启，ERROR代表查询出错
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
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
        """
        :param Address: 目标地址\n        :type Address: str\n        :param Headers: 自定义 Headers\n        :type Headers: list of Header\n        """
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
        """
        :param Name: 触发器名称\n        :type Name: str\n        :param Targets: 触发器目标\n        :type Targets: list of WebhookTarget\n        :param EventTypes: 触发动作\n        :type EventTypes: list of str\n        :param Condition: 触发规则\n        :type Condition: str\n        :param Enabled: 启用触发器\n        :type Enabled: bool\n        :param Id: 触发器Id\n        :type Id: int\n        :param Description: 触发器描述\n        :type Description: str\n        :param NamespaceId: 触发器所属命名空间 Id\n        :type NamespaceId: int\n        """
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
        """
        :param Id: 日志 Id\n        :type Id: int\n        :param TriggerId: 触发器 Id\n        :type TriggerId: int\n        :param EventType: 事件类型\n        :type EventType: str\n        :param NotifyType: 通知类型\n        :type NotifyType: str\n        :param Detail: 详情\n        :type Detail: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param Status: 状态\n        :type Status: str\n        """
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
        