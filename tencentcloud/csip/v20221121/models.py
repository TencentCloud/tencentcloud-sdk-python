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


class AddNewBindRoleUserRequest(AbstractModel):
    """AddNewBindRoleUser请求参数结构体

    """


class AddNewBindRoleUserResponse(AbstractModel):
    """AddNewBindRoleUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 0成功，其他失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class AssetBaseInfoResponse(AbstractModel):
    """主机资产详情

    """

    def __init__(self):
        r"""
        :param VpcId: vpc-id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param VpcName: vpc-name
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param Os: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        :param PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param AccountNum: 账号数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountNum: int
        :param PortNum: 端口数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PortNum: int
        :param ProcessNum: 进程数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessNum: int
        :param SoftApplicationNum: 软件应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftApplicationNum: int
        :param DatabaseNum: 数据库数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseNum: int
        :param WebApplicationNum: Web应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebApplicationNum: int
        :param ServiceNum: 服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceNum: int
        :param WebFrameworkNum: web框架数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebFrameworkNum: int
        :param WebSiteNum: Web站点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSiteNum: int
        :param JarPackageNum: Jar包数量
注意：此字段可能返回 null，表示取不到有效值。
        :type JarPackageNum: int
        :param StartServiceNum: 启动服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartServiceNum: int
        :param ScheduledTaskNum: 计划任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledTaskNum: int
        :param EnvironmentVariableNum: 环境变量数量
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentVariableNum: int
        :param KernelModuleNum: 内核模块数量
注意：此字段可能返回 null，表示取不到有效值。
        :type KernelModuleNum: int
        :param SystemInstallationPackageNum: 系统安装包数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemInstallationPackageNum: int
        :param SurplusProtectDay: 剩余防护时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SurplusProtectDay: int
        :param CWPStatus: 客户端是否安装  1 已安装 0 未安装
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPStatus: int
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param ProtectLevel: 防护等级
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectLevel: str
        :param ProtectedDay: 防护时长
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectedDay: int
        """
        self.VpcId = None
        self.VpcName = None
        self.AssetName = None
        self.Os = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Region = None
        self.AssetType = None
        self.AssetId = None
        self.AccountNum = None
        self.PortNum = None
        self.ProcessNum = None
        self.SoftApplicationNum = None
        self.DatabaseNum = None
        self.WebApplicationNum = None
        self.ServiceNum = None
        self.WebFrameworkNum = None
        self.WebSiteNum = None
        self.JarPackageNum = None
        self.StartServiceNum = None
        self.ScheduledTaskNum = None
        self.EnvironmentVariableNum = None
        self.KernelModuleNum = None
        self.SystemInstallationPackageNum = None
        self.SurplusProtectDay = None
        self.CWPStatus = None
        self.Tag = None
        self.ProtectLevel = None
        self.ProtectedDay = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.AssetName = params.get("AssetName")
        self.Os = params.get("Os")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Region = params.get("Region")
        self.AssetType = params.get("AssetType")
        self.AssetId = params.get("AssetId")
        self.AccountNum = params.get("AccountNum")
        self.PortNum = params.get("PortNum")
        self.ProcessNum = params.get("ProcessNum")
        self.SoftApplicationNum = params.get("SoftApplicationNum")
        self.DatabaseNum = params.get("DatabaseNum")
        self.WebApplicationNum = params.get("WebApplicationNum")
        self.ServiceNum = params.get("ServiceNum")
        self.WebFrameworkNum = params.get("WebFrameworkNum")
        self.WebSiteNum = params.get("WebSiteNum")
        self.JarPackageNum = params.get("JarPackageNum")
        self.StartServiceNum = params.get("StartServiceNum")
        self.ScheduledTaskNum = params.get("ScheduledTaskNum")
        self.EnvironmentVariableNum = params.get("EnvironmentVariableNum")
        self.KernelModuleNum = params.get("KernelModuleNum")
        self.SystemInstallationPackageNum = params.get("SystemInstallationPackageNum")
        self.SurplusProtectDay = params.get("SurplusProtectDay")
        self.CWPStatus = params.get("CWPStatus")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.ProtectLevel = params.get("ProtectLevel")
        self.ProtectedDay = params.get("ProtectedDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMAssetVO(AbstractModel):
    """主机资产信息

    """

    def __init__(self):
        r"""
        :param AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param CWPStatus: 防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CWPStatus: int
        :param AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param PrivateIp: 私网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param VpcName: vpc 名
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param AppId: appid信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param NickName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param AvailableArea: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableArea: str
        :param IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param SubnetName: 子网名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param InstanceUuid: uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceUuid: str
        :param InstanceQUuid: qquid
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceQUuid: str
        :param OsName: os名
注意：此字段可能返回 null，表示取不到有效值。
        :type OsName: str
        :param PartitionCount: 分区
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionCount: int
        :param CPUInfo: cpu信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUInfo: str
        :param CPUSize: cpu大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUSize: int
        :param CPULoad: cpu负载
注意：此字段可能返回 null，表示取不到有效值。
        :type CPULoad: str
        :param MemorySize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemorySize: str
        :param MemoryLoad: 内存负载
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryLoad: str
        :param DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: str
        :param DiskLoad: 硬盘负载
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskLoad: str
        :param AccountCount: 账号数
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountCount: str
        :param ProcessCount: 进程数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessCount: str
        :param AppCount: 软件应用
注意：此字段可能返回 null，表示取不到有效值。
        :type AppCount: str
        :param PortCount: 监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type PortCount: int
        :param Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param Intercept: 网络拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type Intercept: int
        :param InBandwidth: 入向峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InBandwidth: str
        :param OutBandwidth: 出向峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type OutBandwidth: str
        :param InFlow: 入向累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type InFlow: str
        :param OutFlow: 出向累计流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OutFlow: str
        :param LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param NetWorkOut: 恶意主动外联
注意：此字段可能返回 null，表示取不到有效值。
        :type NetWorkOut: int
        :param PortRisk: 端口风险
注意：此字段可能返回 null，表示取不到有效值。
        :type PortRisk: int
        :param VulnerabilityRisk: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityRisk: int
        :param ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param ScanTask: 扫描任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param MemberId: memberId
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param Os: os全称
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        :param RiskExposure: 风险服务暴露
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskExposure: int
        """
        self.AssetId = None
        self.AssetName = None
        self.AssetType = None
        self.Region = None
        self.CWPStatus = None
        self.AssetCreateTime = None
        self.PublicIp = None
        self.PrivateIp = None
        self.VpcId = None
        self.VpcName = None
        self.AppId = None
        self.Uin = None
        self.NickName = None
        self.AvailableArea = None
        self.IsCore = None
        self.SubnetId = None
        self.SubnetName = None
        self.InstanceUuid = None
        self.InstanceQUuid = None
        self.OsName = None
        self.PartitionCount = None
        self.CPUInfo = None
        self.CPUSize = None
        self.CPULoad = None
        self.MemorySize = None
        self.MemoryLoad = None
        self.DiskSize = None
        self.DiskLoad = None
        self.AccountCount = None
        self.ProcessCount = None
        self.AppCount = None
        self.PortCount = None
        self.Attack = None
        self.Access = None
        self.Intercept = None
        self.InBandwidth = None
        self.OutBandwidth = None
        self.InFlow = None
        self.OutFlow = None
        self.LastScanTime = None
        self.NetWorkOut = None
        self.PortRisk = None
        self.VulnerabilityRisk = None
        self.ConfigurationRisk = None
        self.ScanTask = None
        self.Tag = None
        self.MemberId = None
        self.Os = None
        self.RiskExposure = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.AssetName = params.get("AssetName")
        self.AssetType = params.get("AssetType")
        self.Region = params.get("Region")
        self.CWPStatus = params.get("CWPStatus")
        self.AssetCreateTime = params.get("AssetCreateTime")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.NickName = params.get("NickName")
        self.AvailableArea = params.get("AvailableArea")
        self.IsCore = params.get("IsCore")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.InstanceUuid = params.get("InstanceUuid")
        self.InstanceQUuid = params.get("InstanceQUuid")
        self.OsName = params.get("OsName")
        self.PartitionCount = params.get("PartitionCount")
        self.CPUInfo = params.get("CPUInfo")
        self.CPUSize = params.get("CPUSize")
        self.CPULoad = params.get("CPULoad")
        self.MemorySize = params.get("MemorySize")
        self.MemoryLoad = params.get("MemoryLoad")
        self.DiskSize = params.get("DiskSize")
        self.DiskLoad = params.get("DiskLoad")
        self.AccountCount = params.get("AccountCount")
        self.ProcessCount = params.get("ProcessCount")
        self.AppCount = params.get("AppCount")
        self.PortCount = params.get("PortCount")
        self.Attack = params.get("Attack")
        self.Access = params.get("Access")
        self.Intercept = params.get("Intercept")
        self.InBandwidth = params.get("InBandwidth")
        self.OutBandwidth = params.get("OutBandwidth")
        self.InFlow = params.get("InFlow")
        self.OutFlow = params.get("OutFlow")
        self.LastScanTime = params.get("LastScanTime")
        self.NetWorkOut = params.get("NetWorkOut")
        self.PortRisk = params.get("PortRisk")
        self.VulnerabilityRisk = params.get("VulnerabilityRisk")
        self.ConfigurationRisk = params.get("ConfigurationRisk")
        self.ScanTask = params.get("ScanTask")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.MemberId = params.get("MemberId")
        self.Os = params.get("Os")
        self.RiskExposure = params.get("RiskExposure")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpRequest(AbstractModel):
    """CreateDomainAndIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param Content: -
        :type Content: list of str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpResponse(AbstractModel):
    """CreateDomainAndIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回创建成功的数量
        :type Data: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DBAssetVO(AbstractModel):
    """db资产输出字段

    """

    def __init__(self):
        r"""
        :param AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param VpcId: vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param VpcName: vpc标签
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param AssetCreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param ConfigurationRisk: 配置风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigurationRisk: int
        :param Attack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type Attack: int
        :param Access: 网络访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Access: int
        :param ScanTask: 扫描任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanTask: int
        :param AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param NickName: 昵称别名
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        """
        self.AssetId = None
        self.AssetName = None
        self.AssetType = None
        self.VpcId = None
        self.VpcName = None
        self.Region = None
        self.Domain = None
        self.AssetCreateTime = None
        self.LastScanTime = None
        self.ConfigurationRisk = None
        self.Attack = None
        self.Access = None
        self.ScanTask = None
        self.AppId = None
        self.Uin = None
        self.NickName = None
        self.Port = None
        self.Tag = None
        self.PrivateIp = None
        self.PublicIp = None
        self.Status = None
        self.IsCore = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.AssetName = params.get("AssetName")
        self.AssetType = params.get("AssetType")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.Region = params.get("Region")
        self.Domain = params.get("Domain")
        self.AssetCreateTime = params.get("AssetCreateTime")
        self.LastScanTime = params.get("LastScanTime")
        self.ConfigurationRisk = params.get("ConfigurationRisk")
        self.Attack = params.get("Attack")
        self.Access = params.get("Access")
        self.ScanTask = params.get("ScanTask")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.NickName = params.get("NickName")
        self.Port = params.get("Port")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.PrivateIp = params.get("PrivateIp")
        self.PublicIp = params.get("PublicIp")
        self.Status = params.get("Status")
        self.IsCore = params.get("IsCore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbAssetInfo(AbstractModel):
    """db资产详情

    """

    def __init__(self):
        r"""
        :param CFWStatus: 云防状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWStatus: int
        :param AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param VpcName: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param PublicIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param PrivateIp: 私网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param VpcId: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param CFWProtectLevel: 云防保护版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CFWProtectLevel: int
        :param Tag: tag信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        """
        self.CFWStatus = None
        self.AssetId = None
        self.VpcName = None
        self.AssetType = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Region = None
        self.VpcId = None
        self.AssetName = None
        self.CFWProtectLevel = None
        self.Tag = None


    def _deserialize(self, params):
        self.CFWStatus = params.get("CFWStatus")
        self.AssetId = params.get("AssetId")
        self.VpcName = params.get("VpcName")
        self.AssetType = params.get("AssetType")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.AssetName = params.get("AssetName")
        self.CFWProtectLevel = params.get("CFWProtectLevel")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetInfoRequest(AbstractModel):
    """DescribeCVMAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetId: -
        :type AssetId: str
        """
        self.AssetId = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetInfoResponse(AbstractModel):
    """DescribeCVMAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.AssetBaseInfoResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AssetBaseInfoResponse()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCVMAssetsRequest(AbstractModel):
    """DescribeCVMAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self.Filter = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = Filter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetsResponse(AbstractModel):
    """DescribeCVMAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Data: -
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CVMAssetVO
        :param RegionList: 地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param DefenseStatusList: 防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseStatusList: list of FilterDataObject
        :param VpcList: vpc枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcList: list of FilterDataObject
        :param AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param SystemTypeList: 操作系统枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemTypeList: list of FilterDataObject
        :param IpTypeList: ip列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTypeList: list of FilterDataObject
        :param AppIdList: appid列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param ZoneList: 可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneList: list of FilterDataObject
        :param OsList: os列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OsList: list of FilterDataObject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.RegionList = None
        self.DefenseStatusList = None
        self.VpcList = None
        self.AssetTypeList = None
        self.SystemTypeList = None
        self.IpTypeList = None
        self.AppIdList = None
        self.ZoneList = None
        self.OsList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CVMAssetVO()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self.DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.DefenseStatusList.append(obj)
        if params.get("VpcList") is not None:
            self.VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.VpcList.append(obj)
        if params.get("AssetTypeList") is not None:
            self.AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.AssetTypeList.append(obj)
        if params.get("SystemTypeList") is not None:
            self.SystemTypeList = []
            for item in params.get("SystemTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.SystemTypeList.append(obj)
        if params.get("IpTypeList") is not None:
            self.IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.IpTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self.AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        if params.get("OsList") is not None:
            self.OsList = []
            for item in params.get("OsList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.OsList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDbAssetInfoRequest(AbstractModel):
    """DescribeDbAssetInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetId: 资产id
        :type AssetId: str
        """
        self.AssetId = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetInfoResponse(AbstractModel):
    """DescribeDbAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: db资产详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.csip.v20221121.models.DbAssetInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DbAssetInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDbAssetsRequest(AbstractModel):
    """DescribeDbAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self.Filter = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = Filter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetsResponse(AbstractModel):
    """DescribeDbAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Data: 资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DBAssetVO
        :param RegionList: 地域枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionList: list of FilterDataObject
        :param AssetTypeList: 资产类型枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeList: list of FilterDataObject
        :param VpcList: Vpc枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcList: list of FilterDataObject
        :param AppIdList: Appid枚举
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of FilterDataObject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.RegionList = None
        self.AssetTypeList = None
        self.VpcList = None
        self.AppIdList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DBAssetVO()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self.AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self.VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self.AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.AppIdList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanReportListRequest(AbstractModel):
    """DescribeScanReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 列表过滤条件
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self.Filter = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = Filter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanReportListResponse(AbstractModel):
    """DescribeScanReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Data: 任务日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ScanTaskInfo
        :param UINList: 主账户ID列表
        :type UINList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.UINList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.UINList = params.get("UINList")
        self.RequestId = params.get("RequestId")


class DescribeSubnetAssetsRequest(AbstractModel):
    """DescribeSubnetAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self.Filter = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = Filter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetAssetsResponse(AbstractModel):
    """DescribeSubnetAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 列表
        :type Data: list of SubnetAsset
        :param TotalCount: 总数
        :type TotalCount: int
        :param RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param ZoneList: 可用区列表
        :type ZoneList: list of FilterDataObject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RegionList = None
        self.VpcList = None
        self.AppIdList = None
        self.ZoneList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubnetAsset()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.RegionList.append(obj)
        if params.get("VpcList") is not None:
            self.VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self.AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcAssetsRequest(AbstractModel):
    """DescribeVpcAssets请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filter: 过滤参数
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self.Filter = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = Filter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAssetsResponse(AbstractModel):
    """DescribeVpcAssets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 列表
        :type Data: list of Vpc
        :param TotalCount: 总数
        :type TotalCount: int
        :param VpcList: vpc列表
        :type VpcList: list of FilterDataObject
        :param RegionList: 地域列表
        :type RegionList: list of FilterDataObject
        :param AppIdList: appid列表
        :type AppIdList: list of FilterDataObject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.VpcList = None
        self.RegionList = None
        self.AppIdList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Vpc()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcList") is not None:
            self.VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.VpcList.append(obj)
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self.AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self.AppIdList.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """列表查询接口采用新filter 接口，直接传给后台供后台查询过滤

    """

    def __init__(self):
        r"""
        :param Limit: 查询数量限制
        :type Limit: int
        :param Offset: 查询偏移位置
        :type Offset: int
        :param Order: 排序采用升序还是降序 升:asc 降 desc
        :type Order: str
        :param By: 需排序的字段
        :type By: str
        :param Filters: 过滤的列及内容
        :type Filters: list of WhereFilter
        :param StartTime: 可填无， 日志使用查询时间
        :type StartTime: str
        :param EndTime: 可填无， 日志使用查询时间
        :type EndTime: str
        """
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None
        self.Filters = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = WhereFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterDataObject(AbstractModel):
    """过滤数据对象

    """

    def __init__(self):
        r"""
        :param Value: 英文翻译
        :type Value: str
        :param Text: 中文翻译
        :type Text: str
        """
        self.Value = None
        self.Text = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfo(AbstractModel):
    """扫描任务详情

    """

    def __init__(self):
        r"""
        :param TaskId: 任务日志Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TaskName: 任务日志名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param Status: 任务状态码：1等待开始  2正在扫描  3扫描出错 4扫描完成
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Progress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param TaskTime: 对应的展示时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTime: str
        :param ReportId: 报表id
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param ReportName: 报表名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportName: str
        :param ScanPlan: 扫描计划，0-周期任务,1-立即扫描,2-定时扫描,3-自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPlan: int
        :param AssetCount: 关联的资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCount: int
        :param AppId: APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param UIN: 用户主账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param UserName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self.TaskId = None
        self.TaskName = None
        self.Status = None
        self.Progress = None
        self.TaskTime = None
        self.ReportId = None
        self.ReportName = None
        self.ScanPlan = None
        self.AssetCount = None
        self.AppId = None
        self.UIN = None
        self.UserName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.TaskTime = params.get("TaskTime")
        self.ReportId = params.get("ReportId")
        self.ReportName = params.get("ReportName")
        self.ScanPlan = params.get("ScanPlan")
        self.AssetCount = params.get("AssetCount")
        self.AppId = params.get("AppId")
        self.UIN = params.get("UIN")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetAsset(AbstractModel):
    """子网资产

    """

    def __init__(self):
        r"""
        :param AppId: appid
        :type AppId: str
        :param Uin: uin
        :type Uin: str
        :param AssetId: 资产ID
        :type AssetId: str
        :param AssetName: 资产名
        :type AssetName: str
        :param Region: 区域
        :type Region: str
        :param VpcId: 私有网络id
        :type VpcId: str
        :param VpcName: 私有网络名
        :type VpcName: str
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param Nick: 昵称
        :type Nick: str
        :param CIDR: cidr
        :type CIDR: str
        :param Zone: 可用区
        :type Zone: str
        :param CVM: cvm数
        :type CVM: int
        :param AvailableIp: 可用ip数
        :type AvailableIp: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ConfigureRisk: 配置风险
        :type ConfigureRisk: int
        :param ScanTask: 任务数
        :type ScanTask: int
        :param LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param IsCore: 是否核心
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCore: int
        """
        self.AppId = None
        self.Uin = None
        self.AssetId = None
        self.AssetName = None
        self.Region = None
        self.VpcId = None
        self.VpcName = None
        self.Tag = None
        self.Nick = None
        self.CIDR = None
        self.Zone = None
        self.CVM = None
        self.AvailableIp = None
        self.CreateTime = None
        self.ConfigureRisk = None
        self.ScanTask = None
        self.LastScanTime = None
        self.IsCore = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.AssetId = params.get("AssetId")
        self.AssetName = params.get("AssetName")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Nick = params.get("Nick")
        self.CIDR = params.get("CIDR")
        self.Zone = params.get("Zone")
        self.CVM = params.get("CVM")
        self.AvailableIp = params.get("AvailableIp")
        self.CreateTime = params.get("CreateTime")
        self.ConfigureRisk = params.get("ConfigureRisk")
        self.ScanTask = params.get("ScanTask")
        self.LastScanTime = params.get("LastScanTime")
        self.IsCore = params.get("IsCore")
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
        :param Name: 标签名称
        :type Name: str
        :param Value: 标签内容
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
        


class Vpc(AbstractModel):
    """vpc列表数据

    """

    def __init__(self):
        r"""
        :param Subnet: 子网(只支持32位)
        :type Subnet: int
        :param ConnectedVpc: 互通vpc(只支持32位)
        :type ConnectedVpc: int
        :param AssetId: 资产id
        :type AssetId: str
        :param Region: region区域
        :type Region: str
        :param CVM: 云服务器(只支持32位)
        :type CVM: int
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param DNS: dns域名
注意：此字段可能返回 null，表示取不到有效值。
        :type DNS: list of str
        :param AssetName: 资产名称
        :type AssetName: str
        :param CIDR: cidr网段
        :type CIDR: str
        :param CreateTime: 资产创建时间
        :type CreateTime: str
        :param AppId: appid
        :type AppId: str
        :param Uin: uin
        :type Uin: str
        :param Nick: 昵称
        :type Nick: str
        """
        self.Subnet = None
        self.ConnectedVpc = None
        self.AssetId = None
        self.Region = None
        self.CVM = None
        self.Tag = None
        self.DNS = None
        self.AssetName = None
        self.CIDR = None
        self.CreateTime = None
        self.AppId = None
        self.Uin = None
        self.Nick = None


    def _deserialize(self, params):
        self.Subnet = params.get("Subnet")
        self.ConnectedVpc = params.get("ConnectedVpc")
        self.AssetId = params.get("AssetId")
        self.Region = params.get("Region")
        self.CVM = params.get("CVM")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.DNS = params.get("DNS")
        self.AssetName = params.get("AssetName")
        self.CIDR = params.get("CIDR")
        self.CreateTime = params.get("CreateTime")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.Nick = params.get("Nick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhereFilter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤的项
        :type Name: str
        :param Values: 过滤的值
        :type Values: list of str
        :param OperatorType: 精确匹配填 7 模糊匹配填9 ， 兼容 中台定的结构
        :type OperatorType: int
        """
        self.Name = None
        self.Values = None
        self.OperatorType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.OperatorType = params.get("OperatorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        