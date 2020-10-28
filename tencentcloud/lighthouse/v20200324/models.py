# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class Blueprint(AbstractModel):
    """描述了镜像信息。

    """

    def __init__(self):
        """
        :param BlueprintId: 镜像 ID  ，是 blueprint 的唯一标识。
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
        :param BlueprintType: 镜像类型，如 APP_OS、PURE_OS。
        :type BlueprintType: str
        :param ImageUrl: 镜像图片 URL。
        :type ImageUrl: str
        :param RequiredSystemDiskSize: 镜像所需系统盘大小
        :type RequiredSystemDiskSize: int
        :param BlueprintState: 镜像状态，取值：ONLINE、OFFLINE
        :type BlueprintState: str
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


class Bundle(AbstractModel):
    """套餐信息。

    """

    def __init__(self):
        """
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


class CreateFirewallRulesRequest(AbstractModel):
    """CreateFirewallRules请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param FirewallRules: 防火墙规则列表。
        :type FirewallRules: list of FirewallRule
        """
        self.InstanceId = None
        self.FirewallRules = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self.FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self.FirewallRules.append(obj)


class CreateFirewallRulesResponse(AbstractModel):
    """CreateFirewallRules返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param FirewallRules: 防火墙规则列表。
        :type FirewallRules: list of FirewallRule
        """
        self.InstanceId = None
        self.FirewallRules = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FirewallRules") is not None:
            self.FirewallRules = []
            for item in params.get("FirewallRules"):
                obj = FirewallRule()
                obj._deserialize(item)
                self.FirewallRules.append(obj)


class DeleteFirewallRulesResponse(AbstractModel):
    """DeleteFirewallRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBlueprintsRequest(AbstractModel):
    """DescribeBlueprints请求参数结构体

    """

    def __init__(self):
        """
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
取值： APP_OS（预置应用的系统 ）；PURE_OS（纯净的 OS 系统）。
类型：String
必选：否
<li>platform-type</li>按照【镜像平台类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）。
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


class DescribeBlueprintsResponse(AbstractModel):
    """DescribeBlueprints返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeBundlesRequest(AbstractModel):
    """DescribeBundles请求参数结构体

    """

    def __init__(self):
        """
        :param BundleIds: 套餐 ID 列表。
        :type BundleIds: list of str
        :param Offset: 偏移量，默认为 0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/product/1207/47578)中的相关小节。
        :type Limit: int
        :param Filters: 过滤器列表。
<li>bundle-id</li>按照【镜像 ID】进行过滤。
类型：String
必选：否
<li>support-platform-type</li>按照【系统类型】进行过滤。
取值： LINUX_UNIX（Linux/Unix系统）；WINDOWS（Windows 系统）
类型：String
必选：否
每次请求的 Filters 的上限为 10，Filter.Values 的上限为 5。参数不支持同时指定 BundleIds 和 Filters。
        :type Filters: list of Filter
        """
        self.BundleIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


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


class DescribeBundlesResponse(AbstractModel):
    """DescribeBundles返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeFirewallRulesRequest(AbstractModel):
    """DescribeFirewallRules请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeFirewallRulesResponse(AbstractModel):
    """DescribeFirewallRules返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeInstancesTrafficPackagesRequest(AbstractModel):
    """DescribeInstancesTrafficPackages请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeInstancesTrafficPackagesResponse(AbstractModel):
    """DescribeInstancesTrafficPackages返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class FirewallRule(AbstractModel):
    """描述防火墙规则信息。

    """

    def __init__(self):
        """
        :param Protocol: 协议，取值：TCP，UDP，ALL。
        :type Protocol: str
        :param Port: 端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。
        :type Port: str
        """
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")


class FirewallRuleInfo(AbstractModel):
    """描述防火墙规则详细信息。

    """

    def __init__(self):
        """
        :param AppType: 应用类型，取值：自定义，HTTP(80)，HTTPS(443)，Linux登录(22)，Windows登录(3389)，MySQL(3306)，SQL Server(1433)，全部TCP，全部UDP，ALL。
        :type AppType: str
        :param Protocol: 协议，取值：TCP，UDP，ALL。
        :type Protocol: str
        :param Port: 端口，取值：ALL，单独的端口，逗号分隔的离散端口，减号分隔的端口范围。
        :type Port: str
        """
        self.AppType = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.AppType = params.get("AppType")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")


class Instance(AbstractModel):
    """描述了实例信息。

    """

    def __init__(self):
        """
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


class InstancePrice(AbstractModel):
    """关于Lighthouse Instance实例的价格信息

    """

    def __init__(self):
        """
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


class InstanceTrafficPackage(AbstractModel):
    """实例流量包详情

    """

    def __init__(self):
        """
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


class InternetAccessible(AbstractModel):
    """描述了启动配置创建实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等。

    """

    def __init__(self):
        """
        :param InternetChargeType: 网络计费类型。
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


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        """
        :param KeyIds: 密钥 ID 列表。关联密钥后，就可以通过对应的私钥来访问实例。注意：此字段可能返回 []，表示取不到有效值。
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class Price(AbstractModel):
    """价格信息

    """

    def __init__(self):
        """
        :param InstancePrice: 实例价格。
        :type InstancePrice: :class:`tencentcloud.lighthouse.v20200324.models.InstancePrice`
        """
        self.InstancePrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = InstancePrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstanceRequest(AbstractModel):
    """ResetInstance请求参数结构体

    """

    def __init__(self):
        """
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


class ResetInstanceResponse(AbstractModel):
    """ResetInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartInstancesRequest(AbstractModel):
    """StartInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class StartInstancesResponse(AbstractModel):
    """StartInstances返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param InstanceIds: 实例 ID 列表。每次请求批量实例的上限为 100。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1207/47573)接口返回值中的InstanceId获取。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class StopInstancesResponse(AbstractModel):
    """StopInstances返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class TrafficPackage(AbstractModel):
    """流量包详情

    """

    def __init__(self):
        """
        :param TrafficPackageId: 流量包ID。
        :type TrafficPackageId: str
        :param TrafficUsed: 流量包生效周期内的总流量，单位字节。
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