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


class AggregationObj(AbstractModel):
    """聚合类型

    """

    def __init__(self):
        r"""
        :param Type: 类型
        :type Type: str
        :param Bucket: 数组
        :type Bucket: list of Bucket
        """
        self.Type = None
        self.Bucket = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("Bucket") is not None:
            self.Bucket = []
            for item in params.get("Bucket"):
                obj = Bucket()
                obj._deserialize(item)
                self.Bucket.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertDetail(AbstractModel):
    """告警详情

    """

    def __init__(self):
        r"""
        :param BaseInfo: 告警基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseInfo: :class:`tencentcloud.ssa.v20180608.models.AlertType`
        :param Detail: 告警详情，json序列化
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: str
        """
        self.BaseInfo = None
        self.Detail = None


    def _deserialize(self, params):
        if params.get("BaseInfo") is not None:
            self.BaseInfo = AlertType()
            self.BaseInfo._deserialize(params.get("BaseInfo"))
        self.Detail = params.get("Detail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertListAggregations(AbstractModel):
    """空Aggregations结构体

    """

    def __init__(self):
        r"""
        :param Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertListData(AbstractModel):
    """告警列表响应数据

    """

    def __init__(self):
        r"""
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param AlertList: 返回列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertList: list of AlertType
        :param Aggregations: 聚合参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Aggregations: :class:`tencentcloud.ssa.v20180608.models.AlertListAggregations`
        """
        self.Total = None
        self.AlertList = None
        self.Aggregations = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AlertList") is not None:
            self.AlertList = []
            for item in params.get("AlertList"):
                obj = AlertType()
                obj._deserialize(item)
                self.AlertList.append(obj)
        if params.get("Aggregations") is not None:
            self.Aggregations = AlertListAggregations()
            self.Aggregations._deserialize(params.get("Aggregations"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertType(AbstractModel):
    """告警字段

    """

    def __init__(self):
        r"""
        :param AlertTime: 标准时间格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertTime: str
        :param AlertId: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertId: str
        :param AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param AssetPrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetPrivateIp: list of str
        :param AlertName: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertName: str
        :param Level: 告警级别  0:未知 1:低危 2:中危 3:高危 4:严重
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Source: 来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param AttackChain: 攻击字段1
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackChain: str
        :param AttackId: 攻击字段2
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackId: str
        :param Concerns: 关注点
注意：此字段可能返回 null，表示取不到有效值。
        :type Concerns: list of ConcernInfo
        :param Action: 1：已防御，0,2：仅检测(0:告警类 1:拦截类 2:放行类 )
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: int
        :param AttackResult: 0/空：未知，1：未成功，2：成功
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackResult: int
        :param EventStatus: //调查状态  0/空：未启用，1：调查中，2：完成调查
注意：此字段可能返回 null，表示取不到有效值。
        :type EventStatus: int
        :param EventId: //关联事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param Status: //处置状态  0：未关闭，1：已关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param ConcernMaliciousCount: 恶意实体
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcernMaliciousCount: int
        :param ConcernVictimCount: 受害者实体
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcernVictimCount: int
        :param VictimAssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetType: str
        :param SubType: 告警子类
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param AttackName: 攻击技术名字
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackName: str
        :param AssetPublicIp: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetPublicIp: list of str
        :param AttackTactic: 攻击战术名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackTactic: str
        :param VictimAssetSub: 资产子网
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetSub: str
        :param VictimAssetVpc: 资产vpc
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetVpc: str
        :param Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param AssetGroupName: 资产组名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetGroupName: list of str
        :param AssetProjectName: 资产项目名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetProjectName: str
        :param VictimAssetContent: 失陷资产内容
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetContent: list of str
        :param WrongReportStatus: 错误报告状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WrongReportStatus: int
        :param WrongReportConditionId: 错误报告Id
注意：此字段可能返回 null，表示取不到有效值。
        :type WrongReportConditionId: int
        """
        self.AlertTime = None
        self.AlertId = None
        self.AssetId = None
        self.AssetPrivateIp = None
        self.AlertName = None
        self.Level = None
        self.Type = None
        self.Source = None
        self.AttackChain = None
        self.AttackId = None
        self.Concerns = None
        self.Action = None
        self.AttackResult = None
        self.EventStatus = None
        self.EventId = None
        self.Status = None
        self.AssetName = None
        self.ConcernMaliciousCount = None
        self.ConcernVictimCount = None
        self.VictimAssetType = None
        self.SubType = None
        self.AttackName = None
        self.AssetPublicIp = None
        self.AttackTactic = None
        self.VictimAssetSub = None
        self.VictimAssetVpc = None
        self.Timestamp = None
        self.AssetGroupName = None
        self.AssetProjectName = None
        self.VictimAssetContent = None
        self.WrongReportStatus = None
        self.WrongReportConditionId = None


    def _deserialize(self, params):
        self.AlertTime = params.get("AlertTime")
        self.AlertId = params.get("AlertId")
        self.AssetId = params.get("AssetId")
        self.AssetPrivateIp = params.get("AssetPrivateIp")
        self.AlertName = params.get("AlertName")
        self.Level = params.get("Level")
        self.Type = params.get("Type")
        self.Source = params.get("Source")
        self.AttackChain = params.get("AttackChain")
        self.AttackId = params.get("AttackId")
        if params.get("Concerns") is not None:
            self.Concerns = []
            for item in params.get("Concerns"):
                obj = ConcernInfo()
                obj._deserialize(item)
                self.Concerns.append(obj)
        self.Action = params.get("Action")
        self.AttackResult = params.get("AttackResult")
        self.EventStatus = params.get("EventStatus")
        self.EventId = params.get("EventId")
        self.Status = params.get("Status")
        self.AssetName = params.get("AssetName")
        self.ConcernMaliciousCount = params.get("ConcernMaliciousCount")
        self.ConcernVictimCount = params.get("ConcernVictimCount")
        self.VictimAssetType = params.get("VictimAssetType")
        self.SubType = params.get("SubType")
        self.AttackName = params.get("AttackName")
        self.AssetPublicIp = params.get("AssetPublicIp")
        self.AttackTactic = params.get("AttackTactic")
        self.VictimAssetSub = params.get("VictimAssetSub")
        self.VictimAssetVpc = params.get("VictimAssetVpc")
        self.Timestamp = params.get("Timestamp")
        self.AssetGroupName = params.get("AssetGroupName")
        self.AssetProjectName = params.get("AssetProjectName")
        self.VictimAssetContent = params.get("VictimAssetContent")
        self.WrongReportStatus = params.get("WrongReportStatus")
        self.WrongReportConditionId = params.get("WrongReportConditionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Asset(AbstractModel):
    """资产类型

    """

    def __init__(self):
        r"""
        :param AssetType: 资产类型
        :type AssetType: str
        :param Name: 名字
        :type Name: str
        :param AssetRegionName: 区域
        :type AssetRegionName: str
        :param AssetVpcid: 所属网络
        :type AssetVpcid: str
        :param InstanceType: 主机类型
        :type InstanceType: str
        :param InstanceState: 主机状态
        :type InstanceState: str
        :param EngineVersion: 引擎版本
        :type EngineVersion: str
        :param Id: 数据库标识
        :type Id: str
        :param Tag: 标签
        :type Tag: list of Tag
        :param AssetCspmRiskNum: 配置风险统计数
        :type AssetCspmRiskNum: int
        :param PublicIpAddresses: 主机IP
        :type PublicIpAddresses: list of str
        :param AssetUniqid: 资产唯一标识
        :type AssetUniqid: str
        :param ChargeType: 付费类型
        :type ChargeType: str
        :param AssetEventNum: 安全事件统计数
        :type AssetEventNum: int
        :param AssetVulNum: 漏洞统计数
        :type AssetVulNum: int
        :param PrivateIpAddresses: 主机IP内网
        :type PrivateIpAddresses: list of str
        :param GroupName: 所属分组
        :type GroupName: str
        :param SsaAssetDiscoverTime: 发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDiscoverTime: str
        :param SsaAssetDeleteTime: 下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDeleteTime: str
        :param IsNew: 是否是新增资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNew: bool
        :param AssetSubnetId: 所属子网
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetId: str
        :param AssetSubnetName: 子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetName: str
        :param AssetVpcName: vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVpcName: str
        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: int
        :param NameSpace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param LoadBalancerType: 负载均衡实例的网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param LoadBalancerVips: 负载均衡实例的vip列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param AssetIpv6: ipv6信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIpv6: list of str
        :param SSHRisk: ssh端口暴露风险
注意：此字段可能返回 null，表示取不到有效值。
        :type SSHRisk: str
        :param RDPRisk: rdp端口暴露风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RDPRisk: str
        :param EventRisk: 资产失陷事件风险
注意：此字段可能返回 null，表示取不到有效值。
        :type EventRisk: str
        """
        self.AssetType = None
        self.Name = None
        self.AssetRegionName = None
        self.AssetVpcid = None
        self.InstanceType = None
        self.InstanceState = None
        self.EngineVersion = None
        self.Id = None
        self.Tag = None
        self.AssetCspmRiskNum = None
        self.PublicIpAddresses = None
        self.AssetUniqid = None
        self.ChargeType = None
        self.AssetEventNum = None
        self.AssetVulNum = None
        self.PrivateIpAddresses = None
        self.GroupName = None
        self.SsaAssetDiscoverTime = None
        self.SsaAssetDeleteTime = None
        self.IsNew = None
        self.AssetSubnetId = None
        self.AssetSubnetName = None
        self.AssetVpcName = None
        self.ClusterType = None
        self.NameSpace = None
        self.LoadBalancerType = None
        self.LoadBalancerVips = None
        self.AssetIpv6 = None
        self.SSHRisk = None
        self.RDPRisk = None
        self.EventRisk = None


    def _deserialize(self, params):
        self.AssetType = params.get("AssetType")
        self.Name = params.get("Name")
        self.AssetRegionName = params.get("AssetRegionName")
        self.AssetVpcid = params.get("AssetVpcid")
        self.InstanceType = params.get("InstanceType")
        self.InstanceState = params.get("InstanceState")
        self.EngineVersion = params.get("EngineVersion")
        self.Id = params.get("Id")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.AssetCspmRiskNum = params.get("AssetCspmRiskNum")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.AssetUniqid = params.get("AssetUniqid")
        self.ChargeType = params.get("ChargeType")
        self.AssetEventNum = params.get("AssetEventNum")
        self.AssetVulNum = params.get("AssetVulNum")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.GroupName = params.get("GroupName")
        self.SsaAssetDiscoverTime = params.get("SsaAssetDiscoverTime")
        self.SsaAssetDeleteTime = params.get("SsaAssetDeleteTime")
        self.IsNew = params.get("IsNew")
        self.AssetSubnetId = params.get("AssetSubnetId")
        self.AssetSubnetName = params.get("AssetSubnetName")
        self.AssetVpcName = params.get("AssetVpcName")
        self.ClusterType = params.get("ClusterType")
        self.NameSpace = params.get("NameSpace")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.AssetIpv6 = params.get("AssetIpv6")
        self.SSHRisk = params.get("SSHRisk")
        self.RDPRisk = params.get("RDPRisk")
        self.EventRisk = params.get("EventRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetDetail(AbstractModel):
    """资产详情信息

    """

    def __init__(self):
        r"""
        :param AssetType: 资产类型
        :type AssetType: str
        :param Name: 名字
        :type Name: str
        :param Region: 区域
        :type Region: str
        :param VpcId: 所属网络
        :type VpcId: str
        :param InstanceType: 主机类型
        :type InstanceType: str
        :param InstanceState: 主机状态
        :type InstanceState: str
        :param PublicIpAddresses: 主机IP-公网
        :type PublicIpAddresses: list of str
        :param EngineVersion: 引擎版本
        :type EngineVersion: str
        :param Id: 标识
        :type Id: str
        :param Tag: 标签
        :type Tag: list of Tag
        :param Vip: 内网IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param LoadBalancerVips: 负载均衡示例的vip列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param Uin: 账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: int
        :param CreationDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationDate: str
        :param Domain: 访问域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param AssetUniqid: 资产唯一id
        :type AssetUniqid: str
        :param InstanceId: 关联实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param DiskType: 配置硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param DiskSize: 配置硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param AssetStatus: 云硬盘/证书状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetStatus: str
        :param CertType: 证书类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CertType: str
        :param ProjectName: 所属项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param CertEndTime: 到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ProductType: nosql引擎/版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductType: int
        :param PrivateIpAddresses: 主机IP-内网
        :type PrivateIpAddresses: list of str
        :param ValidityPeriod: 证书有效期
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param Port: 端口服务数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: list of str
        :param RiskConfig: 配置风险数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskConfig: list of str
        :param Event: 相关待处理事件
注意：此字段可能返回 null，表示取不到有效值。
        :type Event: str
        :param Vul: 相关待处理漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type Vul: str
        :param SsaAssetDiscoverTime: 资产发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDiscoverTime: str
        :param AssetSubnetId: 所属子网
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetId: str
        :param AssetSubnetName: 子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetName: str
        :param AssetVpcName: vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVpcName: str
        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: int
        :param NameSpace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param AssetCreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param LoadBalancerType: 负载均衡网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param AssetIpv6: ipv6信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIpv6: list of str
        :param SSHRisk: ssh风险
注意：此字段可能返回 null，表示取不到有效值。
        :type SSHRisk: str
        :param RDPRisk: rdp风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RDPRisk: str
        :param EventRisk: 安全事件风险
注意：此字段可能返回 null，表示取不到有效值。
        :type EventRisk: str
        :param AssetVulNum: 漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVulNum: int
        :param AssetEventNum: 资产事件
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetEventNum: int
        :param AssetCspmRiskNum: cspm风险
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCspmRiskNum: int
        :param SsaAssetDeleteTime: 资产删除时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDeleteTime: str
        :param ChargeType: 费用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param AssetRegionName: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetRegionName: str
        :param AssetVpcid: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVpcid: str
        """
        self.AssetType = None
        self.Name = None
        self.Region = None
        self.VpcId = None
        self.InstanceType = None
        self.InstanceState = None
        self.PublicIpAddresses = None
        self.EngineVersion = None
        self.Id = None
        self.Tag = None
        self.Vip = None
        self.Status = None
        self.LoadBalancerVips = None
        self.Uin = None
        self.CreationDate = None
        self.Domain = None
        self.AssetUniqid = None
        self.InstanceId = None
        self.DiskType = None
        self.DiskSize = None
        self.AssetStatus = None
        self.CertType = None
        self.ProjectName = None
        self.CertEndTime = None
        self.ProductType = None
        self.PrivateIpAddresses = None
        self.ValidityPeriod = None
        self.GroupName = None
        self.Port = None
        self.RiskConfig = None
        self.Event = None
        self.Vul = None
        self.SsaAssetDiscoverTime = None
        self.AssetSubnetId = None
        self.AssetSubnetName = None
        self.AssetVpcName = None
        self.ClusterType = None
        self.NameSpace = None
        self.AssetCreateTime = None
        self.LoadBalancerType = None
        self.AssetIpv6 = None
        self.SSHRisk = None
        self.RDPRisk = None
        self.EventRisk = None
        self.AssetVulNum = None
        self.AssetEventNum = None
        self.AssetCspmRiskNum = None
        self.SsaAssetDeleteTime = None
        self.ChargeType = None
        self.AssetRegionName = None
        self.AssetVpcid = None


    def _deserialize(self, params):
        self.AssetType = params.get("AssetType")
        self.Name = params.get("Name")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.InstanceType = params.get("InstanceType")
        self.InstanceState = params.get("InstanceState")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.EngineVersion = params.get("EngineVersion")
        self.Id = params.get("Id")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Vip = params.get("Vip")
        self.Status = params.get("Status")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Uin = params.get("Uin")
        self.CreationDate = params.get("CreationDate")
        self.Domain = params.get("Domain")
        self.AssetUniqid = params.get("AssetUniqid")
        self.InstanceId = params.get("InstanceId")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.AssetStatus = params.get("AssetStatus")
        self.CertType = params.get("CertType")
        self.ProjectName = params.get("ProjectName")
        self.CertEndTime = params.get("CertEndTime")
        self.ProductType = params.get("ProductType")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.GroupName = params.get("GroupName")
        self.Port = params.get("Port")
        self.RiskConfig = params.get("RiskConfig")
        self.Event = params.get("Event")
        self.Vul = params.get("Vul")
        self.SsaAssetDiscoverTime = params.get("SsaAssetDiscoverTime")
        self.AssetSubnetId = params.get("AssetSubnetId")
        self.AssetSubnetName = params.get("AssetSubnetName")
        self.AssetVpcName = params.get("AssetVpcName")
        self.ClusterType = params.get("ClusterType")
        self.NameSpace = params.get("NameSpace")
        self.AssetCreateTime = params.get("AssetCreateTime")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.AssetIpv6 = params.get("AssetIpv6")
        self.SSHRisk = params.get("SSHRisk")
        self.RDPRisk = params.get("RDPRisk")
        self.EventRisk = params.get("EventRisk")
        self.AssetVulNum = params.get("AssetVulNum")
        self.AssetEventNum = params.get("AssetEventNum")
        self.AssetCspmRiskNum = params.get("AssetCspmRiskNum")
        self.SsaAssetDeleteTime = params.get("SsaAssetDeleteTime")
        self.ChargeType = params.get("ChargeType")
        self.AssetRegionName = params.get("AssetRegionName")
        self.AssetVpcid = params.get("AssetVpcid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetList(AbstractModel):
    """资产列表

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param List: 资产数组
        :type List: list of Asset
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Asset()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetQueryFilter(AbstractModel):
    """资产查询过滤参数

    """

    def __init__(self):
        r"""
        :param Filter: 查询参数
        :type Filter: list of QueryFilter
        :param Logic: 查询连接符，1 and  ，2 or
        :type Logic: int
        """
        self.Filter = None
        self.Logic = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filter.append(obj)
        self.Logic = params.get("Logic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetTypeStatistic(AbstractModel):
    """资产测绘结果统计

    """

    def __init__(self):
        r"""
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param AssetCount: 统计计数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCount: int
        """
        self.AssetType = None
        self.AssetCount = None


    def _deserialize(self, params):
        self.AssetType = params.get("AssetType")
        self.AssetCount = params.get("AssetCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bucket(AbstractModel):
    """es聚合数据类型

    """

    def __init__(self):
        r"""
        :param Key: key
        :type Key: str
        :param Count: 数量
        :type Count: int
        """
        self.Key = None
        self.Count = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAssetItem(AbstractModel):
    """检查项资产组每一项

    """

    def __init__(self):
        r"""
        :param Id: 检查项下资产组ID
        :type Id: int
        :param Instid: 资产组实例id
        :type Instid: str
        :param Url: 处置跳转URL
        :type Url: str
        :param Taskid: 检查任务id
        :type Taskid: str
        :param Result: 检查结果
        :type Result: int
        :param Updatetime: 更新时间
        :type Updatetime: str
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param IsIgnore: 是否忽略
        :type IsIgnore: int
        :param IsChecked: 检查状态
        :type IsChecked: int
        :param AssetInfo: 资产组信息
        :type AssetInfo: str
        :param AssetId: 资产组ES的_id
        :type AssetId: str
        :param Detail: 详情
        :type Detail: str
        :param Remarks: 备注内容
        :type Remarks: str
        """
        self.Id = None
        self.Instid = None
        self.Url = None
        self.Taskid = None
        self.Result = None
        self.Updatetime = None
        self.Tag = None
        self.IsIgnore = None
        self.IsChecked = None
        self.AssetInfo = None
        self.AssetId = None
        self.Detail = None
        self.Remarks = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Instid = params.get("Instid")
        self.Url = params.get("Url")
        self.Taskid = params.get("Taskid")
        self.Result = params.get("Result")
        self.Updatetime = params.get("Updatetime")
        self.Tag = params.get("Tag")
        self.IsIgnore = params.get("IsIgnore")
        self.IsChecked = params.get("IsChecked")
        self.AssetInfo = params.get("AssetInfo")
        self.AssetId = params.get("AssetId")
        self.Detail = params.get("Detail")
        self.Remarks = params.get("Remarks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckConfigDetail(AbstractModel):
    """云安全配置检查项详情

    """

    def __init__(self):
        r"""
        :param Id: 检查项Id
        :type Id: str
        :param CheckName: 检查项名称
        :type CheckName: str
        :param Content: 检查项内容
        :type Content: str
        :param Method: 检查项处置方案
        :type Method: str
        :param Doc: 检查项帮助文档
        :type Doc: str
        :param ErrorCount: 未通过总数
        :type ErrorCount: int
        :param IsPass: 是否通过检查
        :type IsPass: int
        :param SafeCount: 通过检查项
        :type SafeCount: int
        :param IgnoreCount: 忽略检查项
        :type IgnoreCount: int
        :param RiskCount: 风险检查项
        :type RiskCount: int
        :param NameEn: 检查项英文
        :type NameEn: str
        :param AssetType: 检查项类型
        :type AssetType: str
        :param ResCount: res_count
        :type ResCount: int
        :param IsIgnore: 是否忽略
        :type IsIgnore: int
        """
        self.Id = None
        self.CheckName = None
        self.Content = None
        self.Method = None
        self.Doc = None
        self.ErrorCount = None
        self.IsPass = None
        self.SafeCount = None
        self.IgnoreCount = None
        self.RiskCount = None
        self.NameEn = None
        self.AssetType = None
        self.ResCount = None
        self.IsIgnore = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CheckName = params.get("CheckName")
        self.Content = params.get("Content")
        self.Method = params.get("Method")
        self.Doc = params.get("Doc")
        self.ErrorCount = params.get("ErrorCount")
        self.IsPass = params.get("IsPass")
        self.SafeCount = params.get("SafeCount")
        self.IgnoreCount = params.get("IgnoreCount")
        self.RiskCount = params.get("RiskCount")
        self.NameEn = params.get("NameEn")
        self.AssetType = params.get("AssetType")
        self.ResCount = params.get("ResCount")
        self.IsIgnore = params.get("IsIgnore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceCheckDetail(AbstractModel):
    """等保资产组记录

    """

    def __init__(self):
        r"""
        :param Id: 检查项ID
        :type Id: str
        :param Category: 检查项类别
        :type Category: str
        :param Type: 检查项类型
        :type Type: str
        :param ErrorCount: 不通过总数
        :type ErrorCount: int
        :param NameEn: 检查项英文名
        :type NameEn: str
        :param CheckName: 检查项名称
        :type CheckName: str
        :param Method: 检查项处置方式
        :type Method: str
        :param Doc: 帮助文档
        :type Doc: str
        :param SafeCount: 通过总数
        :type SafeCount: int
        :param Content: 检查项检查内容
        :type Content: str
        :param IsPass: 是否通过检测
        :type IsPass: int
        :param IgnoreCount: 忽略总数
        :type IgnoreCount: int
        :param RiskCount: 风险总数
        :type RiskCount: int
        :param LastCheckTime: 最近一次检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param AssetType: 资产组类型
        :type AssetType: str
        :param ResCount: res_count
        :type ResCount: int
        :param UUID: 检查项UUID
        :type UUID: str
        :param StandardItem: 标准项
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardItem: str
        :param Chapter: 章节
注意：此字段可能返回 null，表示取不到有效值。
        :type Chapter: str
        :param AssetTypeDesc: 资产类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeDesc: str
        :param IsIgnore: 是否忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnore: int
        :param RiskItem: 风险项
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskItem: str
        :param Title: 合规检查项完整名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        """
        self.Id = None
        self.Category = None
        self.Type = None
        self.ErrorCount = None
        self.NameEn = None
        self.CheckName = None
        self.Method = None
        self.Doc = None
        self.SafeCount = None
        self.Content = None
        self.IsPass = None
        self.IgnoreCount = None
        self.RiskCount = None
        self.LastCheckTime = None
        self.AssetType = None
        self.ResCount = None
        self.UUID = None
        self.StandardItem = None
        self.Chapter = None
        self.AssetTypeDesc = None
        self.IsIgnore = None
        self.RiskItem = None
        self.Title = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Category = params.get("Category")
        self.Type = params.get("Type")
        self.ErrorCount = params.get("ErrorCount")
        self.NameEn = params.get("NameEn")
        self.CheckName = params.get("CheckName")
        self.Method = params.get("Method")
        self.Doc = params.get("Doc")
        self.SafeCount = params.get("SafeCount")
        self.Content = params.get("Content")
        self.IsPass = params.get("IsPass")
        self.IgnoreCount = params.get("IgnoreCount")
        self.RiskCount = params.get("RiskCount")
        self.LastCheckTime = params.get("LastCheckTime")
        self.AssetType = params.get("AssetType")
        self.ResCount = params.get("ResCount")
        self.UUID = params.get("UUID")
        self.StandardItem = params.get("StandardItem")
        self.Chapter = params.get("Chapter")
        self.AssetTypeDesc = params.get("AssetTypeDesc")
        self.IsIgnore = params.get("IsIgnore")
        self.RiskItem = params.get("RiskItem")
        self.Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConcernInfo(AbstractModel):
    """关注点类型

    """

    def __init__(self):
        r"""
        :param ConcernType: 关注点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcernType: int
        :param EntityType: 实体类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EntityType: int
        :param Concern: 关注点
注意：此字段可能返回 null，表示取不到有效值。
        :type Concern: str
        :param StatisticsCount: 最近数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticsCount: int
        :param IpCountry: IP国家
注意：此字段可能返回 null，表示取不到有效值。
        :type IpCountry: str
        :param IpProvince: IP省份
注意：此字段可能返回 null，表示取不到有效值。
        :type IpProvince: str
        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param Confidence: 置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: int
        :param IpIsp: 服务商
注意：此字段可能返回 null，表示取不到有效值。
        :type IpIsp: str
        :param IpInfrastructure: 是否基础设施
注意：此字段可能返回 null，表示取不到有效值。
        :type IpInfrastructure: str
        :param ThreatType: 威胁类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ThreatType: list of str
        :param Groups: 威胁团伙
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of str
        :param Status: 状态威胁情报接口
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Tags: 恶意标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param VictimAssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetType: str
        :param VictimAssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetName: str
        :param DomainRegistrant: 注册者
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainRegistrant: str
        :param DomainRegisteredInstitution: 注册机构
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainRegisteredInstitution: str
        :param DomainRegistrationTime: 注册时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainRegistrationTime: str
        :param FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileMd5: MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMd5: str
        :param VirusName: 病毒名
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param FilePath: 文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param FileSize: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: str
        :param ProcName: 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcName: str
        :param Pid: 进程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Pid: str
        :param ProcPath: 进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcPath: str
        :param ProcUser: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcUser: str
        :param DefendedCount: 已防御
注意：此字段可能返回 null，表示取不到有效值。
        :type DefendedCount: int
        :param DetectedCount: 仅检测
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectedCount: int
        :param SearchData: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchData: str
        :param IpCountryIso: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IpCountryIso: str
        :param IpProvinceIso: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IpProvinceIso: str
        :param IpCity: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IpCity: str
        :param EventSubType: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSubType: str
        """
        self.ConcernType = None
        self.EntityType = None
        self.Concern = None
        self.StatisticsCount = None
        self.IpCountry = None
        self.IpProvince = None
        self.Result = None
        self.Confidence = None
        self.IpIsp = None
        self.IpInfrastructure = None
        self.ThreatType = None
        self.Groups = None
        self.Status = None
        self.Tags = None
        self.VictimAssetType = None
        self.VictimAssetName = None
        self.DomainRegistrant = None
        self.DomainRegisteredInstitution = None
        self.DomainRegistrationTime = None
        self.FileName = None
        self.FileMd5 = None
        self.VirusName = None
        self.FilePath = None
        self.FileSize = None
        self.ProcName = None
        self.Pid = None
        self.ProcPath = None
        self.ProcUser = None
        self.DefendedCount = None
        self.DetectedCount = None
        self.SearchData = None
        self.IpCountryIso = None
        self.IpProvinceIso = None
        self.IpCity = None
        self.EventSubType = None


    def _deserialize(self, params):
        self.ConcernType = params.get("ConcernType")
        self.EntityType = params.get("EntityType")
        self.Concern = params.get("Concern")
        self.StatisticsCount = params.get("StatisticsCount")
        self.IpCountry = params.get("IpCountry")
        self.IpProvince = params.get("IpProvince")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.IpIsp = params.get("IpIsp")
        self.IpInfrastructure = params.get("IpInfrastructure")
        self.ThreatType = params.get("ThreatType")
        self.Groups = params.get("Groups")
        self.Status = params.get("Status")
        self.Tags = params.get("Tags")
        self.VictimAssetType = params.get("VictimAssetType")
        self.VictimAssetName = params.get("VictimAssetName")
        self.DomainRegistrant = params.get("DomainRegistrant")
        self.DomainRegisteredInstitution = params.get("DomainRegisteredInstitution")
        self.DomainRegistrationTime = params.get("DomainRegistrationTime")
        self.FileName = params.get("FileName")
        self.FileMd5 = params.get("FileMd5")
        self.VirusName = params.get("VirusName")
        self.FilePath = params.get("FilePath")
        self.FileSize = params.get("FileSize")
        self.ProcName = params.get("ProcName")
        self.Pid = params.get("Pid")
        self.ProcPath = params.get("ProcPath")
        self.ProcUser = params.get("ProcUser")
        self.DefendedCount = params.get("DefendedCount")
        self.DetectedCount = params.get("DetectedCount")
        self.SearchData = params.get("SearchData")
        self.IpCountryIso = params.get("IpCountryIso")
        self.IpProvinceIso = params.get("IpProvinceIso")
        self.IpCity = params.get("IpCity")
        self.EventSubType = params.get("EventSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataAssetMapping(AbstractModel):
    """资产测绘对象

    """

    def __init__(self):
        r"""
        :param AssetIp: 资产主IP地址(公网IP)
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIp: str
        :param AssetName: 资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param Instid: 资产ID(各模块间通用)
注意：此字段可能返回 null，表示取不到有效值。
        :type Instid: str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param AssetRegionEn: 资产可用区(英文)
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetRegionEn: str
        :param AssetRegionCn: 资产可用区(中文)
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetRegionCn: str
        :param AssetNetwork: 资产所属网络
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetNetwork: str
        :param AssetStatusEn: 资产运行状态(英文)
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetStatusEn: str
        :param AssetStatusCn: 资产运行状态(中文)
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetStatusCn: str
        :param IsWhite: 是否白名单：“True”为白名单不测绘，默认“False”正常测绘
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWhite: str
        :param Status: 资产测绘状态(“unstart”未开始/“running”测绘中/“finish”已完成/“abandoned”任务中止)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Time: 最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param Tag: 资产标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param Group: 资产组
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: list of str
        :param Port: 端口和服务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param Component: 组件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Component: str
        :param AssetInstanceType: 资产实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetInstanceType: str
        :param IsIntranet: 资产是否是内网类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIntranet: int
        """
        self.AssetIp = None
        self.AssetName = None
        self.Instid = None
        self.AssetType = None
        self.AssetRegionEn = None
        self.AssetRegionCn = None
        self.AssetNetwork = None
        self.AssetStatusEn = None
        self.AssetStatusCn = None
        self.IsWhite = None
        self.Status = None
        self.Time = None
        self.Tag = None
        self.Group = None
        self.Port = None
        self.Component = None
        self.AssetInstanceType = None
        self.IsIntranet = None


    def _deserialize(self, params):
        self.AssetIp = params.get("AssetIp")
        self.AssetName = params.get("AssetName")
        self.Instid = params.get("Instid")
        self.AssetType = params.get("AssetType")
        self.AssetRegionEn = params.get("AssetRegionEn")
        self.AssetRegionCn = params.get("AssetRegionCn")
        self.AssetNetwork = params.get("AssetNetwork")
        self.AssetStatusEn = params.get("AssetStatusEn")
        self.AssetStatusCn = params.get("AssetStatusCn")
        self.IsWhite = params.get("IsWhite")
        self.Status = params.get("Status")
        self.Time = params.get("Time")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Group = params.get("Group")
        self.Port = params.get("Port")
        self.Component = params.get("Component")
        self.AssetInstanceType = params.get("AssetInstanceType")
        self.IsIntranet = params.get("IsIntranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataCheck(AbstractModel):
    """检查项详情对象

    """

    def __init__(self):
        r"""
        :param Id: 检查项唯一标识符uuid
        :type Id: str
        :param Name: 检查项名称
        :type Name: str
        :param Type: 检查项类型
        :type Type: str
        :param LastCheckTime: 最近一次检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param Status: 初始未检测状态0, 已通过为1，未通过为2
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param IsIgnored: 0-未忽略,1-已忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnored: int
        :param RiskCount: 有风险的资源总数，未通过数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param IsChecked: 0-检测中,1-结束检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsChecked: int
        :param AssetTotal: 总资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTotal: int
        :param Remarks: 备注内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Remarks: str
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.LastCheckTime = None
        self.Status = None
        self.IsIgnored = None
        self.RiskCount = None
        self.IsChecked = None
        self.AssetTotal = None
        self.Remarks = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.LastCheckTime = params.get("LastCheckTime")
        self.Status = params.get("Status")
        self.IsIgnored = params.get("IsIgnored")
        self.RiskCount = params.get("RiskCount")
        self.IsChecked = params.get("IsChecked")
        self.AssetTotal = params.get("AssetTotal")
        self.Remarks = params.get("Remarks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataCompliance(AbstractModel):
    """合规检查项详情对象

    """

    def __init__(self):
        r"""
        :param Id: 等保唯一标识符
        :type Id: str
        :param CheckItemId: 检查项唯一标识符
        :type CheckItemId: str
        :param Name: 检查项名称
        :type Name: str
        :param AssetType: 检查项资产类型
        :type AssetType: str
        :param Type: 检查项类型
        :type Type: str
        :param Category: 检查项类别
        :type Category: str
        :param StandardItem: 检查项标准项
        :type StandardItem: str
        :param Chapter: 检查项章节号
        :type Chapter: str
        :param LastCheckTime: 最近一次检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param Status: 初始未检测状态0, 已通过为1，未通过为2
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RiskCount: 有风险的资源总数，未通过数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param IsChecked: 0-检测中,1-结束检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsChecked: int
        :param RiskItem: 检查项风险项
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskItem: str
        :param IsIgnored: 0-未忽略,1-已忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnored: int
        :param Title: 等保检查项完整名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param AssetTotal: 资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTotal: int
        :param Remarks: 忽略内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Remarks: str
        """
        self.Id = None
        self.CheckItemId = None
        self.Name = None
        self.AssetType = None
        self.Type = None
        self.Category = None
        self.StandardItem = None
        self.Chapter = None
        self.LastCheckTime = None
        self.Status = None
        self.RiskCount = None
        self.IsChecked = None
        self.RiskItem = None
        self.IsIgnored = None
        self.Title = None
        self.AssetTotal = None
        self.Remarks = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CheckItemId = params.get("CheckItemId")
        self.Name = params.get("Name")
        self.AssetType = params.get("AssetType")
        self.Type = params.get("Type")
        self.Category = params.get("Category")
        self.StandardItem = params.get("StandardItem")
        self.Chapter = params.get("Chapter")
        self.LastCheckTime = params.get("LastCheckTime")
        self.Status = params.get("Status")
        self.RiskCount = params.get("RiskCount")
        self.IsChecked = params.get("IsChecked")
        self.RiskItem = params.get("RiskItem")
        self.IsIgnored = params.get("IsIgnored")
        self.Title = params.get("Title")
        self.AssetTotal = params.get("AssetTotal")
        self.Remarks = params.get("Remarks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataEvent(AbstractModel):
    """事件列表对象

    """

    def __init__(self):
        r"""
        :param OldIdMd5: Md5值
注意：此字段可能返回 null，表示取不到有效值。
        :type OldIdMd5: str
        :param EventName: 事件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EventName: str
        :param EventType1: 事件类型一级分类
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType1: int
        :param EventType2: 事件类型二级分类
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType2: int
        :param Level: 事件等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param Status: 处理状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param SrcIp: 源ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcIp: str
        :param DstIp: 目的ip
注意：此字段可能返回 null，表示取不到有效值。
        :type DstIp: str
        :param Time: 事件发生时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param Dstport: 目的端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Dstport: int
        :param AssetIp: 资产ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIp: str
        :param AssetName: 资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param SsaEventUniqid: 安全事件唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaEventUniqid: str
        :param AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param Source: 事件来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param Id: 索引中的唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param IsAssetDeleted: 受影响资产是否已下线
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssetDeleted: str
        :param SsaSrcCountry: 源ip所属地
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaSrcCountry: str
        :param SsaDstCountry: 目的ip所属地
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaDstCountry: str
        :param SsaDescription: 木马类型的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaDescription: str
        :param SsaAttackChain: 供给链类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAttackChain: str
        :param RuleComponents: 受影响组件
        :type RuleComponents: str
        :param AssetIpAll: 资产ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIpAll: list of str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param PublicIpAddresses: cvm类型资产的公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: cvm类型资产的内网ip
        :type PrivateIpAddresses: list of str
        :param SoarResponseStatus: 事件响应状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SoarResponseStatus: int
        :param SoarResponseTime: 事件最近响应时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SoarResponseTime: int
        :param SoarSuggestStatus: 事件建议处理状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SoarSuggestStatus: int
        :param SoarPlaybookType: 事件剧本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SoarPlaybookType: str
        :param SoarRunId: 剧本任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SoarRunId: str
        :param SsaEventId: 事件Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaEventId: str
        :param IsNewCfwEvent: 是否新接入的云防事件
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewCfwEvent: bool
        :param Direction: 出入站方向
注意：此字段可能返回 null，表示取不到有效值。
        :type Direction: str
        """
        self.OldIdMd5 = None
        self.EventName = None
        self.EventType1 = None
        self.EventType2 = None
        self.Level = None
        self.Status = None
        self.SrcIp = None
        self.DstIp = None
        self.Time = None
        self.Dstport = None
        self.AssetIp = None
        self.AssetName = None
        self.SsaEventUniqid = None
        self.AssetId = None
        self.Source = None
        self.Index = None
        self.Id = None
        self.IsAssetDeleted = None
        self.SsaSrcCountry = None
        self.SsaDstCountry = None
        self.SsaDescription = None
        self.SsaAttackChain = None
        self.RuleComponents = None
        self.AssetIpAll = None
        self.AssetType = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.SoarResponseStatus = None
        self.SoarResponseTime = None
        self.SoarSuggestStatus = None
        self.SoarPlaybookType = None
        self.SoarRunId = None
        self.SsaEventId = None
        self.IsNewCfwEvent = None
        self.Direction = None


    def _deserialize(self, params):
        self.OldIdMd5 = params.get("OldIdMd5")
        self.EventName = params.get("EventName")
        self.EventType1 = params.get("EventType1")
        self.EventType2 = params.get("EventType2")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.SrcIp = params.get("SrcIp")
        self.DstIp = params.get("DstIp")
        self.Time = params.get("Time")
        self.Dstport = params.get("Dstport")
        self.AssetIp = params.get("AssetIp")
        self.AssetName = params.get("AssetName")
        self.SsaEventUniqid = params.get("SsaEventUniqid")
        self.AssetId = params.get("AssetId")
        self.Source = params.get("Source")
        self.Index = params.get("Index")
        self.Id = params.get("Id")
        self.IsAssetDeleted = params.get("IsAssetDeleted")
        self.SsaSrcCountry = params.get("SsaSrcCountry")
        self.SsaDstCountry = params.get("SsaDstCountry")
        self.SsaDescription = params.get("SsaDescription")
        self.SsaAttackChain = params.get("SsaAttackChain")
        self.RuleComponents = params.get("RuleComponents")
        self.AssetIpAll = params.get("AssetIpAll")
        self.AssetType = params.get("AssetType")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.SoarResponseStatus = params.get("SoarResponseStatus")
        self.SoarResponseTime = params.get("SoarResponseTime")
        self.SoarSuggestStatus = params.get("SoarSuggestStatus")
        self.SoarPlaybookType = params.get("SoarPlaybookType")
        self.SoarRunId = params.get("SoarRunId")
        self.SsaEventId = params.get("SsaEventId")
        self.IsNewCfwEvent = params.get("IsNewCfwEvent")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDetailListRequest(AbstractModel):
    """DescribeAssetDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 查询条件，可支持的查询字段：AssetUniqid,AssetName,AssetIpAll,AssetVpcid,Tag
        :type Filter: list of AssetQueryFilter
        :param Sorter: 排序条件，可支持的排序字段：
AssetCspmRiskNum,AssetVulNum,AssetEventNum,SsaAssetDiscoverTime
        :type Sorter: list of QuerySort
        :param RiskTags: 风险标签
        :type RiskTags: list of str
        :param Tags: 标签
        :type Tags: list of str
        :param PageIndex: 页
        :type PageIndex: int
        :param PageSize: 页大小
        :type PageSize: int
        """
        self.Filter = None
        self.Sorter = None
        self.RiskTags = None
        self.Tags = None
        self.PageIndex = None
        self.PageSize = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = AssetQueryFilter()
                obj._deserialize(item)
                self.Filter.append(obj)
        if params.get("Sorter") is not None:
            self.Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self.Sorter.append(obj)
        self.RiskTags = params.get("RiskTags")
        self.Tags = params.get("Tags")
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDetailListResponse(AbstractModel):
    """DescribeAssetDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 业务数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AssetDetail
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AssetDetail()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetDetailRequest(AbstractModel):
    """DescribeAssetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Params: 查询过滤参数
        :type Params: str
        """
        self.Params = None


    def _deserialize(self, params):
        self.Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDetailResponse(AbstractModel):
    """DescribeAssetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 资产详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.AssetDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AssetDetail()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeAssetListRequest(AbstractModel):
    """DescribeAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Params: 查询过滤参数
        :type Params: str
        """
        self.Params = None


    def _deserialize(self, params):
        self.Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetListResponse(AbstractModel):
    """DescribeAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param AssetList: 资产列表
        :type AssetList: :class:`tencentcloud.ssa.v20180608.models.AssetList`
        :param AggregationData: 聚合数据
        :type AggregationData: list of AggregationObj
        :param NamespaceData: 命名空间数据
        :type NamespaceData: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AssetList = None
        self.AggregationData = None
        self.NamespaceData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssetList") is not None:
            self.AssetList = AssetList()
            self.AssetList._deserialize(params.get("AssetList"))
        if params.get("AggregationData") is not None:
            self.AggregationData = []
            for item in params.get("AggregationData"):
                obj = AggregationObj()
                obj._deserialize(item)
                self.AggregationData.append(obj)
        self.NamespaceData = params.get("NamespaceData")
        self.RequestId = params.get("RequestId")


class DescribeAssetsMappingListRequest(AbstractModel):
    """DescribeAssetsMappingList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Params: 请求参数
        :type Params: str
        """
        self.Params = None


    def _deserialize(self, params):
        self.Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetsMappingListResponse(AbstractModel):
    """DescribeAssetsMappingList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 资产测绘列表
        :type Data: list of DataAssetMapping
        :param TotalCount: 资产测绘总数
        :type TotalCount: int
        :param CountByType: 类型分类统计数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CountByType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.CountByType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataAssetMapping()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.CountByType = params.get("CountByType")
        self.RequestId = params.get("RequestId")


class DescribeCheckConfigAssetListRequest(AbstractModel):
    """DescribeCheckConfigAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 检查项UUID
        :type Id: str
        :param Offset: 页码
        :type Offset: int
        :param Limit: 每页列表数
        :type Limit: int
        :param Search: db搜索条件
        :type Search: list of Filter
        :param Filter: ES过滤条件
        :type Filter: list of Filter
        """
        self.Id = None
        self.Offset = None
        self.Limit = None
        self.Search = None
        self.Filter = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Search") is not None:
            self.Search = []
            for item in params.get("Search"):
                obj = Filter()
                obj._deserialize(item)
                self.Search.append(obj)
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckConfigAssetListResponse(AbstractModel):
    """DescribeCheckConfigAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 资产列表总数
        :type Total: int
        :param CheckAssetsList: 资产列表项
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAssetsList: list of CheckAssetItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.CheckAssetsList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("CheckAssetsList") is not None:
            self.CheckAssetsList = []
            for item in params.get("CheckAssetsList"):
                obj = CheckAssetItem()
                obj._deserialize(item)
                self.CheckAssetsList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCheckConfigDetailRequest(AbstractModel):
    """DescribeCheckConfigDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 检查项ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckConfigDetailResponse(AbstractModel):
    """DescribeCheckConfigDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckConfigDetail: 检查项详情
        :type CheckConfigDetail: :class:`tencentcloud.ssa.v20180608.models.CheckConfigDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckConfigDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CheckConfigDetail") is not None:
            self.CheckConfigDetail = CheckConfigDetail()
            self.CheckConfigDetail._deserialize(params.get("CheckConfigDetail"))
        self.RequestId = params.get("RequestId")


class DescribeComplianceAssetListRequest(AbstractModel):
    """DescribeComplianceAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页码
        :type Offset: int
        :param Limit: 每页数量
        :type Limit: int
        :param Id: 检查项uuid
        :type Id: str
        :param Filter: 过滤条件
        :type Filter: list of Filter
        :param Search: 查询条件
        :type Search: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Id = None
        self.Filter = None
        self.Search = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Id = params.get("Id")
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)
        if params.get("Search") is not None:
            self.Search = []
            for item in params.get("Search"):
                obj = Filter()
                obj._deserialize(item)
                self.Search.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceAssetListResponse(AbstractModel):
    """DescribeComplianceAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckAssetsList: 资产组列表
        :type CheckAssetsList: list of CheckAssetItem
        :param Total: 资产组列表总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckAssetsList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CheckAssetsList") is not None:
            self.CheckAssetsList = []
            for item in params.get("CheckAssetsList"):
                obj = CheckAssetItem()
                obj._deserialize(item)
                self.CheckAssetsList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeComplianceDetailRequest(AbstractModel):
    """DescribeComplianceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 检查项uuid
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceDetailResponse(AbstractModel):
    """DescribeComplianceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckConfigDetail: 合规管理检查项详情
        :type CheckConfigDetail: :class:`tencentcloud.ssa.v20180608.models.ComplianceCheckDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckConfigDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CheckConfigDetail") is not None:
            self.CheckConfigDetail = ComplianceCheckDetail()
            self.CheckConfigDetail._deserialize(params.get("CheckConfigDetail"))
        self.RequestId = params.get("RequestId")


class DescribeComplianceListRequest(AbstractModel):
    """DescribeComplianceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 搜索过滤条件
        :type Filter: str
        """
        self.Filter = None


    def _deserialize(self, params):
        self.Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceListResponse(AbstractModel):
    """DescribeComplianceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 检查项列表
        :type Data: list of DataCompliance
        :param AssetTotalNum: 总检查资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTotalNum: int
        :param ConfigTotalNum: 总检查项
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigTotalNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.AssetTotalNum = None
        self.ConfigTotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataCompliance()
                obj._deserialize(item)
                self.Data.append(obj)
        self.AssetTotalNum = params.get("AssetTotalNum")
        self.ConfigTotalNum = params.get("ConfigTotalNum")
        self.RequestId = params.get("RequestId")


class DescribeConfigListRequest(AbstractModel):
    """DescribeConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 搜索过滤条件
        :type Filter: str
        """
        self.Filter = None


    def _deserialize(self, params):
        self.Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigListResponse(AbstractModel):
    """DescribeConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 检查项列表
        :type Data: list of DataCheck
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataCheck()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEventDetailRequest(AbstractModel):
    """DescribeEventDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Index: 事件索引名
        :type Index: str
        :param Id: 事件id
        :type Id: str
        :param Source: 事件来源
        :type Source: str
        :param SubEventType: 事件子类型
        :type SubEventType: int
        :param Name: 事件名称
        :type Name: str
        """
        self.Index = None
        self.Id = None
        self.Source = None
        self.SubEventType = None
        self.Name = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Id = params.get("Id")
        self.Source = params.get("Source")
        self.SubEventType = params.get("SubEventType")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventDetailResponse(AbstractModel):
    """DescribeEventDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 事件详情
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeLeakDetectionListRequest(AbstractModel):
    """DescribeLeakDetectionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 筛选条件
        :type Filters: list of Filter
        :param Limit: 每页数量
        :type Limit: int
        :param Page: 页码
        :type Page: int
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Filters = None
        self.Limit = None
        self.Page = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Page = params.get("Page")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLeakDetectionListResponse(AbstractModel):
    """DescribeLeakDetectionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 数据列表
        :type List: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.List = params.get("List")
        self.RequestId = params.get("RequestId")


class DescribeMappingResultsRequest(AbstractModel):
    """DescribeMappingResults请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 过滤条件，FilterKey 取值范围：AssetId，AssetIp，PrivateIp，Protocol，Service，OS，Process，Component，AssetType，Domain，Port，LastMappingTime，MappingType，Disposal，Vpc
        :type Filter: list of AssetQueryFilter
        :param Sorter: 排序条件，SortKey取值范围：CreateTime，LastMappingTime
        :type Sorter: list of QuerySort
        :param PageIndex: 页码
        :type PageIndex: int
        :param PageSize: 页大小，默认大小20
        :type PageSize: int
        """
        self.Filter = None
        self.Sorter = None
        self.PageIndex = None
        self.PageSize = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = AssetQueryFilter()
                obj._deserialize(item)
                self.Filter.append(obj)
        if params.get("Sorter") is not None:
            self.Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self.Sorter.append(obj)
        self.PageIndex = params.get("PageIndex")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMappingResultsResponse(AbstractModel):
    """DescribeMappingResults返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Data: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.Results`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = Results()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSafetyEventListRequest(AbstractModel):
    """DescribeSafetyEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 搜索过滤查询参数
        :type Filter: str
        :param Limit: 限制数目
        :type Limit: int
        :param Offset: 页偏移
        :type Offset: int
        :param Order: 排序列名
        :type Order: str
        :param By: 排序升降：desc-降序 asc-升序
        :type By: str
        :param StartTime: 开始查询时间
        :type StartTime: str
        :param EndTime: 结束查询时间
        :type EndTime: str
        :param IsFilterResponseTime: 是否过滤响应时间
        :type IsFilterResponseTime: bool
        """
        self.Filter = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None
        self.StartTime = None
        self.EndTime = None
        self.IsFilterResponseTime = None


    def _deserialize(self, params):
        self.Filter = params.get("Filter")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsFilterResponseTime = params.get("IsFilterResponseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSafetyEventListResponse(AbstractModel):
    """DescribeSafetyEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 事件列表
        :type List: list of DataEvent
        :param Total: 事件总条数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DataEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeSocAlertDetailsRequest(AbstractModel):
    """DescribeSocAlertDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param AlertId: 告警id
        :type AlertId: str
        :param AlertTimestamp: 告警时间，取Timestamp字段
        :type AlertTimestamp: str
        """
        self.AlertId = None
        self.AlertTimestamp = None


    def _deserialize(self, params):
        self.AlertId = params.get("AlertId")
        self.AlertTimestamp = params.get("AlertTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocAlertDetailsResponse(AbstractModel):
    """DescribeSocAlertDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回详情数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.AlertDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AlertDetail()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSocAlertListRequest(AbstractModel):
    """DescribeSocAlertList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 页大小
        :type PageSize: int
        :param PageIndex: 页码
        :type PageIndex: int
        :param Scenes: 1:急需关注 2.重保监控 3.全量告警
        :type Scenes: int
        :param Filter: 查询参数
        :type Filter: list of QueryFilter
        :param Sorter: 排序参数
        :type Sorter: list of QuerySort
        :param ExportFlag: 是否导出
        :type ExportFlag: bool
        """
        self.PageSize = None
        self.PageIndex = None
        self.Scenes = None
        self.Filter = None
        self.Sorter = None
        self.ExportFlag = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageIndex = params.get("PageIndex")
        self.Scenes = params.get("Scenes")
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filter.append(obj)
        if params.get("Sorter") is not None:
            self.Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self.Sorter.append(obj)
        self.ExportFlag = params.get("ExportFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocAlertListResponse(AbstractModel):
    """DescribeSocAlertList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 业务数据
        :type Data: :class:`tencentcloud.ssa.v20180608.models.AlertListData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AlertListData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSocCheckItemListRequest(AbstractModel):
    """DescribeSocCheckItemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 查询参数,可支持的排序字段:Name,Type,AssetType,Level,Standard,IsFree
        :type Filter: list of QueryFilter
        :param Sorter: 排序参数:无
        :type Sorter: list of QuerySort
        :param PageSize: 当前页码数据，默认值为10
        :type PageSize: int
        :param PageIndex: 当前页面索引，默认值为0
        :type PageIndex: int
        """
        self.Filter = None
        self.Sorter = None
        self.PageSize = None
        self.PageIndex = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filter.append(obj)
        if params.get("Sorter") is not None:
            self.Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self.Sorter.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageIndex = params.get("PageIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCheckItemListResponse(AbstractModel):
    """DescribeSocCheckItemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 检查项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCheckItemListRspRsp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeSocCheckItemListRspRsp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSocCheckItemListRspRsp(AbstractModel):
    """云安全配置检查项列表

    """

    def __init__(self):
        r"""
        :param List: 检查项详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of SocCheckItemV1
        :param Total: 检查项总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self.List = None
        self.Total = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SocCheckItemV1()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCheckResultListRequest(AbstractModel):
    """DescribeSocCheckResultList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 查询参数,可支持的查询参数：
Name,Type,AssetType,Result,PloyName,PloyId
        :type Filter: list of QueryFilter
        :param Sorter: 排序参数,可支持的排序参数：CheckStatus,RiskCount
        :type Sorter: list of QuerySort
        :param PageSize: 当前页码数据，默认值为10
        :type PageSize: int
        :param PageIndex: 当前页面索引，默认值为0
        :type PageIndex: int
        :param AssetId: 资产id
        :type AssetId: str
        """
        self.Filter = None
        self.Sorter = None
        self.PageSize = None
        self.PageIndex = None
        self.AssetId = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filter.append(obj)
        if params.get("Sorter") is not None:
            self.Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self.Sorter.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageIndex = params.get("PageIndex")
        self.AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCheckResultListResponse(AbstractModel):
    """DescribeSocCheckResultList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCheckResultListRspRsp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeSocCheckResultListRspRsp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSocCheckResultListRspRsp(AbstractModel):
    """检查项结果详情列表

    """

    def __init__(self):
        r"""
        :param List: 具体检查项详情
        :type List: list of SocCheckResult
        :param Total: 检查结果总数
        :type Total: int
        :param LowTotal: 低危个数
        :type LowTotal: int
        :param MiddleTotal: 中危个数
        :type MiddleTotal: int
        :param HighTotal: 高危个数
        :type HighTotal: int
        :param NormalTotal: 正常个数
        :type NormalTotal: int
        """
        self.List = None
        self.Total = None
        self.LowTotal = None
        self.MiddleTotal = None
        self.HighTotal = None
        self.NormalTotal = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SocCheckResult()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.LowTotal = params.get("LowTotal")
        self.MiddleTotal = params.get("MiddleTotal")
        self.HighTotal = params.get("HighTotal")
        self.NormalTotal = params.get("NormalTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCspmComplianceRequest(AbstractModel):
    """DescribeSocCspmCompliance请求参数结构体

    """


class DescribeSocCspmComplianceResponse(AbstractModel):
    """DescribeSocCspmCompliance返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.SocComplianceInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SocComplianceInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeVulDetailRequest(AbstractModel):
    """DescribeVulDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param UniqId: 漏洞唯一标识符
        :type UniqId: str
        :param Source: 查看详情来源
        :type Source: str
        """
        self.UniqId = None
        self.Source = None


    def _deserialize(self, params):
        self.UniqId = params.get("UniqId")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulDetailResponse(AbstractModel):
    """DescribeVulDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulType: 漏洞类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VulType: int
        :param SubVulType: 漏洞子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SubVulType: str
        :param CvssScore: cvss分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssScore: str
        :param Cvss: cvss值
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvss: str
        :param Cve: cve编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Cve: str
        :param Cnvd: cnvd编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Cnvd: str
        :param Cnnvd: cnnvd编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Cnnvd: str
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Reference: 参考
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: str
        :param Repair: 修复意见
注意：此字段可能返回 null，表示取不到有效值。
        :type Repair: str
        :param ReleaseTime: 披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Name: 漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Level: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param ImpactAsset: 受影响资产唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactAsset: str
        :param ImpactAssetName: 受影响资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactAssetName: str
        :param IsAssetDeleted: 受影响资产是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssetDeleted: bool
        :param Source: 漏洞来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param VulUrl: 漏洞URL
注意：此字段可能返回 null，表示取不到有效值。
        :type VulUrl: str
        :param SsaAssetCategory: 资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetCategory: int
        :param VulPath: 资产文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type VulPath: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulType = None
        self.SubVulType = None
        self.CvssScore = None
        self.Cvss = None
        self.Cve = None
        self.Cnvd = None
        self.Cnnvd = None
        self.Desc = None
        self.Reference = None
        self.Repair = None
        self.ReleaseTime = None
        self.UpdateTime = None
        self.Name = None
        self.Level = None
        self.Status = None
        self.ImpactAsset = None
        self.ImpactAssetName = None
        self.IsAssetDeleted = None
        self.Source = None
        self.VulUrl = None
        self.SsaAssetCategory = None
        self.VulPath = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.SubVulType = params.get("SubVulType")
        self.CvssScore = params.get("CvssScore")
        self.Cvss = params.get("Cvss")
        self.Cve = params.get("Cve")
        self.Cnvd = params.get("Cnvd")
        self.Cnnvd = params.get("Cnnvd")
        self.Desc = params.get("Desc")
        self.Reference = params.get("Reference")
        self.Repair = params.get("Repair")
        self.ReleaseTime = params.get("ReleaseTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.ImpactAsset = params.get("ImpactAsset")
        self.ImpactAssetName = params.get("ImpactAssetName")
        self.IsAssetDeleted = params.get("IsAssetDeleted")
        self.Source = params.get("Source")
        self.VulUrl = params.get("VulUrl")
        self.SsaAssetCategory = params.get("SsaAssetCategory")
        self.VulPath = params.get("VulPath")
        self.RequestId = params.get("RequestId")


class DescribeVulListRequest(AbstractModel):
    """DescribeVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Params: 查询过滤参数
        :type Params: str
        """
        self.Params = None


    def _deserialize(self, params):
        self.Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulListResponse(AbstractModel):
    """DescribeVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 漏洞列表
        :type Data: :class:`tencentcloud.ssa.v20180608.models.VulList`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VulList()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否需要精确匹配
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDataSaEventPub(AbstractModel):
    """DataSaEventPub

    """

    def __init__(self):
        r"""
        :param Time: 时间
        :type Time: str
        :param EventType1: 安全事件1级分类
        :type EventType1: int
        :param EventType2: 安全事件2级分类
        :type EventType2: int
        :param EventName: 安全事件名称
        :type EventName: str
        :param Level: 风险等级
        :type Level: int
        :param Status: 安全事件状态
        :type Status: int
        :param SrcIp: 攻击源ip
        :type SrcIp: str
        :param DstIp: 攻击目标ip
        :type DstIp: str
        :param DstPort: 攻击目标端口
        :type DstPort: int
        :param Asset: 受影响资产
        :type Asset: str
        :param OldIdMd5: 私有字段和公有字段映射的原始采集数据唯一标识的MD5值
        :type OldIdMd5: str
        """
        self.Time = None
        self.EventType1 = None
        self.EventType2 = None
        self.EventName = None
        self.Level = None
        self.Status = None
        self.SrcIp = None
        self.DstIp = None
        self.DstPort = None
        self.Asset = None
        self.OldIdMd5 = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.EventType1 = params.get("EventType1")
        self.EventType2 = params.get("EventType2")
        self.EventName = params.get("EventName")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.SrcIp = params.get("SrcIp")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.Asset = params.get("Asset")
        self.OldIdMd5 = params.get("OldIdMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MappingResult(AbstractModel):
    """测绘记录

    """

    def __init__(self):
        r"""
        :param AssetName: 资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param AssetIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIp: str
        :param PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param Service: 服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param Component: 组件
注意：此字段可能返回 null，表示取不到有效值。
        :type Component: str
        :param Process: 进程
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: str
        :param OS: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type OS: str
        :param LastMappingTime: 测绘时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMappingTime: str
        :param DisposalRecommendations: 处置建议
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalRecommendations: str
        :param DisposalRecommendationDetails: 处置建议详情
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalRecommendationDetails: str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param MappingStatus: 测绘状态
注意：此字段可能返回 null，表示取不到有效值。
        :type MappingStatus: int
        :param Region: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param SecurityStatus: 安全防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityStatus: list of SecurityStatus
        :param DisposalRecommendation: 处置建议
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalRecommendation: int
        :param MappingType: 测绘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MappingType: str
        """
        self.AssetName = None
        self.AssetIp = None
        self.PrivateIp = None
        self.AssetId = None
        self.Protocol = None
        self.Port = None
        self.Service = None
        self.Component = None
        self.Process = None
        self.OS = None
        self.LastMappingTime = None
        self.DisposalRecommendations = None
        self.DisposalRecommendationDetails = None
        self.AssetType = None
        self.Domain = None
        self.MappingStatus = None
        self.Region = None
        self.SecurityStatus = None
        self.DisposalRecommendation = None
        self.MappingType = None


    def _deserialize(self, params):
        self.AssetName = params.get("AssetName")
        self.AssetIp = params.get("AssetIp")
        self.PrivateIp = params.get("PrivateIp")
        self.AssetId = params.get("AssetId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Service = params.get("Service")
        self.Component = params.get("Component")
        self.Process = params.get("Process")
        self.OS = params.get("OS")
        self.LastMappingTime = params.get("LastMappingTime")
        self.DisposalRecommendations = params.get("DisposalRecommendations")
        self.DisposalRecommendationDetails = params.get("DisposalRecommendationDetails")
        self.AssetType = params.get("AssetType")
        self.Domain = params.get("Domain")
        self.MappingStatus = params.get("MappingStatus")
        self.Region = params.get("Region")
        if params.get("SecurityStatus") is not None:
            self.SecurityStatus = []
            for item in params.get("SecurityStatus"):
                obj = SecurityStatus()
                obj._deserialize(item)
                self.SecurityStatus.append(obj)
        self.DisposalRecommendation = params.get("DisposalRecommendation")
        self.MappingType = params.get("MappingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjDataSaEventPub(AbstractModel):
    """DataSaEventPub

    """

    def __init__(self):
        r"""
        :param Count: Count
        :type Count: int
        :param List: List
        :type List: list of ListDataSaEventPub
        """
        self.Count = None
        self.List = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ListDataSaEventPub()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param FilterKey: 过滤key
        :type FilterKey: str
        :param FilterOperatorType: 操作符(只支持32位)
        :type FilterOperatorType: int
        :param FilterValue: 过滤value
        :type FilterValue: str
        """
        self.FilterKey = None
        self.FilterOperatorType = None
        self.FilterValue = None


    def _deserialize(self, params):
        self.FilterKey = params.get("FilterKey")
        self.FilterOperatorType = params.get("FilterOperatorType")
        self.FilterValue = params.get("FilterValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySort(AbstractModel):
    """排序的字段

    """

    def __init__(self):
        r"""
        :param SortKey: 排序字段
        :type SortKey: str
        :param SortType: 顺序，1升序2降序
        :type SortType: int
        """
        self.SortKey = None
        self.SortType = None


    def _deserialize(self, params):
        self.SortKey = params.get("SortKey")
        self.SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Results(AbstractModel):
    """测绘结果

    """

    def __init__(self):
        r"""
        :param Statistics: 测绘类型统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Statistics: list of AssetTypeStatistic
        :param Result: 测绘结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of MappingResult
        :param TaskCount: 测绘任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCount: int
        :param TaskMaxCount: 最大测绘任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMaxCount: int
        """
        self.Statistics = None
        self.Result = None
        self.TaskCount = None
        self.TaskMaxCount = None


    def _deserialize(self, params):
        if params.get("Statistics") is not None:
            self.Statistics = []
            for item in params.get("Statistics"):
                obj = AssetTypeStatistic()
                obj._deserialize(item)
                self.Statistics.append(obj)
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = MappingResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.TaskCount = params.get("TaskCount")
        self.TaskMaxCount = params.get("TaskMaxCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaDivulgeDataQueryPub(AbstractModel):
    """查询_通用字段

    """

    def __init__(self):
        r"""
        :param Id: Id信息
        :type Id: str
        :param Uin: 用户Uin
        :type Uin: str
        :param AppId: 用户AppId
        :type AppId: str
        :param EventName: 事件名称
        :type EventName: str
        :param DivulgeSoure: 监控源 0:全部 1:GitHub 2:暗网 默认值1
        :type DivulgeSoure: str
        :param Asset: 受影响资产
        :type Asset: str
        :param RuleName: 命中主题集下的规则topic名称
        :type RuleName: str
        :param RuleId: 命中主题集下的规则topic唯一id
        :type RuleId: str
        :param RuleWord: 命中主题集下的自定义规则策略
        :type RuleWord: str
        :param ScanUrl: 扫描监测url
        :type ScanUrl: str
        :param ScanCount: 扫描监测命中次数
        :type ScanCount: str
        :param Level: 风险等级 -1:未知 1:低危 2:中危 3:高危 4:严重
        :type Level: str
        :param Status: 安全事件处理状态 -1:未知 1:待处理 2:已处理 3:误报 4:已忽略 5:已知晓 6:已信任
        :type Status: str
        :param EventTime: 安全事件发生时间
        :type EventTime: str
        :param InsertTime: 事件插入时间
        :type InsertTime: str
        :param UpdateTime: 事件更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.Uin = None
        self.AppId = None
        self.EventName = None
        self.DivulgeSoure = None
        self.Asset = None
        self.RuleName = None
        self.RuleId = None
        self.RuleWord = None
        self.ScanUrl = None
        self.ScanCount = None
        self.Level = None
        self.Status = None
        self.EventTime = None
        self.InsertTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uin = params.get("Uin")
        self.AppId = params.get("AppId")
        self.EventName = params.get("EventName")
        self.DivulgeSoure = params.get("DivulgeSoure")
        self.Asset = params.get("Asset")
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        self.RuleWord = params.get("RuleWord")
        self.ScanUrl = params.get("ScanUrl")
        self.ScanCount = params.get("ScanCount")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.EventTime = params.get("EventTime")
        self.InsertTime = params.get("InsertTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaDivulgeDataQueryPubList(AbstractModel):
    """自定义泄露事件列表

    """

    def __init__(self):
        r"""
        :param Count: 数据条数
        :type Count: int
        :param List: 自定义泄露事件列表
        :type List: list of SaDivulgeDataQueryPub
        """
        self.Count = None
        self.List = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SaDivulgeDataQueryPub()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaDivulgeDataQueryPubRequest(AbstractModel):
    """SaDivulgeDataQueryPub请求参数结构体

    """

    def __init__(self):
        r"""
        :param QueryKey: 模糊查询字段(针对appid或者uin)
        :type QueryKey: str
        :param EventName: 安全事件名称
        :type EventName: str
        :param DivulgeSoure: 监控源  0:全部 1:GitHub 2:暗网 默认值1
        :type DivulgeSoure: str
        :param Asset: 受影响资产
        :type Asset: str
        :param RuleName: 命中主题集下的规则topic名称
        :type RuleName: str
        :param RuleId: 命中主题集下的规则topic唯一id
        :type RuleId: str
        :param Level: 风险等级 -1:未知 1:低危 2:中危 3:高危 4:严重
        :type Level: str
        :param Status: 安全事件处理状态 -1:未知 1:待处理 2:已处理 3:误报 4:已忽略 5:已知晓 6:已信任
        :type Status: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Offset: 查询起始地址
        :type Offset: str
        :param Limit: 查询个数
        :type Limit: str
        """
        self.QueryKey = None
        self.EventName = None
        self.DivulgeSoure = None
        self.Asset = None
        self.RuleName = None
        self.RuleId = None
        self.Level = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.QueryKey = params.get("QueryKey")
        self.EventName = params.get("EventName")
        self.DivulgeSoure = params.get("DivulgeSoure")
        self.Asset = params.get("Asset")
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaDivulgeDataQueryPubResponse(AbstractModel):
    """SaDivulgeDataQueryPub返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 自定义泄露事件列表
        :type Data: :class:`tencentcloud.ssa.v20180608.models.SaDivulgeDataQueryPubList`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SaDivulgeDataQueryPubList()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SaEventPubRequest(AbstractModel):
    """SaEventPub请求参数结构体

    """

    def __init__(self):
        r"""
        :param Asset: 受影响资产
        :type Asset: str
        :param EventName: 安全事件名称
        :type EventName: str
        :param EventType1: 安全事件1级分类，-1:未知 0:全部 1:攻击事件 2:侦查事件 3:僵木蠕毒 4:违规策略
        :type EventType1: int
        :param EventType2: 安全事件2级分类，-1:未知 0:全部 1:DDOS事件 2:Web攻击 3:木马 4:异地登录 5:密码破解
        :type EventType2: int
        :param Level: 风险等级，-1:未知 0:全部 1:低危 2:中危 3:高危 4:严重，可多选，如：1,2
        :type Level: str
        :param Status: 安全事件状态，-1:未知 0:全部 1:待处理 2:已处理 3:误报 4:已忽略 5:已知晓 6:已信任
        :type Status: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param Offset: 查询起始地址
        :type Offset: int
        :param Limit: 查询个数
        :type Limit: int
        :param EndTime: 结束时间
        :type EndTime: str
        :param OldIdMd5: 私有字段和公有字段映射的原始采集数据唯一标识的MD5值
        :type OldIdMd5: str
        """
        self.Asset = None
        self.EventName = None
        self.EventType1 = None
        self.EventType2 = None
        self.Level = None
        self.Status = None
        self.StartTime = None
        self.Offset = None
        self.Limit = None
        self.EndTime = None
        self.OldIdMd5 = None


    def _deserialize(self, params):
        self.Asset = params.get("Asset")
        self.EventName = params.get("EventName")
        self.EventType1 = params.get("EventType1")
        self.EventType2 = params.get("EventType2")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EndTime = params.get("EndTime")
        self.OldIdMd5 = params.get("OldIdMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaEventPubResponse(AbstractModel):
    """SaEventPub返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataSaEventPub: DataSaEventPub
        :type DataSaEventPub: :class:`tencentcloud.ssa.v20180608.models.ObjDataSaEventPub`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataSaEventPub = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataSaEventPub") is not None:
            self.DataSaEventPub = ObjDataSaEventPub()
            self.DataSaEventPub._deserialize(params.get("DataSaEventPub"))
        self.RequestId = params.get("RequestId")


class SecurityStatus(AbstractModel):
    """安全放回状态

    """


class SocCheckItem(AbstractModel):
    """SocCheckItem类型

    """

    def __init__(self):
        r"""
        :param Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param LevelId: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type LevelId: str
        :param SuccessCount: 成功数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param FailCount: 失败数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCount: int
        """
        self.Name = None
        self.LevelId = None
        self.SuccessCount = None
        self.FailCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.LevelId = params.get("LevelId")
        self.SuccessCount = params.get("SuccessCount")
        self.FailCount = params.get("FailCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocCheckItemV1(AbstractModel):
    """检查项相关信息

    """

    def __init__(self):
        r"""
        :param CheckId: 检查项id
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckId: str
        :param Name: 配置要求
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Type: 检查项类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param AssetType: 检查对象
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param Level: 默认风险等级 2:低危 3:中危 4:高危
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param Standard: 相关规范
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        :param IsFree: 检查项是否付费 1:免费 2:付费
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFree: int
        """
        self.CheckId = None
        self.Name = None
        self.Type = None
        self.AssetType = None
        self.Level = None
        self.Standard = None
        self.IsFree = None


    def _deserialize(self, params):
        self.CheckId = params.get("CheckId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.AssetType = params.get("AssetType")
        self.Level = params.get("Level")
        self.Standard = params.get("Standard")
        self.IsFree = params.get("IsFree")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocCheckResult(AbstractModel):
    """云安全配置检测结果

    """

    def __init__(self):
        r"""
        :param CheckId: 检查项的uuid
        :type CheckId: str
        :param Name: 配置要求
        :type Name: str
        :param Type: 检查项的类型
        :type Type: str
        :param AssetType: 检查对象
        :type AssetType: str
        :param PloyName: 策略名
        :type PloyName: str
        :param PloyId: 策略id
        :type PloyId: int
        :param Result: 正常,低危,中危,高危
        :type Result: str
        :param FailAssetNum: 不符合数
        :type FailAssetNum: int
        :param TotalAssetNum: 总数
        :type TotalAssetNum: int
        :param DealUrl: 处置建议url链接
        :type DealUrl: str
        """
        self.CheckId = None
        self.Name = None
        self.Type = None
        self.AssetType = None
        self.PloyName = None
        self.PloyId = None
        self.Result = None
        self.FailAssetNum = None
        self.TotalAssetNum = None
        self.DealUrl = None


    def _deserialize(self, params):
        self.CheckId = params.get("CheckId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.AssetType = params.get("AssetType")
        self.PloyName = params.get("PloyName")
        self.PloyId = params.get("PloyId")
        self.Result = params.get("Result")
        self.FailAssetNum = params.get("FailAssetNum")
        self.TotalAssetNum = params.get("TotalAssetNum")
        self.DealUrl = params.get("DealUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocComplianceInfoResp(AbstractModel):
    """返回结构

    """

    def __init__(self):
        r"""
        :param Items: 合格项
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SocComplianceItem
        """
        self.Items = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SocComplianceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocComplianceItem(AbstractModel):
    """soc合规信息

    """

    def __init__(self):
        r"""
        :param Item: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param StandardItem: 分类
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardItem: str
        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param Suggestion: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param ProStr: 产品字符
注意：此字段可能返回 null，表示取不到有效值。
        :type ProStr: str
        :param Production: 产品数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Production: list of SocProductionItem
        :param CheckItems: 配置项数组
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckItems: list of SocCheckItem
        """
        self.Item = None
        self.Description = None
        self.StandardItem = None
        self.Result = None
        self.Suggestion = None
        self.ProStr = None
        self.Production = None
        self.CheckItems = None


    def _deserialize(self, params):
        self.Item = params.get("Item")
        self.Description = params.get("Description")
        self.StandardItem = params.get("StandardItem")
        self.Result = params.get("Result")
        self.Suggestion = params.get("Suggestion")
        self.ProStr = params.get("ProStr")
        if params.get("Production") is not None:
            self.Production = []
            for item in params.get("Production"):
                obj = SocProductionItem()
                obj._deserialize(item)
                self.Production.append(obj)
        if params.get("CheckItems") is not None:
            self.CheckItems = []
            for item in params.get("CheckItems"):
                obj = SocCheckItem()
                obj._deserialize(item)
                self.CheckItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocProductionItem(AbstractModel):
    """soc产品购买信息

    """

    def __init__(self):
        r"""
        :param Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Index: 标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.Name = None
        self.Index = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Index = params.get("Index")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param Fid: 数据库标识
        :type Fid: int
        :param Fname: 标签名称字段
        :type Fname: str
        """
        self.Fid = None
        self.Fname = None


    def _deserialize(self, params):
        self.Fid = params.get("Fid")
        self.Fname = params.get("Fname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulItem(AbstractModel):
    """漏洞管理漏洞数据

    """

    def __init__(self):
        r"""
        :param Id: 标识
        :type Id: str
        :param VulName: 漏洞名称
        :type VulName: str
        :param Type: 漏洞类型
        :type Type: int
        :param Level: 风险等级
        :type Level: int
        :param Status: 处理状态
        :type Status: int
        :param Time: 发现时间
        :type Time: str
        :param ImpactAssetNum: 影响资产数
        :type ImpactAssetNum: int
        :param ImpactAsset: 影响资产id
        :type ImpactAsset: str
        :param ImpactAssetName: 影响资产名称
        :type ImpactAssetName: str
        :param VulDetail: 漏洞描述
        :type VulDetail: str
        :param VulRefLink: 参考链接
        :type VulRefLink: str
        :param OldIdMd5: Md5值
        :type OldIdMd5: str
        :param UniqId: 漏洞唯一标识
        :type UniqId: str
        :param OperateTime: 忽略时间
        :type OperateTime: str
        :param IsAssetDeleted: 受影响资产是否下线
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssetDeleted: str
        :param DiscoverTime: 漏洞首次发现时间
        :type DiscoverTime: str
        :param OriginId: 主机源信息标识符
        :type OriginId: int
        :param Region: 资产区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Vpcid: 资产所属网络
注意：此字段可能返回 null，表示取不到有效值。
        :type Vpcid: str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param AssetSubType: 资产子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubType: str
        :param AssetIpAll: 资产IP
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIpAll: list of str
        :param PublicIpAddresses: cvm类型的公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: cvm类型的内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param VulSource: 漏洞来源
注意：此字段可能返回 null，表示取不到有效值。
        :type VulSource: str
        :param AffectedUrl: 影响URL
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedUrl: str
        :param SsaAssetCategory: 资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetCategory: int
        :param VulUrl: 影响url
注意：此字段可能返回 null，表示取不到有效值。
        :type VulUrl: str
        :param IsOpen: 是否扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOpen: bool
        :param YzHostId: 御知主机id
注意：此字段可能返回 null，表示取不到有效值。
        :type YzHostId: int
        :param VulRepairPlan: 漏洞描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VulRepairPlan: str
        :param VulPath: 漏洞文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type VulPath: str
        """
        self.Id = None
        self.VulName = None
        self.Type = None
        self.Level = None
        self.Status = None
        self.Time = None
        self.ImpactAssetNum = None
        self.ImpactAsset = None
        self.ImpactAssetName = None
        self.VulDetail = None
        self.VulRefLink = None
        self.OldIdMd5 = None
        self.UniqId = None
        self.OperateTime = None
        self.IsAssetDeleted = None
        self.DiscoverTime = None
        self.OriginId = None
        self.Region = None
        self.Vpcid = None
        self.AssetType = None
        self.AssetSubType = None
        self.AssetIpAll = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.VulSource = None
        self.AffectedUrl = None
        self.SsaAssetCategory = None
        self.VulUrl = None
        self.IsOpen = None
        self.YzHostId = None
        self.VulRepairPlan = None
        self.VulPath = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.VulName = params.get("VulName")
        self.Type = params.get("Type")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.Time = params.get("Time")
        self.ImpactAssetNum = params.get("ImpactAssetNum")
        self.ImpactAsset = params.get("ImpactAsset")
        self.ImpactAssetName = params.get("ImpactAssetName")
        self.VulDetail = params.get("VulDetail")
        self.VulRefLink = params.get("VulRefLink")
        self.OldIdMd5 = params.get("OldIdMd5")
        self.UniqId = params.get("UniqId")
        self.OperateTime = params.get("OperateTime")
        self.IsAssetDeleted = params.get("IsAssetDeleted")
        self.DiscoverTime = params.get("DiscoverTime")
        self.OriginId = params.get("OriginId")
        self.Region = params.get("Region")
        self.Vpcid = params.get("Vpcid")
        self.AssetType = params.get("AssetType")
        self.AssetSubType = params.get("AssetSubType")
        self.AssetIpAll = params.get("AssetIpAll")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.VulSource = params.get("VulSource")
        self.AffectedUrl = params.get("AffectedUrl")
        self.SsaAssetCategory = params.get("SsaAssetCategory")
        self.VulUrl = params.get("VulUrl")
        self.IsOpen = params.get("IsOpen")
        self.YzHostId = params.get("YzHostId")
        self.VulRepairPlan = params.get("VulRepairPlan")
        self.VulPath = params.get("VulPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulList(AbstractModel):
    """漏洞管理漏洞列表

    """

    def __init__(self):
        r"""
        :param List: 列表
        :type List: list of VulItem
        :param Total: 总数
        :type Total: int
        """
        self.List = None
        self.Total = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = VulItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        