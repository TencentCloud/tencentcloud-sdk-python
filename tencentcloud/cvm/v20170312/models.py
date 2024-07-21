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
        :param _PostPaidQuotaSet: 后付费配额列表
        :type PostPaidQuotaSet: list of PostPaidQuota
        :param _PrePaidQuotaSet: 预付费配额列表
        :type PrePaidQuotaSet: list of PrePaidQuota
        :param _SpotPaidQuotaSet: spot配额列表
        :type SpotPaidQuotaSet: list of SpotPaidQuota
        :param _ImageQuotaSet: 镜像配额列表
        :type ImageQuotaSet: list of ImageQuota
        :param _DisasterRecoverGroupQuotaSet: 置放群组配额列表
        :type DisasterRecoverGroupQuotaSet: list of DisasterRecoverGroupQuota
        """
        self._PostPaidQuotaSet = None
        self._PrePaidQuotaSet = None
        self._SpotPaidQuotaSet = None
        self._ImageQuotaSet = None
        self._DisasterRecoverGroupQuotaSet = None

    @property
    def PostPaidQuotaSet(self):
        return self._PostPaidQuotaSet

    @PostPaidQuotaSet.setter
    def PostPaidQuotaSet(self, PostPaidQuotaSet):
        self._PostPaidQuotaSet = PostPaidQuotaSet

    @property
    def PrePaidQuotaSet(self):
        return self._PrePaidQuotaSet

    @PrePaidQuotaSet.setter
    def PrePaidQuotaSet(self, PrePaidQuotaSet):
        self._PrePaidQuotaSet = PrePaidQuotaSet

    @property
    def SpotPaidQuotaSet(self):
        return self._SpotPaidQuotaSet

    @SpotPaidQuotaSet.setter
    def SpotPaidQuotaSet(self, SpotPaidQuotaSet):
        self._SpotPaidQuotaSet = SpotPaidQuotaSet

    @property
    def ImageQuotaSet(self):
        return self._ImageQuotaSet

    @ImageQuotaSet.setter
    def ImageQuotaSet(self, ImageQuotaSet):
        self._ImageQuotaSet = ImageQuotaSet

    @property
    def DisasterRecoverGroupQuotaSet(self):
        return self._DisasterRecoverGroupQuotaSet

    @DisasterRecoverGroupQuotaSet.setter
    def DisasterRecoverGroupQuotaSet(self, DisasterRecoverGroupQuotaSet):
        self._DisasterRecoverGroupQuotaSet = DisasterRecoverGroupQuotaSet


    def _deserialize(self, params):
        if params.get("PostPaidQuotaSet") is not None:
            self._PostPaidQuotaSet = []
            for item in params.get("PostPaidQuotaSet"):
                obj = PostPaidQuota()
                obj._deserialize(item)
                self._PostPaidQuotaSet.append(obj)
        if params.get("PrePaidQuotaSet") is not None:
            self._PrePaidQuotaSet = []
            for item in params.get("PrePaidQuotaSet"):
                obj = PrePaidQuota()
                obj._deserialize(item)
                self._PrePaidQuotaSet.append(obj)
        if params.get("SpotPaidQuotaSet") is not None:
            self._SpotPaidQuotaSet = []
            for item in params.get("SpotPaidQuotaSet"):
                obj = SpotPaidQuota()
                obj._deserialize(item)
                self._SpotPaidQuotaSet.append(obj)
        if params.get("ImageQuotaSet") is not None:
            self._ImageQuotaSet = []
            for item in params.get("ImageQuotaSet"):
                obj = ImageQuota()
                obj._deserialize(item)
                self._ImageQuotaSet.append(obj)
        if params.get("DisasterRecoverGroupQuotaSet") is not None:
            self._DisasterRecoverGroupQuotaSet = []
            for item in params.get("DisasterRecoverGroupQuotaSet"):
                obj = DisasterRecoverGroupQuota()
                obj._deserialize(item)
                self._DisasterRecoverGroupQuotaSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountQuotaOverview(AbstractModel):
    """配额详情概览

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _AccountQuota: 配额数据
        :type AccountQuota: :class:`tencentcloud.cvm.v20170312.models.AccountQuota`
        """
        self._Region = None
        self._AccountQuota = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AccountQuota(self):
        return self._AccountQuota

    @AccountQuota.setter
    def AccountQuota(self, AccountQuota):
        self._AccountQuota = AccountQuota


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("AccountQuota") is not None:
            self._AccountQuota = AccountQuota()
            self._AccountQuota._deserialize(params.get("AccountQuota"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionTimer(AbstractModel):
    """定时任务

    """

    def __init__(self):
        r"""
        :param _TimerAction: 定时器动作，目前仅支持销毁一个值：TerminateInstances。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimerAction: str
        :param _ActionTime: 执行时间，按照ISO8601标准表示，并且使用UTC时间。格式为 YYYY-MM-DDThh:mm:ssZ。例如 2018-05-29T11:26:40Z，执行时间必须大于当前时间5分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionTime: str
        :param _Externals: 扩展数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        """
        self._TimerAction = None
        self._ActionTime = None
        self._Externals = None

    @property
    def TimerAction(self):
        return self._TimerAction

    @TimerAction.setter
    def TimerAction(self, TimerAction):
        self._TimerAction = TimerAction

    @property
    def ActionTime(self):
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime

    @property
    def Externals(self):
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals


    def _deserialize(self, params):
        self._TimerAction = params.get("TimerAction")
        self._ActionTime = params.get("ActionTime")
        if params.get("Externals") is not None:
            self._Externals = Externals()
            self._Externals._deserialize(params.get("Externals"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsRequest(AbstractModel):
    """AllocateHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _ClientToken: 用于保证请求幂等性的字符串。
        :type ClientToken: str
        :param _HostChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type HostChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.ChargePrepaid`
        :param _HostChargeType: 实例计费类型。目前仅支持：PREPAID（预付费，即包年包月模式），默认为：'PREPAID'。
        :type HostChargeType: str
        :param _HostType: CDH实例机型，默认为：'HS1'。
        :type HostType: str
        :param _HostCount: 购买CDH实例数量，默认为：1。
        :type HostCount: int
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例。
        :type TagSpecification: list of TagSpecification
        """
        self._Placement = None
        self._ClientToken = None
        self._HostChargePrepaid = None
        self._HostChargeType = None
        self._HostType = None
        self._HostCount = None
        self._TagSpecification = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostChargePrepaid(self):
        return self._HostChargePrepaid

    @HostChargePrepaid.setter
    def HostChargePrepaid(self, HostChargePrepaid):
        self._HostChargePrepaid = HostChargePrepaid

    @property
    def HostChargeType(self):
        return self._HostChargeType

    @HostChargeType.setter
    def HostChargeType(self, HostChargeType):
        self._HostChargeType = HostChargeType

    @property
    def HostType(self):
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def HostCount(self):
        return self._HostCount

    @HostCount.setter
    def HostCount(self, HostCount):
        self._HostCount = HostCount

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ClientToken = params.get("ClientToken")
        if params.get("HostChargePrepaid") is not None:
            self._HostChargePrepaid = ChargePrepaid()
            self._HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        self._HostChargeType = params.get("HostChargeType")
        self._HostType = params.get("HostType")
        self._HostCount = params.get("HostCount")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsResponse(AbstractModel):
    """AllocateHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HostIdSet: 新创建云子机的实例ID列表。
        :type HostIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HostIdSet = None
        self._RequestId = None

    @property
    def HostIdSet(self):
        return self._HostIdSet

    @HostIdSet.setter
    def HostIdSet(self, HostIdSet):
        self._HostIdSet = HostIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HostIdSet = params.get("HostIdSet")
        self._RequestId = params.get("RequestId")


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID，每次请求批量实例的上限为100。<br>可以通过以下方式获取可用的实例ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询实例ID。<br><li>通过调用接口 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) ，取返回信息中的`InstanceId`获取实例ID。
        :type InstanceIds: list of str
        :param _KeyIds: 一个或多个待操作的密钥对ID，每次请求批量密钥对的上限为100。密钥对ID形如：`skey-3glfot13`。<br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的`KeyId`获取密钥对ID。
        :type KeyIds: list of str
        :param _ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再绑定密钥。取值范围：<br><li>true：表示在正常关机失败后进行强制关机。<br><li>false：表示在正常关机失败后不进行强制关机。<br>默认取值：false。
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._KeyIds = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._KeyIds = params.get("KeyIds")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateInstancesKeyPairsResponse(AbstractModel):
    """AssociateInstancesKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 要绑定的`安全组ID`，类似sg-efil73jd，只支持绑定单个安全组。
        :type SecurityGroupIds: list of str
        :param _InstanceIds: 被绑定的`实例ID`，类似ins-lesecurk，支持指定多个实例，每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ChargePrepaid(AbstractModel):
    """描述预付费模式，即包年包月相关参数。包括购买时长和自动续费逻辑等。

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _ChcId: CHC物理服务器ID。
        :type ChcId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _SerialNumber: 服务器序列号。
        :type SerialNumber: str
        :param _InstanceState: CHC的状态<br/>
<ul>
<li>INIT: 设备已录入。还未配置带外和部署网络</li>
<li>READY: 已配置带外和部署网络</li>
<li>PREPARED: 可分配云主机</li>
<li>ONLINE: 已分配云主机</li>
<li>OPERATING: 设备操作中，如正在配置带外网络等。</li>
<li>CLEAR_NETWORK_FAILED: 清理带外和部署网络失败</li>
</ul>
        :type InstanceState: str
        :param _DeviceType: 设备类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param _Placement: 所属可用区
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _BmcVirtualPrivateCloud: 带外网络。
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _BmcIp: 带外网络Ip。
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcIp: str
        :param _BmcSecurityGroupIds: 带外网络安全组Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcSecurityGroupIds: list of str
        :param _DeployVirtualPrivateCloud: 部署网络。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _DeployIp: 部署网络Ip。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployIp: str
        :param _DeploySecurityGroupIds: 部署网络安全组Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploySecurityGroupIds: list of str
        :param _CvmInstanceId: 关联的云主机Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceId: str
        :param _CreatedTime: 服务器导入的时间。
        :type CreatedTime: str
        :param _HardwareDescription: 机型的硬件描述，分别为CPU核数，内存容量和磁盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareDescription: str
        :param _CPU: CHC物理服务器的CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: int
        :param _Memory: CHC物理服务器的内存大小，单位为GB
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _Disk: CHC物理服务器的磁盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Disk: str
        :param _BmcMAC: 带外网络下分配的MAC地址
注意：此字段可能返回 null，表示取不到有效值。
        :type BmcMAC: str
        :param _DeployMAC: 部署网络下分配的MAC地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMAC: str
        :param _TenantType: 设备托管类型。
HOSTING: 托管
TENANT: 租赁
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantType: str
        :param _DeployExtraConfig: chc dhcp选项，用于minios调试
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployExtraConfig: :class:`tencentcloud.cvm.v20170312.models.ChcDeployExtraConfig`
        """
        self._ChcId = None
        self._InstanceName = None
        self._SerialNumber = None
        self._InstanceState = None
        self._DeviceType = None
        self._Placement = None
        self._BmcVirtualPrivateCloud = None
        self._BmcIp = None
        self._BmcSecurityGroupIds = None
        self._DeployVirtualPrivateCloud = None
        self._DeployIp = None
        self._DeploySecurityGroupIds = None
        self._CvmInstanceId = None
        self._CreatedTime = None
        self._HardwareDescription = None
        self._CPU = None
        self._Memory = None
        self._Disk = None
        self._BmcMAC = None
        self._DeployMAC = None
        self._TenantType = None
        self._DeployExtraConfig = None

    @property
    def ChcId(self):
        return self._ChcId

    @ChcId.setter
    def ChcId(self, ChcId):
        self._ChcId = ChcId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def BmcVirtualPrivateCloud(self):
        return self._BmcVirtualPrivateCloud

    @BmcVirtualPrivateCloud.setter
    def BmcVirtualPrivateCloud(self, BmcVirtualPrivateCloud):
        self._BmcVirtualPrivateCloud = BmcVirtualPrivateCloud

    @property
    def BmcIp(self):
        return self._BmcIp

    @BmcIp.setter
    def BmcIp(self, BmcIp):
        self._BmcIp = BmcIp

    @property
    def BmcSecurityGroupIds(self):
        return self._BmcSecurityGroupIds

    @BmcSecurityGroupIds.setter
    def BmcSecurityGroupIds(self, BmcSecurityGroupIds):
        self._BmcSecurityGroupIds = BmcSecurityGroupIds

    @property
    def DeployVirtualPrivateCloud(self):
        return self._DeployVirtualPrivateCloud

    @DeployVirtualPrivateCloud.setter
    def DeployVirtualPrivateCloud(self, DeployVirtualPrivateCloud):
        self._DeployVirtualPrivateCloud = DeployVirtualPrivateCloud

    @property
    def DeployIp(self):
        return self._DeployIp

    @DeployIp.setter
    def DeployIp(self, DeployIp):
        self._DeployIp = DeployIp

    @property
    def DeploySecurityGroupIds(self):
        return self._DeploySecurityGroupIds

    @DeploySecurityGroupIds.setter
    def DeploySecurityGroupIds(self, DeploySecurityGroupIds):
        self._DeploySecurityGroupIds = DeploySecurityGroupIds

    @property
    def CvmInstanceId(self):
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def HardwareDescription(self):
        return self._HardwareDescription

    @HardwareDescription.setter
    def HardwareDescription(self, HardwareDescription):
        self._HardwareDescription = HardwareDescription

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def BmcMAC(self):
        return self._BmcMAC

    @BmcMAC.setter
    def BmcMAC(self, BmcMAC):
        self._BmcMAC = BmcMAC

    @property
    def DeployMAC(self):
        return self._DeployMAC

    @DeployMAC.setter
    def DeployMAC(self, DeployMAC):
        self._DeployMAC = DeployMAC

    @property
    def TenantType(self):
        return self._TenantType

    @TenantType.setter
    def TenantType(self, TenantType):
        self._TenantType = TenantType

    @property
    def DeployExtraConfig(self):
        return self._DeployExtraConfig

    @DeployExtraConfig.setter
    def DeployExtraConfig(self, DeployExtraConfig):
        self._DeployExtraConfig = DeployExtraConfig


    def _deserialize(self, params):
        self._ChcId = params.get("ChcId")
        self._InstanceName = params.get("InstanceName")
        self._SerialNumber = params.get("SerialNumber")
        self._InstanceState = params.get("InstanceState")
        self._DeviceType = params.get("DeviceType")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("BmcVirtualPrivateCloud") is not None:
            self._BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self._BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self._BmcIp = params.get("BmcIp")
        self._BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self._DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self._DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self._DeployIp = params.get("DeployIp")
        self._DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._CreatedTime = params.get("CreatedTime")
        self._HardwareDescription = params.get("HardwareDescription")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._BmcMAC = params.get("BmcMAC")
        self._DeployMAC = params.get("DeployMAC")
        self._TenantType = params.get("TenantType")
        if params.get("DeployExtraConfig") is not None:
            self._DeployExtraConfig = ChcDeployExtraConfig()
            self._DeployExtraConfig._deserialize(params.get("DeployExtraConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChcHostDeniedActions(AbstractModel):
    """CHC物理服务器实例禁止操作的返回结构体

    """

    def __init__(self):
        r"""
        :param _ChcId: CHC物理服务器的实例id
        :type ChcId: str
        :param _State: CHC物理服务器的状态
        :type State: str
        :param _DenyActions: 当前CHC物理服务器禁止做的操作
        :type DenyActions: list of str
        """
        self._ChcId = None
        self._State = None
        self._DenyActions = None

    @property
    def ChcId(self):
        return self._ChcId

    @ChcId.setter
    def ChcId(self, ChcId):
        self._ChcId = ChcId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def DenyActions(self):
        return self._DenyActions

    @DenyActions.setter
    def DenyActions(self, DenyActions):
        self._DenyActions = DenyActions


    def _deserialize(self, params):
        self._ChcId = params.get("ChcId")
        self._State = params.get("State")
        self._DenyActions = params.get("DenyActions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcRequest(AbstractModel):
    """ConfigureChcAssistVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC物理服务器的实例Id。
        :type ChcIds: list of str
        :param _BmcVirtualPrivateCloud: 带外网络信息。
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _BmcSecurityGroupIds: 带外网络的安全组列表
        :type BmcSecurityGroupIds: list of str
        :param _DeployVirtualPrivateCloud: 部署网络信息。
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _DeploySecurityGroupIds: 部署网络的安全组列表
        :type DeploySecurityGroupIds: list of str
        """
        self._ChcIds = None
        self._BmcVirtualPrivateCloud = None
        self._BmcSecurityGroupIds = None
        self._DeployVirtualPrivateCloud = None
        self._DeploySecurityGroupIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def BmcVirtualPrivateCloud(self):
        return self._BmcVirtualPrivateCloud

    @BmcVirtualPrivateCloud.setter
    def BmcVirtualPrivateCloud(self, BmcVirtualPrivateCloud):
        self._BmcVirtualPrivateCloud = BmcVirtualPrivateCloud

    @property
    def BmcSecurityGroupIds(self):
        return self._BmcSecurityGroupIds

    @BmcSecurityGroupIds.setter
    def BmcSecurityGroupIds(self, BmcSecurityGroupIds):
        self._BmcSecurityGroupIds = BmcSecurityGroupIds

    @property
    def DeployVirtualPrivateCloud(self):
        return self._DeployVirtualPrivateCloud

    @DeployVirtualPrivateCloud.setter
    def DeployVirtualPrivateCloud(self, DeployVirtualPrivateCloud):
        self._DeployVirtualPrivateCloud = DeployVirtualPrivateCloud

    @property
    def DeploySecurityGroupIds(self):
        return self._DeploySecurityGroupIds

    @DeploySecurityGroupIds.setter
    def DeploySecurityGroupIds(self, DeploySecurityGroupIds):
        self._DeploySecurityGroupIds = DeploySecurityGroupIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        if params.get("BmcVirtualPrivateCloud") is not None:
            self._BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self._BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self._BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self._DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self._DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self._DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcResponse(AbstractModel):
    """ConfigureChcAssistVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ConfigureChcDeployVpcRequest(AbstractModel):
    """ConfigureChcDeployVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC物理服务器的实例Id。
        :type ChcIds: list of str
        :param _DeployVirtualPrivateCloud: 部署网络信息。
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _DeploySecurityGroupIds: 部署网络的安全组列表。
        :type DeploySecurityGroupIds: list of str
        """
        self._ChcIds = None
        self._DeployVirtualPrivateCloud = None
        self._DeploySecurityGroupIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def DeployVirtualPrivateCloud(self):
        return self._DeployVirtualPrivateCloud

    @DeployVirtualPrivateCloud.setter
    def DeployVirtualPrivateCloud(self, DeployVirtualPrivateCloud):
        self._DeployVirtualPrivateCloud = DeployVirtualPrivateCloud

    @property
    def DeploySecurityGroupIds(self):
        return self._DeploySecurityGroupIds

    @DeploySecurityGroupIds.setter
    def DeploySecurityGroupIds(self, DeploySecurityGroupIds):
        self._DeploySecurityGroupIds = DeploySecurityGroupIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self._DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self._DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self._DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcDeployVpcResponse(AbstractModel):
    """ConfigureChcDeployVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CpuTopology(AbstractModel):
    """描述了实例CPU拓扑结构的相关信息。

    """

    def __init__(self):
        r"""
        :param _CoreCount: 决定启用的CPU物理核心数。
        :type CoreCount: int
        :param _ThreadPerCore: 每核心线程数。该参数决定是否开启或关闭超线程。<br><li>1 表示关闭超线程 </li><br><li>2 表示开启超线程</li>
 不设置时，实例使用默认的超线程策略。开关超线程请参考文档：[开启与关闭超线程](https://cloud.tencent.com/document/product/213/103798)。
        :type ThreadPerCore: int
        """
        self._CoreCount = None
        self._ThreadPerCore = None

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def ThreadPerCore(self):
        return self._ThreadPerCore

    @ThreadPerCore.setter
    def ThreadPerCore(self, ThreadPerCore):
        self._ThreadPerCore = ThreadPerCore


    def _deserialize(self, params):
        self._CoreCount = params.get("CoreCount")
        self._ThreadPerCore = params.get("ThreadPerCore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoverGroupRequest(AbstractModel):
    """CreateDisasterRecoverGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 分散置放群组名称，长度1-60个字符，支持中、英文。
        :type Name: str
        :param _Type: 分散置放群组类型，取值范围：<br><li>HOST：物理机<br><li>SW：交换机<br><li>RACK：机架
        :type Type: str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        """
        self._Name = None
        self._Type = None
        self._ClientToken = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoverGroupResponse(AbstractModel):
    """CreateDisasterRecoverGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupId: 分散置放群组ID列表。
        :type DisasterRecoverGroupId: str
        :param _Type: 分散置放群组类型，取值范围：<br><li>HOST：物理机<br><li>SW：交换机<br><li>RACK：机架
        :type Type: str
        :param _Name: 分散置放群组名称，长度1-60个字符，支持中、英文。
        :type Name: str
        :param _CvmQuotaTotal: 置放群组内可容纳的云服务器数量。
        :type CvmQuotaTotal: int
        :param _CurrentNum: 置放群组内已有的云服务器数量。
        :type CurrentNum: int
        :param _CreateTime: 置放群组创建时间。
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DisasterRecoverGroupId = None
        self._Type = None
        self._Name = None
        self._CvmQuotaTotal = None
        self._CurrentNum = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CvmQuotaTotal(self):
        return self._CvmQuotaTotal

    @CvmQuotaTotal.setter
    def CvmQuotaTotal(self, CvmQuotaTotal):
        self._CvmQuotaTotal = CvmQuotaTotal

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._CvmQuotaTotal = params.get("CvmQuotaTotal")
        self._CurrentNum = params.get("CurrentNum")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class CreateHpcClusterRequest(AbstractModel):
    """CreateHpcCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区。
        :type Zone: str
        :param _Name: 高性能计算集群名称。
        :type Name: str
        :param _Remark: 高性能计算集群备注。
        :type Remark: str
        :param _HpcClusterType: 高性能计算集群类型。
        :type HpcClusterType: str
        :param _HpcClusterBusinessId: 高性能计算集群对应的业务场景标识，当前只支持CDC。
        :type HpcClusterBusinessId: str
        """
        self._Zone = None
        self._Name = None
        self._Remark = None
        self._HpcClusterType = None
        self._HpcClusterBusinessId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def HpcClusterType(self):
        return self._HpcClusterType

    @HpcClusterType.setter
    def HpcClusterType(self, HpcClusterType):
        self._HpcClusterType = HpcClusterType

    @property
    def HpcClusterBusinessId(self):
        return self._HpcClusterBusinessId

    @HpcClusterBusinessId.setter
    def HpcClusterBusinessId(self, HpcClusterBusinessId):
        self._HpcClusterBusinessId = HpcClusterBusinessId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._HpcClusterType = params.get("HpcClusterType")
        self._HpcClusterBusinessId = params.get("HpcClusterBusinessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHpcClusterResponse(AbstractModel):
    """CreateHpcCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HpcClusterSet: 高性能计算集群信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type HpcClusterSet: list of HpcClusterInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HpcClusterSet = None
        self._RequestId = None

    @property
    def HpcClusterSet(self):
        return self._HpcClusterSet

    @HpcClusterSet.setter
    def HpcClusterSet(self, HpcClusterSet):
        self._HpcClusterSet = HpcClusterSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HpcClusterSet") is not None:
            self._HpcClusterSet = []
            for item in params.get("HpcClusterSet"):
                obj = HpcClusterInfo()
                obj._deserialize(item)
                self._HpcClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _InstanceId: 需要制作镜像的实例ID。基于实例创建镜像时，为必填参数。
        :type InstanceId: str
        :param _ImageDescription: 镜像描述
        :type ImageDescription: str
        :param _ForcePoweroff: 是否执行强制关机以制作镜像。
取值范围：<br><li>true：表示关机之后制作镜像<br><li>false：表示开机状态制作镜像<br><br>默认取值：false。<br><br>开机状态制作镜像，可能导致部分数据未备份，影响数据安全。
        :type ForcePoweroff: str
        :param _Sysprep: 创建Windows镜像时是否启用Sysprep。
取值范围：true或false，传true表示启用Sysprep，传false表示不启用，默认取值为false。

关于Sysprep的详情请参考[链接](https://cloud.tencent.com/document/product/213/43498)。
        :type Sysprep: str
        :param _DataDiskIds: 基于实例创建整机镜像时，指定包含在镜像里的数据盘ID
        :type DataDiskIds: list of str
        :param _SnapshotIds: 基于快照创建镜像，指定快照ID，必须包含一个系统盘快照。不可与InstanceId同时传入。
        :type SnapshotIds: list of str
        :param _DryRun: 检测本次请求的是否成功，但不会对操作的资源产生任何影响。默认取值为false。
        :type DryRun: bool
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到自定义镜像。
        :type TagSpecification: list of TagSpecification
        """
        self._ImageName = None
        self._InstanceId = None
        self._ImageDescription = None
        self._ForcePoweroff = None
        self._Sysprep = None
        self._DataDiskIds = None
        self._SnapshotIds = None
        self._DryRun = None
        self._TagSpecification = None

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ForcePoweroff(self):
        return self._ForcePoweroff

    @ForcePoweroff.setter
    def ForcePoweroff(self, ForcePoweroff):
        self._ForcePoweroff = ForcePoweroff

    @property
    def Sysprep(self):
        return self._Sysprep

    @Sysprep.setter
    def Sysprep(self, Sysprep):
        self._Sysprep = Sysprep

    @property
    def DataDiskIds(self):
        return self._DataDiskIds

    @DataDiskIds.setter
    def DataDiskIds(self, DataDiskIds):
        self._DataDiskIds = DataDiskIds

    @property
    def SnapshotIds(self):
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._ImageName = params.get("ImageName")
        self._InstanceId = params.get("InstanceId")
        self._ImageDescription = params.get("ImageDescription")
        self._ForcePoweroff = params.get("ForcePoweroff")
        self._Sysprep = params.get("Sysprep")
        self._DataDiskIds = params.get("DataDiskIds")
        self._SnapshotIds = params.get("SnapshotIds")
        self._DryRun = params.get("DryRun")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageId = None
        self._RequestId = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :type KeyName: str
        :param _ProjectId: 密钥对创建后所属的项目ID。
可以通过以下方式获取项目ID：
<li>通过项目列表查询项目ID。</li>
<li>通过调用接口 [DescribeProjects](https://cloud.tencent.com/document/api/651/78725)，取返回信息中的`projectId `获取项目ID。</li>
        :type ProjectId: int
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到密钥对。
        :type TagSpecification: list of TagSpecification
        """
        self._KeyName = None
        self._ProjectId = None
        self._TagSpecification = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyPair: 密钥对信息。
        :type KeyPair: :class:`tencentcloud.cvm.v20170312.models.KeyPair`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyPair = None
        self._RequestId = None

    @property
    def KeyPair(self):
        return self._KeyPair

    @KeyPair.setter
    def KeyPair(self, KeyPair):
        self._KeyPair = KeyPair

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self._KeyPair = KeyPair()
            self._KeyPair._deserialize(params.get("KeyPair"))
        self._RequestId = params.get("RequestId")


class CreateLaunchTemplateRequest(AbstractModel):
    """CreateLaunchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateName: 实例启动模板名称。长度为2~128个英文或中文字符。
        :type LaunchTemplateName: str
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，传入InstanceType获取当前机型支持的镜像列表，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param _LaunchTemplateVersionDescription: 实例启动模板版本描述。长度为2~256个英文或中文字符。
        :type LaunchTemplateVersionDescription: str
        :param _InstanceType: 实例机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则系统将根据当前地域的资源售卖情况动态指定默认机型。</li><li>对于付费模式为CDHPAID的实例创建，该参数以"CDH_"为前缀，根据CPU和内存配置生成，具体形式为：CDH_XCXG，例如对于创建CPU为1核，内存为1G大小的专用宿主机的实例，该参数应该为CDH_1C1G。</li>
        :type InstanceType: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，即表示每个实例的主网卡IP；同时，InstanceCount参数必须与私有网络IP的个数一致且不能大于20。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _InstanceCount: 购买实例数量。包年包月实例取值范围：[1，300]，按量计费实例取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。</li>
        :type InstanceName: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _HostName: 云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li>
        :type HostName: str
        :param _ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param _DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。
        :type TagSpecification: list of TagSpecification
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。
        :type UserData: str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param _CamRoleName: CAM角色名称。可通过[`DescribeRoleList`](https://cloud.tencent.com/document/product/598/13887)接口返回值中的`roleName`获取。
        :type CamRoleName: str
        :param _HpcClusterId: 高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :type HpcClusterId: str
        :param _InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li><li>CDHPAID：独享子机（基于专用宿主机创建，宿主机部分的资源不收费）</li><li>SPOTPAID：竞价付费</li>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>TRUE：表示开启实例保护，不允许通过api接口删除实例</li><li>FALSE：表示关闭实例保护，允许通过api接口删除实例<br></li>默认取值：FALSE。
        :type DisableApiTermination: bool
        """
        self._LaunchTemplateName = None
        self._Placement = None
        self._ImageId = None
        self._LaunchTemplateVersionDescription = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceCount = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._ClientToken = None
        self._HostName = None
        self._ActionTimer = None
        self._DisasterRecoverGroupIds = None
        self._TagSpecification = None
        self._InstanceMarketOptions = None
        self._UserData = None
        self._DryRun = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._DisableApiTermination = None

    @property
    def LaunchTemplateName(self):
        return self._LaunchTemplateName

    @LaunchTemplateName.setter
    def LaunchTemplateName(self, LaunchTemplateName):
        self._LaunchTemplateName = LaunchTemplateName

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LaunchTemplateVersionDescription(self):
        return self._LaunchTemplateVersionDescription

    @LaunchTemplateVersionDescription.setter
    def LaunchTemplateVersionDescription(self, LaunchTemplateVersionDescription):
        self._LaunchTemplateVersionDescription = LaunchTemplateVersionDescription

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination


    def _deserialize(self, params):
        self._LaunchTemplateName = params.get("LaunchTemplateName")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ImageId = params.get("ImageId")
        self._LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ClientToken = params.get("ClientToken")
        self._HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._UserData = params.get("UserData")
        self._DryRun = params.get("DryRun")
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchTemplateResponse(AbstractModel):
    """CreateLaunchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: 当通过本接口来创建实例启动模板时会返回该参数，表示创建成功的实例启动模板`ID`。
        :type LaunchTemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LaunchTemplateId = None
        self._RequestId = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._RequestId = params.get("RequestId")


class CreateLaunchTemplateVersionRequest(AbstractModel):
    """CreateLaunchTemplateVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _LaunchTemplateId: 启动模板ID，新版本将基于该实例启动模板ID创建。
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersion: 若给定，新实例启动模板将基于给定的版本号创建。若未指定则使用默认版本。
        :type LaunchTemplateVersion: int
        :param _LaunchTemplateVersionDescription: 实例启动模板版本描述。长度为2~256个英文或中文字符。
        :type LaunchTemplateVersionDescription: str
        :param _InstanceType: 实例机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则系统将根据当前地域的资源售卖情况动态指定默认机型。</li><br><li>对于付费模式为CDHPAID的实例创建，该参数以"CDH_"为前缀，根据CPU和内存配置生成，具体形式为：CDH_XCXG，例如对于创建CPU为1核，内存为1G大小的专用宿主机的实例，该参数应该为CDH_1C1G。</li>
        :type InstanceType: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，传入InstanceType获取当前机型支持的镜像列表，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，即表示每个实例的主网卡IP；同时，InstanceCount参数必须与私有网络IP的个数一致且不能大于20。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _InstanceCount: 购买实例数量。包年包月实例取值范围：[1，300]，按量计费实例取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。</li>
        :type InstanceName: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _HostName: 云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><br><li>Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><br><li>其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li>
        :type HostName: str
        :param _ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param _DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。
        :type TagSpecification: list of TagSpecification
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。
        :type UserData: str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param _CamRoleName: CAM角色名称。可通过[`DescribeRoleList`](https://cloud.tencent.com/document/product/598/13887)接口返回值中的`roleName`获取。
        :type CamRoleName: str
        :param _HpcClusterId: 高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :type HpcClusterId: str
        :param _InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li><li>CDHPAID：独享子机（基于专用宿主机创建，宿主机部分的资源不收费）</li><li>SPOTPAID：竞价付费</li>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>TRUE：表示开启实例保护，不允许通过api接口删除实例</li><br><li>FALSE：表示关闭实例保护，允许通过api接口删除实例</li><br><br>默认取值：FALSE。
        :type DisableApiTermination: bool
        """
        self._Placement = None
        self._LaunchTemplateId = None
        self._LaunchTemplateVersion = None
        self._LaunchTemplateVersionDescription = None
        self._InstanceType = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceCount = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._ClientToken = None
        self._HostName = None
        self._ActionTimer = None
        self._DisasterRecoverGroupIds = None
        self._TagSpecification = None
        self._InstanceMarketOptions = None
        self._UserData = None
        self._DryRun = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._DisableApiTermination = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersion(self):
        return self._LaunchTemplateVersion

    @LaunchTemplateVersion.setter
    def LaunchTemplateVersion(self, LaunchTemplateVersion):
        self._LaunchTemplateVersion = LaunchTemplateVersion

    @property
    def LaunchTemplateVersionDescription(self):
        return self._LaunchTemplateVersionDescription

    @LaunchTemplateVersionDescription.setter
    def LaunchTemplateVersionDescription(self, LaunchTemplateVersionDescription):
        self._LaunchTemplateVersionDescription = LaunchTemplateVersionDescription

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        self._LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self._InstanceType = params.get("InstanceType")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ClientToken = params.get("ClientToken")
        self._HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._UserData = params.get("UserData")
        self._DryRun = params.get("DryRun")
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchTemplateVersionResponse(AbstractModel):
    """CreateLaunchTemplateVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateVersionNumber: 新创建的实例启动模板版本号。
        :type LaunchTemplateVersionNumber: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LaunchTemplateVersionNumber = None
        self._RequestId = None

    @property
    def LaunchTemplateVersionNumber(self):
        return self._LaunchTemplateVersionNumber

    @LaunchTemplateVersionNumber.setter
    def LaunchTemplateVersionNumber(self, LaunchTemplateVersionNumber):
        self._LaunchTemplateVersionNumber = LaunchTemplateVersionNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LaunchTemplateVersionNumber = params.get("LaunchTemplateVersionNumber")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param _DiskType: 数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br />
<li>
  LOCAL_BASIC：本地硬盘<br />
  <li>
    LOCAL_SSD：本地SSD硬盘<br />
    <li>
      LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br />
      <li>
        LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br />
        <li>
          CLOUD_BASIC：普通云硬盘<br />
          <li>
            CLOUD_PREMIUM：高性能云硬盘<br />
            <li>
              CLOUD_SSD：SSD云硬盘<br />
              <li>
                CLOUD_HSSD：增强型SSD云硬盘<br />
                <li>
                  CLOUD_TSSD：极速型SSD云硬盘<br />
                  <li>
                    CLOUD_BSSD：通用型SSD云硬盘<br /><br />默认取值：LOCAL_BASIC。<br /><br />该参数对`ResizeInstanceDisk`接口无效。
                  </li>
                </li>
              </li>
            </li>
          </li>
        </li>
      </li>
    </li>
  </li>
</li>
        :type DiskType: str
        :param _DiskId: 数据盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID，暂时不支持该参数。
该参数目前仅用于`DescribeInstances`等查询类接口的返回参数，不可用于`RunInstances`等写接口的入参。
        :type DiskId: str
        :param _DeleteWithInstance: 数据盘是否随子机销毁。取值范围：
<li>TRUE：子机销毁时，销毁数据盘，只支持按小时后付费云盘</li>
<li>
  FALSE：子机销毁时，保留数据盘<br />
  默认取值：TRUE<br />
  该参数目前仅用于 `RunInstances` 接口。
</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param _SnapshotId: 数据盘快照ID。选择的数据盘快照大小需小于数据盘大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param _Encrypt: 数据盘是加密。取值范围：
<li>true：加密</li>
<li>
  false：不加密<br />
  默认取值：false<br />
  该参数目前仅用于 `RunInstances` 接口。
</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: bool
        :param _KmsKeyId: 自定义CMK对应的ID，取值为UUID或者类似kms-abcd1234。用于加密云盘。

该参数目前仅用于 `RunInstances` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyId: str
        :param _ThroughputPerformance: 云硬盘性能，单位：MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        :param _CdcId: 所属的独享集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        :param _BurstPerformance: 突发性能

 <b>注：内测中。</b>
注意：此字段可能返回 null，表示取不到有效值。
        :type BurstPerformance: bool
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskId = None
        self._DeleteWithInstance = None
        self._SnapshotId = None
        self._Encrypt = None
        self._KmsKeyId = None
        self._ThroughputPerformance = None
        self._CdcId = None
        self._BurstPerformance = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def KmsKeyId(self):
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def BurstPerformance(self):
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._SnapshotId = params.get("SnapshotId")
        self._Encrypt = params.get("Encrypt")
        self._KmsKeyId = params.get("KmsKeyId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._CdcId = params.get("CdcId")
        self._BurstPerformance = params.get("BurstPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsRequest(AbstractModel):
    """DeleteDisasterRecoverGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，可通过[DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810)接口获取。每次请求允许操作的分散置放群组数量上限是100。
        :type DisasterRecoverGroupIds: list of str
        """
        self._DisasterRecoverGroupIds = None

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds


    def _deserialize(self, params):
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsResponse(AbstractModel):
    """DeleteDisasterRecoverGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteHpcClustersRequest(AbstractModel):
    """DeleteHpcClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HpcClusterIds: 高性能计算集群ID列表。
        :type HpcClusterIds: list of str
        """
        self._HpcClusterIds = None

    @property
    def HpcClusterIds(self):
        return self._HpcClusterIds

    @HpcClusterIds.setter
    def HpcClusterIds(self, HpcClusterIds):
        self._HpcClusterIds = HpcClusterIds


    def _deserialize(self, params):
        self._HpcClusterIds = params.get("HpcClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHpcClustersResponse(AbstractModel):
    """DeleteHpcClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteImagesRequest(AbstractModel):
    """DeleteImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageIds: 准备删除的镜像Id列表
        :type ImageIds: list of str
        :param _DeleteBindedSnap: 是否删除镜像关联的快照
        :type DeleteBindedSnap: bool
        :param _DryRun: 检测是否支持删除镜像
        :type DryRun: bool
        """
        self._ImageIds = None
        self._DeleteBindedSnap = None
        self._DryRun = None

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def DeleteBindedSnap(self):
        return self._DeleteBindedSnap

    @DeleteBindedSnap.setter
    def DeleteBindedSnap(self, DeleteBindedSnap):
        self._DeleteBindedSnap = DeleteBindedSnap

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        self._DeleteBindedSnap = params.get("DeleteBindedSnap")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagesResponse(AbstractModel):
    """DeleteImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteInstancesActionTimerRequest(AbstractModel):
    """DeleteInstancesActionTimer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionTimerIds: 定时任务ID列表，可以通过DescribeInstancesActionTimer接口查询。只能删除未执行的定时任务。
        :type ActionTimerIds: list of str
        """
        self._ActionTimerIds = None

    @property
    def ActionTimerIds(self):
        return self._ActionTimerIds

    @ActionTimerIds.setter
    def ActionTimerIds(self, ActionTimerIds):
        self._ActionTimerIds = ActionTimerIds


    def _deserialize(self, params):
        self._ActionTimerIds = params.get("ActionTimerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstancesActionTimerResponse(AbstractModel):
    """DeleteInstancesActionTimer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteKeyPairsRequest(AbstractModel):
    """DeleteKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 一个或多个待操作的密钥对ID。每次请求批量密钥对的上限为100。<br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。</li><br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的 `KeyId` 获取密钥对ID。</li>
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKeyPairsResponse(AbstractModel):
    """DeleteKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteLaunchTemplateRequest(AbstractModel):
    """DeleteLaunchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        """
        self._LaunchTemplateId = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateResponse(AbstractModel):
    """DeleteLaunchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteLaunchTemplateVersionsRequest(AbstractModel):
    """DeleteLaunchTemplateVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersions: 实例启动模板版本列表。
        :type LaunchTemplateVersions: list of int
        """
        self._LaunchTemplateId = None
        self._LaunchTemplateVersions = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersions(self):
        return self._LaunchTemplateVersions

    @LaunchTemplateVersions.setter
    def LaunchTemplateVersions(self, LaunchTemplateVersions):
        self._LaunchTemplateVersions = LaunchTemplateVersions


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateVersionsResponse(AbstractModel):
    """DeleteLaunchTemplateVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAccountQuotaRequest(AbstractModel):
    """DescribeAccountQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>quota-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>配额类型</strong>】进行过滤。配额类型形如：PostPaidQuotaSet。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：PostPaidQuotaSet,DisasterRecoverGroupQuotaSet,PrePaidQuotaSet,SpotPaidQuotaSet</p>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountQuotaResponse(AbstractModel):
    """DescribeAccountQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 用户appid
        :type AppId: int
        :param _AccountQuotaOverview: 配额数据
        :type AccountQuotaOverview: :class:`tencentcloud.cvm.v20170312.models.AccountQuotaOverview`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._AccountQuotaOverview = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AccountQuotaOverview(self):
        return self._AccountQuotaOverview

    @AccountQuotaOverview.setter
    def AccountQuotaOverview(self, AccountQuotaOverview):
        self._AccountQuotaOverview = AccountQuotaOverview

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("AccountQuotaOverview") is not None:
            self._AccountQuotaOverview = AccountQuotaOverview()
            self._AccountQuotaOverview._deserialize(params.get("AccountQuotaOverview"))
        self._RequestId = params.get("RequestId")


class DescribeChcDeniedActionsRequest(AbstractModel):
    """DescribeChcDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC物理服务器实例id
        :type ChcIds: list of str
        """
        self._ChcIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChcDeniedActionsResponse(AbstractModel):
    """DescribeChcDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcHostDeniedActionSet: CHC实例禁止操作信息
        :type ChcHostDeniedActionSet: list of ChcHostDeniedActions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ChcHostDeniedActionSet = None
        self._RequestId = None

    @property
    def ChcHostDeniedActionSet(self):
        return self._ChcHostDeniedActionSet

    @ChcHostDeniedActionSet.setter
    def ChcHostDeniedActionSet(self, ChcHostDeniedActionSet):
        self._ChcHostDeniedActionSet = ChcHostDeniedActionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ChcHostDeniedActionSet") is not None:
            self._ChcHostDeniedActionSet = []
            for item in params.get("ChcHostDeniedActionSet"):
                obj = ChcHostDeniedActions()
                obj._deserialize(item)
                self._ChcHostDeniedActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChcHostsRequest(AbstractModel):
    """DescribeChcHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC物理服务器实例ID。每次请求的实例的上限为100。参数不支持同时指定`ChcIds`和`Filters`。
        :type ChcIds: list of str
        :param _Filters: <li><strong>zone</strong></li>
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
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ChcIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._ChcIds = params.get("ChcIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChcHostsResponse(AbstractModel):
    """DescribeChcHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _ChcHostSet: 返回的实例列表
        :type ChcHostSet: list of ChcHost
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ChcHostSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ChcHostSet(self):
        return self._ChcHostSet

    @ChcHostSet.setter
    def ChcHostSet(self, ChcHostSet):
        self._ChcHostSet = ChcHostSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ChcHostSet") is not None:
            self._ChcHostSet = []
            for item in params.get("ChcHostSet"):
                obj = ChcHost()
                obj._deserialize(item)
                self._ChcHostSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupQuotaRequest(AbstractModel):
    """DescribeDisasterRecoverGroupQuota请求参数结构体

    """


class DescribeDisasterRecoverGroupQuotaResponse(AbstractModel):
    """DescribeDisasterRecoverGroupQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupQuota: 可创建置放群组数量的上限。
        :type GroupQuota: int
        :param _CurrentNum: 当前用户已经创建的置放群组数量。
        :type CurrentNum: int
        :param _CvmInHostGroupQuota: 物理机类型容灾组内实例的配额数。
        :type CvmInHostGroupQuota: int
        :param _CvmInSwGroupQuota: 交换机类型容灾组内实例的配额数。
        :type CvmInSwGroupQuota: int
        :param _CvmInRackGroupQuota: 机架类型容灾组内实例的配额数。
        :type CvmInRackGroupQuota: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupQuota = None
        self._CurrentNum = None
        self._CvmInHostGroupQuota = None
        self._CvmInSwGroupQuota = None
        self._CvmInRackGroupQuota = None
        self._RequestId = None

    @property
    def GroupQuota(self):
        return self._GroupQuota

    @GroupQuota.setter
    def GroupQuota(self, GroupQuota):
        self._GroupQuota = GroupQuota

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def CvmInHostGroupQuota(self):
        return self._CvmInHostGroupQuota

    @CvmInHostGroupQuota.setter
    def CvmInHostGroupQuota(self, CvmInHostGroupQuota):
        self._CvmInHostGroupQuota = CvmInHostGroupQuota

    @property
    def CvmInSwGroupQuota(self):
        return self._CvmInSwGroupQuota

    @CvmInSwGroupQuota.setter
    def CvmInSwGroupQuota(self, CvmInSwGroupQuota):
        self._CvmInSwGroupQuota = CvmInSwGroupQuota

    @property
    def CvmInRackGroupQuota(self):
        return self._CvmInRackGroupQuota

    @CvmInRackGroupQuota.setter
    def CvmInRackGroupQuota(self, CvmInRackGroupQuota):
        self._CvmInRackGroupQuota = CvmInRackGroupQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupQuota = params.get("GroupQuota")
        self._CurrentNum = params.get("CurrentNum")
        self._CvmInHostGroupQuota = params.get("CvmInHostGroupQuota")
        self._CvmInSwGroupQuota = params.get("CvmInSwGroupQuota")
        self._CvmInRackGroupQuota = params.get("CvmInRackGroupQuota")
        self._RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupsRequest(AbstractModel):
    """DescribeDisasterRecoverGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表。每次请求允许操作的分散置放群组数量上限是100。
        :type DisasterRecoverGroupIds: list of str
        :param _Name: 分散置放群组名称，支持模糊匹配。
        :type Name: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._DisasterRecoverGroupIds = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoverGroupsResponse(AbstractModel):
    """DescribeDisasterRecoverGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupSet: 分散置放群组信息列表。
        :type DisasterRecoverGroupSet: list of DisasterRecoverGroup
        :param _TotalCount: 用户置放群组总量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DisasterRecoverGroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DisasterRecoverGroupSet(self):
        return self._DisasterRecoverGroupSet

    @DisasterRecoverGroupSet.setter
    def DisasterRecoverGroupSet(self, DisasterRecoverGroupSet):
        self._DisasterRecoverGroupSet = DisasterRecoverGroupSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DisasterRecoverGroupSet") is not None:
            self._DisasterRecoverGroupSet = []
            for item in params.get("DisasterRecoverGroupSet"):
                obj = DisasterRecoverGroup()
                obj._deserialize(item)
                self._DisasterRecoverGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostsRequest(AbstractModel):
    """DescribeHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li><strong>zone</strong></li>
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
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsResponse(AbstractModel):
    """DescribeHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的cdh实例总数
        :type TotalCount: int
        :param _HostSet: cdh实例详细信息列表
        :type HostSet: list of HostItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HostSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HostSet(self):
        return self._HostSet

    @HostSet.setter
    def HostSet(self, HostSet):
        self._HostSet = HostSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("HostSet") is not None:
            self._HostSet = []
            for item in params.get("HostSet"):
                obj = HostItem()
                obj._deserialize(item)
                self._HostSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHpcClustersRequest(AbstractModel):
    """DescribeHpcClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HpcClusterIds: 高性能计算集群ID数组。
        :type HpcClusterIds: list of str
        :param _Name: 高性能计算集群名称。
        :type Name: str
        :param _Zone: 可用区。
        :type Zone: str
        :param _Offset: 偏移量, 默认值0。
        :type Offset: int
        :param _Limit: 本次请求量, 默认值20。
        :type Limit: int
        :param _HpcClusterType: 高性能计算集群类型。
        :type HpcClusterType: str
        :param _HpcClusterBusinessId: 高性能计算集群对应的业务场景标识，当前只支持CDC。	
        :type HpcClusterBusinessId: str
        """
        self._HpcClusterIds = None
        self._Name = None
        self._Zone = None
        self._Offset = None
        self._Limit = None
        self._HpcClusterType = None
        self._HpcClusterBusinessId = None

    @property
    def HpcClusterIds(self):
        return self._HpcClusterIds

    @HpcClusterIds.setter
    def HpcClusterIds(self, HpcClusterIds):
        self._HpcClusterIds = HpcClusterIds

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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

    @property
    def HpcClusterType(self):
        return self._HpcClusterType

    @HpcClusterType.setter
    def HpcClusterType(self, HpcClusterType):
        self._HpcClusterType = HpcClusterType

    @property
    def HpcClusterBusinessId(self):
        return self._HpcClusterBusinessId

    @HpcClusterBusinessId.setter
    def HpcClusterBusinessId(self, HpcClusterBusinessId):
        self._HpcClusterBusinessId = HpcClusterBusinessId


    def _deserialize(self, params):
        self._HpcClusterIds = params.get("HpcClusterIds")
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._HpcClusterType = params.get("HpcClusterType")
        self._HpcClusterBusinessId = params.get("HpcClusterBusinessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHpcClustersResponse(AbstractModel):
    """DescribeHpcClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HpcClusterSet: 高性能计算集群信息。
        :type HpcClusterSet: list of HpcClusterInfo
        :param _TotalCount: 高性能计算集群总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HpcClusterSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HpcClusterSet(self):
        return self._HpcClusterSet

    @HpcClusterSet.setter
    def HpcClusterSet(self, HpcClusterSet):
        self._HpcClusterSet = HpcClusterSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HpcClusterSet") is not None:
            self._HpcClusterSet = []
            for item in params.get("HpcClusterSet"):
                obj = HpcClusterInfo()
                obj._deserialize(item)
                self._HpcClusterSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImageQuotaRequest(AbstractModel):
    """DescribeImageQuota请求参数结构体

    """


class DescribeImageQuotaResponse(AbstractModel):
    """DescribeImageQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageNumQuota: 账户的镜像配额
        :type ImageNumQuota: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageNumQuota = None
        self._RequestId = None

    @property
    def ImageNumQuota(self):
        return self._ImageNumQuota

    @ImageNumQuota.setter
    def ImageNumQuota(self, ImageNumQuota):
        self._ImageNumQuota = ImageNumQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageNumQuota = params.get("ImageNumQuota")
        self._RequestId = params.get("RequestId")


class DescribeImageSharePermissionRequest(AbstractModel):
    """DescribeImageSharePermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 需要共享的镜像Id
        :type ImageId: str
        """
        self._ImageId = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSharePermissionResponse(AbstractModel):
    """DescribeImageSharePermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SharePermissionSet: 镜像共享信息
        :type SharePermissionSet: list of SharePermission
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SharePermissionSet = None
        self._RequestId = None

    @property
    def SharePermissionSet(self):
        return self._SharePermissionSet

    @SharePermissionSet.setter
    def SharePermissionSet(self, SharePermissionSet):
        self._SharePermissionSet = SharePermissionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self._SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self._SharePermissionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageIds: 镜像ID列表 。镜像ID如：`img-gvbnzy6f`。array型参数的格式可以参考[API简介](https://cloud.tencent.com/document/api/213/15688)。镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。<br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。
        :type ImageIds: list of str
        :param _Filters: 过滤条件，每次请求的`Filters`的上限为10，`Filters.Values`的上限为5。参数不可以同时指定`ImageIds`和`Filters`。详细的过滤条件如下：

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
        :param _Offset: 偏移量，默认为0。关于Offset详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。
        :type Offset: int
        :param _Limit: 数量限制，默认为20，最大值为100。关于Limit详见[API简介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。
        :type Limit: int
        :param _InstanceType: 实例类型，如 `S1.SMALL1`
        :type InstanceType: str
        """
        self._ImageIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._InstanceType = None

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageSet: 一个关于镜像详细信息的结构体，主要包括镜像的主要状态与属性。
        :type ImageSet: list of Image
        :param _TotalCount: 符合要求的镜像数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ImageSet(self):
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs请求参数结构体

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImportImageOsListSupported: 支持的导入镜像的操作系统类型。
        :type ImportImageOsListSupported: :class:`tencentcloud.cvm.v20170312.models.ImageOsList`
        :param _ImportImageOsVersionSet: 支持的导入镜像的操作系统版本。
        :type ImportImageOsVersionSet: list of OsVersion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImportImageOsListSupported = None
        self._ImportImageOsVersionSet = None
        self._RequestId = None

    @property
    def ImportImageOsListSupported(self):
        return self._ImportImageOsListSupported

    @ImportImageOsListSupported.setter
    def ImportImageOsListSupported(self, ImportImageOsListSupported):
        self._ImportImageOsListSupported = ImportImageOsListSupported

    @property
    def ImportImageOsVersionSet(self):
        return self._ImportImageOsVersionSet

    @ImportImageOsVersionSet.setter
    def ImportImageOsVersionSet(self, ImportImageOsVersionSet):
        self._ImportImageOsVersionSet = ImportImageOsVersionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self._ImportImageOsListSupported = ImageOsList()
            self._ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self._ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self._ImportImageOsVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceFamilyConfigsRequest(AbstractModel):
    """DescribeInstanceFamilyConfigs请求参数结构体

    """


class DescribeInstanceFamilyConfigsResponse(AbstractModel):
    """DescribeInstanceFamilyConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyConfigSet: 实例机型组配置的列表信息
        :type InstanceFamilyConfigSet: list of InstanceFamilyConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceFamilyConfigSet = None
        self._RequestId = None

    @property
    def InstanceFamilyConfigSet(self):
        return self._InstanceFamilyConfigSet

    @InstanceFamilyConfigSet.setter
    def InstanceFamilyConfigSet(self, InstanceFamilyConfigSet):
        self._InstanceFamilyConfigSet = InstanceFamilyConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfigSet") is not None:
            self._InstanceFamilyConfigSet = []
            for item in params.get("InstanceFamilyConfigSet"):
                obj = InstanceFamilyConfig()
                obj._deserialize(item)
                self._InstanceFamilyConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceInternetBandwidthConfigsRequest(AbstractModel):
    """DescribeInstanceInternetBandwidthConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceInternetBandwidthConfigsResponse(AbstractModel):
    """DescribeInstanceInternetBandwidthConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InternetBandwidthConfigSet: 带宽配置信息列表。
        :type InternetBandwidthConfigSet: list of InternetBandwidthConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InternetBandwidthConfigSet = None
        self._RequestId = None

    @property
    def InternetBandwidthConfigSet(self):
        return self._InternetBandwidthConfigSet

    @InternetBandwidthConfigSet.setter
    def InternetBandwidthConfigSet(self, InternetBandwidthConfigSet):
        self._InternetBandwidthConfigSet = InternetBandwidthConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InternetBandwidthConfigSet") is not None:
            self._InternetBandwidthConfigSet = []
            for item in params.get("InternetBandwidthConfigSet"):
                obj = InternetBandwidthConfig()
                obj._deserialize(item)
                self._InternetBandwidthConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigsRequest(AbstractModel):
    """DescribeInstanceTypeConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>instance-family</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例机型系列</strong>】进行过滤。实例机型系列形如：S1、I1、M1等。具体取值参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例类型</strong>】进行过滤。实例类型形如：S5.12XLARGE128、S5.12XLARGE96等。具体取值参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为1。
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTypeConfigsResponse(AbstractModel):
    """DescribeInstanceTypeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypeConfigSet: 实例机型配置列表。
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceTypeConfigSet = None
        self._RequestId = None

    @property
    def InstanceTypeConfigSet(self):
        return self._InstanceTypeConfigSet

    @InstanceTypeConfigSet.setter
    def InstanceTypeConfigSet(self, InstanceTypeConfigSet):
        self._InstanceTypeConfigSet = InstanceTypeConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self._InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self._InstanceTypeConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 一个操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceVncUrl: 实例的管理终端地址。
        :type InstanceVncUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceVncUrl = None
        self._RequestId = None

    @property
    def InstanceVncUrl(self):
        return self._InstanceVncUrl

    @InstanceVncUrl.setter
    def InstanceVncUrl(self, InstanceVncUrl):
        self._InstanceVncUrl = InstanceVncUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceVncUrl = params.get("InstanceVncUrl")
        self._RequestId = params.get("RequestId")


class DescribeInstancesActionTimerRequest(AbstractModel):
    """DescribeInstancesActionTimer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionTimerIds: 定时任务ID列表。
        :type ActionTimerIds: list of str
        :param _InstanceIds: 按照一个或者多个实例ID查询。
        :type InstanceIds: list of str
        :param _TimerAction: 定时任务执行时间，格式如：2018-05-01 19:00:00，必须大于当前时间5分钟。
        :type TimerAction: str
        :param _EndActionTime: 执行时间的结束范围，用于条件筛选，格式如2018-05-01 19:00:00。
        :type EndActionTime: str
        :param _StartActionTime: 执行时间的开始范围，用于条件筛选，格式如2018-05-01 19:00:00。
        :type StartActionTime: str
        :param _StatusList: 定时任务状态列表。<br><li>UNDO：未执行<br><li>DOING：正在执行<br><li>DONE：执行完成。
        :type StatusList: list of str
        """
        self._ActionTimerIds = None
        self._InstanceIds = None
        self._TimerAction = None
        self._EndActionTime = None
        self._StartActionTime = None
        self._StatusList = None

    @property
    def ActionTimerIds(self):
        return self._ActionTimerIds

    @ActionTimerIds.setter
    def ActionTimerIds(self, ActionTimerIds):
        self._ActionTimerIds = ActionTimerIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def TimerAction(self):
        return self._TimerAction

    @TimerAction.setter
    def TimerAction(self, TimerAction):
        self._TimerAction = TimerAction

    @property
    def EndActionTime(self):
        return self._EndActionTime

    @EndActionTime.setter
    def EndActionTime(self, EndActionTime):
        self._EndActionTime = EndActionTime

    @property
    def StartActionTime(self):
        return self._StartActionTime

    @StartActionTime.setter
    def StartActionTime(self, StartActionTime):
        self._StartActionTime = StartActionTime

    @property
    def StatusList(self):
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList


    def _deserialize(self, params):
        self._ActionTimerIds = params.get("ActionTimerIds")
        self._InstanceIds = params.get("InstanceIds")
        self._TimerAction = params.get("TimerAction")
        self._EndActionTime = params.get("EndActionTime")
        self._StartActionTime = params.get("StartActionTime")
        self._StatusList = params.get("StatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesActionTimerResponse(AbstractModel):
    """DescribeInstancesActionTimer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionTimers: 定时任务信息列表。
        :type ActionTimers: list of ActionTimer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActionTimers = None
        self._RequestId = None

    @property
    def ActionTimers(self):
        return self._ActionTimers

    @ActionTimers.setter
    def ActionTimers(self, ActionTimers):
        self._ActionTimers = ActionTimers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ActionTimers") is not None:
            self._ActionTimers = []
            for item in params.get("ActionTimers"):
                obj = ActionTimer()
                obj._deserialize(item)
                self._ActionTimers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesModificationRequest(AbstractModel):
    """DescribeInstancesModification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待查询的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为20。
        :type InstanceIds: list of str
        :param _Filters: <li><strong>status</strong></li>
<p style="padding-left: 30px;">按照【<strong>配置规格状态</strong>】进行过滤。配置规格状态形如：SELL、UNAVAILABLE。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为2。
        :type Filters: list of Filter
        """
        self._InstanceIds = None
        self._Filters = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesModificationResponse(AbstractModel):
    """DescribeInstancesModification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例调整的机型配置的数量。
        :type TotalCount: int
        :param _InstanceTypeConfigStatusSet: 实例支持调整的机型配置列表。
        :type InstanceTypeConfigStatusSet: list of InstanceTypeConfigStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceTypeConfigStatusSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceTypeConfigStatusSet(self):
        return self._InstanceTypeConfigStatusSet

    @InstanceTypeConfigStatusSet.setter
    def InstanceTypeConfigStatusSet(self, InstanceTypeConfigStatusSet):
        self._InstanceTypeConfigStatusSet = InstanceTypeConfigStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceTypeConfigStatusSet") is not None:
            self._InstanceTypeConfigStatusSet = []
            for item in params.get("InstanceTypeConfigStatusSet"):
                obj = InstanceTypeConfigStatus()
                obj._deserialize(item)
                self._InstanceTypeConfigStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesOperationLimitRequest(AbstractModel):
    """DescribeInstancesOperationLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 按照一个或者多个实例ID查询，可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)API返回值中的InstanceId获取。实例ID形如：ins-xxxxxxxx。（此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的ids.N一节）。每次请求的实例的上限为100。
        :type InstanceIds: list of str
        :param _Operation: 实例操作。
<li> INSTANCE_DEGRADE：实例降配操作</li>
        :type Operation: str
        """
        self._InstanceIds = None
        self._Operation = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesOperationLimitResponse(AbstractModel):
    """DescribeInstancesOperationLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceOperationLimitSet: 该参数表示调整配置操作（降配）限制次数查询。
        :type InstanceOperationLimitSet: list of OperationCountLimit
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceOperationLimitSet = None
        self._RequestId = None

    @property
    def InstanceOperationLimitSet(self):
        return self._InstanceOperationLimitSet

    @InstanceOperationLimitSet.setter
    def InstanceOperationLimitSet(self, InstanceOperationLimitSet):
        self._InstanceOperationLimitSet = InstanceOperationLimitSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceOperationLimitSet") is not None:
            self._InstanceOperationLimitSet = []
            for item in params.get("InstanceOperationLimitSet"):
                obj = OperationCountLimit()
                obj._deserialize(item)
                self._InstanceOperationLimitSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID例如：`ins-xxxxxxxx`。（此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的`ids.N`一节）。每次请求的实例的上限为100。参数不支持同时指定`InstanceIds`和`Filters`。
        :type InstanceIds: list of str
        :param _Filters: <li><strong>zone</strong></li> <p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区例如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p> <li><strong>project-id</strong></li> <p style="padding-left: 30px;">按照【<strong>项目ID</strong>】进行过滤，可通过调用[DescribeProjects](https://cloud.tencent.com/document/api/651/78725)查询已创建的项目列表或登录[控制台](https://console.cloud.tencent.com/cvm/index)进行查看；也可以调用[AddProject](https://cloud.tencent.com/document/api/651/81952)创建新的项目。项目ID例如：1002189。</p><p style="padding-left: 30px;">类型：Integer</p><p style="padding-left: 30px;">必选：否</p> <li><strong>host-id</strong></li> <p style="padding-left: 30px;">按照【<strong>[CDH](https://cloud.tencent.com/document/product/416) ID</strong>】进行过滤。[CDH](https://cloud.tencent.com/document/product/416) ID例如：host-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>dedicated-cluster-id</strong></li> <p style="padding-left: 30px;">按照【<strong>[CDC](https://cloud.tencent.com/document/product/1346) ID</strong>】进行过滤。[CDC](https://cloud.tencent.com/document/product/1346) ID例如：cluster-xxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>vpc-id</strong></li> <p style="padding-left: 30px;">按照【<strong>VPC ID</strong>】进行过滤。VPC ID例如：vpc-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>subnet-id</strong></li> <p style="padding-left: 30px;">按照【<strong>子网ID</strong>】进行过滤。子网ID例如：subnet-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>instance-id</strong></li> <p style="padding-left: 30px;">按照【<strong>实例ID</strong>】进行过滤。实例ID例如：ins-xxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>uuid</strong></li> <p style="padding-left: 30px;">按照【<strong>实例UUID</strong>】进行过滤。实例UUID例如：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>security-group-id</strong></li> <p style="padding-left: 30px;">按照【<strong>安全组ID</strong>】进行过滤。安全组ID例如: sg-8jlk3f3r。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>instance-name</strong></li> <p style="padding-left: 30px;">按照【<strong>实例名称</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>instance-charge-type</strong></li> <p style="padding-left: 30px;">按照【<strong>实例计费模式</strong>】进行过滤。(PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费 | CDHPAID：表示[CDH](https://cloud.tencent.com/document/product/416)付费，即只对[CDH](https://cloud.tencent.com/document/product/416)计费，不对[CDH](https://cloud.tencent.com/document/product/416)上的实例计费。)</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>instance-state</strong></li> <p style="padding-left: 30px;">按照【<strong>实例状态</strong>】进行过滤。状态类型详见[实例状态表](https://cloud.tencent.com/document/api/213/15753#InstanceStatus)</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>private-ip-address</strong></li> <p style="padding-left: 30px;">按照【<strong>实例主网卡的内网IP</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>public-ip-address</strong></li> <p style="padding-left: 30px;">按照【<strong>实例主网卡的公网IP</strong>】进行过滤，包含实例创建时自动分配的IP和实例创建后手动绑定的弹性IP。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>ipv6-address</strong></li> <p style="padding-left: 30px;">按照【<strong>实例的IPv6地址</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>tag-key</strong></li> <p style="padding-left: 30px;">按照【<strong>标签键</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>tag-value</strong></li> <p style="padding-left: 30px;">按照【<strong>标签值</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>tag:tag-key</strong></li> <p style="padding-left: 30px;">按照【<strong>标签键值对</strong>】进行过滤。tag-key使用具体的标签键进行替换。使用请参考示例2。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><li><strong>creation-start-time</strong></li> <p style="padding-left: 30px;">按照【<strong>实例创建起始时间</strong>】进行过滤。例如：2023-06-01 00:00:00。
</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>creation-end-time</strong></li> <p style="padding-left: 30px;">按照【<strong>实例创建截止时间</strong>】进行过滤。例如：2023-06-01 00:00:00。
</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> 每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`InstanceIds`和`Filters`。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _InstanceSet: 实例详细信息列表。
        :type InstanceSet: list of Instance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesStatusRequest(AbstractModel):
    """DescribeInstancesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：`ins-11112222`。此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的`ids.N`一节）。每次请求的实例的上限为100。
        :type InstanceIds: list of str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesStatusResponse(AbstractModel):
    """DescribeInstancesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例状态数量。
        :type TotalCount: int
        :param _InstanceStatusSet: [实例状态](https://cloud.tencent.com/document/api/213/15753#InstanceStatus) 列表。
        :type InstanceStatusSet: list of InstanceStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceStatusSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceStatusSet(self):
        return self._InstanceStatusSet

    @InstanceStatusSet.setter
    def InstanceStatusSet(self, InstanceStatusSet):
        self._InstanceStatusSet = InstanceStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceStatusSet") is not None:
            self._InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = InstanceStatus()
                obj._deserialize(item)
                self._InstanceStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInternetChargeTypeConfigsRequest(AbstractModel):
    """DescribeInternetChargeTypeConfigs请求参数结构体

    """


class DescribeInternetChargeTypeConfigsResponse(AbstractModel):
    """DescribeInternetChargeTypeConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InternetChargeTypeConfigSet: 网络计费类型配置。
        :type InternetChargeTypeConfigSet: list of InternetChargeTypeConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InternetChargeTypeConfigSet = None
        self._RequestId = None

    @property
    def InternetChargeTypeConfigSet(self):
        return self._InternetChargeTypeConfigSet

    @InternetChargeTypeConfigSet.setter
    def InternetChargeTypeConfigSet(self, InternetChargeTypeConfigSet):
        self._InternetChargeTypeConfigSet = InternetChargeTypeConfigSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InternetChargeTypeConfigSet") is not None:
            self._InternetChargeTypeConfigSet = []
            for item in params.get("InternetChargeTypeConfigSet"):
                obj = InternetChargeTypeConfig()
                obj._deserialize(item)
                self._InternetChargeTypeConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 密钥对ID，密钥对ID形如：`skey-11112222`（此接口支持同时传入多个ID进行过滤。此参数的具体格式可参考 API [简介](https://cloud.tencent.com/document/api/213/15688)的 `id.N` 一节）。参数不支持同时指定 `KeyIds` 和 `Filters`。密钥对ID可以通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询。
        :type KeyIds: list of str
        :param _Filters: 过滤条件。
<li> project-id - Integer - 是否必填：否 -（过滤条件）按照项目ID过滤。可以通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID，或者调用接口 [DescribeProject](https://cloud.tencent.com/document/api/378/4400)，取返回信息中的projectId获取项目ID。</li>
<li> key-name - String - 是否必填：否 -（过滤条件）按照密钥对名称过滤。</li>
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键过滤。</li>
<li> tag-value - String - 是否必填：否 -（过滤条件）按照标签值过滤。</li>
<li> tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对过滤。tag-key使用具体的标签键进行替换。</li>
参数不支持同时指定 `KeyIds` 和 `Filters`。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._KeyIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._KeyIds = params.get("KeyIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeyPairsResponse(AbstractModel):
    """DescribeKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的密钥对数量。
        :type TotalCount: int
        :param _KeyPairSet: 密钥对详细信息列表。
        :type KeyPairSet: list of KeyPair
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KeyPairSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KeyPairSet(self):
        return self._KeyPairSet

    @KeyPairSet.setter
    def KeyPairSet(self, KeyPairSet):
        self._KeyPairSet = KeyPairSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KeyPairSet") is not None:
            self._KeyPairSet = []
            for item in params.get("KeyPairSet"):
                obj = KeyPair()
                obj._deserialize(item)
                self._KeyPairSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLaunchTemplateVersionsRequest(AbstractModel):
    """DescribeLaunchTemplateVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersions: 实例启动模板列表。
        :type LaunchTemplateVersions: list of int non-negative
        :param _MinVersion: 通过范围指定版本时的最小版本号，默认为0。
        :type MinVersion: int
        :param _MaxVersion: 过范围指定版本时的最大版本号，默认为30。
        :type MaxVersion: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _DefaultVersion: 是否查询默认版本。该参数不可与LaunchTemplateVersions同时指定。
        :type DefaultVersion: bool
        """
        self._LaunchTemplateId = None
        self._LaunchTemplateVersions = None
        self._MinVersion = None
        self._MaxVersion = None
        self._Offset = None
        self._Limit = None
        self._DefaultVersion = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersions(self):
        return self._LaunchTemplateVersions

    @LaunchTemplateVersions.setter
    def LaunchTemplateVersions(self, LaunchTemplateVersions):
        self._LaunchTemplateVersions = LaunchTemplateVersions

    @property
    def MinVersion(self):
        return self._MinVersion

    @MinVersion.setter
    def MinVersion(self, MinVersion):
        self._MinVersion = MinVersion

    @property
    def MaxVersion(self):
        return self._MaxVersion

    @MaxVersion.setter
    def MaxVersion(self, MaxVersion):
        self._MaxVersion = MaxVersion

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

    @property
    def DefaultVersion(self):
        return self._DefaultVersion

    @DefaultVersion.setter
    def DefaultVersion(self, DefaultVersion):
        self._DefaultVersion = DefaultVersion


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        self._MinVersion = params.get("MinVersion")
        self._MaxVersion = params.get("MaxVersion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaunchTemplateVersionsResponse(AbstractModel):
    """DescribeLaunchTemplateVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例启动模板总数。
        :type TotalCount: int
        :param _LaunchTemplateVersionSet: 实例启动模板版本集合。
        :type LaunchTemplateVersionSet: list of LaunchTemplateVersionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LaunchTemplateVersionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LaunchTemplateVersionSet(self):
        return self._LaunchTemplateVersionSet

    @LaunchTemplateVersionSet.setter
    def LaunchTemplateVersionSet(self, LaunchTemplateVersionSet):
        self._LaunchTemplateVersionSet = LaunchTemplateVersionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateVersionSet") is not None:
            self._LaunchTemplateVersionSet = []
            for item in params.get("LaunchTemplateVersionSet"):
                obj = LaunchTemplateVersionInfo()
                obj._deserialize(item)
                self._LaunchTemplateVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLaunchTemplatesRequest(AbstractModel):
    """DescribeLaunchTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateIds: 启动模板ID，一个或者多个启动模板ID。若未指定，则显示用户所有模板。
        :type LaunchTemplateIds: list of str
        :param _Filters: <p style="padding-left: 30px;">按照【<strong>LaunchTemplateName</strong>】进行过滤。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`LaunchTemplateIds`和`Filters`。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._LaunchTemplateIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def LaunchTemplateIds(self):
        return self._LaunchTemplateIds

    @LaunchTemplateIds.setter
    def LaunchTemplateIds(self, LaunchTemplateIds):
        self._LaunchTemplateIds = LaunchTemplateIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._LaunchTemplateIds = params.get("LaunchTemplateIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaunchTemplatesResponse(AbstractModel):
    """DescribeLaunchTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例模板数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _LaunchTemplateSet: 实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateSet: list of LaunchTemplateInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LaunchTemplateSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LaunchTemplateSet(self):
        return self._LaunchTemplateSet

    @LaunchTemplateSet.setter
    def LaunchTemplateSet(self, LaunchTemplateSet):
        self._LaunchTemplateSet = LaunchTemplateSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateSet") is not None:
            self._LaunchTemplateSet = []
            for item in params.get("LaunchTemplateSet"):
                obj = LaunchTemplateInfo()
                obj._deserialize(item)
                self._LaunchTemplateSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 地域数量。
        :type TotalCount: int
        :param _RegionSet: 地域列表信息。
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReservedInstancesConfigInfosRequest(AbstractModel):
    """DescribeReservedInstancesConfigInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: zone
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
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesConfigInfosResponse(AbstractModel):
    """DescribeReservedInstancesConfigInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReservedInstanceConfigInfos: 预留实例静态配置信息列表。
        :type ReservedInstanceConfigInfos: list of ReservedInstanceConfigInfoItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReservedInstanceConfigInfos = None
        self._RequestId = None

    @property
    def ReservedInstanceConfigInfos(self):
        return self._ReservedInstanceConfigInfos

    @ReservedInstanceConfigInfos.setter
    def ReservedInstanceConfigInfos(self, ReservedInstanceConfigInfos):
        self._ReservedInstanceConfigInfos = ReservedInstanceConfigInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReservedInstanceConfigInfos") is not None:
            self._ReservedInstanceConfigInfos = []
            for item in params.get("ReservedInstanceConfigInfos"):
                obj = ReservedInstanceConfigInfoItem()
                obj._deserialize(item)
                self._ReservedInstanceConfigInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReservedInstancesOfferingsRequest(AbstractModel):
    """DescribeReservedInstancesOfferings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DryRun: 试运行, 默认为 false。
        :type DryRun: bool
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _MaxDuration: 以最大有效期作为过滤参数。
计量单位: 秒
默认为 94608000。
        :type MaxDuration: int
        :param _MinDuration: 以最小有效期作为过滤参数。
计量单位: 秒
默认为 2592000。
        :type MinDuration: int
        :param _Filters: <li><strong>zone</strong></li>
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
        self._DryRun = None
        self._Offset = None
        self._Limit = None
        self._MaxDuration = None
        self._MinDuration = None
        self._Filters = None

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

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

    @property
    def MaxDuration(self):
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def MinDuration(self):
        return self._MinDuration

    @MinDuration.setter
    def MinDuration(self, MinDuration):
        self._MinDuration = MinDuration

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MaxDuration = params.get("MaxDuration")
        self._MinDuration = params.get("MinDuration")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesOfferingsResponse(AbstractModel):
    """DescribeReservedInstancesOfferings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的预留实例计费数量。
        :type TotalCount: int
        :param _ReservedInstancesOfferingsSet: 符合条件的预留实例计费列表。
        :type ReservedInstancesOfferingsSet: list of ReservedInstancesOffering
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReservedInstancesOfferingsSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReservedInstancesOfferingsSet(self):
        return self._ReservedInstancesOfferingsSet

    @ReservedInstancesOfferingsSet.setter
    def ReservedInstancesOfferingsSet(self, ReservedInstancesOfferingsSet):
        self._ReservedInstancesOfferingsSet = ReservedInstancesOfferingsSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ReservedInstancesOfferingsSet") is not None:
            self._ReservedInstancesOfferingsSet = []
            for item in params.get("ReservedInstancesOfferingsSet"):
                obj = ReservedInstancesOffering()
                obj._deserialize(item)
                self._ReservedInstancesOfferingsSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReservedInstancesRequest(AbstractModel):
    """DescribeReservedInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DryRun: 试运行。默认为 false。
        :type DryRun: bool
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Filters: <li><strong>zone</strong></li>
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
        self._DryRun = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

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

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesResponse(AbstractModel):
    """DescribeReservedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的预留实例计费数量。
        :type TotalCount: int
        :param _ReservedInstancesSet: 符合条件的预留实例计费列表。
        :type ReservedInstancesSet: list of ReservedInstances
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReservedInstancesSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReservedInstancesSet(self):
        return self._ReservedInstancesSet

    @ReservedInstancesSet.setter
    def ReservedInstancesSet(self, ReservedInstancesSet):
        self._ReservedInstancesSet = ReservedInstancesSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ReservedInstancesSet") is not None:
            self._ReservedInstancesSet = []
            for item in params.get("ReservedInstancesSet"):
                obj = ReservedInstances()
                obj._deserialize(item)
                self._ReservedInstancesSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Product: 按照指定的产品类型查询，支持取值：

- `CVM`：云服务器
- `CDH`：专用宿主机
- `CPM2.0`：裸金属云服务器

未传入或为空时，默认查询全部产品类型。
        :type Product: str
        :param _TaskStatus: 按照一个或多个任务状态ID进行过滤。
`TaskStatus`（任务状态ID）与任务状态中文名的对应关系如下：

- `1`：待授权
- `2`：处理中
- `3`：已结束
- `4`：已预约
- `5`：已取消
- `6`：已避免

各任务状态的具体含义，可参考 [任务状态](https://cloud.tencent.com/document/product/213/67789#.E4.BB.BB.E5.8A.A1.E7.8A.B6.E6.80.81)。
        :type TaskStatus: list of int
        :param _TaskTypeIds: 按照一个或多个任务类型ID进行过滤。

`TaskTypeId`（任务类型ID）与任务类型中文名的对应关系如下：

- `101`：实例运行隐患
- `102`：实例运行异常
- `103`：实例硬盘异常
- `104`：实例网络连接异常
- `105`：实例运行预警
- `106`：实例硬盘预警
- `107`：实例维护升级

各任务类型的具体含义，可参考 [维修任务分类](https://cloud.tencent.com/document/product/213/67789#.E7.BB.B4.E4.BF.AE.E4.BB.BB.E5.8A.A1.E5.88.86.E7.B1.BB)。
        :type TaskTypeIds: list of int
        :param _TaskIds: 按照一个或者多个任务ID查询。任务ID形如：`rep-xxxxxxxx`。
        :type TaskIds: list of str
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：`ins-xxxxxxxx`。
        :type InstanceIds: list of str
        :param _Aliases: 按照一个或者多个实例名称查询。
        :type Aliases: list of str
        :param _StartDate: 时间查询区间的起始位置，会根据任务创建时间`CreateTime`进行过滤。未传入时默认为当天`00:00:00`。
        :type StartDate: str
        :param _EndDate: 时间查询区间的终止位置，会根据任务创建时间`CreateTime`进行过滤。未传入时默认为当前时刻。
        :type EndDate: str
        :param _OrderField: 指定返回维修任务列表的排序字段，目前支持：

- `CreateTime`：任务创建时间
- `AuthTime`：任务授权时间
- `EndTime`：任务结束时间

未传入时或为空时，默认按`CreateTime`字段进行排序。
        :type OrderField: str
        :param _Order: 排序方式，目前支持：

- `0`：升序（默认）
- `1`：降序

未传入或为空时，默认按升序排序。

        :type Order: int
        """
        self._Limit = None
        self._Offset = None
        self._Product = None
        self._TaskStatus = None
        self._TaskTypeIds = None
        self._TaskIds = None
        self._InstanceIds = None
        self._Aliases = None
        self._StartDate = None
        self._EndDate = None
        self._OrderField = None
        self._Order = None

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

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskTypeIds(self):
        return self._TaskTypeIds

    @TaskTypeIds.setter
    def TaskTypeIds(self, TaskTypeIds):
        self._TaskTypeIds = TaskTypeIds

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Aliases(self):
        return self._Aliases

    @Aliases.setter
    def Aliases(self, Aliases):
        self._Aliases = Aliases

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Product = params.get("Product")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskTypeIds = params.get("TaskTypeIds")
        self._TaskIds = params.get("TaskIds")
        self._InstanceIds = params.get("InstanceIds")
        self._Aliases = params.get("Aliases")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询返回的维修任务总数量。
        :type TotalCount: int
        :param _RepairTaskInfoSet: 查询返回的维修任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RepairTaskInfoSet: list of RepairTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RepairTaskInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RepairTaskInfoSet(self):
        return self._RepairTaskInfoSet

    @RepairTaskInfoSet.setter
    def RepairTaskInfoSet(self, RepairTaskInfoSet):
        self._RepairTaskInfoSet = RepairTaskInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RepairTaskInfoSet") is not None:
            self._RepairTaskInfoSet = []
            for item in params.get("RepairTaskInfoSet"):
                obj = RepairTaskInfo()
                obj._deserialize(item)
                self._RepairTaskInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeZoneInstanceConfigInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">按照【<strong>可用区</strong>】进行过滤。可用区形如：ap-guangzhou-1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">可选项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a></p>
<li><strong>instance-family</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例机型系列</strong>】进行过滤。实例机型系列形如：S1、I1、M1等。具体取值参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例机型</strong>】进行过滤。不同实例机型指定了不同的资源规格，具体取值可通过调用接口 [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/product/213/15749) 来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则默认查询筛选条件下所有机型。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>instance-charge-type</strong></li>
<p style="padding-left: 30px;">按照【<strong>实例计费模式</strong>】进行过滤。(PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费 )</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>sort-keys</strong></li>
<p style="padding-left: 30px;">按关键字进行排序,格式为排序字段加排序方式，中间用冒号分隔。 例如： 按cpu数逆序排序 "cpu:desc", 按mem大小顺序排序 "mem:asc"</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为100。
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeZoneInstanceConfigInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypeQuotaSet: 可用区机型配置列表。
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceTypeQuotaSet = None
        self._RequestId = None

    @property
    def InstanceTypeQuotaSet(self):
        return self._InstanceTypeQuotaSet

    @InstanceTypeQuotaSet.setter
    def InstanceTypeQuotaSet(self, InstanceTypeQuotaSet):
        self._InstanceTypeQuotaSet = InstanceTypeQuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self._InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self._InstanceTypeQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可用区数量。
        :type TotalCount: int
        :param _ZoneSet: 可用区列表信息。
        :type ZoneSet: list of ZoneInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID，每次请求批量实例的上限为100。<br><br>可以通过以下方式获取可用的实例ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/index)查询实例ID。<br><li>通过调用接口 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) ，取返回信息中的 `InstanceId` 获取实例ID。
        :type InstanceIds: list of str
        :param _KeyIds: 密钥对ID列表，每次请求批量密钥对的上限为100。密钥对ID形如：`skey-11112222`。<br><br>可以通过以下方式获取可用的密钥ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) ，取返回信息中的 `KeyId` 获取密钥对ID。
        :type KeyIds: list of str
        :param _ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再解绑密钥。取值范围：<br><li>true：表示在正常关机失败后进行强制关机。<br><li>false：表示在正常关机失败后不进行强制关机。<br><br>默认取值：false。
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._KeyIds = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._KeyIds = params.get("KeyIds")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 要解绑的`安全组ID`，类似sg-efil73jd，只支持解绑单个安全组。
        :type SecurityGroupIds: list of str
        :param _InstanceIds: 被解绑的`实例ID`，类似ins-lesecurk，支持指定多个实例，每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DisasterRecoverGroup(AbstractModel):
    """容灾组信息

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupId: 分散置放群组id。
        :type DisasterRecoverGroupId: str
        :param _Name: 分散置放群组名称，长度1-60个字符。
        :type Name: str
        :param _Type: 分散置放群组类型，取值范围：<br><li>HOST：物理机<br><li>SW：交换机<br><li>RACK：机架
        :type Type: str
        :param _CvmQuotaTotal: 分散置放群组内最大容纳云服务器数量。
        :type CvmQuotaTotal: int
        :param _CurrentNum: 分散置放群组内云服务器当前数量。
        :type CurrentNum: int
        :param _InstanceIds: 分散置放群组内，云服务器id列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param _CreateTime: 分散置放群组创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._DisasterRecoverGroupId = None
        self._Name = None
        self._Type = None
        self._CvmQuotaTotal = None
        self._CurrentNum = None
        self._InstanceIds = None
        self._CreateTime = None

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CvmQuotaTotal(self):
        return self._CvmQuotaTotal

    @CvmQuotaTotal.setter
    def CvmQuotaTotal(self, CvmQuotaTotal):
        self._CvmQuotaTotal = CvmQuotaTotal

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CvmQuotaTotal = params.get("CvmQuotaTotal")
        self._CurrentNum = params.get("CurrentNum")
        self._InstanceIds = params.get("InstanceIds")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisasterRecoverGroupQuota(AbstractModel):
    """置放群组配置数据

    """

    def __init__(self):
        r"""
        :param _GroupQuota: 可创建置放群组数量的上限。
        :type GroupQuota: int
        :param _CurrentNum: 当前用户已经创建的置放群组数量。
        :type CurrentNum: int
        :param _CvmInHostGroupQuota: 物理机类型容灾组内实例的配额数。
        :type CvmInHostGroupQuota: int
        :param _CvmInSwitchGroupQuota: 交换机类型容灾组内实例的配额数。
        :type CvmInSwitchGroupQuota: int
        :param _CvmInRackGroupQuota: 机架类型容灾组内实例的配额数。
        :type CvmInRackGroupQuota: int
        """
        self._GroupQuota = None
        self._CurrentNum = None
        self._CvmInHostGroupQuota = None
        self._CvmInSwitchGroupQuota = None
        self._CvmInRackGroupQuota = None

    @property
    def GroupQuota(self):
        return self._GroupQuota

    @GroupQuota.setter
    def GroupQuota(self, GroupQuota):
        self._GroupQuota = GroupQuota

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def CvmInHostGroupQuota(self):
        return self._CvmInHostGroupQuota

    @CvmInHostGroupQuota.setter
    def CvmInHostGroupQuota(self, CvmInHostGroupQuota):
        self._CvmInHostGroupQuota = CvmInHostGroupQuota

    @property
    def CvmInSwitchGroupQuota(self):
        return self._CvmInSwitchGroupQuota

    @CvmInSwitchGroupQuota.setter
    def CvmInSwitchGroupQuota(self, CvmInSwitchGroupQuota):
        self._CvmInSwitchGroupQuota = CvmInSwitchGroupQuota

    @property
    def CvmInRackGroupQuota(self):
        return self._CvmInRackGroupQuota

    @CvmInRackGroupQuota.setter
    def CvmInRackGroupQuota(self, CvmInRackGroupQuota):
        self._CvmInRackGroupQuota = CvmInRackGroupQuota


    def _deserialize(self, params):
        self._GroupQuota = params.get("GroupQuota")
        self._CurrentNum = params.get("CurrentNum")
        self._CvmInHostGroupQuota = params.get("CvmInHostGroupQuota")
        self._CvmInSwitchGroupQuota = params.get("CvmInSwitchGroupQuota")
        self._CvmInRackGroupQuota = params.get("CvmInRackGroupQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        r"""
        :param _SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.cvm.v20170312.models.RunSecurityServiceEnabled`
        :param _MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.cvm.v20170312.models.RunMonitorServiceEnabled`
        :param _AutomationService: 开启云自动化助手服务（TencentCloud Automation Tools，TAT）。若不指定该参数，则公共镜像默认开启云自动化助手服务，其他镜像默认不开启云自动化助手服务。
        :type AutomationService: :class:`tencentcloud.cvm.v20170312.models.RunAutomationServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None

    @property
    def SecurityService(self):
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        self._AutomationService = AutomationService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self._AutomationService = RunAutomationServiceEnabled()
            self._AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterRescueModeRequest(AbstractModel):
    """EnterRescueMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要进入救援模式的实例id
        :type InstanceId: str
        :param _Password: 救援模式下系统密码
        :type Password: str
        :param _Username: 救援模式下系统用户名
        :type Username: str
        :param _ForceStop: 是否强制关机
        :type ForceStop: bool
        """
        self._InstanceId = None
        self._Password = None
        self._Username = None
        self._ForceStop = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._Username = params.get("Username")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterRescueModeResponse(AbstractModel):
    """EnterRescueMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ExitRescueModeRequest(AbstractModel):
    """ExitRescueMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 退出救援模式的实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExitRescueModeResponse(AbstractModel):
    """ExitRescueMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ExportImagesRequest(AbstractModel):
    """ExportImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketName: COS存储桶名称
        :type BucketName: str
        :param _ImageIds: 镜像ID列表
        :type ImageIds: list of str
        :param _ExportFormat: 镜像文件导出格式。取值范围：RAW，QCOW2，VHD，VMDK。默认为RAW
        :type ExportFormat: str
        :param _FileNamePrefixList: 导出文件的名称前缀列表
        :type FileNamePrefixList: list of str
        :param _OnlyExportRootDisk: 是否只导出系统盘
        :type OnlyExportRootDisk: bool
        :param _DryRun: 检测镜像是否支持导出
        :type DryRun: bool
        :param _RoleName: 角色名称。默认为CVM_QcsRole，发起请求前请确认是否存在该角色，以及是否已正确配置COS写入权限。
        :type RoleName: str
        """
        self._BucketName = None
        self._ImageIds = None
        self._ExportFormat = None
        self._FileNamePrefixList = None
        self._OnlyExportRootDisk = None
        self._DryRun = None
        self._RoleName = None

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def ExportFormat(self):
        return self._ExportFormat

    @ExportFormat.setter
    def ExportFormat(self, ExportFormat):
        self._ExportFormat = ExportFormat

    @property
    def FileNamePrefixList(self):
        return self._FileNamePrefixList

    @FileNamePrefixList.setter
    def FileNamePrefixList(self, FileNamePrefixList):
        self._FileNamePrefixList = FileNamePrefixList

    @property
    def OnlyExportRootDisk(self):
        return self._OnlyExportRootDisk

    @OnlyExportRootDisk.setter
    def OnlyExportRootDisk(self, OnlyExportRootDisk):
        self._OnlyExportRootDisk = OnlyExportRootDisk

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._ImageIds = params.get("ImageIds")
        self._ExportFormat = params.get("ExportFormat")
        self._FileNamePrefixList = params.get("FileNamePrefixList")
        self._OnlyExportRootDisk = params.get("OnlyExportRootDisk")
        self._DryRun = params.get("DryRun")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportImagesResponse(AbstractModel):
    """ExportImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 导出镜像任务ID
        :type TaskId: int
        :param _CosPaths: 导出镜像的COS文件名列表
        :type CosPaths: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._CosPaths = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CosPaths(self):
        return self._CosPaths

    @CosPaths.setter
    def CosPaths(self, CosPaths):
        self._CosPaths = CosPaths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._CosPaths = params.get("CosPaths")
        self._RequestId = params.get("RequestId")


class Externals(AbstractModel):
    """扩展数据

    """

    def __init__(self):
        r"""
        :param _ReleaseAddress: 释放地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseAddress: bool
        :param _UnsupportNetworks: 不支持的网络类型，取值范围：<br><li>BASIC：基础网络<br><li>VPC1.0：私有网络VPC1.0
注意：此字段可能返回 null，表示取不到有效值。
        :type UnsupportNetworks: list of str
        :param _StorageBlockAttr: HDD本地存储属性
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageBlockAttr: :class:`tencentcloud.cvm.v20170312.models.StorageBlock`
        """
        self._ReleaseAddress = None
        self._UnsupportNetworks = None
        self._StorageBlockAttr = None

    @property
    def ReleaseAddress(self):
        return self._ReleaseAddress

    @ReleaseAddress.setter
    def ReleaseAddress(self, ReleaseAddress):
        self._ReleaseAddress = ReleaseAddress

    @property
    def UnsupportNetworks(self):
        return self._UnsupportNetworks

    @UnsupportNetworks.setter
    def UnsupportNetworks(self, UnsupportNetworks):
        self._UnsupportNetworks = UnsupportNetworks

    @property
    def StorageBlockAttr(self):
        return self._StorageBlockAttr

    @StorageBlockAttr.setter
    def StorageBlockAttr(self, StorageBlockAttr):
        self._StorageBlockAttr = StorageBlockAttr


    def _deserialize(self, params):
        self._ReleaseAddress = params.get("ReleaseAddress")
        self._UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self._StorageBlockAttr = StorageBlock()
            self._StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GPUInfo(AbstractModel):
    """实例GPU信息

    """

    def __init__(self):
        r"""
        :param _GPUCount: 实例GPU个数。值小于1代表VGPU类型，大于1代表GPU直通类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUCount: float
        :param _GPUId: 实例GPU地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUId: list of str
        :param _GPUType: 实例GPU类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUType: str
        """
        self._GPUCount = None
        self._GPUId = None
        self._GPUType = None

    @property
    def GPUCount(self):
        return self._GPUCount

    @GPUCount.setter
    def GPUCount(self, GPUCount):
        self._GPUCount = GPUCount

    @property
    def GPUId(self):
        return self._GPUId

    @GPUId.setter
    def GPUId(self, GPUId):
        self._GPUId = GPUId

    @property
    def GPUType(self):
        return self._GPUType

    @GPUType.setter
    def GPUType(self, GPUType):
        self._GPUType = GPUType


    def _deserialize(self, params):
        self._GPUCount = params.get("GPUCount")
        self._GPUId = params.get("GPUId")
        self._GPUType = params.get("GPUType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostItem(AbstractModel):
    """专用宿主机实例详细信息

    """

    def __init__(self):
        r"""
        :param _Placement: 专用宿主机实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _HostId: 专用宿主机实例ID
        :type HostId: str
        :param _HostType: 专用宿主机实例类型
        :type HostType: str
        :param _HostName: 专用宿主机实例名称
        :type HostName: str
        :param _HostChargeType: 专用宿主机实例付费模式
        :type HostChargeType: str
        :param _RenewFlag: 专用宿主机实例自动续费标记
        :type RenewFlag: str
        :param _CreatedTime: 专用宿主机实例创建时间
        :type CreatedTime: str
        :param _ExpiredTime: 专用宿主机实例过期时间
        :type ExpiredTime: str
        :param _InstanceIds: 专用宿主机实例上已创建云子机的实例id列表
        :type InstanceIds: list of str
        :param _HostState: 专用宿主机实例状态
        :type HostState: str
        :param _HostIp: 专用宿主机实例IP
        :type HostIp: str
        :param _HostResource: 专用宿主机实例资源信息
        :type HostResource: :class:`tencentcloud.cvm.v20170312.models.HostResource`
        :param _CageId: 专用宿主机所属的围笼ID。该字段仅对金融专区围笼内的专用宿主机有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CageId: str
        :param _Tags: 专用宿主机关联的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._Placement = None
        self._HostId = None
        self._HostType = None
        self._HostName = None
        self._HostChargeType = None
        self._RenewFlag = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._InstanceIds = None
        self._HostState = None
        self._HostIp = None
        self._HostResource = None
        self._CageId = None
        self._Tags = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def HostType(self):
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def HostChargeType(self):
        return self._HostChargeType

    @HostChargeType.setter
    def HostChargeType(self, HostChargeType):
        self._HostChargeType = HostChargeType

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def HostState(self):
        return self._HostState

    @HostState.setter
    def HostState(self, HostState):
        self._HostState = HostState

    @property
    def HostIp(self):
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def HostResource(self):
        return self._HostResource

    @HostResource.setter
    def HostResource(self, HostResource):
        self._HostResource = HostResource

    @property
    def CageId(self):
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._HostId = params.get("HostId")
        self._HostType = params.get("HostType")
        self._HostName = params.get("HostName")
        self._HostChargeType = params.get("HostChargeType")
        self._RenewFlag = params.get("RenewFlag")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._InstanceIds = params.get("InstanceIds")
        self._HostState = params.get("HostState")
        self._HostIp = params.get("HostIp")
        if params.get("HostResource") is not None:
            self._HostResource = HostResource()
            self._HostResource._deserialize(params.get("HostResource"))
        self._CageId = params.get("CageId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostPriceInfo(AbstractModel):
    """cdh相关价格信息

    """

    def __init__(self):
        r"""
        :param _HostPrice: 描述了cdh实例相关的价格信息
        :type HostPrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        """
        self._HostPrice = None

    @property
    def HostPrice(self):
        return self._HostPrice

    @HostPrice.setter
    def HostPrice(self, HostPrice):
        self._HostPrice = HostPrice


    def _deserialize(self, params):
        if params.get("HostPrice") is not None:
            self._HostPrice = ItemPrice()
            self._HostPrice._deserialize(params.get("HostPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostResource(AbstractModel):
    """专用宿主机实例的资源信息

    """

    def __init__(self):
        r"""
        :param _CpuTotal: 专用宿主机实例总CPU核数
        :type CpuTotal: int
        :param _CpuAvailable: 专用宿主机实例可用CPU核数
        :type CpuAvailable: int
        :param _MemTotal: 专用宿主机实例总内存大小（单位为:GiB）
        :type MemTotal: float
        :param _MemAvailable: 专用宿主机实例可用内存大小（单位为:GiB）
        :type MemAvailable: float
        :param _DiskTotal: 专用宿主机实例总磁盘大小（单位为:GiB）
        :type DiskTotal: int
        :param _DiskAvailable: 专用宿主机实例可用磁盘大小（单位为:GiB）
        :type DiskAvailable: int
        :param _DiskType: 专用宿主机实例磁盘类型
        :type DiskType: str
        :param _GpuTotal: 专用宿主机实例总GPU卡数
        :type GpuTotal: int
        :param _GpuAvailable: 专用宿主机实例可用GPU卡数
        :type GpuAvailable: int
        :param _ExclusiveOwner: CDH owner
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveOwner: str
        """
        self._CpuTotal = None
        self._CpuAvailable = None
        self._MemTotal = None
        self._MemAvailable = None
        self._DiskTotal = None
        self._DiskAvailable = None
        self._DiskType = None
        self._GpuTotal = None
        self._GpuAvailable = None
        self._ExclusiveOwner = None

    @property
    def CpuTotal(self):
        return self._CpuTotal

    @CpuTotal.setter
    def CpuTotal(self, CpuTotal):
        self._CpuTotal = CpuTotal

    @property
    def CpuAvailable(self):
        return self._CpuAvailable

    @CpuAvailable.setter
    def CpuAvailable(self, CpuAvailable):
        self._CpuAvailable = CpuAvailable

    @property
    def MemTotal(self):
        return self._MemTotal

    @MemTotal.setter
    def MemTotal(self, MemTotal):
        self._MemTotal = MemTotal

    @property
    def MemAvailable(self):
        return self._MemAvailable

    @MemAvailable.setter
    def MemAvailable(self, MemAvailable):
        self._MemAvailable = MemAvailable

    @property
    def DiskTotal(self):
        return self._DiskTotal

    @DiskTotal.setter
    def DiskTotal(self, DiskTotal):
        self._DiskTotal = DiskTotal

    @property
    def DiskAvailable(self):
        return self._DiskAvailable

    @DiskAvailable.setter
    def DiskAvailable(self, DiskAvailable):
        self._DiskAvailable = DiskAvailable

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def GpuTotal(self):
        return self._GpuTotal

    @GpuTotal.setter
    def GpuTotal(self, GpuTotal):
        self._GpuTotal = GpuTotal

    @property
    def GpuAvailable(self):
        return self._GpuAvailable

    @GpuAvailable.setter
    def GpuAvailable(self, GpuAvailable):
        self._GpuAvailable = GpuAvailable

    @property
    def ExclusiveOwner(self):
        return self._ExclusiveOwner

    @ExclusiveOwner.setter
    def ExclusiveOwner(self, ExclusiveOwner):
        self._ExclusiveOwner = ExclusiveOwner


    def _deserialize(self, params):
        self._CpuTotal = params.get("CpuTotal")
        self._CpuAvailable = params.get("CpuAvailable")
        self._MemTotal = params.get("MemTotal")
        self._MemAvailable = params.get("MemAvailable")
        self._DiskTotal = params.get("DiskTotal")
        self._DiskAvailable = params.get("DiskAvailable")
        self._DiskType = params.get("DiskType")
        self._GpuTotal = params.get("GpuTotal")
        self._GpuAvailable = params.get("GpuAvailable")
        self._ExclusiveOwner = params.get("ExclusiveOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HpcClusterInfo(AbstractModel):
    """高性能计算集群

    """

    def __init__(self):
        r"""
        :param _HpcClusterId: 高性能计算集群ID
        :type HpcClusterId: str
        :param _Name: 高性能计算集群名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Remark: 高性能计算集群备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CvmQuotaTotal: 集群下设备容量
        :type CvmQuotaTotal: int
        :param _Zone: 集群所在可用区
        :type Zone: str
        :param _CurrentNum: 集群当前已有设备量
        :type CurrentNum: int
        :param _CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _InstanceIds: 集群内实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param _HpcClusterType: 高性能计算集群类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type HpcClusterType: str
        :param _HpcClusterBusinessId: 高性能计算集群对应的业务场景标识，当前只支持CDC。	
注意：此字段可能返回 null，表示取不到有效值。
        :type HpcClusterBusinessId: str
        """
        self._HpcClusterId = None
        self._Name = None
        self._Remark = None
        self._CvmQuotaTotal = None
        self._Zone = None
        self._CurrentNum = None
        self._CreateTime = None
        self._InstanceIds = None
        self._HpcClusterType = None
        self._HpcClusterBusinessId = None

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CvmQuotaTotal(self):
        return self._CvmQuotaTotal

    @CvmQuotaTotal.setter
    def CvmQuotaTotal(self, CvmQuotaTotal):
        self._CvmQuotaTotal = CvmQuotaTotal

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CurrentNum(self):
        return self._CurrentNum

    @CurrentNum.setter
    def CurrentNum(self, CurrentNum):
        self._CurrentNum = CurrentNum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def HpcClusterType(self):
        return self._HpcClusterType

    @HpcClusterType.setter
    def HpcClusterType(self, HpcClusterType):
        self._HpcClusterType = HpcClusterType

    @property
    def HpcClusterBusinessId(self):
        return self._HpcClusterBusinessId

    @HpcClusterBusinessId.setter
    def HpcClusterBusinessId(self, HpcClusterBusinessId):
        self._HpcClusterBusinessId = HpcClusterBusinessId


    def _deserialize(self, params):
        self._HpcClusterId = params.get("HpcClusterId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._CvmQuotaTotal = params.get("CvmQuotaTotal")
        self._Zone = params.get("Zone")
        self._CurrentNum = params.get("CurrentNum")
        self._CreateTime = params.get("CreateTime")
        self._InstanceIds = params.get("InstanceIds")
        self._HpcClusterType = params.get("HpcClusterType")
        self._HpcClusterBusinessId = params.get("HpcClusterBusinessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """一个关于镜像详细信息的结构体，主要包括镜像的主要状态与属性。

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _OsName: 镜像操作系统
        :type OsName: str
        :param _ImageType: 镜像类型
        :type ImageType: str
        :param _CreatedTime: 镜像创建时间
        :type CreatedTime: str
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _ImageDescription: 镜像描述
        :type ImageDescription: str
        :param _ImageSize: 镜像大小
        :type ImageSize: int
        :param _Architecture: 镜像架构
        :type Architecture: str
        :param _ImageState: 镜像状态:
CREATING-创建中
NORMAL-正常
CREATEFAILED-创建失败
USING-使用中
SYNCING-同步中
IMPORTING-导入中
IMPORTFAILED-导入失败
        :type ImageState: str
        :param _Platform: 镜像来源平台，包括如TencentOS、 CentOS、 Windows、 Ubuntu、 Debian、Fedora等。
        :type Platform: str
        :param _ImageCreator: 镜像创建者
        :type ImageCreator: str
        :param _ImageSource: 镜像来源
        :type ImageSource: str
        :param _SyncPercent: 同步百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncPercent: int
        :param _IsSupportCloudinit: 镜像是否支持cloud-init
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportCloudinit: bool
        :param _SnapshotSet: 镜像关联的快照信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotSet: list of Snapshot
        :param _Tags: 镜像关联的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _LicenseType: 镜像许可类型
        :type LicenseType: str
        """
        self._ImageId = None
        self._OsName = None
        self._ImageType = None
        self._CreatedTime = None
        self._ImageName = None
        self._ImageDescription = None
        self._ImageSize = None
        self._Architecture = None
        self._ImageState = None
        self._Platform = None
        self._ImageCreator = None
        self._ImageSource = None
        self._SyncPercent = None
        self._IsSupportCloudinit = None
        self._SnapshotSet = None
        self._Tags = None
        self._LicenseType = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ImageSize(self):
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def ImageState(self):
        return self._ImageState

    @ImageState.setter
    def ImageState(self, ImageState):
        self._ImageState = ImageState

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ImageCreator(self):
        return self._ImageCreator

    @ImageCreator.setter
    def ImageCreator(self, ImageCreator):
        self._ImageCreator = ImageCreator

    @property
    def ImageSource(self):
        return self._ImageSource

    @ImageSource.setter
    def ImageSource(self, ImageSource):
        self._ImageSource = ImageSource

    @property
    def SyncPercent(self):
        return self._SyncPercent

    @SyncPercent.setter
    def SyncPercent(self, SyncPercent):
        self._SyncPercent = SyncPercent

    @property
    def IsSupportCloudinit(self):
        return self._IsSupportCloudinit

    @IsSupportCloudinit.setter
    def IsSupportCloudinit(self, IsSupportCloudinit):
        self._IsSupportCloudinit = IsSupportCloudinit

    @property
    def SnapshotSet(self):
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._OsName = params.get("OsName")
        self._ImageType = params.get("ImageType")
        self._CreatedTime = params.get("CreatedTime")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        self._ImageSize = params.get("ImageSize")
        self._Architecture = params.get("Architecture")
        self._ImageState = params.get("ImageState")
        self._Platform = params.get("Platform")
        self._ImageCreator = params.get("ImageCreator")
        self._ImageSource = params.get("ImageSource")
        self._SyncPercent = params.get("SyncPercent")
        self._IsSupportCloudinit = params.get("IsSupportCloudinit")
        if params.get("SnapshotSet") is not None:
            self._SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self._SnapshotSet.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """支持的操作系统类型，根据Windows和Linux分类。

    """

    def __init__(self):
        r"""
        :param _Windows: 支持的Windows操作系统。
注意：此字段可能返回 null，表示取不到有效值。
        :type Windows: list of str
        :param _Linux: 支持的Linux操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Linux: list of str
        """
        self._Windows = None
        self._Linux = None

    @property
    def Windows(self):
        return self._Windows

    @Windows.setter
    def Windows(self, Windows):
        self._Windows = Windows

    @property
    def Linux(self):
        return self._Linux

    @Linux.setter
    def Linux(self, Linux):
        self._Linux = Linux


    def _deserialize(self, params):
        self._Windows = params.get("Windows")
        self._Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageQuota(AbstractModel):
    """镜像配额

    """

    def __init__(self):
        r"""
        :param _UsedQuota: 已使用配额
        :type UsedQuota: int
        :param _TotalQuota: 总配额
        :type TotalQuota: int
        """
        self._UsedQuota = None
        self._TotalQuota = None

    @property
    def UsedQuota(self):
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def TotalQuota(self):
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota


    def _deserialize(self, params):
        self._UsedQuota = params.get("UsedQuota")
        self._TotalQuota = params.get("TotalQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageRequest(AbstractModel):
    """ImportImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Architecture: 导入镜像的操作系统架构，`x86_64` 或 `i386`
        :type Architecture: str
        :param _OsType: 导入镜像的操作系统类型，通过`DescribeImportImageOs`获取
        :type OsType: str
        :param _OsVersion: 导入镜像的操作系统版本，通过`DescribeImportImageOs`获取
        :type OsVersion: str
        :param _ImageUrl: 导入镜像存放的cos地址
        :type ImageUrl: str
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _ImageDescription: 镜像描述
        :type ImageDescription: str
        :param _DryRun: 只检查参数，不执行任务
        :type DryRun: bool
        :param _Force: 是否强制导入，参考[强制导入镜像](https://cloud.tencent.com/document/product/213/12849)
        :type Force: bool
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到自定义镜像。
        :type TagSpecification: list of TagSpecification
        :param _LicenseType: 导入镜像后，激活操作系统采用的许可证类型。
可选项：
TencentCloud: 腾讯云官方许可
BYOL: 自带许可（Bring Your Own License）
        :type LicenseType: str
        :param _BootMode: 启动模式
        :type BootMode: str
        """
        self._Architecture = None
        self._OsType = None
        self._OsVersion = None
        self._ImageUrl = None
        self._ImageName = None
        self._ImageDescription = None
        self._DryRun = None
        self._Force = None
        self._TagSpecification = None
        self._LicenseType = None
        self._BootMode = None

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OsVersion(self):
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def BootMode(self):
        return self._BootMode

    @BootMode.setter
    def BootMode(self, BootMode):
        self._BootMode = BootMode


    def _deserialize(self, params):
        self._Architecture = params.get("Architecture")
        self._OsType = params.get("OsType")
        self._OsVersion = params.get("OsVersion")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        self._DryRun = params.get("DryRun")
        self._Force = params.get("Force")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._LicenseType = params.get("LicenseType")
        self._BootMode = params.get("BootMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ImportInstancesActionTimerRequest(AbstractModel):
    """ImportInstancesActionTimer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例id列表，可以通过DescribeInstances接口查询到。
        :type InstanceIds: list of str
        :param _ActionTimer: 定时器任务信息，目前仅支持定时销毁。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        """
        self._InstanceIds = None
        self._ActionTimer = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportInstancesActionTimerResponse(AbstractModel):
    """ImportInstancesActionTimer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionTimerIds: 定时器id列表
        :type ActionTimerIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActionTimerIds = None
        self._RequestId = None

    @property
    def ActionTimerIds(self):
        return self._ActionTimerIds

    @ActionTimerIds.setter
    def ActionTimerIds(self, ActionTimerIds):
        self._ActionTimerIds = ActionTimerIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActionTimerIds = params.get("ActionTimerIds")
        self._RequestId = params.get("RequestId")


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :type KeyName: str
        :param _ProjectId: 密钥对创建后所属的[项目](https://cloud.tencent.com/document/product/378/10861)ID。<br><br>可以通过以下方式获取项目ID：<br><li>通过[项目列表](https://console.cloud.tencent.com/project)查询项目ID。<br><li>通过调用接口 [DescribeProject](https://cloud.tencent.com/document/api/378/4400)，取返回信息中的 `projectId ` 获取项目ID。

如果是默认项目，直接填0就可以。
        :type ProjectId: int
        :param _PublicKey: 密钥对的公钥内容，`OpenSSH RSA` 格式。
        :type PublicKey: str
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到密钥对。
        :type TagSpecification: list of TagSpecification
        """
        self._KeyName = None
        self._ProjectId = None
        self._PublicKey = None
        self._TagSpecification = None

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        self._PublicKey = params.get("PublicKey")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairResponse(AbstractModel):
    """ImportKeyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥对ID。
        :type KeyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class InquirePricePurchaseReservedInstancesOfferingRequest(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceCount: 购买预留实例计费数量
        :type InstanceCount: int
        :param _ReservedInstancesOfferingId: 预留实例计费配置ID
        :type ReservedInstancesOfferingId: str
        :param _DryRun: 试运行
        :type DryRun: bool
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性
        :type ClientToken: str
        :param _ReservedInstanceName: 预留实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>最多支持60个字符（包含模式串）。</li>
        :type ReservedInstanceName: str
        """
        self._InstanceCount = None
        self._ReservedInstancesOfferingId = None
        self._DryRun = None
        self._ClientToken = None
        self._ReservedInstanceName = None

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ReservedInstanceName(self):
        return self._ReservedInstanceName

    @ReservedInstanceName.setter
    def ReservedInstanceName(self, ReservedInstanceName):
        self._ReservedInstanceName = ReservedInstanceName


    def _deserialize(self, params):
        self._InstanceCount = params.get("InstanceCount")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._DryRun = params.get("DryRun")
        self._ClientToken = params.get("ClientToken")
        self._ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePricePurchaseReservedInstancesOfferingResponse(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示对应配置预留实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ReservedInstancePrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = ReservedInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceModifyInstancesChargeTypeRequest(AbstractModel):
    """InquiryPriceModifyInstancesChargeType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param _InstanceChargeType: 修改后的实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月。</li><li>POSTPAID_BY_HOUR：后付费，即按量付费。</li>
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。<dx-alert infotype="explain" title="">若指定修改后实例的付费模式为预付费则该参数必传。</dx-alert>
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _ModifyPortableDataDisk: 是否同时切换弹性数据云盘计费模式。取值范围：<br><li>true：表示切换弹性数据云盘计费模式</li><li>false：表示不切换弹性数据云盘计费模式</li><br>默认取值：false。
        :type ModifyPortableDataDisk: bool
        """
        self._InstanceIds = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._ModifyPortableDataDisk = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def ModifyPortableDataDisk(self):
        return self._ModifyPortableDataDisk

    @ModifyPortableDataDisk.setter
    def ModifyPortableDataDisk(self, ModifyPortableDataDisk):
        self._ModifyPortableDataDisk = ModifyPortableDataDisk


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._ModifyPortableDataDisk = params.get("ModifyPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceModifyInstancesChargeTypeResponse(AbstractModel):
    """InquiryPriceModifyInstancesChargeType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示对应配置实例转换计费模式的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewHostsRequest(AbstractModel):
    """InquiryPriceRenewHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HostIds: 一个或多个待操作的`CDH`实例`ID`。可通过[`DescribeHosts`](https://cloud.tencent.com/document/api/213/16474)接口返回值中的`HostId`获取。每次请求批量实例的上限为100。
        :type HostIds: list of str
        :param _HostChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。
        :type HostChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.ChargePrepaid`
        :param _DryRun: 试运行，测试使用，不执行具体逻辑。取值范围：<br><li>TRUE：跳过执行逻辑<br><li>FALSE：执行逻辑<br><br>默认取值：FALSE。
        :type DryRun: bool
        """
        self._HostIds = None
        self._HostChargePrepaid = None
        self._DryRun = None

    @property
    def HostIds(self):
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostChargePrepaid(self):
        return self._HostChargePrepaid

    @HostChargePrepaid.setter
    def HostChargePrepaid(self, HostChargePrepaid):
        self._HostChargePrepaid = HostChargePrepaid

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._HostIds = params.get("HostIds")
        if params.get("HostChargePrepaid") is not None:
            self._HostChargePrepaid = ChargePrepaid()
            self._HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewHostsResponse(AbstractModel):
    """InquiryPriceRenewHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: CDH实例续费价格信息
        :type Price: :class:`tencentcloud.cvm.v20170312.models.HostPriceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = HostPriceInfo()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewInstancesRequest(AbstractModel):
    """InquiryPriceRenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _DryRun: 试运行，测试使用，不执行具体逻辑。取值范围：<br><li>true：跳过执行逻辑</li><li>false：执行逻辑<br><br>默认取值：false。</li>
        :type DryRun: bool
        :param _RenewPortableDataDisk: 是否续费弹性数据盘。取值范围：<br><li>true：表示续费包年包月实例同时续费其挂载的弹性数据盘</li><li>false：表示续费包年包月实例同时不再续费其挂载的弹性数据盘</li><br>默认取值：true。
        :type RenewPortableDataDisk: bool
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None
        self._DryRun = None
        self._RenewPortableDataDisk = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def RenewPortableDataDisk(self):
        return self._RenewPortableDataDisk

    @RenewPortableDataDisk.setter
    def RenewPortableDataDisk(self, RenewPortableDataDisk):
        self._RenewPortableDataDisk = RenewPortableDataDisk


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DryRun = params.get("DryRun")
        self._RenewPortableDataDisk = params.get("RenewPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstancesResponse(AbstractModel):
    """InquiryPriceRenewInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示对应配置实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResetInstanceRequest(AbstractModel):
    """InquiryPriceResetInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param _ImageId: 指定有效的[镜像](/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param _SystemDisk: 实例系统盘配置信息。系统盘为云盘的实例可以通过该参数指定重装后的系统盘大小来实现对系统盘的扩容操作，若不指定则默认系统盘大小保持不变。系统盘大小只支持扩容不支持缩容；重装只支持修改系统盘的大小，不能修改系统盘的类型。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        """
        self._InstanceId = None
        self._ImageId = None
        self._SystemDisk = None
        self._LoginSettings = None
        self._EnhancedService = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstanceResponse(AbstractModel):
    """InquiryPriceResetInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示重装成对应配置实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。当调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽时，只支持一个实例。
        :type InstanceIds: list of str
        :param _InternetAccessible: 公网出带宽配置。不同机型带宽上限范围不一致，具体限制详见带宽限制对账表。暂时只支持`InternetMaxBandwidthOut`参数。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _StartTime: 带宽生效的起始时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始时间不能早于当前时间。如果起始时间是今天则新设置的带宽立即生效。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type StartTime: str
        :param _EndTime: 带宽生效的终止时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。新设置的带宽的有效期包含终止时间此日期。终止时间不能晚于包年包月实例的到期时间。实例的到期时间可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`ExpiredTime`获取。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type EndTime: str
        """
        self._InstanceIds = None
        self._InternetAccessible = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示带宽调整为对应大小之后的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResetInstancesTypeRequest(AbstractModel):
    """InquiryPriceResetInstancesType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。本接口每次请求批量实例的上限为1。
        :type InstanceIds: list of str
        :param _InstanceType: 实例机型。不同实例机型指定了不同的资源规格，具体取值可参见附表[实例资源规格](https://cloud.tencent.com/document/product/213/11518)对照表，也可以调用查询[实例资源规格列表](https://cloud.tencent.com/document/product/213/15749)接口获得最新的规格表。
        :type InstanceType: str
        """
        self._InstanceIds = None
        self._InstanceType = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesTypeResponse(AbstractModel):
    """InquiryPriceResetInstancesType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示调整成对应机型实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceResizeInstanceDisksRequest(AbstractModel):
    """InquiryPriceResizeInstanceDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param _DataDisks: 待扩容的数据盘配置信息。只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性）。数据盘容量单位：GB。最小扩容步长：10G。关于数据盘类型的选择请参考硬盘产品简介。可选数据盘类型受到实例类型`InstanceType`限制。另外允许扩容的最大容量也因数据盘类型的不同而有所差异。
<dx-alert infotype="explain" title="">您必须指定参数DataDisks与SystemDisk的其中一个，但不能同时指定。</dx-alert>
        :type DataDisks: list of DataDisk
        :param _ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>true：表示在正常关机失败后进行强制关机</li><br><li>false：表示在正常关机失败后不进行强制关机</li><br><br>默认取值：false。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        """
        self._InstanceId = None
        self._DataDisks = None
        self._ForceStop = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeInstanceDisksResponse(AbstractModel):
    """InquiryPriceResizeInstanceDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示磁盘扩容成对应配置的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceRunInstancesRequest(AbstractModel):
    """InquiryPriceRunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
 <b>注：如果您不指定LaunchTemplate参数，则Placement为必选参数。若同时传递Placement和LaunchTemplate，则默认覆盖LaunchTemplate中对应的Placement的值。</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
 <b>注：如果您不指定LaunchTemplate参数，则ImageId为必选参数。若同时传递ImageId和LaunchTemplate，则默认覆盖LaunchTemplate中对应的ImageId的值。</b>
        :type ImageId: str
        :param _InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>SPOTPAID：竞价付费</li><br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _InstanceType: 实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则默认机型为S1.SMALL1。
        :type InstanceType: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若不指定该参数，则默认使用基础网络。若在此参数中指定了私有网络IP，那么InstanceCount参数只能为1。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _InstanceCount: 购买实例数量。取值范围：[1，100]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。</li>
        :type InstanceName: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则默认不绑定安全组。
        :type SecurityGroupIds: list of str
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _HostName: 云服务器的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><br><li>Windows 实例：主机名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><br><li>其他类型（Linux 等）实例：主机名字符长度为[2, 30]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li>
        :type HostName: str
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云服务器实例。
        :type TagSpecification: list of TagSpecification
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _HpcClusterId: 高性能计算集群ID。
        :type HpcClusterId: str
        :param _LaunchTemplate: 实例启动模板。
        :type LaunchTemplate: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplate`
        """
        self._Placement = None
        self._ImageId = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceCount = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._ClientToken = None
        self._HostName = None
        self._TagSpecification = None
        self._InstanceMarketOptions = None
        self._HpcClusterId = None
        self._LaunchTemplate = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def LaunchTemplate(self):
        return self._LaunchTemplate

    @LaunchTemplate.setter
    def LaunchTemplate(self, LaunchTemplate):
        self._LaunchTemplate = LaunchTemplate


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ImageId = params.get("ImageId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ClientToken = params.get("ClientToken")
        self._HostName = params.get("HostName")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("LaunchTemplate") is not None:
            self._LaunchTemplate = LaunchTemplate()
            self._LaunchTemplate._deserialize(params.get("LaunchTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRunInstancesResponse(AbstractModel):
    """InquiryPriceRunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示对应配置实例的价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquiryPriceTerminateInstancesRequest(AbstractModel):
    """InquiryPriceTerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceTerminateInstancesResponse(AbstractModel):
    """InquiryPriceTerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceRefundsSet: 退款详情。
        :type InstanceRefundsSet: list of InstanceRefund
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceRefundsSet = None
        self._RequestId = None

    @property
    def InstanceRefundsSet(self):
        return self._InstanceRefundsSet

    @InstanceRefundsSet.setter
    def InstanceRefundsSet(self, InstanceRefundsSet):
        self._InstanceRefundsSet = InstanceRefundsSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceRefundsSet") is not None:
            self._InstanceRefundsSet = []
            for item in params.get("InstanceRefundsSet"):
                obj = InstanceRefund()
                obj._deserialize(item)
                self._InstanceRefundsSet.append(obj)
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """描述实例的信息

    """

    def __init__(self):
        r"""
        :param _Placement: 实例所在的位置。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _InstanceId: 实例`ID`。
        :type InstanceId: str
        :param _InstanceType: 实例机型。
        :type InstanceType: str
        :param _CPU: 实例的CPU核数，单位：核。
        :type CPU: int
        :param _Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param _RestrictState: 实例业务状态。取值范围：<br><li>NORMAL：表示正常状态的实例<br><li>EXPIRED：表示过期的实例<br><li>PROTECTIVELY_ISOLATED：表示被安全隔离的实例。
        :type RestrictState: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceChargeType: 实例计费模式。取值范围：<br><li>`PREPAID`：表示预付费，即包年包月<br><li>`POSTPAID_BY_HOUR`：表示后付费，即按量计费<br><li>`CDHPAID`：`专用宿主机`付费，即只对`专用宿主机`计费，不对`专用宿主机`上的实例计费。<br><li>`SPOTPAID`：表示竞价实例付费。
        :type InstanceChargeType: str
        :param _SystemDisk: 实例系统盘信息。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: 实例数据盘信息。
        :type DataDisks: list of DataDisk
        :param _PrivateIpAddresses: 实例主网卡的内网`IP`列表。
        :type PrivateIpAddresses: list of str
        :param _PublicIpAddresses: 实例主网卡的公网`IP`列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param _InternetAccessible: 实例带宽信息。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _VirtualPrivateCloud: 实例所属虚拟私有网络信息。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _ImageId: 生产实例所使用的镜像`ID`。
        :type ImageId: str
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>`NOTIFY_AND_MANUAL_RENEW`：表示通知即将过期，但不自动续费<br><li>`NOTIFY_AND_AUTO_RENEW`：表示通知即将过期，而且自动续费<br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`：表示不通知即将过期，也不自动续费。
<br><li>注意：后付费模式本项为null
        :type RenewFlag: str
        :param _CreatedTime: 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param _ExpiredTime: 到期时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。注意：后付费模式本项为null
        :type ExpiredTime: str
        :param _OsName: 操作系统名称。
        :type OsName: str
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。
        :type SecurityGroupIds: list of str
        :param _LoginSettings: 实例登录设置。目前只返回实例所关联的密钥。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _InstanceState: 实例状态。取值范围：<br><li>PENDING：表示创建中<br></li><li>LAUNCH_FAILED：表示创建失败<br></li><li>RUNNING：表示运行中<br></li><li>STOPPED：表示关机<br></li><li>STARTING：表示开机中<br></li><li>STOPPING：表示关机中<br></li><li>REBOOTING：表示重启中<br></li><li>SHUTDOWN：表示停止待销毁<br></li><li>TERMINATING：表示销毁中。<br></li>
        :type InstanceState: str
        :param _Tags: 实例关联的标签列表。
        :type Tags: list of Tag
        :param _StopChargingMode: 实例的关机计费模式。
取值范围：<br><li>KEEP_CHARGING：关机继续收费<br><li>STOP_CHARGING：关机停止收费<li>NOT_APPLICABLE：实例处于非关机状态或者不适用关机停止计费的条件<br>
        :type StopChargingMode: str
        :param _Uuid: 实例全局唯一ID
        :type Uuid: str
        :param _LatestOperation: 实例的最新操作。例：StopInstances、ResetInstance。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param _LatestOperationState: 实例的最新操作状态。取值范围：<br><li>SUCCESS：表示操作成功<br><li>OPERATING：表示操作执行中<br><li>FAILED：表示操作失败
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param _LatestOperationRequestId: 实例最新操作的唯一请求 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationRequestId: str
        :param _DisasterRecoverGroupId: 分散置放群组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisasterRecoverGroupId: str
        :param _IPv6Addresses: 实例的IPv6地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Addresses: list of str
        :param _CamRoleName: CAM角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type CamRoleName: str
        :param _HpcClusterId: 高性能计算集群`ID`。
注意：此字段可能返回 null，表示取不到有效值。
        :type HpcClusterId: str
        :param _RdmaIpAddresses: 高性能计算集群`IP`列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RdmaIpAddresses: list of str
        :param _DedicatedClusterId: 实例所在的专用集群`ID`。
注意：此字段可能返回 null，表示取不到有效值。
        :type DedicatedClusterId: str
        :param _IsolatedSource: 实例隔离类型。取值范围：<br><li>ARREAR：表示欠费隔离<br></li><li>EXPIRE：表示到期隔离<br></li><li>MANMADE：表示主动退还隔离<br></li><li>NOTISOLATED：表示未隔离<br></li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedSource: str
        :param _GPUInfo: GPU信息。如果是gpu类型子机，该值会返回GPU信息，如果是其他类型子机则不返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUInfo: :class:`tencentcloud.cvm.v20170312.models.GPUInfo`
        :param _LicenseType: 实例的操作系统许可类型，默认为TencentCloud
        :type LicenseType: str
        :param _DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>TRUE：表示开启实例保护，不允许通过api接口删除实例<br><li>FALSE：表示关闭实例保护，允许通过api接口删除实例<br><br>默认取值：FALSE。
        :type DisableApiTermination: bool
        :param _DefaultLoginUser: 默认登录用户。
        :type DefaultLoginUser: str
        :param _DefaultLoginPort: 默认登录端口。
        :type DefaultLoginPort: int
        :param _LatestOperationErrorMsg: 实例的最新操作错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationErrorMsg: str
        """
        self._Placement = None
        self._InstanceId = None
        self._InstanceType = None
        self._CPU = None
        self._Memory = None
        self._RestrictState = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._PrivateIpAddresses = None
        self._PublicIpAddresses = None
        self._InternetAccessible = None
        self._VirtualPrivateCloud = None
        self._ImageId = None
        self._RenewFlag = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._OsName = None
        self._SecurityGroupIds = None
        self._LoginSettings = None
        self._InstanceState = None
        self._Tags = None
        self._StopChargingMode = None
        self._Uuid = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._LatestOperationRequestId = None
        self._DisasterRecoverGroupId = None
        self._IPv6Addresses = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._RdmaIpAddresses = None
        self._DedicatedClusterId = None
        self._IsolatedSource = None
        self._GPUInfo = None
        self._LicenseType = None
        self._DisableApiTermination = None
        self._DefaultLoginUser = None
        self._DefaultLoginPort = None
        self._LatestOperationErrorMsg = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def RestrictState(self):
        return self._RestrictState

    @RestrictState.setter
    def RestrictState(self, RestrictState):
        self._RestrictState = RestrictState

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def StopChargingMode(self):
        return self._StopChargingMode

    @StopChargingMode.setter
    def StopChargingMode(self, StopChargingMode):
        self._StopChargingMode = StopChargingMode

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def LatestOperation(self):
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def LatestOperationRequestId(self):
        return self._LatestOperationRequestId

    @LatestOperationRequestId.setter
    def LatestOperationRequestId(self, LatestOperationRequestId):
        self._LatestOperationRequestId = LatestOperationRequestId

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def IPv6Addresses(self):
        return self._IPv6Addresses

    @IPv6Addresses.setter
    def IPv6Addresses(self, IPv6Addresses):
        self._IPv6Addresses = IPv6Addresses

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def RdmaIpAddresses(self):
        return self._RdmaIpAddresses

    @RdmaIpAddresses.setter
    def RdmaIpAddresses(self, RdmaIpAddresses):
        self._RdmaIpAddresses = RdmaIpAddresses

    @property
    def DedicatedClusterId(self):
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def IsolatedSource(self):
        return self._IsolatedSource

    @IsolatedSource.setter
    def IsolatedSource(self, IsolatedSource):
        self._IsolatedSource = IsolatedSource

    @property
    def GPUInfo(self):
        return self._GPUInfo

    @GPUInfo.setter
    def GPUInfo(self, GPUInfo):
        self._GPUInfo = GPUInfo

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination

    @property
    def DefaultLoginUser(self):
        return self._DefaultLoginUser

    @DefaultLoginUser.setter
    def DefaultLoginUser(self, DefaultLoginUser):
        self._DefaultLoginUser = DefaultLoginUser

    @property
    def DefaultLoginPort(self):
        return self._DefaultLoginPort

    @DefaultLoginPort.setter
    def DefaultLoginPort(self, DefaultLoginPort):
        self._DefaultLoginPort = DefaultLoginPort

    @property
    def LatestOperationErrorMsg(self):
        return self._LatestOperationErrorMsg

    @LatestOperationErrorMsg.setter
    def LatestOperationErrorMsg(self, LatestOperationErrorMsg):
        self._LatestOperationErrorMsg = LatestOperationErrorMsg


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceId = params.get("InstanceId")
        self._InstanceType = params.get("InstanceType")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._RestrictState = params.get("RestrictState")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ImageId = params.get("ImageId")
        self._RenewFlag = params.get("RenewFlag")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._OsName = params.get("OsName")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._InstanceState = params.get("InstanceState")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._StopChargingMode = params.get("StopChargingMode")
        self._Uuid = params.get("Uuid")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._LatestOperationRequestId = params.get("LatestOperationRequestId")
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._IPv6Addresses = params.get("IPv6Addresses")
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        self._RdmaIpAddresses = params.get("RdmaIpAddresses")
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._IsolatedSource = params.get("IsolatedSource")
        if params.get("GPUInfo") is not None:
            self._GPUInfo = GPUInfo()
            self._GPUInfo._deserialize(params.get("GPUInfo"))
        self._LicenseType = params.get("LicenseType")
        self._DisableApiTermination = params.get("DisableApiTermination")
        self._DefaultLoginUser = params.get("DefaultLoginUser")
        self._DefaultLoginPort = params.get("DefaultLoginPort")
        self._LatestOperationErrorMsg = params.get("LatestOperationErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li><br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li><br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li><br><br>默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyConfig(AbstractModel):
    """描述实例的机型族配置信息
    形如：{'InstanceFamilyName': '标准型S1', 'InstanceFamily': 'S1'}、{'InstanceFamilyName': '网络优化型N1', 'InstanceFamily': 'N1'}、{'InstanceFamilyName': '高IO型I1', 'InstanceFamily': 'I1'}等。

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyName: 机型族名称的中文全称。
        :type InstanceFamilyName: str
        :param _InstanceFamily: 机型族名称的英文简称。
        :type InstanceFamily: str
        """
        self._InstanceFamilyName = None
        self._InstanceFamily = None

    @property
    def InstanceFamilyName(self):
        return self._InstanceFamilyName

    @InstanceFamilyName.setter
    def InstanceFamilyName(self, InstanceFamilyName):
        self._InstanceFamilyName = InstanceFamilyName

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily


    def _deserialize(self, params):
        self._InstanceFamilyName = params.get("InstanceFamilyName")
        self._InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMarketOptionsRequest(AbstractModel):
    """竞价请求相关选项

    """

    def __init__(self):
        r"""
        :param _SpotOptions: 竞价相关选项
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotOptions: :class:`tencentcloud.cvm.v20170312.models.SpotMarketOptions`
        :param _MarketType: 市场选项类型，当前只支持取值：spot
注意：此字段可能返回 null，表示取不到有效值。
        :type MarketType: str
        """
        self._SpotOptions = None
        self._MarketType = None

    @property
    def SpotOptions(self):
        return self._SpotOptions

    @SpotOptions.setter
    def SpotOptions(self, SpotOptions):
        self._SpotOptions = SpotOptions

    @property
    def MarketType(self):
        return self._MarketType

    @MarketType.setter
    def MarketType(self, MarketType):
        self._MarketType = MarketType


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self._SpotOptions = SpotMarketOptions()
            self._SpotOptions._deserialize(params.get("SpotOptions"))
        self._MarketType = params.get("MarketType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRefund(AbstractModel):
    """描述退款详情。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Refunds: 退款数额。
注意：此字段可能返回 null，表示取不到有效值。
        :type Refunds: float
        :param _PriceDetail: 退款详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceDetail: str
        """
        self._InstanceId = None
        self._Refunds = None
        self._PriceDetail = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Refunds(self):
        return self._Refunds

    @Refunds.setter
    def Refunds(self, Refunds):
        self._Refunds = Refunds

    @property
    def PriceDetail(self):
        return self._PriceDetail

    @PriceDetail.setter
    def PriceDetail(self, PriceDetail):
        self._PriceDetail = PriceDetail


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Refunds = params.get("Refunds")
        self._PriceDetail = params.get("PriceDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatus(AbstractModel):
    """描述实例的状态。状态类型详见[实例状态表](/document/api/213/15753#InstanceStatus)

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例`ID`。
        :type InstanceId: str
        :param _InstanceState: 实例状态。取值范围：<br><li>PENDING：表示创建中<br></li><li>LAUNCH_FAILED：表示创建失败<br></li><li>RUNNING：表示运行中<br></li><li>STOPPED：表示关机<br></li><li>STARTING：表示开机中<br></li><li>STOPPING：表示关机中<br></li><li>REBOOTING：表示重启中<br></li><li>SHUTDOWN：表示停止待销毁<br></li><li>TERMINATING：表示销毁中<br></li><li>ENTER_RESCUE_MODE：表示进入救援模式<br></li><li>RESCUE_MODE：表示在救援模式中<br></li><li>EXIT_RESCUE_MODE：表示退出救援模式<br></li><li>ENTER_SERVICE_LIVE_MIGRATE：表示进入在线服务迁移<br></li><li>SERVICE_LIVE_MIGRATE：表示在线服务迁移中<br></li><li>EXIT_SERVICE_LIVE_MIGRATE：表示退出在线服务迁移。<br></li>
        :type InstanceState: str
        """
        self._InstanceId = None
        self._InstanceState = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceState = params.get("InstanceState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfig(AbstractModel):
    """描述实例机型配置信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区。
        :type Zone: str
        :param _InstanceType: 实例机型。
        :type InstanceType: str
        :param _InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param _GPU: GPU核数，单位：核。
        :type GPU: int
        :param _CPU: CPU核数，单位：核。
        :type CPU: int
        :param _Memory: 内存容量，单位：`GB`。
        :type Memory: int
        :param _FPGA: FPGA核数，单位：核。
        :type FPGA: int
        :param _GpuCount: 实例机型映射的物理GPU卡数，单位：卡。vGPU卡型小于1，直通卡型大于等于1。vGPU是通过分片虚拟化技术，将物理GPU卡重新划分，同一块GPU卡经虚拟化分割后可分配至不同的实例使用。直通卡型会将GPU设备直接挂载给实例使用。
        :type GpuCount: float
        """
        self._Zone = None
        self._InstanceType = None
        self._InstanceFamily = None
        self._GPU = None
        self._CPU = None
        self._Memory = None
        self._FPGA = None
        self._GpuCount = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def GPU(self):
        return self._GPU

    @GPU.setter
    def GPU(self, GPU):
        self._GPU = GPU

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def FPGA(self):
        return self._FPGA

    @FPGA.setter
    def FPGA(self, FPGA):
        self._FPGA = FPGA

    @property
    def GpuCount(self):
        return self._GpuCount

    @GpuCount.setter
    def GpuCount(self, GpuCount):
        self._GpuCount = GpuCount


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceFamily = params.get("InstanceFamily")
        self._GPU = params.get("GPU")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._FPGA = params.get("FPGA")
        self._GpuCount = params.get("GpuCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfigStatus(AbstractModel):
    """描述实例机型配置信息及状态信息

    """

    def __init__(self):
        r"""
        :param _Status: 状态描述
        :type Status: str
        :param _Message: 状态描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _InstanceTypeConfig: 配置信息
        :type InstanceTypeConfig: :class:`tencentcloud.cvm.v20170312.models.InstanceTypeConfig`
        """
        self._Status = None
        self._Message = None
        self._InstanceTypeConfig = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceTypeConfig(self):
        return self._InstanceTypeConfig

    @InstanceTypeConfig.setter
    def InstanceTypeConfig(self, InstanceTypeConfig):
        self._InstanceTypeConfig = InstanceTypeConfig


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        if params.get("InstanceTypeConfig") is not None:
            self._InstanceTypeConfig = InstanceTypeConfig()
            self._InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeQuotaItem(AbstractModel):
    """描述实例机型配额信息。

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区。
        :type Zone: str
        :param _InstanceType: 实例机型。
        :type InstanceType: str
        :param _InstanceChargeType: 实例计费模式。取值范围： <br><li>PREPAID：表示预付费，即包年包月<br></li>POSTPAID_BY_HOUR：表示后付费，即按量计费<br><li>CDHPAID：表示[专用宿主机](https://cloud.tencent.com/document/product/416)付费，即只对`专用宿主机`计费，不对`专用宿主机`上的实例计费。<br></li>`SPOTPAID`：表示竞价实例付费。
        :type InstanceChargeType: str
        :param _NetworkCard: 网卡类型，例如：25代表25G网卡
        :type NetworkCard: int
        :param _Externals: 扩展属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param _Cpu: 实例的CPU核数，单位：核。
        :type Cpu: int
        :param _Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param _InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param _TypeName: 机型名称。
        :type TypeName: str
        :param _LocalDiskTypeList: 本地磁盘规格列表。当该参数返回为空值时，表示当前情况下无法创建本地盘。
        :type LocalDiskTypeList: list of LocalDiskType
        :param _Status: 实例是否售卖。取值范围： <br><li>SELL：表示实例可购买<br></li>SOLD_OUT：表示实例已售罄。
        :type Status: str
        :param _Price: 实例的售卖价格。
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param _SoldOutReason: 售罄原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type SoldOutReason: str
        :param _InstanceBandwidth: 内网带宽，单位Gbps。
        :type InstanceBandwidth: float
        :param _InstancePps: 网络收发包能力，单位万PPS。
        :type InstancePps: int
        :param _StorageBlockAmount: 本地存储块数量。
        :type StorageBlockAmount: int
        :param _CpuType: 处理器型号。
        :type CpuType: str
        :param _Gpu: 实例的GPU数量。
        :type Gpu: int
        :param _Fpga: 实例的FPGA数量。
        :type Fpga: int
        :param _Remark: 实例备注信息。
        :type Remark: str
        :param _GpuCount: 实例机型映射的物理GPU卡数，单位：卡。vGPU卡型小于1，直通卡型大于等于1。vGPU是通过分片虚拟化技术，将物理GPU卡重新划分，同一块GPU卡经虚拟化分割后可分配至不同的实例使用。直通卡型会将GPU设备直接挂载给实例使用。
        :type GpuCount: float
        :param _Frequency: 实例的CPU主频信息
        :type Frequency: str
        :param _StatusCategory: 描述库存情况。取值范围：
<li> EnoughStock：表示对应库存非常充足</li> 
<li>NormalStock：表示对应库存供应有保障</li>
<li> UnderStock：表示对应库存即将售罄</li> 
<li>WithoutStock：表示对应库存已经售罄</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCategory: str
        """
        self._Zone = None
        self._InstanceType = None
        self._InstanceChargeType = None
        self._NetworkCard = None
        self._Externals = None
        self._Cpu = None
        self._Memory = None
        self._InstanceFamily = None
        self._TypeName = None
        self._LocalDiskTypeList = None
        self._Status = None
        self._Price = None
        self._SoldOutReason = None
        self._InstanceBandwidth = None
        self._InstancePps = None
        self._StorageBlockAmount = None
        self._CpuType = None
        self._Gpu = None
        self._Fpga = None
        self._Remark = None
        self._GpuCount = None
        self._Frequency = None
        self._StatusCategory = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def NetworkCard(self):
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def Externals(self):
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def LocalDiskTypeList(self):
        return self._LocalDiskTypeList

    @LocalDiskTypeList.setter
    def LocalDiskTypeList(self, LocalDiskTypeList):
        self._LocalDiskTypeList = LocalDiskTypeList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def SoldOutReason(self):
        return self._SoldOutReason

    @SoldOutReason.setter
    def SoldOutReason(self, SoldOutReason):
        self._SoldOutReason = SoldOutReason

    @property
    def InstanceBandwidth(self):
        return self._InstanceBandwidth

    @InstanceBandwidth.setter
    def InstanceBandwidth(self, InstanceBandwidth):
        self._InstanceBandwidth = InstanceBandwidth

    @property
    def InstancePps(self):
        return self._InstancePps

    @InstancePps.setter
    def InstancePps(self, InstancePps):
        self._InstancePps = InstancePps

    @property
    def StorageBlockAmount(self):
        return self._StorageBlockAmount

    @StorageBlockAmount.setter
    def StorageBlockAmount(self, StorageBlockAmount):
        self._StorageBlockAmount = StorageBlockAmount

    @property
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def GpuCount(self):
        return self._GpuCount

    @GpuCount.setter
    def GpuCount(self, GpuCount):
        self._GpuCount = GpuCount

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def StatusCategory(self):
        return self._StatusCategory

    @StatusCategory.setter
    def StatusCategory(self, StatusCategory):
        self._StatusCategory = StatusCategory


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self._Externals = Externals()
            self._Externals._deserialize(params.get("Externals"))
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._InstanceFamily = params.get("InstanceFamily")
        self._TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self._LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self._LocalDiskTypeList.append(obj)
        self._Status = params.get("Status")
        if params.get("Price") is not None:
            self._Price = ItemPrice()
            self._Price._deserialize(params.get("Price"))
        self._SoldOutReason = params.get("SoldOutReason")
        self._InstanceBandwidth = params.get("InstanceBandwidth")
        self._InstancePps = params.get("InstancePps")
        self._StorageBlockAmount = params.get("StorageBlockAmount")
        self._CpuType = params.get("CpuType")
        self._Gpu = params.get("Gpu")
        self._Fpga = params.get("Fpga")
        self._Remark = params.get("Remark")
        self._GpuCount = params.get("GpuCount")
        self._Frequency = params.get("Frequency")
        self._StatusCategory = params.get("StatusCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型。取值范围：<br><li>BANDWIDTH_PREPAID：预付费按带宽结算</li><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费</li><li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费</li><li>BANDWIDTH_PACKAGE：带宽包用户</li>默认取值：非带宽包用户默认与子机付费类型保持一致，比如子机付费类型为预付费，网络计费类型默认为预付费；子机付费类型为后付费，网络计费类型默认为后付费。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](https://cloud.tencent.com/document/product/213/12523)。
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: 是否分配公网IP。取值范围：<br><li>true：表示分配公网IP</li><li>false：表示不分配公网IP</li><br>当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。该参数仅在RunInstances接口中作为入参使用。
        :type PublicIpAssigned: bool
        :param _BandwidthPackageId: 带宽包ID。可通过[`DescribeBandwidthPackages`](https://cloud.tencent.com/document/api/215/19209)接口返回值中的`BandwidthPackageId`获取。该参数仅在RunInstances接口中作为入参使用。
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetBandwidthConfig(AbstractModel):
    """描述了按带宽计费的相关信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type StartTime: str
        :param _EndTime: 结束时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type EndTime: str
        :param _InternetAccessible: 实例带宽信息。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        """
        self._StartTime = None
        self._EndTime = None
        self._InternetAccessible = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetChargeTypeConfig(AbstractModel):
    """描述了网络计费

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费模式。
        :type InternetChargeType: str
        :param _Description: 网络计费模式描述信息。
        :type Description: str
        """
        self._InternetChargeType = None
        self._Description = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """描述了单项的价格信息

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 后续合计费用的原价，后付费模式使用，单位：元。<br><li>如返回了其他时间区间项，如UnitPriceSecondStep，则本项代表时间区间在(0, 96)小时；若未返回其他时间区间项，则本项代表全时段，即(0, ∞)小时</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _ChargeUnit: 后续计价单元，后付费模式使用，可取值范围： <br><li>HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）：</li><li>GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param _OriginalPrice: 预支合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPrice: 预支合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _Discount: 折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param _UnitPriceDiscount: 后续合计费用的折扣价，后付费模式使用，单位：元<br><li>如返回了其他时间区间项，如UnitPriceDiscountSecondStep，则本项代表时间区间在(0, 96)小时；若未返回其他时间区间项，则本项代表全时段，即(0, ∞)小时</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _UnitPriceSecondStep: 使用时间区间在(96, 360)小时的后续合计费用的原价，后付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceSecondStep: float
        :param _UnitPriceDiscountSecondStep: 使用时间区间在(96, 360)小时的后续合计费用的折扣价，后付费模式使用，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountSecondStep: float
        :param _UnitPriceThirdStep: 使用时间区间在(360, ∞)小时的后续合计费用的原价，后付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceThirdStep: float
        :param _UnitPriceDiscountThirdStep: 使用时间区间在(360, ∞)小时的后续合计费用的折扣价，后付费模式使用，单位：元
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountThirdStep: float
        :param _OriginalPriceThreeYear: 预支三年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceThreeYear: float
        :param _DiscountPriceThreeYear: 预支三年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceThreeYear: float
        :param _DiscountThreeYear: 预支三年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountThreeYear: float
        :param _OriginalPriceFiveYear: 预支五年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceFiveYear: float
        :param _DiscountPriceFiveYear: 预支五年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceFiveYear: float
        :param _DiscountFiveYear: 预支五年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountFiveYear: float
        :param _OriginalPriceOneYear: 预支一年合计费用的原价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPriceOneYear: float
        :param _DiscountPriceOneYear: 预支一年合计费用的折扣价，预付费模式使用，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPriceOneYear: float
        :param _DiscountOneYear: 预支一年应用的折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountOneYear: float
        """
        self._UnitPrice = None
        self._ChargeUnit = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._UnitPriceDiscount = None
        self._UnitPriceSecondStep = None
        self._UnitPriceDiscountSecondStep = None
        self._UnitPriceThirdStep = None
        self._UnitPriceDiscountThirdStep = None
        self._OriginalPriceThreeYear = None
        self._DiscountPriceThreeYear = None
        self._DiscountThreeYear = None
        self._OriginalPriceFiveYear = None
        self._DiscountPriceFiveYear = None
        self._DiscountFiveYear = None
        self._OriginalPriceOneYear = None
        self._DiscountPriceOneYear = None
        self._DiscountOneYear = None

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceSecondStep(self):
        return self._UnitPriceSecondStep

    @UnitPriceSecondStep.setter
    def UnitPriceSecondStep(self, UnitPriceSecondStep):
        self._UnitPriceSecondStep = UnitPriceSecondStep

    @property
    def UnitPriceDiscountSecondStep(self):
        return self._UnitPriceDiscountSecondStep

    @UnitPriceDiscountSecondStep.setter
    def UnitPriceDiscountSecondStep(self, UnitPriceDiscountSecondStep):
        self._UnitPriceDiscountSecondStep = UnitPriceDiscountSecondStep

    @property
    def UnitPriceThirdStep(self):
        return self._UnitPriceThirdStep

    @UnitPriceThirdStep.setter
    def UnitPriceThirdStep(self, UnitPriceThirdStep):
        self._UnitPriceThirdStep = UnitPriceThirdStep

    @property
    def UnitPriceDiscountThirdStep(self):
        return self._UnitPriceDiscountThirdStep

    @UnitPriceDiscountThirdStep.setter
    def UnitPriceDiscountThirdStep(self, UnitPriceDiscountThirdStep):
        self._UnitPriceDiscountThirdStep = UnitPriceDiscountThirdStep

    @property
    def OriginalPriceThreeYear(self):
        return self._OriginalPriceThreeYear

    @OriginalPriceThreeYear.setter
    def OriginalPriceThreeYear(self, OriginalPriceThreeYear):
        self._OriginalPriceThreeYear = OriginalPriceThreeYear

    @property
    def DiscountPriceThreeYear(self):
        return self._DiscountPriceThreeYear

    @DiscountPriceThreeYear.setter
    def DiscountPriceThreeYear(self, DiscountPriceThreeYear):
        self._DiscountPriceThreeYear = DiscountPriceThreeYear

    @property
    def DiscountThreeYear(self):
        return self._DiscountThreeYear

    @DiscountThreeYear.setter
    def DiscountThreeYear(self, DiscountThreeYear):
        self._DiscountThreeYear = DiscountThreeYear

    @property
    def OriginalPriceFiveYear(self):
        return self._OriginalPriceFiveYear

    @OriginalPriceFiveYear.setter
    def OriginalPriceFiveYear(self, OriginalPriceFiveYear):
        self._OriginalPriceFiveYear = OriginalPriceFiveYear

    @property
    def DiscountPriceFiveYear(self):
        return self._DiscountPriceFiveYear

    @DiscountPriceFiveYear.setter
    def DiscountPriceFiveYear(self, DiscountPriceFiveYear):
        self._DiscountPriceFiveYear = DiscountPriceFiveYear

    @property
    def DiscountFiveYear(self):
        return self._DiscountFiveYear

    @DiscountFiveYear.setter
    def DiscountFiveYear(self, DiscountFiveYear):
        self._DiscountFiveYear = DiscountFiveYear

    @property
    def OriginalPriceOneYear(self):
        return self._OriginalPriceOneYear

    @OriginalPriceOneYear.setter
    def OriginalPriceOneYear(self, OriginalPriceOneYear):
        self._OriginalPriceOneYear = OriginalPriceOneYear

    @property
    def DiscountPriceOneYear(self):
        return self._DiscountPriceOneYear

    @DiscountPriceOneYear.setter
    def DiscountPriceOneYear(self, DiscountPriceOneYear):
        self._DiscountPriceOneYear = DiscountPriceOneYear

    @property
    def DiscountOneYear(self):
        return self._DiscountOneYear

    @DiscountOneYear.setter
    def DiscountOneYear(self, DiscountOneYear):
        self._DiscountOneYear = DiscountOneYear


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._UnitPriceSecondStep = params.get("UnitPriceSecondStep")
        self._UnitPriceDiscountSecondStep = params.get("UnitPriceDiscountSecondStep")
        self._UnitPriceThirdStep = params.get("UnitPriceThirdStep")
        self._UnitPriceDiscountThirdStep = params.get("UnitPriceDiscountThirdStep")
        self._OriginalPriceThreeYear = params.get("OriginalPriceThreeYear")
        self._DiscountPriceThreeYear = params.get("DiscountPriceThreeYear")
        self._DiscountThreeYear = params.get("DiscountThreeYear")
        self._OriginalPriceFiveYear = params.get("OriginalPriceFiveYear")
        self._DiscountPriceFiveYear = params.get("DiscountPriceFiveYear")
        self._DiscountFiveYear = params.get("DiscountFiveYear")
        self._OriginalPriceOneYear = params.get("OriginalPriceOneYear")
        self._DiscountPriceOneYear = params.get("DiscountPriceOneYear")
        self._DiscountOneYear = params.get("DiscountOneYear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """描述密钥对信息

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥对的`ID`，是密钥对的唯一标识。
        :type KeyId: str
        :param _KeyName: 密钥对名称。
        :type KeyName: str
        :param _ProjectId: 密钥对所属的项目`ID`。
        :type ProjectId: int
        :param _Description: 密钥对描述信息。
        :type Description: str
        :param _PublicKey: 密钥对的纯文本公钥。
        :type PublicKey: str
        :param _PrivateKey: 密钥对的纯文本私钥。腾讯云不会保管私钥，请用户自行妥善保存。
        :type PrivateKey: str
        :param _AssociatedInstanceIds: 密钥关联的实例`ID`列表。
        :type AssociatedInstanceIds: list of str
        :param _CreatedTime: 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param _Tags: 密钥关联的标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._KeyId = None
        self._KeyName = None
        self._ProjectId = None
        self._Description = None
        self._PublicKey = None
        self._PrivateKey = None
        self._AssociatedInstanceIds = None
        self._CreatedTime = None
        self._Tags = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def AssociatedInstanceIds(self):
        return self._AssociatedInstanceIds

    @AssociatedInstanceIds.setter
    def AssociatedInstanceIds(self, AssociatedInstanceIds):
        self._AssociatedInstanceIds = AssociatedInstanceIds

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._PublicKey = params.get("PublicKey")
        self._PrivateKey = params.get("PrivateKey")
        self._AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplate(AbstractModel):
    """实例启动模板，通过该参数可使用实例模板中的预设参数创建实例。

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: 实例启动模板ID，通过该参数可使用实例模板中的预设参数创建实例。
        :type LaunchTemplateId: str
        :param _LaunchTemplateVersion: 实例启动模板版本号，若给定，新实例启动模板将基于给定的版本号创建
        :type LaunchTemplateVersion: int
        """
        self._LaunchTemplateId = None
        self._LaunchTemplateVersion = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateVersion(self):
        return self._LaunchTemplateVersion

    @LaunchTemplateVersion.setter
    def LaunchTemplateVersion(self, LaunchTemplateVersion):
        self._LaunchTemplateVersion = LaunchTemplateVersion


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateInfo(AbstractModel):
    """实例启动模板简要信息。

    """

    def __init__(self):
        r"""
        :param _LatestVersionNumber: 实例启动模版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersionNumber: int
        :param _LaunchTemplateId: 实例启动模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateId: str
        :param _LaunchTemplateName: 实例启动模板名。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateName: str
        :param _DefaultVersionNumber: 实例启动模板默认版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultVersionNumber: int
        :param _LaunchTemplateVersionCount: 实例启动模板包含的版本总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateVersionCount: int
        :param _CreatedBy: 创建该模板的用户UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedBy: str
        :param _CreationTime: 创建该模板的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        """
        self._LatestVersionNumber = None
        self._LaunchTemplateId = None
        self._LaunchTemplateName = None
        self._DefaultVersionNumber = None
        self._LaunchTemplateVersionCount = None
        self._CreatedBy = None
        self._CreationTime = None

    @property
    def LatestVersionNumber(self):
        return self._LatestVersionNumber

    @LatestVersionNumber.setter
    def LatestVersionNumber(self, LatestVersionNumber):
        self._LatestVersionNumber = LatestVersionNumber

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def LaunchTemplateName(self):
        return self._LaunchTemplateName

    @LaunchTemplateName.setter
    def LaunchTemplateName(self, LaunchTemplateName):
        self._LaunchTemplateName = LaunchTemplateName

    @property
    def DefaultVersionNumber(self):
        return self._DefaultVersionNumber

    @DefaultVersionNumber.setter
    def DefaultVersionNumber(self, DefaultVersionNumber):
        self._DefaultVersionNumber = DefaultVersionNumber

    @property
    def LaunchTemplateVersionCount(self):
        return self._LaunchTemplateVersionCount

    @LaunchTemplateVersionCount.setter
    def LaunchTemplateVersionCount(self, LaunchTemplateVersionCount):
        self._LaunchTemplateVersionCount = LaunchTemplateVersionCount

    @property
    def CreatedBy(self):
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime


    def _deserialize(self, params):
        self._LatestVersionNumber = params.get("LatestVersionNumber")
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._LaunchTemplateName = params.get("LaunchTemplateName")
        self._DefaultVersionNumber = params.get("DefaultVersionNumber")
        self._LaunchTemplateVersionCount = params.get("LaunchTemplateVersionCount")
        self._CreatedBy = params.get("CreatedBy")
        self._CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionData(AbstractModel):
    """实例启动模板版本信息

    """

    def __init__(self):
        r"""
        :param _Placement: 实例所在的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _InstanceType: 实例机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _InstanceName: 实例名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _InstanceChargeType: 实例计费模式。取值范围：<br><li>`PREPAID`：表示预付费，即包年包月<br><li>`POSTPAID_BY_HOUR`：表示后付费，即按量计费<br><li>`CDHPAID`：`专用宿主机`付费，即只对`专用宿主机`计费，不对`专用宿主机`上的实例计费。<br><li>`SPOTPAID`：表示竞价实例付费。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param _SystemDisk: 实例系统盘信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: 实例数据盘信息。只包含随实例购买的数据盘。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 实例带宽信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _VirtualPrivateCloud: 实例所属虚拟私有网络信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _ImageId: 生产实例所使用的镜像`ID`。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param _LoginSettings: 实例登录设置。目前只返回实例所关联的密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _CamRoleName: CAM角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type CamRoleName: str
        :param _HpcClusterId: 高性能计算集群`ID`。
注意：此字段可能返回 null，表示取不到有效值。
        :type HpcClusterId: str
        :param _InstanceCount: 购买实例数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param _EnhancedService: 增强服务。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserData: str
        :param _DisasterRecoverGroupIds: 置放群组ID，仅支持指定一个。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisasterRecoverGroupIds: list of str
        :param _ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _HostName: 云服务器的主机名。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param _ClientToken: 用于保证请求幂等性的字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的云服务器、云硬盘实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: list of TagSpecification
        :param _DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：

TRUE：表示开启实例保护，不允许通过api接口删除实例
FALSE：表示关闭实例保护，允许通过api接口删除实例

默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableApiTermination: bool
        """
        self._Placement = None
        self._InstanceType = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._VirtualPrivateCloud = None
        self._ImageId = None
        self._SecurityGroupIds = None
        self._LoginSettings = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._InstanceCount = None
        self._EnhancedService = None
        self._UserData = None
        self._DisasterRecoverGroupIds = None
        self._ActionTimer = None
        self._InstanceMarketOptions = None
        self._HostName = None
        self._ClientToken = None
        self._InstanceChargePrepaid = None
        self._TagSpecification = None
        self._DisableApiTermination = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ImageId = params.get("ImageId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        self._InstanceCount = params.get("InstanceCount")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._UserData = params.get("UserData")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._HostName = params.get("HostName")
        self._ClientToken = params.get("ClientToken")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionInfo(AbstractModel):
    """实例启动模板版本集合

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateVersion: 实例启动模板版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateVersion: int
        :param _LaunchTemplateVersionData: 实例启动模板版本数据详情。
        :type LaunchTemplateVersionData: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplateVersionData`
        :param _CreationTime: 实例启动模板版本创建时间。
        :type CreationTime: str
        :param _LaunchTemplateId: 实例启动模板ID。
        :type LaunchTemplateId: str
        :param _IsDefaultVersion: 是否为默认启动模板版本。
        :type IsDefaultVersion: bool
        :param _LaunchTemplateVersionDescription: 实例启动模板版本描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LaunchTemplateVersionDescription: str
        :param _CreatedBy: 创建者。
        :type CreatedBy: str
        """
        self._LaunchTemplateVersion = None
        self._LaunchTemplateVersionData = None
        self._CreationTime = None
        self._LaunchTemplateId = None
        self._IsDefaultVersion = None
        self._LaunchTemplateVersionDescription = None
        self._CreatedBy = None

    @property
    def LaunchTemplateVersion(self):
        return self._LaunchTemplateVersion

    @LaunchTemplateVersion.setter
    def LaunchTemplateVersion(self, LaunchTemplateVersion):
        self._LaunchTemplateVersion = LaunchTemplateVersion

    @property
    def LaunchTemplateVersionData(self):
        return self._LaunchTemplateVersionData

    @LaunchTemplateVersionData.setter
    def LaunchTemplateVersionData(self, LaunchTemplateVersionData):
        self._LaunchTemplateVersionData = LaunchTemplateVersionData

    @property
    def CreationTime(self):
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def IsDefaultVersion(self):
        return self._IsDefaultVersion

    @IsDefaultVersion.setter
    def IsDefaultVersion(self, IsDefaultVersion):
        self._IsDefaultVersion = IsDefaultVersion

    @property
    def LaunchTemplateVersionDescription(self):
        return self._LaunchTemplateVersionDescription

    @LaunchTemplateVersionDescription.setter
    def LaunchTemplateVersionDescription(self, LaunchTemplateVersionDescription):
        self._LaunchTemplateVersionDescription = LaunchTemplateVersionDescription

    @property
    def CreatedBy(self):
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy


    def _deserialize(self, params):
        self._LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        if params.get("LaunchTemplateVersionData") is not None:
            self._LaunchTemplateVersionData = LaunchTemplateVersionData()
            self._LaunchTemplateVersionData._deserialize(params.get("LaunchTemplateVersionData"))
        self._CreationTime = params.get("CreationTime")
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._IsDefaultVersion = params.get("IsDefaultVersion")
        self._LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self._CreatedBy = params.get("CreatedBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskType(AbstractModel):
    """本地磁盘规格

    """

    def __init__(self):
        r"""
        :param _Type: 本地磁盘类型。
        :type Type: str
        :param _PartitionType: 本地磁盘属性。
        :type PartitionType: str
        :param _MinSize: 本地磁盘最小值。
        :type MinSize: int
        :param _MaxSize: 本地磁盘最大值。
        :type MaxSize: int
        :param _Required: 购买时本地盘是否为必选。取值范围：<br><li>REQUIRED：表示必选<br><li>OPTIONAL：表示可选。
        :type Required: str
        """
        self._Type = None
        self._PartitionType = None
        self._MinSize = None
        self._MaxSize = None
        self._Required = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PartitionType(self):
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._PartitionType = params.get("PartitionType")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口[DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699)获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyIds: list of str
        :param _KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepImageLogin: str
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._KeyIds = params.get("KeyIds")
        self._KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeRequest(AbstractModel):
    """ModifyChcAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC物理服务器ID。
        :type ChcIds: list of str
        :param _InstanceName: CHC物理服务器名称
        :type InstanceName: str
        :param _DeviceType: 服务器类型
        :type DeviceType: str
        :param _BmcUser: 合法字符为字母,数字, 横线和下划线
        :type BmcUser: str
        :param _Password: 密码8-16位字符, 允许数字，字母， 和特殊字符()`~!@#$%^&*-+=_|{}[]:;'<>,.?/
        :type Password: str
        :param _BmcSecurityGroupIds: bmc网络的安全组列表
        :type BmcSecurityGroupIds: list of str
        """
        self._ChcIds = None
        self._InstanceName = None
        self._DeviceType = None
        self._BmcUser = None
        self._Password = None
        self._BmcSecurityGroupIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def BmcUser(self):
        return self._BmcUser

    @BmcUser.setter
    def BmcUser(self, BmcUser):
        self._BmcUser = BmcUser

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def BmcSecurityGroupIds(self):
        return self._BmcSecurityGroupIds

    @BmcSecurityGroupIds.setter
    def BmcSecurityGroupIds(self, BmcSecurityGroupIds):
        self._BmcSecurityGroupIds = BmcSecurityGroupIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        self._InstanceName = params.get("InstanceName")
        self._DeviceType = params.get("DeviceType")
        self._BmcUser = params.get("BmcUser")
        self._Password = params.get("Password")
        self._BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeResponse(AbstractModel):
    """ModifyChcAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDisasterRecoverGroupAttributeRequest(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisasterRecoverGroupId: 分散置放群组ID，可使用[DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810)接口获取。
        :type DisasterRecoverGroupId: str
        :param _Name: 分散置放群组名称，长度1-60个字符，支持中、英文。
        :type Name: str
        """
        self._DisasterRecoverGroupId = None
        self._Name = None

    @property
    def DisasterRecoverGroupId(self):
        return self._DisasterRecoverGroupId

    @DisasterRecoverGroupId.setter
    def DisasterRecoverGroupId(self, DisasterRecoverGroupId):
        self._DisasterRecoverGroupId = DisasterRecoverGroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisasterRecoverGroupAttributeResponse(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyHostsAttributeRequest(AbstractModel):
    """ModifyHostsAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HostIds: 一个或多个待操作的CDH实例ID。
        :type HostIds: list of str
        :param _HostName: CDH实例显示名称。可任意命名，但不得超过60个字符。
        :type HostName: str
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param _ProjectId: 项目ID。项目可以使用[AddProject](https://cloud.tencent.com/doc/api/403/4398)接口创建。可通过[`DescribeProject`](https://cloud.tencent.com/document/product/378/4400) API返回值中的`projectId`获取。后续使用[DescribeHosts](https://cloud.tencent.com/document/api/213/16474)接口查询实例时，项目ID可用于过滤结果。
        :type ProjectId: int
        """
        self._HostIds = None
        self._HostName = None
        self._RenewFlag = None
        self._ProjectId = None

    @property
    def HostIds(self):
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._HostIds = params.get("HostIds")
        self._HostName = params.get("HostName")
        self._RenewFlag = params.get("RenewFlag")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsAttributeResponse(AbstractModel):
    """ModifyHostsAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyHpcClusterAttributeRequest(AbstractModel):
    """ModifyHpcClusterAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HpcClusterId: 高性能计算集群ID。
        :type HpcClusterId: str
        :param _Name: 高性能计算集群新名称。
        :type Name: str
        :param _Remark: 高性能计算集群新备注。
        :type Remark: str
        """
        self._HpcClusterId = None
        self._Name = None
        self._Remark = None

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._HpcClusterId = params.get("HpcClusterId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHpcClusterAttributeResponse(AbstractModel):
    """ModifyHpcClusterAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID，形如`img-gvbnzy6f`。镜像ID可以通过如下方式获取：<li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。</li><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。</li>
        :type ImageId: str
        :param _ImageName: 设置新的镜像名称；必须满足下列限制 <li> 不得超过60个字符。</li><li> 镜像名称不能与已有镜像重复。</li>
        :type ImageName: str
        :param _ImageDescription: 设置新的镜像描述；必须满足下列限制： <li> 不得超过 256 个字符。</li>
        :type ImageDescription: str
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageDescription = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyImageSharePermissionRequest(AbstractModel):
    """ModifyImageSharePermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID，形如`img-gvbnzy6f`。镜像Id可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。</li><br><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。</li> <br>镜像ID必须指定为状态为`NORMAL`的镜像。镜像状态请参考[镜像数据表](https://cloud.tencent.com/document/product/213/15753#Image)。
        :type ImageId: str
        :param _AccountIds: 接收共享镜像的主账号ID列表，array型参数的格式可以参考[API简介](/document/api/213/568)。账号ID不同于QQ号，查询用户主账号ID请查看[账号信息](https://console.cloud.tencent.com/developer)中的账号ID栏。
        :type AccountIds: list of str
        :param _Permission: 操作，包括 `SHARE`，`CANCEL`。其中`SHARE`代表共享操作，`CANCEL`代表取消共享操作。
        :type Permission: str
        """
        self._ImageId = None
        self._AccountIds = None
        self._Permission = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def AccountIds(self):
        return self._AccountIds

    @AccountIds.setter
    def AccountIds(self, AccountIds):
        self._AccountIds = AccountIds

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._AccountIds = params.get("AccountIds")
        self._Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSharePermissionResponse(AbstractModel):
    """ModifyImageSharePermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstanceDiskTypeRequest(AbstractModel):
    """ModifyInstanceDiskType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/9388) 接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param _DataDisks: 实例数据盘配置信息，只需要指定要转换的目标云硬盘的介质类型，指定DiskType的值，当前只支持一个数据盘转化。只支持CDHPAID类型实例指定CdcId参数。
        :type DataDisks: list of DataDisk
        :param _SystemDisk: 实例系统盘配置信息，只需要指定要转换的目标云硬盘的介质类型，指定DiskType的值。只支持CDHPAID类型实例指定CdcId参数。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        """
        self._InstanceId = None
        self._DataDisks = None
        self._SystemDisk = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceDiskTypeResponse(AbstractModel):
    """ModifyInstanceDiskType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param _InstanceName: 修改后实例名称。可任意命名，但不得超过60个字符。
<dx-alert infotype="explain" title="">必须指定InstanceName与SecurityGroups的其中一个，但不能同时设置</dx-alert>
        :type InstanceName: str
        :param _UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16 KB。关于获取此参数的详细介绍，请参阅 [Windows](https://cloud.tencent.com/document/product/213/17526) 和 [Linux](https://cloud.tencent.com/document/product/213/17525) 启动时运行命令。
        :type UserData: str
        :param _SecurityGroups: 指定实例的修改后的安全组Id列表，子机将重新关联指定列表的安全组，原本关联的安全组会被解绑。<dx-alert infotype="explain" title="">必须指定SecurityGroups与InstanceName的其中一个，但不能同时设置</dx-alert>
        :type SecurityGroups: list of str
        :param _CamRoleName: 给实例绑定用户角色，传空值为解绑操作
        :type CamRoleName: str
        :param _HostName: 修改后实例的主机名。<li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><li>Windows 实例：主机名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><li>其他类型（Linux 等）实例：主机名字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li>注意点：修改主机名后实例会立即重启，重启后新的主机名生效。
        :type HostName: str
        :param _DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<li>true：表示开启实例保护，不允许通过api接口删除实例</li><li>false：表示关闭实例保护，允许通过api接口删除实例</li>默认取值：false。
        :type DisableApiTermination: bool
        :param _CamRoleType: 角色类别，与CamRoleName搭配使用，该值可从CAM DescribeRoleList, GetRole接口返回RoleType字段获取，当前只接受user、system和service_linked三种类别。
举例：一般CamRoleName中包含“LinkedRoleIn”（如TKE_QCSLinkedRoleInPrometheusService）时，DescribeRoleList和GetRole返回的RoleType为service_linked，则本参数也需要传递service_linked。
该参数默认值为user，若CameRoleName为非service_linked类型，本参数可不传递。
        :type CamRoleType: str
        :param _AutoReboot: 修改实例主机名是否自动重启实例，不传默认自动重启。
- true: 修改主机名，并自动重启实例；
- false: 修改主机名，不自动重启实例，需要手动重启使新主机名生效。
注意点：本参数仅对修改主机名生效。
        :type AutoReboot: bool
        """
        self._InstanceIds = None
        self._InstanceName = None
        self._UserData = None
        self._SecurityGroups = None
        self._CamRoleName = None
        self._HostName = None
        self._DisableApiTermination = None
        self._CamRoleType = None
        self._AutoReboot = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def SecurityGroups(self):
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination

    @property
    def CamRoleType(self):
        return self._CamRoleType

    @CamRoleType.setter
    def CamRoleType(self, CamRoleType):
        self._CamRoleType = CamRoleType

    @property
    def AutoReboot(self):
        return self._AutoReboot

    @AutoReboot.setter
    def AutoReboot(self, AutoReboot):
        self._AutoReboot = AutoReboot


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceName = params.get("InstanceName")
        self._UserData = params.get("UserData")
        self._SecurityGroups = params.get("SecurityGroups")
        self._CamRoleName = params.get("CamRoleName")
        self._HostName = params.get("HostName")
        self._DisableApiTermination = params.get("DisableApiTermination")
        self._CamRoleType = params.get("CamRoleType")
        self._AutoReboot = params.get("AutoReboot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstancesChargeTypeRequest(AbstractModel):
    """ModifyInstancesChargeType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为30。
        :type InstanceIds: list of str
        :param _InstanceChargeType: 修改后实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月。<br><li>POSTPAID_BY_HOUR：后付费，即按量付费。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 修改后预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。<dx-alert infotype="explain" title="">若指定实例的付费模式为预付费则该参数必传。</dx-alert>
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _ModifyPortableDataDisk: 是否同时切换弹性数据云盘计费模式。取值范围：<br><li>true：表示切换弹性数据云盘计费模式<br><li>false：表示不切换弹性数据云盘计费模式<br><br>默认取值：false。
        :type ModifyPortableDataDisk: bool
        """
        self._InstanceIds = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._ModifyPortableDataDisk = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def ModifyPortableDataDisk(self):
        return self._ModifyPortableDataDisk

    @ModifyPortableDataDisk.setter
    def ModifyPortableDataDisk(self, ModifyPortableDataDisk):
        self._ModifyPortableDataDisk = ModifyPortableDataDisk


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._ModifyPortableDataDisk = params.get("ModifyPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesChargeTypeResponse(AbstractModel):
    """ModifyInstancesChargeType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstancesProjectRequest(AbstractModel):
    """ModifyInstancesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param _ProjectId: 项目ID。项目可以使用[AddProject](https://cloud.tencent.com/document/product/651/81952)接口创建。可通过[`DescribeProject`](https://cloud.tencent.com/document/product/378/4400) API返回值中的`projectId`获取。后续使用[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口查询实例时，项目ID可用于过滤结果。
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesProjectResponse(AbstractModel):
    """ModifyInstancesProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstancesRenewFlagRequest(AbstractModel):
    """ModifyInstancesRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li><br>若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._InstanceIds = None
        self._RenewFlag = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesRenewFlagResponse(AbstractModel):
    """ModifyInstancesRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyInstancesVpcAttributeRequest(AbstractModel):
    """ModifyInstancesVpcAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待操作的实例ID数组。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。
        :type InstanceIds: list of str
        :param _VirtualPrivateCloud: 私有网络相关信息配置，通过该参数指定私有网络的ID，子网ID，私有网络ip等信息。<br><li>当指定私有网络ID和子网ID（子网必须在实例所在的可用区）与指定实例所在私有网络不一致时，会将实例迁移至指定的私有网络的子网下。<br><li>可通过`PrivateIpAddresses`指定私有网络子网IP，若需指定则所有已指定的实例均需要指定子网IP，此时`InstanceIds`与`PrivateIpAddresses`一一对应。<br><li>不指定`PrivateIpAddresses`时随机分配私有网络子网IP。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _ForceStop: 是否对运行中的实例选择强制关机。默认为TRUE。
        :type ForceStop: bool
        :param _ReserveHostName: 是否保留主机名。默认为FALSE。
        :type ReserveHostName: bool
        """
        self._InstanceIds = None
        self._VirtualPrivateCloud = None
        self._ForceStop = None
        self._ReserveHostName = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def ReserveHostName(self):
        return self._ReserveHostName

    @ReserveHostName.setter
    def ReserveHostName(self, ReserveHostName):
        self._ReserveHostName = ReserveHostName


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ForceStop = params.get("ForceStop")
        self._ReserveHostName = params.get("ReserveHostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesVpcAttributeResponse(AbstractModel):
    """ModifyInstancesVpcAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyKeyPairAttributeRequest(AbstractModel):
    """ModifyKeyPairAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥对ID，密钥对ID形如：`skey-xxxxxxxx`。<br><br>可以通过以下方式获取可用的密钥 ID：<br><li>通过登录[控制台](https://console.cloud.tencent.com/cvm/sshkey)查询密钥 ID。<br><li>通过调用接口 [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/9403) ，取返回信息中的 `KeyId` 获取密钥对 ID。
        :type KeyId: str
        :param _KeyName: 修改后的密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :type KeyName: str
        :param _Description: 修改后的密钥对描述信息。可任意命名，但不得超过60个字符。
        :type Description: str
        """
        self._KeyId = None
        self._KeyName = None
        self._Description = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKeyPairAttributeResponse(AbstractModel):
    """ModifyKeyPairAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyLaunchTemplateDefaultVersionRequest(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchTemplateId: 启动模板ID。
        :type LaunchTemplateId: str
        :param _DefaultVersion: 待设置的默认版本号。
        :type DefaultVersion: int
        """
        self._LaunchTemplateId = None
        self._DefaultVersion = None

    @property
    def LaunchTemplateId(self):
        return self._LaunchTemplateId

    @LaunchTemplateId.setter
    def LaunchTemplateId(self, LaunchTemplateId):
        self._LaunchTemplateId = LaunchTemplateId

    @property
    def DefaultVersion(self):
        return self._DefaultVersion

    @DefaultVersion.setter
    def DefaultVersion(self, DefaultVersion):
        self._DefaultVersion = DefaultVersion


    def _deserialize(self, params):
        self._LaunchTemplateId = params.get("LaunchTemplateId")
        self._DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLaunchTemplateDefaultVersionResponse(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class OperationCountLimit(AbstractModel):
    """描述了单台实例操作次数限制

    """

    def __init__(self):
        r"""
        :param _Operation: 实例操作。取值范围：<br><li>`INSTANCE_DEGRADE`：降配操作<br><li>`INTERNET_CHARGE_TYPE_CHANGE`：修改网络带宽计费模式
        :type Operation: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _CurrentCount: 当前已使用次数，如果返回值为-1表示该操作无次数限制。
        :type CurrentCount: int
        :param _LimitCount: 操作次数最高额度，如果返回值为-1表示该操作无次数限制，如果返回值为0表示不支持调整配置。
        :type LimitCount: int
        """
        self._Operation = None
        self._InstanceId = None
        self._CurrentCount = None
        self._LimitCount = None

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentCount(self):
        return self._CurrentCount

    @CurrentCount.setter
    def CurrentCount(self, CurrentCount):
        self._CurrentCount = CurrentCount

    @property
    def LimitCount(self):
        return self._LimitCount

    @LimitCount.setter
    def LimitCount(self, LimitCount):
        self._LimitCount = LimitCount


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._InstanceId = params.get("InstanceId")
        self._CurrentCount = params.get("CurrentCount")
        self._LimitCount = params.get("LimitCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """操作系统支持的类型。

    """

    def __init__(self):
        r"""
        :param _OsName: 操作系统类型
        :type OsName: str
        :param _OsVersions: 支持的操作系统版本
        :type OsVersions: list of str
        :param _Architecture: 支持的操作系统架构
        :type Architecture: list of str
        """
        self._OsName = None
        self._OsVersions = None
        self._Architecture = None

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def OsVersions(self):
        return self._OsVersions

    @OsVersions.setter
    def OsVersions(self, OsVersions):
        self._OsVersions = OsVersions

    @property
    def Architecture(self):
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture


    def _deserialize(self, params):
        self._OsName = params.get("OsName")
        self._OsVersions = params.get("OsVersions")
        self._Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目，宿主机（仅专用宿主机产品可用），母机IP等

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属的可用区ID。该参数可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param _HostIds: 实例所属的专用宿主机ID列表，仅用于入参。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。
        :type HostIds: list of str
        :param _HostId: 实例所属的专用宿主机ID，仅用于出参。
        :type HostId: str
        """
        self._Zone = None
        self._ProjectId = None
        self._HostIds = None
        self._HostId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def HostIds(self):
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._HostIds = params.get("HostIds")
        self._HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostPaidQuota(AbstractModel):
    """后付费实例配额

    """

    def __init__(self):
        r"""
        :param _UsedQuota: 累计已使用配额
        :type UsedQuota: int
        :param _RemainingQuota: 剩余配额
        :type RemainingQuota: int
        :param _TotalQuota: 总配额
        :type TotalQuota: int
        :param _Zone: 可用区
        :type Zone: str
        """
        self._UsedQuota = None
        self._RemainingQuota = None
        self._TotalQuota = None
        self._Zone = None

    @property
    def UsedQuota(self):
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def RemainingQuota(self):
        return self._RemainingQuota

    @RemainingQuota.setter
    def RemainingQuota(self, RemainingQuota):
        self._RemainingQuota = RemainingQuota

    @property
    def TotalQuota(self):
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._UsedQuota = params.get("UsedQuota")
        self._RemainingQuota = params.get("RemainingQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrePaidQuota(AbstractModel):
    """预付费实例配额

    """

    def __init__(self):
        r"""
        :param _UsedQuota: 当月已使用配额
        :type UsedQuota: int
        :param _OnceQuota: 单次购买最大数量
        :type OnceQuota: int
        :param _RemainingQuota: 剩余配额
        :type RemainingQuota: int
        :param _TotalQuota: 总配额
        :type TotalQuota: int
        :param _Zone: 可用区
        :type Zone: str
        """
        self._UsedQuota = None
        self._OnceQuota = None
        self._RemainingQuota = None
        self._TotalQuota = None
        self._Zone = None

    @property
    def UsedQuota(self):
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def OnceQuota(self):
        return self._OnceQuota

    @OnceQuota.setter
    def OnceQuota(self, OnceQuota):
        self._OnceQuota = OnceQuota

    @property
    def RemainingQuota(self):
        return self._RemainingQuota

    @RemainingQuota.setter
    def RemainingQuota(self, RemainingQuota):
        self._RemainingQuota = RemainingQuota

    @property
    def TotalQuota(self):
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._UsedQuota = params.get("UsedQuota")
        self._OnceQuota = params.get("OnceQuota")
        self._RemainingQuota = params.get("RemainingQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """价格

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 描述了实例价格。
        :type InstancePrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param _BandwidthPrice: 描述了网络价格。
        :type BandwidthPrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        """
        self._InstancePrice = None
        self._BandwidthPrice = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def BandwidthPrice(self):
        return self._BandwidthPrice

    @BandwidthPrice.setter
    def BandwidthPrice(self, BandwidthPrice):
        self._BandwidthPrice = BandwidthPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self._BandwidthPrice = ItemPrice()
            self._BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramFpgaImageRequest(AbstractModel):
    """ProgramFpgaImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例的ID信息。
        :type InstanceId: str
        :param _FPGAUrl: FPGA镜像文件的COS URL地址。
        :type FPGAUrl: str
        :param _DBDFs: 实例上FPGA卡的DBDF号，不填默认烧录FPGA镜像到实例所拥有的所有FPGA卡。
        :type DBDFs: list of str
        :param _DryRun: 试运行，不会执行实际的烧录动作，默认为False。
        :type DryRun: bool
        """
        self._InstanceId = None
        self._FPGAUrl = None
        self._DBDFs = None
        self._DryRun = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FPGAUrl(self):
        return self._FPGAUrl

    @FPGAUrl.setter
    def FPGAUrl(self, FPGAUrl):
        self._FPGAUrl = FPGAUrl

    @property
    def DBDFs(self):
        return self._DBDFs

    @DBDFs.setter
    def DBDFs(self, DBDFs):
        self._DBDFs = DBDFs

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FPGAUrl = params.get("FPGAUrl")
        self._DBDFs = params.get("DBDFs")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramFpgaImageResponse(AbstractModel):
    """ProgramFpgaImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class PurchaseReservedInstancesOfferingRequest(AbstractModel):
    """PurchaseReservedInstancesOffering请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceCount: 购买预留实例计费数量
        :type InstanceCount: int
        :param _ReservedInstancesOfferingId: 预留实例计费配置ID
        :type ReservedInstancesOfferingId: str
        :param _DryRun: 试运行
        :type DryRun: bool
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。<br>更多详细信息请参阅：如何保证幂等性
        :type ClientToken: str
        :param _ReservedInstanceName: 预留实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>最多支持60个字符（包含模式串）。</li>
        :type ReservedInstanceName: str
        """
        self._InstanceCount = None
        self._ReservedInstancesOfferingId = None
        self._DryRun = None
        self._ClientToken = None
        self._ReservedInstanceName = None

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ReservedInstanceName(self):
        return self._ReservedInstanceName

    @ReservedInstanceName.setter
    def ReservedInstanceName(self, ReservedInstanceName):
        self._ReservedInstanceName = ReservedInstanceName


    def _deserialize(self, params):
        self._InstanceCount = params.get("InstanceCount")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._DryRun = params.get("DryRun")
        self._ClientToken = params.get("ClientToken")
        self._ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurchaseReservedInstancesOfferingResponse(AbstractModel):
    """PurchaseReservedInstancesOffering返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReservedInstanceId: 已购买预留实例计费ID
        :type ReservedInstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReservedInstanceId = None
        self._RequestId = None

    @property
    def ReservedInstanceId(self):
        return self._ReservedInstanceId

    @ReservedInstanceId.setter
    def ReservedInstanceId(self, ReservedInstanceId):
        self._ReservedInstanceId = ReservedInstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReservedInstanceId = params.get("ReservedInstanceId")
        self._RequestId = params.get("RequestId")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param _ForceReboot: 本参数已弃用，推荐使用StopType，不可以与参数StopType同时使用。表示是否在正常重启失败后选择强制重启实例。取值范围：<br><li>true：表示在正常重启失败后进行强制重启<br><li>false：表示在正常重启失败后不进行强制重启<br><br>默认取值：false。
        :type ForceReboot: bool
        :param _StopType: 关机类型。取值范围：<br><li>SOFT：表示软关机<br><li>HARD：表示硬关机<br><li>SOFT_FIRST：表示优先软关机，失败再执行硬关机<br><br>默认取值：SOFT。
        :type StopType: str
        """
        self._InstanceIds = None
        self._ForceReboot = None
        self._StopType = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForceReboot(self):
        return self._ForceReboot

    @ForceReboot.setter
    def ForceReboot(self, ForceReboot):
        self._ForceReboot = ForceReboot

    @property
    def StopType(self):
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ForceReboot = params.get("ForceReboot")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域名称，例如，ap-guangzhou
        :type Region: str
        :param _RegionName: 地域描述，例如，华南地区(广州)
        :type RegionName: str
        :param _RegionState: 地域是否可用状态
        :type RegionState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcRequest(AbstractModel):
    """RemoveChcAssistVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC物理服务器Id。
        :type ChcIds: list of str
        """
        self._ChcIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcResponse(AbstractModel):
    """RemoveChcAssistVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RemoveChcDeployVpcRequest(AbstractModel):
    """RemoveChcDeployVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChcIds: CHC物理服务器Id。
        :type ChcIds: list of str
        """
        self._ChcIds = None

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds


    def _deserialize(self, params):
        self._ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcDeployVpcResponse(AbstractModel):
    """RemoveChcDeployVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RenewHostsRequest(AbstractModel):
    """RenewHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HostIds: 一个或多个待操作的CDH实例ID。每次请求的CDH实例的上限为100。
        :type HostIds: list of str
        :param _HostChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type HostChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.ChargePrepaid`
        """
        self._HostIds = None
        self._HostChargePrepaid = None

    @property
    def HostIds(self):
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostChargePrepaid(self):
        return self._HostChargePrepaid

    @HostChargePrepaid.setter
    def HostChargePrepaid(self, HostChargePrepaid):
        self._HostChargePrepaid = HostChargePrepaid


    def _deserialize(self, params):
        self._HostIds = params.get("HostIds")
        if params.get("HostChargePrepaid") is not None:
            self._HostChargePrepaid = ChargePrepaid()
            self._HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewHostsResponse(AbstractModel):
    """RenewHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RenewInstancesRequest(AbstractModel):
    """RenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。<dx-alert infotype="explain" title="">
包年包月实例该参数为必传参数。</dx-alert>
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _RenewPortableDataDisk: 是否续费弹性数据盘。取值范围：<br><li>true：表示续费包年包月实例同时续费其挂载的弹性数据盘<br><li>false：表示续费包年包月实例同时不再续费其挂载的弹性数据盘<br><br>默认取值：true。
        :type RenewPortableDataDisk: bool
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None
        self._RenewPortableDataDisk = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def RenewPortableDataDisk(self):
        return self._RenewPortableDataDisk

    @RenewPortableDataDisk.setter
    def RenewPortableDataDisk(self, RenewPortableDataDisk):
        self._RenewPortableDataDisk = RenewPortableDataDisk


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._RenewPortableDataDisk = params.get("RenewPortableDataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstancesResponse(AbstractModel):
    """RenewInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RepairTaskControlRequest(AbstractModel):
    """RepairTaskControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 待授权任务实例对应的产品类型，支持取值：

- `CVM`：云服务器
- `CDH`：专用宿主机
- `CPM2.0`：裸金属云服务器
        :type Product: str
        :param _InstanceIds: 指定待操作的实例ID列表，仅允许对列表中的实例ID相关的维修任务发起授权。
        :type InstanceIds: list of str
        :param _TaskId: 维修任务ID。
        :type TaskId: str
        :param _Operate: 操作类型，当前只支持传入`AuthorizeRepair`。
        :type Operate: str
        :param _OrderAuthTime: 预约授权时间，形如`2023-01-01 12:00:00`。预约时间需晚于当前时间至少5分钟，且在48小时之内。
        :type OrderAuthTime: str
        :param _TaskSubMethod: 附加的授权处理策略。
        :type TaskSubMethod: str
        """
        self._Product = None
        self._InstanceIds = None
        self._TaskId = None
        self._Operate = None
        self._OrderAuthTime = None
        self._TaskSubMethod = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def OrderAuthTime(self):
        return self._OrderAuthTime

    @OrderAuthTime.setter
    def OrderAuthTime(self, OrderAuthTime):
        self._OrderAuthTime = OrderAuthTime

    @property
    def TaskSubMethod(self):
        return self._TaskSubMethod

    @TaskSubMethod.setter
    def TaskSubMethod(self, TaskSubMethod):
        self._TaskSubMethod = TaskSubMethod


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceIds = params.get("InstanceIds")
        self._TaskId = params.get("TaskId")
        self._Operate = params.get("Operate")
        self._OrderAuthTime = params.get("OrderAuthTime")
        self._TaskSubMethod = params.get("TaskSubMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepairTaskControlResponse(AbstractModel):
    """RepairTaskControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 已完成授权的维修任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RepairTaskInfo(AbstractModel):
    """描述维修任务的相关信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 维修任务ID
        :type TaskId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Alias: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _TaskTypeId: 任务类型ID，与任务类型中文名的对应关系如下：

- `101`：实例运行隐患
- `102`：实例运行异常
- `103`：实例硬盘异常
- `104`：实例网络连接异常
- `105`：实例运行预警
- `106`：实例硬盘预警
- `107`：实例维护升级

各任务类型的具体含义，可参考 [维修任务分类](https://cloud.tencent.com/document/product/213/67789#.E7.BB.B4.E4.BF.AE.E4.BB.BB.E5.8A.A1.E5.88.86.E7.B1.BB)。
        :type TaskTypeId: int
        :param _TaskTypeName: 任务类型中文名
        :type TaskTypeName: str
        :param _TaskStatus: 任务状态ID，与任务状态中文名的对应关系如下：

- `1`：待授权
- `2`：处理中
- `3`：已结束
- `4`：已预约
- `5`：已取消
- `6`：已避免

各任务状态的具体含义，可参考 [任务状态](https://cloud.tencent.com/document/product/213/67789#.E4.BB.BB.E5.8A.A1.E7.8A.B6.E6.80.81)。
        :type TaskStatus: int
        :param _DeviceStatus: 设备状态ID，与设备状态中文名的对应关系如下：

- `1`：故障中
- `2`：处理中
- `3`：正常
- `4`：已预约
- `5`：已取消
- `6`：已避免
        :type DeviceStatus: int
        :param _OperateStatus: 操作状态ID，与操作状态中文名的对应关系如下：

- `1`：未授权
- `2`：已授权
- `3`：已处理
- `4`：已预约
- `5`：已取消
- `6`：已避免
        :type OperateStatus: int
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _AuthTime: 任务授权时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthTime: str
        :param _EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _TaskDetail: 任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskDetail: str
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _VpcId: 所在私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _VpcName: 所在私有网络名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _SubnetId: 所在子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _SubnetName: 所在子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _WanIp: 实例公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param _LanIp: 实例内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LanIp: str
        :param _Product: 产品类型，支持取值：

- `CVM`：云服务器
- `CDH`：专用宿主机
- `CPM2.0`：裸金属云服务器
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param _TaskSubType: 任务子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSubType: str
        :param _AuthType: 任务授权类型
        :type AuthType: int
        :param _AuthSource: 授权渠道，支持取值：

- `Waiting_auth`：待授权
- `Customer_auth`：客户操作授权
- `System_mandatory_auth`：系统默认授权
- `Pre_policy_auth`：预置策略授权
        :type AuthSource: str
        """
        self._TaskId = None
        self._InstanceId = None
        self._Alias = None
        self._TaskTypeId = None
        self._TaskTypeName = None
        self._TaskStatus = None
        self._DeviceStatus = None
        self._OperateStatus = None
        self._CreateTime = None
        self._AuthTime = None
        self._EndTime = None
        self._TaskDetail = None
        self._Zone = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._SubnetId = None
        self._SubnetName = None
        self._WanIp = None
        self._LanIp = None
        self._Product = None
        self._TaskSubType = None
        self._AuthType = None
        self._AuthSource = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def TaskTypeId(self):
        return self._TaskTypeId

    @TaskTypeId.setter
    def TaskTypeId(self, TaskTypeId):
        self._TaskTypeId = TaskTypeId

    @property
    def TaskTypeName(self):
        return self._TaskTypeName

    @TaskTypeName.setter
    def TaskTypeName(self, TaskTypeName):
        self._TaskTypeName = TaskTypeName

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def DeviceStatus(self):
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus

    @property
    def OperateStatus(self):
        return self._OperateStatus

    @OperateStatus.setter
    def OperateStatus(self, OperateStatus):
        self._OperateStatus = OperateStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AuthTime(self):
        return self._AuthTime

    @AuthTime.setter
    def AuthTime(self, AuthTime):
        self._AuthTime = AuthTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskDetail(self):
        return self._TaskDetail

    @TaskDetail.setter
    def TaskDetail(self, TaskDetail):
        self._TaskDetail = TaskDetail

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def WanIp(self):
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def TaskSubType(self):
        return self._TaskSubType

    @TaskSubType.setter
    def TaskSubType(self, TaskSubType):
        self._TaskSubType = TaskSubType

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def AuthSource(self):
        return self._AuthSource

    @AuthSource.setter
    def AuthSource(self, AuthSource):
        self._AuthSource = AuthSource


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskTypeName = params.get("TaskTypeName")
        self._TaskStatus = params.get("TaskStatus")
        self._DeviceStatus = params.get("DeviceStatus")
        self._OperateStatus = params.get("OperateStatus")
        self._CreateTime = params.get("CreateTime")
        self._AuthTime = params.get("AuthTime")
        self._EndTime = params.get("EndTime")
        self._TaskDetail = params.get("TaskDetail")
        self._Zone = params.get("Zone")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._WanIp = params.get("WanIp")
        self._LanIp = params.get("LanIp")
        self._Product = params.get("Product")
        self._TaskSubType = params.get("TaskSubType")
        self._AuthType = params.get("AuthType")
        self._AuthSource = params.get("AuthSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceConfigInfoItem(AbstractModel):
    """预留实例静态配置信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param _Type: 实例规格。
        :type Type: str
        :param _TypeName: 实例规格名称。
        :type TypeName: str
        :param _Order: 优先级。
        :type Order: int
        :param _InstanceFamilies: 实例族信息列表。
        :type InstanceFamilies: list of ReservedInstanceFamilyItem
        """
        self._Type = None
        self._TypeName = None
        self._Order = None
        self._InstanceFamilies = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def InstanceFamilies(self):
        return self._InstanceFamilies

    @InstanceFamilies.setter
    def InstanceFamilies(self, InstanceFamilies):
        self._InstanceFamilies = InstanceFamilies


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TypeName = params.get("TypeName")
        self._Order = params.get("Order")
        if params.get("InstanceFamilies") is not None:
            self._InstanceFamilies = []
            for item in params.get("InstanceFamilies"):
                obj = ReservedInstanceFamilyItem()
                obj._deserialize(item)
                self._InstanceFamilies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceFamilyItem(AbstractModel):
    """预留实例相关实例族信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param _InstanceFamily: 实例族。
        :type InstanceFamily: str
        :param _Order: 优先级。
        :type Order: int
        :param _InstanceTypes: 实例类型信息列表。
        :type InstanceTypes: list of ReservedInstanceTypeItem
        """
        self._InstanceFamily = None
        self._Order = None
        self._InstanceTypes = None

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes


    def _deserialize(self, params):
        self._InstanceFamily = params.get("InstanceFamily")
        self._Order = params.get("Order")
        if params.get("InstanceTypes") is not None:
            self._InstanceTypes = []
            for item in params.get("InstanceTypes"):
                obj = ReservedInstanceTypeItem()
                obj._deserialize(item)
                self._InstanceTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePrice(AbstractModel):
    """预留实例相关价格信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param _OriginalFixedPrice: 预支合计费用的原价，单位：元。
        :type OriginalFixedPrice: float
        :param _DiscountFixedPrice: 预支合计费用的折扣价，单位：元。
        :type DiscountFixedPrice: float
        :param _OriginalUsagePrice: 后续合计费用的原价，单位：元/小时
        :type OriginalUsagePrice: float
        :param _DiscountUsagePrice: 后续合计费用的折扣价，单位：元/小时
        :type DiscountUsagePrice: float
        """
        self._OriginalFixedPrice = None
        self._DiscountFixedPrice = None
        self._OriginalUsagePrice = None
        self._DiscountUsagePrice = None

    @property
    def OriginalFixedPrice(self):
        return self._OriginalFixedPrice

    @OriginalFixedPrice.setter
    def OriginalFixedPrice(self, OriginalFixedPrice):
        self._OriginalFixedPrice = OriginalFixedPrice

    @property
    def DiscountFixedPrice(self):
        return self._DiscountFixedPrice

    @DiscountFixedPrice.setter
    def DiscountFixedPrice(self, DiscountFixedPrice):
        self._DiscountFixedPrice = DiscountFixedPrice

    @property
    def OriginalUsagePrice(self):
        return self._OriginalUsagePrice

    @OriginalUsagePrice.setter
    def OriginalUsagePrice(self, OriginalUsagePrice):
        self._OriginalUsagePrice = OriginalUsagePrice

    @property
    def DiscountUsagePrice(self):
        return self._DiscountUsagePrice

    @DiscountUsagePrice.setter
    def DiscountUsagePrice(self, DiscountUsagePrice):
        self._DiscountUsagePrice = DiscountUsagePrice


    def _deserialize(self, params):
        self._OriginalFixedPrice = params.get("OriginalFixedPrice")
        self._DiscountFixedPrice = params.get("DiscountFixedPrice")
        self._OriginalUsagePrice = params.get("OriginalUsagePrice")
        self._DiscountUsagePrice = params.get("DiscountUsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePriceItem(AbstractModel):
    """基于付费类型的预留实例相关价格信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param _OfferingType: 付费类型，如："All Upfront","Partial Upfront","No Upfront"
        :type OfferingType: str
        :param _FixedPrice: 预支合计费用，单位：元。
        :type FixedPrice: float
        :param _UsagePrice: 后续合计费用，单位：元/小时
        :type UsagePrice: float
        :param _ReservedInstancesOfferingId: 预留实例配置ID
        :type ReservedInstancesOfferingId: str
        :param _Zone: 预留实例计费可购买的可用区。
        :type Zone: str
        :param _Duration: 预留实例计费【有效期】即预留实例计费购买时长。形如：31536000。
计量单位：秒
        :type Duration: int
        :param _ProductDescription: 预留实例计费的平台描述（即操作系统）。形如：Linux。
返回项： Linux 。
        :type ProductDescription: str
        """
        self._OfferingType = None
        self._FixedPrice = None
        self._UsagePrice = None
        self._ReservedInstancesOfferingId = None
        self._Zone = None
        self._Duration = None
        self._ProductDescription = None

    @property
    def OfferingType(self):
        return self._OfferingType

    @OfferingType.setter
    def OfferingType(self, OfferingType):
        self._OfferingType = OfferingType

    @property
    def FixedPrice(self):
        return self._FixedPrice

    @FixedPrice.setter
    def FixedPrice(self, FixedPrice):
        self._FixedPrice = FixedPrice

    @property
    def UsagePrice(self):
        return self._UsagePrice

    @UsagePrice.setter
    def UsagePrice(self, UsagePrice):
        self._UsagePrice = UsagePrice

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription


    def _deserialize(self, params):
        self._OfferingType = params.get("OfferingType")
        self._FixedPrice = params.get("FixedPrice")
        self._UsagePrice = params.get("UsagePrice")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._Zone = params.get("Zone")
        self._Duration = params.get("Duration")
        self._ProductDescription = params.get("ProductDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceTypeItem(AbstractModel):
    """预留实例类型信息。预留实例当前只针对国际站白名单用户开放。

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型。
        :type InstanceType: str
        :param _Cpu: CPU核数。
        :type Cpu: int
        :param _Memory: 内存大小。
        :type Memory: int
        :param _Gpu: GPU数量。
        :type Gpu: int
        :param _Fpga: FPGA数量。
        :type Fpga: int
        :param _StorageBlock: 本地存储块数量。
        :type StorageBlock: int
        :param _NetworkCard: 网卡数。
        :type NetworkCard: int
        :param _MaxBandwidth: 最大带宽。
        :type MaxBandwidth: float
        :param _Frequency: 主频。
        :type Frequency: str
        :param _CpuModelName: CPU型号名称。
        :type CpuModelName: str
        :param _Pps: 包转发率。
        :type Pps: int
        :param _Externals: 外部信息。
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param _Remark: 备注信息。
        :type Remark: str
        :param _Prices: 预留实例配置价格信息。
        :type Prices: list of ReservedInstancePriceItem
        """
        self._InstanceType = None
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._Fpga = None
        self._StorageBlock = None
        self._NetworkCard = None
        self._MaxBandwidth = None
        self._Frequency = None
        self._CpuModelName = None
        self._Pps = None
        self._Externals = None
        self._Remark = None
        self._Prices = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def StorageBlock(self):
        return self._StorageBlock

    @StorageBlock.setter
    def StorageBlock(self, StorageBlock):
        self._StorageBlock = StorageBlock

    @property
    def NetworkCard(self):
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def MaxBandwidth(self):
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CpuModelName(self):
        return self._CpuModelName

    @CpuModelName.setter
    def CpuModelName(self, CpuModelName):
        self._CpuModelName = CpuModelName

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def Externals(self):
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Prices(self):
        return self._Prices

    @Prices.setter
    def Prices(self, Prices):
        self._Prices = Prices


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._Fpga = params.get("Fpga")
        self._StorageBlock = params.get("StorageBlock")
        self._NetworkCard = params.get("NetworkCard")
        self._MaxBandwidth = params.get("MaxBandwidth")
        self._Frequency = params.get("Frequency")
        self._CpuModelName = params.get("CpuModelName")
        self._Pps = params.get("Pps")
        if params.get("Externals") is not None:
            self._Externals = Externals()
            self._Externals._deserialize(params.get("Externals"))
        self._Remark = params.get("Remark")
        if params.get("Prices") is not None:
            self._Prices = []
            for item in params.get("Prices"):
                obj = ReservedInstancePriceItem()
                obj._deserialize(item)
                self._Prices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstances(AbstractModel):
    """描述用户已购买预留实例计费信息

    """

    def __init__(self):
        r"""
        :param _ReservedInstancesId: （此字段已废弃，建议使用字段：ReservedInstanceId）已购买的预留实例计费ID。形如：ri-rtbh4han。
        :type ReservedInstancesId: str
        :param _InstanceType: 预留实例计费的规格。形如：S3.MEDIUM4。
返回项：<a href="https://cloud.tencent.com/document/product/213/11518">预留实例计费规格列表</a>
        :type InstanceType: str
        :param _Zone: 预留实例计费可购买的可用区。形如：ap-guangzhou-1。
返回项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a>
        :type Zone: str
        :param _StartTime: 预留实例计费开始时间。形如：1949-10-01 00:00:00
        :type StartTime: str
        :param _EndTime: 预留实例计费到期时间。形如：1949-10-01 00:00:00
        :type EndTime: str
        :param _Duration: 预留实例计费【有效期】即预留实例计费购买时长。形如：31536000。
计量单位：秒。
        :type Duration: int
        :param _InstanceCount: 已购买的预留实例计费个数。形如：10。
        :type InstanceCount: int
        :param _ProductDescription: 描述预留实例计费的平台描述（即操作系统）。形如：linux。
返回项： linux 。
        :type ProductDescription: str
        :param _State: 预留实例计费购买的状态。形如：active
返回项： active (以创建) | pending (等待被创建) | retired (过期)。
        :type State: str
        :param _CurrencyCode: 可购买的预留实例计费类型的结算货币，使用ISO 4217标准货币代码。形如：USD。
返回项：USD（美元）。
        :type CurrencyCode: str
        :param _OfferingType: 预留实例计费的付款类型。形如：All Upfront。
返回项： All Upfront (预付全部费用)。
        :type OfferingType: str
        :param _InstanceFamily: 预留实例计费的类型。形如：S3。
返回项：<a href="https://cloud.tencent.com/document/product/213/11518">预留实例计费类型列表</a>
        :type InstanceFamily: str
        :param _ReservedInstanceId: 已购买的预留实例计费ID。形如：ri-rtbh4han。
        :type ReservedInstanceId: str
        :param _ReservedInstanceName: 预留实例显示名称。形如：riname-01
        :type ReservedInstanceName: str
        """
        self._ReservedInstancesId = None
        self._InstanceType = None
        self._Zone = None
        self._StartTime = None
        self._EndTime = None
        self._Duration = None
        self._InstanceCount = None
        self._ProductDescription = None
        self._State = None
        self._CurrencyCode = None
        self._OfferingType = None
        self._InstanceFamily = None
        self._ReservedInstanceId = None
        self._ReservedInstanceName = None

    @property
    def ReservedInstancesId(self):
        return self._ReservedInstancesId

    @ReservedInstancesId.setter
    def ReservedInstancesId(self, ReservedInstancesId):
        self._ReservedInstancesId = ReservedInstancesId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CurrencyCode(self):
        return self._CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, CurrencyCode):
        self._CurrencyCode = CurrencyCode

    @property
    def OfferingType(self):
        return self._OfferingType

    @OfferingType.setter
    def OfferingType(self, OfferingType):
        self._OfferingType = OfferingType

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def ReservedInstanceId(self):
        return self._ReservedInstanceId

    @ReservedInstanceId.setter
    def ReservedInstanceId(self, ReservedInstanceId):
        self._ReservedInstanceId = ReservedInstanceId

    @property
    def ReservedInstanceName(self):
        return self._ReservedInstanceName

    @ReservedInstanceName.setter
    def ReservedInstanceName(self, ReservedInstanceName):
        self._ReservedInstanceName = ReservedInstanceName


    def _deserialize(self, params):
        self._ReservedInstancesId = params.get("ReservedInstancesId")
        self._InstanceType = params.get("InstanceType")
        self._Zone = params.get("Zone")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Duration = params.get("Duration")
        self._InstanceCount = params.get("InstanceCount")
        self._ProductDescription = params.get("ProductDescription")
        self._State = params.get("State")
        self._CurrencyCode = params.get("CurrencyCode")
        self._OfferingType = params.get("OfferingType")
        self._InstanceFamily = params.get("InstanceFamily")
        self._ReservedInstanceId = params.get("ReservedInstanceId")
        self._ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancesOffering(AbstractModel):
    """描述可购买预留实例计费信息

    """

    def __init__(self):
        r"""
        :param _Zone: 预留实例计费可购买的可用区。形如：ap-guangzhou-1。
返回项：<a href="https://cloud.tencent.com/document/product/213/6091">可用区列表</a>
        :type Zone: str
        :param _CurrencyCode: 可购买的预留实例计费类型的结算货币，使用ISO 4217标准货币代码。
返回项：USD（美元）。
        :type CurrencyCode: str
        :param _Duration: 预留实例计费【有效期】即预留实例计费购买时长。形如：31536000。
计量单位：秒
        :type Duration: int
        :param _FixedPrice: 预留实例计费的购买价格。形如：4000.0。
计量单位：与 currencyCode 一致，目前支持 USD（美元）
        :type FixedPrice: float
        :param _InstanceType: 预留实例计费的实例类型。形如：S3.MEDIUM4。
返回项：<a href="https://cloud.tencent.com/product/cvm/instances">预留实例计费类型列表</a>
        :type InstanceType: str
        :param _OfferingType: 预留实例计费的付款类型。形如：All Upfront。
返回项： All Upfront (预付全部费用)。
        :type OfferingType: str
        :param _ReservedInstancesOfferingId: 可购买的预留实例计费配置ID。形如：650c138f-ae7e-4750-952a-96841d6e9fc1。
        :type ReservedInstancesOfferingId: str
        :param _ProductDescription: 预留实例计费的平台描述（即操作系统）。形如：linux。
返回项： linux 。
        :type ProductDescription: str
        :param _UsagePrice: 扣除预付费之后的使用价格 (按小时计费)。形如：0.0。
目前，因为只支持 All Upfront 付款类型，所以默认为 0元/小时。
计量单位：元/小时，货币单位与 currencyCode 一致，目前支持 USD（美元）
        :type UsagePrice: float
        """
        self._Zone = None
        self._CurrencyCode = None
        self._Duration = None
        self._FixedPrice = None
        self._InstanceType = None
        self._OfferingType = None
        self._ReservedInstancesOfferingId = None
        self._ProductDescription = None
        self._UsagePrice = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CurrencyCode(self):
        return self._CurrencyCode

    @CurrencyCode.setter
    def CurrencyCode(self, CurrencyCode):
        self._CurrencyCode = CurrencyCode

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FixedPrice(self):
        return self._FixedPrice

    @FixedPrice.setter
    def FixedPrice(self, FixedPrice):
        self._FixedPrice = FixedPrice

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def OfferingType(self):
        return self._OfferingType

    @OfferingType.setter
    def OfferingType(self, OfferingType):
        self._OfferingType = OfferingType

    @property
    def ReservedInstancesOfferingId(self):
        return self._ReservedInstancesOfferingId

    @ReservedInstancesOfferingId.setter
    def ReservedInstancesOfferingId(self, ReservedInstancesOfferingId):
        self._ReservedInstancesOfferingId = ReservedInstancesOfferingId

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def UsagePrice(self):
        return self._UsagePrice

    @UsagePrice.setter
    def UsagePrice(self, UsagePrice):
        self._UsagePrice = UsagePrice


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._CurrencyCode = params.get("CurrencyCode")
        self._Duration = params.get("Duration")
        self._FixedPrice = params.get("FixedPrice")
        self._InstanceType = params.get("InstanceType")
        self._OfferingType = params.get("OfferingType")
        self._ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self._ProductDescription = params.get("ProductDescription")
        self._UsagePrice = params.get("UsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceRequest(AbstractModel):
    """ResetInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
默认取值：默认使用当前镜像。
        :type ImageId: str
        :param _SystemDisk: 实例系统盘配置信息。系统盘为云盘的实例可以通过该参数指定重装后的系统盘大小来实现对系统盘的扩容操作。系统盘大小只支持扩容不支持缩容；重装只支持修改系统盘的大小，不能修改系统盘的类型。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _HostName: 重装系统时，可以指定修改实例的主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><br><li>Windows 实例：主机名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><br><li>其他类型（Linux 等）实例：主机名字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li>
        :type HostName: str
        :param _UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。
        :type UserData: str
        """
        self._InstanceId = None
        self._ImageId = None
        self._SystemDisk = None
        self._LoginSettings = None
        self._EnhancedService = None
        self._HostName = None
        self._UserData = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._HostName = params.get("HostName")
        self._UserData = params.get("UserData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceResponse(AbstractModel):
    """ResetInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """ResetInstancesInternetMaxBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口返回值中的 `InstanceId` 获取。 每次请求批量实例的上限为100。当调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽时，只支持一个实例。
        :type InstanceIds: list of str
        :param _InternetAccessible: 公网出带宽配置。不同机型带宽上限范围不一致，具体限制详见带宽限制对账表。暂时只支持 `InternetMaxBandwidthOut` 参数。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _StartTime: 带宽生效的起始时间。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始时间不能早于当前时间。如果起始时间是今天则新设置的带宽立即生效。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type StartTime: str
        :param _EndTime: 带宽生效的终止时间。格式： `YYYY-MM-DD` ，例如：`2016-10-30` 。新设置的带宽的有效期包含终止时间此日期。终止时间不能晚于包年包月实例的到期时间。实例的到期时间可通过 [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口返回值中的`ExpiredTime`获取。该参数只对包年包月带宽有效，其他模式带宽不支持该参数，否则接口会以相应错误码返回。
        :type EndTime: str
        """
        self._InstanceIds = None
        self._InternetAccessible = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """ResetInstancesInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728) API返回值中的`InstanceId`获取。每次请求允许操作的实例数量上限是100。
        :type InstanceIds: list of str
        :param _Password: 重置后的实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：
Linux 实例密码必须8-30位，推荐使用12位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字：0-9<br><li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;'<>,.?/
Windows 实例密码必须12\~30位，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字： 0-9<br><li>特殊字符：()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/<br><li>如果实例即包含 `Linux` 实例又包含 `Windows` 实例，则密码复杂度限制按照 `Windows` 实例的限制。
        :type Password: str
        :param _UserName: 待重置密码的实例操作系统的用户名。不得超过64个字符。
        :type UserName: str
        :param _ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>true：表示在正常关机失败后进行强制关机<br><li>false：表示在正常关机失败后不进行强制关机<br><br>默认取值：false。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._Password = None
        self._UserName = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Password = params.get("Password")
        self._UserName = params.get("UserName")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ResetInstancesTypeRequest(AbstractModel):
    """ResetInstancesType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。本接口目前仅支持每次操作1个实例。
        :type InstanceIds: list of str
        :param _InstanceType: 调整后的实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口[`DescribeInstanceTypeConfigs`](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机。取值范围：<br><li>true：表示在正常关机失败后进行强制关机<br><li>false：表示在正常关机失败后不进行强制关机<br><br>默认取值：false。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._InstanceType = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesTypeResponse(AbstractModel):
    """ResetInstancesType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ResizeInstanceDisksRequest(AbstractModel):
    """ResizeInstanceDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例ID。可通过[`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param _DataDisks: 待扩容的数据盘配置信息。只支持扩容非弹性数据盘（[`DescribeDisks`](https://cloud.tencent.com/document/api/362/16315)接口返回值中的`Portable`为`false`表示非弹性）。数据盘容量单位：GB。最小扩容步长：10G。关于数据盘类型的选择请参考[硬盘产品简介](https://cloud.tencent.com/document/product/362/2353)。可选数据盘类型受到实例类型`InstanceType`限制。另外允许扩容的最大容量也因数据盘类型的不同而有所差异。
<dx-alert infotype="explain" title="">您必须指定参数DataDisks与SystemDisk的其中一个，但不能同时指定。</dx-alert>
        :type DataDisks: list of DataDisk
        :param _ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再重置用户密码。取值范围：<br><li>true：表示在正常关机失败后进行强制关机</li><br><li>false：表示在正常关机失败后不进行强制关机</li><br><br>默认取值：false。<br><br>强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        :type ForceStop: bool
        :param _SystemDisk: 待扩容的系统盘配置信息。只支持扩容云盘。
<dx-alert infotype="explain" title="">您必须指定参数DataDisks与SystemDisk的其中一个，但不能同时指定。</dx-alert>
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _ResizeOnline: 扩容云盘的方式是否为在线扩容。
        :type ResizeOnline: bool
        """
        self._InstanceId = None
        self._DataDisks = None
        self._ForceStop = None
        self._SystemDisk = None
        self._ResizeOnline = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def ResizeOnline(self):
        return self._ResizeOnline

    @ResizeOnline.setter
    def ResizeOnline(self, ResizeOnline):
        self._ResizeOnline = ResizeOnline


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._ForceStop = params.get("ForceStop")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._ResizeOnline = params.get("ResizeOnline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeInstanceDisksResponse(AbstractModel):
    """ResizeInstanceDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class RunAutomationServiceEnabled(AbstractModel):
    """描述了 “云自动化助手” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启云自动化助手。取值范围：<br><li>true：表示开启云自动化助手服务<br><li>false：表示不开启云自动化助手服务<br><br>默认取值：false。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 实例[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>CDHPAID：独享子机（基于专用宿主机创建，宿主机部分的资源不收费）</li><br><li>SPOTPAID：竞价付费</li><br><li>CDCPAID：专用集群付费</li><br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。
 <b>注：如果您不指定LaunchTemplate参数，则Placement为必选参数。若同时传递Placement和LaunchTemplate，则默认覆盖LaunchTemplate中对应的Placement的值。</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param _InstanceType: 实例机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。若不指定该参数，则系统将根据当前地域的资源售卖情况动态指定默认机型。</li><br><li>对于付费模式为CDHPAID的实例创建，该参数以"CDH_"为前缀，根据CPU和内存配置生成，具体形式为：CDH_XCXG，例如对于创建CPU为1核，内存为1G大小的专用宿主机的实例，该参数应该为CDH_1C1G。</li>
        :type InstanceType: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，传入InstanceType获取当前机型支持的镜像列表，取返回信息中的`ImageId`字段。</li>
 <b>注：如果您不指定LaunchTemplate参数，则ImageId为必选参数。若同时传递ImageId和LaunchTemplate，则默认覆盖LaunchTemplate中对应的ImageId的值。</b>
        :type ImageId: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。若在此参数中指定了私有网络IP，即表示每个实例的主网卡IP；同时，InstanceCount参数必须与私有网络IP的个数一致且不能大于20。
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param _InstanceCount: 购买实例数量。包年包月实例取值范围：[1，500]，按量计费实例取值范围：[1，500]。默认取值：1。指定购买实例的数量不能超过用户所能购买的剩余配额数量，具体配额相关限制详见[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)。
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称。<br><li>不指定实例显示名称则默认显示‘未命名’。</li><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server_{R:3}`，购买1台时，实例显示名称为`server_3`；购买2台时，实例显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。</li><li>购买多台实例，如果不指定模式串，则在实例显示名称添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server_`，购买2台时，实例显示名称分别为`server_1`，`server_2`。</li><li>最多支持60个字符（包含模式串）。</li>
        :type InstanceName: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务；自定义镜像与镜像市场镜像默认不开启云监控，云安全服务，而使用镜像里保留的服务。
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _HostName: 实例主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><br><li>Windows 实例：主机名名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><br><li>其他类型（Linux 等）实例：主机名字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li><br><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server{R:3}`，购买1台时，实例主机名为`server3`；购买2台时，实例主机名分别为`server3`，`server4`。支持指定多个模式串`{R:x}`。</li><br><li>购买多台实例，如果不指定模式串，则在实例主机名添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server`，购买2台时，实例主机名分别为`server1`，`server2`。</li>
        :type HostName: str
        :param _ActionTimer: 定时任务。通过该参数可以为实例指定定时任务，目前仅支持定时销毁。
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param _DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param _TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的云服务器、云硬盘实例。
        :type TagSpecification: list of TagSpecification
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费但没有传递该参数时，默认按当前固定折扣价格出价。
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param _UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB。关于获取此参数的详细介绍，请参阅[Windows](https://cloud.tencent.com/document/product/213/17526)和[Linux](https://cloud.tencent.com/document/product/213/17525)启动时运行命令。
        :type UserData: str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param _CpuTopology: 描述了实例CPU拓扑结构的相关信息。若不指定该参数，则按系统资源情况决定。
        :type CpuTopology: :class:`tencentcloud.cvm.v20170312.models.CpuTopology`
        :param _CamRoleName: CAM角色名称。可通过[`DescribeRoleList`](https://cloud.tencent.com/document/product/598/13887)接口返回值中的`roleName`获取。
        :type CamRoleName: str
        :param _HpcClusterId: 高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :type HpcClusterId: str
        :param _LaunchTemplate: 实例启动模板。
        :type LaunchTemplate: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplate`
        :param _DedicatedClusterId: 指定专用集群创建。
        :type DedicatedClusterId: str
        :param _ChcIds: 指定CHC物理服务器来创建CHC云主机。
        :type ChcIds: list of str
        :param _DisableApiTermination: 实例销毁保护标志，表示是否允许通过api接口删除实例。取值范围：<br><li>true：表示开启实例保护，不允许通过api接口删除实例</li><br><li>false：表示关闭实例保护，允许通过api接口删除实例</li><br><br>默认取值：false。
        :type DisableApiTermination: bool
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._Placement = None
        self._InstanceType = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceCount = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._ClientToken = None
        self._HostName = None
        self._ActionTimer = None
        self._DisasterRecoverGroupIds = None
        self._TagSpecification = None
        self._InstanceMarketOptions = None
        self._UserData = None
        self._DryRun = None
        self._CpuTopology = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._LaunchTemplate = None
        self._DedicatedClusterId = None
        self._ChcIds = None
        self._DisableApiTermination = None

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ActionTimer(self):
        return self._ActionTimer

    @ActionTimer.setter
    def ActionTimer(self, ActionTimer):
        self._ActionTimer = ActionTimer

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def CpuTopology(self):
        return self._CpuTopology

    @CpuTopology.setter
    def CpuTopology(self, CpuTopology):
        self._CpuTopology = CpuTopology

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def LaunchTemplate(self):
        return self._LaunchTemplate

    @LaunchTemplate.setter
    def LaunchTemplate(self, LaunchTemplate):
        self._LaunchTemplate = LaunchTemplate

    @property
    def DedicatedClusterId(self):
        return self._DedicatedClusterId

    @DedicatedClusterId.setter
    def DedicatedClusterId(self, DedicatedClusterId):
        self._DedicatedClusterId = DedicatedClusterId

    @property
    def ChcIds(self):
        return self._ChcIds

    @ChcIds.setter
    def ChcIds(self, ChcIds):
        self._ChcIds = ChcIds

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceType = params.get("InstanceType")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ClientToken = params.get("ClientToken")
        self._HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self._ActionTimer = ActionTimer()
            self._ActionTimer._deserialize(params.get("ActionTimer"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._UserData = params.get("UserData")
        self._DryRun = params.get("DryRun")
        if params.get("CpuTopology") is not None:
            self._CpuTopology = CpuTopology()
            self._CpuTopology._deserialize(params.get("CpuTopology"))
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("LaunchTemplate") is not None:
            self._LaunchTemplate = LaunchTemplate()
            self._LaunchTemplate._deserialize(params.get("LaunchTemplate"))
        self._DedicatedClusterId = params.get("DedicatedClusterId")
        self._ChcIds = params.get("ChcIds")
        self._DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 当通过本接口来创建实例时会返回该参数，表示一个或多个实例`ID`。返回实例`ID`列表并不代表实例创建成功，可根据 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口查询返回的InstancesSet中对应实例的`ID`的状态来判断创建是否完成；如果实例状态由“PENDING(创建中)”变为“RUNNING(运行中)”，则为创建成功。
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “云监控” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[云监控](/document/product/248)服务。取值范围：<br><li>true：表示开启云监控服务<br><li>false：表示不开启云监控服务<br><br>默认取值：true。
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[云安全](/document/product/296)服务。取值范围：<br><li>true：表示开启云安全服务<br><li>false：表示不开启云安全服务<br><br>默认取值：true。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SharePermission(AbstractModel):
    """镜像分享信息结构

    """

    def __init__(self):
        r"""
        :param _CreatedTime: 镜像分享时间
        :type CreatedTime: str
        :param _AccountId: 镜像分享的账户ID
        :type AccountId: str
        """
        self._CreatedTime = None
        self._AccountId = None

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._CreatedTime = params.get("CreatedTime")
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """描述镜像关联的快照信息

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照Id。
        :type SnapshotId: str
        :param _DiskUsage: 创建此快照的云硬盘类型。取值范围：
SYSTEM_DISK：系统盘
DATA_DISK：数据盘。
        :type DiskUsage: str
        :param _DiskSize: 创建此快照的云硬盘大小，单位GB。
        :type DiskSize: int
        """
        self._SnapshotId = None
        self._DiskUsage = None
        self._DiskSize = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotMarketOptions(AbstractModel):
    """竞价相关选项

    """

    def __init__(self):
        r"""
        :param _MaxPrice: 竞价出价
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPrice: str
        :param _SpotInstanceType: 竞价请求类型，当前仅支持类型：one-time
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotInstanceType: str
        """
        self._MaxPrice = None
        self._SpotInstanceType = None

    @property
    def MaxPrice(self):
        return self._MaxPrice

    @MaxPrice.setter
    def MaxPrice(self, MaxPrice):
        self._MaxPrice = MaxPrice

    @property
    def SpotInstanceType(self):
        return self._SpotInstanceType

    @SpotInstanceType.setter
    def SpotInstanceType(self, SpotInstanceType):
        self._SpotInstanceType = SpotInstanceType


    def _deserialize(self, params):
        self._MaxPrice = params.get("MaxPrice")
        self._SpotInstanceType = params.get("SpotInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotPaidQuota(AbstractModel):
    """竞价实例配额

    """

    def __init__(self):
        r"""
        :param _UsedQuota: 已使用配额，单位：vCPU核心数
        :type UsedQuota: int
        :param _RemainingQuota: 剩余配额，单位：vCPU核心数
        :type RemainingQuota: int
        :param _TotalQuota: 总配额，单位：vCPU核心数
        :type TotalQuota: int
        :param _Zone: 可用区
        :type Zone: str
        """
        self._UsedQuota = None
        self._RemainingQuota = None
        self._TotalQuota = None
        self._Zone = None

    @property
    def UsedQuota(self):
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def RemainingQuota(self):
        return self._RemainingQuota

    @RemainingQuota.setter
    def RemainingQuota(self, RemainingQuota):
        self._RemainingQuota = RemainingQuota

    @property
    def TotalQuota(self):
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._UsedQuota = params.get("UsedQuota")
        self._RemainingQuota = params.get("RemainingQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class StopInstancesRequest(AbstractModel):
    """StopInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param _ForceStop: 本参数已弃用，推荐使用StopType，不可以与参数StopType同时使用。表示是否在正常关闭失败后选择强制关闭实例。取值范围：<br><li>true：表示在正常关闭失败后进行强制关闭<br><li>false：表示在正常关闭失败后不进行强制关闭<br><br>默认取值：false。
        :type ForceStop: bool
        :param _StopType: 实例的关闭模式。取值范围：<br><li>SOFT_FIRST：表示在正常关闭失败后进行强制关闭<br><li>HARD：直接强制关闭<br><li>SOFT：仅软关机<br>默认取值：SOFT。
        :type StopType: str
        :param _StoppedMode: 按量计费实例关机收费模式。
取值范围：<br><li>KEEP_CHARGING：关机继续收费<br><li>STOP_CHARGING：关机停止收费<br>默认取值：KEEP_CHARGING。
该参数只针对部分按量计费云硬盘实例生效，详情参考[按量计费实例关机不收费说明](https://cloud.tencent.com/document/product/213/19918)
        :type StoppedMode: str
        """
        self._InstanceIds = None
        self._ForceStop = None
        self._StopType = None
        self._StoppedMode = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ForceStop(self):
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def StopType(self):
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType

    @property
    def StoppedMode(self):
        return self._StoppedMode

    @StoppedMode.setter
    def StoppedMode(self, StoppedMode):
        self._StoppedMode = StoppedMode


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ForceStop = params.get("ForceStop")
        self._StopType = params.get("StopType")
        self._StoppedMode = params.get("StoppedMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class StorageBlock(AbstractModel):
    """HDD的本地存储信息

    """

    def __init__(self):
        r"""
        :param _Type: HDD本地存储类型，值为：LOCAL_PRO.
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _MinSize: HDD本地存储的最小容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinSize: int
        :param _MaxSize: HDD本地存储的最大容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self._Type = None
        self._MinSize = None
        self._MaxSize = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImage(AbstractModel):
    """同步镜像信息

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _Region: 地域
        :type Region: str
        """
        self._ImageId = None
        self._Region = None

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesRequest(AbstractModel):
    """SyncImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageIds: 镜像ID列表 ，镜像ID可以通过如下方式获取：<br><li>通过[DescribeImages](https://cloud.tencent.com/document/api/213/15715)接口返回的`ImageId`获取。</li><li>通过[镜像控制台](https://console.cloud.tencent.com/cvm/image)获取。<br>镜像ID必须满足限制：</li><li>镜像ID对应的镜像状态必须为`NORMAL`。</li>镜像状态请参考[镜像数据表](https://cloud.tencent.com/document/product/213/15753#Image)。
        :type ImageIds: list of str
        :param _DestinationRegions: 目的同步地域列表，必须满足如下限制：<br><li>必须是一个合法的Region。</li><li>如果是自定义镜像，则目标同步地域不能为源地域。</li><li>如果是共享镜像，则目的同步地域仅支持源地域，表示将共享镜像复制为源地域的自定义镜像。</li><li>暂不支持部分地域同步。</li>具体地域参数请参考[Region](https://cloud.tencent.com/document/product/213/6091)。
        :type DestinationRegions: list of str
        :param _DryRun: 检测是否支持发起同步镜像。
        :type DryRun: bool
        :param _ImageName: 目标镜像名称。
        :type ImageName: str
        :param _ImageSetRequired: 是否需要返回目的地域的镜像ID。
        :type ImageSetRequired: bool
        """
        self._ImageIds = None
        self._DestinationRegions = None
        self._DryRun = None
        self._ImageName = None
        self._ImageSetRequired = None

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def DestinationRegions(self):
        return self._DestinationRegions

    @DestinationRegions.setter
    def DestinationRegions(self, DestinationRegions):
        self._DestinationRegions = DestinationRegions

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageSetRequired(self):
        return self._ImageSetRequired

    @ImageSetRequired.setter
    def ImageSetRequired(self, ImageSetRequired):
        self._ImageSetRequired = ImageSetRequired


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        self._DestinationRegions = params.get("DestinationRegions")
        self._DryRun = params.get("DryRun")
        self._ImageName = params.get("ImageName")
        self._ImageSetRequired = params.get("ImageSetRequired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesResponse(AbstractModel):
    """SyncImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageSet: 目的地域的镜像ID信息。
        :type ImageSet: list of SyncImage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageSet = None
        self._RequestId = None

    @property
    def ImageSet(self):
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = SyncImage()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。系统盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_BSSD：通用性SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><br>默认取值：当前有库存的硬盘类型。
        :type DiskType: str
        :param _DiskId: 系统盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID。暂时不支持该参数。
该参数目前仅用于`DescribeInstances`等查询类接口的返回参数，不可用于`RunInstances`等写接口的入参。
        :type DiskId: str
        :param _DiskSize: 系统盘大小，单位：GB。默认值为 50
        :type DiskSize: int
        :param _CdcId: 所属的独享集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None
        self._CdcId = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def CdcId(self):
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对，可以通过调用 [DescribeTags](https://cloud.tencent.com/document/api/651/35316) 返回值中的 Tags 字段来获取。

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """创建资源实例时同时绑定的标签对说明

    """

    def __init__(self):
        r"""
        :param _ResourceType: 标签绑定的资源类型，云服务器为“instance”，专用宿主机为“host”，镜像为“image”，密钥为“keypair”
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _Tags: 标签对列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 一个或多个待操作的实例ID。可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param _ReleasePrepaidDataDisks: 释放实例挂载的包年包月数据盘。true表示销毁实例同时释放包年包月数据盘，false表示只销毁实例。
        :type ReleasePrepaidDataDisks: bool
        """
        self._InstanceIds = None
        self._ReleasePrepaidDataDisks = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ReleasePrepaidDataDisks(self):
        return self._ReleasePrepaidDataDisks

    @ReleasePrepaidDataDisks.setter
    def ReleasePrepaidDataDisks(self, ReleasePrepaidDataDisks):
        self._ReleasePrepaidDataDisks = ReleasePrepaidDataDisks


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ReleasePrepaidDataDisks = params.get("ReleasePrepaidDataDisks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相关信息，包括子网，IP信息等

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。若在创建子机时VpcId与SubnetId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。若在创建子机时SubnetId与VpcId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type SubnetId: str
        :param _AsVpcGateway: 是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：<br><li>true：表示用作公网网关<br><li>false：表示不作为公网网关<br><br>默认取值：false。
        :type AsVpcGateway: bool
        :param _PrivateIpAddresses: 私有网络子网 IP 数组，在创建实例、修改实例vpc属性操作中可使用此参数。当前仅批量创建多台实例时支持传入相同子网的多个 IP。
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: 为弹性网卡指定随机生成的 IPv6 地址数量。
        :type Ipv6AddressCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._AsVpcGateway = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AsVpcGateway(self):
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AsVpcGateway = params.get("AsVpcGateway")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称，例如，ap-guangzhou-3
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
        :param _ZoneName: 可用区描述，例如，广州三区
        :type ZoneName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _ZoneState: 可用区状态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :type ZoneState: str
        """
        self._Zone = None
        self._ZoneName = None
        self._ZoneId = None
        self._ZoneState = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneState(self):
        return self._ZoneState

    @ZoneState.setter
    def ZoneState(self, ZoneState):
        self._ZoneState = ZoneState


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneState = params.get("ZoneState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        