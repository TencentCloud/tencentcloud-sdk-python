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


class AccountQuota(AbstractModel):
    """配额详情

    """

    def __init__(self):
        r"""
        :param PostPaidQuotaSet: 后付费配额列表
        :type PostPaidQuotaSet: list of PostPaidQuota
        :param PrePaidQuotaSet: 预付费配额列表
        :type PrePaidQuotaSet: list of PrePaidQuota
        :param SpotPaidQuotaSet: spot配额列表
        :type SpotPaidQuotaSet: list of SpotPaidQuota
        :param ImageQuotaSet: 镜像配额列表
        :type ImageQuotaSet: list of ImageQuota
        :param DisasterRecoverGroupQuotaSet: 置放群组配额列表
        :type DisasterRecoverGroupQuotaSet: list of DisasterRecoverGroupQuota
        """
        self.PostPaidQuotaSet = None
        self.PrePaidQuotaSet = None
        self.SpotPaidQuotaSet = None
        self.ImageQuotaSet = None
        self.DisasterRecoverGroupQuotaSet = None


    def _deserialize(self, params):
        if params.get("PostPaidQuotaSet") is not None:
            self.PostPaidQuotaSet = []
            for item in params.get("PostPaidQuotaSet"):
                obj = PostPaidQuota()
                obj._deserialize(item)
                self.PostPaidQuotaSet.append(obj)
        if params.get("PrePaidQuotaSet") is not None:
            self.PrePaidQuotaSet = []
            for item in params.get("PrePaidQuotaSet"):
                obj = PrePaidQuota()
                obj._deserialize(item)
                self.PrePaidQuotaSet.append(obj)
        if params.get("SpotPaidQuotaSet") is not None:
            self.SpotPaidQuotaSet = []
            for item in params.get("SpotPaidQuotaSet"):
                obj = SpotPaidQuota()
                obj._deserialize(item)
                self.SpotPaidQuotaSet.append(obj)
        if params.get("ImageQuotaSet") is not None:
            self.ImageQuotaSet = []
            for item in params.get("ImageQuotaSet"):
                obj = ImageQuota()
                obj._deserialize(item)
                self.ImageQuotaSet.append(obj)
        if params.get("DisasterRecoverGroupQuotaSet") is not None:
            self.DisasterRecoverGroupQuotaSet = []
            for item in params.get("DisasterRecoverGroupQuotaSet"):
                obj = DisasterRecoverGroupQuota()
                obj._deserialize(item)
                self.DisasterRecoverGroupQuotaSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountQuotaOverview(AbstractModel):
    """配额详情概览

    """

    def __init__(self):
        r"""
        :param Region: 地域
        :type Region: str
        :param AccountQuota: 配额数据
        :type AccountQuota: :class:`tencentcloud.cvm.v20170312.models.AccountQuota`
        """
        self.Region = None
        self.AccountQuota = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("AccountQuota") is not None:
            self.AccountQuota = AccountQuota()
            self.AccountQuota._deserialize(params.get("AccountQuota"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionTimer(AbstractModel):
    """定时任务

    """

    def __init__(self):
        r"""
        :param Externals: 扩展数据
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param TimerAction: 定时器名称，目前仅支持销毁一个值：TerminateInstances。
        :type TimerAction: str
        :param ActionTime: 执行时间，格式形如：2018-5-29 11:26:40,执行时间必须大于当前时间5分钟。
        :type ActionTime: str
        """
        self.Externals = None
        self.TimerAction = None
        self.ActionTime = None


    def _deserialize(self, params):
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.TimerAction = params.get("TimerAction")
        self.ActionTime = params.get("ActionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsRequest(AbstractModel):
    """AllocateHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param ClientToken: 用于保证请求幂等性的字符串。
        :type ClientToken: str
        :param HostChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type HostChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.ChargePrepaid`
        :param HostChargeType: 实例计费类型。目前仅支持：PREPAID（预付费，即包年包月模式），默认为：'PREPAID'。
        :type HostChargeType: str
        :param HostType: CDH实例机型，默认为：'HS1'。
        :type HostType: str
        :param HostCount: 购买CDH实例数量，默认为：1。
        :type HostCount: int
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例。
        :type TagSpecification: list of TagSpecification
        """
        self.Placement = None
        self.ClientToken = None
        self.HostChargePrepaid = None
        self.HostChargeType = None
        self.HostType = None
        self.HostCount = None
        self.TagSpecification = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClientToken = params.get("ClientToken")
        if params.get("HostChargePrepaid") is not None:
            self.HostChargePrepaid = ChargePrepaid()
            self.HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        self.HostChargeType = params.get("HostChargeType")
        self.HostType = params.get("HostType")
        self.HostCount = params.get("HostCount")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsResponse(AbstractModel):
    """AllocateHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param HostIdSet: 新创建云子机的实例id列表。
        :type HostIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HostIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HostIdSet = params.get("HostIdSet")
        self.RequestId = params.get("RequestId")


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID，每次请求批量实例的上限为100。<br>可以通过以下方式获取可用的实例ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询实例ID。<br><li>通过调用接口 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) ，取返回信息中的`InstanceId`获取实例ID。
        :type InstanceIds: list of str
        :param KeyIds: 一个或多个待操作的密钥对ID，每次请求批量密钥对的上限为100。密钥对ID形如：`skey-3glfot13`。<br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的`KeyId`获取密钥对ID。
        :type KeyIds: list of str
        :param ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再绑定密钥。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机。<br><li>FALSE：表示在正常关机失败后不进行强制关机。<br>默认取值：FALSE。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.KeyIds = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.KeyIds = params.get("KeyIds")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateInstancesKeyPairsResponse(AbstractModel):
    """AssociateInstancesKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityGroupIds: 要绑定的`安全组ID`，类似sg-efil73jd，只支持绑定单个安全组。
        :type SecurityGroupIds: list of str
        :param InstanceIds: 被绑定的`实例ID`，类似ins-lesecurk，支持指定多个实例，每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChargePrepaid(AbstractModel):
    """描述预付费模式，即包年包月相关参数。包括购买时长和自动续费逻辑等。

    """

    def __init__(self):
        r"""
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
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
        


class ChcDeployExtraConfig(AbstractModel):
    """chc部署网络minos引导配置。

    """


class ChcHost(AbstractModel):
    """CHC物理服务器信息

    """

    def __init__(self):
        r"""
        :param ChcId: CHC物理服务器ID。
        :type ChcId: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param SerialNumber: 服务器序列号。
        :type SerialNumber: str
        :param InstanceState: CHC的状态<br/>
<ul>
<li>REGISTERED: 设备已录入。还未配置带外和部署网络</li>
<li>VPC_READY: 已配置带外和部署网络</li>
<li>PREPARED: 可分配云主机</li>
<li>ONLINE: 已分配云主机</li>
</ul>
        :type InstanceState: str
        :param DeviceType: 设备类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param Placement: 所属可用区
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param BmcVirtualPrivateCloud: 带外网络。
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param BmcIp: 带外网络Ip。
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcIp: str
        :param BmcSecurityGroupIds: 带外网络安全组Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcSecurityGroupIds: list of str
        :param DeployVirtualPrivateCloud: 部署网络。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param DeployIp: 部署网络Ip。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployIp: str
        :param DeploySecurityGroupIds: 部署网络安全组Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploySecurityGroupIds: list of str
        :param CvmInstanceId: 关联的云主机Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceId: str
        :param CreatedTime: 服务器导入的时间。
        :type CreatedTime: str
        :param HardwareDescription: 机型的硬件描述，分别为CPU核数，内存容量和磁盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareDescription: str
        :param CPU: CHC物理服务器的CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: int
        :param Memory: CHC物理服务器的内存大小，单位为GB
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param Disk: CHC物理服务器的磁盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Disk: str
        :param BmcMAC: 带外网络下分配的MAC地址
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcMAC: str
        :param DeployMAC: 部署网络下分配的MAC地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMAC: str
        :param TenantType: 设备托管类型。
HOSTING: 托管
TENANT: 租赁
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantType: str
        :param DeployExtraConfig: chc dhcp选项，用于minios调试
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployExtraConfig: :class:`tencentcloud.cvm.v20170312.models.ChcDeployExtraConfig`
        """
        self.ChcId = None
        self.InstanceName = None
        self.SerialNumber = None
        self.InstanceState = None
        self.DeviceType = None
        self.Placement = None
        self.BmcVirtualPrivateCloud = None
        self.BmcIp = None
        self.BmcSecurityGroupIds = None
        self.DeployVirtualPrivateCloud = None
        self.DeployIp = None
        self.DeploySecurityGroupIds = None
        self.CvmInstanceId = None
        self.CreatedTime = None
        self.HardwareDescription = None
        self.CPU = None
        self.Memory = None
        self.Disk = None
        self.BmcMAC = None
        self.DeployMAC = None
        self.TenantType = None
        self.DeployExtraConfig = None


    def _deserialize(self, params):
        self.ChcId = params.get("ChcId")
        self.InstanceName = params.get("InstanceName")
        self.SerialNumber = params.get("SerialNumber")
        self.InstanceState = params.get("InstanceState")
        self.DeviceType = params.get("DeviceType")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("BmcVirtualPrivateCloud") is not None:
            self.BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self.BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self.BmcIp = params.get("BmcIp")
        self.BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self.DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self.DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self.DeployIp = params.get("DeployIp")
        self.DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.CreatedTime = params.get("CreatedTime")
        self.HardwareDescription = params.get("HardwareDescription")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.Disk = params.get("Disk")
        self.BmcMAC = params.get("BmcMAC")
        self.DeployMAC = params.get("DeployMAC")
        self.TenantType = params.get("TenantType")
        if params.get("DeployExtraConfig") is not None:
            self.DeployExtraConfig = ChcDeployExtraConfig()
            self.DeployExtraConfig._deserialize(params.get("DeployExtraConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChcHostDeniedActions(AbstractModel):
    """CHC物理服务器实例禁止操作的返回结构体

    """

    def __init__(self):
        r"""
        :param ChcId: CHC物理服务器的实例id
        :type ChcId: str
        :param State: CHC物理服务器的状态
        :type State: str
        :param DenyActions: 当前CHC物理服务器禁止做的操作
        :type DenyActions: list of str
        """
        self.ChcId = None
        self.State = None
        self.DenyActions = None


    def _deserialize(self, params):
        self.ChcId = params.get("ChcId")
        self.State = params.get("State")
        self.DenyActions = params.get("DenyActions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcRequest(AbstractModel):
    """ConfigureChcAssistVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC物理服务器的实例Id。
        :type ChcIds: list of str
        :param BmcVirtualPrivateCloud: 带外网络信息。
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param BmcSecurityGroupIds: 带外网络的安全组列表
        :type BmcSecurityGroupIds: list of str
        :param DeployVirtualPrivateCloud: 部署网络信息。
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param DeploySecurityGroupIds: 部署网络的安全组列表
        :type DeploySecurityGroupIds: list of str
        """
        self.ChcIds = None
        self.BmcVirtualPrivateCloud = None
        self.BmcSecurityGroupIds = None
        self.DeployVirtualPrivateCloud = None
        self.DeploySecurityGroupIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        if params.get("BmcVirtualPrivateCloud") is not None:
            self.BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self.BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self.BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self.DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self.DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self.DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcResponse(AbstractModel):
    """ConfigureChcAssistVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConfigureChcDeployVpcRequest(AbstractModel):
    """ConfigureChcDeployVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC物理服务器的实例Id。
        :type ChcIds: list of str
        :param DeployVirtualPrivateCloud: 部署网络信息。
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param DeploySecurityGroupIds: 部署网络的安全组列表。
        :type DeploySecurityGroupIds: list of str
        """
        self.ChcIds = None
        self.DeployVirtualPrivateCloud = None
        self.DeploySecurityGroupIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self.DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self.DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self.DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcDeployVpcResponse(AbstractModel):
    """ConfigureChcDeployVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDisasterRecoverGroupRequest(AbstractModel):
    """CreateDisasterRecoverGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 分散置放群组名称，长度1-60个字符，支持中、英文。
        :type Name: str
        :param Type: 分散置放群组类型，取值范围：<br><li>HOST：物理机<br><li>SW：交换机<br><li>RACK：机架
        :type Type: str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        """
        self.Name = None
        self.Type = None
        self.ClientToken = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoverGroupResponse(AbstractModel):
    """CreateDisasterRecoverGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupId: 分散置放群组ID列表。
        :type DisasterRecoverGroupId: str
        :param Type: 分散置放群组类型，取值范围：<br><li>HOST：物理机<br><li>SW：交换机<br><li>RACK：机架
        :type Type: str
        :param Name: 分散置放群组名称，长度1-60个字符，支持中、英文。
        :type Name: str
        :param CvmQuotaTotal: 置放群组内可容纳的云服务器数量。
        :type CvmQuotaTotal: int
        :param CurrentNum: 置放群组内已有的云服务器数量。
        :type CurrentNum: int
        :param CreateTime: 置放群组创建时间。
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DisasterRecoverGroupId = None
        self.Type = None
        self.Name = None
        self.CvmQuotaTotal = None
        self.CurrentNum = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.CvmQuotaTotal = params.get("CvmQuotaTotal")
        self.CurrentNum = params.get("CurrentNum")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageName: 镜像名称
        :type ImageName: str
        :param InstanceId: 需要制作镜像的实例ID。基于实例创建镜像时，为必填参数。
        :type InstanceId: str
        :param ImageDescription: 镜像描述
        :type ImageDescription: str
        :param ForcePoweroff: 是否执行强制关机以制作镜像。
取值范围：<br><li>TRUE：表示关机之后制作镜像<br><li>FALSE：表示开机状态制作镜像<br><br>默认取值：FALSE。<br><br>开机状态制作镜像，可能导致部分数据未备份，影响数据安全。
        :type ForcePoweroff: str
        :param Sysprep: 创建Windows镜像时是否启用Sysprep。
取值范围：TRUE或FALSE，默认取值为FALSE。

关于Sysprep的详情请参考[链接](https://cloud.tencent.com/document/product/213/43498)。
        :type Sysprep: str
        :param DataDiskIds: 基于实例创建整机镜像时，指定包含在镜像里的数据盘Id
        :type DataDiskIds: list of str
        :param SnapshotIds: 基于快照创建镜像，指定快照ID，必须包含一个系统盘快照。不可与InstanceId同时传入。
        :type SnapshotIds: list of str
        :param DryRun: 检测本次请求的是否成功，但不会对操作的资源产生任何影响
        :type DryRun: bool
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到自定义镜像。
        :type TagSpecification: list of TagSpecification
        """
        self.ImageName = None
        self.InstanceId = None
        self.ImageDescription = None
        self.ForcePoweroff = None
        self.Sysprep = None
        self.DataDiskIds = None
        self.SnapshotIds = None
        self.DryRun = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.ImageName = params.get("ImageName")
        self.InstanceId = params.get("InstanceId")
        self.ImageDescription = params.get("ImageDescription")
        self.ForcePoweroff = params.get("ForcePoweroff")
        self.Sysprep = params.get("Sysprep")
        self.DataDiskIds = params.get("DataDiskIds")
        self.SnapshotIds = params.get("SnapshotIds")
        self.DryRun = params.get("DryRun")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :type KeyName: str
        :param ProjectId: 密钥对创建后所属的项目ID。
可以通过以下方式获取项目ID：
<li>通过项目列表查询项目ID。
<li>通过调用接口DescribeProject，取返回信息中的`projectId `获取项目ID。
        :type ProjectId: int
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到密钥对。
        :type TagSpecification: list of TagSpecification
        """
        self.KeyName = None
        self.ProjectId = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param KeyPair: 密钥对信息。
        :type KeyPair: :class:`tencentcloud.cvm.v20170312.models.KeyPair`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyPair = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self.KeyPair = KeyPair()
            self.KeyPair._deserialize(params.get("KeyPair"))
        self.RequestId = params.get("RequestId")


class CreateLaunchTemplateRequest(AbstractModel):
    """CreateLaunchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateName: 实例启动模板名称。长度为2~128个英文或中文字符。
        :type LaunchTemplateName: str
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，传入InstanceType获取当前机型支持的镜像列表，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param LaunchTemplateVersionDescription: 实例启动模板版本描述。长度为2~256个英文或中文字符。
        :type LaunchTemplateVersionDescription: str
        :param InstanceType: 实例机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则系统将根据当前地域的资源售卖情况动态指定默认机型。<br><li>对于付费模式为CDHPAID的实例创建，该参数以"CDH_"为前缀，根据CPU和内存配置生成，具体形式为：CDH_XCXG，例如对于创建CPU为1核，内存为1G大小的专用宿主机的实例，该参数应该为CDH_1C1G。
        :type InstanceType: str
        :param SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，即表示每个实例的主网卡IP；同时，InstanceCount参数必须与私有网络IP的个数一致且不能大于20。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: 购买实例数量。包年包月实例取值范围：[1，300]，按量计费实例取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。
        :type InstanceName: str
        :param LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param HostName: 云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。
        :type HostName: str
        :param ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。
        :type UserData: str
        :param DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param CamRoleName: CAM角色名称。可通过[`DescribeRoleList`](https://cloud.tencent.com/document/product/598/13887)接口返回值中的`roleName`获取。
        :type CamRoleName: str
        :param HpcClusterId: 高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :type HpcClusterId: str
        :param InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDHPAID：独享子机（基于专用宿主机创建，宿主机部分的资源不收费）<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>TRUE：表示开启实例保护，不允许通过api接口删除实例<br><li>FALSE：表示关闭实例保护，允许通过api接口删除实例<br><br>默认取值：FALSE。
        :type DisableApiTermination: bool
        """
        self.LaunchTemplateName = None
        self.Placement = None
        self.ImageId = None
        self.LaunchTemplateVersionDescription = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.ActionTimer = None
        self.DisasterRecoverGroupIds = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.UserData = None
        self.DryRun = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.DisableApiTermination = None


    def _deserialize(self, params):
        self.LaunchTemplateName = params.get("LaunchTemplateName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ImageId = params.get("ImageId")
        self.LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.UserData = params.get("UserData")
        self.DryRun = params.get("DryRun")
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchTemplateResponse(AbstractModel):
    """CreateLaunchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: 当通过本接口来创建实例启动模板时会返回该参数，表示创建成功的实例启动模板`ID`。
        :type LaunchTemplateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LaunchTemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.RequestId = params.get("RequestId")


class CreateLaunchTemplateVersionRequest(AbstractModel):
    """CreateLaunchTemplateVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param LaunchTemplateId: 启动模板ID，新版本将基于该实例启动模板ID创建。
        :type LaunchTemplateId: str
        :param LaunchTemplateVersion: 若给定，新实例启动模板将基于给定的版本号创建。若未指定则使用默认版本。
        :type LaunchTemplateVersion: int
        :param LaunchTemplateVersionDescription: 实例启动模板版本描述。长度为2~256个英文或中文字符。
        :type LaunchTemplateVersionDescription: str
        :param InstanceType: 实例机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则系统将根据当前地域的资源售卖情况动态指定默认机型。<br><li>对于付费模式为CDHPAID的实例创建，该参数以"CDH_"为前缀，根据CPU和内存配置生成，具体形式为：CDH_XCXG，例如对于创建CPU为1核，内存为1G大小的专用宿主机的实例，该参数应该为CDH_1C1G。
        :type InstanceType: str
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，传入InstanceType获取当前机型支持的镜像列表，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，即表示每个实例的主网卡IP；同时，InstanceCount参数必须与私有网络IP的个数一致且不能大于20。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: 购买实例数量。包年包月实例取值范围：[1，300]，按量计费实例取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。
        :type InstanceName: str
        :param LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param HostName: 云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。
        :type HostName: str
        :param ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。
        :type UserData: str
        :param DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param CamRoleName: CAM角色名称。可通过[`DescribeRoleList`](https://cloud.tencent.com/document/product/598/13887)接口返回值中的`roleName`获取。
        :type CamRoleName: str
        :param HpcClusterId: 高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :type HpcClusterId: str
        :param InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDHPAID：独享子机（基于专用宿主机创建，宿主机部分的资源不收费）<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>TRUE：表示开启实例保护，不允许通过api接口删除实例<br><li>FALSE：表示关闭实例保护，允许通过api接口删除实例<br><br>默认取值：FALSE。
        :type DisableApiTermination: bool
        """
        self.Placement = None
        self.LaunchTemplateId = None
        self.LaunchTemplateVersion = None
        self.LaunchTemplateVersionDescription = None
        self.InstanceType = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.ActionTimer = None
        self.DisasterRecoverGroupIds = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.UserData = None
        self.DryRun = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.DisableApiTermination = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        self.LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self.InstanceType = params.get("InstanceType")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.UserData = params.get("UserData")
        self.DryRun = params.get("DryRun")
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchTemplateVersionResponse(AbstractModel):
    """CreateLaunchTemplateVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateVersionNumber: 新创建的实例启动模板版本号。
        :type LaunchTemplateVersionNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LaunchTemplateVersionNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchTemplateVersionNumber = params.get("LaunchTemplateVersionNumber")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        r"""
        :param DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param DiskType: 数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br><li>LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><li>CLOUD_BSSD：通用型SSD云硬盘<br><br>默认取值：LOCAL_BASIC。<br><br>该参数对`ResizeInstanceDisk`接口无效。
        :type DiskType: str
        :param DiskId: 数据盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID，暂时不支持该参数。
该参数目前仅用于`DescribeInstances`等查询类接口的返回参数，不可用于`RunInstances`等写接口的入参。
        :type DiskId: str
        :param DeleteWithInstance: 数据盘是否随子机销毁。取值范围：
<li>TRUE：子机销毁时，销毁数据盘，只支持按小时后付费云盘
<li>FALSE：子机销毁时，保留数据盘<br>
默认取值：TRUE<br>
该参数目前仅用于 `RunInstances` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param SnapshotId: 数据盘快照ID。选择的数据盘快照大小需小于数据盘大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param Encrypt: 数据盘是加密。取值范围：
<li>TRUE：加密
<li>FALSE：不加密<br>
默认取值：FALSE<br>
该参数目前仅用于 `RunInstances` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: bool
        :param KmsKeyId: 自定义CMK对应的ID，取值为UUID或者类似kms-abcd1234。用于加密云盘。

该参数目前仅用于 `RunInstances` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyId: str
        :param ThroughputPerformance: 云硬盘性能，单位：MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        :param CdcId: 所属的独享集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskId = None
        self.DeleteWithInstance = None
        self.SnapshotId = None
        self.Encrypt = None
        self.KmsKeyId = None
        self.ThroughputPerformance = None
        self.CdcId = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.SnapshotId = params.get("SnapshotId")
        self.Encrypt = params.get("Encrypt")
        self.KmsKeyId = params.get("KmsKeyId")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsRequest(AbstractModel):
    """DeleteDisasterRecoverGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupIds: 分散置放群组ID列表，可通过[DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810)接口获取。每次请求允许操作的分散置放群组数量上限是100。
        :type DisasterRecoverGroupIds: list of str
        """
        self.DisasterRecoverGroupIds = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsResponse(AbstractModel):
    """DeleteDisasterRecoverGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImagesRequest(AbstractModel):
    """DeleteImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageIds: 准备删除的镜像Id列表
        :type ImageIds: list of str
        :param DeleteBindedSnap: 是否删除镜像关联的快照
        :type DeleteBindedSnap: bool
        :param DryRun: 检测是否支持删除镜像
        :type DryRun: bool
        """
        self.ImageIds = None
        self.DeleteBindedSnap = None
        self.DryRun = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        self.DeleteBindedSnap = params.get("DeleteBindedSnap")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagesResponse(AbstractModel):
    """DeleteImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteKeyPairsRequest(AbstractModel):
    """DeleteKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyIds: 一个或多个待操作的密钥对ID。每次请求批量密钥对的上限为100。<br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的 `KeyId` 获取密钥对ID。
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKeyPairsResponse(AbstractModel):
    """DeleteKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLaunchTemplateRequest(AbstractModel):
    """DeleteLaunchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        """
        self.LaunchTemplateId = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateResponse(AbstractModel):
    """DeleteLaunchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLaunchTemplateVersionsRequest(AbstractModel):
    """DeleteLaunchTemplateVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        :param LaunchTemplateVersions: 实例启动模板版本列表。
        :type LaunchTemplateVersions: list of int
        """
        self.LaunchTemplateId = None
        self.LaunchTemplateVersions = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateVersionsResponse(AbstractModel):
    """DeleteLaunchTemplateVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountQuotaRequest(AbstractModel):
    """DescribeAccountQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>quota-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>配额类型</strong>】进行过滤。配额类型形如：PostPaidQuotaSet。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：PostPaidQuotaSet,DisasterRecoverGroupQuotaSet,PrePaidQuotaSet,SpotPaidQuotaSet</p>
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountQuotaResponse(AbstractModel):
    """DescribeAccountQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppId: 用户appid
        :type AppId: str
        :param AccountQuotaOverview: 配额数据
        :type AccountQuotaOverview: :class:`tencentcloud.cvm.v20170312.models.AccountQuotaOverview`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.AccountQuotaOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        if params.get("AccountQuotaOverview") is not None:
            self.AccountQuotaOverview = AccountQuotaOverview()
            self.AccountQuotaOverview._deserialize(params.get("AccountQuotaOverview"))
        self.RequestId = params.get("RequestId")


class DescribeChcDeniedActionsRequest(AbstractModel):
    """DescribeChcDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC物理服务器实例id
        :type ChcIds: list of str
        """
        self.ChcIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChcDeniedActionsResponse(AbstractModel):
    """DescribeChcDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param ChcHostDeniedActionSet: CHC实例禁止操作信息
        :type ChcHostDeniedActionSet: list of ChcHostDeniedActions
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ChcHostDeniedActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ChcHostDeniedActionSet") is not None:
            self.ChcHostDeniedActionSet = []
            for item in params.get("ChcHostDeniedActionSet"):
                obj = ChcHostDeniedActions()
                obj._deserialize(item)
                self.ChcHostDeniedActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeChcHostsRequest(AbstractModel):
    """DescribeChcHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC物理服务器实例ID。每次请求的实例的上限为100。参数不支持同时指定`ChcIds`和`Filters`。
        :type ChcIds: list of str
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>instance-name</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例名称</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-state</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例状态</strong>】进行过滤。状态类型详见[实例状态表](https://cloud.tencent.com/document/api/213/15753#InstanceStatus)</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>device-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>设备类型</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>vpc-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>私有网络唯一ID</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>subnet-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>私有子网唯一ID</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ChcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChcHostsResponse(AbstractModel):
    """DescribeChcHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param ChcHostSet: 返回的实例列表
        :type ChcHostSet: list of ChcHost
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ChcHostSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ChcHostSet") is not None:
            self.ChcHostSet = []
            for item in params.get("ChcHostSet"):
                obj = ChcHost()
                obj._deserialize(item)
                self.ChcHostSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupQuotaRequest(AbstractModel):
    """DescribeDisasterRecoverGroupQuota请求参数结构体

    """


class DescribeDisasterRecoverGroupQuotaResponse(AbstractModel):
    """DescribeDisasterRecoverGroupQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupQuota: 可创建置放群组数量的上限。
        :type GroupQuota: int
        :param CurrentNum: 当前用户已经创建的置放群组数量。
        :type CurrentNum: int
        :param CvmInHostGroupQuota: 物理机类型容灾组内实例的配额数。
        :type CvmInHostGroupQuota: int
        :param CvmInSwGroupQuota: 交换机类型容灾组内实例的配额数。
        :type CvmInSwGroupQuota: int
        :param CvmInRackGroupQuota: 机架类型容灾组内实例的配额数。
        :type CvmInRackGroupQuota: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupQuota = None
        self.CurrentNum = None
        self.CvmInHostGroupQuota = None
        self.CvmInSwGroupQuota = None
        self.CvmInRackGroupQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupQuota = params.get("GroupQuota")
        self.CurrentNum = params.get("CurrentNum")
        self.CvmInHostGroupQuota = params.get("CvmInHostGroupQuota")
        self.CvmInSwGroupQuota = params.get("CvmInSwGroupQuota")
        self.CvmInRackGroupQuota = params.get("CvmInRackGroupQuota")
        self.RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupsRequest(AbstractModel):
    """DescribeDisasterRecoverGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupIds: 分散置放群组ID列表。每次请求允许操作的分散置放群组数量上限是100。
        :type DisasterRecoverGroupIds: list of str
        :param Name: 分散置放群组名称，支持模糊匹配。
        :type Name: str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.DisasterRecoverGroupIds = None
        self.Name = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoverGroupsResponse(AbstractModel):
    """DescribeDisasterRecoverGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupSet: 分散置放群组信息列表。
        :type DisasterRecoverGroupSet: list of DisasterRecoverGroup
        :param TotalCount: 用户置放群组总量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DisasterRecoverGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DisasterRecoverGroupSet") is not None:
            self.DisasterRecoverGroupSet = []
            for item in params.get("DisasterRecoverGroupSet"):
                obj = DisasterRecoverGroup()
                obj._deserialize(item)
                self.DisasterRecoverGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostsRequest(AbstractModel):
    """DescribeHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>project-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>项目ID</strong>】进行过滤，可通过调用[DescribeProject](https://cloud.tencent.com/document/api/378/4400)查询已创建的项目列表或登录[控制台](https://console.cloud.tencent.com/cvm/index)进行查看；也可以调用[AddProject](https://cloud.tencent.com/document/api/378/4398)创建新的项目。项目ID形如：1002189。</p><p style="padding-left: 30px;">类型：Integer</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>host-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>[CDH](https://cloud.tencent.com/document/product/416) ID</strong>】进行过滤。[CDH](https://cloud.tencent.com/document/product/416) ID形如：host-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>host-name</strong></li>
<p style="padding-left: 30px;">按照【<strong>CDH实例名称</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>host-state</strong></li>
<p style="padding-left: 30px;">按照【<strong>CDH实例状态</strong>】进行过滤。（PENDING：创建中 | LAUNCH_FAILURE：创建失败 | RUNNING：运行中 | EXPIRED：已过期）</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsResponse(AbstractModel):
    """DescribeHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的cdh实例总数
        :type TotalCount: int
        :param HostSet: cdh实例详细信息列表
        :type HostSet: list of HostItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HostSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HostSet") is not None:
            self.HostSet = []
            for item in params.get("HostSet"):
                obj = HostItem()
                obj._deserialize(item)
                self.HostSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageQuotaRequest(AbstractModel):
    """DescribeImageQuota请求参数结构体

    """


class DescribeImageQuotaResponse(AbstractModel):
    """DescribeImageQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageNumQuota: 账户的镜像配额
        :type ImageNumQuota: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageNumQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageNumQuota = params.get("ImageNumQuota")
        self.RequestId = params.get("RequestId")


class DescribeImageSharePermissionRequest(AbstractModel):
    """DescribeImageSharePermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageId: 需要共享的镜像Id
        :type ImageId: str
        """
        self.ImageId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSharePermissionResponse(AbstractModel):
    """DescribeImageSharePermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param SharePermissionSet: 镜像共享信息
        :type SharePermissionSet: list of SharePermission
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SharePermissionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self.SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self.SharePermissionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageIds: 镜像ID列表 。镜像ID如：`img-gvbnzy6f`。array型参数的格式可以参考[API简介](https://cloud.tencent.com/document/api/213/15688)。镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。
        :type ImageIds: list of str
        :param Filters: 过滤条件，每次请求的`Filters`的上限为10，`Filters.Values`的上限为5。参数不可以同时指定`ImageIds`和`Filters`。详细的过滤条件如下：

<li><strong>image-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>镜像ID</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>image-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>镜像类型</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：</p><p style="padding-left: 30px;">PRIVATE_IMAGE: 私有镜像 (本账户创建的镜像)</p><p style="padding-left: 30px;">PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)</p><p style="padding-left: 30px;">SHARED_IMAGE: 共享镜像(其他账户共享给本账户的镜像)</p>
<li><strong>image-name</strong></li>
<p style="padding-left: 30px;">按照【<strong>镜像名称</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>platform</strong></li>
<p style="padding-left: 30px;">按照【<strong>镜像平台</strong>】进行过滤，如CentOS。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>tag-key</strong></li>
<p style="padding-left: 30px;">按照【<strong>标签键</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>tag-value</strong></li>
<p style="padding-left: 30px;">按照【<strong>标签值</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>tag:tag-key</strong></li>
<p style="padding-left: 30px;">按照【<strong>标签键值对</strong>】进行过滤。tag-key使用具体的标签键进行替换。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于Offset详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。
        :type Offset: int
        :param Limit: 数量限制，默认为20，最大值为100。关于Limit详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。
        :type Limit: int
        :param InstanceType: 实例类型，如 `S1.SMALL1`
        :type InstanceType: str
        """
        self.ImageIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceType = params.get("InstanceType")
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
        :param ImageSet: 一个关于镜像详细信息的结构体，主要包括镜像的主要状态与属性。
        :type ImageSet: list of Image
        :param TotalCount: 符合要求的镜像数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageSet") is not None:
            self.ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self.ImageSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs请求参数结构体

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImportImageOsListSupported: 支持的导入镜像的操作系统类型。
        :type ImportImageOsListSupported: :class:`tencentcloud.cvm.v20170312.models.ImageOsList`
        :param ImportImageOsVersionSet: 支持的导入镜像的操作系统版本。
        :type ImportImageOsVersionSet: list of OsVersion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImportImageOsListSupported = None
        self.ImportImageOsVersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self.ImportImageOsListSupported = ImageOsList()
            self.ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self.ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self.ImportImageOsVersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceFamilyConfigsRequest(AbstractModel):
    """DescribeInstanceFamilyConfigs请求参数结构体

    """


class DescribeInstanceFamilyConfigsResponse(AbstractModel):
    """DescribeInstanceFamilyConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceFamilyConfigSet: 实例机型组配置的列表信息
        :type InstanceFamilyConfigSet: list of InstanceFamilyConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceFamilyConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfigSet") is not None:
            self.InstanceFamilyConfigSet = []
            for item in params.get("InstanceFamilyConfigSet"):
                obj = InstanceFamilyConfig()
                obj._deserialize(item)
                self.InstanceFamilyConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceInternetBandwidthConfigsRequest(AbstractModel):
    """DescribeInstanceInternetBandwidthConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceInternetBandwidthConfigsResponse(AbstractModel):
    """DescribeInstanceInternetBandwidthConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param InternetBandwidthConfigSet: 带宽配置信息列表。
        :type InternetBandwidthConfigSet: list of InternetBandwidthConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InternetBandwidthConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InternetBandwidthConfigSet") is not None:
            self.InternetBandwidthConfigSet = []
            for item in params.get("InternetBandwidthConfigSet"):
                obj = InternetBandwidthConfig()
                obj._deserialize(item)
                self.InternetBandwidthConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigsRequest(AbstractModel):
    """DescribeInstanceTypeConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>instance-family</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例机型系列</strong>】进行过滤。实例机型系列形如：S1、I1、M1等。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为1。
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTypeConfigsResponse(AbstractModel):
    """DescribeInstanceTypeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceTypeConfigSet: 实例机型配置列表。
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 一个操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceVncUrl: 实例的管理终端地址。
        :type InstanceVncUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceVncUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceVncUrl = params.get("InstanceVncUrl")
        self.RequestId = params.get("RequestId")


class DescribeInstancesModificationRequest(AbstractModel):
    """DescribeInstancesModification请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待查询的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为20。
        :type InstanceIds: list of str
        :param Filters: <li><strong>status</strong></li>
<p style="padding-left: 30px;">按照【<strong>配置规格状态</strong>】进行过滤。配置规格状态形如：SELL、UNAVAILABLE。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为2。
        :type Filters: list of Filter
        """
        self.InstanceIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesModificationResponse(AbstractModel):
    """DescribeInstancesModification返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例调整的机型配置的数量。
        :type TotalCount: int
        :param InstanceTypeConfigStatusSet: 实例支持调整的机型配置列表。
        :type InstanceTypeConfigStatusSet: list of InstanceTypeConfigStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceTypeConfigStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceTypeConfigStatusSet") is not None:
            self.InstanceTypeConfigStatusSet = []
            for item in params.get("InstanceTypeConfigStatusSet"):
                obj = InstanceTypeConfigStatus()
                obj._deserialize(item)
                self.InstanceTypeConfigStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesOperationLimitRequest(AbstractModel):
    """DescribeInstancesOperationLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 按照一个或者多个实例ID查询，可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)API返回值中的InstanceId获取。实例ID形如：ins-xxxxxxxx。（此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的ids.N一节）。每次请求的实例的上限为100。
        :type InstanceIds: list of str
        :param Operation: 实例操作。
<li> INSTANCE_DEGRADE：实例降配操作</li>
        :type Operation: str
        """
        self.InstanceIds = None
        self.Operation = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesOperationLimitResponse(AbstractModel):
    """DescribeInstancesOperationLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceOperationLimitSet: 该参数表示调整配置操作（降配）限制次数查询。
        :type InstanceOperationLimitSet: list of OperationCountLimit
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceOperationLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceOperationLimitSet") is not None:
            self.InstanceOperationLimitSet = []
            for item in params.get("InstanceOperationLimitSet"):
                obj = OperationCountLimit()
                obj._deserialize(item)
                self.InstanceOperationLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：`ins-xxxxxxxx`。（此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的`ids.N`一节）。每次请求的实例的上限为100。参数不支持同时指定`InstanceIds`和`Filters`。
        :type InstanceIds: list of str
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>project-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>项目ID</strong>】进行过滤，可通过调用[DescribeProject](https://cloud.tencent.com/document/api/378/4400)查询已创建的项目列表或登录[控制台](https://console.cloud.tencent.com/cvm/index)进行查看；也可以调用[AddProject](https://cloud.tencent.com/document/api/378/4398)创建新的项目。项目ID形如：1002189。</p><p style="padding-left: 30px;">类型：Integer</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>host-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>[CDH](https://cloud.tencent.com/document/product/416) ID</strong>】进行过滤。[CDH](https://cloud.tencent.com/document/product/416) ID形如：host-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>dedicated-cluster-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>[CDC](https://cloud.tencent.com/document/product/1346) ID</strong>】进行过滤。[CDC](https://cloud.tencent.com/document/product/1346) ID形如：cluster-xxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>vpc-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>VPC ID</strong>】进行过滤。VPC ID形如：vpc-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>subnet-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>子网ID</strong>】进行过滤。子网ID形如：subnet-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例ID</strong>】进行过滤。实例ID形如：ins-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>uuid</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例UUID</strong>】进行过滤。实例UUID形如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>security-group-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>安全组ID</strong>】进行过滤。安全组ID形如: sg-8jlk3f3r。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-name</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例名称</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-charge-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例计费模式</strong>】进行过滤。(PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费 | CDHPAID：表示[CDH](https://cloud.tencent.com/document/product/416)付费，即只对[CDH](https://cloud.tencent.com/document/product/416)计费，不对[CDH](https://cloud.tencent.com/document/product/416)上的实例计费。)</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-state</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例状态</strong>】进行过滤。状态类型详见[实例状态表](https://cloud.tencent.com/document/api/213/15753#InstanceStatus)</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>private-ip-address</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例主网卡的内网IP</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>public-ip-address</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例主网卡的公网IP</strong>】进行过滤，包含实例创建时自动分配的IP和实例创建后手动绑定的弹性IP。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>ipv6-address</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例的IPv6地址</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>tag-key</strong></li>
<p style="padding-left: 30px;">按照【<strong>标签键</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>tag-value</strong></li>
<p style="padding-left: 30px;">按照【<strong>标签值</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>tag:tag-key</strong></li>
<p style="padding-left: 30px;">按照【<strong>标签键值对</strong>】进行过滤。tag-key使用具体的标签键进行替换。使用请参考示例2。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`InstanceIds`和`Filters`。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param InstanceSet: 实例详细信息列表。
        :type InstanceSet: list of Instance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesStatusRequest(AbstractModel):
    """DescribeInstancesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：`ins-11112222`。此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的`ids.N`一节）。每次请求的实例的上限为100。
        :type InstanceIds: list of str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesStatusResponse(AbstractModel):
    """DescribeInstancesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的实例状态数量。
        :type TotalCount: int
        :param InstanceStatusSet: [实例状态](https://cloud.tencent.com/document/api/213/15753#InstanceStatus) 列表。
        :type InstanceStatusSet: list of InstanceStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceStatusSet") is not None:
            self.InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = InstanceStatus()
                obj._deserialize(item)
                self.InstanceStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternetChargeTypeConfigsRequest(AbstractModel):
    """DescribeInternetChargeTypeConfigs请求参数结构体

    """


class DescribeInternetChargeTypeConfigsResponse(AbstractModel):
    """DescribeInternetChargeTypeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param InternetChargeTypeConfigSet: 网络计费类型配置。
        :type InternetChargeTypeConfigSet: list of InternetChargeTypeConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InternetChargeTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InternetChargeTypeConfigSet") is not None:
            self.InternetChargeTypeConfigSet = []
            for item in params.get("InternetChargeTypeConfigSet"):
                obj = InternetChargeTypeConfig()
                obj._deserialize(item)
                self.InternetChargeTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyIds: 密钥对ID，密钥对ID形如：`skey-11112222`（此接口支持同时传入多个ID进行过滤。此参数的具体格式可参考 API [简介](https://cloud.tencent.com/document/api/213/15688)的 `id.N` 一节）。参数不支持同时指定 `KeyIds` 和 `Filters`。密钥对ID可以通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询。
        :type KeyIds: list of str
        :param Filters: 过滤条件。
<li> project-id - Integer - 是否必填：否 -（过滤条件）按照项目ID过滤。可以通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID，或者调用接口 [DescribeProject](https://cloud.tencent.com/document/api/378/4400)，取返回信息中的projectId获取项目ID。</li>
<li> key-name - String - 是否必填：否 -（过滤条件）按照密钥对名称过滤。</li>
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键过滤。</li>
<li> tag-value - String - 是否必填：否 -（过滤条件）按照标签值过滤。</li>
<li> tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对过滤。tag-key使用具体的标签键进行替换。</li>
参数不支持同时指定 `KeyIds` 和 `Filters`。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.KeyIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeyPairsResponse(AbstractModel):
    """DescribeKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的密钥对数量。
        :type TotalCount: int
        :param KeyPairSet: 密钥对详细信息列表。
        :type KeyPairSet: list of KeyPair
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.KeyPairSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyPairSet") is not None:
            self.KeyPairSet = []
            for item in params.get("KeyPairSet"):
                obj = KeyPair()
                obj._deserialize(item)
                self.KeyPairSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLaunchTemplateVersionsRequest(AbstractModel):
    """DescribeLaunchTemplateVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        :param LaunchTemplateVersions: 实例启动模板列表。
        :type LaunchTemplateVersions: list of int non-negative
        :param MinVersion: 通过范围指定版本时的最小版本号，默认为0。
        :type MinVersion: int
        :param MaxVersion: 过范围指定版本时的最大版本号，默认为30。
        :type MaxVersion: int
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param DefaultVersion: 是否查询默认版本。该参数不可与LaunchTemplateVersions同时指定。
        :type DefaultVersion: bool
        """
        self.LaunchTemplateId = None
        self.LaunchTemplateVersions = None
        self.MinVersion = None
        self.MaxVersion = None
        self.Offset = None
        self.Limit = None
        self.DefaultVersion = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        self.MinVersion = params.get("MinVersion")
        self.MaxVersion = params.get("MaxVersion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaunchTemplateVersionsResponse(AbstractModel):
    """DescribeLaunchTemplateVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例启动模板总数。
        :type TotalCount: int
        :param LaunchTemplateVersionSet: 实例启动模板版本集合。
        :type LaunchTemplateVersionSet: list of LaunchTemplateVersionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LaunchTemplateVersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateVersionSet") is not None:
            self.LaunchTemplateVersionSet = []
            for item in params.get("LaunchTemplateVersionSet"):
                obj = LaunchTemplateVersionInfo()
                obj._deserialize(item)
                self.LaunchTemplateVersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLaunchTemplatesRequest(AbstractModel):
    """DescribeLaunchTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateIds: 启动模板ID，一个或者多个启动模板ID。若未指定，则显示用户所有模板。
        :type LaunchTemplateIds: list of str
        :param Filters: <p style="padding-left: 30px;">按照【<strong>LaunchTemplateName</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`LaunchTemplateIds`和`Filters`。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.LaunchTemplateIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.LaunchTemplateIds = params.get("LaunchTemplateIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaunchTemplatesResponse(AbstractModel):
    """DescribeLaunchTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的实例模板数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param LaunchTemplateSet: 实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateSet: list of LaunchTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LaunchTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateSet") is not None:
            self.LaunchTemplateSet = []
            for item in params.get("LaunchTemplateSet"):
                obj = LaunchTemplateInfo()
                obj._deserialize(item)
                self.LaunchTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 地域数量
        :type TotalCount: int
        :param RegionSet: 地域列表信息
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReservedInstancesConfigInfosRequest(AbstractModel):
    """DescribeReservedInstancesConfigInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: zone
按照预留实例计费可购买的可用区进行过滤。形如：ap-guangzhou-1。
类型：String
必选：否
可选项：各地域可用区列表

product-description
按照预留实例计费的平台描述（即操作系统）进行过滤。形如：linux。
类型：String
必选：否
可选项：linux

duration
按照预留实例计费有效期，即预留实例计费购买时长进行过滤。形如：31536000。
类型：Integer
计量单位：秒
必选：否
可选项：31536000 (1年)
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesConfigInfosResponse(AbstractModel):
    """DescribeReservedInstancesConfigInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReservedInstanceConfigInfos: 预留实例静态配置信息列表。
        :type ReservedInstanceConfigInfos: list of ReservedInstanceConfigInfoItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReservedInstanceConfigInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReservedInstanceConfigInfos") is not None:
            self.ReservedInstanceConfigInfos = []
            for item in params.get("ReservedInstanceConfigInfos"):
                obj = ReservedInstanceConfigInfoItem()
                obj._deserialize(item)
                self.ReservedInstanceConfigInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReservedInstancesOfferingsRequest(AbstractModel):
    """DescribeReservedInstancesOfferings请求参数结构体

    """

    def __init__(self):
        r"""
        :param DryRun: 试运行, 默认为 false。
        :type DryRun: bool
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param MaxDuration: 以最大有效期作为过滤参数。
计量单位: 秒
默认为 94608000。
        :type MaxDuration: int
        :param MinDuration: 以最小有效期作为过滤参数。
计量单位: 秒
默认为 2592000。
        :type MinDuration: int
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照预留实例计费可购买的【<strong>可用区</strong>】进行过滤。形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>duration</strong></li>
<p style="padding-left: 30px;">按照预留实例计费【<strong>有效期</strong>】即预留实例计费购买时长进行过滤。形如：31536000。</p><p style="padding-left: 30px;">类型：Integer</p><p style="padding-left: 30px;">计量单位：秒</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：31536000 (1年) | 94608000（3年）</p>
<li><strong>instance-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>预留实例计费类型</strong>】进行过滤。形如：S3.MEDIUM4。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/11518">预留实例计费类型列表</a></p>
<li><strong>offering-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>付款类型</strong>】进行过滤。形如：All Upfront (预付全部费用)。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：All Upfront (预付全部费用)</p>
<li><strong>product-description</strong></li>
<p style="padding-left: 30px;">按照预留实例计费的【<strong>平台描述</strong>】（即操作系统）进行过滤。形如：linux。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：linux</p>
<li><strong>reserved-instances-offering-id</strong></li>
<p style="padding-left: 30px;">按照【<strong>预留实例计费配置ID</strong>】进行过滤。形如：650c138f-ae7e-4750-952a-96841d6e9fc1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。
        :type Filters: list of Filter
        """
        self.DryRun = None
        self.Offset = None
        self.Limit = None
        self.MaxDuration = None
        self.MinDuration = None
        self.Filters = None


    def _deserialize(self, params):
        self.DryRun = params.get("DryRun")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MaxDuration = params.get("MaxDuration")
        self.MinDuration = params.get("MinDuration")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesOfferingsResponse(AbstractModel):
    """DescribeReservedInstancesOfferings返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的预留实例计费数量。
        :type TotalCount: int
        :param ReservedInstancesOfferingsSet: 符合条件的预留实例计费列表。
        :type ReservedInstancesOfferingsSet: list of ReservedInstancesOffering
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReservedInstancesOfferingsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReservedInstancesOfferingsSet") is not None:
            self.ReservedInstancesOfferingsSet = []
            for item in params.get("ReservedInstancesOfferingsSet"):
                obj = ReservedInstancesOffering()
                obj._deserialize(item)
                self.ReservedInstancesOfferingsSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReservedInstancesRequest(AbstractModel):
    """DescribeReservedInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param DryRun: 试运行。默认为 false。
        :type DryRun: bool
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照预留实例计费可购买的【<strong>可用区</strong>】进行过滤。形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>duration</strong></li>
<p style="padding-left: 30px;">按照预留实例计费【<strong>有效期</strong>】即预留实例计费购买时长进行过滤。形如：31536000。</p><p style="padding-left: 30px;">类型：Integer</p><p style="padding-left: 30px;">计量单位：秒</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：31536000 (1年) | 94608000（3年）</p>
<li><strong>instance-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>预留实例规格</strong>】进行过滤。形如：S3.MEDIUM4。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/11518">预留实例规格列表</a></p>
<li><strong>instance-family</strong></li>
<p style="padding-left: 30px;">按照【<strong>预留实例类型</strong>】进行过滤。形如：S3。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/11518">预留实例类型列表</a></p>
<li><strong>offering-type</strong></li>
<li><strong>offering-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>付款类型</strong>】进行过滤。形如：All Upfront (全预付)。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：All Upfront (全预付) | Partial Upfront (部分预付) | No Upfront (零预付)</p>
<li><strong>product-description</strong></li>
<p style="padding-left: 30px;">按照预留实例计费的【<strong>平台描述</strong>】（即操作系统）进行过滤。形如：linux。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：linux</p>
<li><strong>reserved-instances-id</strong></li>
<p style="padding-left: 30px;">按照已购买【<strong>预留实例计费ID</strong>】进行过滤。形如：650c138f-ae7e-4750-952a-96841d6e9fc1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>state</strong></li>
<p style="padding-left: 30px;">按照已购买【<strong>预留实例计费状态</strong>】进行过滤。形如：active。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：active (已创建) | pending (等待被创建) | retired (过期)</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。
        :type Filters: list of Filter
        """
        self.DryRun = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.DryRun = params.get("DryRun")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesResponse(AbstractModel):
    """DescribeReservedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的预留实例计费数量。
        :type TotalCount: int
        :param ReservedInstancesSet: 符合条件的预留实例计费列表。
        :type ReservedInstancesSet: list of ReservedInstances
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReservedInstancesSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReservedInstancesSet") is not None:
            self.ReservedInstancesSet = []
            for item in params.get("ReservedInstancesSet"):
                obj = ReservedInstances()
                obj._deserialize(item)
                self.ReservedInstancesSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeZoneInstanceConfigInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>instance-family</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例机型系列</strong>】进行过滤。实例机型系列形如：S1、I1、M1等。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例机型</strong>】进行过滤。不同实例机型指定了不同的资源规格，具体取值可通过调用接口 [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/product/213/15749) 来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则默认机型为S1.SMALL1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-charge-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例计费模式</strong>】进行过滤。(PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费 )</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>sort-keys</strong></li>
<p style="padding-left: 30px;">按关键字进行排序,格式为排序字段加排序方式，中间用冒号分隔。 例如： 按cpu数逆序排序 "cpu:desc", 按mem大小顺序排序 "mem:asc"</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>offset</strong></li>
<p style="padding-left: 30px;">按照偏移量进行分页</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>limit</strong></li>
<p style="padding-left: 30px;">每页返回的数据条数</p><p style="padding-left: 30px;">类型：Integer</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为100。
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeZoneInstanceConfigInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceTypeQuotaSet: 可用区机型配置列表。
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceTypeQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self.InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self.InstanceTypeQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 可用区数量。
        :type TotalCount: int
        :param ZoneSet: 可用区列表信息。
        :type ZoneSet: list of ZoneInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID，每次请求批量实例的上限为100。<br><br>可以通过以下方式获取可用的实例ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询实例ID。<br><li>通过调用接口 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) ，取返回信息中的 `InstanceId` 获取实例ID。
        :type InstanceIds: list of str
        :param KeyIds: 密钥对ID列表，每次请求批量密钥对的上限为100。密钥对ID形如：`skey-11112222`。<br><br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的 `KeyId` 获取密钥对ID。
        :type KeyIds: list of str
        :param ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再解绑密钥。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机。<br><li>FALSE：表示在正常关机失败后不进行强制关机。<br><br>默认取值：FALSE。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.KeyIds = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.KeyIds = params.get("KeyIds")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityGroupIds: 要解绑的`安全组ID`，类似sg-efil73jd，只支持解绑单个安全组。
        :type SecurityGroupIds: list of str
        :param InstanceIds: 被解绑的`实例ID`，类似ins-lesecurk，支持指定多个实例 。
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisasterRecoverGroup(AbstractModel):
    """容灾组信息

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupId: 分散置放群组id。
        :type DisasterRecoverGroupId: str
        :param Name: 分散置放群组名称，长度1-60个字符。
        :type Name: str
        :param Type: 分散置放群组类型，取值范围：<br><li>HOST：物理机<br><li>SW：交换机<br><li>RACK：机架
        :type Type: str
        :param CvmQuotaTotal: 分散置放群组内最大容纳云服务器数量。
        :type CvmQuotaTotal: int
        :param CurrentNum: 分散置放群组内云服务器当前数量。
        :type CurrentNum: int
        :param InstanceIds: 分散置放群组内，云服务器id列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param CreateTime: 分散置放群组创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.DisasterRecoverGroupId = None
        self.Name = None
        self.Type = None
        self.CvmQuotaTotal = None
        self.CurrentNum = None
        self.InstanceIds = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.CvmQuotaTotal = params.get("CvmQuotaTotal")
        self.CurrentNum = params.get("CurrentNum")
        self.InstanceIds = params.get("InstanceIds")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisasterRecoverGroupQuota(AbstractModel):
    """置放群组配置数据

    """

    def __init__(self):
        r"""
        :param GroupQuota: 可创建置放群组数量的上限。
        :type GroupQuota: int
        :param CurrentNum: 当前用户已经创建的置放群组数量。
        :type CurrentNum: int
        :param CvmInHostGroupQuota: 物理机类型容灾组内实例的配额数。
        :type CvmInHostGroupQuota: int
        :param CvmInSwitchGroupQuota: 交换机类型容灾组内实例的配额数。
        :type CvmInSwitchGroupQuota: int
        :param CvmInRackGroupQuota: 机架类型容灾组内实例的配额数。
        :type CvmInRackGroupQuota: int
        """
        self.GroupQuota = None
        self.CurrentNum = None
        self.CvmInHostGroupQuota = None
        self.CvmInSwitchGroupQuota = None
        self.CvmInRackGroupQuota = None


    def _deserialize(self, params):
        self.GroupQuota = params.get("GroupQuota")
        self.CurrentNum = params.get("CurrentNum")
        self.CvmInHostGroupQuota = params.get("CvmInHostGroupQuota")
        self.CvmInSwitchGroupQuota = params.get("CvmInSwitchGroupQuota")
        self.CvmInRackGroupQuota = params.get("CvmInRackGroupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        r"""
        :param SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.cvm.v20170312.models.RunSecurityServiceEnabled`
        :param MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.cvm.v20170312.models.RunMonitorServiceEnabled`
        :param AutomationService: 开启云自动化助手服务。若不指定该参数，则默认不开启云自动化助手服务。
        :type AutomationService: :class:`tencentcloud.cvm.v20170312.models.RunAutomationServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None
        self.AutomationService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self.AutomationService = RunAutomationServiceEnabled()
            self.AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportImagesRequest(AbstractModel):
    """ExportImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param BucketName: COS存储桶名称
        :type BucketName: str
        :param ImageIds: 镜像ID列表
        :type ImageIds: list of str
        :param ExportFormat: 镜像文件导出格式。取值范围：RAW，QCOW2，VHD，VMDK。默认为RAW
        :type ExportFormat: str
        :param FileNamePrefixList: 导出文件的名称前缀列表
        :type FileNamePrefixList: list of str
        :param OnlyExportRootDisk: 是否只导出系统盘
        :type OnlyExportRootDisk: bool
        :param DryRun: 检测镜像是否支持导出
        :type DryRun: bool
        :param RoleName: 角色名称。默认为CVM_QcsRole，发起请求前请确认是否存在该角色，以及是否已正确配置COS写入权限。
        :type RoleName: str
        """
        self.BucketName = None
        self.ImageIds = None
        self.ExportFormat = None
        self.FileNamePrefixList = None
        self.OnlyExportRootDisk = None
        self.DryRun = None
        self.RoleName = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ImageIds = params.get("ImageIds")
        self.ExportFormat = params.get("ExportFormat")
        self.FileNamePrefixList = params.get("FileNamePrefixList")
        self.OnlyExportRootDisk = params.get("OnlyExportRootDisk")
        self.DryRun = params.get("DryRun")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportImagesResponse(AbstractModel):
    """ExportImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 导出镜像任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Externals(AbstractModel):
    """扩展数据

    """

    def __init__(self):
        r"""
        :param ReleaseAddress: 释放地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseAddress: bool
        :param UnsupportNetworks: 不支持的网络类型，取值范围：<br><li>BASIC：基础网络<br><li>VPC1.0：私有网络VPC1.0
注意：此字段可能返回 null，表示取不到有效值。
        :type UnsupportNetworks: list of str
        :param StorageBlockAttr: HDD本地存储属性
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageBlockAttr: :class:`tencentcloud.cvm.v20170312.models.StorageBlock`
        """
        self.ReleaseAddress = None
        self.UnsupportNetworks = None
        self.StorageBlockAttr = None


    def _deserialize(self, params):
        self.ReleaseAddress = params.get("ReleaseAddress")
        self.UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self.StorageBlockAttr = StorageBlock()
            self.StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区 ***并且*** 实例计费模式（`instance-charge-type`）为包年包月 ***或者*** 按量计费的实例时，可如下实现：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        r"""
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
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
        


class GPUInfo(AbstractModel):
    """实例GPU信息

    """

    def __init__(self):
        r"""
        :param GPUCount: 实例GPU个数。值小于1代表VGPU类型，大于1代表GPU直通类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUCount: float
        :param GPUId: 实例GPU地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUId: list of str
        :param GPUType: 实例GPU类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUType: str
        """
        self.GPUCount = None
        self.GPUId = None
        self.GPUType = None


    def _deserialize(self, params):
        self.GPUCount = params.get("GPUCount")
        self.GPUId = params.get("GPUId")
        self.GPUType = params.get("GPUType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostItem(AbstractModel):
    """专用宿主机实例详细信息

    """

    def __init__(self):
        r"""
        :param Placement: 专用宿主机实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param HostId: 专用宿主机实例id
        :type HostId: str
        :param HostType: 专用宿主机实例类型
        :type HostType: str
        :param HostName: 专用宿主机实例名称
        :type HostName: str
        :param HostChargeType: 专用宿主机实例付费模式
        :type HostChargeType: str
        :param RenewFlag: 专用宿主机实例自动续费标记
        :type RenewFlag: str
        :param CreatedTime: 专用宿主机实例创建时间
        :type CreatedTime: str
        :param ExpiredTime: 专用宿主机实例过期时间
        :type ExpiredTime: str
        :param InstanceIds: 专用宿主机实例上已创建云子机的实例id列表
        :type InstanceIds: list of str
        :param HostState: 专用宿主机实例状态
        :type HostState: str
        :param HostIp: 专用宿主机实例ip
        :type HostIp: str
        :param HostResource: 专用宿主机实例资源信息
        :type HostResource: :class:`tencentcloud.cvm.v20170312.models.HostResource`
        :param CageId: 专用宿主机所属的围笼ID。该字段仅对金融专区围笼内的专用宿主机有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CageId: str
        """
        self.Placement = None
        self.HostId = None
        self.HostType = None
        self.HostName = None
        self.HostChargeType = None
        self.RenewFlag = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.InstanceIds = None
        self.HostState = None
        self.HostIp = None
        self.HostResource = None
        self.CageId = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.HostId = params.get("HostId")
        self.HostType = params.get("HostType")
        self.HostName = params.get("HostName")
        self.HostChargeType = params.get("HostChargeType")
        self.RenewFlag = params.get("RenewFlag")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.InstanceIds = params.get("InstanceIds")
        self.HostState = params.get("HostState")
        self.HostIp = params.get("HostIp")
        if params.get("HostResource") is not None:
            self.HostResource = HostResource()
            self.HostResource._deserialize(params.get("HostResource"))
        self.CageId = params.get("CageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostResource(AbstractModel):
    """专用宿主机实例的资源信息

    """

    def __init__(self):
        r"""
        :param CpuTotal: 专用宿主机实例总cpu核数
        :type CpuTotal: int
        :param CpuAvailable: 专用宿主机实例可用cpu核数
        :type CpuAvailable: int
        :param MemTotal: 专用宿主机实例总内存大小（单位为:GiB）
        :type MemTotal: float
        :param MemAvailable: 专用宿主机实例可用内存大小（单位为:GiB）
        :type MemAvailable: float
        :param DiskTotal: 专用宿主机实例总磁盘大小（单位为:GiB）
        :type DiskTotal: int
        :param DiskAvailable: 专用宿主机实例可用磁盘大小（单位为:GiB）
        :type DiskAvailable: int
        :param DiskType: 专用宿主机实例磁盘类型
        :type DiskType: str
        :param GpuTotal: 专用宿主机实例总GPU卡数
        :type GpuTotal: int
        :param GpuAvailable: 专用宿主机实例可用GPU卡数
        :type GpuAvailable: int
        """
        self.CpuTotal = None
        self.CpuAvailable = None
        self.MemTotal = None
        self.MemAvailable = None
        self.DiskTotal = None
        self.DiskAvailable = None
        self.DiskType = None
        self.GpuTotal = None
        self.GpuAvailable = None


    def _deserialize(self, params):
        self.CpuTotal = params.get("CpuTotal")
        self.CpuAvailable = params.get("CpuAvailable")
        self.MemTotal = params.get("MemTotal")
        self.MemAvailable = params.get("MemAvailable")
        self.DiskTotal = params.get("DiskTotal")
        self.DiskAvailable = params.get("DiskAvailable")
        self.DiskType = params.get("DiskType")
        self.GpuTotal = params.get("GpuTotal")
        self.GpuAvailable = params.get("GpuAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """一个关于镜像详细信息的结构体，主要包括镜像的主要状态与属性。

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像ID
        :type ImageId: str
        :param OsName: 镜像操作系统
        :type OsName: str
        :param ImageType: 镜像类型
        :type ImageType: str
        :param CreatedTime: 镜像创建时间
        :type CreatedTime: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageDescription: 镜像描述
        :type ImageDescription: str
        :param ImageSize: 镜像大小
        :type ImageSize: int
        :param Architecture: 镜像架构
        :type Architecture: str
        :param ImageState: 镜像状态:
CREATING-创建中
NORMAL-正常
CREATEFAILED-创建失败
USING-使用中
SYNCING-同步中
IMPORTING-导入中
IMPORTFAILED-导入失败
        :type ImageState: str
        :param Platform: 镜像来源平台
        :type Platform: str
        :param ImageCreator: 镜像创建者
        :type ImageCreator: str
        :param ImageSource: 镜像来源
        :type ImageSource: str
        :param SyncPercent: 同步百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncPercent: int
        :param IsSupportCloudinit: 镜像是否支持cloud-init
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportCloudinit: bool
        :param SnapshotSet: 镜像关联的快照信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotSet: list of Snapshot
        :param Tags: 镜像关联的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param LicenseType: 镜像许可类型
        :type LicenseType: str
        """
        self.ImageId = None
        self.OsName = None
        self.ImageType = None
        self.CreatedTime = None
        self.ImageName = None
        self.ImageDescription = None
        self.ImageSize = None
        self.Architecture = None
        self.ImageState = None
        self.Platform = None
        self.ImageCreator = None
        self.ImageSource = None
        self.SyncPercent = None
        self.IsSupportCloudinit = None
        self.SnapshotSet = None
        self.Tags = None
        self.LicenseType = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.OsName = params.get("OsName")
        self.ImageType = params.get("ImageType")
        self.CreatedTime = params.get("CreatedTime")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        self.ImageSize = params.get("ImageSize")
        self.Architecture = params.get("Architecture")
        self.ImageState = params.get("ImageState")
        self.Platform = params.get("Platform")
        self.ImageCreator = params.get("ImageCreator")
        self.ImageSource = params.get("ImageSource")
        self.SyncPercent = params.get("SyncPercent")
        self.IsSupportCloudinit = params.get("IsSupportCloudinit")
        if params.get("SnapshotSet") is not None:
            self.SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self.SnapshotSet.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """支持的操作系统类型，根据windows和Linux分类。

    """

    def __init__(self):
        r"""
        :param Windows: 支持的windows操作系统。
注意：此字段可能返回 null，表示取不到有效值。
        :type Windows: list of str
        :param Linux: 支持的linux操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Linux: list of str
        """
        self.Windows = None
        self.Linux = None


    def _deserialize(self, params):
        self.Windows = params.get("Windows")
        self.Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageQuota(AbstractModel):
    """镜像配额

    """

    def __init__(self):
        r"""
        :param UsedQuota: 已使用配额
        :type UsedQuota: int
        :param TotalQuota: 总配额
        :type TotalQuota: int
        """
        self.UsedQuota = None
        self.TotalQuota = None


    def _deserialize(self, params):
        self.UsedQuota = params.get("UsedQuota")
        self.TotalQuota = params.get("TotalQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageRequest(AbstractModel):
    """ImportImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Architecture: 导入镜像的操作系统架构，`x86_64` 或 `i386`
        :type Architecture: str
        :param OsType: 导入镜像的操作系统类型，通过`DescribeImportImageOs`获取
        :type OsType: str
        :param OsVersion: 导入镜像的操作系统版本，通过`DescribeImportImageOs`获取
        :type OsVersion: str
        :param ImageUrl: 导入镜像存放的cos地址
        :type ImageUrl: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageDescription: 镜像描述
        :type ImageDescription: str
        :param DryRun: 只检查参数，不执行任务
        :type DryRun: bool
        :param Force: 是否强制导入，参考[强制导入镜像](https://cloud.tencent.com/document/product/213/12849)
        :type Force: bool
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到自定义镜像。
        :type TagSpecification: list of TagSpecification
        :param LicenseType: 导入镜像后，激活操作系统采用的许可证类型。
可选项：
TencentCloud: 腾讯云官方许可
BYOL: 自带许可（Bring Your Own License）
        :type LicenseType: str
        """
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.ImageUrl = None
        self.ImageName = None
        self.ImageDescription = None
        self.DryRun = None
        self.Force = None
        self.TagSpecification = None
        self.LicenseType = None


    def _deserialize(self, params):
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        self.DryRun = params.get("DryRun")
        self.Force = params.get("Force")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :type KeyName: str
        :param ProjectId: 密钥对创建后所属的[项目](https://cloud.tencent.com/document/product/378/10861)ID。<br><br>可以通过以下方式获取项目ID：<br><li>通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID。<br><li>通过调用接口 [DescribeProject](https://cloud.tencent.com/document/api/378/4400)，取返回信息中的 `projectId ` 获取项目ID。

如果是默认项目，直接填0就可以。
        :type ProjectId: int
        :param PublicKey: 密钥对的公钥内容，`OpenSSH RSA` 格式。
        :type PublicKey: str
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到密钥对。
        :type TagSpecification: list of TagSpecification
        """
        self.KeyName = None
        self.ProjectId = None
        self.PublicKey = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.PublicKey = params.get("PublicKey")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairResponse(AbstractModel):
    """ImportKeyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param KeyId: 密钥对ID。
        :type KeyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class InquirePricePurchaseReservedInstancesOfferingRequest(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceCount: 购买预留实例计费数量
        :type InstanceCount: int
        :param ReservedInstancesOfferingId: 预留实例计费配置ID
        :type ReservedInstancesOfferingId: str
        :param DryRun: 试运行
        :type DryRun: bool
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性
        :type ClientToken: str
        :param ReservedInstanceName: 预留实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>最多支持60个字符（包含模式串）。</li>
        :type ReservedInstanceName: str
        """
        self.InstanceCount = None
        self.ReservedInstancesOfferingId = None
        self.DryRun = None
        self.ClientToken = None
        self.ReservedInstanceName = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.DryRun = params.get("DryRun")
        self.ClientToken = params.get("ClientToken")
        self.ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePricePurchaseReservedInstancesOfferingResponse(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示对应配置预留实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ReservedInstancePrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = ReservedInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceModifyInstancesChargeTypeRequest(AbstractModel):
    """InquiryPriceModifyInstancesChargeType请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月。<br><li>POSTPAID_BY_HOUR：后付费，即按量付费。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。<dx-alert infotype="explain" title="">若指定实例的付费模式为预付费则该参数必传。</dx-alert>
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param ModifyPortableDataDisk: 是否同时切换弹性数据云盘计费模式。取值范围：<br><li>TRUE：表示切换弹性数据云盘计费模式<br><li>FALSE：表示不切换弹性数据云盘计费模式<br><br>默认取值：FALSE。
        :type ModifyPortableDataDisk: bool
        """
        self.InstanceIds = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.ModifyPortableDataDisk = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.ModifyPortableDataDisk = params.get("ModifyPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceModifyInstancesChargeTypeResponse(AbstractModel):
    """InquiryPriceModifyInstancesChargeType返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示对应配置实例转换计费模式的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewInstancesRequest(AbstractModel):
    """InquiryPriceRenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param DryRun: 试运行，测试使用，不执行具体逻辑。取值范围：<br><li>TRUE：跳过执行逻辑<br><li>FALSE：执行逻辑<br><br>默认取值：FALSE。
        :type DryRun: bool
        :param RenewPortableDataDisk: 是否续费弹性数据盘。取值范围：<br><li>TRUE：表示续费包年包月实例同时续费其挂载的弹性数据盘<br><li>FALSE：表示续费包年包月实例同时不再续费其挂载的弹性数据盘<br><br>默认取值：TRUE。
        :type RenewPortableDataDisk: bool
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None
        self.DryRun = None
        self.RenewPortableDataDisk = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.DryRun = params.get("DryRun")
        self.RenewPortableDataDisk = params.get("RenewPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstancesResponse(AbstractModel):
    """InquiryPriceRenewInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示对应配置实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstanceRequest(AbstractModel):
    """InquiryPriceResetInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param ImageId: 指定有效的[镜像](/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param SystemDisk: 实例系统盘配置信息。系统盘为云盘的实例可以通过该参数指定重装后的系统盘大小来实现对系统盘的扩容操作，若不指定则默认系统盘大小保持不变。系统盘大小只支持扩容不支持缩容；重装只支持修改系统盘的大小，不能修改系统盘的类型。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        """
        self.InstanceId = None
        self.ImageId = None
        self.SystemDisk = None
        self.LoginSettings = None
        self.EnhancedService = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstanceResponse(AbstractModel):
    """InquiryPriceResetInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示重装成对应配置实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。当调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽时，只支持一个实例。
        :type InstanceIds: list of str
        :param InternetAccessible: 公网出带宽配置。不同机型带宽上限范围不一致，具体限制详见带宽限制对账表。暂时只支持`InternetMaxBandwidthOut`参数。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param StartTime: 带宽生效的起始时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始时间不能早于当前时间。如果起始时间是今天则新设置的带宽立即生效。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type StartTime: str
        :param EndTime: 带宽生效的终止时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。新设置的带宽的有效期包含终止时间此日期。终止时间不能晚于包年包月实例的到期时间。实例的到期时间可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`ExpiredTime`获取。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type EndTime: str
        """
        self.InstanceIds = None
        self.InternetAccessible = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示带宽调整为对应大小之后的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstancesTypeRequest(AbstractModel):
    """InquiryPriceResetInstancesType请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。本接口每次请求批量实例的上限为1。
        :type InstanceIds: list of str
        :param InstanceType: 实例机型。不同实例机型指定了不同的资源规格，具体取值可参见附表[实例资源规格](https://cloud.tencent.com/document/product/213/11518)对照表，也可以调用查询[实例资源规格列表](https://cloud.tencent.com/document/product/213/15749)接口获得最新的规格表。
        :type InstanceType: str
        """
        self.InstanceIds = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesTypeResponse(AbstractModel):
    """InquiryPriceResetInstancesType返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示调整成对应机型实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResizeInstanceDisksRequest(AbstractModel):
    """InquiryPriceResizeInstanceDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param DataDisks: 待扩容的数据盘配置信息。只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性），且[数据盘类型](https://cloud.tencent.com/document/product/213/15753#DataDisk)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。数据盘容量单位：GB。最小扩容步长：10G。关于数据盘类型的选择请参考硬盘产品简介。可选数据盘类型受到实例类型`InstanceType`限制。另外允许扩容的最大容量也因数据盘类型的不同而有所差异。
        :type DataDisks: list of DataDisk
        :param ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        """
        self.InstanceId = None
        self.DataDisks = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeInstanceDisksResponse(AbstractModel):
    """InquiryPriceResizeInstanceDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示磁盘扩容成对应配置的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRunInstancesRequest(AbstractModel):
    """InquiryPriceRunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
 <b>注：如果您不指定LaunchTemplate参数，则Placement为必选参数。若同时传递Placement和LaunchTemplate，则默认覆盖LaunchTemplate中对应的Placement的值。</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
 <b>注：如果您不指定LaunchTemplate参数，则ImageId为必选参数。若同时传递ImageId和LaunchTemplate，则默认覆盖LaunchTemplate中对应的ImageId的值。</b>
        :type ImageId: str
        :param InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param InstanceType: 实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则默认机型为S1.SMALL1。
        :type InstanceType: str
        :param SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，那么InstanceCount参数只能为1。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: 购买实例数量。取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。
        :type InstanceName: str
        :param LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则默认不绑定安全组。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param HostName: 云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 30]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。
        :type HostName: str
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param HpcClusterId: 高性能计算集群ID。
        :type HpcClusterId: str
        """
        self.Placement = None
        self.ImageId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.HpcClusterId = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ImageId = params.get("ImageId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.HpcClusterId = params.get("HpcClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRunInstancesResponse(AbstractModel):
    """InquiryPriceRunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 该参数表示对应配置实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceTerminateInstancesRequest(AbstractModel):
    """InquiryPriceTerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceTerminateInstancesResponse(AbstractModel):
    """InquiryPriceTerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceRefundsSet: 退款详情。
        :type InstanceRefundsSet: list of InstanceRefund
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceRefundsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceRefundsSet") is not None:
            self.InstanceRefundsSet = []
            for item in params.get("InstanceRefundsSet"):
                obj = InstanceRefund()
                obj._deserialize(item)
                self.InstanceRefundsSet.append(obj)
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """描述实例的信息

    """

    def __init__(self):
        r"""
        :param Placement: 实例所在的位置。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param InstanceId: 实例`ID`。
        :type InstanceId: str
        :param InstanceType: 实例机型。
        :type InstanceType: str
        :param CPU: 实例的CPU核数，单位：核。
        :type CPU: int
        :param Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param RestrictState: 实例业务状态。取值范围：<br><li>NORMAL：表示正常状态的实例<br><li>EXPIRED：表示过期的实例<br><li>PROTECTIVELY_ISOLATED：表示被安全隔离的实例。
        :type RestrictState: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param InstanceChargeType: 实例计费模式。取值范围：<br><li>`PREPAID`：表示预付费，即包年包月<br><li>`POSTPAID_BY_HOUR`：表示后付费，即按量计费<br><li>`CDHPAID`：`专用宿主机`付费，即只对`专用宿主机`计费，不对`专用宿主机`上的实例计费。<br><li>`SPOTPAID`：表示竞价实例付费。
        :type InstanceChargeType: str
        :param SystemDisk: 实例系统盘信息。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 实例数据盘信息。
        :type DataDisks: list of DataDisk
        :param PrivateIpAddresses: 实例主网卡的内网`IP`列表。
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: 实例主网卡的公网`IP`列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param InternetAccessible: 实例带宽信息。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param VirtualPrivateCloud: 实例所属虚拟私有网络信息。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ImageId: 生产实例所使用的镜像`ID`。
        :type ImageId: str
        :param RenewFlag: 自动续费标识。取值范围：<br><li>`NOTIFY_AND_MANUAL_RENEW`：表示通知即将过期，但不自动续费<br><li>`NOTIFY_AND_AUTO_RENEW`：表示通知即将过期，而且自动续费<br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`：表示不通知即将过期，也不自动续费。
<br><li>注意：后付费模式本项为null
        :type RenewFlag: str
        :param CreatedTime: 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param ExpiredTime: 到期时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。注意：后付费模式本项为null
        :type ExpiredTime: str
        :param OsName: 操作系统名称。
        :type OsName: str
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。
        :type SecurityGroupIds: list of str
        :param LoginSettings: 实例登录设置。目前只返回实例所关联的密钥。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param InstanceState: 实例状态。取值范围：<br><li>PENDING：表示创建中<br></li><li>LAUNCH_FAILED：表示创建失败<br></li><li>RUNNING：表示运行中<br></li><li>STOPPED：表示关机<br></li><li>STARTING：表示开机中<br></li><li>STOPPING：表示关机中<br></li><li>REBOOTING：表示重启中<br></li><li>SHUTDOWN：表示停止待销毁<br></li><li>TERMINATING：表示销毁中。<br></li>
        :type InstanceState: str
        :param Tags: 实例关联的标签列表。
        :type Tags: list of Tag
        :param StopChargingMode: 实例的关机计费模式。
取值范围：<br><li>KEEP_CHARGING：关机继续收费<br><li>STOP_CHARGING：关机停止收费<li>NOT_APPLICABLE：实例处于非关机状态或者不适用关机停止计费的条件<br>
        :type StopChargingMode: str
        :param Uuid: 实例全局唯一ID
        :type Uuid: str
        :param LatestOperation: 实例的最新操作。例：StopInstances、ResetInstance。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param LatestOperationState: 实例的最新操作状态。取值范围：<br><li>SUCCESS：表示操作成功<br><li>OPERATING：表示操作执行中<br><li>FAILED：表示操作失败
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param LatestOperationRequestId: 实例最新操作的唯一请求 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationRequestId: str
        :param DisasterRecoverGroupId: 分散置放群组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisasterRecoverGroupId: str
        :param IPv6Addresses: 实例的IPv6地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Addresses: list of str
        :param CamRoleName: CAM角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type CamRoleName: str
        :param HpcClusterId: 高性能计算集群`ID`。
注意：此字段可能返回 null，表示取不到有效值。
        :type HpcClusterId: str
        :param RdmaIpAddresses: 高性能计算集群`IP`列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RdmaIpAddresses: list of str
        :param IsolatedSource: 实例隔离类型。取值范围：<br><li>ARREAR：表示欠费隔离<br></li><li>EXPIRE：表示到期隔离<br></li><li>MANMADE：表示主动退还隔离<br></li><li>NOTISOLATED：表示未隔离<br></li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedSource: str
        :param GPUInfo: GPU信息。如果是gpu类型子机，该值会返回GPU信息，如果是其他类型子机则不返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUInfo: :class:`tencentcloud.cvm.v20170312.models.GPUInfo`
        :param LicenseType: 实例的操作系统许可类型，默认为TencentCloud
        :type LicenseType: str
        """
        self.Placement = None
        self.InstanceId = None
        self.InstanceType = None
        self.CPU = None
        self.Memory = None
        self.RestrictState = None
        self.InstanceName = None
        self.InstanceChargeType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.InternetAccessible = None
        self.VirtualPrivateCloud = None
        self.ImageId = None
        self.RenewFlag = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.OsName = None
        self.SecurityGroupIds = None
        self.LoginSettings = None
        self.InstanceState = None
        self.Tags = None
        self.StopChargingMode = None
        self.Uuid = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.LatestOperationRequestId = None
        self.DisasterRecoverGroupId = None
        self.IPv6Addresses = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.RdmaIpAddresses = None
        self.IsolatedSource = None
        self.GPUInfo = None
        self.LicenseType = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceId = params.get("InstanceId")
        self.InstanceType = params.get("InstanceType")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.RestrictState = params.get("RestrictState")
        self.InstanceName = params.get("InstanceName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ImageId = params.get("ImageId")
        self.RenewFlag = params.get("RenewFlag")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.OsName = params.get("OsName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.InstanceState = params.get("InstanceState")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.StopChargingMode = params.get("StopChargingMode")
        self.Uuid = params.get("Uuid")
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.LatestOperationRequestId = params.get("LatestOperationRequestId")
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.IPv6Addresses = params.get("IPv6Addresses")
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        self.RdmaIpAddresses = params.get("RdmaIpAddresses")
        self.IsolatedSource = params.get("IsolatedSource")
        if params.get("GPUInfo") is not None:
            self.GPUInfo = GPUInfo()
            self.GPUInfo._deserialize(params.get("GPUInfo"))
        self.LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
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
        


class InstanceFamilyConfig(AbstractModel):
    """描述实例的机型族配置信息
    形如：{'InstanceFamilyName': '标准型S1', 'InstanceFamily': 'S1'}、{'InstanceFamilyName': '网络优化型N1', 'InstanceFamily': 'N1'}、{'InstanceFamilyName': '高IO型I1', 'InstanceFamily': 'I1'}等。

    """

    def __init__(self):
        r"""
        :param InstanceFamilyName: 机型族名称的中文全称。
        :type InstanceFamilyName: str
        :param InstanceFamily: 机型族名称的英文简称。
        :type InstanceFamily: str
        """
        self.InstanceFamilyName = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.InstanceFamilyName = params.get("InstanceFamilyName")
        self.InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMarketOptionsRequest(AbstractModel):
    """竞价请求相关选项

    """

    def __init__(self):
        r"""
        :param SpotOptions: 竞价相关选项
        :type SpotOptions: :class:`tencentcloud.cvm.v20170312.models.SpotMarketOptions`
        :param MarketType: 市场选项类型，当前只支持取值：spot
        :type MarketType: str
        """
        self.SpotOptions = None
        self.MarketType = None


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))
        self.MarketType = params.get("MarketType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRefund(AbstractModel):
    """描述退款详情。

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Refunds: 退款数额。
注意：此字段可能返回 null，表示取不到有效值。
        :type Refunds: float
        :param PriceDetail: 退款详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceDetail: str
        """
        self.InstanceId = None
        self.Refunds = None
        self.PriceDetail = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Refunds = params.get("Refunds")
        self.PriceDetail = params.get("PriceDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatus(AbstractModel):
    """描述实例的状态。状态类型详见[实例状态表](/document/api/213/15753#InstanceStatus)

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例`ID`。
        :type InstanceId: str
        :param InstanceState: 实例状态。取值范围：<br><li>PENDING：表示创建中<br></li><li>LAUNCH_FAILED：表示创建失败<br></li><li>RUNNING：表示运行中<br></li><li>STOPPED：表示关机<br></li><li>STARTING：表示开机中<br></li><li>STOPPING：表示关机中<br></li><li>REBOOTING：表示重启中<br></li><li>SHUTDOWN：表示停止待销毁<br></li><li>TERMINATING：表示销毁中。<br></li>
        :type InstanceState: str
        """
        self.InstanceId = None
        self.InstanceState = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceState = params.get("InstanceState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfig(AbstractModel):
    """描述实例机型配置信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区。
        :type Zone: str
        :param InstanceType: 实例机型。
        :type InstanceType: str
        :param InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param GPU: GPU核数，单位：核。
        :type GPU: int
        :param CPU: CPU核数，单位：核。
        :type CPU: int
        :param Memory: 内存容量，单位：`GB`。
        :type Memory: int
        :param FPGA: FPGA核数，单位：核。
        :type FPGA: int
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceFamily = None
        self.GPU = None
        self.CPU = None
        self.Memory = None
        self.FPGA = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceFamily = params.get("InstanceFamily")
        self.GPU = params.get("GPU")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.FPGA = params.get("FPGA")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfigStatus(AbstractModel):
    """描述实例机型配置信息及状态信息

    """

    def __init__(self):
        r"""
        :param Status: 状态描述
        :type Status: str
        :param Message: 状态描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param InstanceTypeConfig: 配置信息
        :type InstanceTypeConfig: :class:`tencentcloud.cvm.v20170312.models.InstanceTypeConfig`
        """
        self.Status = None
        self.Message = None
        self.InstanceTypeConfig = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeQuotaItem(AbstractModel):
    """描述实例机型配额信息。

    """

    def __init__(self):
        r"""
        :param Zone: 可用区。
        :type Zone: str
        :param InstanceType: 实例机型。
        :type InstanceType: str
        :param InstanceChargeType: 实例计费模式。取值范围： <br><li>PREPAID：表示预付费，即包年包月<br><li>POSTPAID_BY_HOUR：表示后付费，即按量计费<br><li>CDHPAID：表示[专用宿主机](https://cloud.tencent.com/document/product/416)付费，即只对`专用宿主机`计费，不对`专用宿主机`上的实例计费。<br><li>`SPOTPAID`：表示竞价实例付费。
        :type InstanceChargeType: str
        :param NetworkCard: 网卡类型，例如：25代表25G网卡
        :type NetworkCard: int
        :param Externals: 扩展属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param Cpu: 实例的CPU核数，单位：核。
        :type Cpu: int
        :param Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param TypeName: 机型名称。
        :type TypeName: str
        :param LocalDiskTypeList: 本地磁盘规格列表。当该参数返回为空值时，表示当前情况下无法创建本地盘。
        :type LocalDiskTypeList: list of LocalDiskType
        :param Status: 实例是否售卖。取值范围： <br><li>SELL：表示实例可购买<br><li>SOLD_OUT：表示实例已售罄。
        :type Status: str
        :param Price: 实例的售卖价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param SoldOutReason: 售罄原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type SoldOutReason: str
        :param InstanceBandwidth: 内网带宽，单位Gbps。
        :type InstanceBandwidth: float
        :param InstancePps: 网络收发包能力，单位万PPS。
        :type InstancePps: int
        :param StorageBlockAmount: 本地存储块数量。
        :type StorageBlockAmount: int
        :param CpuType: 处理器型号。
        :type CpuType: str
        :param Gpu: 实例的GPU数量。
        :type Gpu: int
        :param Fpga: 实例的FPGA数量。
        :type Fpga: int
        :param Remark: 实例备注信息。
        :type Remark: str
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceChargeType = None
        self.NetworkCard = None
        self.Externals = None
        self.Cpu = None
        self.Memory = None
        self.InstanceFamily = None
        self.TypeName = None
        self.LocalDiskTypeList = None
        self.Status = None
        self.Price = None
        self.SoldOutReason = None
        self.InstanceBandwidth = None
        self.InstancePps = None
        self.StorageBlockAmount = None
        self.CpuType = None
        self.Gpu = None
        self.Fpga = None
        self.Remark = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.InstanceFamily = params.get("InstanceFamily")
        self.TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self.LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self.LocalDiskTypeList.append(obj)
        self.Status = params.get("Status")
        if params.get("Price") is not None:
            self.Price = ItemPrice()
            self.Price._deserialize(params.get("Price"))
        self.SoldOutReason = params.get("SoldOutReason")
        self.InstanceBandwidth = params.get("InstanceBandwidth")
        self.InstancePps = params.get("InstancePps")
        self.StorageBlockAmount = params.get("StorageBlockAmount")
        self.CpuType = params.get("CpuType")
        self.Gpu = params.get("Gpu")
        self.Fpga = params.get("Fpga")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param InternetChargeType: 网络计费类型。取值范围：<br><li>BANDWIDTH_PREPAID：预付费按带宽结算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费<br><li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费<br><li>BANDWIDTH_PACKAGE：带宽包用户<br>默认取值：非带宽包用户默认与子机付费类型保持一致。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](https://cloud.tencent.com/document/product/213/12523)。
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: 是否分配公网IP。取值范围：<br><li>TRUE：表示分配公网IP<br><li>FALSE：表示不分配公网IP<br><br>当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。该参数仅在RunInstances接口中作为入参使用。
        :type PublicIpAssigned: bool
        :param BandwidthPackageId: 带宽包ID。可通过[`DescribeBandwidthPackages`](https://cloud.tencent.com/document/api/215/19209)接口返回值中的`BandwidthPackageId`获取。该参数仅在RunInstances接口中作为入参使用。
        :type BandwidthPackageId: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetBandwidthConfig(AbstractModel):
    """描述了按带宽计费的相关信息

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type StartTime: str
        :param EndTime: 结束时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type EndTime: str
        :param InternetAccessible: 实例带宽信息。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        """
        self.StartTime = None
        self.EndTime = None
        self.InternetAccessible = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetChargeTypeConfig(AbstractModel):
    """描述了网络计费

    """

    def __init__(self):
        r"""
        :param InternetChargeType: 网络计费模式。
        :type InternetChargeType: str
        :param Description: 网络计费模式描述信息。
        :type Description: str
        """
        self.InternetChargeType = None
        self.Description = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """描述了单项的价格信息

    """

    def __init__(self):
        r"""
        :param UnitPrice: 后续合计费用的原价，后付费模式使用，单位：元。<br><li>如返回了其他时间区间项，如UnitPriceSecondStep，则本项代表时间区间在(0, 96)小时；若未返回其他时间区间项，则本项代表全时段，即(0, ∞)小时
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param ChargeUnit: 后续计价单元，后付费模式使用，可取值范围： <br><li>HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）：<br><li>GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param OriginalPrice: 预支合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param DiscountPrice: 预支合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param Discount: 折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param UnitPriceDiscount: 后续合计费用的折扣价，后付费模式使用，单位：元<br><li>如返回了其他时间区间项，如UnitPriceDiscountSecondStep，则本项代表时间区间在(0, 96)小时；若未返回其他时间区间项，则本项代表全时段，即(0, ∞)小时
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param UnitPriceSecondStep: 使用时间区间在(96, 360)小时的后续合计费用的原价，后付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceSecondStep: float
        :param UnitPriceDiscountSecondStep: 使用时间区间在(96, 360)小时的后续合计费用的折扣价，后付费模式使用，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountSecondStep: float
        :param UnitPriceThirdStep: 使用时间区间在(360, ∞)小时的后续合计费用的原价，后付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceThirdStep: float
        :param UnitPriceDiscountThirdStep: 使用时间区间在(360, ∞)小时的后续合计费用的折扣价，后付费模式使用，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountThirdStep: float
        :param OriginalPriceThreeYear: 预支三年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceThreeYear: float
        :param DiscountPriceThreeYear: 预支三年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceThreeYear: float
        :param DiscountThreeYear: 预支三年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountThreeYear: float
        :param OriginalPriceFiveYear: 预支五年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceFiveYear: float
        :param DiscountPriceFiveYear: 预支五年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceFiveYear: float
        :param DiscountFiveYear: 预支五年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountFiveYear: float
        :param OriginalPriceOneYear: 预支一年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceOneYear: float
        :param DiscountPriceOneYear: 预支一年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceOneYear: float
        :param DiscountOneYear: 预支一年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountOneYear: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.Discount = None
        self.UnitPriceDiscount = None
        self.UnitPriceSecondStep = None
        self.UnitPriceDiscountSecondStep = None
        self.UnitPriceThirdStep = None
        self.UnitPriceDiscountThirdStep = None
        self.OriginalPriceThreeYear = None
        self.DiscountPriceThreeYear = None
        self.DiscountThreeYear = None
        self.OriginalPriceFiveYear = None
        self.DiscountPriceFiveYear = None
        self.DiscountFiveYear = None
        self.OriginalPriceOneYear = None
        self.DiscountPriceOneYear = None
        self.DiscountOneYear = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.Discount = params.get("Discount")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")
        self.UnitPriceSecondStep = params.get("UnitPriceSecondStep")
        self.UnitPriceDiscountSecondStep = params.get("UnitPriceDiscountSecondStep")
        self.UnitPriceThirdStep = params.get("UnitPriceThirdStep")
        self.UnitPriceDiscountThirdStep = params.get("UnitPriceDiscountThirdStep")
        self.OriginalPriceThreeYear = params.get("OriginalPriceThreeYear")
        self.DiscountPriceThreeYear = params.get("DiscountPriceThreeYear")
        self.DiscountThreeYear = params.get("DiscountThreeYear")
        self.OriginalPriceFiveYear = params.get("OriginalPriceFiveYear")
        self.DiscountPriceFiveYear = params.get("DiscountPriceFiveYear")
        self.DiscountFiveYear = params.get("DiscountFiveYear")
        self.OriginalPriceOneYear = params.get("OriginalPriceOneYear")
        self.DiscountPriceOneYear = params.get("DiscountPriceOneYear")
        self.DiscountOneYear = params.get("DiscountOneYear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """描述密钥对信息

    """

    def __init__(self):
        r"""
        :param KeyId: 密钥对的`ID`，是密钥对的唯一标识。
        :type KeyId: str
        :param KeyName: 密钥对名称。
        :type KeyName: str
        :param ProjectId: 密钥对所属的项目`ID`。
        :type ProjectId: int
        :param Description: 密钥对描述信息。
        :type Description: str
        :param PublicKey: 密钥对的纯文本公钥。
        :type PublicKey: str
        :param PrivateKey: 密钥对的纯文本私钥。腾讯云不会保管私钥，请用户自行妥善保存。
        :type PrivateKey: str
        :param AssociatedInstanceIds: 密钥关联的实例`ID`列表。
        :type AssociatedInstanceIds: list of str
        :param CreatedTime: 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param Tags: 密钥关联的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.KeyId = None
        self.KeyName = None
        self.ProjectId = None
        self.Description = None
        self.PublicKey = None
        self.PrivateKey = None
        self.AssociatedInstanceIds = None
        self.CreatedTime = None
        self.Tags = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.Description = params.get("Description")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self.CreatedTime = params.get("CreatedTime")
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
        


class LaunchTemplate(AbstractModel):
    """实例启动模板，通过该参数可使用实例模板中的预设参数创建实例。

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: 实例启动模板ID，通过该参数可使用实例模板中的预设参数创建实例。
        :type LaunchTemplateId: str
        :param LaunchTemplateVersion: 实例启动模板版本号，若给定，新实例启动模板将基于给定的版本号创建
        :type LaunchTemplateVersion: int
        """
        self.LaunchTemplateId = None
        self.LaunchTemplateVersion = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateInfo(AbstractModel):
    """实例启动模板简要信息。

    """

    def __init__(self):
        r"""
        :param LatestVersionNumber: 实例启动模版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersionNumber: int
        :param LaunchTemplateId: 实例启动模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateId: str
        :param LaunchTemplateName: 实例启动模板名。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateName: str
        :param DefaultVersionNumber: 实例启动模板默认版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultVersionNumber: int
        :param LaunchTemplateVersionCount: 实例启动模板包含的版本总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateVersionCount: int
        :param CreatedBy: 创建该模板的用户UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedBy: str
        :param CreationTime: 创建该模板的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        """
        self.LatestVersionNumber = None
        self.LaunchTemplateId = None
        self.LaunchTemplateName = None
        self.DefaultVersionNumber = None
        self.LaunchTemplateVersionCount = None
        self.CreatedBy = None
        self.CreationTime = None


    def _deserialize(self, params):
        self.LatestVersionNumber = params.get("LatestVersionNumber")
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateName = params.get("LaunchTemplateName")
        self.DefaultVersionNumber = params.get("DefaultVersionNumber")
        self.LaunchTemplateVersionCount = params.get("LaunchTemplateVersionCount")
        self.CreatedBy = params.get("CreatedBy")
        self.CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionData(AbstractModel):
    """实例启动模板版本信息

    """

    def __init__(self):
        r"""
        :param Placement: 实例所在的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param InstanceType: 实例机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param InstanceName: 实例名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param InstanceChargeType: 实例计费模式。取值范围：<br><li>`PREPAID`：表示预付费，即包年包月<br><li>`POSTPAID_BY_HOUR`：表示后付费，即按量计费<br><li>`CDHPAID`：`专用宿主机`付费，即只对`专用宿主机`计费，不对`专用宿主机`上的实例计费。<br><li>`SPOTPAID`：表示竞价实例付费。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param SystemDisk: 实例系统盘信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 实例数据盘信息。只包含随实例购买的数据盘。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 实例带宽信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param VirtualPrivateCloud: 实例所属虚拟私有网络信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ImageId: 生产实例所使用的镜像`ID`。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param LoginSettings: 实例登录设置。目前只返回实例所关联的密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param CamRoleName: CAM角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type CamRoleName: str
        :param HpcClusterId: 高性能计算集群`ID`。
注意：此字段可能返回 null，表示取不到有效值。
        :type HpcClusterId: str
        :param InstanceCount: 购买实例数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param EnhancedService: 增强服务。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserData: str
        :param DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisasterRecoverGroupIds: list of str
        :param ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param HostName: 云服务器的主机名。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param ClientToken: 用于保证请求幂等性的字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的云服务器、云硬盘实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: list of TagSpecification
        """
        self.Placement = None
        self.InstanceType = None
        self.InstanceName = None
        self.InstanceChargeType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.VirtualPrivateCloud = None
        self.ImageId = None
        self.SecurityGroupIds = None
        self.LoginSettings = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.InstanceCount = None
        self.EnhancedService = None
        self.UserData = None
        self.DisasterRecoverGroupIds = None
        self.ActionTimer = None
        self.InstanceMarketOptions = None
        self.HostName = None
        self.ClientToken = None
        self.InstanceChargePrepaid = None
        self.TagSpecification = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceType = params.get("InstanceType")
        self.InstanceName = params.get("InstanceName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ImageId = params.get("ImageId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        self.InstanceCount = params.get("InstanceCount")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.UserData = params.get("UserData")
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.HostName = params.get("HostName")
        self.ClientToken = params.get("ClientToken")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionInfo(AbstractModel):
    """实例启动模板版本集合

    """

    def __init__(self):
        r"""
        :param LaunchTemplateVersion: 实例启动模板版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateVersion: int
        :param LaunchTemplateVersionData: 实例启动模板版本数据详情。
        :type LaunchTemplateVersionData: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplateVersionData`
        :param CreationTime: 实例启动模板版本创建时间。
        :type CreationTime: str
        :param LaunchTemplateId: 实例启动模板ID。
        :type LaunchTemplateId: str
        :param IsDefaultVersion: 是否为默认启动模板版本。
        :type IsDefaultVersion: bool
        :param LaunchTemplateVersionDescription: 实例启动模板版本描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateVersionDescription: str
        :param CreatedBy: 创建者。
        :type CreatedBy: str
        """
        self.LaunchTemplateVersion = None
        self.LaunchTemplateVersionData = None
        self.CreationTime = None
        self.LaunchTemplateId = None
        self.IsDefaultVersion = None
        self.LaunchTemplateVersionDescription = None
        self.CreatedBy = None


    def _deserialize(self, params):
        self.LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        if params.get("LaunchTemplateVersionData") is not None:
            self.LaunchTemplateVersionData = LaunchTemplateVersionData()
            self.LaunchTemplateVersionData._deserialize(params.get("LaunchTemplateVersionData"))
        self.CreationTime = params.get("CreationTime")
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        self.LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self.CreatedBy = params.get("CreatedBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskType(AbstractModel):
    """本地磁盘规格

    """

    def __init__(self):
        r"""
        :param Type: 本地磁盘类型。
        :type Type: str
        :param PartitionType: 本地磁盘属性。
        :type PartitionType: str
        :param MinSize: 本地磁盘最小值。
        :type MinSize: int
        :param MaxSize: 本地磁盘最大值。
        :type MaxSize: int
        :param Required: 购买时本地盘是否为必选。取值范围：<br><li>REQUIRED：表示必选<br><li>OPTIONAL：表示可选。
        :type Required: str
        """
        self.Type = None
        self.PartitionType = None
        self.MinSize = None
        self.MaxSize = None
        self.Required = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PartitionType = params.get("PartitionType")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        r"""
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口[DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699)获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeRequest(AbstractModel):
    """ModifyChcAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC物理服务器ID。
        :type ChcIds: list of str
        :param InstanceName: CHC物理服务器名称
        :type InstanceName: str
        :param DeviceType: 服务器类型
        :type DeviceType: str
        :param BmcUser: 合法字符为字母,数字, 横线和下划线
        :type BmcUser: str
        :param Password: 密码8-16位字符, 允许数字，字母， 和特殊字符()`~!@#$%^&*-+=_|{}[]:;'<>,.?/
        :type Password: str
        :param BmcSecurityGroupIds: bmc网络的安全组列表
        :type BmcSecurityGroupIds: list of str
        """
        self.ChcIds = None
        self.InstanceName = None
        self.DeviceType = None
        self.BmcUser = None
        self.Password = None
        self.BmcSecurityGroupIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        self.InstanceName = params.get("InstanceName")
        self.DeviceType = params.get("DeviceType")
        self.BmcUser = params.get("BmcUser")
        self.Password = params.get("Password")
        self.BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeResponse(AbstractModel):
    """ModifyChcAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDisasterRecoverGroupAttributeRequest(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupId: 分散置放群组ID，可使用[DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810)接口获取。
        :type DisasterRecoverGroupId: str
        :param Name: 分散置放群组名称，长度1-60个字符，支持中、英文。
        :type Name: str
        """
        self.DisasterRecoverGroupId = None
        self.Name = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisasterRecoverGroupAttributeResponse(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHostsAttributeRequest(AbstractModel):
    """ModifyHostsAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param HostIds: 一个或多个待操作的CDH实例ID。
        :type HostIds: list of str
        :param HostName: CDH实例显示名称。可任意命名，但不得超过60个字符。
        :type HostName: str
        :param RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param ProjectId: 项目ID。项目可以使用[AddProject](https://cloud.tencent.com/doc/api/403/4398)接口创建。可通过[`DescribeProject`](https://cloud.tencent.com/document/product/378/4400) API返回值中的`projectId`获取。后续使用[DescribeHosts](https://cloud.tencent.com/document/api/213/16474)接口查询实例时，项目ID可用于过滤结果。
        :type ProjectId: int
        """
        self.HostIds = None
        self.HostName = None
        self.RenewFlag = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.HostIds = params.get("HostIds")
        self.HostName = params.get("HostName")
        self.RenewFlag = params.get("RenewFlag")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsAttributeResponse(AbstractModel):
    """ModifyHostsAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像ID，形如`img-gvbnzy6f`。镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。
        :type ImageId: str
        :param ImageName: 设置新的镜像名称；必须满足下列限制：<br> <li> 不得超过20个字符。<br> <li> 镜像名称不能与已有镜像重复。
        :type ImageName: str
        :param ImageDescription: 设置新的镜像描述；必须满足下列限制：<br> <li> 不得超过60个字符。
        :type ImageDescription: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSharePermissionRequest(AbstractModel):
    """ModifyImageSharePermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageId: 镜像ID，形如`img-gvbnzy6f`。镜像Id可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。 <br>镜像ID必须指定为状态为`NORMAL`的镜像。镜像状态请参考[镜像数据表](https://cloud.tencent.com/document/product/213/15753#Image)。
        :type ImageId: str
        :param AccountIds: 接收分享镜像的账号Id列表，array型参数的格式可以参考[API简介](/document/api/213/568)。帐号ID不同于QQ号，查询用户帐号ID请查看[帐号信息](https://console.cloud.tencent.com/developer)中的帐号ID栏。
        :type AccountIds: list of str
        :param Permission: 操作，包括 `SHARE`，`CANCEL`。其中`SHARE`代表分享操作，`CANCEL`代表取消分享操作。
        :type Permission: str
        """
        self.ImageId = None
        self.AccountIds = None
        self.Permission = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.AccountIds = params.get("AccountIds")
        self.Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSharePermissionResponse(AbstractModel):
    """ModifyImageSharePermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceDiskTypeRequest(AbstractModel):
    """ModifyInstanceDiskType请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param DataDisks: 实例数据盘配置信息，只需要指定要转换的目标云硬盘的介质类型，指定DiskType的值，当前只支持一个数据盘转化。只支持CDHPAID类型实例指定CdcId参数。
        :type DataDisks: list of DataDisk
        :param SystemDisk: 实例系统盘配置信息，只需要指定要转换的目标云硬盘的介质类型，指定DiskType的值。只支持CDHPAID类型实例指定CdcId参数。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        """
        self.InstanceId = None
        self.DataDisks = None
        self.SystemDisk = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceDiskTypeResponse(AbstractModel):
    """ModifyInstanceDiskType返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param InstanceName: 实例名称。可任意命名，但不得超过60个字符。
<dx-alert infotype="explain" title="">必须指定InstanceName与SecurityGroups的其中一个，但不能同时设置</dx-alert>
        :type InstanceName: str
        :param SecurityGroups: 指定实例的安全组Id列表，子机将重新关联指定列表的安全组，原本关联的安全组会被解绑。<dx-alert infotype="explain" title="">必须指定SecurityGroups与InstanceName的其中一个，但不能同时设置</dx-alert>
        :type SecurityGroups: list of str
        :param CamRoleName: 给实例绑定用户角色，传空值为解绑操作
        :type CamRoleName: str
        :param DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>TRUE：表示开启实例保护，不允许通过api接口删除实例<br><li>FALSE：表示关闭实例保护，允许通过api接口删除实例<br><br>默认取值：FALSE。
        :type DisableApiTermination: bool
        :param CamRoleType: 角色类别，与CamRoleName搭配使用，该值可从CAM DescribeRoleList, GetRole接口返回RoleType字段获取，当前只接受user、system和service_linked三种类别。
举例：一般CamRoleName中包含“LinkedRoleIn”（如TKE_QCSLinkedRoleInPrometheusService）时，DescribeRoleList和GetRole返回的RoleType为service_linked，则本参数也需要传递service_linked。
该参数默认值为user，若CameRoleName为非service_linked类型，本参数可不传递。
        :type CamRoleType: str
        """
        self.InstanceIds = None
        self.InstanceName = None
        self.SecurityGroups = None
        self.CamRoleName = None
        self.DisableApiTermination = None
        self.CamRoleType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroups = params.get("SecurityGroups")
        self.CamRoleName = params.get("CamRoleName")
        self.DisableApiTermination = params.get("DisableApiTermination")
        self.CamRoleType = params.get("CamRoleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesChargeTypeRequest(AbstractModel):
    """ModifyInstancesChargeType请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为30。
        :type InstanceIds: list of str
        :param InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月。<br><li>POSTPAID_BY_HOUR：后付费，即按量付费。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。<dx-alert infotype="explain" title="">若指定实例的付费模式为预付费则该参数必传。</dx-alert>
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param ModifyPortableDataDisk: 是否同时切换弹性数据云盘计费模式。取值范围：<br><li>TRUE：表示切换弹性数据云盘计费模式<br><li>FALSE：表示不切换弹性数据云盘计费模式<br><br>默认取值：FALSE。
        :type ModifyPortableDataDisk: bool
        """
        self.InstanceIds = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.ModifyPortableDataDisk = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.ModifyPortableDataDisk = params.get("ModifyPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesChargeTypeResponse(AbstractModel):
    """ModifyInstancesChargeType返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesProjectRequest(AbstractModel):
    """ModifyInstancesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param ProjectId: 项目ID。项目可以使用[AddProject](https://cloud.tencent.com/doc/api/403/4398)接口创建。可通过[`DescribeProject`](https://cloud.tencent.com/document/product/378/4400) API返回值中的`projectId`获取。后续使用[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口查询实例时，项目ID可用于过滤结果。
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesProjectResponse(AbstractModel):
    """ModifyInstancesProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesRenewFlagRequest(AbstractModel):
    """ModifyInstancesRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self.InstanceIds = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesRenewFlagResponse(AbstractModel):
    """ModifyInstancesRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesVpcAttributeRequest(AbstractModel):
    """ModifyInstancesVpcAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 待操作的实例ID数组。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。
        :type InstanceIds: list of str
        :param VirtualPrivateCloud: 私有网络相关信息配置，通过该参数指定私有网络的ID，子网ID，私有网络ip等信息。<br><li>当指定私有网络ID和子网ID（子网必须在实例所在的可用区）与指定实例所在私有网络不一致时，会将实例迁移至指定的私有网络的子网下。<br><li>可通过`PrivateIpAddresses`指定私有网络子网IP，若需指定则所有已指定的实例均需要指定子网IP，此时`InstanceIds`与`PrivateIpAddresses`一一对应。<br><li>不指定`PrivateIpAddresses`时随机分配私有网络子网IP。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ForceStop: 是否对运行中的实例选择强制关机。默认为TRUE。
        :type ForceStop: bool
        :param ReserveHostName: 是否保留主机名。默认为FALSE。
        :type ReserveHostName: bool
        """
        self.InstanceIds = None
        self.VirtualPrivateCloud = None
        self.ForceStop = None
        self.ReserveHostName = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ForceStop = params.get("ForceStop")
        self.ReserveHostName = params.get("ReserveHostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesVpcAttributeResponse(AbstractModel):
    """ModifyInstancesVpcAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyKeyPairAttributeRequest(AbstractModel):
    """ModifyKeyPairAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyId: 密钥对ID，密钥对ID形如：`skey-xxxxxxxx`。<br><br>可以通过以下方式获取可用的密钥 ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥 ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/9403) ，取返回信息中的 `KeyId` 获取密钥对 ID。
        :type KeyId: str
        :param KeyName: 修改后的密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :type KeyName: str
        :param Description: 修改后的密钥对描述信息。可任意命名，但不得超过60个字符。
        :type Description: str
        """
        self.KeyId = None
        self.KeyName = None
        self.Description = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKeyPairAttributeResponse(AbstractModel):
    """ModifyKeyPairAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLaunchTemplateDefaultVersionRequest(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        :param DefaultVersion: 待设置的默认版本号。
        :type DefaultVersion: int
        """
        self.LaunchTemplateId = None
        self.DefaultVersion = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLaunchTemplateDefaultVersionResponse(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OperationCountLimit(AbstractModel):
    """描述了单台实例操作次数限制

    """

    def __init__(self):
        r"""
        :param Operation: 实例操作。取值范围：<br><li>`INSTANCE_DEGRADE`：降配操作<br><li>`INTERNET_CHARGE_TYPE_CHANGE`：修改网络带宽计费模式
        :type Operation: str
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param CurrentCount: 当前已使用次数，如果返回值为-1表示该操作无次数限制。
        :type CurrentCount: int
        :param LimitCount: 操作次数最高额度，如果返回值为-1表示该操作无次数限制，如果返回值为0表示不支持调整配置。
        :type LimitCount: int
        """
        self.Operation = None
        self.InstanceId = None
        self.CurrentCount = None
        self.LimitCount = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.InstanceId = params.get("InstanceId")
        self.CurrentCount = params.get("CurrentCount")
        self.LimitCount = params.get("LimitCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """操作系统支持的类型。

    """

    def __init__(self):
        r"""
        :param OsName: 操作系统类型
        :type OsName: str
        :param OsVersions: 支持的操作系统版本
        :type OsVersions: list of str
        :param Architecture: 支持的操作系统架构
        :type Architecture: list of str
        """
        self.OsName = None
        self.OsVersions = None
        self.Architecture = None


    def _deserialize(self, params):
        self.OsName = params.get("OsName")
        self.OsVersions = params.get("OsVersions")
        self.Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目，宿主机（仅专用宿主机产品可用），母机ip等

    """

    def __init__(self):
        r"""
        :param Zone: 实例所属的可用区ID。该参数可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param HostIds: 实例所属的专用宿主机ID列表，仅用于入参。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。
        :type HostIds: list of str
        :param HostIps: 指定母机ip生产子机
        :type HostIps: list of str
        :param HostId: 实例所属的专用宿主机ID，仅用于出参。
        :type HostId: str
        """
        self.Zone = None
        self.ProjectId = None
        self.HostIds = None
        self.HostIps = None
        self.HostId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.HostIds = params.get("HostIds")
        self.HostIps = params.get("HostIps")
        self.HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostPaidQuota(AbstractModel):
    """后付费实例配额

    """

    def __init__(self):
        r"""
        :param UsedQuota: 累计已使用配额
        :type UsedQuota: int
        :param RemainingQuota: 剩余配额
        :type RemainingQuota: int
        :param TotalQuota: 总配额
        :type TotalQuota: int
        :param Zone: 可用区
        :type Zone: str
        """
        self.UsedQuota = None
        self.RemainingQuota = None
        self.TotalQuota = None
        self.Zone = None


    def _deserialize(self, params):
        self.UsedQuota = params.get("UsedQuota")
        self.RemainingQuota = params.get("RemainingQuota")
        self.TotalQuota = params.get("TotalQuota")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrePaidQuota(AbstractModel):
    """预付费实例配额

    """

    def __init__(self):
        r"""
        :param UsedQuota: 当月已使用配额
        :type UsedQuota: int
        :param OnceQuota: 单次购买最大数量
        :type OnceQuota: int
        :param RemainingQuota: 剩余配额
        :type RemainingQuota: int
        :param TotalQuota: 总配额
        :type TotalQuota: int
        :param Zone: 可用区
        :type Zone: str
        """
        self.UsedQuota = None
        self.OnceQuota = None
        self.RemainingQuota = None
        self.TotalQuota = None
        self.Zone = None


    def _deserialize(self, params):
        self.UsedQuota = params.get("UsedQuota")
        self.OnceQuota = params.get("OnceQuota")
        self.RemainingQuota = params.get("RemainingQuota")
        self.TotalQuota = params.get("TotalQuota")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """价格

    """

    def __init__(self):
        r"""
        :param InstancePrice: 描述了实例价格。
        :type InstancePrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param BandwidthPrice: 描述了网络价格。
        :type BandwidthPrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramFpgaImageRequest(AbstractModel):
    """ProgramFpgaImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例的ID信息。
        :type InstanceId: str
        :param FPGAUrl: FPGA镜像文件的COS URL地址。
        :type FPGAUrl: str
        :param DBDFs: 实例上FPGA卡的DBDF号，不填默认烧录FPGA镜像到实例所拥有的所有FPGA卡。
        :type DBDFs: list of str
        :param DryRun: 试运行，不会执行实际的烧录动作，默认为False。
        :type DryRun: bool
        """
        self.InstanceId = None
        self.FPGAUrl = None
        self.DBDFs = None
        self.DryRun = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FPGAUrl = params.get("FPGAUrl")
        self.DBDFs = params.get("DBDFs")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramFpgaImageResponse(AbstractModel):
    """ProgramFpgaImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PurchaseReservedInstancesOfferingRequest(AbstractModel):
    """PurchaseReservedInstancesOffering请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceCount: 购买预留实例计费数量
        :type InstanceCount: int
        :param ReservedInstancesOfferingId: 预留实例计费配置ID
        :type ReservedInstancesOfferingId: str
        :param DryRun: 试运行
        :type DryRun: bool
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性
        :type ClientToken: str
        :param ReservedInstanceName: 预留实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>最多支持60个字符（包含模式串）。</li>
        :type ReservedInstanceName: str
        """
        self.InstanceCount = None
        self.ReservedInstancesOfferingId = None
        self.DryRun = None
        self.ClientToken = None
        self.ReservedInstanceName = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.DryRun = params.get("DryRun")
        self.ClientToken = params.get("ClientToken")
        self.ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurchaseReservedInstancesOfferingResponse(AbstractModel):
    """PurchaseReservedInstancesOffering返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReservedInstanceId: 已购买预留实例计费ID
        :type ReservedInstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReservedInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedInstanceId = params.get("ReservedInstanceId")
        self.RequestId = params.get("RequestId")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param ForceReboot: 本参数已弃用，推荐使用StopType，不可以与参数StopType同时使用。表示是否在正常重启失败后选择强制重启实例。取值范围：<br><li>TRUE：表示在正常重启失败后进行强制重启<br><li>FALSE：表示在正常重启失败后不进行强制重启<br><br>默认取值：FALSE。
        :type ForceReboot: bool
        :param StopType: 关机类型。取值范围：<br><li>SOFT：表示软关机<br><li>HARD：表示硬关机<br><li>SOFT_FIRST：表示优先软关机，失败再执行硬关机<br><br>默认取值：SOFT。
        :type StopType: str
        """
        self.InstanceIds = None
        self.ForceReboot = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ForceReboot = params.get("ForceReboot")
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param Region: 地域名称，例如，ap-guangzhou
        :type Region: str
        :param RegionName: 地域描述，例如，华南地区(广州)
        :type RegionName: str
        :param RegionState: 地域是否可用状态
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcRequest(AbstractModel):
    """RemoveChcAssistVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC物理服务器Id。
        :type ChcIds: list of str
        """
        self.ChcIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcResponse(AbstractModel):
    """RemoveChcAssistVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveChcDeployVpcRequest(AbstractModel):
    """RemoveChcDeployVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC物理服务器Id。
        :type ChcIds: list of str
        """
        self.ChcIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcDeployVpcResponse(AbstractModel):
    """RemoveChcDeployVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewHostsRequest(AbstractModel):
    """RenewHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param HostIds: 一个或多个待操作的CDH实例ID。每次请求的CDH实例的上限为100。
        :type HostIds: list of str
        :param HostChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type HostChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.ChargePrepaid`
        """
        self.HostIds = None
        self.HostChargePrepaid = None


    def _deserialize(self, params):
        self.HostIds = params.get("HostIds")
        if params.get("HostChargePrepaid") is not None:
            self.HostChargePrepaid = ChargePrepaid()
            self.HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewHostsResponse(AbstractModel):
    """RenewHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewInstancesRequest(AbstractModel):
    """RenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。<dx-alert infotype="explain" title="">
包年包月实例该参数为必传参数。</dx-alert>
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param RenewPortableDataDisk: 是否续费弹性数据盘。取值范围：<br><li>TRUE：表示续费包年包月实例同时续费其挂载的弹性数据盘<br><li>FALSE：表示续费包年包月实例同时不再续费其挂载的弹性数据盘<br><br>默认取值：TRUE。
        :type RenewPortableDataDisk: bool
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None
        self.RenewPortableDataDisk = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.RenewPortableDataDisk = params.get("RenewPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstancesResponse(AbstractModel):
    """RenewInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReservedInstanceConfigInfoItem(AbstractModel):
    """预留实例静态配置信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param Type: 实例规格。
        :type Type: str
        :param TypeName: 实例规格名称。
        :type TypeName: str
        :param Order: 优先级。
        :type Order: int
        :param InstanceFamilies: 实例族信息列表。
        :type InstanceFamilies: list of ReservedInstanceFamilyItem
        """
        self.Type = None
        self.TypeName = None
        self.Order = None
        self.InstanceFamilies = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        self.Order = params.get("Order")
        if params.get("InstanceFamilies") is not None:
            self.InstanceFamilies = []
            for item in params.get("InstanceFamilies"):
                obj = ReservedInstanceFamilyItem()
                obj._deserialize(item)
                self.InstanceFamilies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceFamilyItem(AbstractModel):
    """预留实例相关实例族信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param InstanceFamily: 实例族。
        :type InstanceFamily: str
        :param Order: 优先级。
        :type Order: int
        :param InstanceTypes: 实例类型信息列表。
        :type InstanceTypes: list of ReservedInstanceTypeItem
        """
        self.InstanceFamily = None
        self.Order = None
        self.InstanceTypes = None


    def _deserialize(self, params):
        self.InstanceFamily = params.get("InstanceFamily")
        self.Order = params.get("Order")
        if params.get("InstanceTypes") is not None:
            self.InstanceTypes = []
            for item in params.get("InstanceTypes"):
                obj = ReservedInstanceTypeItem()
                obj._deserialize(item)
                self.InstanceTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePrice(AbstractModel):
    """预留实例相关价格信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param OriginalFixedPrice: 预支合计费用的原价，单位：元。
        :type OriginalFixedPrice: float
        :param DiscountFixedPrice: 预支合计费用的折扣价，单位：元。
        :type DiscountFixedPrice: float
        :param OriginalUsagePrice: 后续合计费用的原价，单位：元/小时
        :type OriginalUsagePrice: float
        :param DiscountUsagePrice: 后续合计费用的折扣价，单位：元/小时
        :type DiscountUsagePrice: float
        """
        self.OriginalFixedPrice = None
        self.DiscountFixedPrice = None
        self.OriginalUsagePrice = None
        self.DiscountUsagePrice = None


    def _deserialize(self, params):
        self.OriginalFixedPrice = params.get("OriginalFixedPrice")
        self.DiscountFixedPrice = params.get("DiscountFixedPrice")
        self.OriginalUsagePrice = params.get("OriginalUsagePrice")
        self.DiscountUsagePrice = params.get("DiscountUsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePriceItem(AbstractModel):
    """基于付费类型的预留实例相关价格信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param OfferingType: 付费类型，如："All Upfront","Partial Upfront","No Upfront"
        :type OfferingType: str
        :param FixedPrice: 预支合计费用，单位：元。
        :type FixedPrice: float
        :param UsagePrice: 后续合计费用，单位：元/小时
        :type UsagePrice: float
        :param ReservedInstancesOfferingId: 预留实例配置ID
        :type ReservedInstancesOfferingId: str
        :param Zone: 预留实例计费可购买的可用区。
        :type Zone: str
        :param Duration: 预留实例计费【有效期】即预留实例计费购买时长。形如：31536000。
计量单位：秒
        :type Duration: int
        :param ProductDescription: 预留实例计费的平台描述（即操作系统）。形如：linux。
返回项： linux 。
        :type ProductDescription: str
        """
        self.OfferingType = None
        self.FixedPrice = None
        self.UsagePrice = None
        self.ReservedInstancesOfferingId = None
        self.Zone = None
        self.Duration = None
        self.ProductDescription = None


    def _deserialize(self, params):
        self.OfferingType = params.get("OfferingType")
        self.FixedPrice = params.get("FixedPrice")
        self.UsagePrice = params.get("UsagePrice")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.Zone = params.get("Zone")
        self.Duration = params.get("Duration")
        self.ProductDescription = params.get("ProductDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceTypeItem(AbstractModel):
    """预留实例类型信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param InstanceType: 实例类型。
        :type InstanceType: str
        :param Cpu: CPU核数。
        :type Cpu: int
        :param Memory: 内存大小。
        :type Memory: int
        :param Gpu: GPU数量。
        :type Gpu: int
        :param Fpga: FPGA数量。
        :type Fpga: int
        :param StorageBlock: 本地存储块数量。
        :type StorageBlock: int
        :param NetworkCard: 网卡数。
        :type NetworkCard: int
        :param MaxBandwidth: 最大带宽。
        :type MaxBandwidth: float
        :param Frequency: 主频。
        :type Frequency: str
        :param CpuModelName: CPU型号名称。
        :type CpuModelName: str
        :param Pps: 包转发率。
        :type Pps: int
        :param Externals: 外部信息。
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param Remark: 备注信息。
        :type Remark: str
        :param Prices: 预留实例配置价格信息。
        :type Prices: list of ReservedInstancePriceItem
        """
        self.InstanceType = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.Fpga = None
        self.StorageBlock = None
        self.NetworkCard = None
        self.MaxBandwidth = None
        self.Frequency = None
        self.CpuModelName = None
        self.Pps = None
        self.Externals = None
        self.Remark = None
        self.Prices = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.Fpga = params.get("Fpga")
        self.StorageBlock = params.get("StorageBlock")
        self.NetworkCard = params.get("NetworkCard")
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.Frequency = params.get("Frequency")
        self.CpuModelName = params.get("CpuModelName")
        self.Pps = params.get("Pps")
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.Remark = params.get("Remark")
        if params.get("Prices") is not None:
            self.Prices = []
            for item in params.get("Prices"):
                obj = ReservedInstancePriceItem()
                obj._deserialize(item)
                self.Prices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstances(AbstractModel):
    """描述用户已购买预留实例计费信息

    """

    def __init__(self):
        r"""
        :param ReservedInstancesId: （此字段已废弃，建议使用字段：ReservedInstanceId）已购买的预留实例计费ID。形如：ri-rtbh4han。
        :type ReservedInstancesId: str
        :param InstanceType: 预留实例计费的规格。形如：S3.MEDIUM4。
返回项：<a href="https://cloud.tencent.com/document/product/213/11518">预留实例计费规格列表</a>
        :type InstanceType: str
        :param Zone: 预留实例计费可购买的可用区。形如：ap-guangzhou-1。
返回项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a>
        :type Zone: str
        :param StartTime: 预留实例计费开始时间。形如：1949-10-01 00:00:00
        :type StartTime: str
        :param EndTime: 预留实例计费到期时间。形如：1949-10-01 00:00:00
        :type EndTime: str
        :param Duration: 预留实例计费【有效期】即预留实例计费购买时长。形如：31536000。
计量单位：秒。
        :type Duration: int
        :param InstanceCount: 已购买的预留实例计费个数。形如：10。
        :type InstanceCount: int
        :param ProductDescription: 描述预留实例计费的平台描述（即操作系统）。形如：linux。
返回项： linux 。
        :type ProductDescription: str
        :param State: 预留实例计费购买的状态。形如：active
返回项： active (以创建) | pending (等待被创建) | retired (过期)。
        :type State: str
        :param CurrencyCode: 可购买的预留实例计费类型的结算货币，使用ISO 4217标准货币代码。形如：USD。
返回项：USD（美元）。
        :type CurrencyCode: str
        :param OfferingType: 预留实例计费的付款类型。形如：All Upfront。
返回项： All Upfront (预付全部费用)。
        :type OfferingType: str
        :param InstanceFamily: 预留实例计费的类型。形如：S3。
返回项：<a href="https://cloud.tencent.com/document/product/213/11518">预留实例计费类型列表</a>
        :type InstanceFamily: str
        :param ReservedInstanceId: 已购买的预留实例计费ID。形如：ri-rtbh4han。
        :type ReservedInstanceId: str
        :param ReservedInstanceName: 预留实例显示名称。形如：riname-01
        :type ReservedInstanceName: str
        """
        self.ReservedInstancesId = None
        self.InstanceType = None
        self.Zone = None
        self.StartTime = None
        self.EndTime = None
        self.Duration = None
        self.InstanceCount = None
        self.ProductDescription = None
        self.State = None
        self.CurrencyCode = None
        self.OfferingType = None
        self.InstanceFamily = None
        self.ReservedInstanceId = None
        self.ReservedInstanceName = None


    def _deserialize(self, params):
        self.ReservedInstancesId = params.get("ReservedInstancesId")
        self.InstanceType = params.get("InstanceType")
        self.Zone = params.get("Zone")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Duration = params.get("Duration")
        self.InstanceCount = params.get("InstanceCount")
        self.ProductDescription = params.get("ProductDescription")
        self.State = params.get("State")
        self.CurrencyCode = params.get("CurrencyCode")
        self.OfferingType = params.get("OfferingType")
        self.InstanceFamily = params.get("InstanceFamily")
        self.ReservedInstanceId = params.get("ReservedInstanceId")
        self.ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancesOffering(AbstractModel):
    """描述可购买预留实例计费信息

    """

    def __init__(self):
        r"""
        :param Zone: 预留实例计费可购买的可用区。形如：ap-guangzhou-1。
返回项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a>
        :type Zone: str
        :param CurrencyCode: 可购买的预留实例计费类型的结算货币，使用ISO 4217标准货币代码。
返回项：USD（美元）。
        :type CurrencyCode: str
        :param Duration: 预留实例计费【有效期】即预留实例计费购买时长。形如：31536000。
计量单位：秒
        :type Duration: int
        :param FixedPrice: 预留实例计费的购买价格。形如：4000.0。
计量单位：与 currencyCode 一致，目前支持 USD（美元）
        :type FixedPrice: float
        :param InstanceType: 预留实例计费的实例类型。形如：S3.MEDIUM4。
返回项：<a href="https://cloud.tencent.com/product/cvm/instances">预留实例计费类型列表</a>
        :type InstanceType: str
        :param OfferingType: 预留实例计费的付款类型。形如：All Upfront。
返回项： All Upfront (预付全部费用)。
        :type OfferingType: str
        :param ReservedInstancesOfferingId: 可购买的预留实例计费配置ID。形如：650c138f-ae7e-4750-952a-96841d6e9fc1。
        :type ReservedInstancesOfferingId: str
        :param ProductDescription: 预留实例计费的平台描述（即操作系统）。形如：linux。
返回项： linux 。
        :type ProductDescription: str
        :param UsagePrice: 扣除预付费之后的使用价格 (按小时计费)。形如：0.0。
目前，因为只支持 All Upfront 付款类型，所以默认为 0元/小时。
计量单位：元/小时，货币单位与 currencyCode 一致，目前支持 USD（美元）
        :type UsagePrice: float
        """
        self.Zone = None
        self.CurrencyCode = None
        self.Duration = None
        self.FixedPrice = None
        self.InstanceType = None
        self.OfferingType = None
        self.ReservedInstancesOfferingId = None
        self.ProductDescription = None
        self.UsagePrice = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.CurrencyCode = params.get("CurrencyCode")
        self.Duration = params.get("Duration")
        self.FixedPrice = params.get("FixedPrice")
        self.InstanceType = params.get("InstanceType")
        self.OfferingType = params.get("OfferingType")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.ProductDescription = params.get("ProductDescription")
        self.UsagePrice = params.get("UsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceRequest(AbstractModel):
    """ResetInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
<br>默认取值：默认使用当前镜像。
        :type ImageId: str
        :param SystemDisk: 实例系统盘配置信息。系统盘为云盘的实例可以通过该参数指定重装后的系统盘大小来实现对系统盘的扩容操作。系统盘大小只支持扩容不支持缩容；重装只支持修改系统盘的大小，不能修改系统盘的类型。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param HostName: 重装系统时，可以指定修改实例的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。
        :type HostName: str
        """
        self.InstanceId = None
        self.ImageId = None
        self.SystemDisk = None
        self.LoginSettings = None
        self.EnhancedService = None
        self.HostName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceResponse(AbstractModel):
    """ResetInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """ResetInstancesInternetMaxBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口返回值中的 `InstanceId` 获取。 每次请求批量实例的上限为100。当调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽时，只支持一个实例。
        :type InstanceIds: list of str
        :param InternetAccessible: 公网出带宽配置。不同机型带宽上限范围不一致，具体限制详见带宽限制对账表。暂时只支持 `InternetMaxBandwidthOut` 参数。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param StartTime: 带宽生效的起始时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始时间不能早于当前时间。如果起始时间是今天则新设置的带宽立即生效。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type StartTime: str
        :param EndTime: 带宽生效的终止时间。格式： `YYYY-MM-DD` ，例如：`2016-10-30` 。新设置的带宽的有效期包含终止时间此日期。终止时间不能晚于包年包月实例的到期时间。实例的到期时间可通过 [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口返回值中的`ExpiredTime`获取。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type EndTime: str
        """
        self.InstanceIds = None
        self.InternetAccessible = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """ResetInstancesInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：
Linux 实例密码必须8-30位，推荐使用12位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字：0-9<br><li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;'<>,.?/
Windows 实例密码必须12\~30位，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字： 0-9<br><li>特殊字符：()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/<br><li>如果实例即包含 `Linux` 实例又包含 `Windows` 实例，则密码复杂度限制按照 `Windows` 实例的限制。
        :type Password: str
        :param UserName: 待重置密码的实例操作系统的用户名。不得超过64个字符。
        :type UserName: str
        :param ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.Password = None
        self.UserName = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Password = params.get("Password")
        self.UserName = params.get("UserName")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesTypeRequest(AbstractModel):
    """ResetInstancesType请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。本接口目前仅支持每次操作1个实例。
        :type InstanceIds: list of str
        :param InstanceType: 实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口[`DescribeInstanceTypeConfigs`](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesTypeResponse(AbstractModel):
    """ResetInstancesType返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeInstanceDisksRequest(AbstractModel):
    """ResizeInstanceDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param DataDisks: 待扩容的数据盘配置信息。只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性），且[数据盘类型](/document/api/213/9452#block_device)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。数据盘容量单位：GB。最小扩容步长：10G。关于数据盘类型的选择请参考[硬盘产品简介](https://cloud.tencent.com/document/product/362/2353)。可选数据盘类型受到实例类型`InstanceType`限制。另外允许扩容的最大容量也因数据盘类型的不同而有所差异。
        :type DataDisks: list of DataDisk
        :param ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>TRUE：表示在正常关机失败后进行强制关机<br><li>FALSE：表示在正常关机失败后不进行强制关机<br><br>默认取值：FALSE。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        :param SystemDisk: 待扩容的系统盘配置信息。只支持扩容云盘。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param ResizeOnline: 扩容云盘的方式是否为在线扩容。
        :type ResizeOnline: bool
        """
        self.InstanceId = None
        self.DataDisks = None
        self.ForceStop = None
        self.SystemDisk = None
        self.ResizeOnline = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.ForceStop = params.get("ForceStop")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        self.ResizeOnline = params.get("ResizeOnline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeInstanceDisksResponse(AbstractModel):
    """ResizeInstanceDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunAutomationServiceEnabled(AbstractModel):
    """描述了 “云自动化助手” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启云自动化助手。取值范围：<br><li>TRUE：表示开启云自动化助手服务<br><li>FALSE：表示不开启云自动化助手服务<br><br>默认取值：FALSE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDHPAID：独享子机（基于专用宿主机创建，宿主机部分的资源不收费）<br><li>SPOTPAID：竞价付费<br><li>CDCPAID：专用集群付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。
 <b>注：如果您不指定LaunchTemplate参数，则Placement为必选参数。若同时传递Placement和LaunchTemplate，则默认覆盖LaunchTemplate中对应的Placement的值。</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param InstanceType: 实例机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则系统将根据当前地域的资源售卖情况动态指定默认机型。<br><li>对于付费模式为CDHPAID的实例创建，该参数以"CDH_"为前缀，根据CPU和内存配置生成，具体形式为：CDH_XCXG，例如对于创建CPU为1核，内存为1G大小的专用宿主机的实例，该参数应该为CDH_1C1G。
        :type InstanceType: str
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，传入InstanceType获取当前机型支持的镜像列表，取返回信息中的`ImageId`字段。</li>
 <b>注：如果您不指定LaunchTemplate参数，则ImageId为必选参数。若同时传递ImageId和LaunchTemplate，则默认覆盖LaunchTemplate中对应的ImageId的值。</b>
        :type ImageId: str
        :param SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若在此参数中指定了私有网络IP，即表示每个实例的主网卡IP；同时，InstanceCount参数必须与私有网络IP的个数一致且不能大于20。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: 购买实例数量。包年包月实例取值范围：[1，300]，按量计费实例取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。
        :type InstanceName: str
        :param LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param HostName: 实例主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。<br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。<br><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。<br><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server{R:3}`，购买1台时，实例主机名为`server3`；购买2台时，实例主机名分别为`server3`，`server4`。支持指定多个模式串`{R:x}`。</li><br><li>购买多台实例，如果不指定模式串，则在实例主机名添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server`，购买2台时，实例主机名分别为`server1`，`server2`。
        :type HostName: str
        :param ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的云服务器、云硬盘实例。
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费但没有传递该参数时，默认按当前固定折扣价格出价。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。
        :type UserData: str
        :param DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param CamRoleName: CAM角色名称。可通过[`DescribeRoleList`](https://cloud.tencent.com/document/product/598/13887)接口返回值中的`roleName`获取。
        :type CamRoleName: str
        :param HpcClusterId: 高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :type HpcClusterId: str
        :param LaunchTemplate: 实例启动模板。
        :type LaunchTemplate: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplate`
        :param DedicatedClusterId: 指定专用集群创建。
        :type DedicatedClusterId: str
        :param ChcIds: 指定CHC物理服务器来创建CHC云主机。
        :type ChcIds: list of str
        :param DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>TRUE：表示开启实例保护，不允许通过api接口删除实例<br><li>FALSE：表示关闭实例保护，允许通过api接口删除实例<br><br>默认取值：FALSE。
        :type DisableApiTermination: bool
        """
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.Placement = None
        self.InstanceType = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.ActionTimer = None
        self.DisasterRecoverGroupIds = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.UserData = None
        self.DryRun = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.LaunchTemplate = None
        self.DedicatedClusterId = None
        self.ChcIds = None
        self.DisableApiTermination = None


    def _deserialize(self, params):
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceType = params.get("InstanceType")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.UserData = params.get("UserData")
        self.DryRun = params.get("DryRun")
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        if params.get("LaunchTemplate") is not None:
            self.LaunchTemplate = LaunchTemplate()
            self.LaunchTemplate._deserialize(params.get("LaunchTemplate"))
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        self.ChcIds = params.get("ChcIds")
        self.DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: 当通过本接口来创建实例时会返回该参数，表示一个或多个实例`ID`。返回实例`ID`列表并不代表实例创建成功，可根据 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口查询返回的InstancesSet中对应实例的`ID`的状态来判断创建是否完成；如果实例状态由“PENDING(创建中)”变为“运行中(RUNNING)”，则为创建成功。
        :type InstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “云监控” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启[云监控](/document/product/248)服务。取值范围：<br><li>TRUE：表示开启云监控服务<br><li>FALSE：表示不开启云监控服务<br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启[云安全](/document/product/296)服务。取值范围：<br><li>TRUE：表示开启云安全服务<br><li>FALSE：表示不开启云安全服务<br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SharePermission(AbstractModel):
    """镜像分享信息结构

    """

    def __init__(self):
        r"""
        :param CreatedTime: 镜像分享时间
        :type CreatedTime: str
        :param AccountId: 镜像分享的账户ID
        :type AccountId: str
        """
        self.CreatedTime = None
        self.AccountId = None


    def _deserialize(self, params):
        self.CreatedTime = params.get("CreatedTime")
        self.AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """描述镜像关联的快照信息

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照Id。
        :type SnapshotId: str
        :param DiskUsage: 创建此快照的云硬盘类型。取值范围：
SYSTEM_DISK：系统盘
DATA_DISK：数据盘。
        :type DiskUsage: str
        :param DiskSize: 创建此快照的云硬盘大小，单位GB。
        :type DiskSize: int
        """
        self.SnapshotId = None
        self.DiskUsage = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotMarketOptions(AbstractModel):
    """竞价相关选项

    """

    def __init__(self):
        r"""
        :param MaxPrice: 竞价出价
        :type MaxPrice: str
        :param SpotInstanceType: 竞价请求类型，当前仅支持类型：one-time
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotPaidQuota(AbstractModel):
    """竞价实例配额

    """

    def __init__(self):
        r"""
        :param UsedQuota: 已使用配额，单位：vCPU核心数
        :type UsedQuota: int
        :param RemainingQuota: 剩余配额，单位：vCPU核心数
        :type RemainingQuota: int
        :param TotalQuota: 总配额，单位：vCPU核心数
        :type TotalQuota: int
        :param Zone: 可用区
        :type Zone: str
        """
        self.UsedQuota = None
        self.RemainingQuota = None
        self.TotalQuota = None
        self.Zone = None


    def _deserialize(self, params):
        self.UsedQuota = params.get("UsedQuota")
        self.RemainingQuota = params.get("RemainingQuota")
        self.TotalQuota = params.get("TotalQuota")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    """StopInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param ForceStop: 本参数已弃用，推荐使用StopType，不可以与参数StopType同时使用。表示是否在正常关闭失败后选择强制关闭实例。取值范围：<br><li>TRUE：表示在正常关闭失败后进行强制关闭<br><li>FALSE：表示在正常关闭失败后不进行强制关闭<br><br>默认取值：FALSE。
        :type ForceStop: bool
        :param StopType: 实例的关闭模式。取值范围：<br><li>SOFT_FIRST：表示在正常关闭失败后进行强制关闭<br><li>HARD：直接强制关闭<br><li>SOFT：仅软关机<br>默认取值：SOFT。
        :type StopType: str
        :param StoppedMode: 按量计费实例关机收费模式。
取值范围：<br><li>KEEP_CHARGING：关机继续收费<br><li>STOP_CHARGING：关机停止收费<br>默认取值：KEEP_CHARGING。
该参数只针对部分按量计费云硬盘实例生效，详情参考[按量计费实例关机不收费说明](https://cloud.tencent.com/document/product/213/19918)
        :type StoppedMode: str
        """
        self.InstanceIds = None
        self.ForceStop = None
        self.StopType = None
        self.StoppedMode = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ForceStop = params.get("ForceStop")
        self.StopType = params.get("StopType")
        self.StoppedMode = params.get("StoppedMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StorageBlock(AbstractModel):
    """HDD的本地存储信息

    """

    def __init__(self):
        r"""
        :param Type: HDD本地存储类型，值为：LOCAL_PRO.
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param MinSize: HDD本地存储的最小容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinSize: int
        :param MaxSize: HDD本地存储的最大容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self.Type = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesRequest(AbstractModel):
    """SyncImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageIds: 镜像ID列表 ，镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。<br>镜像ID必须满足限制：<br><li>镜像ID对应的镜像状态必须为`NORMAL`。<br>镜像状态请参考[镜像数据表](https://cloud.tencent.com/document/product/213/15753#Image)。
        :type ImageIds: list of str
        :param DestinationRegions: 目的同步地域列表；必须满足限制：<br><li>不能为源地域，<br><li>必须是一个合法的Region。<br><li>暂不支持部分地域同步。<br>具体地域参数请参考[Region](https://cloud.tencent.com/document/product/213/6091)。

如果是共享镜像，则目的同步地域仅支持源地域，表示将共享镜像复制为同地域的自定义镜像。
        :type DestinationRegions: list of str
        :param DryRun: 检测是否支持发起同步镜像。
        :type DryRun: bool
        :param ImageName: 目标镜像名称。
        :type ImageName: str
        """
        self.ImageIds = None
        self.DestinationRegions = None
        self.DryRun = None
        self.ImageName = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        self.DestinationRegions = params.get("DestinationRegions")
        self.DryRun = params.get("DryRun")
        self.ImageName = params.get("ImageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesResponse(AbstractModel):
    """SyncImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param DiskType: 系统盘类型。系统盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_BSSD：通用性SSD云硬盘<br><br>默认取值：当前有库存的硬盘类型。
        :type DiskType: str
        :param DiskId: 系统盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID。暂时不支持该参数。
该参数目前仅用于`DescribeInstances`等查询类接口的返回参数，不可用于`RunInstances`等写接口的入参。
        :type DiskId: str
        :param DiskSize: 系统盘大小，单位：GB。默认值为 50
        :type DiskSize: int
        :param CdcId: 所属的独享集群ID。
        :type CdcId: str
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None
        self.CdcId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param Key: 标签键
        :type Key: str
        :param Value: 标签值
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
        


class TagSpecification(AbstractModel):
    """创建资源实例时同时绑定的标签对说明

    """

    def __init__(self):
        r"""
        :param ResourceType: 标签绑定的资源类型，云服务器为“instance”，专用宿主机为“host”，镜像为“image”，密钥为“keypair”
        :type ResourceType: str
        :param Tags: 标签对列表
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
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相关信息，包括子网，IP信息等

    """

    def __init__(self):
        r"""
        :param VpcId: 私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。若在创建子机时VpcId与SubnetId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。若在创建子机时SubnetId与VpcId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type SubnetId: str
        :param AsVpcGateway: 是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：<br><li>TRUE：表示用作公网网关<br><li>FALSE：表示不作为公网网关<br><br>默认取值：FALSE。
        :type AsVpcGateway: bool
        :param PrivateIpAddresses: 私有网络子网 IP 数组，在创建实例、修改实例vpc属性操作中可使用此参数。当前仅批量创建多台实例时支持传入相同子网的多个 IP。
        :type PrivateIpAddresses: list of str
        :param Ipv6AddressCount: 为弹性网卡指定随机生成的 IPv6 地址数量。
        :type Ipv6AddressCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.AsVpcGateway = None
        self.PrivateIpAddresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AsVpcGateway = params.get("AsVpcGateway")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区名称，例如，ap-guangzhou-3
全网可用区名称如下：
<li> ap-chongqing-1 </li>
<li> ap-seoul-1 </li>
<li> ap-seoul-2 </li>
<li> ap-chengdu-1 </li>
<li> ap-chengdu-2 </li>
<li> ap-hongkong-1（售罄） </li>
<li> ap-hongkong-2 </li>
<li> ap-hongkong-3 </li>
<li> ap-shenzhen-fsi-1 </li>
<li> ap-shenzhen-fsi-2 </li>
<li> ap-shenzhen-fsi-3 </li>
<li> ap-guangzhou-1（售罄）</li>
<li> ap-guangzhou-2（售罄）</li>
<li> ap-guangzhou-3 </li>
<li> ap-guangzhou-4 </li>
<li> ap-guangzhou-6 </li>
<li> ap-guangzhou-7 </li>
<li> ap-tokyo-1 </li>
<li> ap-tokyo-2 </li>
<li> ap-singapore-1 </li>
<li> ap-singapore-2 </li>
<li> ap-singapore-3 </li>
<li>ap-singapore-4 </li>
<li> ap-shanghai-fsi-1 </li>
<li> ap-shanghai-fsi-2 </li>
<li> ap-shanghai-fsi-3 </li>
<li> ap-bangkok-1 </li>
<li> ap-bangkok-2 </li>
<li> ap-shanghai-1（售罄） </li>
<li> ap-shanghai-2 </li>
<li> ap-shanghai-3 </li>
<li> ap-shanghai-4 </li>
<li> ap-shanghai-5 </li>
<li> ap-shanghai-8 </li>
<li> ap-mumbai-1 </li>
<li> ap-mumbai-2 </li>
<li> eu-moscow-1 </li>
<li> ap-beijing-1（售罄）</li>
<li> ap-beijing-2 </li>
<li> ap-beijing-3 </li>
<li> ap-beijing-4 </li>
<li> ap-beijing-5 </li>
<li> ap-beijing-6 </li>
<li> ap-beijing-7 </li>
<li> na-siliconvalley-1 </li>
<li> na-siliconvalley-2 </li>
<li> eu-frankfurt-1 </li>
<li> eu-frankfurt-2 </li>
<li> na-toronto-1 </li>
<li> na-ashburn-1 </li>
<li> na-ashburn-2 </li>
<li> ap-nanjing-1 </li>
<li> ap-nanjing-2 </li>
<li> ap-nanjing-3 </li>
<li> sa-saopaulo-1</li>
<li> ap-jakarta-1 </li>
<li> ap-jakarta-2 </li>
        :type Zone: str
        :param ZoneName: 可用区描述，例如，广州三区
        :type ZoneName: str
        :param ZoneId: 可用区ID
        :type ZoneId: str
        :param ZoneState: 可用区状态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :type ZoneState: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        