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


class AttachCamRoleRequest(AbstractModel):
    """AttachCamRole请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 服务器ID
        :type InstanceId: str
        :param RoleName: 角色名称。
        :type RoleName: str
        """
        self.InstanceId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCamRoleResponse(AbstractModel):
    """AttachCamRole返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindPsaTagRequest(AbstractModel):
    """BindPsaTag请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        :param TagKey: 需要绑定的标签key
        :type TagKey: str
        :param TagValue: 需要绑定的标签value
        :type TagValue: str
        """
        self.PsaId = None
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPsaTagResponse(AbstractModel):
    """BindPsaTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BuyDevicesRequest(AbstractModel):
    """BuyDevices请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区ID。通过接口[查询地域以及可用区(DescribeRegions)](https://cloud.tencent.com/document/api/386/33564)获取可用区信息
        :type Zone: str
        :param OsTypeId: 部署服务器的操作系统ID。通过接口[查询操作系统信息(DescribeOsInfo)](https://cloud.tencent.com/document/product/386/32902)获取操作系统信息
        :type OsTypeId: int
        :param RaidId: RAID类型ID。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)获取RAID信息
        :type RaidId: int
        :param GoodsCount: 购买数量
        :type GoodsCount: int
        :param VpcId: 购买至私有网络ID
        :type VpcId: str
        :param SubnetId: 购买至子网ID
        :type SubnetId: str
        :param DeviceClassCode: 购买的机型ID。通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)获取机型信息
        :type DeviceClassCode: str
        :param TimeUnit: 购买时长单位，取值：M(月) D(天)
        :type TimeUnit: str
        :param TimeSpan: 购买时长
        :type TimeSpan: int
        :param NeedSecurityAgent: 是否安装安全Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedSecurityAgent: int
        :param NeedMonitorAgent: 是否安装监控Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedMonitorAgent: int
        :param NeedEMRAgent: 是否安装EMR Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRAgent: int
        :param NeedEMRSoftware: 是否安装EMR软件包，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRSoftware: int
        :param ApplyEip: 是否分配弹性公网IP，取值：1(分配) 0(不分配)，默认取值0
        :type ApplyEip: int
        :param EipPayMode: 弹性公网IP计费模式，取值：Flow(按流量计费) Bandwidth(按带宽计费)，默认取值Flow
        :type EipPayMode: str
        :param EipBandwidth: 弹性公网IP带宽限制，单位Mb
        :type EipBandwidth: int
        :param IsZoning: 数据盘是否格式化，取值：1(格式化) 0(不格式化)，默认取值为1
        :type IsZoning: int
        :param CpmPayMode: 物理机计费模式，取值：1(预付费) 2(后付费)，默认取值为1
        :type CpmPayMode: int
        :param ImageId: 自定义镜像ID，取值生效时用自定义镜像部署物理机
        :type ImageId: str
        :param Password: 设置Linux root或Windows Administrator的密码
        :type Password: str
        :param AutoRenewFlag: 自动续费标志位，取值：1(自动续费) 0(不自动续费)，默认取值0
        :type AutoRenewFlag: int
        :param SysRootSpace: 系统盘根分区大小，单位为G，默认取值10G。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)获取根分区信息
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: 系统盘swap分区或/boot/efi分区的大小，单位为G。若是uefi启动的机器，分区为/boot/efi，且此值是默认是2G。 普通机器为swap分区，可以不指定此分区。 机型是否是uefi启动，参见接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: /usr/local分区大小，单位为G
        :type SysUsrlocalSpace: int
        :param SysDataSpace: /data分区大小，单位为G。如果系统盘还有剩余大小，会分配给/data分区。（特殊情况：如果剩余空间不足10G，并且没有指定/data分区，则剩余空间会分配给Root分区）
        :type SysDataSpace: int
        :param HyperThreading: 是否开启超线程，取值：1(开启) 0(关闭)，默认取值1
        :type HyperThreading: int
        :param LanIps: 指定的内网IP列表，不指定时自动分配
        :type LanIps: list of str
        :param Aliases: 设备名称列表
        :type Aliases: list of str
        :param CpuId: CPU型号ID，自定义机型需要传入，取值：
<br/><li>1: E5-2620v3 (6核) &#42; 2</li><li>2: E5-2680v4 (14核) &#42; 2</li><li>3: E5-2670v3 (12核) &#42; 2</li><li>4: E5-2620v4 (8核) &#42; 2</li><li>5: 4110 (8核) &#42; 2</li><li>6: 6133 (20核) &#42; 2</li><br/>
        :type CpuId: int
        :param ContainRaidCard: 是否有RAID卡，取值：1(有) 0(无)，自定义机型需要传入
        :type ContainRaidCard: int
        :param MemSize: 内存大小，单位为G，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type MemSize: int
        :param SystemDiskTypeId: 系统盘ID，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 系统盘数量，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type SystemDiskCount: int
        :param DataDiskTypeId: 数据盘ID，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type DataDiskTypeId: int
        :param DataDiskCount: 数据盘数量，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type DataDiskCount: int
        :param Tags: 绑定的标签列表
        :type Tags: list of Tag
        :param FileSystem: 指定数据盘的文件系统格式，当前支持 EXT4和XFS选项， 默认为EXT4。 参数适用于数据盘和Linux， 且在IsZoning为1时生效
        :type FileSystem: str
        :param BuySession: 此参数是为了防止重复发货。如果两次调用传入相同的BuySession，只会发货一次。 不要以设备别名作为BuySession，这样只会第一次购买成功。参数长度为128位，合法字符为大小字母，数字，下划线，横线。
        :type BuySession: str
        :param SgId: 绑定已有的安全组ID。仅在NeedSecurityAgent为1时生效
        :type SgId: str
        :param TemplateId: 安全组模板ID，由模板创建新安全组并绑定。TemplateId和SgId不能同时传入
        :type TemplateId: str
        """
        self.Zone = None
        self.OsTypeId = None
        self.RaidId = None
        self.GoodsCount = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceClassCode = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.NeedSecurityAgent = None
        self.NeedMonitorAgent = None
        self.NeedEMRAgent = None
        self.NeedEMRSoftware = None
        self.ApplyEip = None
        self.EipPayMode = None
        self.EipBandwidth = None
        self.IsZoning = None
        self.CpmPayMode = None
        self.ImageId = None
        self.Password = None
        self.AutoRenewFlag = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.SysDataSpace = None
        self.HyperThreading = None
        self.LanIps = None
        self.Aliases = None
        self.CpuId = None
        self.ContainRaidCard = None
        self.MemSize = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None
        self.Tags = None
        self.FileSystem = None
        self.BuySession = None
        self.SgId = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.OsTypeId = params.get("OsTypeId")
        self.RaidId = params.get("RaidId")
        self.GoodsCount = params.get("GoodsCount")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.NeedSecurityAgent = params.get("NeedSecurityAgent")
        self.NeedMonitorAgent = params.get("NeedMonitorAgent")
        self.NeedEMRAgent = params.get("NeedEMRAgent")
        self.NeedEMRSoftware = params.get("NeedEMRSoftware")
        self.ApplyEip = params.get("ApplyEip")
        self.EipPayMode = params.get("EipPayMode")
        self.EipBandwidth = params.get("EipBandwidth")
        self.IsZoning = params.get("IsZoning")
        self.CpmPayMode = params.get("CpmPayMode")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.SysDataSpace = params.get("SysDataSpace")
        self.HyperThreading = params.get("HyperThreading")
        self.LanIps = params.get("LanIps")
        self.Aliases = params.get("Aliases")
        self.CpuId = params.get("CpuId")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.MemSize = params.get("MemSize")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.FileSystem = params.get("FileSystem")
        self.BuySession = params.get("BuySession")
        self.SgId = params.get("SgId")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuyDevicesResponse(AbstractModel):
    """BuyDevices返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 购买的物理机实例ID列表
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CpuInfo(AbstractModel):
    """cpu信息

    """

    def __init__(self):
        """
        :param CpuId: CPU的ID
        :type CpuId: int
        :param CpuDescription: CPU型号描述
        :type CpuDescription: str
        :param Series: 机型序列
        :type Series: int
        :param ContainRaidCard: 支持的RAID方式，0：有RAID卡，1：没有RAID卡
        :type ContainRaidCard: list of int non-negative
        """
        self.CpuId = None
        self.CpuDescription = None
        self.Series = None
        self.ContainRaidCard = None


    def _deserialize(self, params):
        self.CpuId = params.get("CpuId")
        self.CpuDescription = params.get("CpuDescription")
        self.Series = params.get("Series")
        self.ContainRaidCard = params.get("ContainRaidCard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomImageRequest(AbstractModel):
    """CreateCustomImage请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 用于制作镜像的物理机ID
        :type InstanceId: str
        :param ImageName: 镜像别名
        :type ImageName: str
        :param ImageDescription: 镜像描述
        :type ImageDescription: str
        """
        self.InstanceId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomImageResponse(AbstractModel):
    """CreateCustomImage返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param ImageId: 镜像ID
        :type ImageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.ImageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ImageId = params.get("ImageId")
        self.RequestId = params.get("RequestId")


class CreatePsaRegulationRequest(AbstractModel):
    """CreatePsaRegulation请求参数结构体

    """

    def __init__(self):
        """
        :param PsaName: 规则别名
        :type PsaName: str
        :param TaskTypeIds: 关联的故障类型ID列表
        :type TaskTypeIds: list of int non-negative
        :param RepairLimit: 维修实例上限，默认为5
        :type RepairLimit: int
        :param PsaDescription: 规则备注
        :type PsaDescription: str
        """
        self.PsaName = None
        self.TaskTypeIds = None
        self.RepairLimit = None
        self.PsaDescription = None


    def _deserialize(self, params):
        self.PsaName = params.get("PsaName")
        self.TaskTypeIds = params.get("TaskTypeIds")
        self.RepairLimit = params.get("RepairLimit")
        self.PsaDescription = params.get("PsaDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePsaRegulationResponse(AbstractModel):
    """CreatePsaRegulation返回参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 创建的预授权规则ID
        :type PsaId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PsaId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.RequestId = params.get("RequestId")


class CreateSpotDeviceRequest(AbstractModel):
    """CreateSpotDevice请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区名称。如ap-guangzhou-bls-1, 通过DescribeRegions获取
        :type Zone: str
        :param ComputeType: 计算单元类型, 如v3.c2.medium，更详细的ComputeType参考[竞价实例产品文档](https://cloud.tencent.com/document/product/386/30256)
        :type ComputeType: str
        :param OsTypeId: 操作系统类型ID
        :type OsTypeId: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param GoodsNum: 购买的计算单元个数
        :type GoodsNum: int
        :param SpotStrategy: 出价策略。可取值为SpotWithPriceLimit和SpotAsPriceGo。SpotWithPriceLimit，用户设置价格上限，需要传SpotPriceLimit参数， 如果市场价高于用户的指定价格，则购买不成功;  SpotAsPriceGo 是随市场价的策略。
        :type SpotStrategy: str
        :param SpotPriceLimit: 用户设置的价格。当为SpotWithPriceLimit竞价策略时有效
        :type SpotPriceLimit: float
        :param Passwd: 设置竞价实例密码。可选参数，没有指定会生成随机密码
        :type Passwd: str
        """
        self.Zone = None
        self.ComputeType = None
        self.OsTypeId = None
        self.VpcId = None
        self.SubnetId = None
        self.GoodsNum = None
        self.SpotStrategy = None
        self.SpotPriceLimit = None
        self.Passwd = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ComputeType = params.get("ComputeType")
        self.OsTypeId = params.get("OsTypeId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.GoodsNum = params.get("GoodsNum")
        self.SpotStrategy = params.get("SpotStrategy")
        self.SpotPriceLimit = params.get("SpotPriceLimit")
        self.Passwd = params.get("Passwd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSpotDeviceResponse(AbstractModel):
    """CreateSpotDevice返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceIds: 创建的服务器ID
        :type ResourceIds: list of str
        :param FlowId: 任务ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceIds = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateUserCmdRequest(AbstractModel):
    """CreateUserCmd请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 用户自定义脚本的名称
        :type Alias: str
        :param OsType: 命令适用的操作系统类型，取值linux或xserver
        :type OsType: str
        :param Content: 脚本内容，必须经过base64编码
        :type Content: str
        """
        self.Alias = None
        self.OsType = None
        self.Content = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.OsType = params.get("OsType")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserCmdResponse(AbstractModel):
    """CreateUserCmd返回参数结构体

    """

    def __init__(self):
        """
        :param CmdId: 脚本ID
        :type CmdId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CmdId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.RequestId = params.get("RequestId")


class CustomImage(AbstractModel):
    """自定义镜像信息

    """

    def __init__(self):
        """
        :param ImageId: 镜像ID
        :type ImageId: str
        :param ImageName: 镜像别名
        :type ImageName: str
        :param ImageStatus: 镜像状态码
        :type ImageStatus: int
        :param OsClass: 镜像OS名
        :type OsClass: str
        :param OsVersion: 镜像OS版本
        :type OsVersion: str
        :param OsBit: OS是64还是32位
        :type OsBit: int
        :param ImageSize: 镜像大小(M)
        :type ImageSize: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PartitionInfoSet: 分区信息
        :type PartitionInfoSet: list of PartitionInfo
        :param DeviceClassCode: 适用机型
        :type DeviceClassCode: str
        :param ImageDescription: 备注
        :type ImageDescription: str
        :param OsTypeId: 原始镜像id
        :type OsTypeId: int
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageStatus = None
        self.OsClass = None
        self.OsVersion = None
        self.OsBit = None
        self.ImageSize = None
        self.CreateTime = None
        self.PartitionInfoSet = None
        self.DeviceClassCode = None
        self.ImageDescription = None
        self.OsTypeId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageStatus = params.get("ImageStatus")
        self.OsClass = params.get("OsClass")
        self.OsVersion = params.get("OsVersion")
        self.OsBit = params.get("OsBit")
        self.ImageSize = params.get("ImageSize")
        self.CreateTime = params.get("CreateTime")
        if params.get("PartitionInfoSet") is not None:
            self.PartitionInfoSet = []
            for item in params.get("PartitionInfoSet"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.PartitionInfoSet.append(obj)
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.ImageDescription = params.get("ImageDescription")
        self.OsTypeId = params.get("OsTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomImageProcess(AbstractModel):
    """镜像制作进度列表

    """

    def __init__(self):
        """
        :param StepName: 步骤
        :type StepName: str
        :param StartTime: 此步骤开始时间
        :type StartTime: str
        :param StepType: 0: 已完成 1: 当前进行 2: 未开始
        :type StepType: int
        """
        self.StepName = None
        self.StartTime = None
        self.StepType = None


    def _deserialize(self, params):
        self.StepName = params.get("StepName")
        self.StartTime = params.get("StartTime")
        self.StepType = params.get("StepType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomImagesRequest(AbstractModel):
    """DeleteCustomImages请求参数结构体

    """

    def __init__(self):
        """
        :param ImageIds: 准备删除的镜像ID列表
        :type ImageIds: list of str
        """
        self.ImageIds = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomImagesResponse(AbstractModel):
    """DeleteCustomImages返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeletePsaRegulationRequest(AbstractModel):
    """DeletePsaRegulation请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        """
        self.PsaId = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePsaRegulationResponse(AbstractModel):
    """DeletePsaRegulation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserCmdsRequest(AbstractModel):
    """DeleteUserCmds请求参数结构体

    """

    def __init__(self):
        """
        :param CmdIds: 需要删除的脚本ID
        :type CmdIds: list of str
        """
        self.CmdIds = None


    def _deserialize(self, params):
        self.CmdIds = params.get("CmdIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserCmdsResponse(AbstractModel):
    """DeleteUserCmds返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomImageProcessRequest(AbstractModel):
    """DescribeCustomImageProcess请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 镜像ID
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
        


class DescribeCustomImageProcessResponse(AbstractModel):
    """DescribeCustomImageProcess返回参数结构体

    """

    def __init__(self):
        """
        :param CustomImageProcessSet: 镜像制作进度
        :type CustomImageProcessSet: list of CustomImageProcess
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomImageProcessSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomImageProcessSet") is not None:
            self.CustomImageProcessSet = []
            for item in params.get("CustomImageProcessSet"):
                obj = CustomImageProcess()
                obj._deserialize(item)
                self.CustomImageProcessSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomImagesRequest(AbstractModel):
    """DescribeCustomImages请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param OrderField: 排序字段，仅支持CreateTime
        :type OrderField: str
        :param Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        :param ImageId: 按ImageId查找指定镜像信息，ImageId字段存在时其他字段失效
        :type ImageId: str
        :param SearchKey: 模糊查询过滤，可以查询镜像ID或镜像名
        :type SearchKey: str
        :param ImageStatus: <ul>
镜像状态过滤列表，有效取值为：
<li>1：制作中</li>
<li>2：制作失败</li>
<li>3：正常</li>
<li>4：删除中</li>
</ul>
        :type ImageStatus: list of int non-negative
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.ImageId = None
        self.SearchKey = None
        self.ImageStatus = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.ImageId = params.get("ImageId")
        self.SearchKey = params.get("SearchKey")
        self.ImageStatus = params.get("ImageStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomImagesResponse(AbstractModel):
    """DescribeCustomImages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回镜像数量
        :type TotalCount: int
        :param CustomImageSet: 镜像信息列表
        :type CustomImageSet: list of CustomImage
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CustomImageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CustomImageSet") is not None:
            self.CustomImageSet = []
            for item in params.get("CustomImageSet"):
                obj = CustomImage()
                obj._deserialize(item)
                self.CustomImageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceClassPartitionRequest(AbstractModel):
    """DescribeDeviceClassPartition请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceClassCode: 设备类型代号。代号通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)查询。标准机型需要传入此参数。虽是可选参数，但DeviceClassCode和InstanceId参数，必须要填写一个。
        :type DeviceClassCode: str
        :param InstanceId: 需要查询自定义机型RAID信息时，传入自定义机型实例ID。InstanceId存在时其余参数失效。
        :type InstanceId: str
        :param CpuId: CPU型号ID，查询自定义机型时需要传入
        :type CpuId: int
        :param MemSize: 内存大小，单位为G，查询自定义机型时需要传入
        :type MemSize: int
        :param ContainRaidCard: 是否有RAID卡，取值：1(有) 0(无)。查询自定义机型时需要传入
        :type ContainRaidCard: int
        :param SystemDiskTypeId: 系统盘类型ID，查询自定义机型时需要传入
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 系统盘数量，查询自定义机型时需要传入
        :type SystemDiskCount: int
        :param DataDiskTypeId: 数据盘类型ID，查询自定义机型时可传入
        :type DataDiskTypeId: int
        :param DataDiskCount: 数据盘数量，查询自定义机型时可传入
        :type DataDiskCount: int
        """
        self.DeviceClassCode = None
        self.InstanceId = None
        self.CpuId = None
        self.MemSize = None
        self.ContainRaidCard = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None


    def _deserialize(self, params):
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.InstanceId = params.get("InstanceId")
        self.CpuId = params.get("CpuId")
        self.MemSize = params.get("MemSize")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceClassPartitionResponse(AbstractModel):
    """DescribeDeviceClassPartition返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceClassPartitionInfoSet: 支持的RAID格式列表
        :type DeviceClassPartitionInfoSet: list of DeviceClassPartitionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceClassPartitionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceClassPartitionInfoSet") is not None:
            self.DeviceClassPartitionInfoSet = []
            for item in params.get("DeviceClassPartitionInfoSet"):
                obj = DeviceClassPartitionInfo()
                obj._deserialize(item)
                self.DeviceClassPartitionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceClassRequest(AbstractModel):
    """DescribeDeviceClass请求参数结构体

    """

    def __init__(self):
        """
        :param OnSale: 是否仅查询在售标准机型配置信息。取值0：查询所有机型；1：查询在售机型。默认为1
        :type OnSale: int
        :param NeedPriceInfo: 是否返回价格信息。取值0：不返回价格信息，接口返回速度更快；1：返回价格信息。默认为1
        :type NeedPriceInfo: int
        """
        self.OnSale = None
        self.NeedPriceInfo = None


    def _deserialize(self, params):
        self.OnSale = params.get("OnSale")
        self.NeedPriceInfo = params.get("NeedPriceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceClassResponse(AbstractModel):
    """DescribeDeviceClass返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceClassSet: 物理机设备类型列表
        :type DeviceClassSet: list of DeviceClass
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceClassSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceClassSet") is not None:
            self.DeviceClassSet = []
            for item in params.get("DeviceClassSet"):
                obj = DeviceClass()
                obj._deserialize(item)
                self.DeviceClassSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceHardwareInfoRequest(AbstractModel):
    """DescribeDeviceHardwareInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 设备 ID 列表
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
        


class DescribeDeviceHardwareInfoResponse(AbstractModel):
    """DescribeDeviceHardwareInfo返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceHardwareInfoSet: 设备硬件配置信息
        :type DeviceHardwareInfoSet: list of DeviceHardwareInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceHardwareInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceHardwareInfoSet") is not None:
            self.DeviceHardwareInfoSet = []
            for item in params.get("DeviceHardwareInfoSet"):
                obj = DeviceHardwareInfo()
                obj._deserialize(item)
                self.DeviceHardwareInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceInventoryRequest(AbstractModel):
    """DescribeDeviceInventory请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区
        :type Zone: str
        :param DeviceClassCode: 设备型号
        :type DeviceClassCode: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param CpuId: CPU型号ID，查询自定义机型时必填
        :type CpuId: int
        :param MemSize: 内存大小，单位为G，查询自定义机型时必填
        :type MemSize: int
        :param ContainRaidCard: 是否有RAID卡，取值：1(有) 0(无)，查询自定义机型时必填
        :type ContainRaidCard: int
        :param SystemDiskTypeId: 系统盘类型ID，查询自定义机型时必填
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 系统盘数量，查询自定义机型时必填
        :type SystemDiskCount: int
        :param DataDiskTypeId: 数据盘类型ID，查询自定义机型时可填
        :type DataDiskTypeId: int
        :param DataDiskCount: 数据盘数量，查询自定义机型时可填
        :type DataDiskCount: int
        """
        self.Zone = None
        self.DeviceClassCode = None
        self.VpcId = None
        self.SubnetId = None
        self.CpuId = None
        self.MemSize = None
        self.ContainRaidCard = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CpuId = params.get("CpuId")
        self.MemSize = params.get("MemSize")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceInventoryResponse(AbstractModel):
    """DescribeDeviceInventory返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceCount: 库存设备数量
        :type DeviceCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceCount = params.get("DeviceCount")
        self.RequestId = params.get("RequestId")


class DescribeDeviceOperationLogRequest(AbstractModel):
    """DescribeDeviceOperationLog请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 设备实例ID
        :type InstanceId: str
        :param StartTime: 查询开始日期
        :type StartTime: str
        :param EndTime: 查询结束日期
        :type EndTime: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        


class DescribeDeviceOperationLogResponse(AbstractModel):
    """DescribeDeviceOperationLog返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceOperationLogSet: 操作日志列表
        :type DeviceOperationLogSet: list of DeviceOperationLog
        :param TotalCount: 返回数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceOperationLogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceOperationLogSet") is not None:
            self.DeviceOperationLogSet = []
            for item in params.get("DeviceOperationLogSet"):
                obj = DeviceOperationLog()
                obj._deserialize(item)
                self.DeviceOperationLogSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDevicePartitionRequest(AbstractModel):
    """DescribeDevicePartition请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
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
        


class DescribeDevicePartitionResponse(AbstractModel):
    """DescribeDevicePartition返回参数结构体

    """

    def __init__(self):
        """
        :param DevicePartition: 物理机分区格式
        :type DevicePartition: :class:`tencentcloud.bm.v20180423.models.DevicePartition`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DevicePartition = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DevicePartition") is not None:
            self.DevicePartition = DevicePartition()
            self.DevicePartition._deserialize(params.get("DevicePartition"))
        self.RequestId = params.get("RequestId")


class DescribeDevicePositionRequest(AbstractModel):
    """DescribeDevicePosition请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param Alias: 实例别名
        :type Alias: str
        """
        self.Offset = None
        self.Limit = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceIds = None
        self.Alias = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceIds = params.get("InstanceIds")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePositionResponse(AbstractModel):
    """DescribeDevicePosition返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回数量
        :type TotalCount: int
        :param DevicePositionInfoSet: 设备所在机架信息
        :type DevicePositionInfoSet: list of DevicePositionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DevicePositionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DevicePositionInfoSet") is not None:
            self.DevicePositionInfoSet = []
            for item in params.get("DevicePositionInfoSet"):
                obj = DevicePositionInfo()
                obj._deserialize(item)
                self.DevicePositionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicePriceInfoRequest(AbstractModel):
    """DescribeDevicePriceInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要查询的实例列表
        :type InstanceIds: list of str
        :param TimeUnit: 购买时长单位，当前只支持取值为m
        :type TimeUnit: str
        :param TimeSpan: 购买时长
        :type TimeSpan: int
        """
        self.InstanceIds = None
        self.TimeUnit = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePriceInfoResponse(AbstractModel):
    """DescribeDevicePriceInfo返回参数结构体

    """

    def __init__(self):
        """
        :param DevicePriceInfoSet: 服务器价格信息列表
        :type DevicePriceInfoSet: list of DevicePriceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DevicePriceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DevicePriceInfoSet") is not None:
            self.DevicePriceInfoSet = []
            for item in params.get("DevicePriceInfoSet"):
                obj = DevicePriceInfo()
                obj._deserialize(item)
                self.DevicePriceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        :param DeviceClassCode: 机型ID，通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)查询
        :type DeviceClassCode: str
        :param InstanceIds: 设备ID数组
        :type InstanceIds: list of str
        :param WanIps: 外网IP数组
        :type WanIps: list of str
        :param LanIps: 内网IP数组
        :type LanIps: list of str
        :param Alias: 设备名称
        :type Alias: str
        :param VagueIp: 模糊IP查询
        :type VagueIp: str
        :param DeadlineStartTime: 设备到期时间查询的起始时间
        :type DeadlineStartTime: str
        :param DeadlineEndTime: 设备到期时间查询的结束时间
        :type DeadlineEndTime: str
        :param AutoRenewFlag: 自动续费标志 0:不自动续费，1:自动续费
        :type AutoRenewFlag: int
        :param VpcId: 私有网络唯一ID
        :type VpcId: str
        :param SubnetId: 子网唯一ID
        :type SubnetId: str
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param DeviceType: 设备类型，取值有: compute(计算型), standard(标准型), storage(存储型) 等
        :type DeviceType: str
        :param IsLuckyDevice: 竞价实例机器的过滤。如果未指定此参数，则不做过滤。0: 查询非竞价实例的机器; 1: 查询竞价实例的机器。
        :type IsLuckyDevice: int
        :param OrderField: 排序字段
        :type OrderField: str
        :param Order: 排序方式，取值：0:增序(默认)，1:降序
        :type Order: int
        """
        self.Offset = None
        self.Limit = None
        self.DeviceClassCode = None
        self.InstanceIds = None
        self.WanIps = None
        self.LanIps = None
        self.Alias = None
        self.VagueIp = None
        self.DeadlineStartTime = None
        self.DeadlineEndTime = None
        self.AutoRenewFlag = None
        self.VpcId = None
        self.SubnetId = None
        self.Tags = None
        self.DeviceType = None
        self.IsLuckyDevice = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.InstanceIds = params.get("InstanceIds")
        self.WanIps = params.get("WanIps")
        self.LanIps = params.get("LanIps")
        self.Alias = params.get("Alias")
        self.VagueIp = params.get("VagueIp")
        self.DeadlineStartTime = params.get("DeadlineStartTime")
        self.DeadlineEndTime = params.get("DeadlineEndTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.IsLuckyDevice = params.get("IsLuckyDevice")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回数量
        :type TotalCount: int
        :param DeviceInfoSet: 物理机信息列表
        :type DeviceInfoSet: list of DeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceInfoSet") is not None:
            self.DeviceInfoSet = []
            for item in params.get("DeviceInfoSet"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.DeviceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHardwareSpecificationRequest(AbstractModel):
    """DescribeHardwareSpecification请求参数结构体

    """


class DescribeHardwareSpecificationResponse(AbstractModel):
    """DescribeHardwareSpecification返回参数结构体

    """

    def __init__(self):
        """
        :param CpuInfoSet: CPU型号列表
        :type CpuInfoSet: list of CpuInfo
        :param MemSet: 内存的取值，单位为G
        :type MemSet: list of int non-negative
        :param DiskInfoSet: 硬盘型号列表
        :type DiskInfoSet: list of DiskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CpuInfoSet = None
        self.MemSet = None
        self.DiskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CpuInfoSet") is not None:
            self.CpuInfoSet = []
            for item in params.get("CpuInfoSet"):
                obj = CpuInfo()
                obj._deserialize(item)
                self.CpuInfoSet.append(obj)
        self.MemSet = params.get("MemSet")
        if params.get("DiskInfoSet") is not None:
            self.DiskInfoSet = []
            for item in params.get("DiskInfoSet"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DiskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostedDeviceOutBandInfoRequest(AbstractModel):
    """DescribeHostedDeviceOutBandInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 托管设备的唯一ID数组,数组个数不超过20
        :type InstanceIds: list of str
        :param Zone: 可用区ID
        :type Zone: str
        """
        self.InstanceIds = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostedDeviceOutBandInfoResponse(AbstractModel):
    """DescribeHostedDeviceOutBandInfo返回参数结构体

    """

    def __init__(self):
        """
        :param HostedDeviceOutBandInfoSet: 托管设备带外信息
        :type HostedDeviceOutBandInfoSet: list of HostedDeviceOutBandInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HostedDeviceOutBandInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HostedDeviceOutBandInfoSet") is not None:
            self.HostedDeviceOutBandInfoSet = []
            for item in params.get("HostedDeviceOutBandInfoSet"):
                obj = HostedDeviceOutBandInfo()
                obj._deserialize(item)
                self.HostedDeviceOutBandInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOperationResultRequest(AbstractModel):
    """DescribeOperationResult请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
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
        


class DescribeOperationResultResponse(AbstractModel):
    """DescribeOperationResult返回参数结构体

    """

    def __init__(self):
        """
        :param TaskStatus: 任务的整体状态，取值如下：<br>
1：成功<br>
2：失败<br>
3：部分成功，部分失败<br>
4：未完成<br>
5：部分成功，部分未完成<br>
6：部分未完成，部分失败<br>
7：部分未完成，部分失败，部分成功
        :type TaskStatus: int
        :param SubtaskStatusSet: 各实例对应任务的状态ID
        :type SubtaskStatusSet: list of SubtaskStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.SubtaskStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("SubtaskStatusSet") is not None:
            self.SubtaskStatusSet = []
            for item in params.get("SubtaskStatusSet"):
                obj = SubtaskStatus()
                obj._deserialize(item)
                self.SubtaskStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOsInfoRequest(AbstractModel):
    """DescribeOsInfo请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceClassCode: 设备类型代号。 可以从DescribeDeviceClass查询设备类型列表
        :type DeviceClassCode: str
        """
        self.DeviceClassCode = None


    def _deserialize(self, params):
        self.DeviceClassCode = params.get("DeviceClassCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOsInfoResponse(AbstractModel):
    """DescribeOsInfo返回参数结构体

    """

    def __init__(self):
        """
        :param OsInfoSet: 操作系统信息列表
        :type OsInfoSet: list of OsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OsInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OsInfoSet") is not None:
            self.OsInfoSet = []
            for item in params.get("OsInfoSet"):
                obj = OsInfo()
                obj._deserialize(item)
                self.OsInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePsaRegulationsRequest(AbstractModel):
    """DescribePsaRegulations请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 数量限制
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param PsaIds: 规则ID过滤，支持模糊查询
        :type PsaIds: list of str
        :param PsaNames: 规则别名过滤，支持模糊查询
        :type PsaNames: list of str
        :param Tags: 标签过滤
        :type Tags: list of Tag
        :param OrderField: 排序字段，取值支持：CreateTime
        :type OrderField: str
        :param Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        """
        self.Limit = None
        self.Offset = None
        self.PsaIds = None
        self.PsaNames = None
        self.Tags = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.PsaIds = params.get("PsaIds")
        self.PsaNames = params.get("PsaNames")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePsaRegulationsResponse(AbstractModel):
    """DescribePsaRegulations返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回规则数量
        :type TotalCount: int
        :param PsaRegulations: 返回规则列表
        :type PsaRegulations: list of PsaRegulation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PsaRegulations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PsaRegulations") is not None:
            self.PsaRegulations = []
            for item in params.get("PsaRegulations"):
                obj = PsaRegulation()
                obj._deserialize(item)
                self.PsaRegulations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """

    def __init__(self):
        """
        :param RegionId: 地域整型ID，目前黑石可用地域包括：8-北京，4-上海，1-广州， 19-重庆
        :type RegionId: int
        """
        self.RegionId = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param RegionInfoSet: 地域信息
        :type RegionInfoSet: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionInfoSet") is not None:
            self.RegionInfoSet = []
            for item in params.get("RegionInfoSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRepairTaskConstantRequest(AbstractModel):
    """DescribeRepairTaskConstant请求参数结构体

    """


class DescribeRepairTaskConstantResponse(AbstractModel):
    """DescribeRepairTaskConstant返回参数结构体

    """

    def __init__(self):
        """
        :param TaskTypeSet: 故障类型ID与对应中文名列表
        :type TaskTypeSet: list of TaskType
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskTypeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskTypeSet") is not None:
            self.TaskTypeSet = []
            for item in params.get("TaskTypeSet"):
                obj = TaskType()
                obj._deserialize(item)
                self.TaskTypeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 开始位置
        :type Offset: int
        :param Limit: 数据条数
        :type Limit: int
        :param StartDate: 时间过滤下限
        :type StartDate: str
        :param EndDate: 时间过滤上限
        :type EndDate: str
        :param TaskStatus: 任务状态ID过滤
        :type TaskStatus: list of int non-negative
        :param OrderField: 排序字段，目前支持：CreateTime，AuthTime，EndTime
        :type OrderField: str
        :param Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        :param TaskIds: 任务ID过滤
        :type TaskIds: list of str
        :param InstanceIds: 实例ID过滤
        :type InstanceIds: list of str
        :param Aliases: 实例别名过滤
        :type Aliases: list of str
        :param TaskTypeIds: 故障类型ID过滤
        :type TaskTypeIds: list of int non-negative
        """
        self.Offset = None
        self.Limit = None
        self.StartDate = None
        self.EndDate = None
        self.TaskStatus = None
        self.OrderField = None
        self.Order = None
        self.TaskIds = None
        self.InstanceIds = None
        self.Aliases = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.TaskStatus = params.get("TaskStatus")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.TaskIds = params.get("TaskIds")
        self.InstanceIds = params.get("InstanceIds")
        self.Aliases = params.get("Aliases")
        self.TaskTypeIds = params.get("TaskTypeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回任务总数量
        :type TotalCount: int
        :param TaskInfoSet: 任务信息列表
        :type TaskInfoSet: list of TaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfoSet") is not None:
            self.TaskInfoSet = []
            for item in params.get("TaskInfoSet"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.TaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskOperationLogRequest(AbstractModel):
    """DescribeTaskOperationLog请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 维修任务ID
        :type TaskId: str
        :param OrderField: 排序字段，目前支持：OperationTime
        :type OrderField: str
        :param Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        """
        self.TaskId = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskOperationLogResponse(AbstractModel):
    """DescribeTaskOperationLog返回参数结构体

    """

    def __init__(self):
        """
        :param TaskOperationLogSet: 操作日志
        :type TaskOperationLogSet: list of TaskOperationLog
        :param TotalCount: 日志条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskOperationLogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskOperationLogSet") is not None:
            self.TaskOperationLogSet = []
            for item in params.get("TaskOperationLogSet"):
                obj = TaskOperationLog()
                obj._deserialize(item)
                self.TaskOperationLogSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUserCmdTaskInfoRequest(AbstractModel):
    """DescribeUserCmdTaskInfo请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param OrderField: 排序字段，支持： RunBeginTime,RunEndTime,Status
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        :param SearchKey: 关键字搜索，可搜索ID或别名，支持模糊搜索
        :type SearchKey: str
        """
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCmdTaskInfoResponse(AbstractModel):
    """DescribeUserCmdTaskInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回数量
        :type TotalCount: int
        :param UserCmdTaskInfoSet: 自定义脚本任务详细信息列表
        :type UserCmdTaskInfoSet: list of UserCmdTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmdTaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmdTaskInfoSet") is not None:
            self.UserCmdTaskInfoSet = []
            for item in params.get("UserCmdTaskInfoSet"):
                obj = UserCmdTaskInfo()
                obj._deserialize(item)
                self.UserCmdTaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserCmdTasksRequest(AbstractModel):
    """DescribeUserCmdTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param OrderField: 排序字段，支持： RunBeginTime,RunEndTime,InstanceCount,SuccessCount,FailureCount
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCmdTasksResponse(AbstractModel):
    """DescribeUserCmdTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 脚本任务信息数量
        :type TotalCount: int
        :param UserCmdTasks: 脚本任务信息列表
        :type UserCmdTasks: list of UserCmdTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmdTasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmdTasks") is not None:
            self.UserCmdTasks = []
            for item in params.get("UserCmdTasks"):
                obj = UserCmdTask()
                obj._deserialize(item)
                self.UserCmdTasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserCmdsRequest(AbstractModel):
    """DescribeUserCmds请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 数量限制
        :type Limit: int
        :param OrderField: 排序字段，支持： OsType,CreateTime,ModifyTime
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        :param SearchKey: 关键字搜索，可搜索ID或别名，支持模糊搜索
        :type SearchKey: str
        :param CmdId: 查询的脚本ID
        :type CmdId: str
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.SearchKey = None
        self.CmdId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.SearchKey = params.get("SearchKey")
        self.CmdId = params.get("CmdId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCmdsResponse(AbstractModel):
    """DescribeUserCmds返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回数量
        :type TotalCount: int
        :param UserCmds: 脚本信息列表
        :type UserCmds: list of UserCmd
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmds") is not None:
            self.UserCmds = []
            for item in params.get("UserCmds"):
                obj = UserCmd()
                obj._deserialize(item)
                self.UserCmds.append(obj)
        self.RequestId = params.get("RequestId")


class DetachCamRoleRequest(AbstractModel):
    """DetachCamRole请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 服务器ID
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
        


class DetachCamRoleResponse(AbstractModel):
    """DetachCamRole返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeviceAlias(AbstractModel):
    """设备ID与别名

    """

    def __init__(self):
        """
        :param InstanceId: 设备ID
        :type InstanceId: str
        :param Alias: 设备别名
        :type Alias: str
        """
        self.InstanceId = None
        self.Alias = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceClass(AbstractModel):
    """物理机设备类型

    """

    def __init__(self):
        """
        :param DeviceClassCode: 机型ID
        :type DeviceClassCode: str
        :param CpuDescription: CPU描述
        :type CpuDescription: str
        :param MemDescription: 内存描述
        :type MemDescription: str
        :param DiskDescription: 硬盘描述
        :type DiskDescription: str
        :param HaveRaidCard: 是否支持RAID. 0:不支持; 1:支持
        :type HaveRaidCard: int
        :param NicDescription: 网卡描述
        :type NicDescription: str
        :param GpuDescription: GPU描述
        :type GpuDescription: str
        :param Discount: 单价折扣
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param UnitPrice: 用户刊例价格
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: int
        :param RealPrice: 实际价格
注意：此字段可能返回 null，表示取不到有效值。
        :type RealPrice: int
        :param NormalPrice: 官网刊例价格
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalPrice: int
        :param DeviceType: 设备使用场景类型
        :type DeviceType: str
        :param Series: 机型系列
        :type Series: int
        :param Cpu: cpu的核心数。仅是物理服务器未开启超线程的核心数， 超线程的核心数为Cpu*2
        :type Cpu: int
        :param Mem: 内存容量。单位G
        :type Mem: int
        """
        self.DeviceClassCode = None
        self.CpuDescription = None
        self.MemDescription = None
        self.DiskDescription = None
        self.HaveRaidCard = None
        self.NicDescription = None
        self.GpuDescription = None
        self.Discount = None
        self.UnitPrice = None
        self.RealPrice = None
        self.NormalPrice = None
        self.DeviceType = None
        self.Series = None
        self.Cpu = None
        self.Mem = None


    def _deserialize(self, params):
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.CpuDescription = params.get("CpuDescription")
        self.MemDescription = params.get("MemDescription")
        self.DiskDescription = params.get("DiskDescription")
        self.HaveRaidCard = params.get("HaveRaidCard")
        self.NicDescription = params.get("NicDescription")
        self.GpuDescription = params.get("GpuDescription")
        self.Discount = params.get("Discount")
        self.UnitPrice = params.get("UnitPrice")
        self.RealPrice = params.get("RealPrice")
        self.NormalPrice = params.get("NormalPrice")
        self.DeviceType = params.get("DeviceType")
        self.Series = params.get("Series")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceClassPartitionInfo(AbstractModel):
    """RAID和设备分区结构

    """

    def __init__(self):
        """
        :param RaidId: RAID类型ID
        :type RaidId: int
        :param Raid: RAID名称
        :type Raid: str
        :param RaidDisplay: RAID名称（前台展示用）
        :type RaidDisplay: str
        :param SystemDiskSize: 系统盘总大小（单位GiB）
        :type SystemDiskSize: int
        :param SysRootSpace: 系统盘/分区默认大小（单位GiB）
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: 系统盘swap分区默认大小（单位GiB）
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: 系统盘/usr/local分区默认大小（单位GiB）
        :type SysUsrlocalSpace: int
        :param SysDataSpace: 系统盘/data分区默认大小（单位GiB）
        :type SysDataSpace: int
        :param SysIsUefiType: 设备是否是uefi启动方式。0:legacy启动; 1:uefi启动
        :type SysIsUefiType: int
        :param DataDiskSize: 数据盘总大小
        :type DataDiskSize: int
        :param DeviceDiskSizeInfoSet: 硬盘列表
        :type DeviceDiskSizeInfoSet: list of DeviceDiskSizeInfo
        """
        self.RaidId = None
        self.Raid = None
        self.RaidDisplay = None
        self.SystemDiskSize = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.SysDataSpace = None
        self.SysIsUefiType = None
        self.DataDiskSize = None
        self.DeviceDiskSizeInfoSet = None


    def _deserialize(self, params):
        self.RaidId = params.get("RaidId")
        self.Raid = params.get("Raid")
        self.RaidDisplay = params.get("RaidDisplay")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.SysDataSpace = params.get("SysDataSpace")
        self.SysIsUefiType = params.get("SysIsUefiType")
        self.DataDiskSize = params.get("DataDiskSize")
        if params.get("DeviceDiskSizeInfoSet") is not None:
            self.DeviceDiskSizeInfoSet = []
            for item in params.get("DeviceDiskSizeInfoSet"):
                obj = DeviceDiskSizeInfo()
                obj._deserialize(item)
                self.DeviceDiskSizeInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDiskSizeInfo(AbstractModel):
    """硬盘大小的描述

    """

    def __init__(self):
        """
        :param DiskName: 硬盘名称
        :type DiskName: str
        :param DiskSize: 硬盘大小（单位GiB）
        :type DiskSize: int
        """
        self.DiskName = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskName = params.get("DiskName")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceHardwareInfo(AbstractModel):
    """设备硬件配置信息

    """

    def __init__(self):
        """
        :param InstanceId: 设备实例 ID
        :type InstanceId: str
        :param IsElastic: 是否自定义机型
        :type IsElastic: int
        :param CpmPayMode: 机型计费模式，1 为预付费，2 为后付费
        :type CpmPayMode: int
        :param CpuId: 自定义机型，CPU 型号 ID（非自定义机型返回0）
        :type CpuId: int
        :param Mem: 自定义机型，内存大小, 单位 GB（非自定义机型返回0）
        :type Mem: int
        :param ContainRaidCard: 是否有 RAID 卡，0：没有 RAID 卡； 1：有 RAID 卡
        :type ContainRaidCard: int
        :param SystemDiskTypeId: 自定义机型系统盘类型ID（若没有则返回0）
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 自定义机型系统盘数量（若没有则返回0）
        :type SystemDiskCount: int
        :param DataDiskTypeId: 自定义机型数据盘类型 ID（若没有则返回0）
        :type DataDiskTypeId: int
        :param DataDiskCount: 自定义机型数据盘数量（若没有则返回0）
        :type DataDiskCount: int
        :param CpuDescription: CPU 型号描述
        :type CpuDescription: str
        :param MemDescription: 内存描述
        :type MemDescription: str
        :param DiskDescription: 磁盘描述
        :type DiskDescription: str
        :param NicDescription: 网卡描述
        :type NicDescription: str
        :param RaidDescription: 是否支持 RAID 的描述
        :type RaidDescription: str
        :param Cpu: cpu的核心数。仅是物理服务器未开启超线程的核心数， 超线程的核心数为Cpu*2
        :type Cpu: int
        :param DeviceClassCode: 机型外部代号
        :type DeviceClassCode: str
        """
        self.InstanceId = None
        self.IsElastic = None
        self.CpmPayMode = None
        self.CpuId = None
        self.Mem = None
        self.ContainRaidCard = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None
        self.CpuDescription = None
        self.MemDescription = None
        self.DiskDescription = None
        self.NicDescription = None
        self.RaidDescription = None
        self.Cpu = None
        self.DeviceClassCode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IsElastic = params.get("IsElastic")
        self.CpmPayMode = params.get("CpmPayMode")
        self.CpuId = params.get("CpuId")
        self.Mem = params.get("Mem")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")
        self.CpuDescription = params.get("CpuDescription")
        self.MemDescription = params.get("MemDescription")
        self.DiskDescription = params.get("DiskDescription")
        self.NicDescription = params.get("NicDescription")
        self.RaidDescription = params.get("RaidDescription")
        self.Cpu = params.get("Cpu")
        self.DeviceClassCode = params.get("DeviceClassCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """物理机信息

    """

    def __init__(self):
        """
        :param InstanceId: 设备唯一ID
        :type InstanceId: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param DeviceStatus: 设备状态ID，取值：<li>1：申领设备中</li><li>2：初始化中</li><li>4：运营中</li><li>7：隔离中</li><li>8：已隔离</li><li>10：解隔离中</li><li>16：故障中</li>
        :type DeviceStatus: int
        :param OperateStatus: 设备操作状态ID，取值：
<li>1：运行中</li><li>2：正在关机</li><li>3：已关机</li><li>5：正在开机</li><li>7：重启中</li><li>9：重装中</li><li>12：绑定EIP</li><li>13：解绑EIP</li><li>14：绑定LB</li><li>15：解绑LB</li><li>19：更换IP中</li><li>20：制作镜像中</li><li>21：制作镜像失败</li><li>23：故障待重装</li>
        :type OperateStatus: int
        :param OsTypeId: 操作系统ID，参考接口[查询操作系统信息(DescribeOsInfo)](https://cloud.tencent.com/document/product/386/32902)
        :type OsTypeId: int
        :param RaidId: RAID类型ID，参考接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/product/386/32910)
        :type RaidId: int
        :param Alias: 设备别名
        :type Alias: str
        :param AppId: 用户AppId
        :type AppId: int
        :param Zone: 可用区
        :type Zone: str
        :param WanIp: 外网IP
        :type WanIp: str
        :param LanIp: 内网IP
        :type LanIp: str
        :param DeliverTime: 设备交付时间
        :type DeliverTime: str
        :param Deadline: 设备到期时间
        :type Deadline: str
        :param AutoRenewFlag: 自动续费标识。0: 不自动续费; 1:自动续费
        :type AutoRenewFlag: int
        :param DeviceClassCode: 设备类型
        :type DeviceClassCode: str
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param CpmPayMode: 计费模式。1: 预付费; 2: 后付费; 3:预付费转后付费中
        :type CpmPayMode: int
        :param DhcpIp: 带外IP
        :type DhcpIp: str
        :param VpcName: 所在私有网络别名
        :type VpcName: str
        :param SubnetName: 所在子网别名
        :type SubnetName: str
        :param VpcCidrBlock: 所在私有网络CIDR
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: 所在子网CIDR
        :type SubnetCidrBlock: str
        :param IsLuckyDevice: 标识是否是竞价实例。0: 普通设备; 1: 竞价实例设备
        :type IsLuckyDevice: int
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceStatus = None
        self.OperateStatus = None
        self.OsTypeId = None
        self.RaidId = None
        self.Alias = None
        self.AppId = None
        self.Zone = None
        self.WanIp = None
        self.LanIp = None
        self.DeliverTime = None
        self.Deadline = None
        self.AutoRenewFlag = None
        self.DeviceClassCode = None
        self.Tags = None
        self.CpmPayMode = None
        self.DhcpIp = None
        self.VpcName = None
        self.SubnetName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.IsLuckyDevice = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceStatus = params.get("DeviceStatus")
        self.OperateStatus = params.get("OperateStatus")
        self.OsTypeId = params.get("OsTypeId")
        self.RaidId = params.get("RaidId")
        self.Alias = params.get("Alias")
        self.AppId = params.get("AppId")
        self.Zone = params.get("Zone")
        self.WanIp = params.get("WanIp")
        self.LanIp = params.get("LanIp")
        self.DeliverTime = params.get("DeliverTime")
        self.Deadline = params.get("Deadline")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeviceClassCode = params.get("DeviceClassCode")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CpmPayMode = params.get("CpmPayMode")
        self.DhcpIp = params.get("DhcpIp")
        self.VpcName = params.get("VpcName")
        self.SubnetName = params.get("SubnetName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.IsLuckyDevice = params.get("IsLuckyDevice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceOperationLog(AbstractModel):
    """设备操作日志

    """

    def __init__(self):
        """
        :param Id: 日志的ID
        :type Id: int
        :param InstanceId: 设备ID
        :type InstanceId: str
        :param TaskId: 日志对应的操作任务ID
        :type TaskId: int
        :param TaskName: 操作任务名称
        :type TaskName: str
        :param TaskDescription: 操作任务中文名称
        :type TaskDescription: str
        :param StartTime: 操作开始时间
        :type StartTime: str
        :param EndTime: 操作结束时间
        :type EndTime: str
        :param Status: 操作状态，0: 正在执行中；1：任务成功； 2: 任务失败。
        :type Status: int
        :param OpUin: 操作者
        :type OpUin: str
        :param LogDescription: 操作描述
        :type LogDescription: str
        """
        self.Id = None
        self.InstanceId = None
        self.TaskId = None
        self.TaskName = None
        self.TaskDescription = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.OpUin = None
        self.LogDescription = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.InstanceId = params.get("InstanceId")
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.TaskDescription = params.get("TaskDescription")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.OpUin = params.get("OpUin")
        self.LogDescription = params.get("LogDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePartition(AbstractModel):
    """物理机分区格式

    """

    def __init__(self):
        """
        :param SystemDiskSize: 系统盘大小
        :type SystemDiskSize: int
        :param DataDiskSize: 数据盘大小
        :type DataDiskSize: int
        :param SysIsUefiType: 是否兼容Uefi
        :type SysIsUefiType: bool
        :param SysRootSpace: root分区大小
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: Swaporuefi分区大小
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: Usrlocal分区大小
        :type SysUsrlocalSpace: int
        :param SysDataSpace: data分区大小
        :type SysDataSpace: int
        :param DeviceDiskSizeInfoSet: 硬盘大小详情
        :type DeviceDiskSizeInfoSet: list of DeviceDiskSizeInfo
        """
        self.SystemDiskSize = None
        self.DataDiskSize = None
        self.SysIsUefiType = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.SysDataSpace = None
        self.DeviceDiskSizeInfoSet = None


    def _deserialize(self, params):
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.DataDiskSize = params.get("DataDiskSize")
        self.SysIsUefiType = params.get("SysIsUefiType")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.SysDataSpace = params.get("SysDataSpace")
        if params.get("DeviceDiskSizeInfoSet") is not None:
            self.DeviceDiskSizeInfoSet = []
            for item in params.get("DeviceDiskSizeInfoSet"):
                obj = DeviceDiskSizeInfo()
                obj._deserialize(item)
                self.DeviceDiskSizeInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePositionInfo(AbstractModel):
    """物理机机架信息

    """

    def __init__(self):
        """
        :param InstanceId: 设备ID
        :type InstanceId: str
        :param Zone: 所在可用区
        :type Zone: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param LanIp: 业务IP
        :type LanIp: str
        :param Alias: 实例别名
        :type Alias: str
        :param RckName: 机架名称
        :type RckName: str
        :param PosCode: 机位
        :type PosCode: int
        :param SwitchName: 交换机名称
        :type SwitchName: str
        :param DeliverTime: 设备交付时间
        :type DeliverTime: str
        :param Deadline: 过期时间
        :type Deadline: str
        """
        self.InstanceId = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.LanIp = None
        self.Alias = None
        self.RckName = None
        self.PosCode = None
        self.SwitchName = None
        self.DeliverTime = None
        self.Deadline = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.LanIp = params.get("LanIp")
        self.Alias = params.get("Alias")
        self.RckName = params.get("RckName")
        self.PosCode = params.get("PosCode")
        self.SwitchName = params.get("SwitchName")
        self.DeliverTime = params.get("DeliverTime")
        self.Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePriceInfo(AbstractModel):
    """服务器价格信息

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
        :type InstanceId: str
        :param DeviceClassCode: 设备型号
        :type DeviceClassCode: str
        :param IsElastic: 是否是弹性机型，1：是，0：否
        :type IsElastic: int
        :param CpmPayMode: 付费模式ID, 1:预付费; 2:后付费; 3:预付费转后付费中
        :type CpmPayMode: int
        :param CpuDescription: Cpu信息描述
        :type CpuDescription: str
        :param MemDescription: 内存信息描述
        :type MemDescription: str
        :param DiskDescription: 硬盘信息描述
        :type DiskDescription: str
        :param NicDescription: 网卡信息描述
        :type NicDescription: str
        :param GpuDescription: Gpu信息描述
        :type GpuDescription: str
        :param RaidDescription: Raid信息描述
        :type RaidDescription: str
        :param Price: 客户的单价
        :type Price: int
        :param NormalPrice: 刊例单价
        :type NormalPrice: int
        :param TotalCost: 原价
        :type TotalCost: int
        :param RealTotalCost: 折扣价
        :type RealTotalCost: int
        :param TimeSpan: 计费时长
        :type TimeSpan: int
        :param TimeUnit: 计费时长单位, M:按月计费; D:按天计费
        :type TimeUnit: str
        :param GoodsCount: 商品数量
        :type GoodsCount: int
        """
        self.InstanceId = None
        self.DeviceClassCode = None
        self.IsElastic = None
        self.CpmPayMode = None
        self.CpuDescription = None
        self.MemDescription = None
        self.DiskDescription = None
        self.NicDescription = None
        self.GpuDescription = None
        self.RaidDescription = None
        self.Price = None
        self.NormalPrice = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.GoodsCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.IsElastic = params.get("IsElastic")
        self.CpmPayMode = params.get("CpmPayMode")
        self.CpuDescription = params.get("CpuDescription")
        self.MemDescription = params.get("MemDescription")
        self.DiskDescription = params.get("DiskDescription")
        self.NicDescription = params.get("NicDescription")
        self.GpuDescription = params.get("GpuDescription")
        self.RaidDescription = params.get("RaidDescription")
        self.Price = params.get("Price")
        self.NormalPrice = params.get("NormalPrice")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.GoodsCount = params.get("GoodsCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskInfo(AbstractModel):
    """自定义机型磁盘的描述

    """

    def __init__(self):
        """
        :param DiskTypeId: 磁盘ID
        :type DiskTypeId: int
        :param Size: 磁盘的容量，单位为G
        :type Size: int
        :param DiskDescription: 磁盘信息描述
        :type DiskDescription: str
        """
        self.DiskTypeId = None
        self.Size = None
        self.DiskDescription = None


    def _deserialize(self, params):
        self.DiskTypeId = params.get("DiskTypeId")
        self.Size = params.get("Size")
        self.DiskDescription = params.get("DiskDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedTaskInfo(AbstractModel):
    """运行失败的自定义脚本信息

    """

    def __init__(self):
        """
        :param InstanceId: 运行脚本的设备ID
        :type InstanceId: str
        :param ErrorMsg: 失败原因
        :type ErrorMsg: str
        """
        self.InstanceId = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostedDeviceOutBandInfo(AbstractModel):
    """托管设备带外信息

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
        :type InstanceId: str
        :param OutBandIp: 带外IP
        :type OutBandIp: str
        :param VpnIp: VPN的IP
        :type VpnIp: str
        :param VpnPort: VPN的端口
        :type VpnPort: int
        """
        self.InstanceId = None
        self.OutBandIp = None
        self.VpnIp = None
        self.VpnPort = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OutBandIp = params.get("OutBandIp")
        self.VpnIp = params.get("VpnIp")
        self.VpnPort = params.get("VpnPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomImageAttributeRequest(AbstractModel):
    """ModifyCustomImageAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 镜像ID
        :type ImageId: str
        :param ImageName: 设置新的镜像名
        :type ImageName: str
        :param ImageDescription: 设置新的镜像描述
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
        


class ModifyCustomImageAttributeResponse(AbstractModel):
    """ModifyCustomImageAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceAliasesRequest(AbstractModel):
    """ModifyDeviceAliases请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceAliases: 需要改名的设备与别名列表
        :type DeviceAliases: list of DeviceAlias
        """
        self.DeviceAliases = None


    def _deserialize(self, params):
        if params.get("DeviceAliases") is not None:
            self.DeviceAliases = []
            for item in params.get("DeviceAliases"):
                obj = DeviceAlias()
                obj._deserialize(item)
                self.DeviceAliases.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceAliasesResponse(AbstractModel):
    """ModifyDeviceAliases返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceAutoRenewFlagRequest(AbstractModel):
    """ModifyDeviceAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param AutoRenewFlag: 自动续费标志位。0: 不自动续费; 1: 自动续费
        :type AutoRenewFlag: int
        :param InstanceIds: 需要修改的设备ID列表
        :type InstanceIds: list of str
        """
        self.AutoRenewFlag = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceAutoRenewFlagResponse(AbstractModel):
    """ModifyDeviceAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLanIpRequest(AbstractModel):
    """ModifyLanIp请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
        :type InstanceId: str
        :param VpcId: 指定新VPC
        :type VpcId: str
        :param SubnetId: 指定新子网
        :type SubnetId: str
        :param LanIp: 指定新内网IP
        :type LanIp: str
        :param RebootDevice: 是否需要重启机器，取值 1(需要) 0(不需要)，默认取值0
        :type RebootDevice: int
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.LanIp = None
        self.RebootDevice = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.LanIp = params.get("LanIp")
        self.RebootDevice = params.get("RebootDevice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLanIpResponse(AbstractModel):
    """ModifyLanIp返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyPayModePre2PostRequest(AbstractModel):
    """ModifyPayModePre2Post请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要修改的设备ID列表
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
        


class ModifyPayModePre2PostResponse(AbstractModel):
    """ModifyPayModePre2Post返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPsaRegulationRequest(AbstractModel):
    """ModifyPsaRegulation请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        :param PsaName: 预授权规则别名
        :type PsaName: str
        :param RepairLimit: 维修中的实例上限
        :type RepairLimit: int
        :param PsaDescription: 预授权规则备注
        :type PsaDescription: str
        :param TaskTypeIds: 预授权规则关联故障类型ID列表
        :type TaskTypeIds: list of int non-negative
        """
        self.PsaId = None
        self.PsaName = None
        self.RepairLimit = None
        self.PsaDescription = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.PsaName = params.get("PsaName")
        self.RepairLimit = params.get("RepairLimit")
        self.PsaDescription = params.get("PsaDescription")
        self.TaskTypeIds = params.get("TaskTypeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPsaRegulationResponse(AbstractModel):
    """ModifyPsaRegulation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserCmdRequest(AbstractModel):
    """ModifyUserCmd请求参数结构体

    """

    def __init__(self):
        """
        :param CmdId: 待修改的脚本ID
        :type CmdId: str
        :param Alias: 待修改的脚本名称
        :type Alias: str
        :param OsType: 脚本适用的操作系统类型
        :type OsType: str
        :param Content: 待修改的脚本内容，必须经过base64编码
        :type Content: str
        """
        self.CmdId = None
        self.Alias = None
        self.OsType = None
        self.Content = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.Alias = params.get("Alias")
        self.OsType = params.get("OsType")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserCmdResponse(AbstractModel):
    """ModifyUserCmd返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineDevicesRequest(AbstractModel):
    """OfflineDevices请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要退还的物理机ID列表
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
        


class OfflineDevicesResponse(AbstractModel):
    """OfflineDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class OsInfo(AbstractModel):
    """操作系统类型

    """

    def __init__(self):
        """
        :param OsTypeId: 操作系统ID
        :type OsTypeId: int
        :param OsName: 操作系统名称
        :type OsName: str
        :param OsDescription: 操作系统名称描述
        :type OsDescription: str
        :param OsEnglishDescription: 操作系统英文名称
        :type OsEnglishDescription: str
        :param OsClass: 操作系统的分类，如CentOs Debian
        :type OsClass: str
        :param ImageTag: 标识镜像分类。public:公共镜像; private: 专属镜像
        :type ImageTag: str
        :param MaxPartitionSize: 操作系统，ext4文件下所支持的最大的磁盘大小。单位为T
        :type MaxPartitionSize: int
        :param OsMinorVersion: 黑石版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OsMinorVersion: str
        :param OsMinorClass: 黑石版本
注意：此字段可能返回 null，表示取不到有效值。
        :type OsMinorClass: str
        """
        self.OsTypeId = None
        self.OsName = None
        self.OsDescription = None
        self.OsEnglishDescription = None
        self.OsClass = None
        self.ImageTag = None
        self.MaxPartitionSize = None
        self.OsMinorVersion = None
        self.OsMinorClass = None


    def _deserialize(self, params):
        self.OsTypeId = params.get("OsTypeId")
        self.OsName = params.get("OsName")
        self.OsDescription = params.get("OsDescription")
        self.OsEnglishDescription = params.get("OsEnglishDescription")
        self.OsClass = params.get("OsClass")
        self.ImageTag = params.get("ImageTag")
        self.MaxPartitionSize = params.get("MaxPartitionSize")
        self.OsMinorVersion = params.get("OsMinorVersion")
        self.OsMinorClass = params.get("OsMinorClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionInfo(AbstractModel):
    """描述设备分区信息

    """

    def __init__(self):
        """
        :param Name: 分区名称
        :type Name: str
        :param Size: 分区大小
        :type Size: int
        """
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PsaRegulation(AbstractModel):
    """一条预授权规则

    """

    def __init__(self):
        """
        :param PsaId: 规则ID
        :type PsaId: str
        :param PsaName: 规则别名
        :type PsaName: str
        :param TagCount: 关联标签数量
        :type TagCount: int
        :param InstanceCount: 关联实例数量
        :type InstanceCount: int
        :param RepairCount: 故障实例数量
        :type RepairCount: int
        :param RepairLimit: 故障实例上限
        :type RepairLimit: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PsaDescription: 规则备注
        :type PsaDescription: str
        :param Tags: 关联标签
        :type Tags: list of Tag
        :param TaskTypeIds: 关联故障类型id
        :type TaskTypeIds: list of int non-negative
        """
        self.PsaId = None
        self.PsaName = None
        self.TagCount = None
        self.InstanceCount = None
        self.RepairCount = None
        self.RepairLimit = None
        self.CreateTime = None
        self.PsaDescription = None
        self.Tags = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.PsaName = params.get("PsaName")
        self.TagCount = params.get("TagCount")
        self.InstanceCount = params.get("InstanceCount")
        self.RepairCount = params.get("RepairCount")
        self.RepairLimit = params.get("RepairLimit")
        self.CreateTime = params.get("CreateTime")
        self.PsaDescription = params.get("PsaDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.TaskTypeIds = params.get("TaskTypeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootDevicesRequest(AbstractModel):
    """RebootDevices请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要重启的设备ID列表
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
        


class RebootDevicesResponse(AbstractModel):
    """RebootDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RecoverDevicesRequest(AbstractModel):
    """RecoverDevices请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要恢复的物理机ID列表
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
        


class RecoverDevicesResponse(AbstractModel):
    """RecoverDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        """
        :param Region: 地域ID
        :type Region: str
        :param RegionId: 地域整型ID
        :type RegionId: int
        :param RegionDescription: 地域描述
        :type RegionDescription: str
        :param ZoneInfoSet: 该地域下的可用区信息
        :type ZoneInfoSet: list of ZoneInfo
        """
        self.Region = None
        self.RegionId = None
        self.RegionDescription = None
        self.ZoneInfoSet = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.RegionDescription = params.get("RegionDescription")
        if params.get("ZoneInfoSet") is not None:
            self.ZoneInfoSet = []
            for item in params.get("ZoneInfoSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadDeviceOsRequest(AbstractModel):
    """ReloadDeviceOs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 设备的唯一ID
        :type InstanceId: str
        :param Password: 密码。 用户设置的linux root或Windows Administrator密码。密码校验规则: <li> Windows机器密码需12到16位，至少包括三项 `[a-z]`,`[A-Z]`,`[0-9]`和`[()`'`~!@#$%^&*-+=_`|`{}[]:;'<>,.?/]`的特殊符号, 密码不能包含Administrator(不区分大小写); <li> Linux机器密码需8到16位，至少包括两项`[a-z,A-Z]`,`[0-9]`和`[()`'`~!@#$%^&*-+=_`|`{}[]:;'<>,.?/]`的特殊符号
        :type Password: str
        :param OsTypeId: 操作系统类型ID。通过接口[查询操作系统信息(DescribeOsInfo)](https://cloud.tencent.com/document/api/386/32902)获取操作系统信息
        :type OsTypeId: int
        :param RaidId: RAID类型ID。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)获取RAID信息
        :type RaidId: int
        :param IsZoning: 是否格式化数据盘。0: 不格式化（默认值）；1：格式化
        :type IsZoning: int
        :param SysRootSpace: 系统盘根分区大小，默认是10G。系统盘的大小参考接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: 系统盘swap分区或/boot/efi分区的大小。若是uefi启动的机器，分区为/boot/efi ,且此值是默认是2G。普通机器为swap分区，可以不指定此分区。机型是否是uefi启动，参考接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: /usr/local分区大小
        :type SysUsrlocalSpace: int
        :param VpcId: 重装到新的私有网络的ID。如果改变VPC子网，则要求与SubnetId同时传参，否则可不填
        :type VpcId: str
        :param SubnetId: 重装到新的子网的ID。如果改变VPC子网，则要求与VpcId同时传参，否则可不填
        :type SubnetId: str
        :param LanIp: 重装指定IP地址
        :type LanIp: str
        :param HyperThreading: 指定是否开启超线程。 0：关闭超线程；1：开启超线程（默认值）
        :type HyperThreading: int
        :param ImageId: 自定义镜像ID。传此字段则用自定义镜像重装
        :type ImageId: str
        :param FileSystem: 指定数据盘的文件系统格式，当前支持 EXT4和XFS选项， 默认为EXT4。 参数适用于数据盘和Linux， 且在IsZoning为1时生效
        :type FileSystem: str
        :param NeedSecurityAgent: 是否安装安全Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedSecurityAgent: int
        :param NeedMonitorAgent: 是否安装监控Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedMonitorAgent: int
        :param NeedEMRAgent: 是否安装EMR Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRAgent: int
        :param NeedEMRSoftware: 是否安装EMR软件包，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRSoftware: int
        :param ReserveSgConfig: 是否保留安全组配置，取值：1(保留) 0(不保留)，默认取值0
        :type ReserveSgConfig: int
        :param SysDataSpace: /data分区大小，可不填。除root、swap、usr/local的剩余空间会自动分配到data分区
        :type SysDataSpace: int
        """
        self.InstanceId = None
        self.Password = None
        self.OsTypeId = None
        self.RaidId = None
        self.IsZoning = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.VpcId = None
        self.SubnetId = None
        self.LanIp = None
        self.HyperThreading = None
        self.ImageId = None
        self.FileSystem = None
        self.NeedSecurityAgent = None
        self.NeedMonitorAgent = None
        self.NeedEMRAgent = None
        self.NeedEMRSoftware = None
        self.ReserveSgConfig = None
        self.SysDataSpace = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        self.OsTypeId = params.get("OsTypeId")
        self.RaidId = params.get("RaidId")
        self.IsZoning = params.get("IsZoning")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.LanIp = params.get("LanIp")
        self.HyperThreading = params.get("HyperThreading")
        self.ImageId = params.get("ImageId")
        self.FileSystem = params.get("FileSystem")
        self.NeedSecurityAgent = params.get("NeedSecurityAgent")
        self.NeedMonitorAgent = params.get("NeedMonitorAgent")
        self.NeedEMRAgent = params.get("NeedEMRAgent")
        self.NeedEMRSoftware = params.get("NeedEMRSoftware")
        self.ReserveSgConfig = params.get("ReserveSgConfig")
        self.SysDataSpace = params.get("SysDataSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadDeviceOsResponse(AbstractModel):
    """ReloadDeviceOs返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RepairTaskControlRequest(AbstractModel):
    """RepairTaskControl请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 维修任务ID
        :type TaskId: str
        :param Operate: 操作
        :type Operate: str
        """
        self.TaskId = None
        self.Operate = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepairTaskControlResponse(AbstractModel):
    """RepairTaskControl返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 出参TaskId是黑石异步任务ID，不同于入参TaskId字段。
此字段可作为DescriptionOperationResult查询异步任务状态接口的入参，查询异步任务执行结果。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResetDevicePasswordRequest(AbstractModel):
    """ResetDevicePassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要重置密码的服务器ID列表
        :type InstanceIds: list of str
        :param Password: 新密码
        :type Password: str
        """
        self.InstanceIds = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDevicePasswordResponse(AbstractModel):
    """ResetDevicePassword返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReturnDevicesRequest(AbstractModel):
    """ReturnDevices请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要退还的物理机ID列表
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
        


class ReturnDevicesResponse(AbstractModel):
    """ReturnDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RunUserCmdRequest(AbstractModel):
    """RunUserCmd请求参数结构体

    """

    def __init__(self):
        """
        :param CmdId: 自定义脚本ID
        :type CmdId: str
        :param UserName: 执行脚本机器的用户名
        :type UserName: str
        :param Password: 执行脚本机器的用户名的密码
        :type Password: str
        :param InstanceIds: 执行脚本的服务器实例
        :type InstanceIds: list of str
        :param CmdParam: 执行脚本的参数，必须经过base64编码
        :type CmdParam: str
        """
        self.CmdId = None
        self.UserName = None
        self.Password = None
        self.InstanceIds = None
        self.CmdParam = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.InstanceIds = params.get("InstanceIds")
        self.CmdParam = params.get("CmdParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunUserCmdResponse(AbstractModel):
    """RunUserCmd返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessTaskInfoSet: 运行成功的任务信息列表
        :type SuccessTaskInfoSet: list of SuccessTaskInfo
        :param FailedTaskInfoSet: 运行失败的任务信息列表
        :type FailedTaskInfoSet: list of FailedTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessTaskInfoSet = None
        self.FailedTaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SuccessTaskInfoSet") is not None:
            self.SuccessTaskInfoSet = []
            for item in params.get("SuccessTaskInfoSet"):
                obj = SuccessTaskInfo()
                obj._deserialize(item)
                self.SuccessTaskInfoSet.append(obj)
        if params.get("FailedTaskInfoSet") is not None:
            self.FailedTaskInfoSet = []
            for item in params.get("FailedTaskInfoSet"):
                obj = FailedTaskInfo()
                obj._deserialize(item)
                self.FailedTaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SetOutBandVpnAuthPasswordRequest(AbstractModel):
    """SetOutBandVpnAuthPassword请求参数结构体

    """

    def __init__(self):
        """
        :param Password: 设置的Vpn认证密码
        :type Password: str
        :param Operate: 操作字段，取值为：Create（创建）或Update（修改）
        :type Operate: str
        """
        self.Password = None
        self.Operate = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOutBandVpnAuthPasswordResponse(AbstractModel):
    """SetOutBandVpnAuthPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ShutdownDevicesRequest(AbstractModel):
    """ShutdownDevices请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要关闭的设备ID列表
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
        


class ShutdownDevicesResponse(AbstractModel):
    """ShutdownDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StartDevicesRequest(AbstractModel):
    """StartDevices请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 需要开机的设备ID列表
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
        


class StartDevicesResponse(AbstractModel):
    """StartDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SubtaskStatus(AbstractModel):
    """各实例对应的异步任务执行结果

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param TaskStatus: 实例ID对应任务的状态，取值如下：<br>
1：成功<br>
2：失败<br>
3：部分成功，部分失败<br>
4：未完成<br>
5：部分成功，部分未完成<br>
6：部分未完成，部分失败<br>
7：部分未完成，部分失败，部分成功
        :type TaskStatus: int
        """
        self.InstanceId = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessTaskInfo(AbstractModel):
    """成功运行的自定义脚本信息

    """

    def __init__(self):
        """
        :param InstanceId: 运行脚本的设备ID
        :type InstanceId: str
        :param TaskId: 黑石异步任务ID
        :type TaskId: int
        :param CmdTaskId: 黑石自定义脚本运行任务ID
        :type CmdTaskId: str
        """
        self.InstanceId = None
        self.TaskId = None
        self.CmdTaskId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TaskId = params.get("TaskId")
        self.CmdTaskId = params.get("CmdTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键与值

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValues: 标签键对应的值
        :type TagValues: list of str
        """
        self.TagKey = None
        self.TagValues = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """维护平台维修任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务id
        :type TaskId: str
        :param InstanceId: 主机id
        :type InstanceId: str
        :param Alias: 主机别名
        :type Alias: str
        :param TaskTypeId: 故障类型id
        :type TaskTypeId: int
        :param TaskStatus: 任务状态id
        :type TaskStatus: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param AuthTime: 授权时间
        :type AuthTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param TaskDetail: 任务详情
        :type TaskDetail: str
        :param DeviceStatus: 设备状态
        :type DeviceStatus: int
        :param OperateStatus: 设备操作状态
        :type OperateStatus: int
        :param Zone: 可用区
        :type Zone: str
        :param Region: 地域
        :type Region: str
        :param VpcId: 所属网络
        :type VpcId: str
        :param SubnetId: 所在子网
        :type SubnetId: str
        :param SubnetName: 子网名
        :type SubnetName: str
        :param VpcName: VPC名
        :type VpcName: str
        :param VpcCidrBlock: VpcCidrBlock
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: SubnetCidrBlock
        :type SubnetCidrBlock: str
        :param WanIp: 公网ip
        :type WanIp: str
        :param LanIp: 内网IP
        :type LanIp: str
        :param MgtIp: 管理IP
        :type MgtIp: str
        :param TaskTypeName: 故障类中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        :param TaskSubType: 故障类型，取值：unconfirmed (不明确故障)；redundancy (有冗余故障)；nonredundancy (无冗余故障)
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSubType: str
        """
        self.TaskId = None
        self.InstanceId = None
        self.Alias = None
        self.TaskTypeId = None
        self.TaskStatus = None
        self.CreateTime = None
        self.AuthTime = None
        self.EndTime = None
        self.TaskDetail = None
        self.DeviceStatus = None
        self.OperateStatus = None
        self.Zone = None
        self.Region = None
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.WanIp = None
        self.LanIp = None
        self.MgtIp = None
        self.TaskTypeName = None
        self.TaskSubType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.TaskTypeId = params.get("TaskTypeId")
        self.TaskStatus = params.get("TaskStatus")
        self.CreateTime = params.get("CreateTime")
        self.AuthTime = params.get("AuthTime")
        self.EndTime = params.get("EndTime")
        self.TaskDetail = params.get("TaskDetail")
        self.DeviceStatus = params.get("DeviceStatus")
        self.OperateStatus = params.get("OperateStatus")
        self.Zone = params.get("Zone")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.WanIp = params.get("WanIp")
        self.LanIp = params.get("LanIp")
        self.MgtIp = params.get("MgtIp")
        self.TaskTypeName = params.get("TaskTypeName")
        self.TaskSubType = params.get("TaskSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOperationLog(AbstractModel):
    """维修任务操作日志

    """

    def __init__(self):
        """
        :param TaskStep: 操作步骤
        :type TaskStep: str
        :param Operator: 操作人
        :type Operator: str
        :param OperationDetail: 操作描述
        :type OperationDetail: str
        :param OperationTime: 操作时间
        :type OperationTime: str
        """
        self.TaskStep = None
        self.Operator = None
        self.OperationDetail = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.TaskStep = params.get("TaskStep")
        self.Operator = params.get("Operator")
        self.OperationDetail = params.get("OperationDetail")
        self.OperationTime = params.get("OperationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskType(AbstractModel):
    """故障id对应故障名列表

    """

    def __init__(self):
        """
        :param TypeId: 故障类ID
        :type TypeId: int
        :param TypeName: 故障类中文名
        :type TypeName: str
        :param TaskSubType: 故障类型父类
        :type TaskSubType: str
        """
        self.TypeId = None
        self.TypeName = None
        self.TaskSubType = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.TypeName = params.get("TypeName")
        self.TaskSubType = params.get("TaskSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindPsaTagRequest(AbstractModel):
    """UnbindPsaTag请求参数结构体

    """

    def __init__(self):
        """
        :param PsaId: 预授权规则ID
        :type PsaId: str
        :param TagKey: 需要解绑的标签key
        :type TagKey: str
        :param TagValue: 需要解绑的标签value
        :type TagValue: str
        """
        self.PsaId = None
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindPsaTagResponse(AbstractModel):
    """UnbindPsaTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserCmd(AbstractModel):
    """脚本信息

    """

    def __init__(self):
        """
        :param Alias: 用户自定义脚本名
        :type Alias: str
        :param AppId: AppId
        :type AppId: int
        :param AutoId: 脚本自增ID
        :type AutoId: int
        :param CmdId: 脚本ID
        :type CmdId: str
        :param Content: 脚本内容
        :type Content: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param OsType: 命令适用的操作系统类型
        :type OsType: str
        """
        self.Alias = None
        self.AppId = None
        self.AutoId = None
        self.CmdId = None
        self.Content = None
        self.CreateTime = None
        self.ModifyTime = None
        self.OsType = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.AppId = params.get("AppId")
        self.AutoId = params.get("AutoId")
        self.CmdId = params.get("CmdId")
        self.Content = params.get("Content")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserCmdTask(AbstractModel):
    """自定义脚本任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        :param Status: 任务状态ID，取值: -1(进行中) 0(结束)
        :type Status: int
        :param Alias: 脚本名称
        :type Alias: str
        :param CmdId: 脚本ID
        :type CmdId: str
        :param InstanceCount: 运行实例数量
        :type InstanceCount: int
        :param SuccessCount: 运行成功数量
        :type SuccessCount: int
        :param FailureCount: 运行失败数量
        :type FailureCount: int
        :param RunBeginTime: 执行开始时间
        :type RunBeginTime: str
        :param RunEndTime: 执行结束时间
        :type RunEndTime: str
        """
        self.TaskId = None
        self.Status = None
        self.Alias = None
        self.CmdId = None
        self.InstanceCount = None
        self.SuccessCount = None
        self.FailureCount = None
        self.RunBeginTime = None
        self.RunEndTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Alias = params.get("Alias")
        self.CmdId = params.get("CmdId")
        self.InstanceCount = params.get("InstanceCount")
        self.SuccessCount = params.get("SuccessCount")
        self.FailureCount = params.get("FailureCount")
        self.RunBeginTime = params.get("RunBeginTime")
        self.RunEndTime = params.get("RunEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserCmdTaskInfo(AbstractModel):
    """自定义脚本任务详细信息

    """

    def __init__(self):
        """
        :param AutoId: 自动编号，可忽略
        :type AutoId: int
        :param TaskId: 任务ID
        :type TaskId: str
        :param RunBeginTime: 任务开始时间
        :type RunBeginTime: str
        :param RunEndTime: 任务结束时间
        :type RunEndTime: str
        :param Status: 任务状态ID，取值为 -1：进行中；0：成功；>0：失败错误码
        :type Status: int
        :param InstanceName: 设备别名
        :type InstanceName: str
        :param InstanceId: 设备ID
        :type InstanceId: str
        :param VpcName: 私有网络名
        :type VpcName: str
        :param VpcId: 私有网络整型ID
        :type VpcId: str
        :param VpcCidrBlock: 私有网络Cidr
        :type VpcCidrBlock: str
        :param SubnetName: 子网名
        :type SubnetName: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param SubnetCidrBlock: 子网Cidr
        :type SubnetCidrBlock: str
        :param LanIp: 内网IP
        :type LanIp: str
        :param CmdContent: 脚本内容，base64编码后的值
        :type CmdContent: str
        :param CmdParam: 脚本参数，base64编码后的值
        :type CmdParam: str
        :param CmdResult: 脚本执行结果，base64编码后的值
        :type CmdResult: str
        :param AppId: 用户AppId
        :type AppId: int
        :param LastShellExit: 用户执行脚本结束退出的返回值，没有返回值为-1
        :type LastShellExit: int
        """
        self.AutoId = None
        self.TaskId = None
        self.RunBeginTime = None
        self.RunEndTime = None
        self.Status = None
        self.InstanceName = None
        self.InstanceId = None
        self.VpcName = None
        self.VpcId = None
        self.VpcCidrBlock = None
        self.SubnetName = None
        self.SubnetId = None
        self.SubnetCidrBlock = None
        self.LanIp = None
        self.CmdContent = None
        self.CmdParam = None
        self.CmdResult = None
        self.AppId = None
        self.LastShellExit = None


    def _deserialize(self, params):
        self.AutoId = params.get("AutoId")
        self.TaskId = params.get("TaskId")
        self.RunBeginTime = params.get("RunBeginTime")
        self.RunEndTime = params.get("RunEndTime")
        self.Status = params.get("Status")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.LanIp = params.get("LanIp")
        self.CmdContent = params.get("CmdContent")
        self.CmdParam = params.get("CmdParam")
        self.CmdResult = params.get("CmdResult")
        self.AppId = params.get("AppId")
        self.LastShellExit = params.get("LastShellExit")
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
        """
        :param Zone: 可用区ID
        :type Zone: str
        :param ZoneId: 可用区整型ID
        :type ZoneId: int
        :param ZoneDescription: 可用区描述
        :type ZoneDescription: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneDescription = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneDescription = params.get("ZoneDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        