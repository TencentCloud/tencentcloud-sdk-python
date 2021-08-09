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


class Alias(AbstractModel):
    """别名对象

    """

    def __init__(self):
        """
        :param AliasId: 别名的唯一标识符\n        :type AliasId: str\n        :param AliasArn: 别名的全局唯一资源标识符\n        :type AliasArn: str\n        :param Name: 名字，长度不小于1字符不超过1024字符\n        :type Name: str\n        :param Description: 别名的可读说明，长度不小于1字符不超过1024字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param RoutingStrategy: 别名的路由配置\n        :type RoutingStrategy: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param LastUpdatedTime: 上次修改此数据对象的时间\n        :type LastUpdatedTime: str\n        :param Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        """
        self.AliasId = None
        self.AliasArn = None
        self.Name = None
        self.Description = None
        self.RoutingStrategy = None
        self.CreationTime = None
        self.LastUpdatedTime = None
        self.Tags = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.AliasArn = params.get("AliasArn")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("RoutingStrategy") is not None:
            self.RoutingStrategy = RoutingStrategy()
            self.RoutingStrategy._deserialize(params.get("RoutingStrategy"))
        self.CreationTime = params.get("CreationTime")
        self.LastUpdatedTime = params.get("LastUpdatedTime")
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
        


class Asset(AbstractModel):
    """生成包信息

    """

    def __init__(self):
        """
        :param AssetId: 生成包ID\n        :type AssetId: str\n        :param AssetName: 生成包名字，最小长度为1，最大长度为64\n        :type AssetName: str\n        :param AssetVersion: 生成包版本，最小长度为1，最大长度为64\n        :type AssetVersion: str\n        :param OperateSystem: 生成包可运行的操作系统，暂时只支持CentOS7.16\n        :type OperateSystem: str\n        :param Stauts: 生成包状态，0代表上传中，1代表上传失败，2代表上传成功\n        :type Stauts: int\n        :param Size: 生成包大小\n        :type Size: str\n        :param CreateTime: 生成包创建时间\n        :type CreateTime: str\n        :param BindFleetNum: 生成包绑定的Fleet个数，最小值为0\n        :type BindFleetNum: int\n        :param AssetArn: 生成包的全局唯一资源标识符\n        :type AssetArn: str\n        :param ImageId: 生成包支持的操作系统镜像id\n        :type ImageId: str\n        :param OsType: 生成包支持的操作系统类型\n        :type OsType: str\n        :param ResourceType: 生成包资源类型，ASSET 或者 IMAGE；ASSET 代表是原有生成包类型，IMAGE 为扩充使用镜像类型\n        :type ResourceType: str\n        :param SharingStatus: 镜像资源共享类型，当 ResourceType 为 IMAGE 时该字段有意义，SHARED 表示共享、SHARED_IMAGE 表示未共享；ResourceType 为 ASSET 时这里返回 UNKNOWN_SHARED 用于占位\n        :type SharingStatus: str\n        :param Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        """
        self.AssetId = None
        self.AssetName = None
        self.AssetVersion = None
        self.OperateSystem = None
        self.Stauts = None
        self.Size = None
        self.CreateTime = None
        self.BindFleetNum = None
        self.AssetArn = None
        self.ImageId = None
        self.OsType = None
        self.ResourceType = None
        self.SharingStatus = None
        self.Tags = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.AssetName = params.get("AssetName")
        self.AssetVersion = params.get("AssetVersion")
        self.OperateSystem = params.get("OperateSystem")
        self.Stauts = params.get("Stauts")
        self.Size = params.get("Size")
        self.CreateTime = params.get("CreateTime")
        self.BindFleetNum = params.get("BindFleetNum")
        self.AssetArn = params.get("AssetArn")
        self.ImageId = params.get("ImageId")
        self.OsType = params.get("OsType")
        self.ResourceType = params.get("ResourceType")
        self.SharingStatus = params.get("SharingStatus")
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
        


class AssetCredentials(AbstractModel):
    """上传Asset的临时证书

    """

    def __init__(self):
        """
        :param TmpSecretId: 临时证书密钥ID\n        :type TmpSecretId: str\n        :param TmpSecretKey: 临时证书密钥Key\n        :type TmpSecretKey: str\n        :param Token: 临时证书Token\n        :type Token: str\n        """
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.Token = None


    def _deserialize(self, params):
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetSupportSys(AbstractModel):
    """生成包支持操作系统详细信息

    """

    def __init__(self):
        """
        :param ImageId: 生成包操作系统的镜像Id\n        :type ImageId: str\n        :param OsType: 生成包操作系统的类型\n        :type OsType: str\n        :param OsBit: 生成包操作系统的位数\n        :type OsBit: int\n        :param OsVersion: 生成包操作系统的版本\n        :type OsVersion: str\n        """
        self.ImageId = None
        self.OsType = None
        self.OsBit = None
        self.OsVersion = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.OsType = params.get("OsType")
        self.OsBit = params.get("OsBit")
        self.OsVersion = params.get("OsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnInstancesRequest(AbstractModel):
    """AttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param AccountId: 云联网账号 Uin\n        :type AccountId: str\n        :param CcnId: 云联网 Id\n        :type CcnId: str\n        """
        self.FleetId = None
        self.AccountId = None
        self.CcnId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.AccountId = params.get("AccountId")
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnInstancesResponse(AbstractModel):
    """AttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CcnInfo(AbstractModel):
    """云联网相关信息

    """

    def __init__(self):
        """
        :param AccountId: 云联网所属账号\n        :type AccountId: str\n        :param CcnId: 云联网id\n        :type CcnId: str\n        """
        self.AccountId = None
        self.CcnId = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnInstanceSets(AbstractModel):
    """云联网实例信息

    """

    def __init__(self):
        """
        :param AccountId: 云联网账号 Uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccountId: str\n        :param CcnId: 云联网 Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type CcnId: str\n        :param CreateTime: 云联网关联时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param InstanceName: 云联网实例名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param State: 云联网状态：申请中、已连接、已过期、已拒绝、已删除、失败的、关联中、解关联中、解关联失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type State: str\n        """
        self.AccountId = None
        self.CcnId = None
        self.CreateTime = None
        self.InstanceName = None
        self.State = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.CcnId = params.get("CcnId")
        self.CreateTime = params.get("CreateTime")
        self.InstanceName = params.get("InstanceName")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetRequest(AbstractModel):
    """CopyFleet请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param CopyNumber: 复制数量，最小值1，最大值为剩余配额，可以根据[获取用户配额](https://cloud.tencent.com/document/product/1165/48732)接口获取。\n        :type CopyNumber: int\n        :param AssetId: 生成包 Id\n        :type AssetId: str\n        :param Description: 描述，最小长度0，最大长度100\n        :type Description: str\n        :param InboundPermissions: 网络配置\n        :type InboundPermissions: list of InboundPermission\n        :param InstanceType: 服务器类型，参数根据[获取服务器实例类型列表](https://cloud.tencent.com/document/product/1165/48732)接口获取。\n        :type InstanceType: str\n        :param FleetType: 服务器舰队类型，目前只支持ON_DEMAND类型\n        :type FleetType: str\n        :param Name: 服务器舰队名称，最小长度1，最大长度50\n        :type Name: str\n        :param NewGameServerSessionProtectionPolicy: 保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection\n        :type NewGameServerSessionProtectionPolicy: str\n        :param ResourceCreationLimitPolicy: 资源创建限制策略\n        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`\n        :param RuntimeConfiguration: 进程配置\n        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`\n        :param GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效\n        :type GameServerSessionProtectionTimeLimit: int\n        :param SelectedScalingType: 是否选择扩缩容：SCALING_SELECTED 或者 SCALING_UNSELECTED；默认是 SCALING_UNSELECTED\n        :type SelectedScalingType: str\n        :param SelectedCcnType: 是否选择云联网：CCN_SELECTED_BEFORE_CREATE（创建前关联）， CCN_SELECTED_AFTER_CREATE（创建后关联）或者 CCN_UNSELECTED（不关联）；默认是 CCN_UNSELECTED\n        :type SelectedCcnType: str\n        :param Tags: 标签列表，最大长度50组\n        :type Tags: list of Tag\n        :param SystemDiskInfo: 系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位\n        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`\n        :param DataDiskInfo: 数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位\n        :type DataDiskInfo: list of DiskInfo\n        :param SelectedTimerType: 是否选择复制定时器策略：TIMER_SELECTED 或者 TIMER_UNSELECTED；默认是 TIMER_UNSELECTED\n        :type SelectedTimerType: str\n        :param CcnInfos: 云联网信息，包含对应的账号信息及所属id\n        :type CcnInfos: list of CcnInfo\n        :param InternetMaxBandwidthOut: fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps\n        :type InternetMaxBandwidthOut: int\n        """
        self.FleetId = None
        self.CopyNumber = None
        self.AssetId = None
        self.Description = None
        self.InboundPermissions = None
        self.InstanceType = None
        self.FleetType = None
        self.Name = None
        self.NewGameServerSessionProtectionPolicy = None
        self.ResourceCreationLimitPolicy = None
        self.RuntimeConfiguration = None
        self.GameServerSessionProtectionTimeLimit = None
        self.SelectedScalingType = None
        self.SelectedCcnType = None
        self.Tags = None
        self.SystemDiskInfo = None
        self.DataDiskInfo = None
        self.SelectedTimerType = None
        self.CcnInfos = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.CopyNumber = params.get("CopyNumber")
        self.AssetId = params.get("AssetId")
        self.Description = params.get("Description")
        if params.get("InboundPermissions") is not None:
            self.InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self.InboundPermissions.append(obj)
        self.InstanceType = params.get("InstanceType")
        self.FleetType = params.get("FleetType")
        self.Name = params.get("Name")
        self.NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self.ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self.ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        if params.get("RuntimeConfiguration") is not None:
            self.RuntimeConfiguration = RuntimeConfiguration()
            self.RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self.GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self.SelectedScalingType = params.get("SelectedScalingType")
        self.SelectedCcnType = params.get("SelectedCcnType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self.SystemDiskInfo = DiskInfo()
            self.SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("DataDiskInfo") is not None:
            self.DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDiskInfo.append(obj)
        self.SelectedTimerType = params.get("SelectedTimerType")
        if params.get("CcnInfos") is not None:
            self.CcnInfos = []
            for item in params.get("CcnInfos"):
                obj = CcnInfo()
                obj._deserialize(item)
                self.CcnInfos.append(obj)
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFleetResponse(AbstractModel):
    """CopyFleet返回参数结构体

    """

    def __init__(self):
        """
        :param FleetAttributes: 服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetAttributes: list of FleetAttributes\n        :param TotalCount: 服务器舰队数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetAttributes = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self.FleetAttributes = []
            for item in params.get("FleetAttributes"):
                obj = FleetAttributes()
                obj._deserialize(item)
                self.FleetAttributes.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class CreateAliasRequest(AbstractModel):
    """CreateAlias请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 名字，长度不小于1字符不超过1024字符\n        :type Name: str\n        :param RoutingStrategy: 别名的路由配置\n        :type RoutingStrategy: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`\n        :param Description: 别名的可读说明，长度不小于1字符不超过1024字符\n        :type Description: str\n        :param Tags: 标签列表，最大长度50组\n        :type Tags: list of Tag\n        """
        self.Name = None
        self.RoutingStrategy = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("RoutingStrategy") is not None:
            self.RoutingStrategy = RoutingStrategy()
            self.RoutingStrategy._deserialize(params.get("RoutingStrategy"))
        self.Description = params.get("Description")
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
        


class CreateAliasResponse(AbstractModel):
    """CreateAlias返回参数结构体

    """

    def __init__(self):
        """
        :param Alias: 别名对象\n        :type Alias: :class:`tencentcloud.gse.v20191112.models.Alias`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Alias = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alias") is not None:
            self.Alias = Alias()
            self.Alias._deserialize(params.get("Alias"))
        self.RequestId = params.get("RequestId")


class CreateAssetRequest(AbstractModel):
    """CreateAsset请求参数结构体

    """

    def __init__(self):
        """
        :param BucketKey: 生成包的ZIP包名，例如：server.zip\n        :type BucketKey: str\n        :param AssetName: 生成包名字，最小长度为1，最大长度为64\n        :type AssetName: str\n        :param AssetVersion: 生成包版本，最小长度为1，最大长度为64\n        :type AssetVersion: str\n        :param AssetRegion: 生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)\n        :type AssetRegion: str\n        :param OperateSystem: 生成包可运行的操作系统，若传入参数为CentOS7.16则不需要传入ImageId字段，否则，需要传入Imageid字段（该方式是为了兼容之前的版本，后续建议使用ImageId来替代该字段）。这里可通过[DescribeAssetSystems](https://cloud.tencent.com/document/product/1165/49191)接口获取asset支持的操作系统进行传入（使用AssetSupportSys的OsVersion字段）\n        :type OperateSystem: str\n        :param ImageId: 生成包支持的操作系统镜像id，若传入OperateSystem字段的值是CentOS7.16，则不需要传入该值；如果不是，则需要通过[DescribeAssetSystems](https://cloud.tencent.com/document/product/1165/49191)接口获取asset支持的操作系统ImageId进行传入\n        :type ImageId: str\n        :param Tags: 标签列表，最大长度50组\n        :type Tags: list of Tag\n        """
        self.BucketKey = None
        self.AssetName = None
        self.AssetVersion = None
        self.AssetRegion = None
        self.OperateSystem = None
        self.ImageId = None
        self.Tags = None


    def _deserialize(self, params):
        self.BucketKey = params.get("BucketKey")
        self.AssetName = params.get("AssetName")
        self.AssetVersion = params.get("AssetVersion")
        self.AssetRegion = params.get("AssetRegion")
        self.OperateSystem = params.get("OperateSystem")
        self.ImageId = params.get("ImageId")
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
        


class CreateAssetResponse(AbstractModel):
    """CreateAsset返回参数结构体

    """

    def __init__(self):
        """
        :param AssetId: 生成包ID\n        :type AssetId: str\n        :param AssetArn: 生成包的全局唯一资源标识符\n        :type AssetArn: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AssetId = None
        self.AssetArn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.AssetArn = params.get("AssetArn")
        self.RequestId = params.get("RequestId")


class CreateAssetWithImageRequest(AbstractModel):
    """CreateAssetWithImage请求参数结构体

    """

    def __init__(self):
        """
        :param AssetName: 生成包名字，最小长度为1，最大长度为64\n        :type AssetName: str\n        :param AssetVersion: 生成包版本，最小长度为1，最大长度为64\n        :type AssetVersion: str\n        :param AssetRegion: 生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)\n        :type AssetRegion: str\n        :param ImageId: 生成包支持的操作系统镜像id\n        :type ImageId: str\n        :param ImageSize: 操作系统镜像包大小，比如：40GB，支持单位 KB、MB、GB\n        :type ImageSize: str\n        :param ImageOs: 操作系统镜像包名称，最小长度为1，最大长度为64\n        :type ImageOs: str\n        :param OsType: 操作系统镜像包类型，CentOS 或者 Windows\n        :type OsType: str\n        :param ImageType: 操作系统镜像包类型，当前只支持 SHARED_IMAGE\n        :type ImageType: str\n        :param OsBit: 操作系统镜像包位数，32 或者 64\n        :type OsBit: int\n        """
        self.AssetName = None
        self.AssetVersion = None
        self.AssetRegion = None
        self.ImageId = None
        self.ImageSize = None
        self.ImageOs = None
        self.OsType = None
        self.ImageType = None
        self.OsBit = None


    def _deserialize(self, params):
        self.AssetName = params.get("AssetName")
        self.AssetVersion = params.get("AssetVersion")
        self.AssetRegion = params.get("AssetRegion")
        self.ImageId = params.get("ImageId")
        self.ImageSize = params.get("ImageSize")
        self.ImageOs = params.get("ImageOs")
        self.OsType = params.get("OsType")
        self.ImageType = params.get("ImageType")
        self.OsBit = params.get("OsBit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssetWithImageResponse(AbstractModel):
    """CreateAssetWithImage返回参数结构体

    """

    def __init__(self):
        """
        :param AssetId: 生成包ID\n        :type AssetId: str\n        :param AssetArn: 生成包的全局唯一资源标识符\n        :type AssetArn: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AssetId = None
        self.AssetArn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.AssetArn = params.get("AssetArn")
        self.RequestId = params.get("RequestId")


class CreateFleetRequest(AbstractModel):
    """CreateFleet请求参数结构体

    """

    def __init__(self):
        """
        :param AssetId: 生成包 Id\n        :type AssetId: str\n        :param Description: 描述，最小长度0，最大长度100\n        :type Description: str\n        :param InboundPermissions: 网络配置\n        :type InboundPermissions: list of InboundPermission\n        :param InstanceType: 服务器类型，参数根据[获取服务器实例类型列表](https://cloud.tencent.com/document/product/1165/48732)接口获取。\n        :type InstanceType: str\n        :param FleetType: 服务器舰队类型，目前只支持ON_DEMAND类型\n        :type FleetType: str\n        :param Name: 服务器舰队名称，最小长度1，最大长度50\n        :type Name: str\n        :param NewGameServerSessionProtectionPolicy: 保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection\n        :type NewGameServerSessionProtectionPolicy: str\n        :param PeerVpcId: VPC 网络 Id，对等连接已不再使用\n        :type PeerVpcId: str\n        :param ResourceCreationLimitPolicy: 资源创建限制策略\n        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`\n        :param RuntimeConfiguration: 进程配置\n        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`\n        :param SubNetId: VPC 子网，对等连接已不再使用\n        :type SubNetId: str\n        :param GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效\n        :type GameServerSessionProtectionTimeLimit: int\n        :param Tags: 标签列表，最大长度50组\n        :type Tags: list of Tag\n        :param SystemDiskInfo: 系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位\n        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`\n        :param DataDiskInfo: 数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位\n        :type DataDiskInfo: list of DiskInfo\n        :param CcnInfos: 云联网信息，包含对应的账号信息及所属id\n        :type CcnInfos: list of CcnInfo\n        :param InternetMaxBandwidthOut: fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps\n        :type InternetMaxBandwidthOut: int\n        """
        self.AssetId = None
        self.Description = None
        self.InboundPermissions = None
        self.InstanceType = None
        self.FleetType = None
        self.Name = None
        self.NewGameServerSessionProtectionPolicy = None
        self.PeerVpcId = None
        self.ResourceCreationLimitPolicy = None
        self.RuntimeConfiguration = None
        self.SubNetId = None
        self.GameServerSessionProtectionTimeLimit = None
        self.Tags = None
        self.SystemDiskInfo = None
        self.DataDiskInfo = None
        self.CcnInfos = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.Description = params.get("Description")
        if params.get("InboundPermissions") is not None:
            self.InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self.InboundPermissions.append(obj)
        self.InstanceType = params.get("InstanceType")
        self.FleetType = params.get("FleetType")
        self.Name = params.get("Name")
        self.NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        self.PeerVpcId = params.get("PeerVpcId")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self.ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self.ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        if params.get("RuntimeConfiguration") is not None:
            self.RuntimeConfiguration = RuntimeConfiguration()
            self.RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self.SubNetId = params.get("SubNetId")
        self.GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self.SystemDiskInfo = DiskInfo()
            self.SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("DataDiskInfo") is not None:
            self.DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDiskInfo.append(obj)
        if params.get("CcnInfos") is not None:
            self.CcnInfos = []
            for item in params.get("CcnInfos"):
                obj = CcnInfo()
                obj._deserialize(item)
                self.CcnInfos.append(obj)
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFleetResponse(AbstractModel):
    """CreateFleet返回参数结构体

    """

    def __init__(self):
        """
        :param FleetAttributes: 服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetAttributes: :class:`tencentcloud.gse.v20191112.models.FleetAttributes`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetAttributes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self.FleetAttributes = FleetAttributes()
            self.FleetAttributes._deserialize(params.get("FleetAttributes"))
        self.RequestId = params.get("RequestId")


class CreateGameServerSessionQueueRequest(AbstractModel):
    """CreateGameServerSessionQueue请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 游戏服务器会话队列名称，长度1~128\n        :type Name: str\n        :param Destinations: 目的服务器舰队（可为别名）列表\n        :type Destinations: list of GameServerSessionQueueDestination\n        :param PlayerLatencyPolicies: 延迟策略集合\n        :type PlayerLatencyPolicies: list of PlayerLatencyPolicy\n        :param TimeoutInSeconds: 超时时间（单位秒，默认值为600秒）\n        :type TimeoutInSeconds: int\n        :param Tags: 标签列表，最大长度50组\n        :type Tags: list of Tag\n        """
        self.Name = None
        self.Destinations = None
        self.PlayerLatencyPolicies = None
        self.TimeoutInSeconds = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = GameServerSessionQueueDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        if params.get("PlayerLatencyPolicies") is not None:
            self.PlayerLatencyPolicies = []
            for item in params.get("PlayerLatencyPolicies"):
                obj = PlayerLatencyPolicy()
                obj._deserialize(item)
                self.PlayerLatencyPolicies.append(obj)
        self.TimeoutInSeconds = params.get("TimeoutInSeconds")
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
        


class CreateGameServerSessionQueueResponse(AbstractModel):
    """CreateGameServerSessionQueue返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionQueue: 游戏服务器会话队列\n        :type GameServerSessionQueue: :class:`tencentcloud.gse.v20191112.models.GameServerSessionQueue`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessionQueue = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionQueue") is not None:
            self.GameServerSessionQueue = GameServerSessionQueue()
            self.GameServerSessionQueue._deserialize(params.get("GameServerSessionQueue"))
        self.RequestId = params.get("RequestId")


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param MaximumPlayerSessionCount: 最大玩家数量，最小值不小于0\n        :type MaximumPlayerSessionCount: int\n        :param AliasId: 别名ID。每个请求需要指定别名ID 或者舰队 ID，如果两个同时指定时，优先选择舰队 ID\n        :type AliasId: str\n        :param CreatorId: 创建者ID，最大长度不超过1024个ASCII字符\n        :type CreatorId: str\n        :param FleetId: 舰队ID。每个请求需要指定别名ID 或者舰队 ID，如果两个同时指定时，优先选择舰队 ID\n        :type FleetId: str\n        :param GameProperties: 游戏属性，最大长度不超过16组\n        :type GameProperties: list of GameProperty\n        :param GameServerSessionData: 游戏服务器会话属性详情，最大长度不超过4096个ASCII字符\n        :type GameServerSessionData: str\n        :param GameServerSessionId: 游戏服务器会话自定义ID，最大长度不超过4096个ASCII字符\n        :type GameServerSessionId: str\n        :param IdempotencyToken: 幂等token，最大长度不超过48个ASCII字符\n        :type IdempotencyToken: str\n        :param Name: 游戏服务器会话名称，最大长度不超过1024个ASCII字符\n        :type Name: str\n        """
        self.MaximumPlayerSessionCount = None
        self.AliasId = None
        self.CreatorId = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IdempotencyToken = None
        self.Name = None


    def _deserialize(self, params):
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.AliasId = params.get("AliasId")
        self.CreatorId = params.get("CreatorId")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IdempotencyToken = params.get("IdempotencyToken")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSession: 游戏服务器会话
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """访问实例所需要的凭据

    """

    def __init__(self):
        """
        :param Secret: ssh私钥\n        :type Secret: str\n        :param UserName: 用户名\n        :type UserName: str\n        """
        self.Secret = None
        self.UserName = None


    def _deserialize(self, params):
        self.Secret = params.get("Secret")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasRequest(AbstractModel):
    """DeleteAlias请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 要删除的别名ID\n        :type AliasId: str\n        """
        self.AliasId = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasResponse(AbstractModel):
    """DeleteAlias返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAssetRequest(AbstractModel):
    """DeleteAsset请求参数结构体

    """

    def __init__(self):
        """
        :param AssetId: 生成包ID\n        :type AssetId: str\n        """
        self.AssetId = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAssetResponse(AbstractModel):
    """DeleteAsset返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFleetRequest(AbstractModel):
    """DeleteFleet请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        """
        self.FleetId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFleetResponse(AbstractModel):
    """DeleteFleet返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGameServerSessionQueueRequest(AbstractModel):
    """DeleteGameServerSessionQueue请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 游戏服务器会话队列名字，长度1~128\n        :type Name: str\n        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGameServerSessionQueueResponse(AbstractModel):
    """DeleteGameServerSessionQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param Name: 扩缩容策略名称，最小长度为0，最大长度为1024\n        :type Name: str\n        """
        self.FleetId = None
        self.Name = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTimerScalingPolicyRequest(AbstractModel):
    """DeleteTimerScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param TimerId: 定时器ID, 进行encode\n        :type TimerId: str\n        :param FleetId: 扩缩容配置服务器舰队ID\n        :type FleetId: str\n        :param TimerName: 定时器名称\n        :type TimerName: str\n        """
        self.TimerId = None
        self.FleetId = None
        self.TimerName = None


    def _deserialize(self, params):
        self.TimerId = params.get("TimerId")
        self.FleetId = params.get("FleetId")
        self.TimerName = params.get("TimerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimerScalingPolicyResponse(AbstractModel):
    """DeleteTimerScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAliasRequest(AbstractModel):
    """DescribeAlias请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 要检索的队列别名的唯一标识符\n        :type AliasId: str\n        """
        self.AliasId = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAliasResponse(AbstractModel):
    """DescribeAlias返回参数结构体

    """

    def __init__(self):
        """
        :param Alias: 别名对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: :class:`tencentcloud.gse.v20191112.models.Alias`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Alias = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alias") is not None:
            self.Alias = Alias()
            self.Alias._deserialize(params.get("Alias"))
        self.RequestId = params.get("RequestId")


class DescribeAssetRequest(AbstractModel):
    """DescribeAsset请求参数结构体

    """

    def __init__(self):
        """
        :param AssetId: 生成包ID\n        :type AssetId: str\n        """
        self.AssetId = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetResponse(AbstractModel):
    """DescribeAsset返回参数结构体

    """

    def __init__(self):
        """
        :param Asset: 生成包信息\n        :type Asset: :class:`tencentcloud.gse.v20191112.models.Asset`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Asset = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Asset") is not None:
            self.Asset = Asset()
            self.Asset._deserialize(params.get("Asset"))
        self.RequestId = params.get("RequestId")


class DescribeAssetSystemsRequest(AbstractModel):
    """DescribeAssetSystems请求参数结构体

    """

    def __init__(self):
        """
        :param OsType: 生成包支持的操作系统类型\n        :type OsType: str\n        :param OsBit: 生成包支持的操作系统位数\n        :type OsBit: int\n        """
        self.OsType = None
        self.OsBit = None


    def _deserialize(self, params):
        self.OsType = params.get("OsType")
        self.OsBit = params.get("OsBit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetSystemsResponse(AbstractModel):
    """DescribeAssetSystems返回参数结构体

    """

    def __init__(self):
        """
        :param AssetSupportSys: 生成包支持的操作系统类型列表\n        :type AssetSupportSys: list of AssetSupportSys\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AssetSupportSys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssetSupportSys") is not None:
            self.AssetSupportSys = []
            for item in params.get("AssetSupportSys"):
                obj = AssetSupportSys()
                obj._deserialize(item)
                self.AssetSupportSys.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetsRequest(AbstractModel):
    """DescribeAssets请求参数结构体

    """

    def __init__(self):
        """
        :param AssetRegion: 生成包支持的可部署 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)\n        :type AssetRegion: str\n        :param Offset: 偏移，代表页数，与asset实际数量相关\n        :type Offset: int\n        :param Limit: 前端界面每页显示的最大条数，不超过100\n        :type Limit: int\n        :param Filter: 搜索条件，支持包ID或包名字过滤，该字段会逐步废弃，建议使用 Filters 字段\n        :type Filter: str\n        :param Filters: 资源过滤字段，可以按照资源名称、资源ID和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（生成包当前仅支持单个名称的过滤）- 资源ID过滤    - Key: 固定字符串 "resource:resourceId"    - Values: 生成包ID数组（生成包当前仅支持单个生成包ID的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]\n        :type Filters: list of Filter\n        """
        self.AssetRegion = None
        self.Offset = None
        self.Limit = None
        self.Filter = None
        self.Filters = None


    def _deserialize(self, params):
        self.AssetRegion = params.get("AssetRegion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Filter = params.get("Filter")
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
        


class DescribeAssetsResponse(AbstractModel):
    """DescribeAssets返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 生成包总数\n        :type TotalCount: int\n        :param Assets: 生成包列表\n        :type Assets: list of Asset\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Assets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Assets") is not None:
            self.Assets = []
            for item in params.get("Assets"):
                obj = Asset()
                obj._deserialize(item)
                self.Assets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnInstancesRequest(AbstractModel):
    """DescribeCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        """
        self.FleetId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnInstancesResponse(AbstractModel):
    """DescribeCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param CcnInstanceSets: 云联网实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type CcnInstanceSets: list of CcnInstanceSets\n        :param TotalCount: 云联网实例个数，最小值为0\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CcnInstanceSets = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CcnInstanceSets") is not None:
            self.CcnInstanceSets = []
            for item in params.get("CcnInstanceSets"):
                obj = CcnInstanceSets()
                obj._deserialize(item)
                self.CcnInstanceSets.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFleetAttributesRequest(AbstractModel):
    """DescribeFleetAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param FleetIds: 服务器舰队 Ids\n        :type FleetIds: list of str\n        :param Limit: 结果返回最大数量，默认值20，最大值100\n        :type Limit: int\n        :param Offset: 返回结果偏移，最小值0\n        :type Offset: int\n        """
        self.FleetIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.FleetIds = params.get("FleetIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetAttributesResponse(AbstractModel):
    """DescribeFleetAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param FleetAttributes: 服务器舰队属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetAttributes: list of FleetAttributes\n        :param TotalCount: 服务器舰队总数，最小值0\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetAttributes = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FleetAttributes") is not None:
            self.FleetAttributes = []
            for item in params.get("FleetAttributes"):
                obj = FleetAttributes()
                obj._deserialize(item)
                self.FleetAttributes.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFleetCapacityRequest(AbstractModel):
    """DescribeFleetCapacity请求参数结构体

    """

    def __init__(self):
        """
        :param FleetIds: 服务器舰队ID列表\n        :type FleetIds: list of str\n        :param Limit: 结果返回最大数量，最大值 100\n        :type Limit: int\n        :param Offset: 返回结果偏移，最小值 0\n        :type Offset: int\n        """
        self.FleetIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.FleetIds = params.get("FleetIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetCapacityResponse(AbstractModel):
    """DescribeFleetCapacity返回参数结构体

    """

    def __init__(self):
        """
        :param FleetCapacity: 服务器舰队的容量配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetCapacity: list of FleetCapacity\n        :param TotalCount: 结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetCapacity = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FleetCapacity") is not None:
            self.FleetCapacity = []
            for item in params.get("FleetCapacity"):
                obj = FleetCapacity()
                obj._deserialize(item)
                self.FleetCapacity.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFleetEventsRequest(AbstractModel):
    """DescribeFleetEvents请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param Limit: 分页时返回服务器舰队事件的数量，默认为20，最大值为100\n        :type Limit: int\n        :param Offset: 分页时的数据偏移量，默认为0\n        :type Offset: int\n        :param EventCode: 事件代码\n        :type EventCode: str\n        :param StartTime: 发生事件的开始时间\n        :type StartTime: str\n        :param EndTime: 发生事件的结束时间\n        :type EndTime: str\n        """
        self.FleetId = None
        self.Limit = None
        self.Offset = None
        self.EventCode = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.EventCode = params.get("EventCode")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetEventsResponse(AbstractModel):
    """DescribeFleetEvents返回参数结构体

    """

    def __init__(self):
        """
        :param Events: 返回的事件列表\n        :type Events: list of Event\n        :param TotalCount: 返回的事件总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Events = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFleetPortSettingsRequest(AbstractModel):
    """DescribeFleetPortSettings请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        """
        self.FleetId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetPortSettingsResponse(AbstractModel):
    """DescribeFleetPortSettings返回参数结构体

    """

    def __init__(self):
        """
        :param InboundPermissions: 安全组信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InboundPermissions: list of InboundPermission\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InboundPermissions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InboundPermissions") is not None:
            self.InboundPermissions = []
            for item in params.get("InboundPermissions"):
                obj = InboundPermission()
                obj._deserialize(item)
                self.InboundPermissions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFleetRelatedResourcesRequest(AbstractModel):
    """DescribeFleetRelatedResources请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        """
        self.FleetId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetRelatedResourcesResponse(AbstractModel):
    """DescribeFleetRelatedResources返回参数结构体

    """

    def __init__(self):
        """
        :param Resources: 与服务器舰队关联的资源信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Resources: list of FleetRelatedResource\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Resources = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = FleetRelatedResource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFleetStatisticDetailsRequest(AbstractModel):
    """DescribeFleetStatisticDetails请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param BeginTime: 查询开始时间，时间格式：YYYY-MM-DD hh:mm:ss\n        :type BeginTime: str\n        :param EndTime: 查询结束时间，时间格式：YYYY-MM-DD hh:mm:ss\n        :type EndTime: str\n        :param Limit: 结果返回最大数量，最小值0，最大值100\n        :type Limit: int\n        :param Offset: 返回结果偏移，最小值0\n        :type Offset: int\n        """
        self.FleetId = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetStatisticDetailsResponse(AbstractModel):
    """DescribeFleetStatisticDetails返回参数结构体

    """

    def __init__(self):
        """
        :param DetailList: 服务部署统计详情列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type DetailList: list of FleetStatisticDetail\n        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param TimeType: 统计时间类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DetailList = None
        self.TotalCount = None
        self.TimeType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = FleetStatisticDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.TimeType = params.get("TimeType")
        self.RequestId = params.get("RequestId")


class DescribeFleetStatisticFlowsRequest(AbstractModel):
    """DescribeFleetStatisticFlows请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param BeginTime: 查询开始时间，时间格式：YYYY-MM-DD hh:mm:ss\n        :type BeginTime: str\n        :param EndTime: 查询结束时间，时间格式：YYYY-MM-DD hh:mm:ss\n        :type EndTime: str\n        :param Limit: 结果返回最大数量，最小值0，最大值100\n        :type Limit: int\n        :param Offset: 返回结果偏移，最小值0\n        :type Offset: int\n        """
        self.FleetId = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetStatisticFlowsResponse(AbstractModel):
    """DescribeFleetStatisticFlows返回参数结构体

    """

    def __init__(self):
        """
        :param UsedFlowList: 流量统计列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsedFlowList: list of FleetStatisticFlows\n        :param UsedTimeList: 时长统计列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsedTimeList: list of FleetStatisticTimes\n        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param TimeType: 统计时间类型，取值：小时和天
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.UsedFlowList = None
        self.UsedTimeList = None
        self.TotalCount = None
        self.TimeType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsedFlowList") is not None:
            self.UsedFlowList = []
            for item in params.get("UsedFlowList"):
                obj = FleetStatisticFlows()
                obj._deserialize(item)
                self.UsedFlowList.append(obj)
        if params.get("UsedTimeList") is not None:
            self.UsedTimeList = []
            for item in params.get("UsedTimeList"):
                obj = FleetStatisticTimes()
                obj._deserialize(item)
                self.UsedTimeList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.TimeType = params.get("TimeType")
        self.RequestId = params.get("RequestId")


class DescribeFleetStatisticSummaryRequest(AbstractModel):
    """DescribeFleetStatisticSummary请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param BeginTime: 查询开始时间，时间格式: YYYY-MM-DD hh:mm:ss\n        :type BeginTime: str\n        :param EndTime: 查询结束时间，时间格式: YYYY-MM-DD hh:mm:ss\n        :type EndTime: str\n        """
        self.FleetId = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetStatisticSummaryResponse(AbstractModel):
    """DescribeFleetStatisticSummary返回参数结构体

    """

    def __init__(self):
        """
        :param TotalUsedTimeSeconds: 总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalUsedTimeSeconds: str\n        :param TotalUsedFlowMegaBytes: 总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalUsedFlowMegaBytes: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalUsedTimeSeconds = None
        self.TotalUsedFlowMegaBytes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalUsedTimeSeconds = params.get("TotalUsedTimeSeconds")
        self.TotalUsedFlowMegaBytes = params.get("TotalUsedFlowMegaBytes")
        self.RequestId = params.get("RequestId")


class DescribeFleetUtilizationRequest(AbstractModel):
    """DescribeFleetUtilization请求参数结构体

    """

    def __init__(self):
        """
        :param FleetIds: 服务器舰队 Ids\n        :type FleetIds: list of str\n        """
        self.FleetIds = None


    def _deserialize(self, params):
        self.FleetIds = params.get("FleetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFleetUtilizationResponse(AbstractModel):
    """DescribeFleetUtilization返回参数结构体

    """

    def __init__(self):
        """
        :param FleetUtilization: 服务器舰队利用率
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetUtilization: list of FleetUtilization\n        :param TotalCount: 总数，最小值0\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetUtilization = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FleetUtilization") is not None:
            self.FleetUtilization = []
            for item in params.get("FleetUtilization"):
                obj = FleetUtilization()
                obj._deserialize(item)
                self.FleetUtilization.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID\n        :type AliasId: str\n        :param FleetId: 舰队ID\n        :type FleetId: str\n        :param GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符\n        :type GameServerSessionId: str\n        :param Limit: 单次查询记录数上限\n        :type Limit: int\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type NextToken: str\n        :param StatusFilter: 游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)\n        :type StatusFilter: str\n        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionDetails: 游戏服务器会话详情列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionDetails: list of GameServerSessionDetail\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextToken: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessionDetails = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionDetails") is not None:
            self.GameServerSessionDetails = []
            for item in params.get("GameServerSessionDetails"):
                obj = GameServerSessionDetail()
                obj._deserialize(item)
                self.GameServerSessionDetails.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionPlacementRequest(AbstractModel):
    """DescribeGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 游戏服务器会话放置的唯一标识符\n        :type PlacementId: str\n        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置\n        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionQueuesRequest(AbstractModel):
    """DescribeGameServerSessionQueues请求参数结构体

    """

    def __init__(self):
        """
        :param Names: 游戏服务器会话队列名称数组，单个名字长度1~128\n        :type Names: list of str\n        :param Limit: 结果返回最大数量，最小值0，最大值100\n        :type Limit: int\n        :param Offset: 返回结果偏移，最小值0\n        :type Offset: int\n        :param Filters: 资源过滤字段，可以按照资源名称、资源ID和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（游戏服务器会话队列支持多个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]\n        :type Filters: list of Filter\n        """
        self.Names = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeGameServerSessionQueuesResponse(AbstractModel):
    """DescribeGameServerSessionQueues返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionQueues: 游戏服务器会话队列数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionQueues: list of GameServerSessionQueue\n        :param TotalCount: 游戏服务器会话队列总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessionQueues = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionQueues") is not None:
            self.GameServerSessionQueues = []
            for item in params.get("GameServerSessionQueues"):
                obj = GameServerSessionQueue()
                obj._deserialize(item)
                self.GameServerSessionQueues.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionsRequest(AbstractModel):
    """DescribeGameServerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID\n        :type AliasId: str\n        :param FleetId: 舰队ID\n        :type FleetId: str\n        :param GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符\n        :type GameServerSessionId: str\n        :param Limit: 单次查询记录数上限\n        :type Limit: int\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type NextToken: str\n        :param StatusFilter: 游戏服务器会话状态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)\n        :type StatusFilter: str\n        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessions: 游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessions: list of GameServerSession\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextToken: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeInstanceLimitRequest(AbstractModel):
    """DescribeInstanceLimit请求参数结构体

    """


class DescribeInstanceLimitResponse(AbstractModel):
    """DescribeInstanceLimit返回参数结构体

    """

    def __init__(self):
        """
        :param Limit: 限额\n        :type Limit: int\n        :param ExtraInfos: 详细信息\n        :type ExtraInfos: list of ExtraInfos\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Limit = None
        self.ExtraInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        if params.get("ExtraInfos") is not None:
            self.ExtraInfos = []
            for item in params.get("ExtraInfos"):
                obj = ExtraInfos()
                obj._deserialize(item)
                self.ExtraInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypesRequest(AbstractModel):
    """DescribeInstanceTypes请求参数结构体

    """


class DescribeInstanceTypesResponse(AbstractModel):
    """DescribeInstanceTypes返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceTypeList: 服务器实例类型列表\n        :type InstanceTypeList: list of InstanceTypeInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeList") is not None:
            self.InstanceTypeList = []
            for item in params.get("InstanceTypeList"):
                obj = InstanceTypeInfo()
                obj._deserialize(item)
                self.InstanceTypeList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesExtendRequest(AbstractModel):
    """DescribeInstancesExtend请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param Offset: 返回结果偏移，最小值0\n        :type Offset: int\n        :param Limit: 结果返回最大数量，最小值0，最大值100\n        :type Limit: int\n        :param IpAddress: CVM实例公网IP\n        :type IpAddress: str\n        """
        self.FleetId = None
        self.Offset = None
        self.Limit = None
        self.IpAddress = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IpAddress = params.get("IpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesExtendResponse(AbstractModel):
    """DescribeInstancesExtend返回参数结构体

    """

    def __init__(self):
        """
        :param Instances: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Instances: list of InstanceExtend\n        :param TotalCount: 梳理信息总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Instances = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceExtend()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param InstanceId: CVM实例ID\n        :type InstanceId: str\n        :param Offset: 结果返回最大数量，最小值0，最大值100\n        :type Offset: int\n        :param Limit: 返回结果偏移，最小值0\n        :type Limit: int\n        :param IpAddress: CVM实例公网IP\n        :type IpAddress: str\n        """
        self.FleetId = None
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.IpAddress = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IpAddress = params.get("IpAddress")
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
        :param Instances: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Instances: list of Instance\n        :param TotalCount: 结果返回最大数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Instances = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符\n        :type GameServerSessionId: str\n        :param Limit: 单次查询记录数上限\n        :type Limit: int\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type NextToken: str\n        :param PlayerId: 玩家ID，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type PlayerId: str\n        :param PlayerSessionId: 玩家会话ID，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type PlayerSessionId: str\n        :param PlayerSessionStatusFilter: 玩家会话状态（RESERVED,ACTIVE,COMPLETED,TIMEDOUT）\n        :type PlayerSessionStatusFilter: str\n        """
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.PlayerSessionStatusFilter = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.PlayerSessionStatusFilter = params.get("PlayerSessionStatusFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param PlayerSessions: 玩家会话列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerSessions: list of PlayerSession\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextToken: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PlayerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self.PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self.PlayerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeRuntimeConfigurationRequest(AbstractModel):
    """DescribeRuntimeConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        """
        self.FleetId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuntimeConfigurationResponse(AbstractModel):
    """DescribeRuntimeConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param RuntimeConfiguration: 服务器舰队运行配置信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RuntimeConfiguration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuntimeConfiguration") is not None:
            self.RuntimeConfiguration = RuntimeConfiguration()
            self.RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self.RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param StatusFilter: 状态过滤条件，取值：ACTIVE表示活跃\n        :type StatusFilter: str\n        :param Offset: 返回结果偏移，最小值0\n        :type Offset: int\n        :param Limit: 结果返回最大数量，最小值0，最大值100\n        :type Limit: int\n        """
        self.FleetId = None
        self.StatusFilter = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.StatusFilter = params.get("StatusFilter")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param ScalingPolicies: 动态扩缩容配置策略数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScalingPolicies: list of ScalingPolicy\n        :param TotalCount: 动态扩缩容配置策略总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ScalingPolicies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScalingPolicies") is not None:
            self.ScalingPolicies = []
            for item in params.get("ScalingPolicies"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self.ScalingPolicies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTimerScalingPoliciesRequest(AbstractModel):
    """DescribeTimerScalingPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 扩缩容配置服务器舰队ID\n        :type FleetId: str\n        :param TimerName: 定时器名称\n        :type TimerName: str\n        :param BeginTime: 定时器开始时间\n        :type BeginTime: str\n        :param EndTime: 定时器结束时间\n        :type EndTime: str\n        :param Offset: 分页偏移量\n        :type Offset: int\n        :param Limit: 页大小\n        :type Limit: int\n        """
        self.FleetId = None
        self.TimerName = None
        self.BeginTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.TimerName = params.get("TimerName")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimerScalingPoliciesResponse(AbstractModel):
    """DescribeTimerScalingPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param TimerScalingPolicies: 定时器扩缩容策略配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerScalingPolicies: list of TimerScalingPolicy\n        :param TotalCount: 定时器总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TimerScalingPolicies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TimerScalingPolicies") is not None:
            self.TimerScalingPolicies = []
            for item in params.get("TimerScalingPolicies"):
                obj = TimerScalingPolicy()
                obj._deserialize(item)
                self.TimerScalingPolicies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUserQuotaRequest(AbstractModel):
    """DescribeUserQuota请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型\n        :type ResourceType: int\n        """
        self.ResourceType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserQuotaResponse(AbstractModel):
    """DescribeUserQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaResource: 配额资源信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type QuotaResource: :class:`tencentcloud.gse.v20191112.models.QuotaResource`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.QuotaResource = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaResource") is not None:
            self.QuotaResource = QuotaResource()
            self.QuotaResource._deserialize(params.get("QuotaResource"))
        self.RequestId = params.get("RequestId")


class DescribeUserQuotasRequest(AbstractModel):
    """DescribeUserQuotas请求参数结构体

    """


class DescribeUserQuotasResponse(AbstractModel):
    """DescribeUserQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaResource: 配额信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type QuotaResource: list of QuotaResource\n        :param Total: 配额信息列表总数，最小值0\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.QuotaResource = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaResource") is not None:
            self.QuotaResource = []
            for item in params.get("QuotaResource"):
                obj = QuotaResource()
                obj._deserialize(item)
                self.QuotaResource.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DesiredPlayerSession(AbstractModel):
    """玩家游戏会话信息

    """

    def __init__(self):
        """
        :param PlayerId: 与玩家会话关联的唯一玩家标识\n        :type PlayerId: str\n        :param PlayerData: 开发人员定义的玩家数据\n        :type PlayerData: str\n        """
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesRequest(AbstractModel):
    """DetachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        """
        self.FleetId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesResponse(AbstractModel):
    """DetachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """磁盘存储信息

    """

    def __init__(self):
        """
        :param DiskType: 磁盘类型，支持：高性能云硬盘（CLOUD_PREMIUM）、SSD云硬盘（CLOUD_SSD）\n        :type DiskType: str\n        :param DiskSize: 系统盘：可选硬盘容量，50-500GB，数字以1为单位，数据盘：可选硬盘容量：10-32000GB，数字以10为单位；当磁盘类型为SSD云硬盘（CLOUD_SSD）最小大小为 100GB\n        :type DiskSize: int\n        """
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
        


class EndGameServerSessionAndProcessRequest(AbstractModel):
    """EndGameServerSessionAndProcess请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID，如果传入游戏服务器会话ID，结束对应进程以及游戏服务器会话和玩家会话。\n        :type GameServerSessionId: str\n        :param IpAddress: CVM的公网IP地址，需同时传入IpAddress和Port，结束IpAddress和Port对应的进程以及游戏服务器会话（如果存在）和玩家会话（如果存在），单独传入IpAddress不生效。\n        :type IpAddress: str\n        :param Port: 端口号，取值范围1025-60000，需同时传入IpAddress和Port，结束IpAddress和Port对应的进程以及游戏服务器会话（如果存在）和玩家会话（如果存在），单独传入Port不生效。\n        :type Port: int\n        """
        self.GameServerSessionId = None
        self.IpAddress = None
        self.Port = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndGameServerSessionAndProcessResponse(AbstractModel):
    """EndGameServerSessionAndProcess返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Event(AbstractModel):
    """事件对象

    """

    def __init__(self):
        """
        :param EventCode: 事件代码，支持以下的事件代码

- FLEET_CREATED 
- FLEET_STATE_DOWNLOADING 
- FLEET_BINARY_DOWNLOAD_FAILED 
- FLEET_CREATION_EXTRACTING_BUILD
- FLEET_CREATION_VALIDATING_RUNTIME_CONFIG
- FLEET_STATE_VALIDATING
- FLEET_STATE_BUILDING 
- FLEET_STATE_ACTIVATING
- FLEET_STATE_ACTIVE
- FLEET_SCALING_EVENT
- FLEET_STATE_ERROR
- FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND
- FLEET_ACTIVATION_FAILED_NO_INSTANCES
- FLEET_VPC_PEERING_SUCCEEDED
- FLEET_VPC_PEERING_FAILED
- FLEET_VPC_PEERING_DELETE
- FLEET_INITIALIZATION_FAILED
- FLEET_DELETED
- FLEET_STATE_DELETING
- FLEET_ACTIVATION_FAILED
- GAME_SESSION_ACTIVATION_TIMEOUT\n        :type EventCode: str\n        :param EventId: 事件的唯一标识 ID\n        :type EventId: str\n        :param EventTime: 事件的发生时间，UTC 时间格式\n        :type EventTime: str\n        :param Message: 事件的消息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        :param PreSignedLogUrl: 事件相关的日志存储路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type PreSignedLogUrl: str\n        :param ResourceId: 事件对应的资源对象唯一标识 ID，例如服务器舰队 ID\n        :type ResourceId: str\n        """
        self.EventCode = None
        self.EventId = None
        self.EventTime = None
        self.Message = None
        self.PreSignedLogUrl = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.EventCode = params.get("EventCode")
        self.EventId = params.get("EventId")
        self.EventTime = params.get("EventTime")
        self.Message = params.get("Message")
        self.PreSignedLogUrl = params.get("PreSignedLogUrl")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraInfos(AbstractModel):
    """实例类型限额配置额外信息

    """

    def __init__(self):
        """
        :param InstanceType: 实例类型，例如S5.LARGE8
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param TotalInstances: 实例限额数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalInstances: int\n        """
        self.InstanceType = None
        self.TotalInstances = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.TotalInstances = params.get("TotalInstances")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤字段内容

    """

    def __init__(self):
        """
        :param Key: 过滤属性的 key\n        :type Key: str\n        :param Values: 过滤属性的 values 值\n        :type Values: list of str\n        """
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
        


class FleetAttributes(AbstractModel):
    """服务部署属性

    """

    def __init__(self):
        """
        :param AssetId: 生成包 Id\n        :type AssetId: str\n        :param CreationTime: 创建服务器舰队时间\n        :type CreationTime: str\n        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param FleetArn: 服务器舰队资源描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetArn: str\n        :param FleetId: 服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param FleetType: 服务器舰队类型，目前只支持ON_DEMAND
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetType: str\n        :param InstanceType: 服务器类型，例如S5.LARGE8
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param Name: 服务器舰队名称\n        :type Name: str\n        :param NewGameServerSessionProtectionPolicy: 游戏会话保护策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type NewGameServerSessionProtectionPolicy: str\n        :param OperatingSystem: 操作系统类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type OperatingSystem: str\n        :param ResourceCreationLimitPolicy: 资源创建限制策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`\n        :param Status: 状态：新建、下载中、验证中、生成中、激活中、活跃、异常、删除中、结束
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param StoppedActions: 服务器舰队停止状态，为空时表示自动扩缩容
注意：此字段可能返回 null，表示取不到有效值。\n        :type StoppedActions: list of str\n        :param TerminationTime: 服务器舰队终止时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TerminationTime: str\n        :param GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionProtectionTimeLimit: int\n        :param BillingStatus: 计费状态：未开通、已开通、异常、欠费隔离、销毁、解冻
注意：此字段可能返回 null，表示取不到有效值。\n        :type BillingStatus: str\n        :param Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param DataDiskInfo: 数据盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-32000GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，10-32000GB；容量以10为单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataDiskInfo: list of DiskInfo\n        :param SystemDiskInfo: 系统盘，储存类型为 SSD 云硬盘（CLOUD_SSD）时，100-500GB；储存类型为高性能云硬盘（CLOUD_PREMIUM）时，50-500GB；容量以1为单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type SystemDiskInfo: :class:`tencentcloud.gse.v20191112.models.DiskInfo`\n        :param RelatedCcnInfos: 云联网相关信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelatedCcnInfos: list of RelatedCcnInfo\n        :param InternetMaxBandwidthOut: fleet公网出带宽最大值，默认100Mbps，范围1-200Mbps
注意：此字段可能返回 null，表示取不到有效值。\n        :type InternetMaxBandwidthOut: int\n        """
        self.AssetId = None
        self.CreationTime = None
        self.Description = None
        self.FleetArn = None
        self.FleetId = None
        self.FleetType = None
        self.InstanceType = None
        self.Name = None
        self.NewGameServerSessionProtectionPolicy = None
        self.OperatingSystem = None
        self.ResourceCreationLimitPolicy = None
        self.Status = None
        self.StoppedActions = None
        self.TerminationTime = None
        self.GameServerSessionProtectionTimeLimit = None
        self.BillingStatus = None
        self.Tags = None
        self.DataDiskInfo = None
        self.SystemDiskInfo = None
        self.RelatedCcnInfos = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.CreationTime = params.get("CreationTime")
        self.Description = params.get("Description")
        self.FleetArn = params.get("FleetArn")
        self.FleetId = params.get("FleetId")
        self.FleetType = params.get("FleetType")
        self.InstanceType = params.get("InstanceType")
        self.Name = params.get("Name")
        self.NewGameServerSessionProtectionPolicy = params.get("NewGameServerSessionProtectionPolicy")
        self.OperatingSystem = params.get("OperatingSystem")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self.ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self.ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        self.Status = params.get("Status")
        self.StoppedActions = params.get("StoppedActions")
        self.TerminationTime = params.get("TerminationTime")
        self.GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        self.BillingStatus = params.get("BillingStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("DataDiskInfo") is not None:
            self.DataDiskInfo = []
            for item in params.get("DataDiskInfo"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDiskInfo.append(obj)
        if params.get("SystemDiskInfo") is not None:
            self.SystemDiskInfo = DiskInfo()
            self.SystemDiskInfo._deserialize(params.get("SystemDiskInfo"))
        if params.get("RelatedCcnInfos") is not None:
            self.RelatedCcnInfos = []
            for item in params.get("RelatedCcnInfos"):
                obj = RelatedCcnInfo()
                obj._deserialize(item)
                self.RelatedCcnInfos.append(obj)
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetCapacity(AbstractModel):
    """服务部署组容量配置

    """

    def __init__(self):
        """
        :param FleetId: 服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param InstanceType: 服务器类型，如S3.LARGE8,S2.LARGE8,S5.LARGE8等
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param InstanceCounts: 服务器实例统计数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCounts: :class:`tencentcloud.gse.v20191112.models.InstanceCounts`\n        :param ScalingInterval: 服务器伸缩容间隔，单位分钟，最小值3，最大值30，默认值10
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScalingInterval: int\n        """
        self.FleetId = None
        self.InstanceType = None
        self.InstanceCounts = None
        self.ScalingInterval = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceType = params.get("InstanceType")
        if params.get("InstanceCounts") is not None:
            self.InstanceCounts = InstanceCounts()
            self.InstanceCounts._deserialize(params.get("InstanceCounts"))
        self.ScalingInterval = params.get("ScalingInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetRelatedResource(AbstractModel):
    """与服务器舰队关联的资源，如别名和队列

    """

    def __init__(self):
        """
        :param Type: 资源类型。
- ALIAS：别名
- QUEUE：队列
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param ResourceId: 资源ID，目前仅支持别名ID和队列名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceId: str\n        :param ResourceRegion: 资源所在区域，如ap-shanghai、na-siliconvalley等
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceRegion: str\n        """
        self.Type = None
        self.ResourceId = None
        self.ResourceRegion = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ResourceId = params.get("ResourceId")
        self.ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetStatisticDetail(AbstractModel):
    """舰队统计详情

    """

    def __init__(self):
        """
        :param FleetId: 舰队ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param InstanceIP: 实例IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceIP: str\n        :param BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type BeginTime: str\n        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        :param TotalUsedTimeSeconds: 总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalUsedTimeSeconds: str\n        :param TotalUsedFlowMegaBytes: 总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalUsedFlowMegaBytes: float\n        """
        self.FleetId = None
        self.InstanceId = None
        self.InstanceIP = None
        self.BeginTime = None
        self.EndTime = None
        self.TotalUsedTimeSeconds = None
        self.TotalUsedFlowMegaBytes = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceIP = params.get("InstanceIP")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TotalUsedTimeSeconds = params.get("TotalUsedTimeSeconds")
        self.TotalUsedFlowMegaBytes = params.get("TotalUsedFlowMegaBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetStatisticFlows(AbstractModel):
    """舰队统计流量

    """

    def __init__(self):
        """
        :param TotalUsedFlowMegaBytes: 总流量，单位MB
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalUsedFlowMegaBytes: float\n        :param BeginTime: 统计开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type BeginTime: str\n        """
        self.TotalUsedFlowMegaBytes = None
        self.BeginTime = None


    def _deserialize(self, params):
        self.TotalUsedFlowMegaBytes = params.get("TotalUsedFlowMegaBytes")
        self.BeginTime = params.get("BeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetStatisticTimes(AbstractModel):
    """舰队统计总时长

    """

    def __init__(self):
        """
        :param BeginTime: 统计开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type BeginTime: str\n        :param TotalUsedTimeSeconds: 统计总时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalUsedTimeSeconds: str\n        """
        self.BeginTime = None
        self.TotalUsedTimeSeconds = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.TotalUsedTimeSeconds = params.get("TotalUsedTimeSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FleetUtilization(AbstractModel):
    """服务部署利用率

    """

    def __init__(self):
        """
        :param ActiveGameServerSessionCount: 游戏会话数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActiveGameServerSessionCount: int\n        :param ActiveServerProcessCount: 活跃进程数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActiveServerProcessCount: int\n        :param CurrentPlayerSessionCount: 当前游戏玩家数
注意：此字段可能返回 null，表示取不到有效值。\n        :type CurrentPlayerSessionCount: int\n        :param FleetId: 服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param MaximumPlayerSessionCount: 最大玩家会话数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaximumPlayerSessionCount: int\n        """
        self.ActiveGameServerSessionCount = None
        self.ActiveServerProcessCount = None
        self.CurrentPlayerSessionCount = None
        self.FleetId = None
        self.MaximumPlayerSessionCount = None


    def _deserialize(self, params):
        self.ActiveGameServerSessionCount = params.get("ActiveGameServerSessionCount")
        self.ActiveServerProcessCount = params.get("ActiveServerProcessCount")
        self.CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self.FleetId = params.get("FleetId")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameProperty(AbstractModel):
    """游戏属性详情

    """

    def __init__(self):
        """
        :param Key: 属性名称，最大长度不超过32个ASCII字符\n        :type Key: str\n        :param Value: 属性值，最大长度不超过96个ASCII字符\n        :type Value: str\n        """
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
        


class GameServerSession(AbstractModel):
    """游戏会话详情

    """

    def __init__(self):
        """
        :param CreationTime: 游戏服务器会话创建时间\n        :type CreationTime: str\n        :param CreatorId: 创建者ID，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatorId: str\n        :param CurrentPlayerSessionCount: 当前玩家数量，最小值不小于0\n        :type CurrentPlayerSessionCount: int\n        :param DnsName: CVM的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。\n        :type DnsName: str\n        :param FleetId: 舰队ID\n        :type FleetId: str\n        :param GameProperties: 游戏属性，最大长度不超过16组
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameProperties: list of GameProperty\n        :param GameServerSessionData: 游戏服务器会话属性详情，最大长度不超过4096个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionData: str\n        :param GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符\n        :type GameServerSessionId: str\n        :param IpAddress: CVM IP地址\n        :type IpAddress: str\n        :param MatchmakerData: 对战进程详情，最大长度不超过400000个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchmakerData: str\n        :param MaximumPlayerSessionCount: 最大玩家数量，最小值不小于0\n        :type MaximumPlayerSessionCount: int\n        :param Name: 游戏服务器会话名称，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param PlayerSessionCreationPolicy: 玩家会话创建策略（ACCEPT_ALL,DENY_ALL）
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerSessionCreationPolicy: str\n        :param Port: 端口号，最小值不小于1，最大值不超过60000\n        :type Port: int\n        :param Status: 游戏服务器会话状态（ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR）\n        :type Status: str\n        :param StatusReason: 游戏服务器会话状态附加信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusReason: str\n        :param TerminationTime: 终止的时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TerminationTime: str\n        :param InstanceType: 实例类型，最大长度不超过128个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param CurrentCustomCount: 当前自定义数
注意：此字段可能返回 null，表示取不到有效值。\n        :type CurrentCustomCount: int\n        :param MaxCustomCount: 最大自定义数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxCustomCount: int\n        :param Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param AvailabilityStatus: 会话可用性状态，是否被屏蔽（Enable,Disable）
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvailabilityStatus: str\n        """
        self.CreationTime = None
        self.CreatorId = None
        self.CurrentPlayerSessionCount = None
        self.DnsName = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.MatchmakerData = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.Port = None
        self.Status = None
        self.StatusReason = None
        self.TerminationTime = None
        self.InstanceType = None
        self.CurrentCustomCount = None
        self.MaxCustomCount = None
        self.Weight = None
        self.AvailabilityStatus = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreatorId = params.get("CreatorId")
        self.CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.MatchmakerData = params.get("MatchmakerData")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.StatusReason = params.get("StatusReason")
        self.TerminationTime = params.get("TerminationTime")
        self.InstanceType = params.get("InstanceType")
        self.CurrentCustomCount = params.get("CurrentCustomCount")
        self.MaxCustomCount = params.get("MaxCustomCount")
        self.Weight = params.get("Weight")
        self.AvailabilityStatus = params.get("AvailabilityStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionDetail(AbstractModel):
    """游戏服务器会话详情（GameServerSessionDetail）

    """

    def __init__(self):
        """
        :param GameServerSession: 游戏服务器会话\n        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`\n        :param ProtectionPolicy: 保护策略，可选（NoProtection,FullProtection）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProtectionPolicy: str\n        """
        self.GameServerSession = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionPlacement(AbstractModel):
    """游戏会话部署对象

    """

    def __init__(self):
        """
        :param PlacementId: 部署Id\n        :type PlacementId: str\n        :param GameServerSessionQueueName: 服务部署组名称\n        :type GameServerSessionQueueName: str\n        :param PlayerLatencies: 玩家延迟
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerLatencies: list of PlayerLatency\n        :param Status: 服务部署状态\n        :type Status: str\n        :param DnsName: 分配给正在运行游戏会话的实例的DNS标识符
注意：此字段可能返回 null，表示取不到有效值。\n        :type DnsName: str\n        :param GameServerSessionId: 游戏会话Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionId: str\n        :param GameServerSessionName: 游戏会话名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionName: str\n        :param GameServerSessionRegion: 服务部署区域
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionRegion: str\n        :param GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameProperties: list of GameProperty\n        :param MaximumPlayerSessionCount: 游戏服务器允许同时连接到游戏会话的最大玩家数量，最小值1，最大值为玩家会话最大限额\n        :type MaximumPlayerSessionCount: int\n        :param GameServerSessionData: 游戏会话数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessionData: str\n        :param IpAddress: 运行游戏会话的实例的IP地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpAddress: str\n        :param Port: 运行游戏会话的实例的端口号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param MatchmakerData: 游戏匹配数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchmakerData: str\n        :param PlacedPlayerSessions: 部署的玩家游戏数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlacedPlayerSessions: list of PlacedPlayerSession\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.PlayerLatencies = None
        self.Status = None
        self.DnsName = None
        self.GameServerSessionId = None
        self.GameServerSessionName = None
        self.GameServerSessionRegion = None
        self.GameProperties = None
        self.MaximumPlayerSessionCount = None
        self.GameServerSessionData = None
        self.IpAddress = None
        self.Port = None
        self.MatchmakerData = None
        self.PlacedPlayerSessions = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)
        self.Status = params.get("Status")
        self.DnsName = params.get("DnsName")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.GameServerSessionName = params.get("GameServerSessionName")
        self.GameServerSessionRegion = params.get("GameServerSessionRegion")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.IpAddress = params.get("IpAddress")
        self.Port = params.get("Port")
        self.MatchmakerData = params.get("MatchmakerData")
        if params.get("PlacedPlayerSessions") is not None:
            self.PlacedPlayerSessions = []
            for item in params.get("PlacedPlayerSessions"):
                obj = PlacedPlayerSession()
                obj._deserialize(item)
                self.PlacedPlayerSessions.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GameServerSessionQueue(AbstractModel):
    """服务部署组对象

    """

    def __init__(self):
        """
        :param Name: 服务部署组名字\n        :type Name: str\n        :param GameServerSessionQueueArn: 服务部署组资源\n        :type GameServerSessionQueueArn: str\n        :param Destinations: 目的fleet（可为别名）列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Destinations: list of GameServerSessionQueueDestination\n        :param PlayerLatencyPolicies: 延迟策略集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerLatencyPolicies: list of PlayerLatencyPolicy\n        :param TimeoutInSeconds: 超时时间\n        :type TimeoutInSeconds: int\n        :param Tags: 标签列表，最大长度50组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        """
        self.Name = None
        self.GameServerSessionQueueArn = None
        self.Destinations = None
        self.PlayerLatencyPolicies = None
        self.TimeoutInSeconds = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.GameServerSessionQueueArn = params.get("GameServerSessionQueueArn")
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = GameServerSessionQueueDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        if params.get("PlayerLatencyPolicies") is not None:
            self.PlayerLatencyPolicies = []
            for item in params.get("PlayerLatencyPolicies"):
                obj = PlayerLatencyPolicy()
                obj._deserialize(item)
                self.PlayerLatencyPolicies.append(obj)
        self.TimeoutInSeconds = params.get("TimeoutInSeconds")
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
        


class GameServerSessionQueueDestination(AbstractModel):
    """服务部署组目的集合

    """

    def __init__(self):
        """
        :param DestinationArn: 服务部署组目的的资源描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type DestinationArn: str\n        :param FleetStatus: 服务部署组目的的状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetStatus: str\n        """
        self.DestinationArn = None
        self.FleetStatus = None


    def _deserialize(self, params):
        self.DestinationArn = params.get("DestinationArn")
        self.FleetStatus = params.get("FleetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerInstanceLogUrlRequest(AbstractModel):
    """GetGameServerInstanceLogUrl请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 游戏舰队ID\n        :type FleetId: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param ServerIp: 实例IP\n        :type ServerIp: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Size: 每次条数\n        :type Size: int\n        """
        self.FleetId = None
        self.InstanceId = None
        self.ServerIp = None
        self.Offset = None
        self.Size = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.ServerIp = params.get("ServerIp")
        self.Offset = params.get("Offset")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerInstanceLogUrlResponse(AbstractModel):
    """GetGameServerInstanceLogUrl返回参数结构体

    """

    def __init__(self):
        """
        :param PresignedUrls: 日志下载URL的数组，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type PresignedUrls: list of str\n        :param Total: 总条数\n        :type Total: int\n        :param HasNext: 是否还有没拉取完的\n        :type HasNext: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PresignedUrls = None
        self.Total = None
        self.HasNext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PresignedUrls = params.get("PresignedUrls")
        self.Total = params.get("Total")
        self.HasNext = params.get("HasNext")
        self.RequestId = params.get("RequestId")


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID，最小长度不小于1个ASCII字符，最大长度不超过48个ASCII字符\n        :type GameServerSessionId: str\n        """
        self.GameServerSessionId = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl返回参数结构体

    """

    def __init__(self):
        """
        :param PreSignedUrl: 日志下载URL，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type PreSignedUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PreSignedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedUrl = params.get("PreSignedUrl")
        self.RequestId = params.get("RequestId")


class GetInstanceAccessRequest(AbstractModel):
    """GetInstanceAccess请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param InstanceId: 实例Id\n        :type InstanceId: str\n        """
        self.FleetId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetInstanceAccessResponse(AbstractModel):
    """GetInstanceAccess返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceAccess: 实例登录所需要的凭据\n        :type InstanceAccess: :class:`tencentcloud.gse.v20191112.models.InstanceAccess`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceAccess") is not None:
            self.InstanceAccess = InstanceAccess()
            self.InstanceAccess._deserialize(params.get("InstanceAccess"))
        self.RequestId = params.get("RequestId")


class GetUploadCredentialsRequest(AbstractModel):
    """GetUploadCredentials请求参数结构体

    """

    def __init__(self):
        """
        :param AssetRegion: 生成包所在地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1165/42053#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)\n        :type AssetRegion: str\n        :param BucketKey: 生成包的ZIP包名，例如：server.zip\n        :type BucketKey: str\n        """
        self.AssetRegion = None
        self.BucketKey = None


    def _deserialize(self, params):
        self.AssetRegion = params.get("AssetRegion")
        self.BucketKey = params.get("BucketKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUploadCredentialsResponse(AbstractModel):
    """GetUploadCredentials返回参数结构体

    """

    def __init__(self):
        """
        :param BucketAuth: 上传文件授权信息Auth\n        :type BucketAuth: str\n        :param BucketName: Bucket名字\n        :type BucketName: str\n        :param AssetRegion: 生成包所在地域\n        :type AssetRegion: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BucketAuth = None
        self.BucketName = None
        self.AssetRegion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BucketAuth = params.get("BucketAuth")
        self.BucketName = params.get("BucketName")
        self.AssetRegion = params.get("AssetRegion")
        self.RequestId = params.get("RequestId")


class GetUploadFederationTokenRequest(AbstractModel):
    """GetUploadFederationToken请求参数结构体

    """


class GetUploadFederationTokenResponse(AbstractModel):
    """GetUploadFederationToken返回参数结构体

    """

    def __init__(self):
        """
        :param ExpiredTime: 临时证书的过期时间，Unix 时间戳，精确到秒\n        :type ExpiredTime: int\n        :param AssetCredentials: 临时证书\n        :type AssetCredentials: :class:`tencentcloud.gse.v20191112.models.AssetCredentials`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ExpiredTime = None
        self.AssetCredentials = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExpiredTime = params.get("ExpiredTime")
        if params.get("AssetCredentials") is not None:
            self.AssetCredentials = AssetCredentials()
            self.AssetCredentials._deserialize(params.get("AssetCredentials"))
        self.RequestId = params.get("RequestId")


class InboundPermission(AbstractModel):
    """允许网络访问范围

    """

    def __init__(self):
        """
        :param FromPort: 起始端口号，最小值1025\n        :type FromPort: int\n        :param IpRange: IP 段范围，合法的 CIDR 地址类型，如所有IPv4来源：0.0.0.0/0\n        :type IpRange: str\n        :param Protocol: 协议类型：TCP或者UDP\n        :type Protocol: str\n        :param ToPort: 终止端口号，最大值60000\n        :type ToPort: int\n        """
        self.FromPort = None
        self.IpRange = None
        self.Protocol = None
        self.ToPort = None


    def _deserialize(self, params):
        self.FromPort = params.get("FromPort")
        self.IpRange = params.get("IpRange")
        self.Protocol = params.get("Protocol")
        self.ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InboundPermissionAuthorization(AbstractModel):
    """用于新增安全组

    """

    def __init__(self):
        """
        :param FromPort: 起始端口号\n        :type FromPort: int\n        :param IpRange: IP 端范围，CIDR方式划分\n        :type IpRange: str\n        :param Protocol: 协议类型\n        :type Protocol: str\n        :param ToPort: 终止端口号\n        :type ToPort: int\n        """
        self.FromPort = None
        self.IpRange = None
        self.Protocol = None
        self.ToPort = None


    def _deserialize(self, params):
        self.FromPort = params.get("FromPort")
        self.IpRange = params.get("IpRange")
        self.Protocol = params.get("Protocol")
        self.ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InboundPermissionRevocations(AbstractModel):
    """需要移除的安全组

    """

    def __init__(self):
        """
        :param FromPort: 起始端口号\n        :type FromPort: int\n        :param IpRange: IP 端范围，CIDR 方式换分\n        :type IpRange: str\n        :param Protocol: 协议类型：UDP或者TCP\n        :type Protocol: str\n        :param ToPort: 终止端口号\n        :type ToPort: int\n        """
        self.FromPort = None
        self.IpRange = None
        self.Protocol = None
        self.ToPort = None


    def _deserialize(self, params):
        self.FromPort = params.get("FromPort")
        self.IpRange = params.get("IpRange")
        self.Protocol = params.get("Protocol")
        self.ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param IpAddress: IP地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpAddress: str\n        :param DnsName: dns
注意：此字段可能返回 null，表示取不到有效值。\n        :type DnsName: str\n        :param OperatingSystem: 操作系统
注意：此字段可能返回 null，表示取不到有效值。\n        :type OperatingSystem: str\n        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Weight: 实例权重
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param ReserveValue: 实例是否保留, 1-保留，0-不保留,默认
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReserveValue: int\n        :param PrivateIpAddress: 实例的私有IP地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIpAddress: str\n        """
        self.FleetId = None
        self.InstanceId = None
        self.IpAddress = None
        self.DnsName = None
        self.OperatingSystem = None
        self.Status = None
        self.Type = None
        self.CreateTime = None
        self.Weight = None
        self.ReserveValue = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.IpAddress = params.get("IpAddress")
        self.DnsName = params.get("DnsName")
        self.OperatingSystem = params.get("OperatingSystem")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.Weight = params.get("Weight")
        self.ReserveValue = params.get("ReserveValue")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAccess(AbstractModel):
    """实例访问凭证信息

    """

    def __init__(self):
        """
        :param Credentials: 访问实例所需要的凭据\n        :type Credentials: :class:`tencentcloud.gse.v20191112.models.Credentials`\n        :param FleetId: 服务部署Id\n        :type FleetId: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param IpAddress: 实例公网IP\n        :type IpAddress: str\n        :param OperatingSystem: 操作系统\n        :type OperatingSystem: str\n        """
        self.Credentials = None
        self.FleetId = None
        self.InstanceId = None
        self.IpAddress = None
        self.OperatingSystem = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.IpAddress = params.get("IpAddress")
        self.OperatingSystem = params.get("OperatingSystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceCounts(AbstractModel):
    """服务器实例统计数据

    """

    def __init__(self):
        """
        :param Active: 活跃的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Active: int\n        :param Desired: 期望的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Desired: int\n        :param Idle: 空闲的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Idle: int\n        :param MaxiNum: 服务器实例数最大限制
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxiNum: int\n        :param MiniNum: 服务器实例数最小限制
注意：此字段可能返回 null，表示取不到有效值。\n        :type MiniNum: int\n        :param Pending: 已开始创建，但未激活的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Pending: int\n        :param Terminating: 结束中的服务器实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Terminating: int\n        """
        self.Active = None
        self.Desired = None
        self.Idle = None
        self.MaxiNum = None
        self.MiniNum = None
        self.Pending = None
        self.Terminating = None


    def _deserialize(self, params):
        self.Active = params.get("Active")
        self.Desired = params.get("Desired")
        self.Idle = params.get("Idle")
        self.MaxiNum = params.get("MaxiNum")
        self.MiniNum = params.get("MiniNum")
        self.Pending = params.get("Pending")
        self.Terminating = params.get("Terminating")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtend(AbstractModel):
    """实例扩展信息

    """

    def __init__(self):
        """
        :param Instance: 实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Instance: :class:`tencentcloud.gse.v20191112.models.Instance`\n        :param State: 实例状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type State: str\n        :param HealthyProcessCnt: 健康进程数
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthyProcessCnt: int\n        :param ActiveProcessCnt: 活跃进程数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActiveProcessCnt: int\n        :param GameSessionCnt: 当前游戏会话总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameSessionCnt: int\n        :param MaxGameSessionCnt: 最大游戏会话数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxGameSessionCnt: int\n        :param PlayerSessionCnt: 当前玩家会话数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerSessionCnt: int\n        :param MaxPlayerSessionCnt: 最大玩家会话数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxPlayerSessionCnt: int\n        """
        self.Instance = None
        self.State = None
        self.HealthyProcessCnt = None
        self.ActiveProcessCnt = None
        self.GameSessionCnt = None
        self.MaxGameSessionCnt = None
        self.PlayerSessionCnt = None
        self.MaxPlayerSessionCnt = None


    def _deserialize(self, params):
        if params.get("Instance") is not None:
            self.Instance = Instance()
            self.Instance._deserialize(params.get("Instance"))
        self.State = params.get("State")
        self.HealthyProcessCnt = params.get("HealthyProcessCnt")
        self.ActiveProcessCnt = params.get("ActiveProcessCnt")
        self.GameSessionCnt = params.get("GameSessionCnt")
        self.MaxGameSessionCnt = params.get("MaxGameSessionCnt")
        self.PlayerSessionCnt = params.get("PlayerSessionCnt")
        self.MaxPlayerSessionCnt = params.get("MaxPlayerSessionCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeInfo(AbstractModel):
    """服务器实例类型信息

    """

    def __init__(self):
        """
        :param TypeName: 类型名，例如“标准型SA1”\n        :type TypeName: str\n        :param InstanceType: 类型，例如"SA1.SMALL1"\n        :type InstanceType: str\n        :param Cpu: CPU，例如1核就是1\n        :type Cpu: int\n        :param Memory: 内存，例如2G就是2\n        :type Memory: int\n        :param NetworkCard: 网络收到包,例如25万PPS就是25\n        :type NetworkCard: int\n        """
        self.TypeName = None
        self.InstanceType = None
        self.Cpu = None
        self.Memory = None
        self.NetworkCard = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.InstanceType = params.get("InstanceType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.NetworkCard = params.get("NetworkCard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchRequest(AbstractModel):
    """JoinGameServerSessionBatch请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符\n        :type GameServerSessionId: str\n        :param PlayerIds: 玩家ID列表，最小1组，最大25组\n        :type PlayerIds: list of str\n        :param PlayerDataMap: 玩家自定义数据\n        :type PlayerDataMap: :class:`tencentcloud.gse.v20191112.models.PlayerDataMap`\n        """
        self.GameServerSessionId = None
        self.PlayerIds = None
        self.PlayerDataMap = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerIds = params.get("PlayerIds")
        if params.get("PlayerDataMap") is not None:
            self.PlayerDataMap = PlayerDataMap()
            self.PlayerDataMap._deserialize(params.get("PlayerDataMap"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionBatchResponse(AbstractModel):
    """JoinGameServerSessionBatch返回参数结构体

    """

    def __init__(self):
        """
        :param PlayerSessions: 玩家会话列表，最大25组
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerSessions: list of PlayerSession\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PlayerSessions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self.PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self.PlayerSessions.append(obj)
        self.RequestId = params.get("RequestId")


class JoinGameServerSessionRequest(AbstractModel):
    """JoinGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符\n        :type GameServerSessionId: str\n        :param PlayerId: 玩家ID，最大长度1024个ASCII字符\n        :type PlayerId: str\n        :param PlayerData: 玩家自定义数据，最大长度2048个ASCII字符\n        :type PlayerData: str\n        """
        self.GameServerSessionId = None
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param PlayerSession: 玩家会话
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerSession: :class:`tencentcloud.gse.v20191112.models.PlayerSession`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PlayerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSession") is not None:
            self.PlayerSession = PlayerSession()
            self.PlayerSession._deserialize(params.get("PlayerSession"))
        self.RequestId = params.get("RequestId")


class ListAliasesRequest(AbstractModel):
    """ListAliases请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 名字，长度不小于1字符不超过1024字符\n        :type Name: str\n        :param RoutingStrategyType: 路由策略类型，有效值常规别名(SIMPLE)、终止别名(TERMINAL)\n        :type RoutingStrategyType: str\n        :param Limit: 要返回的最大结果数，最小值1\n        :type Limit: int\n        :param Offset: 偏移，默认0\n        :type Offset: int\n        :param OrderBy: 排序字段，例如CreationTime\n        :type OrderBy: str\n        :param OrderWay: 排序方式，有效值asc|desc\n        :type OrderWay: str\n        :param Filters: 资源过滤字段，可以按照资源名称和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（舰队当前仅支持单个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]\n        :type Filters: list of Filter\n        """
        self.Name = None
        self.RoutingStrategyType = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderWay = None
        self.Filters = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RoutingStrategyType = params.get("RoutingStrategyType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderWay = params.get("OrderWay")
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
        


class ListAliasesResponse(AbstractModel):
    """ListAliases返回参数结构体

    """

    def __init__(self):
        """
        :param Aliases: 别名对象数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Aliases: list of Alias\n        :param TotalCount: 总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Aliases = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Aliases") is not None:
            self.Aliases = []
            for item in params.get("Aliases"):
                obj = Alias()
                obj._deserialize(item)
                self.Aliases.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListFleetsRequest(AbstractModel):
    """ListFleets请求参数结构体

    """

    def __init__(self):
        """
        :param AssetId: 生成包 Id\n        :type AssetId: str\n        :param Limit: 结果返回最大值，暂未使用\n        :type Limit: int\n        :param Offset: 结果返回偏移，暂未使用\n        :type Offset: int\n        :param Filters: 资源过滤字段，可以按照资源名称和标签进行过滤- 资源名称过滤    - Key: 固定字符串 "resource:name"    - Values: 资源名称数组（当前仅支持单个名称的过滤）- 标签过滤    - 通过标签键过滤        - Key: 固定字符串 "tag:key"        - Values 不传    - 通过标签键值过滤        - Key: 固定字符串 "tag:key-value"        - Values: 标签键值对数组，例如 ["key1:value1", "key1:value2", "key2:value2"]\n        :type Filters: list of Filter\n        """
        self.AssetId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class ListFleetsResponse(AbstractModel):
    """ListFleets返回参数结构体

    """

    def __init__(self):
        """
        :param FleetIds: 服务器舰队 Id 列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetIds: list of str\n        :param TotalCount: 服务器舰队 Id 总数，最小值0\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetIds = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetIds = params.get("FleetIds")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class PlacedPlayerSession(AbstractModel):
    """部署的玩家游戏会话

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id\n        :type PlayerId: str\n        :param PlayerSessionId: 玩家会话Id\n        :type PlayerSessionId: str\n        """
        self.PlayerId = None
        self.PlayerSessionId = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerDataMap(AbstractModel):
    """玩家自定义数据

    """

    def __init__(self):
        """
        :param Key: 玩家自定义数据键，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type Key: str\n        :param Value: 玩家自定义数据值，最小长度不小于1个ASCII字符，最大长度不超过2048个ASCII字符\n        :type Value: str\n        """
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
        


class PlayerLatency(AbstractModel):
    """玩家延迟信息

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerId: str\n        :param RegionIdentifier: 延迟对应的区域名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionIdentifier: str\n        :param LatencyInMilliseconds: 毫秒级延迟\n        :type LatencyInMilliseconds: int\n        """
        self.PlayerId = None
        self.RegionIdentifier = None
        self.LatencyInMilliseconds = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.RegionIdentifier = params.get("RegionIdentifier")
        self.LatencyInMilliseconds = params.get("LatencyInMilliseconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerLatencyPolicy(AbstractModel):
    """延迟策略

    """

    def __init__(self):
        """
        :param MaximumIndividualPlayerLatencyMilliseconds: 任意player允许的最大延迟，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaximumIndividualPlayerLatencyMilliseconds: int\n        :param PolicyDurationSeconds: 放置新GameServerSession时强制实施策略的时间长度，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type PolicyDurationSeconds: int\n        """
        self.MaximumIndividualPlayerLatencyMilliseconds = None
        self.PolicyDurationSeconds = None


    def _deserialize(self, params):
        self.MaximumIndividualPlayerLatencyMilliseconds = params.get("MaximumIndividualPlayerLatencyMilliseconds")
        self.PolicyDurationSeconds = params.get("PolicyDurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayerSession(AbstractModel):
    """玩家会话详情

    """

    def __init__(self):
        """
        :param CreationTime: 玩家会话创建时间\n        :type CreationTime: str\n        :param DnsName: 游戏服务器会话运行的DNS标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type DnsName: str\n        :param FleetId: 舰队ID\n        :type FleetId: str\n        :param GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符\n        :type GameServerSessionId: str\n        :param IpAddress: 游戏服务器会话运行的CVM地址\n        :type IpAddress: str\n        :param PlayerData: 玩家自定义数据，最大长度2048个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerData: str\n        :param PlayerId: 玩家ID，最大长度1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayerId: str\n        :param PlayerSessionId: 玩家会话ID\n        :type PlayerSessionId: str\n        :param Port: 端口号，最小值不小于1，最大值不超过60000\n        :type Port: int\n        :param Status: 玩家会话的状态（RESERVED = 1,ACTIVE = 2,COMPLETED = 3,TIMEDOUT = 4）\n        :type Status: str\n        :param TerminationTime: 玩家会话终止时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TerminationTime: str\n        """
        self.CreationTime = None
        self.DnsName = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.PlayerData = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.Port = None
        self.Status = None
        self.TerminationTime = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.PlayerData = params.get("PlayerData")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.TerminationTime = params.get("TerminationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutScalingPolicyRequest(AbstractModel):
    """PutScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 扩缩容配置服务器舰队ID\n        :type FleetId: str\n        :param Name: 扩缩容策略名称，最小长度为1，最大长度为1024\n        :type Name: str\n        :param ScalingAdjustment: 扩缩容调整值，ScalingAdjustmentType取值PercentChangeInCapacity时，取值范围-99~99
ScalingAdjustmentType取值ChangeInCapacity或ExactCapacity时，最小值要缩容的最多CVM个数，最大值为实际最大的CVM个数限额\n        :type ScalingAdjustment: int\n        :param ScalingAdjustmentType: 扩缩容调整类型，取值（ChangeInCapacity，ExactCapacity，PercentChangeInCapacity）\n        :type ScalingAdjustmentType: str\n        :param Threshold: 扩缩容指标阈值\n        :type Threshold: float\n        :param ComparisonOperator: 扩缩容策略比较符，取值：>,>=,<,<=\n        :type ComparisonOperator: str\n        :param EvaluationPeriods: 单个策略持续时间长度（分钟）\n        :type EvaluationPeriods: int\n        :param MetricName: 扩缩容参与计算的指标名称，PolicyType取值RuleBased，
MetricName取值（AvailableGameServerSessions，AvailableCustomCount，PercentAvailableCustomCount，ActiveInstances，IdleInstances，CurrentPlayerSessions和PercentIdleInstances）；
PolicyType取值TargetBased时，MetricName取值PercentAvailableGameSessions\n        :type MetricName: str\n        :param PolicyType: 策略类型，取值：TargetBased表示基于目标的策略；RuleBased表示基于规则的策略\n        :type PolicyType: str\n        :param TargetConfiguration: 扩缩容目标值配置，只有TargetBased类型的策略生效\n        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`\n        """
        self.FleetId = None
        self.Name = None
        self.ScalingAdjustment = None
        self.ScalingAdjustmentType = None
        self.Threshold = None
        self.ComparisonOperator = None
        self.EvaluationPeriods = None
        self.MetricName = None
        self.PolicyType = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")
        self.ScalingAdjustment = params.get("ScalingAdjustment")
        self.ScalingAdjustmentType = params.get("ScalingAdjustmentType")
        self.Threshold = params.get("Threshold")
        self.ComparisonOperator = params.get("ComparisonOperator")
        self.EvaluationPeriods = params.get("EvaluationPeriods")
        self.MetricName = params.get("MetricName")
        self.PolicyType = params.get("PolicyType")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutScalingPolicyResponse(AbstractModel):
    """PutScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Name: 规则名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class PutTimerScalingPolicyRequest(AbstractModel):
    """PutTimerScalingPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param TimerScalingPolicy: 定时器策略消息\n        :type TimerScalingPolicy: :class:`tencentcloud.gse.v20191112.models.TimerScalingPolicy`\n        """
        self.TimerScalingPolicy = None


    def _deserialize(self, params):
        if params.get("TimerScalingPolicy") is not None:
            self.TimerScalingPolicy = TimerScalingPolicy()
            self.TimerScalingPolicy._deserialize(params.get("TimerScalingPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTimerScalingPolicyResponse(AbstractModel):
    """PutTimerScalingPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QuotaResource(AbstractModel):
    """配额资源

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型，1生成包、2服务部署、3别名、4游戏服务器队列、5实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceType: int\n        :param HardLimit: 总额度
注意：此字段可能返回 null，表示取不到有效值。\n        :type HardLimit: int\n        :param Remaining: 剩余额度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remaining: int\n        :param ExtraInfo: 额外信息，可能为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExtraInfo: str\n        """
        self.ResourceType = None
        self.HardLimit = None
        self.Remaining = None
        self.ExtraInfo = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.HardLimit = params.get("HardLimit")
        self.Remaining = params.get("Remaining")
        self.ExtraInfo = params.get("ExtraInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedCcnInfo(AbstractModel):
    """云联网相关信息描述

    """

    def __init__(self):
        """
        :param AccountId: 云联网所属账号\n        :type AccountId: str\n        :param CcnId: 云联网 ID\n        :type CcnId: str\n        :param AttachType: 关联云联网状态\n        :type AttachType: str\n        """
        self.AccountId = None
        self.CcnId = None
        self.AttachType = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.CcnId = params.get("CcnId")
        self.AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResolveAliasRequest(AbstractModel):
    """ResolveAlias请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 要获取fleetId的别名ID\n        :type AliasId: str\n        """
        self.AliasId = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResolveAliasResponse(AbstractModel):
    """ResolveAlias返回参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 别名指向的fleet的唯一标识符
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.RequestId = params.get("RequestId")


class ResourceCreationLimitPolicy(AbstractModel):
    """资源创建规则

    """

    def __init__(self):
        """
        :param NewGameServerSessionsPerCreator: 创建数量，最小值1，默认2\n        :type NewGameServerSessionsPerCreator: int\n        :param PolicyPeriodInMinutes: 单位时间，最小值1，默认3，单位分钟\n        :type PolicyPeriodInMinutes: int\n        """
        self.NewGameServerSessionsPerCreator = None
        self.PolicyPeriodInMinutes = None


    def _deserialize(self, params):
        self.NewGameServerSessionsPerCreator = params.get("NewGameServerSessionsPerCreator")
        self.PolicyPeriodInMinutes = params.get("PolicyPeriodInMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoutingStrategy(AbstractModel):
    """路由策略

    """

    def __init__(self):
        """
        :param Type: 别名的路由策略的类型，有效值常规别名(SIMPLE)、终止别名(TERMINAL)\n        :type Type: str\n        :param FleetId: 别名指向的队列的唯一标识符
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param Message: 与终端路由策略一起使用的消息文本，长度不小于1字符不超过1024字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        """
        self.Type = None
        self.FleetId = None
        self.Message = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FleetId = params.get("FleetId")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeConfiguration(AbstractModel):
    """运行配置

    """

    def __init__(self):
        """
        :param GameServerSessionActivationTimeoutSeconds: 游戏会话进程超时，最小值1，最大值600，单位秒\n        :type GameServerSessionActivationTimeoutSeconds: int\n        :param MaxConcurrentGameServerSessionActivations: 最大游戏会话数，最小值1，最大值2147483647\n        :type MaxConcurrentGameServerSessionActivations: int\n        :param ServerProcesses: 服务进程配置，至少有一个进程配置\n        :type ServerProcesses: list of ServerProcesse\n        """
        self.GameServerSessionActivationTimeoutSeconds = None
        self.MaxConcurrentGameServerSessionActivations = None
        self.ServerProcesses = None


    def _deserialize(self, params):
        self.GameServerSessionActivationTimeoutSeconds = params.get("GameServerSessionActivationTimeoutSeconds")
        self.MaxConcurrentGameServerSessionActivations = params.get("MaxConcurrentGameServerSessionActivations")
        if params.get("ServerProcesses") is not None:
            self.ServerProcesses = []
            for item in params.get("ServerProcesses"):
                obj = ServerProcesse()
                obj._deserialize(item)
                self.ServerProcesses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScalingPolicy(AbstractModel):
    """动态扩缩容配置

    """

    def __init__(self):
        """
        :param FleetId: 服务部署ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param ScalingAdjustment: 保留参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScalingAdjustment: str\n        :param ScalingAdjustmentType: 保留参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScalingAdjustmentType: str\n        :param ComparisonOperator: 保留参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ComparisonOperator: str\n        :param Threshold: 保留参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Threshold: str\n        :param EvaluationPeriods: 保留参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type EvaluationPeriods: str\n        :param MetricName: 保留参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MetricName: str\n        :param PolicyType: 策略类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type PolicyType: str\n        :param TargetConfiguration: 基于规则的配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`\n        """
        self.FleetId = None
        self.Name = None
        self.Status = None
        self.ScalingAdjustment = None
        self.ScalingAdjustmentType = None
        self.ComparisonOperator = None
        self.Threshold = None
        self.EvaluationPeriods = None
        self.MetricName = None
        self.PolicyType = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ScalingAdjustment = params.get("ScalingAdjustment")
        self.ScalingAdjustmentType = params.get("ScalingAdjustmentType")
        self.ComparisonOperator = params.get("ComparisonOperator")
        self.Threshold = params.get("Threshold")
        self.EvaluationPeriods = params.get("EvaluationPeriods")
        self.MetricName = params.get("MetricName")
        self.PolicyType = params.get("PolicyType")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsRequest(AbstractModel):
    """SearchGameServerSessions请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 别名ID\n        :type AliasId: str\n        :param FleetId: 舰队ID\n        :type FleetId: str\n        :param Limit: 单次查询记录数上限\n        :type Limit: int\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type NextToken: str\n        :param FilterExpression: 搜索条件表达式，支持如下变量
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number
hasAvailablePlayerSessions 是否有可用玩家数 String 取值true或false
gameServerSessionProperties 游戏会话属性 String

表达式String类型 等于=，不等于<>判断
表示Number类型支持 =,<>,>,>=,<,<=

例如：
FilterExpression取值
playerSessionCount>=2 AND hasAvailablePlayerSessions=true"
表示查找至少有两个玩家，而且有可用玩家会话的游戏会话。
FilterExpression取值
gameServerSessionProperties.K1 = 'V1' AND gameServerSessionProperties.K2 = 'V2' OR gameServerSessionProperties.K3 = 'V3'

表示
查询满足如下游戏服务器会话属性的游戏会话
{
    "GameProperties":[
        {
            "Key":"K1",
            "Value":"V1"
        },
        {
            "Key":"K2",
            "Value":"V2"
        },
        {
            "Key":"K3",
            "Value":"V3"
        }
    ]
}\n        :type FilterExpression: str\n        :param SortExpression: 排序条件关键字
支持排序字段
gameServerSessionName 游戏会话名称 String
gameServerSessionId 游戏会话ID String
maximumSessions 最大的玩家会话数 Number
creationTimeMillis 创建时间，单位：毫秒 Number
playerSessionCount 当前玩家会话数 Number\n        :type SortExpression: str\n        """
        self.AliasId = None
        self.FleetId = None
        self.Limit = None
        self.NextToken = None
        self.FilterExpression = None
        self.SortExpression = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.FilterExpression = params.get("FilterExpression")
        self.SortExpression = params.get("SortExpression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchGameServerSessionsResponse(AbstractModel):
    """SearchGameServerSessions返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessions: 游戏服务器会话列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameServerSessions: list of GameServerSession\n        :param NextToken: 页偏移，用于查询下一页，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextToken: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class ServerProcesse(AbstractModel):
    """游戏服务进程

    """

    def __init__(self):
        """
        :param ConcurrentExecutions: 并发执行数量，所有进程并发执行总数最小值1，最大值50\n        :type ConcurrentExecutions: int\n        :param LaunchPath: 启动路径：Linux路径/local/game/ 或WIndows路径C:\game\，最小长度1，最大长度1024\n        :type LaunchPath: str\n        :param Parameters: 启动参数，最小长度0，最大长度1024\n        :type Parameters: str\n        """
        self.ConcurrentExecutions = None
        self.LaunchPath = None
        self.Parameters = None


    def _deserialize(self, params):
        self.ConcurrentExecutions = params.get("ConcurrentExecutions")
        self.LaunchPath = params.get("LaunchPath")
        self.Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedRequest(AbstractModel):
    """SetServerReserved请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 扩缩容配置服务器舰队ID\n        :type FleetId: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param ReserveValue: 实例是否保留, 1-保留，0-不保留,默认\n        :type ReserveValue: int\n        """
        self.FleetId = None
        self.InstanceId = None
        self.ReserveValue = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.ReserveValue = params.get("ReserveValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerReservedResponse(AbstractModel):
    """SetServerReserved返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetServerWeightRequest(AbstractModel):
    """SetServerWeight请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Weight: 权重，最小值0，最大值10，默认值5\n        :type Weight: int\n        """
        self.FleetId = None
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetServerWeightResponse(AbstractModel):
    """SetServerWeight返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartFleetActionsRequest(AbstractModel):
    """StartFleetActions请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param Actions: 服务器舰队扩展策略，值为["AUTO_SCALING"]\n        :type Actions: list of str\n        """
        self.FleetId = None
        self.Actions = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartFleetActionsResponse(AbstractModel):
    """StartFleetActions返回参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.RequestId = params.get("RequestId")


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 开始部署游戏服务器会话的唯一标识符，最大值48个ASCII字符，模式：[a-zA-Z0-9-]+\n        :type PlacementId: str\n        :param GameServerSessionQueueName: 游戏服务器会话队列名称\n        :type GameServerSessionQueueName: str\n        :param MaximumPlayerSessionCount: 游戏服务器允许同时连接到游戏会话的最大玩家数量，最小值1，最大值为玩家会话最大限额\n        :type MaximumPlayerSessionCount: int\n        :param DesiredPlayerSessions: 玩家游戏会话信息\n        :type DesiredPlayerSessions: list of DesiredPlayerSession\n        :param GameProperties: 玩家游戏会话属性\n        :type GameProperties: list of GameProperty\n        :param GameServerSessionData: 游戏服务器会话数据，最大长度不超过4096个ASCII字符\n        :type GameServerSessionData: str\n        :param GameServerSessionName: 游戏服务器会话名称，最大长度不超过4096个ASCII字符\n        :type GameServerSessionName: str\n        :param PlayerLatencies: 玩家延迟\n        :type PlayerLatencies: list of PlayerLatency\n        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.MaximumPlayerSessionCount = None
        self.DesiredPlayerSessions = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionName = None
        self.PlayerLatencies = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        if params.get("DesiredPlayerSessions") is not None:
            self.DesiredPlayerSessions = []
            for item in params.get("DesiredPlayerSessions"):
                obj = DesiredPlayerSession()
                obj._deserialize(item)
                self.DesiredPlayerSessions.append(obj)
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionName = params.get("GameServerSessionName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置\n        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class StopFleetActionsRequest(AbstractModel):
    """StopFleetActions请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param Actions: 服务器舰队扩展策略，值为["AUTO_SCALING"]\n        :type Actions: list of str\n        """
        self.FleetId = None
        self.Actions = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopFleetActionsResponse(AbstractModel):
    """StopFleetActions返回参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.RequestId = params.get("RequestId")


class StopGameServerSessionPlacementRequest(AbstractModel):
    """StopGameServerSessionPlacement请求参数结构体

    """

    def __init__(self):
        """
        :param PlacementId: 游戏服务器会话放置的唯一标识符\n        :type PlacementId: str\n        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 游戏服务器会话放置\n        :type GameServerSessionPlacement: :class:`tencentcloud.gse.v20191112.models.GameServerSessionPlacement`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签结构体

    """

    def __init__(self):
        """
        :param Key: 标签键，最大长度127字节\n        :type Key: str\n        :param Value: 标签值，最大长度255字节\n        :type Value: str\n        """
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
        


class TargetConfiguration(AbstractModel):
    """基于规则的动态扩缩容配置项

    """

    def __init__(self):
        """
        :param TargetValue: 预留存率
注意：此字段可能返回 null，表示取不到有效值。\n        :type TargetValue: int\n        """
        self.TargetValue = None


    def _deserialize(self, params):
        self.TargetValue = params.get("TargetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerConfiguration(AbstractModel):
    """重复周期配置

    """

    def __init__(self):
        """
        :param TimerType: 定时器重复周期类型（未定义0，单次1、按天2、按月3、按周4）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerType: int\n        :param TimerValue: 定时器取值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerValue: :class:`tencentcloud.gse.v20191112.models.TimerValue`\n        :param BeginTime: 定时器开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type BeginTime: str\n        :param EndTime: 定时器结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        """
        self.TimerType = None
        self.TimerValue = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.TimerType = params.get("TimerType")
        if params.get("TimerValue") is not None:
            self.TimerValue = TimerValue()
            self.TimerValue._deserialize(params.get("TimerValue"))
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerFleetCapacity(AbstractModel):
    """定时器弹性伸缩策略

    """

    def __init__(self):
        """
        :param FleetId: 扩缩容配置服务器舰队ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param DesiredInstances: 期望实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type DesiredInstances: int\n        :param MinSize: 最小实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinSize: int\n        :param MaxSize: 最大实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxSize: int\n        :param ScalingInterval: 伸缩容间隔，单位：分钟
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScalingInterval: int\n        :param ScalingType: 扩缩容类型（手动1，自动2、未定义0）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScalingType: int\n        :param TargetConfiguration: 基于目标的扩展策略的设置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TargetConfiguration: :class:`tencentcloud.gse.v20191112.models.TargetConfiguration`\n        """
        self.FleetId = None
        self.DesiredInstances = None
        self.MinSize = None
        self.MaxSize = None
        self.ScalingInterval = None
        self.ScalingType = None
        self.TargetConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.DesiredInstances = params.get("DesiredInstances")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.ScalingInterval = params.get("ScalingInterval")
        self.ScalingType = params.get("ScalingType")
        if params.get("TargetConfiguration") is not None:
            self.TargetConfiguration = TargetConfiguration()
            self.TargetConfiguration._deserialize(params.get("TargetConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerScalingPolicy(AbstractModel):
    """定时器策略消息

    """

    def __init__(self):
        """
        :param TimerId: 定时器ID，进行encode，填写时更新
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerId: str\n        :param TimerName: 定时器名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerName: str\n        :param TimerStatus: 定时器状态(未定义0、未生效1、生效中2、已停止3、已过期4)
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerStatus: int\n        :param TimerFleetCapacity: 定时器弹性伸缩策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerFleetCapacity: :class:`tencentcloud.gse.v20191112.models.TimerFleetCapacity`\n        :param TimerConfiguration: 重复周期配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimerConfiguration: :class:`tencentcloud.gse.v20191112.models.TimerConfiguration`\n        """
        self.TimerId = None
        self.TimerName = None
        self.TimerStatus = None
        self.TimerFleetCapacity = None
        self.TimerConfiguration = None


    def _deserialize(self, params):
        self.TimerId = params.get("TimerId")
        self.TimerName = params.get("TimerName")
        self.TimerStatus = params.get("TimerStatus")
        if params.get("TimerFleetCapacity") is not None:
            self.TimerFleetCapacity = TimerFleetCapacity()
            self.TimerFleetCapacity._deserialize(params.get("TimerFleetCapacity"))
        if params.get("TimerConfiguration") is not None:
            self.TimerConfiguration = TimerConfiguration()
            self.TimerConfiguration._deserialize(params.get("TimerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerValue(AbstractModel):
    """定时器取值配置

    """

    def __init__(self):
        """
        :param Day: 每X天，执行一次(重复周期-按天/单次)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Day: int\n        :param FromDay: 每月从第x天，执行一次(重复周期-按月)
注意：此字段可能返回 null，表示取不到有效值。\n        :type FromDay: int\n        :param ToDay: 每月到第x天，执行一次(重复周期-按月)
注意：此字段可能返回 null，表示取不到有效值。\n        :type ToDay: int\n        :param WeekDays: 重复周期-按周，周几（多个值,取值周一(1,2,3,4,5,6,7)周日）
注意：此字段可能返回 null，表示取不到有效值。\n        :type WeekDays: list of int\n        """
        self.Day = None
        self.FromDay = None
        self.ToDay = None
        self.WeekDays = None


    def _deserialize(self, params):
        self.Day = params.get("Day")
        self.FromDay = params.get("FromDay")
        self.ToDay = params.get("ToDay")
        self.WeekDays = params.get("WeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias请求参数结构体

    """

    def __init__(self):
        """
        :param AliasId: 要更新的别名的唯一标识符\n        :type AliasId: str\n        :param Name: 名字，长度不小于1字符不超过1024字符\n        :type Name: str\n        :param Description: 别名的可读说明，长度不小于1字符不超过1024字符\n        :type Description: str\n        :param RoutingStrategy: 别名的路由配置\n        :type RoutingStrategy: :class:`tencentcloud.gse.v20191112.models.RoutingStrategy`\n        """
        self.AliasId = None
        self.Name = None
        self.Description = None
        self.RoutingStrategy = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("RoutingStrategy") is not None:
            self.RoutingStrategy = RoutingStrategy()
            self.RoutingStrategy._deserialize(params.get("RoutingStrategy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回参数结构体

    """

    def __init__(self):
        """
        :param Alias: 别名对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: :class:`tencentcloud.gse.v20191112.models.Alias`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Alias = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alias") is not None:
            self.Alias = Alias()
            self.Alias._deserialize(params.get("Alias"))
        self.RequestId = params.get("RequestId")


class UpdateAssetRequest(AbstractModel):
    """UpdateAsset请求参数结构体

    """

    def __init__(self):
        """
        :param AssetId: 生成包ID\n        :type AssetId: str\n        :param AssetName: 生成包名字，最小长度为1，最大长度为64\n        :type AssetName: str\n        :param AssetVersion: 生成包版本，最小长度为1，最大长度为64\n        :type AssetVersion: str\n        """
        self.AssetId = None
        self.AssetName = None
        self.AssetVersion = None


    def _deserialize(self, params):
        self.AssetId = params.get("AssetId")
        self.AssetName = params.get("AssetName")
        self.AssetVersion = params.get("AssetVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssetResponse(AbstractModel):
    """UpdateAsset返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateBucketAccelerateOptRequest(AbstractModel):
    """UpdateBucketAccelerateOpt请求参数结构体

    """

    def __init__(self):
        """
        :param Allowed: true为开启全球加速，false为关闭\n        :type Allowed: bool\n        """
        self.Allowed = None


    def _deserialize(self, params):
        self.Allowed = params.get("Allowed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketAccelerateOptResponse(AbstractModel):
    """UpdateBucketAccelerateOpt返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateBucketCORSOptRequest(AbstractModel):
    """UpdateBucketCORSOpt请求参数结构体

    """

    def __init__(self):
        """
        :param AllowedOrigins: 允许的访问来源;具体参见 [cos文档](https://cloud.tencent.com/document/product/436/8279)\n        :type AllowedOrigins: list of str\n        :param AllowedMethods: 允许的 HTTP 操作方法;可以配置多个:PUT、GET、POST、HEAD。[cos文档](https://cloud.tencent.com/document/product/436/8279)\n        :type AllowedMethods: list of str\n        :param AllowedHeaders: 用于指定允许浏览器发送 CORS 请求时携带的自定义 HTTP 请求头部;可以配置*，代表允许所有头部，为了避免遗漏，推荐配置为*。[cos文档](https://cloud.tencent.com/document/product/436/8279)\n        :type AllowedHeaders: list of str\n        :param MaxAgeSeconds: 跨域资源共享配置的有效时间，单位为秒。[cos文档](https://cloud.tencent.com/document/product/436/8279)\n        :type MaxAgeSeconds: int\n        :param ExposeHeaders: 允许浏览器获取的 CORS 请求响应中的头部，不区分大小写；默认情况下浏览器只能访问简单响应头部：Cache-Control、Content-Type、Expires、Last-Modified，如果需要访问其他响应头部，需要添加 ExposeHeader 配置。[cos文档](https://cloud.tencent.com/document/product/436/8279)\n        :type ExposeHeaders: list of str\n        """
        self.AllowedOrigins = None
        self.AllowedMethods = None
        self.AllowedHeaders = None
        self.MaxAgeSeconds = None
        self.ExposeHeaders = None


    def _deserialize(self, params):
        self.AllowedOrigins = params.get("AllowedOrigins")
        self.AllowedMethods = params.get("AllowedMethods")
        self.AllowedHeaders = params.get("AllowedHeaders")
        self.MaxAgeSeconds = params.get("MaxAgeSeconds")
        self.ExposeHeaders = params.get("ExposeHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBucketCORSOptResponse(AbstractModel):
    """UpdateBucketCORSOpt返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFleetAttributesRequest(AbstractModel):
    """UpdateFleetAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param Description: 服务器舰队描述，最小长度0，最大长度100\n        :type Description: str\n        :param Name: 服务器舰队名称，最小长度1，最大长度50\n        :type Name: str\n        :param NewGameSessionProtectionPolicy: 保护策略：不保护NoProtection、完全保护FullProtection、时限保护TimeLimitProtection\n        :type NewGameSessionProtectionPolicy: str\n        :param ResourceCreationLimitPolicy: 资源创建限制策略\n        :type ResourceCreationLimitPolicy: :class:`tencentcloud.gse.v20191112.models.ResourceCreationLimitPolicy`\n        :param GameServerSessionProtectionTimeLimit: 时限保护超时时间，默认60分钟，最小值5，最大值1440；当NewGameSessionProtectionPolicy为TimeLimitProtection时参数有效\n        :type GameServerSessionProtectionTimeLimit: int\n        """
        self.FleetId = None
        self.Description = None
        self.Name = None
        self.NewGameSessionProtectionPolicy = None
        self.ResourceCreationLimitPolicy = None
        self.GameServerSessionProtectionTimeLimit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.NewGameSessionProtectionPolicy = params.get("NewGameSessionProtectionPolicy")
        if params.get("ResourceCreationLimitPolicy") is not None:
            self.ResourceCreationLimitPolicy = ResourceCreationLimitPolicy()
            self.ResourceCreationLimitPolicy._deserialize(params.get("ResourceCreationLimitPolicy"))
        self.GameServerSessionProtectionTimeLimit = params.get("GameServerSessionProtectionTimeLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetAttributesResponse(AbstractModel):
    """UpdateFleetAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.RequestId = params.get("RequestId")


class UpdateFleetCapacityRequest(AbstractModel):
    """UpdateFleetCapacity请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID\n        :type FleetId: str\n        :param DesiredInstances: 期望的服务器实例数\n        :type DesiredInstances: int\n        :param MinSize: 服务器实例数最小限制，最小值0，最大值不超过最高配额查看各地区最高配额减1\n        :type MinSize: int\n        :param MaxSize: 服务器实例数最大限制，最小值1，最大值不超过最高配额查看各地区最高配额\n        :type MaxSize: int\n        :param ScalingInterval: 服务器伸缩容间隔，单位分钟，最小值3，最大值30，默认值10\n        :type ScalingInterval: int\n        """
        self.FleetId = None
        self.DesiredInstances = None
        self.MinSize = None
        self.MaxSize = None
        self.ScalingInterval = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.DesiredInstances = params.get("DesiredInstances")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.ScalingInterval = params.get("ScalingInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetCapacityResponse(AbstractModel):
    """UpdateFleetCapacity返回参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.RequestId = params.get("RequestId")


class UpdateFleetNameRequest(AbstractModel):
    """UpdateFleetName请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param Name: 服务器舰队名称，最小长度1，最大长度50\n        :type Name: str\n        """
        self.FleetId = None
        self.Name = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetNameResponse(AbstractModel):
    """UpdateFleetName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFleetPortSettingsRequest(AbstractModel):
    """UpdateFleetPortSettings请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队 Id\n        :type FleetId: str\n        :param InboundPermissionAuthorizations: 新增安全组\n        :type InboundPermissionAuthorizations: list of InboundPermissionAuthorization\n        :param InboundPermissionRevocations: 移除安全组\n        :type InboundPermissionRevocations: list of InboundPermissionRevocations\n        """
        self.FleetId = None
        self.InboundPermissionAuthorizations = None
        self.InboundPermissionRevocations = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        if params.get("InboundPermissionAuthorizations") is not None:
            self.InboundPermissionAuthorizations = []
            for item in params.get("InboundPermissionAuthorizations"):
                obj = InboundPermissionAuthorization()
                obj._deserialize(item)
                self.InboundPermissionAuthorizations.append(obj)
        if params.get("InboundPermissionRevocations") is not None:
            self.InboundPermissionRevocations = []
            for item in params.get("InboundPermissionRevocations"):
                obj = InboundPermissionRevocations()
                obj._deserialize(item)
                self.InboundPermissionRevocations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFleetPortSettingsResponse(AbstractModel):
    """UpdateFleetPortSettings返回参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务部署 Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FleetId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FleetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.RequestId = params.get("RequestId")


class UpdateGameServerSessionQueueRequest(AbstractModel):
    """UpdateGameServerSessionQueue请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 游戏服务器会话队列名字，长度1~128\n        :type Name: str\n        :param Destinations: 目的服务器舰队（可为别名）列表\n        :type Destinations: list of GameServerSessionQueueDestination\n        :param PlayerLatencyPolicies: 延迟策略集合\n        :type PlayerLatencyPolicies: list of PlayerLatencyPolicy\n        :param TimeoutInSeconds: 超时时间\n        :type TimeoutInSeconds: int\n        """
        self.Name = None
        self.Destinations = None
        self.PlayerLatencyPolicies = None
        self.TimeoutInSeconds = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = GameServerSessionQueueDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        if params.get("PlayerLatencyPolicies") is not None:
            self.PlayerLatencyPolicies = []
            for item in params.get("PlayerLatencyPolicies"):
                obj = PlayerLatencyPolicy()
                obj._deserialize(item)
                self.PlayerLatencyPolicies.append(obj)
        self.TimeoutInSeconds = params.get("TimeoutInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGameServerSessionQueueResponse(AbstractModel):
    """UpdateGameServerSessionQueue返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionQueue: 部署服务组对象\n        :type GameServerSessionQueue: :class:`tencentcloud.gse.v20191112.models.GameServerSessionQueue`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSessionQueue = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionQueue") is not None:
            self.GameServerSessionQueue = GameServerSessionQueue()
            self.GameServerSessionQueue._deserialize(params.get("GameServerSessionQueue"))
        self.RequestId = params.get("RequestId")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession请求参数结构体

    """

    def __init__(self):
        """
        :param GameServerSessionId: 游戏服务器会话ID，最小长度1个ASCII字符，最大长度不超过256个ASCII字符\n        :type GameServerSessionId: str\n        :param MaximumPlayerSessionCount: 最大玩家数量，最小值不小于0\n        :type MaximumPlayerSessionCount: int\n        :param Name: 游戏服务器会话名称，最小长度不小于1个ASCII字符，最大长度不超过1024个ASCII字符\n        :type Name: str\n        :param PlayerSessionCreationPolicy: 玩家会话创建策略，包括允许所有玩家加入和禁止所有玩家加入（ACCEPT_ALL,DENY_ALL）\n        :type PlayerSessionCreationPolicy: str\n        :param ProtectionPolicy: 保护策略，包括不保护、时限保护和完全保护(NoProtection,TimeLimitProtection,FullProtection)\n        :type ProtectionPolicy: str\n        """
        self.GameServerSessionId = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.ProtectionPolicy = params.get("ProtectionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession返回参数结构体

    """

    def __init__(self):
        """
        :param GameServerSession: 更新后的游戏会话\n        :type GameServerSession: :class:`tencentcloud.gse.v20191112.models.GameServerSession`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")


class UpdateRuntimeConfigurationRequest(AbstractModel):
    """UpdateRuntimeConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param FleetId: 服务器舰队Id\n        :type FleetId: str\n        :param RuntimeConfiguration: 服务器舰队配置\n        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`\n        """
        self.FleetId = None
        self.RuntimeConfiguration = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        if params.get("RuntimeConfiguration") is not None:
            self.RuntimeConfiguration = RuntimeConfiguration()
            self.RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuntimeConfigurationResponse(AbstractModel):
    """UpdateRuntimeConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param RuntimeConfiguration: 服务器舰队配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuntimeConfiguration: :class:`tencentcloud.gse.v20191112.models.RuntimeConfiguration`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RuntimeConfiguration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuntimeConfiguration") is not None:
            self.RuntimeConfiguration = RuntimeConfiguration()
            self.RuntimeConfiguration._deserialize(params.get("RuntimeConfiguration"))
        self.RequestId = params.get("RequestId")