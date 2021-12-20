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


class ApplyInstanceSnapshotRequest(AbstractModel):
    """ApplyInstanceSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param SnapshotId: 快照 ID。
        :type SnapshotId: str
        """
        self.InstanceId = None
        self.SnapshotId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInstanceSnapshotResponse(AbstractModel):
    """ApplyInstanceSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyIds: 密钥对 ID 列表。每次请求批量密钥对的上限为 100。
        :type KeyIds: list of str
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self.KeyIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        self.InstanceIds = params.get("InstanceIds")
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


class AttachCcnRequest(AbstractModel):
    """AttachCcn请求参数结构体

    """

    def __init__(self):
        r"""
        :param CcnId: 云联网实例ID。
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnResponse(AbstractModel):
    """AttachCcn返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachDetail(AbstractModel):
    """挂载信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param AttachedDiskCount: 实例已挂载弹性云盘数量
        :type AttachedDiskCount: int
        :param MaxAttachCount: 可挂载弹性云盘数量
        :type MaxAttachCount: int
        """
        self.InstanceId = None
        self.AttachedDiskCount = None
        self.MaxAttachCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AttachedDiskCount = params.get("AttachedDiskCount")
        self.MaxAttachCount = params.get("MaxAttachCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksRequest(AbstractModel):
    """AttachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param RenewFlag: 续费标识。
        :type RenewFlag: str
        """
        self.DiskIds = None
        self.InstanceId = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.InstanceId = params.get("InstanceId")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksResponse(AbstractModel):
    """AttachDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Blueprint(AbstractModel):
    """描述了镜像信息。

    """

    def __init__(self):
        r"""
        :param BlueprintId: 镜像 ID  ，是 Blueprint 的唯一标识。
        :type BlueprintId: str
        :param DisplayTitle: 镜像对外展示标题。
        :type DisplayTitle: str
        :param DisplayVersion: 镜像对外展示版本。
        :type DisplayVersion: str
        :param Description: 镜像描述信息。
        :type Description: str
        :param OsName: 操作系统名称。
        :type OsName: str
        :param Platform: 操作系统平台。
        :type Platform: str
        :param PlatformType: 操作系统平台类型，如 LINUX_UNIX、WINDOWS。
        :type PlatformType: str
        :param BlueprintType: 镜像类型，如 APP_OS、PURE_OS、PRIVATE。
        :type BlueprintType: str
        :param ImageUrl: 镜像图片 URL。
        :type ImageUrl: str
        :param RequiredSystemDiskSize: 镜像所需系统盘大小，单位 GB。
        :type RequiredSystemDiskSize: int
        :param BlueprintState: 镜像状态。
        :type BlueprintState: str
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param BlueprintName: 镜像名称。
        :type BlueprintName: str
        :param SupportAutomationTools: 镜像是否支持自动化助手。
        :type SupportAutomationTools: bool
        :param RequiredMemorySize: 镜像所需内存大小, 单位: GB
        :type RequiredMemorySize: int
        :param ImageId: CVM镜像共享到轻量应用服务器轻量应用服务器后的CVM镜像ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        """
        self.BlueprintId = None
        self.DisplayTitle = None
        self.DisplayVersion = None
        self.Description = None
        self.OsName = None
        self.Platform = None
        self.PlatformType = None
        self.BlueprintType = None
        self.ImageUrl = None
        self.RequiredSystemDiskSize = None
        self.BlueprintState = None
        self.CreatedTime = None
        self.BlueprintName = None
        self.SupportAutomationTools = None
        self.RequiredMemorySize = None
        self.ImageId = None


    def _deserialize(self, params):
        self.BlueprintId = params.get("BlueprintId")
        self.DisplayTitle = params.get("DisplayTitle")
        self.DisplayVersion = params.get("DisplayVersion")
        self.Description = params.get("Description")
        self.OsName = params.get("OsName")
        self.Platform = params.get("Platform")
        self.PlatformType = params.get("PlatformType")
        self.BlueprintType = params.get("BlueprintType")
        self.ImageUrl = params.get("ImageUrl")
        self.RequiredSystemDiskSize = params.get("RequiredSystemDiskSize")
        self.BlueprintState = params.get("BlueprintState")
        self.CreatedTime = params.get("CreatedTime")
        self.BlueprintName = params.get("BlueprintName")
        self.SupportAutomationTools = params.get("SupportAutomationTools")
        self.RequiredMemorySize = params.get("RequiredMemorySize")
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlueprintInstance(AbstractModel):
    """描述镜像实例信息。

    """

    def __init__(self):
        r"""
        :param Blueprint: 镜像信息。
        :type Blueprint: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        :param SoftwareSet: 软件列表。
        :type SoftwareSet: list of Software
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self.Blueprint = None
        self.SoftwareSet = None
        self.InstanceId = None


    def _deserialize(self, params):
        if params.get("Blueprint") is not None:
            self.Blueprint = Blueprint()
            self.Blueprint._deserialize(params.get("Blueprint"))
        if params.get("SoftwareSet") is not None:
            self.SoftwareSet = []
            for item in params.get("SoftwareSet"):
                obj = Software()
                obj._deserialize(item)
                self.SoftwareSet.append(obj)
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlueprintPrice(AbstractModel):
    """BlueprintPrice	自定义镜像的价格参数。

    """

    def __init__(self):
        r"""
        :param OriginalBlueprintPrice: 镜像单价，原价。单位元。
        :type OriginalBlueprintPrice: float
        :param OriginalPrice: 镜像总价，原价。单位元。
        :type OriginalPrice: float
        :param Discount: 折扣。
        :type Discount: int
        :param DiscountPrice: 镜像折扣后总价。单位元。
        :type DiscountPrice: float
        """
        self.OriginalBlueprintPrice = None
        self.OriginalPrice = None
        self.Discount = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.OriginalBlueprintPrice = params.get("OriginalBlueprintPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        self.Discount = params.get("Discount")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bundle(AbstractModel):
    """套餐信息。

    """

    def __init__(self):
        r"""
        :param BundleId: 套餐 ID。
        :type BundleId: str
        :param Memory: 内存大小，单位 GB。
        :type Memory: int
        :param SystemDiskType: 系统盘类型。
取值范围： 
<li> LOCAL_BASIC：本地硬盘</li><li> LOCAL_SSD：本地 SSD 硬盘</li><li> CLOUD_BASIC：普通云硬盘</li><li> CLOUD_SSD：SSD 云硬盘</li><li> CLOUD_PREMIUM：高性能云硬盘</li>
        :type SystemDiskType: str
        :param SystemDiskSize: 系统盘大小。
        :type SystemDiskSize: int
        :param MonthlyTraffic: 每月网络流量，单位 Gb。
        :type MonthlyTraffic: int
        :param SupportLinuxUnixPlatform: 是否支持 Linux/Unix 平台。
        :type SupportLinuxUnixPlatform: bool
        :param SupportWindowsPlatform: 是否支持 Windows 平台。
        :type SupportWindowsPlatform: bool
        :param Price: 套餐当前单位价格信息。
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param CPU: CPU 核数。
        :type CPU: int
        :param InternetMaxBandwidthOut: 峰值带宽，单位 Mbps。
        :type InternetMaxBandwidthOut: int
        :param InternetChargeType: 网络计费类型。
        :type InternetChargeType: str
        :param BundleSalesState: 套餐售卖状态,取值:‘AVAILABLE’(可用) , ‘SOLD_OUT’(售罄)
        :type BundleSalesState: str
        :param BundleType: 套餐类型。
取值范围：
<li> GENERAL_BUNDLE：通用型</li><li> STORAGE_BUNDLE：存储型 </li>
        :type BundleType: str
        :param BundleDisplayLabel: 套餐展示标签.
取值范围:
"ACTIVITY": 活动套餐,
"NORMAL": 普通套餐
"CAREFREE": 无忧套餐
        :type BundleDisplayLabel: str
        """
        self.BundleId = None
        self.Memory = None
        self.SystemDiskType = None
        self.SystemDiskSize = None
        self.MonthlyTraffic = None
        self.SupportLinuxUnixPlatform = None
        self.SupportWindowsPlatform = None
        self.Price = None
        self.CPU = None
        self.InternetMaxBandwidthOut = None
        self.InternetChargeType = None
        self.BundleSalesState = None
        self.BundleType = None
        self.BundleDisplayLabel = None


    def _deserialize(self, params):
        self.BundleId = params.get("BundleId")
        self.Memory = params.get("Memory")
        self.SystemDiskType = params.get("SystemDiskType")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.MonthlyTraffic = params.get("MonthlyTraffic")
        self.SupportLinuxUnixPlatform = params.get("SupportLinuxUnixPlatform")
        self.SupportWindowsPlatform = params.get("SupportWindowsPlatform")
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.CPU = params.get("CPU")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InternetChargeType = params.get("InternetChargeType")
        self.BundleSalesState = params.get("BundleSalesState")
        self.BundleType = params.get("BundleType")
        self.BundleDisplayLabel = params.get("BundleDisplayLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnAttachedInstance(AbstractModel):
    """云联网关联的实例列表。

    """

    def __init__(self):
        r"""
        :param CcnId: 云联网ID。
        :type CcnId: str
        :param CidrBlock: 关联实例CIDR。
        :type CidrBlock: list of str
        :param State: 关联实例状态：

•  PENDING：申请中
•  ACTIVE：已连接
•  EXPIRED：已过期
•  REJECTED：已拒绝
•  DELETED：已删除
•  FAILED：失败的（2小时后将异步强制解关联）
•  ATTACHING：关联中
•  DETACHING：解关联中
•  DETACHFAILED：解关联失败（2小时后将异步强制解关联）
        :type State: str
        :param AttachedTime: 关联时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedTime: str
        :param Description: 备注
        :type Description: str
        """
        self.CcnId = None
        self.CidrBlock = None
        self.State = None
        self.AttachedTime = None
        self.Description = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CidrBlock = params.get("CidrBlock")
        self.State = params.get("State")
        self.AttachedTime = params.get("AttachedTime")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlueprintRequest(AbstractModel):
    """CreateBlueprint请求参数结构体

    """

    def __init__(self):
        r"""
        :param BlueprintName: 镜像名称。最大长度60。
        :type BlueprintName: str
        :param Description: 镜像描述。最大长度60。
        :type Description: str
        :param InstanceId: 需要制作镜像的实例ID。
        :type InstanceId: str
        """
        self.BlueprintName = None
        self.Description = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.BlueprintName = params.get("BlueprintName")
        self.Description = params.get("Description")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlueprintResponse(AbstractModel):
    """CreateBlueprint返回参数结构体

    """

    def __init__(self):
        r"""
        :param BlueprintId: 自定义镜像ID。
        :type BlueprintId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlueprintId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlueprintId = params.get("BlueprintId")
        self.RequestId = params.get("RequestId")


class CreateFirewallRulesRequest(AbstractModel):
    """CreateFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param FirewallRules: 防火墙规则列表。
        :type FirewallRules: list of FirewallRule
        :param FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self.InstanceId = None
        self.FirewallRules = None
        self.FirewallVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self.FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self.FirewallRules.append(obj)
        self.FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFirewallRulesResponse(AbstractModel):
    """CreateFirewallRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceSnapshotRequest(AbstractModel):
    """CreateInstanceSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 需要创建快照的实例 ID。
        :type InstanceId: str
        :param SnapshotName: 快照名称，最长为 60 个字符。
        :type SnapshotName: str
        """
        self.InstanceId = None
        self.SnapshotName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceSnapshotResponse(AbstractModel):
    """CreateInstanceSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照 ID。
        :type SnapshotId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过 25 个字符。
        :type KeyName: str
        """
        self.KeyName = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
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
        :type KeyPair: :class:`tencentcloud.lighthouse.v20200324.models.KeyPair`
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


class DataDiskPrice(AbstractModel):
    """数据盘价格

    """

    def __init__(self):
        r"""
        :param DiskId: 云硬盘ID。
        :type DiskId: str
        :param OriginalDiskPrice: 云硬盘单价。
        :type OriginalDiskPrice: float
        :param OriginalPrice: 云硬盘总价。
        :type OriginalPrice: float
        :param Discount: 折扣。
        :type Discount: float
        :param DiscountPrice: 折后总价。
        :type DiscountPrice: float
        """
        self.DiskId = None
        self.OriginalDiskPrice = None
        self.OriginalPrice = None
        self.Discount = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.OriginalDiskPrice = params.get("OriginalDiskPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        self.Discount = params.get("Discount")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlueprintsRequest(AbstractModel):
    """DeleteBlueprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param BlueprintIds: 镜像ID列表。镜像ID，可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintIds: list of str
        """
        self.BlueprintIds = None


    def _deserialize(self, params):
        self.BlueprintIds = params.get("BlueprintIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlueprintsResponse(AbstractModel):
    """DeleteBlueprints返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFirewallRulesRequest(AbstractModel):
    """DeleteFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param FirewallRules: 防火墙规则列表。
        :type FirewallRules: list of FirewallRule
        :param FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self.InstanceId = None
        self.FirewallRules = None
        self.FirewallVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self.FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self.FirewallRules.append(obj)
        self.FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFirewallRulesResponse(AbstractModel):
    """DeleteFirewallRules返回参数结构体

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
        :param KeyIds: 密钥对 ID 列表，每次请求批量密钥对的上限为 10。
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


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotIds: 要删除的快照 ID 列表，可通过 DescribeSnapshots 查询。
        :type SnapshotIds: list of str
        """
        self.SnapshotIds = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeniedAction(AbstractModel):
    """限制操作。

    """

    def __init__(self):
        r"""
        :param Action: 限制操作名。
        :type Action: str
        :param Code: 限制操作消息码。
        :type Code: str
        :param Message: 限制操作消息。
        :type Message: str
        """
        self.Action = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlueprintInstancesRequest(AbstractModel):
    """DescribeBlueprintInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表，当前最多支持 1 个。
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
        


class DescribeBlueprintInstancesResponse(AbstractModel):
    """DescribeBlueprintInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的镜像实例数量。
        :type TotalCount: int
        :param BlueprintInstanceSet: 镜像实例列表信息。
        :type BlueprintInstanceSet: list of BlueprintInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BlueprintInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BlueprintInstanceSet") is not None:
            self.BlueprintInstanceSet = []
            for item in params.get("BlueprintInstanceSet"):
                obj = BlueprintInstance()
                obj._deserialize(item)
                self.BlueprintInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlueprintsRequest(AbstractModel):
    """DescribeBlueprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param BlueprintIds: 镜像 ID 列表。
        :type BlueprintIds: list of str
        :param Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param Filters: 过滤器列表。
<li>blueprint-id</li>按照【镜像 ID】进行过滤。
类型：String
必选：否
<li>blueprint-type</li>按照【镜像类型】进行过滤。
取值：APP_OS（应用镜像 ）；PURE_OS（系统镜像）；PRIVATE（自定义镜像）；SHARED（共享镜像）。
类型：String
必选：否
<li>platform-type</li>按照【镜像平台类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）。
类型：String
必选：否
<li>blueprint-name</li>按照【镜像名称】进行过滤。
类型：String
必选：否
<li>blueprint-state</li>按照【镜像状态】进行过滤。
类型：String
必选：否

每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 BlueprintIds 和 Filters 。
        :type Filters: list of Filter
        """
        self.BlueprintIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.BlueprintIds = params.get("BlueprintIds")
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
        


class DescribeBlueprintsResponse(AbstractModel):
    """DescribeBlueprints返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的镜像数量。
        :type TotalCount: int
        :param BlueprintSet: 镜像详细信息列表。
        :type BlueprintSet: list of Blueprint
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BlueprintSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BlueprintSet") is not None:
            self.BlueprintSet = []
            for item in params.get("BlueprintSet"):
                obj = Blueprint()
                obj._deserialize(item)
                self.BlueprintSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBundleDiscountRequest(AbstractModel):
    """DescribeBundleDiscount请求参数结构体

    """

    def __init__(self):
        r"""
        :param BundleId: 套餐 ID。
        :type BundleId: str
        """
        self.BundleId = None


    def _deserialize(self, params):
        self.BundleId = params.get("BundleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBundleDiscountResponse(AbstractModel):
    """DescribeBundleDiscount返回参数结构体

    """

    def __init__(self):
        r"""
        :param Currency: 币种：CNY人民币，USD 美元。
        :type Currency: str
        :param DiscountDetail: 折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :type DiscountDetail: list of DiscountDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Currency = None
        self.DiscountDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        if params.get("DiscountDetail") is not None:
            self.DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self.DiscountDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBundlesRequest(AbstractModel):
    """DescribeBundles请求参数结构体

    """

    def __init__(self):
        r"""
        :param BundleIds: 套餐 ID 列表。
        :type BundleIds: list of str
        :param Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param Filters: 过滤器列表。
<li>bundle-id</li>按照【套餐 ID】进行过滤。
类型：String
必选：否
<li>support-platform-type</li>按照【系统类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 BundleIds 和 Filters。
        :type Filters: list of Filter
        :param Zones: 可用区列表。默认为全部可用区。
        :type Zones: list of str
        """
        self.BundleIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Zones = None


    def _deserialize(self, params):
        self.BundleIds = params.get("BundleIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBundlesResponse(AbstractModel):
    """DescribeBundles返回参数结构体

    """

    def __init__(self):
        r"""
        :param BundleSet: 套餐详细信息列表。
        :type BundleSet: list of Bundle
        :param TotalCount: 符合要求的套餐总数，用于分页展示。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BundleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BundleSet") is not None:
            self.BundleSet = []
            for item in params.get("BundleSet"):
                obj = Bundle()
                obj._deserialize(item)
                self.BundleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCcnAttachedInstancesRequest(AbstractModel):
    """DescribeCcnAttachedInstances请求参数结构体

    """


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    """DescribeCcnAttachedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param CcnAttachedInstanceSet: 云联网关联的实例列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnAttachedInstanceSet: list of CcnAttachedInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CcnAttachedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CcnAttachedInstanceSet") is not None:
            self.CcnAttachedInstanceSet = []
            for item in params.get("CcnAttachedInstanceSet"):
                obj = CcnAttachedInstance()
                obj._deserialize(item)
                self.CcnAttachedInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskConfigsRequest(AbstractModel):
    """DescribeDiskConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤器列表。
<li>zone</li>按照【可用区】进行过滤。
类型：String
必选：否
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
        


class DescribeDiskConfigsResponse(AbstractModel):
    """DescribeDiskConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param DiskConfigSet: 云硬盘配置列表。
        :type DiskConfigSet: list of DiskConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self.DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self.DiskConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskDiscountRequest(AbstractModel):
    """DescribeDiskDiscount请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskType: 云硬盘类型, 取值: "CLOUD_PREMIUM"。
        :type DiskType: str
        :param DiskSize: 云硬盘大小。
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiskDiscountResponse(AbstractModel):
    """DescribeDiskDiscount返回参数结构体

    """

    def __init__(self):
        r"""
        :param Currency: 币种：CNY人民币，USD 美元。
        :type Currency: str
        :param DiscountDetail: 折扣梯度详情，每个梯度包含的信息有：时长，折扣数，总价，折扣价，折扣详情（用户折扣、官网折扣、最终折扣）。
        :type DiscountDetail: list of DiscountDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Currency = None
        self.DiscountDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        if params.get("DiscountDetail") is not None:
            self.DiscountDetail = []
            for item in params.get("DiscountDetail"):
                obj = DiscountDetail()
                obj._deserialize(item)
                self.DiscountDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDisksDeniedActionsRequest(AbstractModel):
    """DescribeDisksDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        """
        self.DiskIds = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksDeniedActionsResponse(AbstractModel):
    """DescribeDisksDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param DiskDeniedActionSet: 云硬盘操作限制列表详细信息。
        :type DiskDeniedActionSet: list of DiskDeniedActions
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskDeniedActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskDeniedActionSet") is not None:
            self.DiskDeniedActionSet = []
            for item in params.get("DiskDeniedActionSet"):
                obj = DiskDeniedActions()
                obj._deserialize(item)
                self.DiskDeniedActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        :param Filters: 过滤器列表。
disk-id
按照【云硬盘 ID】进行过滤。
类型：String
必选：否
instance-id
按照【实例ID】进行过滤。
类型：String
必选：否
disk-name
按照【云硬盘名称】进行过滤。
类型：String
必选：否
zone
按照【可用区】进行过滤。
类型：String
必选：否
disk-usage
按照【云硬盘类型】进行过滤。
类型：String
必选：否
disk-state
按照【云硬盘状态】进行过滤。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 DiskIds 和 Filters。
        :type Filters: list of Filter
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param OrderField: 云硬盘列表排序的依据字段。取值范围："CREATED_TIME"：依据云硬盘的创建时间排序。 "EXPIRED_TIME"：依据云硬盘的到期时间排序。"DISK_SIZE"：依据云硬盘的大小排序。默认按云硬盘创建时间排序。
        :type OrderField: str
        :param Order: 输出云硬盘列表的排列顺序。取值范围："ASC"：升序排列。 "DESC"：降序排列。默认按降序排列。
        :type Order: str
        """
        self.DiskIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param DiskSet: 云硬盘信息列表。
        :type DiskSet: list of Disk
        :param TotalCount: 符合条件的云硬盘信息数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskSet") is not None:
            self.DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self.DiskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDisksReturnableRequest(AbstractModel):
    """DescribeDisksReturnable请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.DiskIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksReturnableResponse(AbstractModel):
    """DescribeDisksReturnable返回参数结构体

    """

    def __init__(self):
        r"""
        :param DiskReturnableSet: 可退还云硬盘详细信息列表。
        :type DiskReturnableSet: list of DiskReturnable
        :param TotalCount: 符合条件的云硬盘数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskReturnableSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskReturnableSet") is not None:
            self.DiskReturnableSet = []
            for item in params.get("DiskReturnableSet"):
                obj = DiskReturnable()
                obj._deserialize(item)
                self.DiskReturnableSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFirewallRulesRequest(AbstractModel):
    """DescribeFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirewallRulesResponse(AbstractModel):
    """DescribeFirewallRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的防火墙规则数量。
        :type TotalCount: int
        :param FirewallRuleSet: 防火墙规则详细信息列表。
        :type FirewallRuleSet: list of FirewallRuleInfo
        :param FirewallVersion: 防火墙版本号。
        :type FirewallVersion: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.FirewallRuleSet = None
        self.FirewallVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("FirewallRuleSet") is not None:
            self.FirewallRuleSet = []
            for item in params.get("FirewallRuleSet"):
                obj = FirewallRuleInfo()
                obj._deserialize(item)
                self.FirewallRuleSet.append(obj)
        self.FirewallVersion = params.get("FirewallVersion")
        self.RequestId = params.get("RequestId")


class DescribeFirewallRulesTemplateRequest(AbstractModel):
    """DescribeFirewallRulesTemplate请求参数结构体

    """


class DescribeFirewallRulesTemplateResponse(AbstractModel):
    """DescribeFirewallRulesTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的防火墙规则数量。
        :type TotalCount: int
        :param FirewallRuleSet: 防火墙规则详细信息列表。
        :type FirewallRuleSet: list of FirewallRuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.FirewallRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("FirewallRuleSet") is not None:
            self.FirewallRuleSet = []
            for item in params.get("FirewallRuleSet"):
                obj = FirewallRuleInfo()
                obj._deserialize(item)
                self.FirewallRuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGeneralResourceQuotasRequest(AbstractModel):
    """DescribeGeneralResourceQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceNames: 资源名列表，取值为：USER_KEY_PAIR、INSTANCE、SNAPSHOT。
        :type ResourceNames: list of str
        """
        self.ResourceNames = None


    def _deserialize(self, params):
        self.ResourceNames = params.get("ResourceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralResourceQuotasResponse(AbstractModel):
    """DescribeGeneralResourceQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param GeneralResourceQuotaSet: 通用资源配额详细信息列表。
        :type GeneralResourceQuotaSet: list of GeneralResourceQuota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GeneralResourceQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GeneralResourceQuotaSet") is not None:
            self.GeneralResourceQuotaSet = []
            for item in params.get("GeneralResourceQuotaSet"):
                obj = GeneralResourceQuota()
                obj._deserialize(item)
                self.GeneralResourceQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceLoginKeyPairAttributeRequest(AbstractModel):
    """DescribeInstanceLoginKeyPairAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
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
        


class DescribeInstanceLoginKeyPairAttributeResponse(AbstractModel):
    """DescribeInstanceLoginKeyPairAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param PermitLogin: 是否允许使用默认密钥对登录，YES：允许登录 NO：禁止登录。
        :type PermitLogin: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PermitLogin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PermitLogin = params.get("PermitLogin")
        self.RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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
        


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceDeniedActionSet: 实例操作限制列表详细信息。
        :type InstanceDeniedActionSet: list of InstanceDeniedActions
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceDeniedActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceDeniedActionSet") is not None:
            self.InstanceDeniedActionSet = []
            for item in params.get("InstanceDeniedActionSet"):
                obj = InstanceDeniedActions()
                obj._deserialize(item)
                self.InstanceDeniedActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    """DescribeInstancesDiskNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例ID列表。
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
        


class DescribeInstancesDiskNumResponse(AbstractModel):
    """DescribeInstancesDiskNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param AttachDetailSet: 挂载信息列表
        :type AttachDetailSet: list of AttachDetail
        :param TotalCount: 挂载信息数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AttachDetailSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttachDetailSet") is not None:
            self.AttachDetailSet = []
            for item in params.get("AttachDetailSet"):
                obj = AttachDetail()
                obj._deserialize(item)
                self.AttachDetailSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。
        :type InstanceIds: list of str
        :param Filters: 过滤器列表。
<li>instance-name</li>按照【实例名称】进行过滤。
类型：String
必选：否
<li>private-ip-address</li>按照【实例主网卡的内网 IP】进行过滤。
类型：String
必选：否
<li>public-ip-address</li>按照【实例主网卡的公网 IP】进行过滤。
类型：String
必选：否
<li>zone</li>按照【可用区】进行过滤。
类型：String
必选：否
<li>instance-state</li>按照【实例状态】进行过滤。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 InstanceIds 和 Filters。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
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


class DescribeInstancesReturnableRequest(AbstractModel):
    """DescribeInstancesReturnable请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。
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
        


class DescribeInstancesReturnableResponse(AbstractModel):
    """DescribeInstancesReturnable返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param InstanceReturnableSet: 可退还实例详细信息列表。
        :type InstanceReturnableSet: list of InstanceReturnable
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceReturnableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceReturnableSet") is not None:
            self.InstanceReturnableSet = []
            for item in params.get("InstanceReturnableSet"):
                obj = InstanceReturnable()
                obj._deserialize(item)
                self.InstanceReturnableSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesTrafficPackagesRequest(AbstractModel):
    """DescribeInstancesTrafficPackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。
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
        


class DescribeInstancesTrafficPackagesResponse(AbstractModel):
    """DescribeInstancesTrafficPackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的实例流量包详情数量。
        :type TotalCount: int
        :param InstanceTrafficPackageSet: 实例流量包详情列表。
        :type InstanceTrafficPackageSet: list of InstanceTrafficPackage
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceTrafficPackageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceTrafficPackageSet") is not None:
            self.InstanceTrafficPackageSet = []
            for item in params.get("InstanceTrafficPackageSet"):
                obj = InstanceTrafficPackage()
                obj._deserialize(item)
                self.InstanceTrafficPackageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyIds: 密钥对 ID 列表。
        :type KeyIds: list of str
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Filters: 过滤器列表。
<li>key-id</li>按照【密钥对ID】进行过滤。
类型：String
必选：否
<li>key-name</li>按照【密钥对名称】进行过滤。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 KeyIds 和 Filters。
        :type Filters: list of Filter
        """
        self.KeyIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
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


class DescribeModifyInstanceBundlesRequest(AbstractModel):
    """DescribeModifyInstanceBundles请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Filters: 过滤器列表。
<li>bundle-id</li>按照【套餐 ID】进行过滤。
类型：String
必选：否
<li>support-platform-type</li>按照【系统类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        """
        self.InstanceId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        


class DescribeModifyInstanceBundlesResponse(AbstractModel):
    """DescribeModifyInstanceBundles返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的套餐数量。
        :type TotalCount: int
        :param ModifyBundleSet: 变更套餐详细信息。
        :type ModifyBundleSet: list of ModifyBundle
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ModifyBundleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ModifyBundleSet") is not None:
            self.ModifyBundleSet = []
            for item in params.get("ModifyBundleSet"):
                obj = ModifyBundle()
                obj._deserialize(item)
                self.ModifyBundleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 地域数量。
        :type TotalCount: int
        :param RegionSet: 地域信息列表。
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


class DescribeResetInstanceBlueprintsRequest(AbstractModel):
    """DescribeResetInstanceBlueprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param Filters: 过滤器列表。
<li>blueprint-id</li>按照【镜像 ID】进行过滤。
类型：String
必选：否
<li>blueprint-type</li>按照【镜像类型】进行过滤。
取值： APP_OS（应用镜像 ）；PURE_OS（ 系统镜像）；PRIVATE（自定义镜像）。
类型：String
必选：否
<li>platform-type</li>按照【镜像平台类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）。
类型：String
必选：否
<li>blueprint-name</li>按照【镜像名称】进行过滤。
类型：String
必选：否
<li>blueprint-state</li>按照【镜像状态】进行过滤。
类型：String
必选：否

每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 BlueprintIds 和 Filters 。
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        


class DescribeResetInstanceBlueprintsResponse(AbstractModel):
    """DescribeResetInstanceBlueprints返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的镜像数量。
        :type TotalCount: int
        :param ResetInstanceBlueprintSet: 镜像重置信息列表
        :type ResetInstanceBlueprintSet: list of ResetInstanceBlueprint
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ResetInstanceBlueprintSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResetInstanceBlueprintSet") is not None:
            self.ResetInstanceBlueprintSet = []
            for item in params.get("ResetInstanceBlueprintSet"):
                obj = ResetInstanceBlueprint()
                obj._deserialize(item)
                self.ResetInstanceBlueprintSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsDeniedActionsRequest(AbstractModel):
    """DescribeSnapshotsDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotIds: 快照 ID 列表, 可通过 DescribeSnapshots 查询。
        :type SnapshotIds: list of str
        """
        self.SnapshotIds = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsDeniedActionsResponse(AbstractModel):
    """DescribeSnapshotsDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotDeniedActionSet: 快照操作限制列表详细信息。
        :type SnapshotDeniedActionSet: list of SnapshotDeniedActions
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotDeniedActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SnapshotDeniedActionSet") is not None:
            self.SnapshotDeniedActionSet = []
            for item in params.get("SnapshotDeniedActionSet"):
                obj = SnapshotDeniedActions()
                obj._deserialize(item)
                self.SnapshotDeniedActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotIds: 要查询快照的 ID 列表。
参数不支持同时指定 SnapshotIds 和 Filters。
        :type SnapshotIds: list of str
        :param Filters: 过滤器列表。
<li>snapshot-id</li>按照【快照 ID】进行过滤。
类型：String
必选：否
<li>disk-id</li>按照【磁盘 ID】进行过滤。
类型：String
必选：否
<li>snapshot-name</li>按照【快照名称】进行过滤。
类型：String
必选：否
<li>instance-id</li>按照【实例 ID 】进行过滤。
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 SnapshotIds 和 Filters。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self.SnapshotIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
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
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 快照的数量。
        :type TotalCount: int
        :param SnapshotSet: 快照的详情列表。
        :type SnapshotSet: list of Snapshot
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotSet") is not None:
            self.SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self.SnapshotSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 可用区数量
        :type TotalCount: int
        :param ZoneInfoSet: 可用区详细信息列表
        :type ZoneInfoSet: list of ZoneInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneInfoSet") is not None:
            self.ZoneInfoSet = []
            for item in params.get("ZoneInfoSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachCcnRequest(AbstractModel):
    """DetachCcn请求参数结构体

    """

    def __init__(self):
        r"""
        :param CcnId: 云联网实例ID。
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnResponse(AbstractModel):
    """DetachCcn返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachDisksRequest(AbstractModel):
    """DetachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        """
        self.DiskIds = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachDisksResponse(AbstractModel):
    """DetachDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyIds: 密钥对 ID 列表。每次请求批量密钥对的上限为 100。
        :type KeyIds: list of str
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self.KeyIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        self.InstanceIds = params.get("InstanceIds")
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


class DiscountDetail(AbstractModel):
    """套餐折扣详情（仅用于控制台调用询价相关接口返回）。

    """

    def __init__(self):
        r"""
        :param TimeSpan: 计费时长。
        :type TimeSpan: int
        :param TimeUnit: 计费单元。
        :type TimeUnit: str
        :param TotalCost: 总价。
        :type TotalCost: float
        :param RealTotalCost: 折后总价。
        :type RealTotalCost: float
        :param Discount: 折扣。
        :type Discount: int
        :param PolicyDetail: 具体折扣详情。
        :type PolicyDetail: :class:`tencentcloud.lighthouse.v20200324.models.PolicyDetail`
        """
        self.TimeSpan = None
        self.TimeUnit = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.Discount = None
        self.PolicyDetail = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.Discount = params.get("Discount")
        if params.get("PolicyDetail") is not None:
            self.PolicyDetail = PolicyDetail()
            self.PolicyDetail._deserialize(params.get("PolicyDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Disk(AbstractModel):
    """磁盘信息

    """

    def __init__(self):
        r"""
        :param DiskId: 磁盘ID
        :type DiskId: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Zone: 可用区
        :type Zone: str
        :param DiskName: 磁盘名称
        :type DiskName: str
        :param DiskUsage: 磁盘类型
        :type DiskUsage: str
        :param DiskType: 磁盘介质类型
        :type DiskType: str
        :param DiskChargeType: 磁盘付费类型
        :type DiskChargeType: str
        :param DiskSize: 磁盘大小
        :type DiskSize: int
        :param RenewFlag: 续费标识
        :type RenewFlag: str
        :param DiskState: 磁盘状态
        :type DiskState: str
        :param Attached: 磁盘挂载状态
        :type Attached: bool
        :param DeleteWithInstance: 是否随实例释放
        :type DeleteWithInstance: bool
        :param LatestOperation: 上一次操作
        :type LatestOperation: str
        :param LatestOperationState: 上一次操作状态
        :type LatestOperationState: str
        :param LatestOperationRequestId: 上一次请求ID
        :type LatestOperationRequestId: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param ExpiredTime: 到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param IsolatedTime: 隔离时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        """
        self.DiskId = None
        self.InstanceId = None
        self.Zone = None
        self.DiskName = None
        self.DiskUsage = None
        self.DiskType = None
        self.DiskChargeType = None
        self.DiskSize = None
        self.RenewFlag = None
        self.DiskState = None
        self.Attached = None
        self.DeleteWithInstance = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.LatestOperationRequestId = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.IsolatedTime = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.InstanceId = params.get("InstanceId")
        self.Zone = params.get("Zone")
        self.DiskName = params.get("DiskName")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskType = params.get("DiskType")
        self.DiskChargeType = params.get("DiskChargeType")
        self.DiskSize = params.get("DiskSize")
        self.RenewFlag = params.get("RenewFlag")
        self.DiskState = params.get("DiskState")
        self.Attached = params.get("Attached")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.LatestOperationRequestId = params.get("LatestOperationRequestId")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.IsolatedTime = params.get("IsolatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskChargePrepaid(AbstractModel):
    """云硬盘包年包月相关参数设置

    """

    def __init__(self):
        r"""
        :param Period: 新购周期。
        :type Period: int
        :param RenewFlag: 续费标识。
        :type RenewFlag: str
        :param TimeUnit: 新购单位. 默认值: "m"。
        :type TimeUnit: str
        """
        self.Period = None
        self.RenewFlag = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        self.TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskConfig(AbstractModel):
    """云硬盘配置

    """

    def __init__(self):
        r"""
        :param Zone: 可用区。
        :type Zone: str
        :param DiskType: 云硬盘类型。
        :type DiskType: str
        :param DiskSalesState: 云硬盘可售卖状态。
        :type DiskSalesState: str
        :param MaxDiskSize: 最大云硬盘大小。
        :type MaxDiskSize: int
        :param MinDiskSize: 最小云硬盘大小。
        :type MinDiskSize: int
        :param DiskStepSize: 云硬盘步长。
        :type DiskStepSize: int
        """
        self.Zone = None
        self.DiskType = None
        self.DiskSalesState = None
        self.MaxDiskSize = None
        self.MinDiskSize = None
        self.DiskStepSize = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DiskType = params.get("DiskType")
        self.DiskSalesState = params.get("DiskSalesState")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.MinDiskSize = params.get("MinDiskSize")
        self.DiskStepSize = params.get("DiskStepSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskDeniedActions(AbstractModel):
    """磁盘操作限制列表详细信息

    """

    def __init__(self):
        r"""
        :param DiskId: 云硬盘ID。
        :type DiskId: str
        :param DeniedActions: 操作限制列表。
        :type DeniedActions: list of DeniedAction
        """
        self.DiskId = None
        self.DeniedActions = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        if params.get("DeniedActions") is not None:
            self.DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self.DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskPrice(AbstractModel):
    """云硬盘价格

    """

    def __init__(self):
        r"""
        :param OriginalDiskPrice: 云硬盘单价。
        :type OriginalDiskPrice: float
        :param OriginalPrice: 云硬盘总价。
        :type OriginalPrice: float
        :param Discount: 折扣。
        :type Discount: float
        :param DiscountPrice: 折后总价。
        :type DiscountPrice: float
        """
        self.OriginalDiskPrice = None
        self.OriginalPrice = None
        self.Discount = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.OriginalDiskPrice = params.get("OriginalDiskPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        self.Discount = params.get("Discount")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskReturnable(AbstractModel):
    """可退还云硬盘详细信息

    """

    def __init__(self):
        r"""
        :param DiskId: 云硬盘ID。
        :type DiskId: str
        :param IsReturnable: 云硬盘是否可退还。
        :type IsReturnable: bool
        :param ReturnFailCode: 云硬盘退还失败错误码。
        :type ReturnFailCode: int
        :param ReturnFailMessage: 云硬盘退还失败错误信息。
        :type ReturnFailMessage: str
        """
        self.DiskId = None
        self.IsReturnable = None
        self.ReturnFailCode = None
        self.ReturnFailMessage = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.IsReturnable = params.get("IsReturnable")
        self.ReturnFailCode = params.get("ReturnFailCode")
        self.ReturnFailMessage = params.get("ReturnFailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤名称等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以DescribeInstances接口的`Filter`为例。若我们需要查询实例名称（`instance-name`）为test ***并且*** 实例内网IP（`private-ip-address`）为10.10.10.10的实例时，可如下实现：
    ```
    Filters.0.Name=instance-name
    &Filters.0.Values.0=test
    &Filters.1.Name=private-ip-address
    &Filters.1.Values.0=10.10.10.10
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
        


class FirewallRule(AbstractModel):
    """描述防火墙规则信息。

    """

    def __init__(self):
        r"""
        :param Protocol: 协议，取值：TCP，UDP，ICMP，ALL。
        :type Protocol: str
        :param Port: 端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。
        :type Port: str
        :param CidrBlock: 网段或 IP (互斥)。默认为 0.0.0.0/0，表示所有来源。
        :type CidrBlock: str
        :param Action: 取值：ACCEPT，DROP。默认为 ACCEPT。
        :type Action: str
        :param FirewallRuleDescription: 防火墙规则描述。
        :type FirewallRuleDescription: str
        """
        self.Protocol = None
        self.Port = None
        self.CidrBlock = None
        self.Action = None
        self.FirewallRuleDescription = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.CidrBlock = params.get("CidrBlock")
        self.Action = params.get("Action")
        self.FirewallRuleDescription = params.get("FirewallRuleDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirewallRuleInfo(AbstractModel):
    """描述防火墙规则详细信息。

    """

    def __init__(self):
        r"""
        :param AppType: 应用类型，取值：自定义，HTTP(80)，HTTPS(443)，Linux登录(22)，Windows登录(3389)，MySQL(3306)，SQL Server(1433)，全部TCP，全部UDP，Ping-ICMP，ALL。
        :type AppType: str
        :param Protocol: 协议，取值：TCP，UDP，ICMP，ALL。
        :type Protocol: str
        :param Port: 端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。
        :type Port: str
        :param CidrBlock: 网段或 IP (互斥)。默认为 0.0.0.0/0，表示所有来源。
        :type CidrBlock: str
        :param Action: 取值：ACCEPT，DROP。默认为 ACCEPT。
        :type Action: str
        :param FirewallRuleDescription: 防火墙规则描述。
        :type FirewallRuleDescription: str
        """
        self.AppType = None
        self.Protocol = None
        self.Port = None
        self.CidrBlock = None
        self.Action = None
        self.FirewallRuleDescription = None


    def _deserialize(self, params):
        self.AppType = params.get("AppType")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.CidrBlock = params.get("CidrBlock")
        self.Action = params.get("Action")
        self.FirewallRuleDescription = params.get("FirewallRuleDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralResourceQuota(AbstractModel):
    """描述通用资源配额信息。


    """

    def __init__(self):
        r"""
        :param ResourceName: 资源名称。
        :type ResourceName: str
        :param ResourceQuotaAvailable: 资源当前可用数量。
        :type ResourceQuotaAvailable: int
        :param ResourceQuotaTotal: 资源总数量。
        :type ResourceQuotaTotal: int
        """
        self.ResourceName = None
        self.ResourceQuotaAvailable = None
        self.ResourceQuotaTotal = None


    def _deserialize(self, params):
        self.ResourceName = params.get("ResourceName")
        self.ResourceQuotaAvailable = params.get("ResourceQuotaAvailable")
        self.ResourceQuotaTotal = params.get("ResourceQuotaTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过 25 个字符。
        :type KeyName: str
        :param PublicKey: 密钥对的公钥内容， OpenSSH RSA 格式。
        :type PublicKey: str
        """
        self.KeyName = None
        self.PublicKey = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.PublicKey = params.get("PublicKey")
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
        :param KeyId: 密钥对 ID。
        :type KeyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class InquirePriceCreateBlueprintRequest(AbstractModel):
    """InquirePriceCreateBlueprint请求参数结构体

    """

    def __init__(self):
        r"""
        :param BlueprintCount: 自定义镜像的个数。默认值为1。
        :type BlueprintCount: int
        """
        self.BlueprintCount = None


    def _deserialize(self, params):
        self.BlueprintCount = params.get("BlueprintCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateBlueprintResponse(AbstractModel):
    """InquirePriceCreateBlueprint返回参数结构体

    """

    def __init__(self):
        r"""
        :param BlueprintPrice: 自定义镜像的价格参数。
        :type BlueprintPrice: :class:`tencentcloud.lighthouse.v20200324.models.BlueprintPrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlueprintPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BlueprintPrice") is not None:
            self.BlueprintPrice = BlueprintPrice()
            self.BlueprintPrice._deserialize(params.get("BlueprintPrice"))
        self.RequestId = params.get("RequestId")


class InquirePriceCreateDisksRequest(AbstractModel):
    """InquirePriceCreateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskSize: 云硬盘大小, 单位: GB。
        :type DiskSize: int
        :param DiskType: 云硬盘介质类型。取值: "CLOUD_PREMIUM"(高性能云盘), "CLOUD_SSD"(SSD云硬盘)。
        :type DiskType: str
        :param DiskChargePrepaid: 新购云硬盘包年包月相关参数设置。
        :type DiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.DiskChargePrepaid`
        :param DiskCount: 云硬盘个数, 默认值: 1。
        :type DiskCount: int
        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskChargePrepaid = None
        self.DiskCount = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDisksResponse(AbstractModel):
    """InquirePriceCreateDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param DiskPrice: 云硬盘价格。
        :type DiskPrice: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = DiskPrice()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquirePriceCreateInstancesRequest(AbstractModel):
    """InquirePriceCreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param BundleId: 实例的套餐 ID。
        :type BundleId: str
        :param InstanceCount: 创建数量，默认为 1。
        :type InstanceCount: int
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param BlueprintId: 应用镜像 ID，使用收费应用镜像时必填。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintId: str
        """
        self.BundleId = None
        self.InstanceCount = None
        self.InstanceChargePrepaid = None
        self.BlueprintId = None


    def _deserialize(self, params):
        self.BundleId = params.get("BundleId")
        self.InstanceCount = params.get("InstanceCount")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.BlueprintId = params.get("BlueprintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateInstancesResponse(AbstractModel):
    """InquirePriceCreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 询价信息。
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
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


class InquirePriceRenewDisksRequest(AbstractModel):
    """InquirePriceRenewDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        :param RenewDiskChargePrepaid: 续费云硬盘包年包月相关参数设置。
        :type RenewDiskChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.RenewDiskChargePrepaid`
        """
        self.DiskIds = None
        self.RenewDiskChargePrepaid = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        if params.get("RenewDiskChargePrepaid") is not None:
            self.RenewDiskChargePrepaid = RenewDiskChargePrepaid()
            self.RenewDiskChargePrepaid._deserialize(params.get("RenewDiskChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewDisksResponse(AbstractModel):
    """InquirePriceRenewDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param DiskPrice: 云硬盘价格。
        :type DiskPrice: :class:`tencentcloud.lighthouse.v20200324.models.DiskPrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = DiskPrice()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquirePriceRenewInstancesRequest(AbstractModel):
    """InquirePriceRenewInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 待续费的实例。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.lighthouse.v20200324.models.InstanceChargePrepaid`
        :param RenewDataDisk: 是否续费数据盘
        :type RenewDataDisk: bool
        :param AlignInstanceExpiredTime: 数据盘是否对齐实例到期时间
        :type AlignInstanceExpiredTime: bool
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None
        self.RenewDataDisk = None
        self.AlignInstanceExpiredTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.RenewDataDisk = params.get("RenewDataDisk")
        self.AlignInstanceExpiredTime = params.get("AlignInstanceExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewInstancesResponse(AbstractModel):
    """InquirePriceRenewInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 询价信息。
        :type Price: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param DataDiskPriceSet: 数据盘价格信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDiskPriceSet: list of DataDiskPrice
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.DataDiskPriceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        if params.get("DataDiskPriceSet") is not None:
            self.DataDiskPriceSet = []
            for item in params.get("DataDiskPriceSet"):
                obj = DataDiskPrice()
                obj._deserialize(item)
                self.DataDiskPriceSet.append(obj)
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """描述了实例信息。

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param BundleId: 套餐 ID。
        :type BundleId: str
        :param BlueprintId: 镜像 ID。
        :type BlueprintId: str
        :param CPU: 实例的 CPU 核数，单位：核。
        :type CPU: int
        :param Memory: 实例内存容量，单位：GB 。
        :type Memory: int
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param InstanceChargeType: 实例计费模式。取值范围： 
PREPAID：表示预付费，即包年包月。
        :type InstanceChargeType: str
        :param SystemDisk: 实例系统盘信息。
        :type SystemDisk: :class:`tencentcloud.lighthouse.v20200324.models.SystemDisk`
        :param PrivateAddresses: 实例主网卡的内网 IP。 
注意：此字段可能返回 空，表示取不到有效值。
        :type PrivateAddresses: list of str
        :param PublicAddresses: 实例主网卡的公网 IP。 
注意：此字段可能返回 空，表示取不到有效值。
        :type PublicAddresses: list of str
        :param InternetAccessible: 实例带宽信息。
        :type InternetAccessible: :class:`tencentcloud.lighthouse.v20200324.models.InternetAccessible`
        :param RenewFlag: 自动续费标识。取值范围： 
NOTIFY_AND_MANUAL_RENEW：表示通知即将过期，但不自动续费  
NOTIFY_AND_AUTO_RENEW：表示通知即将过期，而且自动续费 。
        :type RenewFlag: str
        :param LoginSettings: 实例登录设置。
        :type LoginSettings: :class:`tencentcloud.lighthouse.v20200324.models.LoginSettings`
        :param InstanceState: 实例状态。取值范围： 
<li>PENDING：表示创建中</li><li>LAUNCH_FAILED：表示创建失败</li><li>RUNNING：表示运行中</li><li>STOPPED：表示关机</li><li>STARTING：表示开机中</li><li>STOPPING：表示关机中</li><li>REBOOTING：表示重启中</li><li>SHUTDOWN：表示停止待销毁</li><li>TERMINATING：表示销毁中</li>
        :type InstanceState: str
        :param Uuid: 实例全局唯一 ID。
        :type Uuid: str
        :param LatestOperation: 实例的最新操作。例：StopInstances、ResetInstance。注意：此字段可能返回 空值，表示取不到有效值。
        :type LatestOperation: str
        :param LatestOperationState: 实例的最新操作状态。取值范围： 
SUCCESS：表示操作成功 
OPERATING：表示操作执行中 
FAILED：表示操作失败 
注意：此字段可能返回 空值，表示取不到有效值。
        :type LatestOperationState: str
        :param LatestOperationRequestId: 实例最新操作的唯一请求 ID。 
注意：此字段可能返回 空值，表示取不到有效值。
        :type LatestOperationRequestId: str
        :param IsolatedTime: 隔离时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ExpiredTime: 到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ 。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param PlatformType: 操作系统平台类型，如 LINUX_UNIX、WINDOWS。
        :type PlatformType: str
        :param Platform: 操作系统平台。
        :type Platform: str
        :param OsName: 操作系统名称。
        :type OsName: str
        :param Zone: 可用区。
        :type Zone: str
        """
        self.InstanceId = None
        self.BundleId = None
        self.BlueprintId = None
        self.CPU = None
        self.Memory = None
        self.InstanceName = None
        self.InstanceChargeType = None
        self.SystemDisk = None
        self.PrivateAddresses = None
        self.PublicAddresses = None
        self.InternetAccessible = None
        self.RenewFlag = None
        self.LoginSettings = None
        self.InstanceState = None
        self.Uuid = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.LatestOperationRequestId = None
        self.IsolatedTime = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.PlatformType = None
        self.Platform = None
        self.OsName = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BundleId = params.get("BundleId")
        self.BlueprintId = params.get("BlueprintId")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.InstanceName = params.get("InstanceName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        self.PrivateAddresses = params.get("PrivateAddresses")
        self.PublicAddresses = params.get("PublicAddresses")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.RenewFlag = params.get("RenewFlag")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.InstanceState = params.get("InstanceState")
        self.Uuid = params.get("Uuid")
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.LatestOperationRequestId = params.get("LatestOperationRequestId")
        self.IsolatedTime = params.get("IsolatedTime")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.PlatformType = params.get("PlatformType")
        self.Platform = params.get("Platform")
        self.OsName = params.get("OsName")
        self.Zone = params.get("Zone")
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
        :param RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费，用户需要手动续费<br><li>DISABLE_NOTIFY_AND_AUTO_RENEW：不自动续费，且不通知<br><br>默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
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
        


class InstanceDeniedActions(AbstractModel):
    """实例操作限制列表。

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param DeniedActions: 操作限制列表。
        :type DeniedActions: list of DeniedAction
        """
        self.InstanceId = None
        self.DeniedActions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self.DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self.DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePrice(AbstractModel):
    """关于Lighthouse Instance实例的价格信息

    """

    def __init__(self):
        r"""
        :param OriginalBundlePrice: 套餐单价原价。
        :type OriginalBundlePrice: float
        :param OriginalPrice: 原价。
        :type OriginalPrice: float
        :param Discount: 折扣。
        :type Discount: int
        :param DiscountPrice: 折后价。
        :type DiscountPrice: float
        """
        self.OriginalBundlePrice = None
        self.OriginalPrice = None
        self.Discount = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.OriginalBundlePrice = params.get("OriginalBundlePrice")
        self.OriginalPrice = params.get("OriginalPrice")
        self.Discount = params.get("Discount")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceReturnable(AbstractModel):
    """实例可退还信息。

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param IsReturnable: 实例是否可退还。
        :type IsReturnable: bool
        :param ReturnFailCode: 实例退还失败错误码。
        :type ReturnFailCode: int
        :param ReturnFailMessage: 实例退还失败错误信息。
        :type ReturnFailMessage: str
        """
        self.InstanceId = None
        self.IsReturnable = None
        self.ReturnFailCode = None
        self.ReturnFailMessage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IsReturnable = params.get("IsReturnable")
        self.ReturnFailCode = params.get("ReturnFailCode")
        self.ReturnFailMessage = params.get("ReturnFailMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTrafficPackage(AbstractModel):
    """实例流量包详情

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param TrafficPackageSet: 流量包详情列表。
        :type TrafficPackageSet: list of TrafficPackage
        """
        self.InstanceId = None
        self.TrafficPackageSet = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("TrafficPackageSet") is not None:
            self.TrafficPackageSet = []
            for item in params.get("TrafficPackageSet"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self.TrafficPackageSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """描述了启动配置创建实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等。

    """

    def __init__(self):
        r"""
        :param InternetChargeType: 网络计费类型，取值范围：
<li>按流量包付费：TRAFFIC_POSTPAID_BY_HOUR</li>
<li>按带宽付费： BANDWIDTH_POSTPAID_BY_HOUR</li>
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: 是否分配公网 IP。
        :type PublicIpAssigned: bool
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """描述密钥对信息。

    """

    def __init__(self):
        r"""
        :param KeyId: 密钥对 ID ，是密钥对的唯一标识。
        :type KeyId: str
        :param KeyName: 密钥对名称。
        :type KeyName: str
        :param PublicKey: 密钥对的纯文本公钥。
        :type PublicKey: str
        :param AssociatedInstanceIds: 密钥对关联的实例 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociatedInstanceIds: list of str
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param PrivateKey: 密钥对私钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        """
        self.KeyId = None
        self.KeyName = None
        self.PublicKey = None
        self.AssociatedInstanceIds = None
        self.CreatedTime = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.PublicKey = params.get("PublicKey")
        self.AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self.CreatedTime = params.get("CreatedTime")
        self.PrivateKey = params.get("PrivateKey")
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
        :param KeyIds: 密钥 ID 列表。关联密钥后，就可以通过对应的私钥来访问实例。注意：此字段可能返回 []，表示取不到有效值。
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
        


class ModifyBlueprintAttributeRequest(AbstractModel):
    """ModifyBlueprintAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param BlueprintId: 镜像 ID。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintId: str
        :param BlueprintName: 设置新的镜像名称。最大长度60。
        :type BlueprintName: str
        :param Description: 设置新的镜像描述。最大长度60。
        :type Description: str
        """
        self.BlueprintId = None
        self.BlueprintName = None
        self.Description = None


    def _deserialize(self, params):
        self.BlueprintId = params.get("BlueprintId")
        self.BlueprintName = params.get("BlueprintName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlueprintAttributeResponse(AbstractModel):
    """ModifyBlueprintAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBundle(AbstractModel):
    """描述了实例可变更的套餐。

    """

    def __init__(self):
        r"""
        :param ModifyPrice: 更改实例套餐后需要补的差价。
        :type ModifyPrice: :class:`tencentcloud.lighthouse.v20200324.models.Price`
        :param ModifyBundleState: 变更套餐状态。取值：
<li>SOLD_OUT：套餐售罄</li>
<li>AVAILABLE：支持套餐变更</li>
<li>UNAVAILABLE：暂不支持套餐变更</li>
        :type ModifyBundleState: str
        :param Bundle: 套餐信息。
        :type Bundle: :class:`tencentcloud.lighthouse.v20200324.models.Bundle`
        """
        self.ModifyPrice = None
        self.ModifyBundleState = None
        self.Bundle = None


    def _deserialize(self, params):
        if params.get("ModifyPrice") is not None:
            self.ModifyPrice = Price()
            self.ModifyPrice._deserialize(params.get("ModifyPrice"))
        self.ModifyBundleState = params.get("ModifyBundleState")
        if params.get("Bundle") is not None:
            self.Bundle = Bundle()
            self.Bundle._deserialize(params.get("Bundle"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksAttributeRequest(AbstractModel):
    """ModifyDisksAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        :param DiskName: 云硬盘名称。
        :type DiskName: str
        """
        self.DiskIds = None
        self.DiskName = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.DiskName = params.get("DiskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksAttributeResponse(AbstractModel):
    """ModifyDisksAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDisksRenewFlagRequest(AbstractModel):
    """ModifyDisksRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        :param RenewFlag: 续费标识。
        :type RenewFlag: str
        """
        self.DiskIds = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisksRenewFlagResponse(AbstractModel):
    """ModifyDisksRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFirewallRuleDescriptionRequest(AbstractModel):
    """ModifyFirewallRuleDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param FirewallRule: 防火墙规则。
        :type FirewallRule: :class:`tencentcloud.lighthouse.v20200324.models.FirewallRule`
        :param FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self.InstanceId = None
        self.FirewallRule = None
        self.FirewallVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FirewallRule") is not None:
            self.FirewallRule = FirewallRule()
            self.FirewallRule._deserialize(params.get("FirewallRule"))
        self.FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFirewallRuleDescriptionResponse(AbstractModel):
    """ModifyFirewallRuleDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFirewallRulesRequest(AbstractModel):
    """ModifyFirewallRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param FirewallRules: 防火墙规则列表。
        :type FirewallRules: list of FirewallRule
        :param FirewallVersion: 防火墙当前版本。用户每次更新防火墙规则时版本会自动加1，防止规则已过期，不填不考虑冲突。
        :type FirewallVersion: int
        """
        self.InstanceId = None
        self.FirewallRules = None
        self.FirewallVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self.FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self.FirewallRules.append(obj)
        self.FirewallVersion = params.get("FirewallVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFirewallRulesResponse(AbstractModel):
    """ModifyFirewallRules返回参数结构体

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
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        :param InstanceName: 实例名称。可任意命名，但不得超过 60 个字符。
        :type InstanceName: str
        """
        self.InstanceIds = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceName = params.get("InstanceName")
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


class ModifyInstancesLoginKeyPairAttributeRequest(AbstractModel):
    """ModifyInstancesLoginKeyPairAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。
        :type InstanceIds: list of str
        :param PermitLogin: 是否允许使用默认密钥对登录，YES：允许登录；NO：禁止登录
        :type PermitLogin: str
        """
        self.InstanceIds = None
        self.PermitLogin = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.PermitLogin = params.get("PermitLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesLoginKeyPairAttributeResponse(AbstractModel):
    """ModifyInstancesLoginKeyPairAttribute返回参数结构体

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
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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


class ModifySnapshotAttributeRequest(AbstractModel):
    """ModifySnapshotAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照 ID, 可通过 DescribeSnapshots 查询。
        :type SnapshotId: str
        :param SnapshotName: 新的快照名称，最长为 60 个字符。
        :type SnapshotName: str
        """
        self.SnapshotId = None
        self.SnapshotName = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotAttributeResponse(AbstractModel):
    """ModifySnapshotAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PolicyDetail(AbstractModel):
    """折扣详情信息。

    """

    def __init__(self):
        r"""
        :param UserDiscount: 用户折扣。
        :type UserDiscount: int
        :param CommonDiscount: 公共折扣。
        :type CommonDiscount: int
        :param FinalDiscount: 最终折扣。
        :type FinalDiscount: int
        """
        self.UserDiscount = None
        self.CommonDiscount = None
        self.FinalDiscount = None


    def _deserialize(self, params):
        self.UserDiscount = params.get("UserDiscount")
        self.CommonDiscount = params.get("CommonDiscount")
        self.FinalDiscount = params.get("FinalDiscount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """价格信息

    """

    def __init__(self):
        r"""
        :param InstancePrice: 实例价格。
        :type InstancePrice: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        """
        self.InstancePrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = InstancePrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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
    """描述地域信息。

    """

    def __init__(self):
        r"""
        :param Region: 地域名称，例如，ap-guangzhou。
        :type Region: str
        :param RegionName: 地域描述，例如，华南地区(广州)。
        :type RegionName: str
        :param RegionState: 地域是否可用状态，取值仅为AVAILABLE。
        :type RegionState: str
        :param IsChinaMainland: 是否中国大陆地域
        :type IsChinaMainland: bool
        """
        self.Region = None
        self.RegionName = None
        self.RegionState = None
        self.IsChinaMainland = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")
        self.IsChinaMainland = params.get("IsChinaMainland")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDiskChargePrepaid(AbstractModel):
    """续费云硬盘包年包月相关参数设置

    """

    def __init__(self):
        r"""
        :param Period: 新购周期。
        :type Period: int
        :param RenewFlag: 续费标识。
        :type RenewFlag: str
        :param TimeUnit: 周期单位. 默认值: "m"。
        :type TimeUnit: str
        :param CurInstanceDeadline: 当前实例到期时间。
        :type CurInstanceDeadline: str
        """
        self.Period = None
        self.RenewFlag = None
        self.TimeUnit = None
        self.CurInstanceDeadline = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        self.TimeUnit = params.get("TimeUnit")
        self.CurInstanceDeadline = params.get("CurInstanceDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAttachCcnRequest(AbstractModel):
    """ResetAttachCcn请求参数结构体

    """

    def __init__(self):
        r"""
        :param CcnId: 云联网实例ID。
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAttachCcnResponse(AbstractModel):
    """ResetAttachCcn返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstanceBlueprint(AbstractModel):
    """描述了镜像重置信息

    """

    def __init__(self):
        r"""
        :param BlueprintInfo: 镜像详细信息
        :type BlueprintInfo: :class:`tencentcloud.lighthouse.v20200324.models.Blueprint`
        :param IsResettable: 实例镜像是否可重置为目标镜像
        :type IsResettable: bool
        :param NonResettableMessage: 不可重置信息.当镜像可重置时为""
        :type NonResettableMessage: str
        """
        self.BlueprintInfo = None
        self.IsResettable = None
        self.NonResettableMessage = None


    def _deserialize(self, params):
        if params.get("BlueprintInfo") is not None:
            self.BlueprintInfo = Blueprint()
            self.BlueprintInfo._deserialize(params.get("BlueprintInfo"))
        self.IsResettable = params.get("IsResettable")
        self.NonResettableMessage = params.get("NonResettableMessage")
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
        :param InstanceId: 实例 ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceId: str
        :param BlueprintId: 镜像 ID。可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintId获取。
        :type BlueprintId: str
        """
        self.InstanceId = None
        self.BlueprintId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BlueprintId = params.get("BlueprintId")
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


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。
        :type InstanceIds: list of str
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：
`LINUX_UNIX` 实例密码必须 8-30 位，推荐使用 12 位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字：0-9<br><li>特殊字符： ()\`~!@#$%^&\*-+=\_|{}[]:;'<>,.?/</li>
`WINDOWS` 实例密码必须 12-30 位，不能以“/”开头且不包括用户名，至少包含以下字符中的三种不同字符<br><li>小写字母：[a-z]<br><li>大写字母：[A-Z]<br><li>数字： 0-9<br><li>特殊字符：()\`~!@#$%^&\*-+=\_|{}[]:;' <>,.?/<br><li>如果实例即包含 `LINUX_UNIX` 实例又包含 `WINDOWS` 实例，则密码复杂度限制按照 `WINDOWS` 实例的限制。
        :type Password: str
        :param UserName: 待重置密码的实例操作系统用户名。不得超过 64 个字符。
        :type UserName: str
        """
        self.InstanceIds = None
        self.Password = None
        self.UserName = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Password = params.get("Password")
        self.UserName = params.get("UserName")
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


class Snapshot(AbstractModel):
    """描述了快照相关信息。

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照 ID。
        :type SnapshotId: str
        :param DiskUsage: 创建此快照的磁盘类型。取值：<li>SYSTEM_DISK：系统盘</li>
        :type DiskUsage: str
        :param DiskId: 创建此快照的磁盘 ID。
        :type DiskId: str
        :param DiskSize: 创建此快照的磁盘大小，单位 GB。
        :type DiskSize: int
        :param SnapshotName: 快照名称，用户自定义的快照别名。
        :type SnapshotName: str
        :param SnapshotState: 快照的状态。取值范围：
<li>NORMAL：正常 </li>
<li>CREATING：创建中</li>
<li>ROLLBACKING：回滚中。</li>
        :type SnapshotState: str
        :param Percent: 创建或回滚快照进度百分比，成功后此字段取值为 100。
        :type Percent: int
        :param LatestOperation: 快照的最新操作，只有创建、回滚快照时记录。
取值如 CreateInstanceSnapshot，RollbackInstanceSnapshot。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param LatestOperationState: 快照的最新操作状态，只有创建、回滚快照时记录。
取值范围：
<li>SUCCESS：表示操作成功</li>
<li>OPERATING：表示操作执行中</li>
<li>FAILED：表示操作失败</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param LatestOperationRequestId: 快照最新操作的唯一请求 ID，只有创建、回滚快照时记录。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationRequestId: str
        :param CreatedTime: 快照的创建时间。
        :type CreatedTime: str
        """
        self.SnapshotId = None
        self.DiskUsage = None
        self.DiskId = None
        self.DiskSize = None
        self.SnapshotName = None
        self.SnapshotState = None
        self.Percent = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.LatestOperationRequestId = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.SnapshotName = params.get("SnapshotName")
        self.SnapshotState = params.get("SnapshotState")
        self.Percent = params.get("Percent")
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.LatestOperationRequestId = params.get("LatestOperationRequestId")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotDeniedActions(AbstractModel):
    """快照操作限制列表。

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照 ID。
        :type SnapshotId: str
        :param DeniedActions: 操作限制列表。
        :type DeniedActions: list of DeniedAction
        """
        self.SnapshotId = None
        self.DeniedActions = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        if params.get("DeniedActions") is not None:
            self.DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = DeniedAction()
                obj._deserialize(item)
                self.DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Software(AbstractModel):
    """描述镜像软件信息。

    """

    def __init__(self):
        r"""
        :param Name: 软件名称。
        :type Name: str
        :param Version: 软件版本。
        :type Version: str
        :param ImageUrl: 软件图片 URL。
        :type ImageUrl: str
        :param InstallDir: 软件安装目录。
        :type InstallDir: str
        :param DetailSet: 软件详情列表。
        :type DetailSet: list of SoftwareDetail
        """
        self.Name = None
        self.Version = None
        self.ImageUrl = None
        self.InstallDir = None
        self.DetailSet = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.ImageUrl = params.get("ImageUrl")
        self.InstallDir = params.get("InstallDir")
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = SoftwareDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftwareDetail(AbstractModel):
    """描述镜像软件详细信息。

    """

    def __init__(self):
        r"""
        :param Key: 详情唯一键。
        :type Key: str
        :param Title: 详情标题。
        :type Title: str
        :param Value: 详情值。
        :type Value: str
        """
        self.Key = None
        self.Title = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Title = params.get("Title")
        self.Value = params.get("Value")
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
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息。

    """

    def __init__(self):
        r"""
        :param DiskType: 系统盘类型。
取值范围： 
<li> LOCAL_BASIC：本地硬盘</li><li> LOCAL_SSD：本地 SSD 硬盘</li><li> CLOUD_BASIC：普通云硬盘</li><li> CLOUD_SSD：SSD 云硬盘</li><li> CLOUD_PREMIUM：高性能云硬盘</li>
        :type DiskType: str
        :param DiskSize: 系统盘大小，单位：GB。
        :type DiskSize: int
        :param DiskId: 系统盘ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskId: str
        """
        self.DiskType = None
        self.DiskSize = None
        self.DiskId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.DiskId = params.get("DiskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param DiskIds: 云硬盘ID列表。
        :type DiskIds: list of str
        """
        self.DiskIds = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例ID列表。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
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


class TrafficPackage(AbstractModel):
    """流量包详情

    """

    def __init__(self):
        r"""
        :param TrafficPackageId: 流量包ID。
        :type TrafficPackageId: str
        :param TrafficUsed: 流量包生效周期内已使用流量，单位字节。
        :type TrafficUsed: int
        :param TrafficPackageTotal: 流量包生效周期内的总流量，单位字节。
        :type TrafficPackageTotal: int
        :param TrafficPackageRemaining: 流量包生效周期内的剩余流量，单位字节。
        :type TrafficPackageRemaining: int
        :param TrafficOverflow: 流量包生效周期内超出流量包额度的流量，单位字节。
        :type TrafficOverflow: int
        :param StartTime: 流量包生效周期开始时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 流量包生效周期结束时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Deadline: 流量包到期时间。按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: str
        :param Status: 流量包状态：
<li>NETWORK_NORMAL：正常</li>
<li>OVERDUE_NETWORK_DISABLED：欠费断网</li>
        :type Status: str
        """
        self.TrafficPackageId = None
        self.TrafficUsed = None
        self.TrafficPackageTotal = None
        self.TrafficPackageRemaining = None
        self.TrafficOverflow = None
        self.StartTime = None
        self.EndTime = None
        self.Deadline = None
        self.Status = None


    def _deserialize(self, params):
        self.TrafficPackageId = params.get("TrafficPackageId")
        self.TrafficUsed = params.get("TrafficUsed")
        self.TrafficPackageTotal = params.get("TrafficPackageTotal")
        self.TrafficPackageRemaining = params.get("TrafficPackageRemaining")
        self.TrafficOverflow = params.get("TrafficOverflow")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Deadline = params.get("Deadline")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """可用区详细信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param ZoneName: 可用区中文名称
        :type ZoneName: str
        :param InstanceDisplayLabel: 实例购买页可用区展示标签
        :type InstanceDisplayLabel: str
        """
        self.Zone = None
        self.ZoneName = None
        self.InstanceDisplayLabel = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.InstanceDisplayLabel = params.get("InstanceDisplayLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        