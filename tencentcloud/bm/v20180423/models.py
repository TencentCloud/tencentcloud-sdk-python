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
        r"""
        :param _InstanceId: 服务器ID
        :type InstanceId: str
        :param _RoleName: 角色名称。
        :type RoleName: str
        """
        self._InstanceId = None
        self._RoleName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCamRoleResponse(AbstractModel):
    """AttachCamRole返回参数结构体

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


class BindPsaTagRequest(AbstractModel):
    """BindPsaTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PsaId: 预授权规则ID
        :type PsaId: str
        :param _TagKey: 需要绑定的标签key
        :type TagKey: str
        :param _TagValue: 需要绑定的标签value
        :type TagValue: str
        """
        self._PsaId = None
        self._TagKey = None
        self._TagValue = None

    @property
    def PsaId(self):
        return self._PsaId

    @PsaId.setter
    def PsaId(self, PsaId):
        self._PsaId = PsaId

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._PsaId = params.get("PsaId")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPsaTagResponse(AbstractModel):
    """BindPsaTag返回参数结构体

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


class BuyDevicesRequest(AbstractModel):
    """BuyDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区ID。通过接口[查询地域以及可用区(DescribeRegions)](https://cloud.tencent.com/document/api/386/33564)获取可用区信息
        :type Zone: str
        :param _OsTypeId: 部署服务器的操作系统ID。通过接口[查询操作系统信息(DescribeOsInfo)](https://cloud.tencent.com/document/product/386/32902)获取操作系统信息
        :type OsTypeId: int
        :param _RaidId: RAID类型ID。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)获取RAID信息
        :type RaidId: int
        :param _GoodsCount: 购买数量
        :type GoodsCount: int
        :param _VpcId: 购买至私有网络ID
        :type VpcId: str
        :param _SubnetId: 购买至子网ID
        :type SubnetId: str
        :param _DeviceClassCode: 购买的机型ID。通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)获取机型信息
        :type DeviceClassCode: str
        :param _TimeUnit: 购买时长单位，取值：M(月) D(天)
        :type TimeUnit: str
        :param _TimeSpan: 购买时长
        :type TimeSpan: int
        :param _NeedSecurityAgent: 是否安装安全Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedSecurityAgent: int
        :param _NeedMonitorAgent: 是否安装监控Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedMonitorAgent: int
        :param _NeedEMRAgent: 是否安装EMR Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRAgent: int
        :param _NeedEMRSoftware: 是否安装EMR软件包，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRSoftware: int
        :param _ApplyEip: 是否分配弹性公网IP，取值：1(分配) 0(不分配)，默认取值0
        :type ApplyEip: int
        :param _EipPayMode: 弹性公网IP计费模式，取值：Flow(按流量计费) Bandwidth(按带宽计费)，默认取值Flow
        :type EipPayMode: str
        :param _EipBandwidth: 弹性公网IP带宽限制，单位Mb
        :type EipBandwidth: int
        :param _IsZoning: 数据盘是否格式化，取值：1(格式化) 0(不格式化)，默认取值为1
        :type IsZoning: int
        :param _CpmPayMode: 物理机计费模式，取值：1(预付费) 2(后付费)，默认取值为1
        :type CpmPayMode: int
        :param _ImageId: 自定义镜像ID，取值生效时用自定义镜像部署物理机
        :type ImageId: str
        :param _Password: 设置Linux root或Windows Administrator的密码
        :type Password: str
        :param _AutoRenewFlag: 自动续费标志位，取值：1(自动续费) 0(不自动续费)，默认取值0
        :type AutoRenewFlag: int
        :param _SysRootSpace: 系统盘根分区大小，单位为G，默认取值10G。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)获取根分区信息
        :type SysRootSpace: int
        :param _SysSwaporuefiSpace: 系统盘swap分区或/boot/efi分区的大小，单位为G。若是uefi启动的机器，分区为/boot/efi，且此值是默认是2G。 普通机器为swap分区，可以不指定此分区。 机型是否是uefi启动，参见接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)
        :type SysSwaporuefiSpace: int
        :param _SysUsrlocalSpace: /usr/local分区大小，单位为G
        :type SysUsrlocalSpace: int
        :param _SysDataSpace: /data分区大小，单位为G。如果系统盘还有剩余大小，会分配给/data分区。（特殊情况：如果剩余空间不足10G，并且没有指定/data分区，则剩余空间会分配给Root分区）
        :type SysDataSpace: int
        :param _HyperThreading: 是否开启超线程，取值：1(开启) 0(关闭)，默认取值1
        :type HyperThreading: int
        :param _LanIps: 指定的内网IP列表，不指定时自动分配
        :type LanIps: list of str
        :param _Aliases: 设备名称列表
        :type Aliases: list of str
        :param _CpuId: CPU型号ID，自定义机型需要传入，取值：
<br/><li>1: E5-2620v3 (6核) &#42; 2</li><li>2: E5-2680v4 (14核) &#42; 2</li><li>3: E5-2670v3 (12核) &#42; 2</li><li>4: E5-2620v4 (8核) &#42; 2</li><li>5: 4110 (8核) &#42; 2</li><li>6: 6133 (20核) &#42; 2</li><br/>
        :type CpuId: int
        :param _ContainRaidCard: 是否有RAID卡，取值：1(有) 0(无)，自定义机型需要传入
        :type ContainRaidCard: int
        :param _MemSize: 内存大小，单位为G，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type MemSize: int
        :param _SystemDiskTypeId: 系统盘ID，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type SystemDiskTypeId: int
        :param _SystemDiskCount: 系统盘数量，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type SystemDiskCount: int
        :param _DataDiskTypeId: 数据盘ID，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type DataDiskTypeId: int
        :param _DataDiskCount: 数据盘数量，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/33565)返回值
        :type DataDiskCount: int
        :param _Tags: 绑定的标签列表
        :type Tags: list of Tag
        :param _FileSystem: 指定数据盘的文件系统格式，当前支持 EXT4和XFS选项， 默认为EXT4。 参数适用于数据盘和Linux， 且在IsZoning为1时生效
        :type FileSystem: str
        :param _BuySession: 此参数是为了防止重复发货。如果两次调用传入相同的BuySession，只会发货一次。 不要以设备别名作为BuySession，这样只会第一次购买成功。参数长度为128位，合法字符为大小字母，数字，下划线，横线。
        :type BuySession: str
        :param _SgId: 绑定已有的安全组ID。仅在NeedSecurityAgent为1时生效
        :type SgId: str
        :param _TemplateId: 安全组模板ID，由模板创建新安全组并绑定。TemplateId和SgId不能同时传入
        :type TemplateId: str
        """
        self._Zone = None
        self._OsTypeId = None
        self._RaidId = None
        self._GoodsCount = None
        self._VpcId = None
        self._SubnetId = None
        self._DeviceClassCode = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._NeedSecurityAgent = None
        self._NeedMonitorAgent = None
        self._NeedEMRAgent = None
        self._NeedEMRSoftware = None
        self._ApplyEip = None
        self._EipPayMode = None
        self._EipBandwidth = None
        self._IsZoning = None
        self._CpmPayMode = None
        self._ImageId = None
        self._Password = None
        self._AutoRenewFlag = None
        self._SysRootSpace = None
        self._SysSwaporuefiSpace = None
        self._SysUsrlocalSpace = None
        self._SysDataSpace = None
        self._HyperThreading = None
        self._LanIps = None
        self._Aliases = None
        self._CpuId = None
        self._ContainRaidCard = None
        self._MemSize = None
        self._SystemDiskTypeId = None
        self._SystemDiskCount = None
        self._DataDiskTypeId = None
        self._DataDiskCount = None
        self._Tags = None
        self._FileSystem = None
        self._BuySession = None
        self._SgId = None
        self._TemplateId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId

    @property
    def RaidId(self):
        return self._RaidId

    @RaidId.setter
    def RaidId(self, RaidId):
        self._RaidId = RaidId

    @property
    def GoodsCount(self):
        return self._GoodsCount

    @GoodsCount.setter
    def GoodsCount(self, GoodsCount):
        self._GoodsCount = GoodsCount

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
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def NeedSecurityAgent(self):
        return self._NeedSecurityAgent

    @NeedSecurityAgent.setter
    def NeedSecurityAgent(self, NeedSecurityAgent):
        self._NeedSecurityAgent = NeedSecurityAgent

    @property
    def NeedMonitorAgent(self):
        return self._NeedMonitorAgent

    @NeedMonitorAgent.setter
    def NeedMonitorAgent(self, NeedMonitorAgent):
        self._NeedMonitorAgent = NeedMonitorAgent

    @property
    def NeedEMRAgent(self):
        return self._NeedEMRAgent

    @NeedEMRAgent.setter
    def NeedEMRAgent(self, NeedEMRAgent):
        self._NeedEMRAgent = NeedEMRAgent

    @property
    def NeedEMRSoftware(self):
        return self._NeedEMRSoftware

    @NeedEMRSoftware.setter
    def NeedEMRSoftware(self, NeedEMRSoftware):
        self._NeedEMRSoftware = NeedEMRSoftware

    @property
    def ApplyEip(self):
        return self._ApplyEip

    @ApplyEip.setter
    def ApplyEip(self, ApplyEip):
        self._ApplyEip = ApplyEip

    @property
    def EipPayMode(self):
        return self._EipPayMode

    @EipPayMode.setter
    def EipPayMode(self, EipPayMode):
        self._EipPayMode = EipPayMode

    @property
    def EipBandwidth(self):
        return self._EipBandwidth

    @EipBandwidth.setter
    def EipBandwidth(self, EipBandwidth):
        self._EipBandwidth = EipBandwidth

    @property
    def IsZoning(self):
        return self._IsZoning

    @IsZoning.setter
    def IsZoning(self, IsZoning):
        self._IsZoning = IsZoning

    @property
    def CpmPayMode(self):
        return self._CpmPayMode

    @CpmPayMode.setter
    def CpmPayMode(self, CpmPayMode):
        self._CpmPayMode = CpmPayMode

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SysRootSpace(self):
        return self._SysRootSpace

    @SysRootSpace.setter
    def SysRootSpace(self, SysRootSpace):
        self._SysRootSpace = SysRootSpace

    @property
    def SysSwaporuefiSpace(self):
        return self._SysSwaporuefiSpace

    @SysSwaporuefiSpace.setter
    def SysSwaporuefiSpace(self, SysSwaporuefiSpace):
        self._SysSwaporuefiSpace = SysSwaporuefiSpace

    @property
    def SysUsrlocalSpace(self):
        return self._SysUsrlocalSpace

    @SysUsrlocalSpace.setter
    def SysUsrlocalSpace(self, SysUsrlocalSpace):
        self._SysUsrlocalSpace = SysUsrlocalSpace

    @property
    def SysDataSpace(self):
        return self._SysDataSpace

    @SysDataSpace.setter
    def SysDataSpace(self, SysDataSpace):
        self._SysDataSpace = SysDataSpace

    @property
    def HyperThreading(self):
        return self._HyperThreading

    @HyperThreading.setter
    def HyperThreading(self, HyperThreading):
        self._HyperThreading = HyperThreading

    @property
    def LanIps(self):
        return self._LanIps

    @LanIps.setter
    def LanIps(self, LanIps):
        self._LanIps = LanIps

    @property
    def Aliases(self):
        return self._Aliases

    @Aliases.setter
    def Aliases(self, Aliases):
        self._Aliases = Aliases

    @property
    def CpuId(self):
        return self._CpuId

    @CpuId.setter
    def CpuId(self, CpuId):
        self._CpuId = CpuId

    @property
    def ContainRaidCard(self):
        return self._ContainRaidCard

    @ContainRaidCard.setter
    def ContainRaidCard(self, ContainRaidCard):
        self._ContainRaidCard = ContainRaidCard

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def SystemDiskTypeId(self):
        return self._SystemDiskTypeId

    @SystemDiskTypeId.setter
    def SystemDiskTypeId(self, SystemDiskTypeId):
        self._SystemDiskTypeId = SystemDiskTypeId

    @property
    def SystemDiskCount(self):
        return self._SystemDiskCount

    @SystemDiskCount.setter
    def SystemDiskCount(self, SystemDiskCount):
        self._SystemDiskCount = SystemDiskCount

    @property
    def DataDiskTypeId(self):
        return self._DataDiskTypeId

    @DataDiskTypeId.setter
    def DataDiskTypeId(self, DataDiskTypeId):
        self._DataDiskTypeId = DataDiskTypeId

    @property
    def DataDiskCount(self):
        return self._DataDiskCount

    @DataDiskCount.setter
    def DataDiskCount(self, DataDiskCount):
        self._DataDiskCount = DataDiskCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def BuySession(self):
        return self._BuySession

    @BuySession.setter
    def BuySession(self, BuySession):
        self._BuySession = BuySession

    @property
    def SgId(self):
        return self._SgId

    @SgId.setter
    def SgId(self, SgId):
        self._SgId = SgId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._OsTypeId = params.get("OsTypeId")
        self._RaidId = params.get("RaidId")
        self._GoodsCount = params.get("GoodsCount")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DeviceClassCode = params.get("DeviceClassCode")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._NeedSecurityAgent = params.get("NeedSecurityAgent")
        self._NeedMonitorAgent = params.get("NeedMonitorAgent")
        self._NeedEMRAgent = params.get("NeedEMRAgent")
        self._NeedEMRSoftware = params.get("NeedEMRSoftware")
        self._ApplyEip = params.get("ApplyEip")
        self._EipPayMode = params.get("EipPayMode")
        self._EipBandwidth = params.get("EipBandwidth")
        self._IsZoning = params.get("IsZoning")
        self._CpmPayMode = params.get("CpmPayMode")
        self._ImageId = params.get("ImageId")
        self._Password = params.get("Password")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SysRootSpace = params.get("SysRootSpace")
        self._SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self._SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self._SysDataSpace = params.get("SysDataSpace")
        self._HyperThreading = params.get("HyperThreading")
        self._LanIps = params.get("LanIps")
        self._Aliases = params.get("Aliases")
        self._CpuId = params.get("CpuId")
        self._ContainRaidCard = params.get("ContainRaidCard")
        self._MemSize = params.get("MemSize")
        self._SystemDiskTypeId = params.get("SystemDiskTypeId")
        self._SystemDiskCount = params.get("SystemDiskCount")
        self._DataDiskTypeId = params.get("DataDiskTypeId")
        self._DataDiskCount = params.get("DataDiskCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._FileSystem = params.get("FileSystem")
        self._BuySession = params.get("BuySession")
        self._SgId = params.get("SgId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuyDevicesResponse(AbstractModel):
    """BuyDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 购买的物理机实例ID列表
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIds = None
        self._RequestId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CpuInfo(AbstractModel):
    """cpu信息

    """

    def __init__(self):
        r"""
        :param _CpuId: CPU的ID
        :type CpuId: int
        :param _CpuDescription: CPU型号描述
        :type CpuDescription: str
        :param _Series: 机型序列
        :type Series: int
        :param _ContainRaidCard: 支持的RAID方式，0：有RAID卡，1：没有RAID卡
        :type ContainRaidCard: list of int non-negative
        """
        self._CpuId = None
        self._CpuDescription = None
        self._Series = None
        self._ContainRaidCard = None

    @property
    def CpuId(self):
        return self._CpuId

    @CpuId.setter
    def CpuId(self, CpuId):
        self._CpuId = CpuId

    @property
    def CpuDescription(self):
        return self._CpuDescription

    @CpuDescription.setter
    def CpuDescription(self, CpuDescription):
        self._CpuDescription = CpuDescription

    @property
    def Series(self):
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def ContainRaidCard(self):
        return self._ContainRaidCard

    @ContainRaidCard.setter
    def ContainRaidCard(self, ContainRaidCard):
        self._ContainRaidCard = ContainRaidCard


    def _deserialize(self, params):
        self._CpuId = params.get("CpuId")
        self._CpuDescription = params.get("CpuDescription")
        self._Series = params.get("Series")
        self._ContainRaidCard = params.get("ContainRaidCard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomImageRequest(AbstractModel):
    """CreateCustomImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 用于制作镜像的物理机ID
        :type InstanceId: str
        :param _ImageName: 镜像别名
        :type ImageName: str
        :param _ImageDescription: 镜像描述
        :type ImageDescription: str
        """
        self._InstanceId = None
        self._ImageName = None
        self._ImageDescription = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomImageResponse(AbstractModel):
    """CreateCustomImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ImageId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._ImageId = params.get("ImageId")
        self._RequestId = params.get("RequestId")


class CreatePsaRegulationRequest(AbstractModel):
    """CreatePsaRegulation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PsaName: 规则别名
        :type PsaName: str
        :param _TaskTypeIds: 关联的故障类型ID列表
        :type TaskTypeIds: list of int non-negative
        :param _RepairLimit: 维修实例上限，默认为5
        :type RepairLimit: int
        :param _PsaDescription: 规则备注
        :type PsaDescription: str
        """
        self._PsaName = None
        self._TaskTypeIds = None
        self._RepairLimit = None
        self._PsaDescription = None

    @property
    def PsaName(self):
        return self._PsaName

    @PsaName.setter
    def PsaName(self, PsaName):
        self._PsaName = PsaName

    @property
    def TaskTypeIds(self):
        return self._TaskTypeIds

    @TaskTypeIds.setter
    def TaskTypeIds(self, TaskTypeIds):
        self._TaskTypeIds = TaskTypeIds

    @property
    def RepairLimit(self):
        return self._RepairLimit

    @RepairLimit.setter
    def RepairLimit(self, RepairLimit):
        self._RepairLimit = RepairLimit

    @property
    def PsaDescription(self):
        return self._PsaDescription

    @PsaDescription.setter
    def PsaDescription(self, PsaDescription):
        self._PsaDescription = PsaDescription


    def _deserialize(self, params):
        self._PsaName = params.get("PsaName")
        self._TaskTypeIds = params.get("TaskTypeIds")
        self._RepairLimit = params.get("RepairLimit")
        self._PsaDescription = params.get("PsaDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePsaRegulationResponse(AbstractModel):
    """CreatePsaRegulation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PsaId: 创建的预授权规则ID
        :type PsaId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PsaId = None
        self._RequestId = None

    @property
    def PsaId(self):
        return self._PsaId

    @PsaId.setter
    def PsaId(self, PsaId):
        self._PsaId = PsaId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PsaId = params.get("PsaId")
        self._RequestId = params.get("RequestId")


class CreateSpotDeviceRequest(AbstractModel):
    """CreateSpotDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区名称。如ap-guangzhou-bls-1, 通过DescribeRegions获取
        :type Zone: str
        :param _ComputeType: 计算单元类型, 如v3.c2.medium，更详细的ComputeType参考[竞价实例产品文档](https://cloud.tencent.com/document/product/386/30256)
        :type ComputeType: str
        :param _OsTypeId: 操作系统类型ID
        :type OsTypeId: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _GoodsNum: 购买的计算单元个数
        :type GoodsNum: int
        :param _SpotStrategy: 出价策略。可取值为SpotWithPriceLimit和SpotAsPriceGo。SpotWithPriceLimit，用户设置价格上限，需要传SpotPriceLimit参数， 如果市场价高于用户的指定价格，则购买不成功;  SpotAsPriceGo 是随市场价的策略。
        :type SpotStrategy: str
        :param _SpotPriceLimit: 用户设置的价格。当为SpotWithPriceLimit竞价策略时有效
        :type SpotPriceLimit: float
        :param _Passwd: 设置竞价实例密码。可选参数，没有指定会生成随机密码
        :type Passwd: str
        """
        self._Zone = None
        self._ComputeType = None
        self._OsTypeId = None
        self._VpcId = None
        self._SubnetId = None
        self._GoodsNum = None
        self._SpotStrategy = None
        self._SpotPriceLimit = None
        self._Passwd = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ComputeType(self):
        return self._ComputeType

    @ComputeType.setter
    def ComputeType(self, ComputeType):
        self._ComputeType = ComputeType

    @property
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId

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
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def SpotStrategy(self):
        return self._SpotStrategy

    @SpotStrategy.setter
    def SpotStrategy(self, SpotStrategy):
        self._SpotStrategy = SpotStrategy

    @property
    def SpotPriceLimit(self):
        return self._SpotPriceLimit

    @SpotPriceLimit.setter
    def SpotPriceLimit(self, SpotPriceLimit):
        self._SpotPriceLimit = SpotPriceLimit

    @property
    def Passwd(self):
        return self._Passwd

    @Passwd.setter
    def Passwd(self, Passwd):
        self._Passwd = Passwd


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ComputeType = params.get("ComputeType")
        self._OsTypeId = params.get("OsTypeId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._GoodsNum = params.get("GoodsNum")
        self._SpotStrategy = params.get("SpotStrategy")
        self._SpotPriceLimit = params.get("SpotPriceLimit")
        self._Passwd = params.get("Passwd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSpotDeviceResponse(AbstractModel):
    """CreateSpotDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 创建的服务器ID
        :type ResourceIds: list of str
        :param _FlowId: 任务ID
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceIds = None
        self._FlowId = None
        self._RequestId = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateUserCmdRequest(AbstractModel):
    """CreateUserCmd请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 用户自定义脚本的名称
        :type Alias: str
        :param _OsType: 命令适用的操作系统类型，取值linux或xserver
        :type OsType: str
        :param _Content: 脚本内容，必须经过base64编码
        :type Content: str
        """
        self._Alias = None
        self._OsType = None
        self._Content = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._OsType = params.get("OsType")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserCmdResponse(AbstractModel):
    """CreateUserCmd返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdId: 脚本ID
        :type CmdId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CmdId = None
        self._RequestId = None

    @property
    def CmdId(self):
        return self._CmdId

    @CmdId.setter
    def CmdId(self, CmdId):
        self._CmdId = CmdId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CmdId = params.get("CmdId")
        self._RequestId = params.get("RequestId")


class CustomImage(AbstractModel):
    """自定义镜像信息

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _ImageName: 镜像别名
        :type ImageName: str
        :param _ImageStatus: 镜像状态码
        :type ImageStatus: int
        :param _OsClass: 镜像OS名
        :type OsClass: str
        :param _OsVersion: 镜像OS版本
        :type OsVersion: str
        :param _OsBit: OS是64还是32位
        :type OsBit: int
        :param _ImageSize: 镜像大小(M)
        :type ImageSize: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PartitionInfoSet: 分区信息
        :type PartitionInfoSet: list of PartitionInfo
        :param _DeviceClassCode: 适用机型
        :type DeviceClassCode: str
        :param _ImageDescription: 备注
        :type ImageDescription: str
        :param _OsTypeId: 原始镜像id
        :type OsTypeId: int
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageStatus = None
        self._OsClass = None
        self._OsVersion = None
        self._OsBit = None
        self._ImageSize = None
        self._CreateTime = None
        self._PartitionInfoSet = None
        self._DeviceClassCode = None
        self._ImageDescription = None
        self._OsTypeId = None

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
    def ImageStatus(self):
        return self._ImageStatus

    @ImageStatus.setter
    def ImageStatus(self, ImageStatus):
        self._ImageStatus = ImageStatus

    @property
    def OsClass(self):
        return self._OsClass

    @OsClass.setter
    def OsClass(self, OsClass):
        self._OsClass = OsClass

    @property
    def OsVersion(self):
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def OsBit(self):
        return self._OsBit

    @OsBit.setter
    def OsBit(self, OsBit):
        self._OsBit = OsBit

    @property
    def ImageSize(self):
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PartitionInfoSet(self):
        return self._PartitionInfoSet

    @PartitionInfoSet.setter
    def PartitionInfoSet(self, PartitionInfoSet):
        self._PartitionInfoSet = PartitionInfoSet

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

    @property
    def ImageDescription(self):
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageStatus = params.get("ImageStatus")
        self._OsClass = params.get("OsClass")
        self._OsVersion = params.get("OsVersion")
        self._OsBit = params.get("OsBit")
        self._ImageSize = params.get("ImageSize")
        self._CreateTime = params.get("CreateTime")
        if params.get("PartitionInfoSet") is not None:
            self._PartitionInfoSet = []
            for item in params.get("PartitionInfoSet"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self._PartitionInfoSet.append(obj)
        self._DeviceClassCode = params.get("DeviceClassCode")
        self._ImageDescription = params.get("ImageDescription")
        self._OsTypeId = params.get("OsTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomImageProcess(AbstractModel):
    """镜像制作进度列表

    """

    def __init__(self):
        r"""
        :param _StepName: 步骤
        :type StepName: str
        :param _StartTime: 此步骤开始时间
        :type StartTime: str
        :param _StepType: 0: 已完成 1: 当前进行 2: 未开始
        :type StepType: int
        """
        self._StepName = None
        self._StartTime = None
        self._StepType = None

    @property
    def StepName(self):
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StepType(self):
        return self._StepType

    @StepType.setter
    def StepType(self, StepType):
        self._StepType = StepType


    def _deserialize(self, params):
        self._StepName = params.get("StepName")
        self._StartTime = params.get("StartTime")
        self._StepType = params.get("StepType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomImagesRequest(AbstractModel):
    """DeleteCustomImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageIds: 准备删除的镜像ID列表
        :type ImageIds: list of str
        """
        self._ImageIds = None

    @property
    def ImageIds(self):
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomImagesResponse(AbstractModel):
    """DeleteCustomImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
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


class DeletePsaRegulationRequest(AbstractModel):
    """DeletePsaRegulation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PsaId: 预授权规则ID
        :type PsaId: str
        """
        self._PsaId = None

    @property
    def PsaId(self):
        return self._PsaId

    @PsaId.setter
    def PsaId(self, PsaId):
        self._PsaId = PsaId


    def _deserialize(self, params):
        self._PsaId = params.get("PsaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePsaRegulationResponse(AbstractModel):
    """DeletePsaRegulation返回参数结构体

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


class DeleteUserCmdsRequest(AbstractModel):
    """DeleteUserCmds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdIds: 需要删除的脚本ID
        :type CmdIds: list of str
        """
        self._CmdIds = None

    @property
    def CmdIds(self):
        return self._CmdIds

    @CmdIds.setter
    def CmdIds(self, CmdIds):
        self._CmdIds = CmdIds


    def _deserialize(self, params):
        self._CmdIds = params.get("CmdIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserCmdsResponse(AbstractModel):
    """DeleteUserCmds返回参数结构体

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


class DescribeCustomImageProcessRequest(AbstractModel):
    """DescribeCustomImageProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
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
        


class DescribeCustomImageProcessResponse(AbstractModel):
    """DescribeCustomImageProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomImageProcessSet: 镜像制作进度
        :type CustomImageProcessSet: list of CustomImageProcess
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomImageProcessSet = None
        self._RequestId = None

    @property
    def CustomImageProcessSet(self):
        return self._CustomImageProcessSet

    @CustomImageProcessSet.setter
    def CustomImageProcessSet(self, CustomImageProcessSet):
        self._CustomImageProcessSet = CustomImageProcessSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomImageProcessSet") is not None:
            self._CustomImageProcessSet = []
            for item in params.get("CustomImageProcessSet"):
                obj = CustomImageProcess()
                obj._deserialize(item)
                self._CustomImageProcessSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomImagesRequest(AbstractModel):
    """DescribeCustomImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量限制
        :type Limit: int
        :param _OrderField: 排序字段，仅支持CreateTime
        :type OrderField: str
        :param _Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        :param _ImageId: 按ImageId查找指定镜像信息，ImageId字段存在时其他字段失效
        :type ImageId: str
        :param _SearchKey: 模糊查询过滤，可以查询镜像ID或镜像名
        :type SearchKey: str
        :param _ImageStatus: <ul>
镜像状态过滤列表，有效取值为：
<li>1：制作中</li>
<li>2：制作失败</li>
<li>3：正常</li>
<li>4：删除中</li>
</ul>
        :type ImageStatus: list of int non-negative
        """
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._ImageId = None
        self._SearchKey = None
        self._ImageStatus = None

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

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ImageStatus(self):
        return self._ImageStatus

    @ImageStatus.setter
    def ImageStatus(self, ImageStatus):
        self._ImageStatus = ImageStatus


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._ImageId = params.get("ImageId")
        self._SearchKey = params.get("SearchKey")
        self._ImageStatus = params.get("ImageStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomImagesResponse(AbstractModel):
    """DescribeCustomImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回镜像数量
        :type TotalCount: int
        :param _CustomImageSet: 镜像信息列表
        :type CustomImageSet: list of CustomImage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CustomImageSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CustomImageSet(self):
        return self._CustomImageSet

    @CustomImageSet.setter
    def CustomImageSet(self, CustomImageSet):
        self._CustomImageSet = CustomImageSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CustomImageSet") is not None:
            self._CustomImageSet = []
            for item in params.get("CustomImageSet"):
                obj = CustomImage()
                obj._deserialize(item)
                self._CustomImageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceClassPartitionRequest(AbstractModel):
    """DescribeDeviceClassPartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceClassCode: 设备类型代号。代号通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)查询。标准机型需要传入此参数。虽是可选参数，但DeviceClassCode和InstanceId参数，必须要填写一个。
        :type DeviceClassCode: str
        :param _InstanceId: 需要查询自定义机型RAID信息时，传入自定义机型实例ID。InstanceId存在时其余参数失效。
        :type InstanceId: str
        :param _CpuId: CPU型号ID，查询自定义机型时需要传入
        :type CpuId: int
        :param _MemSize: 内存大小，单位为G，查询自定义机型时需要传入
        :type MemSize: int
        :param _ContainRaidCard: 是否有RAID卡，取值：1(有) 0(无)。查询自定义机型时需要传入
        :type ContainRaidCard: int
        :param _SystemDiskTypeId: 系统盘类型ID，查询自定义机型时需要传入
        :type SystemDiskTypeId: int
        :param _SystemDiskCount: 系统盘数量，查询自定义机型时需要传入
        :type SystemDiskCount: int
        :param _DataDiskTypeId: 数据盘类型ID，查询自定义机型时可传入
        :type DataDiskTypeId: int
        :param _DataDiskCount: 数据盘数量，查询自定义机型时可传入
        :type DataDiskCount: int
        """
        self._DeviceClassCode = None
        self._InstanceId = None
        self._CpuId = None
        self._MemSize = None
        self._ContainRaidCard = None
        self._SystemDiskTypeId = None
        self._SystemDiskCount = None
        self._DataDiskTypeId = None
        self._DataDiskCount = None

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CpuId(self):
        return self._CpuId

    @CpuId.setter
    def CpuId(self, CpuId):
        self._CpuId = CpuId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def ContainRaidCard(self):
        return self._ContainRaidCard

    @ContainRaidCard.setter
    def ContainRaidCard(self, ContainRaidCard):
        self._ContainRaidCard = ContainRaidCard

    @property
    def SystemDiskTypeId(self):
        return self._SystemDiskTypeId

    @SystemDiskTypeId.setter
    def SystemDiskTypeId(self, SystemDiskTypeId):
        self._SystemDiskTypeId = SystemDiskTypeId

    @property
    def SystemDiskCount(self):
        return self._SystemDiskCount

    @SystemDiskCount.setter
    def SystemDiskCount(self, SystemDiskCount):
        self._SystemDiskCount = SystemDiskCount

    @property
    def DataDiskTypeId(self):
        return self._DataDiskTypeId

    @DataDiskTypeId.setter
    def DataDiskTypeId(self, DataDiskTypeId):
        self._DataDiskTypeId = DataDiskTypeId

    @property
    def DataDiskCount(self):
        return self._DataDiskCount

    @DataDiskCount.setter
    def DataDiskCount(self, DataDiskCount):
        self._DataDiskCount = DataDiskCount


    def _deserialize(self, params):
        self._DeviceClassCode = params.get("DeviceClassCode")
        self._InstanceId = params.get("InstanceId")
        self._CpuId = params.get("CpuId")
        self._MemSize = params.get("MemSize")
        self._ContainRaidCard = params.get("ContainRaidCard")
        self._SystemDiskTypeId = params.get("SystemDiskTypeId")
        self._SystemDiskCount = params.get("SystemDiskCount")
        self._DataDiskTypeId = params.get("DataDiskTypeId")
        self._DataDiskCount = params.get("DataDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceClassPartitionResponse(AbstractModel):
    """DescribeDeviceClassPartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceClassPartitionInfoSet: 支持的RAID格式列表
        :type DeviceClassPartitionInfoSet: list of DeviceClassPartitionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceClassPartitionInfoSet = None
        self._RequestId = None

    @property
    def DeviceClassPartitionInfoSet(self):
        return self._DeviceClassPartitionInfoSet

    @DeviceClassPartitionInfoSet.setter
    def DeviceClassPartitionInfoSet(self, DeviceClassPartitionInfoSet):
        self._DeviceClassPartitionInfoSet = DeviceClassPartitionInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceClassPartitionInfoSet") is not None:
            self._DeviceClassPartitionInfoSet = []
            for item in params.get("DeviceClassPartitionInfoSet"):
                obj = DeviceClassPartitionInfo()
                obj._deserialize(item)
                self._DeviceClassPartitionInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceClassRequest(AbstractModel):
    """DescribeDeviceClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OnSale: 是否仅查询在售标准机型配置信息。取值0：查询所有机型；1：查询在售机型。默认为1
        :type OnSale: int
        :param _NeedPriceInfo: 是否返回价格信息。取值0：不返回价格信息，接口返回速度更快；1：返回价格信息。默认为1
        :type NeedPriceInfo: int
        """
        self._OnSale = None
        self._NeedPriceInfo = None

    @property
    def OnSale(self):
        return self._OnSale

    @OnSale.setter
    def OnSale(self, OnSale):
        self._OnSale = OnSale

    @property
    def NeedPriceInfo(self):
        return self._NeedPriceInfo

    @NeedPriceInfo.setter
    def NeedPriceInfo(self, NeedPriceInfo):
        self._NeedPriceInfo = NeedPriceInfo


    def _deserialize(self, params):
        self._OnSale = params.get("OnSale")
        self._NeedPriceInfo = params.get("NeedPriceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceClassResponse(AbstractModel):
    """DescribeDeviceClass返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceClassSet: 物理机设备类型列表
        :type DeviceClassSet: list of DeviceClass
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceClassSet = None
        self._RequestId = None

    @property
    def DeviceClassSet(self):
        return self._DeviceClassSet

    @DeviceClassSet.setter
    def DeviceClassSet(self, DeviceClassSet):
        self._DeviceClassSet = DeviceClassSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceClassSet") is not None:
            self._DeviceClassSet = []
            for item in params.get("DeviceClassSet"):
                obj = DeviceClass()
                obj._deserialize(item)
                self._DeviceClassSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceHardwareInfoRequest(AbstractModel):
    """DescribeDeviceHardwareInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 设备 ID 列表
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
        


class DescribeDeviceHardwareInfoResponse(AbstractModel):
    """DescribeDeviceHardwareInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceHardwareInfoSet: 设备硬件配置信息
        :type DeviceHardwareInfoSet: list of DeviceHardwareInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceHardwareInfoSet = None
        self._RequestId = None

    @property
    def DeviceHardwareInfoSet(self):
        return self._DeviceHardwareInfoSet

    @DeviceHardwareInfoSet.setter
    def DeviceHardwareInfoSet(self, DeviceHardwareInfoSet):
        self._DeviceHardwareInfoSet = DeviceHardwareInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceHardwareInfoSet") is not None:
            self._DeviceHardwareInfoSet = []
            for item in params.get("DeviceHardwareInfoSet"):
                obj = DeviceHardwareInfo()
                obj._deserialize(item)
                self._DeviceHardwareInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceInventoryRequest(AbstractModel):
    """DescribeDeviceInventory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _DeviceClassCode: 设备型号
        :type DeviceClassCode: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _CpuId: CPU型号ID，查询自定义机型时必填
        :type CpuId: int
        :param _MemSize: 内存大小，单位为G，查询自定义机型时必填
        :type MemSize: int
        :param _ContainRaidCard: 是否有RAID卡，取值：1(有) 0(无)，查询自定义机型时必填
        :type ContainRaidCard: int
        :param _SystemDiskTypeId: 系统盘类型ID，查询自定义机型时必填
        :type SystemDiskTypeId: int
        :param _SystemDiskCount: 系统盘数量，查询自定义机型时必填
        :type SystemDiskCount: int
        :param _DataDiskTypeId: 数据盘类型ID，查询自定义机型时可填
        :type DataDiskTypeId: int
        :param _DataDiskCount: 数据盘数量，查询自定义机型时可填
        :type DataDiskCount: int
        """
        self._Zone = None
        self._DeviceClassCode = None
        self._VpcId = None
        self._SubnetId = None
        self._CpuId = None
        self._MemSize = None
        self._ContainRaidCard = None
        self._SystemDiskTypeId = None
        self._SystemDiskCount = None
        self._DataDiskTypeId = None
        self._DataDiskCount = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

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
    def CpuId(self):
        return self._CpuId

    @CpuId.setter
    def CpuId(self, CpuId):
        self._CpuId = CpuId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def ContainRaidCard(self):
        return self._ContainRaidCard

    @ContainRaidCard.setter
    def ContainRaidCard(self, ContainRaidCard):
        self._ContainRaidCard = ContainRaidCard

    @property
    def SystemDiskTypeId(self):
        return self._SystemDiskTypeId

    @SystemDiskTypeId.setter
    def SystemDiskTypeId(self, SystemDiskTypeId):
        self._SystemDiskTypeId = SystemDiskTypeId

    @property
    def SystemDiskCount(self):
        return self._SystemDiskCount

    @SystemDiskCount.setter
    def SystemDiskCount(self, SystemDiskCount):
        self._SystemDiskCount = SystemDiskCount

    @property
    def DataDiskTypeId(self):
        return self._DataDiskTypeId

    @DataDiskTypeId.setter
    def DataDiskTypeId(self, DataDiskTypeId):
        self._DataDiskTypeId = DataDiskTypeId

    @property
    def DataDiskCount(self):
        return self._DataDiskCount

    @DataDiskCount.setter
    def DataDiskCount(self, DataDiskCount):
        self._DataDiskCount = DataDiskCount


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DeviceClassCode = params.get("DeviceClassCode")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CpuId = params.get("CpuId")
        self._MemSize = params.get("MemSize")
        self._ContainRaidCard = params.get("ContainRaidCard")
        self._SystemDiskTypeId = params.get("SystemDiskTypeId")
        self._SystemDiskCount = params.get("SystemDiskCount")
        self._DataDiskTypeId = params.get("DataDiskTypeId")
        self._DataDiskCount = params.get("DataDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceInventoryResponse(AbstractModel):
    """DescribeDeviceInventory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceCount: 库存设备数量
        :type DeviceCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceCount = None
        self._RequestId = None

    @property
    def DeviceCount(self):
        return self._DeviceCount

    @DeviceCount.setter
    def DeviceCount(self, DeviceCount):
        self._DeviceCount = DeviceCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceCount = params.get("DeviceCount")
        self._RequestId = params.get("RequestId")


class DescribeDeviceOperationLogRequest(AbstractModel):
    """DescribeDeviceOperationLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 设备实例ID
        :type InstanceId: str
        :param _StartTime: 查询开始日期
        :type StartTime: str
        :param _EndTime: 查询结束日期
        :type EndTime: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceOperationLogResponse(AbstractModel):
    """DescribeDeviceOperationLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceOperationLogSet: 操作日志列表
        :type DeviceOperationLogSet: list of DeviceOperationLog
        :param _TotalCount: 返回数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceOperationLogSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DeviceOperationLogSet(self):
        return self._DeviceOperationLogSet

    @DeviceOperationLogSet.setter
    def DeviceOperationLogSet(self, DeviceOperationLogSet):
        self._DeviceOperationLogSet = DeviceOperationLogSet

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
        if params.get("DeviceOperationLogSet") is not None:
            self._DeviceOperationLogSet = []
            for item in params.get("DeviceOperationLogSet"):
                obj = DeviceOperationLog()
                obj._deserialize(item)
                self._DeviceOperationLogSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDevicePartitionRequest(AbstractModel):
    """DescribeDevicePartition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机ID
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
        


class DescribeDevicePartitionResponse(AbstractModel):
    """DescribeDevicePartition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DevicePartition: 物理机分区格式
        :type DevicePartition: :class:`tencentcloud.bm.v20180423.models.DevicePartition`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DevicePartition = None
        self._RequestId = None

    @property
    def DevicePartition(self):
        return self._DevicePartition

    @DevicePartition.setter
    def DevicePartition(self, DevicePartition):
        self._DevicePartition = DevicePartition

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DevicePartition") is not None:
            self._DevicePartition = DevicePartition()
            self._DevicePartition._deserialize(params.get("DevicePartition"))
        self._RequestId = params.get("RequestId")


class DescribeDevicePositionRequest(AbstractModel):
    """DescribeDevicePosition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量限制
        :type Limit: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _Alias: 实例别名
        :type Alias: str
        """
        self._Offset = None
        self._Limit = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceIds = None
        self._Alias = None

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceIds = params.get("InstanceIds")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePositionResponse(AbstractModel):
    """DescribeDevicePosition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回数量
        :type TotalCount: int
        :param _DevicePositionInfoSet: 设备所在机架信息
        :type DevicePositionInfoSet: list of DevicePositionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DevicePositionInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DevicePositionInfoSet(self):
        return self._DevicePositionInfoSet

    @DevicePositionInfoSet.setter
    def DevicePositionInfoSet(self, DevicePositionInfoSet):
        self._DevicePositionInfoSet = DevicePositionInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DevicePositionInfoSet") is not None:
            self._DevicePositionInfoSet = []
            for item in params.get("DevicePositionInfoSet"):
                obj = DevicePositionInfo()
                obj._deserialize(item)
                self._DevicePositionInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicePriceInfoRequest(AbstractModel):
    """DescribeDevicePriceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要查询的实例列表
        :type InstanceIds: list of str
        :param _TimeUnit: 购买时长单位，当前只支持取值为m
        :type TimeUnit: str
        :param _TimeSpan: 购买时长
        :type TimeSpan: int
        """
        self._InstanceIds = None
        self._TimeUnit = None
        self._TimeSpan = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePriceInfoResponse(AbstractModel):
    """DescribeDevicePriceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DevicePriceInfoSet: 服务器价格信息列表
        :type DevicePriceInfoSet: list of DevicePriceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DevicePriceInfoSet = None
        self._RequestId = None

    @property
    def DevicePriceInfoSet(self):
        return self._DevicePriceInfoSet

    @DevicePriceInfoSet.setter
    def DevicePriceInfoSet(self, DevicePriceInfoSet):
        self._DevicePriceInfoSet = DevicePriceInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DevicePriceInfoSet") is not None:
            self._DevicePriceInfoSet = []
            for item in params.get("DevicePriceInfoSet"):
                obj = DevicePriceInfo()
                obj._deserialize(item)
                self._DevicePriceInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _DeviceClassCode: 机型ID，通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)查询
        :type DeviceClassCode: str
        :param _InstanceIds: 设备ID数组
        :type InstanceIds: list of str
        :param _WanIps: 外网IP数组
        :type WanIps: list of str
        :param _LanIps: 内网IP数组
        :type LanIps: list of str
        :param _Alias: 设备名称
        :type Alias: str
        :param _VagueIp: 模糊IP查询
        :type VagueIp: str
        :param _DeadlineStartTime: 设备到期时间查询的起始时间
        :type DeadlineStartTime: str
        :param _DeadlineEndTime: 设备到期时间查询的结束时间
        :type DeadlineEndTime: str
        :param _AutoRenewFlag: 自动续费标志 0:不自动续费，1:自动续费
        :type AutoRenewFlag: int
        :param _VpcId: 私有网络唯一ID
        :type VpcId: str
        :param _SubnetId: 子网唯一ID
        :type SubnetId: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _DeviceType: 设备类型，取值有: compute(计算型), standard(标准型), storage(存储型) 等
        :type DeviceType: str
        :param _IsLuckyDevice: 竞价实例机器的过滤。如果未指定此参数，则不做过滤。0: 查询非竞价实例的机器; 1: 查询竞价实例的机器。
        :type IsLuckyDevice: int
        :param _OrderField: 排序字段
        :type OrderField: str
        :param _Order: 排序方式，取值：0:增序(默认)，1:降序
        :type Order: int
        :param _MaintainStatus: 按照维保方式过滤。可取值为 Maintain: 在保;  WillExpire: 即将过保; Expire: 已过保
        :type MaintainStatus: str
        """
        self._Offset = None
        self._Limit = None
        self._DeviceClassCode = None
        self._InstanceIds = None
        self._WanIps = None
        self._LanIps = None
        self._Alias = None
        self._VagueIp = None
        self._DeadlineStartTime = None
        self._DeadlineEndTime = None
        self._AutoRenewFlag = None
        self._VpcId = None
        self._SubnetId = None
        self._Tags = None
        self._DeviceType = None
        self._IsLuckyDevice = None
        self._OrderField = None
        self._Order = None
        self._MaintainStatus = None

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
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def WanIps(self):
        return self._WanIps

    @WanIps.setter
    def WanIps(self, WanIps):
        self._WanIps = WanIps

    @property
    def LanIps(self):
        return self._LanIps

    @LanIps.setter
    def LanIps(self, LanIps):
        self._LanIps = LanIps

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def VagueIp(self):
        return self._VagueIp

    @VagueIp.setter
    def VagueIp(self, VagueIp):
        self._VagueIp = VagueIp

    @property
    def DeadlineStartTime(self):
        return self._DeadlineStartTime

    @DeadlineStartTime.setter
    def DeadlineStartTime(self, DeadlineStartTime):
        self._DeadlineStartTime = DeadlineStartTime

    @property
    def DeadlineEndTime(self):
        return self._DeadlineEndTime

    @DeadlineEndTime.setter
    def DeadlineEndTime(self, DeadlineEndTime):
        self._DeadlineEndTime = DeadlineEndTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

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
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def IsLuckyDevice(self):
        return self._IsLuckyDevice

    @IsLuckyDevice.setter
    def IsLuckyDevice(self, IsLuckyDevice):
        self._IsLuckyDevice = IsLuckyDevice

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

    @property
    def MaintainStatus(self):
        return self._MaintainStatus

    @MaintainStatus.setter
    def MaintainStatus(self, MaintainStatus):
        self._MaintainStatus = MaintainStatus


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DeviceClassCode = params.get("DeviceClassCode")
        self._InstanceIds = params.get("InstanceIds")
        self._WanIps = params.get("WanIps")
        self._LanIps = params.get("LanIps")
        self._Alias = params.get("Alias")
        self._VagueIp = params.get("VagueIp")
        self._DeadlineStartTime = params.get("DeadlineStartTime")
        self._DeadlineEndTime = params.get("DeadlineEndTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeviceType = params.get("DeviceType")
        self._IsLuckyDevice = params.get("IsLuckyDevice")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._MaintainStatus = params.get("MaintainStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回数量
        :type TotalCount: int
        :param _DeviceInfoSet: 物理机信息列表
        :type DeviceInfoSet: list of DeviceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeviceInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceInfoSet(self):
        return self._DeviceInfoSet

    @DeviceInfoSet.setter
    def DeviceInfoSet(self, DeviceInfoSet):
        self._DeviceInfoSet = DeviceInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeviceInfoSet") is not None:
            self._DeviceInfoSet = []
            for item in params.get("DeviceInfoSet"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._DeviceInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHardwareSpecificationRequest(AbstractModel):
    """DescribeHardwareSpecification请求参数结构体

    """


class DescribeHardwareSpecificationResponse(AbstractModel):
    """DescribeHardwareSpecification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CpuInfoSet: CPU型号列表
        :type CpuInfoSet: list of CpuInfo
        :param _MemSet: 内存的取值，单位为G
        :type MemSet: list of int non-negative
        :param _DiskInfoSet: 硬盘型号列表
        :type DiskInfoSet: list of DiskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CpuInfoSet = None
        self._MemSet = None
        self._DiskInfoSet = None
        self._RequestId = None

    @property
    def CpuInfoSet(self):
        return self._CpuInfoSet

    @CpuInfoSet.setter
    def CpuInfoSet(self, CpuInfoSet):
        self._CpuInfoSet = CpuInfoSet

    @property
    def MemSet(self):
        return self._MemSet

    @MemSet.setter
    def MemSet(self, MemSet):
        self._MemSet = MemSet

    @property
    def DiskInfoSet(self):
        return self._DiskInfoSet

    @DiskInfoSet.setter
    def DiskInfoSet(self, DiskInfoSet):
        self._DiskInfoSet = DiskInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CpuInfoSet") is not None:
            self._CpuInfoSet = []
            for item in params.get("CpuInfoSet"):
                obj = CpuInfo()
                obj._deserialize(item)
                self._CpuInfoSet.append(obj)
        self._MemSet = params.get("MemSet")
        if params.get("DiskInfoSet") is not None:
            self._DiskInfoSet = []
            for item in params.get("DiskInfoSet"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DiskInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostedDeviceOutBandInfoRequest(AbstractModel):
    """DescribeHostedDeviceOutBandInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 托管设备的唯一ID数组,数组个数不超过20
        :type InstanceIds: list of str
        :param _Zone: 可用区ID
        :type Zone: str
        """
        self._InstanceIds = None
        self._Zone = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostedDeviceOutBandInfoResponse(AbstractModel):
    """DescribeHostedDeviceOutBandInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HostedDeviceOutBandInfoSet: 托管设备带外信息
        :type HostedDeviceOutBandInfoSet: list of HostedDeviceOutBandInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HostedDeviceOutBandInfoSet = None
        self._RequestId = None

    @property
    def HostedDeviceOutBandInfoSet(self):
        return self._HostedDeviceOutBandInfoSet

    @HostedDeviceOutBandInfoSet.setter
    def HostedDeviceOutBandInfoSet(self, HostedDeviceOutBandInfoSet):
        self._HostedDeviceOutBandInfoSet = HostedDeviceOutBandInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HostedDeviceOutBandInfoSet") is not None:
            self._HostedDeviceOutBandInfoSet = []
            for item in params.get("HostedDeviceOutBandInfoSet"):
                obj = HostedDeviceOutBandInfo()
                obj._deserialize(item)
                self._HostedDeviceOutBandInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOperationResultRequest(AbstractModel):
    """DescribeOperationResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOperationResultResponse(AbstractModel):
    """DescribeOperationResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 任务的整体状态，取值如下：<br>
1：成功<br>
2：失败<br>
3：部分成功，部分失败<br>
4：未完成<br>
5：部分成功，部分未完成<br>
6：部分未完成，部分失败<br>
7：部分未完成，部分失败，部分成功
        :type TaskStatus: int
        :param _SubtaskStatusSet: 各实例对应任务的状态ID
        :type SubtaskStatusSet: list of SubtaskStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._SubtaskStatusSet = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def SubtaskStatusSet(self):
        return self._SubtaskStatusSet

    @SubtaskStatusSet.setter
    def SubtaskStatusSet(self, SubtaskStatusSet):
        self._SubtaskStatusSet = SubtaskStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskStatus = params.get("TaskStatus")
        if params.get("SubtaskStatusSet") is not None:
            self._SubtaskStatusSet = []
            for item in params.get("SubtaskStatusSet"):
                obj = SubtaskStatus()
                obj._deserialize(item)
                self._SubtaskStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOsInfoRequest(AbstractModel):
    """DescribeOsInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceClassCode: 设备类型代号。 可以从DescribeDeviceClass查询设备类型列表
        :type DeviceClassCode: str
        """
        self._DeviceClassCode = None

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode


    def _deserialize(self, params):
        self._DeviceClassCode = params.get("DeviceClassCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOsInfoResponse(AbstractModel):
    """DescribeOsInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OsInfoSet: 操作系统信息列表
        :type OsInfoSet: list of OsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OsInfoSet = None
        self._RequestId = None

    @property
    def OsInfoSet(self):
        return self._OsInfoSet

    @OsInfoSet.setter
    def OsInfoSet(self, OsInfoSet):
        self._OsInfoSet = OsInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OsInfoSet") is not None:
            self._OsInfoSet = []
            for item in params.get("OsInfoSet"):
                obj = OsInfo()
                obj._deserialize(item)
                self._OsInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePsaRegulationsRequest(AbstractModel):
    """DescribePsaRegulations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量限制
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _PsaIds: 规则ID过滤，支持模糊查询
        :type PsaIds: list of str
        :param _PsaNames: 规则别名过滤，支持模糊查询
        :type PsaNames: list of str
        :param _Tags: 标签过滤
        :type Tags: list of Tag
        :param _OrderField: 排序字段，取值支持：CreateTime
        :type OrderField: str
        :param _Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        """
        self._Limit = None
        self._Offset = None
        self._PsaIds = None
        self._PsaNames = None
        self._Tags = None
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
    def PsaIds(self):
        return self._PsaIds

    @PsaIds.setter
    def PsaIds(self, PsaIds):
        self._PsaIds = PsaIds

    @property
    def PsaNames(self):
        return self._PsaNames

    @PsaNames.setter
    def PsaNames(self, PsaNames):
        self._PsaNames = PsaNames

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

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
        self._PsaIds = params.get("PsaIds")
        self._PsaNames = params.get("PsaNames")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePsaRegulationsResponse(AbstractModel):
    """DescribePsaRegulations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回规则数量
        :type TotalCount: int
        :param _PsaRegulations: 返回规则列表
        :type PsaRegulations: list of PsaRegulation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PsaRegulations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PsaRegulations(self):
        return self._PsaRegulations

    @PsaRegulations.setter
    def PsaRegulations(self, PsaRegulations):
        self._PsaRegulations = PsaRegulations

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PsaRegulations") is not None:
            self._PsaRegulations = []
            for item in params.get("PsaRegulations"):
                obj = PsaRegulation()
                obj._deserialize(item)
                self._PsaRegulations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域整型ID，目前黑石可用地域包括：8-北京，4-上海，1-广州， 19-重庆
        :type RegionId: int
        """
        self._RegionId = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionInfoSet: 地域信息
        :type RegionInfoSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionInfoSet = None
        self._RequestId = None

    @property
    def RegionInfoSet(self):
        return self._RegionInfoSet

    @RegionInfoSet.setter
    def RegionInfoSet(self, RegionInfoSet):
        self._RegionInfoSet = RegionInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionInfoSet") is not None:
            self._RegionInfoSet = []
            for item in params.get("RegionInfoSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRepairTaskConstantRequest(AbstractModel):
    """DescribeRepairTaskConstant请求参数结构体

    """


class DescribeRepairTaskConstantResponse(AbstractModel):
    """DescribeRepairTaskConstant返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskTypeSet: 故障类型ID与对应中文名列表
        :type TaskTypeSet: list of TaskType
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskTypeSet = None
        self._RequestId = None

    @property
    def TaskTypeSet(self):
        return self._TaskTypeSet

    @TaskTypeSet.setter
    def TaskTypeSet(self, TaskTypeSet):
        self._TaskTypeSet = TaskTypeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskTypeSet") is not None:
            self._TaskTypeSet = []
            for item in params.get("TaskTypeSet"):
                obj = TaskType()
                obj._deserialize(item)
                self._TaskTypeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 开始位置
        :type Offset: int
        :param _Limit: 数据条数
        :type Limit: int
        :param _StartDate: 时间过滤下限
        :type StartDate: str
        :param _EndDate: 时间过滤上限
        :type EndDate: str
        :param _TaskStatus: 任务状态ID过滤
        :type TaskStatus: list of int non-negative
        :param _OrderField: 排序字段，目前支持：CreateTime，AuthTime，EndTime
        :type OrderField: str
        :param _Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        :param _TaskIds: 任务ID过滤
        :type TaskIds: list of str
        :param _InstanceIds: 实例ID过滤
        :type InstanceIds: list of str
        :param _Aliases: 实例别名过滤
        :type Aliases: list of str
        :param _TaskTypeIds: 故障类型ID过滤
        :type TaskTypeIds: list of int non-negative
        """
        self._Offset = None
        self._Limit = None
        self._StartDate = None
        self._EndDate = None
        self._TaskStatus = None
        self._OrderField = None
        self._Order = None
        self._TaskIds = None
        self._InstanceIds = None
        self._Aliases = None
        self._TaskTypeIds = None

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
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

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
    def TaskTypeIds(self):
        return self._TaskTypeIds

    @TaskTypeIds.setter
    def TaskTypeIds(self, TaskTypeIds):
        self._TaskTypeIds = TaskTypeIds


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._TaskStatus = params.get("TaskStatus")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._TaskIds = params.get("TaskIds")
        self._InstanceIds = params.get("InstanceIds")
        self._Aliases = params.get("Aliases")
        self._TaskTypeIds = params.get("TaskTypeIds")
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
        :param _TotalCount: 返回任务总数量
        :type TotalCount: int
        :param _TaskInfoSet: 任务信息列表
        :type TaskInfoSet: list of TaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInfoSet(self):
        return self._TaskInfoSet

    @TaskInfoSet.setter
    def TaskInfoSet(self, TaskInfoSet):
        self._TaskInfoSet = TaskInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskInfoSet") is not None:
            self._TaskInfoSet = []
            for item in params.get("TaskInfoSet"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._TaskInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskOperationLogRequest(AbstractModel):
    """DescribeTaskOperationLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 维修任务ID
        :type TaskId: str
        :param _OrderField: 排序字段，目前支持：OperationTime
        :type OrderField: str
        :param _Order: 排序方式 0:递增(默认) 1:递减
        :type Order: int
        """
        self._TaskId = None
        self._OrderField = None
        self._Order = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskOperationLogResponse(AbstractModel):
    """DescribeTaskOperationLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskOperationLogSet: 操作日志
        :type TaskOperationLogSet: list of TaskOperationLog
        :param _TotalCount: 日志条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskOperationLogSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TaskOperationLogSet(self):
        return self._TaskOperationLogSet

    @TaskOperationLogSet.setter
    def TaskOperationLogSet(self, TaskOperationLogSet):
        self._TaskOperationLogSet = TaskOperationLogSet

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
        if params.get("TaskOperationLogSet") is not None:
            self._TaskOperationLogSet = []
            for item in params.get("TaskOperationLogSet"):
                obj = TaskOperationLog()
                obj._deserialize(item)
                self._TaskOperationLogSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserCmdTaskInfoRequest(AbstractModel):
    """DescribeUserCmdTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量限制
        :type Limit: int
        :param _OrderField: 排序字段，支持： RunBeginTime,RunEndTime,Status
        :type OrderField: str
        :param _Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        :param _SearchKey: 关键字搜索，可搜索ID或别名，支持模糊搜索
        :type SearchKey: str
        """
        self._TaskId = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._SearchKey = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCmdTaskInfoResponse(AbstractModel):
    """DescribeUserCmdTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回数量
        :type TotalCount: int
        :param _UserCmdTaskInfoSet: 自定义脚本任务详细信息列表
        :type UserCmdTaskInfoSet: list of UserCmdTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserCmdTaskInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserCmdTaskInfoSet(self):
        return self._UserCmdTaskInfoSet

    @UserCmdTaskInfoSet.setter
    def UserCmdTaskInfoSet(self, UserCmdTaskInfoSet):
        self._UserCmdTaskInfoSet = UserCmdTaskInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UserCmdTaskInfoSet") is not None:
            self._UserCmdTaskInfoSet = []
            for item in params.get("UserCmdTaskInfoSet"):
                obj = UserCmdTaskInfo()
                obj._deserialize(item)
                self._UserCmdTaskInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserCmdTasksRequest(AbstractModel):
    """DescribeUserCmdTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量限制
        :type Limit: int
        :param _OrderField: 排序字段，支持： RunBeginTime,RunEndTime,InstanceCount,SuccessCount,FailureCount
        :type OrderField: str
        :param _Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        """
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCmdTasksResponse(AbstractModel):
    """DescribeUserCmdTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 脚本任务信息数量
        :type TotalCount: int
        :param _UserCmdTasks: 脚本任务信息列表
        :type UserCmdTasks: list of UserCmdTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserCmdTasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserCmdTasks(self):
        return self._UserCmdTasks

    @UserCmdTasks.setter
    def UserCmdTasks(self, UserCmdTasks):
        self._UserCmdTasks = UserCmdTasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UserCmdTasks") is not None:
            self._UserCmdTasks = []
            for item in params.get("UserCmdTasks"):
                obj = UserCmdTask()
                obj._deserialize(item)
                self._UserCmdTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserCmdsRequest(AbstractModel):
    """DescribeUserCmds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量限制
        :type Limit: int
        :param _OrderField: 排序字段，支持： OsType,CreateTime,ModifyTime
        :type OrderField: str
        :param _Order: 排序方式，取值: 1倒序，0顺序；默认倒序
        :type Order: int
        :param _SearchKey: 关键字搜索，可搜索ID或别名，支持模糊搜索
        :type SearchKey: str
        :param _CmdId: 查询的脚本ID
        :type CmdId: str
        """
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._SearchKey = None
        self._CmdId = None

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

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def CmdId(self):
        return self._CmdId

    @CmdId.setter
    def CmdId(self, CmdId):
        self._CmdId = CmdId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._SearchKey = params.get("SearchKey")
        self._CmdId = params.get("CmdId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCmdsResponse(AbstractModel):
    """DescribeUserCmds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回数量
        :type TotalCount: int
        :param _UserCmds: 脚本信息列表
        :type UserCmds: list of UserCmd
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UserCmds = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UserCmds(self):
        return self._UserCmds

    @UserCmds.setter
    def UserCmds(self, UserCmds):
        self._UserCmds = UserCmds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UserCmds") is not None:
            self._UserCmds = []
            for item in params.get("UserCmds"):
                obj = UserCmd()
                obj._deserialize(item)
                self._UserCmds.append(obj)
        self._RequestId = params.get("RequestId")


class DetachCamRoleRequest(AbstractModel):
    """DetachCamRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 服务器ID
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
        


class DetachCamRoleResponse(AbstractModel):
    """DetachCamRole返回参数结构体

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


class DeviceAlias(AbstractModel):
    """设备ID与别名

    """

    def __init__(self):
        r"""
        :param _InstanceId: 设备ID
        :type InstanceId: str
        :param _Alias: 设备别名
        :type Alias: str
        """
        self._InstanceId = None
        self._Alias = None

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceClass(AbstractModel):
    """物理机设备类型

    """

    def __init__(self):
        r"""
        :param _DeviceClassCode: 机型ID
        :type DeviceClassCode: str
        :param _CpuDescription: CPU描述
        :type CpuDescription: str
        :param _MemDescription: 内存描述
        :type MemDescription: str
        :param _DiskDescription: 硬盘描述
        :type DiskDescription: str
        :param _HaveRaidCard: 是否支持RAID. 0:不支持; 1:支持
        :type HaveRaidCard: int
        :param _NicDescription: 网卡描述
        :type NicDescription: str
        :param _GpuDescription: GPU描述
        :type GpuDescription: str
        :param _Discount: 单价折扣
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param _UnitPrice: 用户刊例价格
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: int
        :param _RealPrice: 实际价格
注意：此字段可能返回 null，表示取不到有效值。
        :type RealPrice: int
        :param _NormalPrice: 官网刊例价格
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalPrice: int
        :param _DeviceType: 设备使用场景类型
        :type DeviceType: str
        :param _Series: 机型系列
        :type Series: int
        :param _Cpu: cpu的核心数。仅是物理服务器未开启超线程的核心数， 超线程的核心数为Cpu*2
        :type Cpu: int
        :param _Mem: 内存容量。单位G
        :type Mem: int
        """
        self._DeviceClassCode = None
        self._CpuDescription = None
        self._MemDescription = None
        self._DiskDescription = None
        self._HaveRaidCard = None
        self._NicDescription = None
        self._GpuDescription = None
        self._Discount = None
        self._UnitPrice = None
        self._RealPrice = None
        self._NormalPrice = None
        self._DeviceType = None
        self._Series = None
        self._Cpu = None
        self._Mem = None

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

    @property
    def CpuDescription(self):
        return self._CpuDescription

    @CpuDescription.setter
    def CpuDescription(self, CpuDescription):
        self._CpuDescription = CpuDescription

    @property
    def MemDescription(self):
        return self._MemDescription

    @MemDescription.setter
    def MemDescription(self, MemDescription):
        self._MemDescription = MemDescription

    @property
    def DiskDescription(self):
        return self._DiskDescription

    @DiskDescription.setter
    def DiskDescription(self, DiskDescription):
        self._DiskDescription = DiskDescription

    @property
    def HaveRaidCard(self):
        return self._HaveRaidCard

    @HaveRaidCard.setter
    def HaveRaidCard(self, HaveRaidCard):
        self._HaveRaidCard = HaveRaidCard

    @property
    def NicDescription(self):
        return self._NicDescription

    @NicDescription.setter
    def NicDescription(self, NicDescription):
        self._NicDescription = NicDescription

    @property
    def GpuDescription(self):
        return self._GpuDescription

    @GpuDescription.setter
    def GpuDescription(self, GpuDescription):
        self._GpuDescription = GpuDescription

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def RealPrice(self):
        return self._RealPrice

    @RealPrice.setter
    def RealPrice(self, RealPrice):
        self._RealPrice = RealPrice

    @property
    def NormalPrice(self):
        return self._NormalPrice

    @NormalPrice.setter
    def NormalPrice(self, NormalPrice):
        self._NormalPrice = NormalPrice

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Series(self):
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem


    def _deserialize(self, params):
        self._DeviceClassCode = params.get("DeviceClassCode")
        self._CpuDescription = params.get("CpuDescription")
        self._MemDescription = params.get("MemDescription")
        self._DiskDescription = params.get("DiskDescription")
        self._HaveRaidCard = params.get("HaveRaidCard")
        self._NicDescription = params.get("NicDescription")
        self._GpuDescription = params.get("GpuDescription")
        self._Discount = params.get("Discount")
        self._UnitPrice = params.get("UnitPrice")
        self._RealPrice = params.get("RealPrice")
        self._NormalPrice = params.get("NormalPrice")
        self._DeviceType = params.get("DeviceType")
        self._Series = params.get("Series")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceClassPartitionInfo(AbstractModel):
    """RAID和设备分区结构

    """

    def __init__(self):
        r"""
        :param _RaidId: RAID类型ID
        :type RaidId: int
        :param _Raid: RAID名称
        :type Raid: str
        :param _RaidDisplay: RAID名称（前台展示用）
        :type RaidDisplay: str
        :param _SystemDiskSize: 系统盘总大小（单位GiB）
        :type SystemDiskSize: int
        :param _SysRootSpace: 系统盘/分区默认大小（单位GiB）
        :type SysRootSpace: int
        :param _SysSwaporuefiSpace: 系统盘swap分区默认大小（单位GiB）
        :type SysSwaporuefiSpace: int
        :param _SysUsrlocalSpace: 系统盘/usr/local分区默认大小（单位GiB）
        :type SysUsrlocalSpace: int
        :param _SysDataSpace: 系统盘/data分区默认大小（单位GiB）
        :type SysDataSpace: int
        :param _SysIsUefiType: 设备是否是uefi启动方式。0:legacy启动; 1:uefi启动
        :type SysIsUefiType: int
        :param _DataDiskSize: 数据盘总大小
        :type DataDiskSize: int
        :param _DeviceDiskSizeInfoSet: 硬盘列表
        :type DeviceDiskSizeInfoSet: list of DeviceDiskSizeInfo
        """
        self._RaidId = None
        self._Raid = None
        self._RaidDisplay = None
        self._SystemDiskSize = None
        self._SysRootSpace = None
        self._SysSwaporuefiSpace = None
        self._SysUsrlocalSpace = None
        self._SysDataSpace = None
        self._SysIsUefiType = None
        self._DataDiskSize = None
        self._DeviceDiskSizeInfoSet = None

    @property
    def RaidId(self):
        return self._RaidId

    @RaidId.setter
    def RaidId(self, RaidId):
        self._RaidId = RaidId

    @property
    def Raid(self):
        return self._Raid

    @Raid.setter
    def Raid(self, Raid):
        self._Raid = Raid

    @property
    def RaidDisplay(self):
        return self._RaidDisplay

    @RaidDisplay.setter
    def RaidDisplay(self, RaidDisplay):
        self._RaidDisplay = RaidDisplay

    @property
    def SystemDiskSize(self):
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def SysRootSpace(self):
        return self._SysRootSpace

    @SysRootSpace.setter
    def SysRootSpace(self, SysRootSpace):
        self._SysRootSpace = SysRootSpace

    @property
    def SysSwaporuefiSpace(self):
        return self._SysSwaporuefiSpace

    @SysSwaporuefiSpace.setter
    def SysSwaporuefiSpace(self, SysSwaporuefiSpace):
        self._SysSwaporuefiSpace = SysSwaporuefiSpace

    @property
    def SysUsrlocalSpace(self):
        return self._SysUsrlocalSpace

    @SysUsrlocalSpace.setter
    def SysUsrlocalSpace(self, SysUsrlocalSpace):
        self._SysUsrlocalSpace = SysUsrlocalSpace

    @property
    def SysDataSpace(self):
        return self._SysDataSpace

    @SysDataSpace.setter
    def SysDataSpace(self, SysDataSpace):
        self._SysDataSpace = SysDataSpace

    @property
    def SysIsUefiType(self):
        return self._SysIsUefiType

    @SysIsUefiType.setter
    def SysIsUefiType(self, SysIsUefiType):
        self._SysIsUefiType = SysIsUefiType

    @property
    def DataDiskSize(self):
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def DeviceDiskSizeInfoSet(self):
        return self._DeviceDiskSizeInfoSet

    @DeviceDiskSizeInfoSet.setter
    def DeviceDiskSizeInfoSet(self, DeviceDiskSizeInfoSet):
        self._DeviceDiskSizeInfoSet = DeviceDiskSizeInfoSet


    def _deserialize(self, params):
        self._RaidId = params.get("RaidId")
        self._Raid = params.get("Raid")
        self._RaidDisplay = params.get("RaidDisplay")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._SysRootSpace = params.get("SysRootSpace")
        self._SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self._SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self._SysDataSpace = params.get("SysDataSpace")
        self._SysIsUefiType = params.get("SysIsUefiType")
        self._DataDiskSize = params.get("DataDiskSize")
        if params.get("DeviceDiskSizeInfoSet") is not None:
            self._DeviceDiskSizeInfoSet = []
            for item in params.get("DeviceDiskSizeInfoSet"):
                obj = DeviceDiskSizeInfo()
                obj._deserialize(item)
                self._DeviceDiskSizeInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDiskSizeInfo(AbstractModel):
    """硬盘大小的描述

    """

    def __init__(self):
        r"""
        :param _DiskName: 硬盘名称
        :type DiskName: str
        :param _DiskSize: 硬盘大小（单位GiB）
        :type DiskSize: int
        """
        self._DiskName = None
        self._DiskSize = None

    @property
    def DiskName(self):
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskName = params.get("DiskName")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceHardwareInfo(AbstractModel):
    """设备硬件配置信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 设备实例 ID
        :type InstanceId: str
        :param _IsElastic: 是否自定义机型
        :type IsElastic: int
        :param _CpmPayMode: 机型计费模式，1 为预付费，2 为后付费
        :type CpmPayMode: int
        :param _CpuId: 自定义机型，CPU 型号 ID（非自定义机型返回0）
        :type CpuId: int
        :param _Mem: 自定义机型，内存大小, 单位 GB（非自定义机型返回0）
        :type Mem: int
        :param _ContainRaidCard: 是否有 RAID 卡，0：没有 RAID 卡； 1：有 RAID 卡
        :type ContainRaidCard: int
        :param _SystemDiskTypeId: 自定义机型系统盘类型ID（若没有则返回0）
        :type SystemDiskTypeId: int
        :param _SystemDiskCount: 自定义机型系统盘数量（若没有则返回0）
        :type SystemDiskCount: int
        :param _DataDiskTypeId: 自定义机型数据盘类型 ID（若没有则返回0）
        :type DataDiskTypeId: int
        :param _DataDiskCount: 自定义机型数据盘数量（若没有则返回0）
        :type DataDiskCount: int
        :param _CpuDescription: CPU 型号描述
        :type CpuDescription: str
        :param _MemDescription: 内存描述
        :type MemDescription: str
        :param _DiskDescription: 磁盘描述
        :type DiskDescription: str
        :param _NicDescription: 网卡描述
        :type NicDescription: str
        :param _RaidDescription: 是否支持 RAID 的描述
        :type RaidDescription: str
        :param _Cpu: cpu的核心数。仅是物理服务器未开启超线程的核心数， 超线程的核心数为Cpu*2
        :type Cpu: int
        :param _DeviceClassCode: 机型外部代号
        :type DeviceClassCode: str
        """
        self._InstanceId = None
        self._IsElastic = None
        self._CpmPayMode = None
        self._CpuId = None
        self._Mem = None
        self._ContainRaidCard = None
        self._SystemDiskTypeId = None
        self._SystemDiskCount = None
        self._DataDiskTypeId = None
        self._DataDiskCount = None
        self._CpuDescription = None
        self._MemDescription = None
        self._DiskDescription = None
        self._NicDescription = None
        self._RaidDescription = None
        self._Cpu = None
        self._DeviceClassCode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IsElastic(self):
        return self._IsElastic

    @IsElastic.setter
    def IsElastic(self, IsElastic):
        self._IsElastic = IsElastic

    @property
    def CpmPayMode(self):
        return self._CpmPayMode

    @CpmPayMode.setter
    def CpmPayMode(self, CpmPayMode):
        self._CpmPayMode = CpmPayMode

    @property
    def CpuId(self):
        return self._CpuId

    @CpuId.setter
    def CpuId(self, CpuId):
        self._CpuId = CpuId

    @property
    def Mem(self):
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def ContainRaidCard(self):
        return self._ContainRaidCard

    @ContainRaidCard.setter
    def ContainRaidCard(self, ContainRaidCard):
        self._ContainRaidCard = ContainRaidCard

    @property
    def SystemDiskTypeId(self):
        return self._SystemDiskTypeId

    @SystemDiskTypeId.setter
    def SystemDiskTypeId(self, SystemDiskTypeId):
        self._SystemDiskTypeId = SystemDiskTypeId

    @property
    def SystemDiskCount(self):
        return self._SystemDiskCount

    @SystemDiskCount.setter
    def SystemDiskCount(self, SystemDiskCount):
        self._SystemDiskCount = SystemDiskCount

    @property
    def DataDiskTypeId(self):
        return self._DataDiskTypeId

    @DataDiskTypeId.setter
    def DataDiskTypeId(self, DataDiskTypeId):
        self._DataDiskTypeId = DataDiskTypeId

    @property
    def DataDiskCount(self):
        return self._DataDiskCount

    @DataDiskCount.setter
    def DataDiskCount(self, DataDiskCount):
        self._DataDiskCount = DataDiskCount

    @property
    def CpuDescription(self):
        return self._CpuDescription

    @CpuDescription.setter
    def CpuDescription(self, CpuDescription):
        self._CpuDescription = CpuDescription

    @property
    def MemDescription(self):
        return self._MemDescription

    @MemDescription.setter
    def MemDescription(self, MemDescription):
        self._MemDescription = MemDescription

    @property
    def DiskDescription(self):
        return self._DiskDescription

    @DiskDescription.setter
    def DiskDescription(self, DiskDescription):
        self._DiskDescription = DiskDescription

    @property
    def NicDescription(self):
        return self._NicDescription

    @NicDescription.setter
    def NicDescription(self, NicDescription):
        self._NicDescription = NicDescription

    @property
    def RaidDescription(self):
        return self._RaidDescription

    @RaidDescription.setter
    def RaidDescription(self, RaidDescription):
        self._RaidDescription = RaidDescription

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IsElastic = params.get("IsElastic")
        self._CpmPayMode = params.get("CpmPayMode")
        self._CpuId = params.get("CpuId")
        self._Mem = params.get("Mem")
        self._ContainRaidCard = params.get("ContainRaidCard")
        self._SystemDiskTypeId = params.get("SystemDiskTypeId")
        self._SystemDiskCount = params.get("SystemDiskCount")
        self._DataDiskTypeId = params.get("DataDiskTypeId")
        self._DataDiskCount = params.get("DataDiskCount")
        self._CpuDescription = params.get("CpuDescription")
        self._MemDescription = params.get("MemDescription")
        self._DiskDescription = params.get("DiskDescription")
        self._NicDescription = params.get("NicDescription")
        self._RaidDescription = params.get("RaidDescription")
        self._Cpu = params.get("Cpu")
        self._DeviceClassCode = params.get("DeviceClassCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """物理机信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 设备唯一ID
        :type InstanceId: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _DeviceStatus: 设备状态ID，取值：<li>1：申领设备中</li><li>2：初始化中</li><li>4：运营中</li><li>7：隔离中</li><li>8：已隔离</li><li>10：解隔离中</li><li>16：故障中</li>
        :type DeviceStatus: int
        :param _OperateStatus: 设备操作状态ID，取值：
<li>1：运行中</li><li>2：正在关机</li><li>3：已关机</li><li>5：正在开机</li><li>7：重启中</li><li>9：重装中</li><li>12：绑定EIP</li><li>13：解绑EIP</li><li>14：绑定LB</li><li>15：解绑LB</li><li>19：更换IP中</li><li>20：制作镜像中</li><li>21：制作镜像失败</li><li>23：故障待重装</li><li>24：无备件待退回</li>
        :type OperateStatus: int
        :param _OsTypeId: 操作系统ID，参考接口[查询操作系统信息(DescribeOsInfo)](https://cloud.tencent.com/document/product/386/32902)
        :type OsTypeId: int
        :param _RaidId: RAID类型ID，参考接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/product/386/32910)
        :type RaidId: int
        :param _Alias: 设备别名
        :type Alias: str
        :param _AppId: 用户AppId
        :type AppId: int
        :param _Zone: 可用区
        :type Zone: str
        :param _WanIp: 外网IP
        :type WanIp: str
        :param _LanIp: 内网IP
        :type LanIp: str
        :param _DeliverTime: 设备交付时间
        :type DeliverTime: str
        :param _Deadline: 设备到期时间
        :type Deadline: str
        :param _AutoRenewFlag: 自动续费标识。0: 不自动续费; 1:自动续费
        :type AutoRenewFlag: int
        :param _DeviceClassCode: 设备类型
        :type DeviceClassCode: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _CpmPayMode: 计费模式。1: 预付费; 2: 后付费; 3:预付费转后付费中
        :type CpmPayMode: int
        :param _DhcpIp: 带外IP
        :type DhcpIp: str
        :param _VpcName: 所在私有网络别名
        :type VpcName: str
        :param _SubnetName: 所在子网别名
        :type SubnetName: str
        :param _VpcCidrBlock: 所在私有网络CIDR
        :type VpcCidrBlock: str
        :param _SubnetCidrBlock: 所在子网CIDR
        :type SubnetCidrBlock: str
        :param _IsLuckyDevice: 标识是否是竞价实例。0: 普通设备; 1: 竞价实例设备
        :type IsLuckyDevice: int
        :param _MaintainStatus: 标识机器维保状态。Maintain: 在保;  WillExpire: 即将过保; Expire: 已过保
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainStatus: str
        :param _MaintainMessage: 维保信息描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainMessage: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._DeviceStatus = None
        self._OperateStatus = None
        self._OsTypeId = None
        self._RaidId = None
        self._Alias = None
        self._AppId = None
        self._Zone = None
        self._WanIp = None
        self._LanIp = None
        self._DeliverTime = None
        self._Deadline = None
        self._AutoRenewFlag = None
        self._DeviceClassCode = None
        self._Tags = None
        self._CpmPayMode = None
        self._DhcpIp = None
        self._VpcName = None
        self._SubnetName = None
        self._VpcCidrBlock = None
        self._SubnetCidrBlock = None
        self._IsLuckyDevice = None
        self._MaintainStatus = None
        self._MaintainMessage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId

    @property
    def RaidId(self):
        return self._RaidId

    @RaidId.setter
    def RaidId(self, RaidId):
        self._RaidId = RaidId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def DeliverTime(self):
        return self._DeliverTime

    @DeliverTime.setter
    def DeliverTime(self, DeliverTime):
        self._DeliverTime = DeliverTime

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CpmPayMode(self):
        return self._CpmPayMode

    @CpmPayMode.setter
    def CpmPayMode(self, CpmPayMode):
        self._CpmPayMode = CpmPayMode

    @property
    def DhcpIp(self):
        return self._DhcpIp

    @DhcpIp.setter
    def DhcpIp(self, DhcpIp):
        self._DhcpIp = DhcpIp

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetCidrBlock(self):
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock

    @property
    def IsLuckyDevice(self):
        return self._IsLuckyDevice

    @IsLuckyDevice.setter
    def IsLuckyDevice(self, IsLuckyDevice):
        self._IsLuckyDevice = IsLuckyDevice

    @property
    def MaintainStatus(self):
        return self._MaintainStatus

    @MaintainStatus.setter
    def MaintainStatus(self, MaintainStatus):
        self._MaintainStatus = MaintainStatus

    @property
    def MaintainMessage(self):
        return self._MaintainMessage

    @MaintainMessage.setter
    def MaintainMessage(self, MaintainMessage):
        self._MaintainMessage = MaintainMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._DeviceStatus = params.get("DeviceStatus")
        self._OperateStatus = params.get("OperateStatus")
        self._OsTypeId = params.get("OsTypeId")
        self._RaidId = params.get("RaidId")
        self._Alias = params.get("Alias")
        self._AppId = params.get("AppId")
        self._Zone = params.get("Zone")
        self._WanIp = params.get("WanIp")
        self._LanIp = params.get("LanIp")
        self._DeliverTime = params.get("DeliverTime")
        self._Deadline = params.get("Deadline")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DeviceClassCode = params.get("DeviceClassCode")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CpmPayMode = params.get("CpmPayMode")
        self._DhcpIp = params.get("DhcpIp")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        self._IsLuckyDevice = params.get("IsLuckyDevice")
        self._MaintainStatus = params.get("MaintainStatus")
        self._MaintainMessage = params.get("MaintainMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceOperationLog(AbstractModel):
    """设备操作日志

    """

    def __init__(self):
        r"""
        :param _Id: 日志的ID
        :type Id: int
        :param _InstanceId: 设备ID
        :type InstanceId: str
        :param _TaskId: 日志对应的操作任务ID
        :type TaskId: int
        :param _TaskName: 操作任务名称
        :type TaskName: str
        :param _TaskDescription: 操作任务中文名称
        :type TaskDescription: str
        :param _StartTime: 操作开始时间
        :type StartTime: str
        :param _EndTime: 操作结束时间
        :type EndTime: str
        :param _Status: 操作状态，0: 正在执行中；1：任务成功； 2: 任务失败。
        :type Status: int
        :param _OpUin: 操作者
        :type OpUin: str
        :param _LogDescription: 操作描述
        :type LogDescription: str
        """
        self._Id = None
        self._InstanceId = None
        self._TaskId = None
        self._TaskName = None
        self._TaskDescription = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._OpUin = None
        self._LogDescription = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskDescription(self):
        return self._TaskDescription

    @TaskDescription.setter
    def TaskDescription(self, TaskDescription):
        self._TaskDescription = TaskDescription

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OpUin(self):
        return self._OpUin

    @OpUin.setter
    def OpUin(self, OpUin):
        self._OpUin = OpUin

    @property
    def LogDescription(self):
        return self._LogDescription

    @LogDescription.setter
    def LogDescription(self, LogDescription):
        self._LogDescription = LogDescription


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._TaskDescription = params.get("TaskDescription")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._OpUin = params.get("OpUin")
        self._LogDescription = params.get("LogDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePartition(AbstractModel):
    """物理机分区格式

    """

    def __init__(self):
        r"""
        :param _SystemDiskSize: 系统盘大小
        :type SystemDiskSize: int
        :param _DataDiskSize: 数据盘大小
        :type DataDiskSize: int
        :param _SysIsUefiType: 是否兼容Uefi
        :type SysIsUefiType: bool
        :param _SysRootSpace: root分区大小
        :type SysRootSpace: int
        :param _SysSwaporuefiSpace: Swaporuefi分区大小
        :type SysSwaporuefiSpace: int
        :param _SysUsrlocalSpace: Usrlocal分区大小
        :type SysUsrlocalSpace: int
        :param _SysDataSpace: data分区大小
        :type SysDataSpace: int
        :param _DeviceDiskSizeInfoSet: 硬盘大小详情
        :type DeviceDiskSizeInfoSet: list of DeviceDiskSizeInfo
        """
        self._SystemDiskSize = None
        self._DataDiskSize = None
        self._SysIsUefiType = None
        self._SysRootSpace = None
        self._SysSwaporuefiSpace = None
        self._SysUsrlocalSpace = None
        self._SysDataSpace = None
        self._DeviceDiskSizeInfoSet = None

    @property
    def SystemDiskSize(self):
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def DataDiskSize(self):
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def SysIsUefiType(self):
        return self._SysIsUefiType

    @SysIsUefiType.setter
    def SysIsUefiType(self, SysIsUefiType):
        self._SysIsUefiType = SysIsUefiType

    @property
    def SysRootSpace(self):
        return self._SysRootSpace

    @SysRootSpace.setter
    def SysRootSpace(self, SysRootSpace):
        self._SysRootSpace = SysRootSpace

    @property
    def SysSwaporuefiSpace(self):
        return self._SysSwaporuefiSpace

    @SysSwaporuefiSpace.setter
    def SysSwaporuefiSpace(self, SysSwaporuefiSpace):
        self._SysSwaporuefiSpace = SysSwaporuefiSpace

    @property
    def SysUsrlocalSpace(self):
        return self._SysUsrlocalSpace

    @SysUsrlocalSpace.setter
    def SysUsrlocalSpace(self, SysUsrlocalSpace):
        self._SysUsrlocalSpace = SysUsrlocalSpace

    @property
    def SysDataSpace(self):
        return self._SysDataSpace

    @SysDataSpace.setter
    def SysDataSpace(self, SysDataSpace):
        self._SysDataSpace = SysDataSpace

    @property
    def DeviceDiskSizeInfoSet(self):
        return self._DeviceDiskSizeInfoSet

    @DeviceDiskSizeInfoSet.setter
    def DeviceDiskSizeInfoSet(self, DeviceDiskSizeInfoSet):
        self._DeviceDiskSizeInfoSet = DeviceDiskSizeInfoSet


    def _deserialize(self, params):
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._DataDiskSize = params.get("DataDiskSize")
        self._SysIsUefiType = params.get("SysIsUefiType")
        self._SysRootSpace = params.get("SysRootSpace")
        self._SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self._SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self._SysDataSpace = params.get("SysDataSpace")
        if params.get("DeviceDiskSizeInfoSet") is not None:
            self._DeviceDiskSizeInfoSet = []
            for item in params.get("DeviceDiskSizeInfoSet"):
                obj = DeviceDiskSizeInfo()
                obj._deserialize(item)
                self._DeviceDiskSizeInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePositionInfo(AbstractModel):
    """物理机机架信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 设备ID
        :type InstanceId: str
        :param _Zone: 所在可用区
        :type Zone: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _LanIp: 业务IP
        :type LanIp: str
        :param _Alias: 实例别名
        :type Alias: str
        :param _RckName: 机架名称
        :type RckName: str
        :param _PosCode: 机位
        :type PosCode: int
        :param _SwitchName: 交换机名称
        :type SwitchName: str
        :param _DeliverTime: 设备交付时间
        :type DeliverTime: str
        :param _Deadline: 过期时间
        :type Deadline: str
        """
        self._InstanceId = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._LanIp = None
        self._Alias = None
        self._RckName = None
        self._PosCode = None
        self._SwitchName = None
        self._DeliverTime = None
        self._Deadline = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def RckName(self):
        return self._RckName

    @RckName.setter
    def RckName(self, RckName):
        self._RckName = RckName

    @property
    def PosCode(self):
        return self._PosCode

    @PosCode.setter
    def PosCode(self, PosCode):
        self._PosCode = PosCode

    @property
    def SwitchName(self):
        return self._SwitchName

    @SwitchName.setter
    def SwitchName(self, SwitchName):
        self._SwitchName = SwitchName

    @property
    def DeliverTime(self):
        return self._DeliverTime

    @DeliverTime.setter
    def DeliverTime(self, DeliverTime):
        self._DeliverTime = DeliverTime

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._LanIp = params.get("LanIp")
        self._Alias = params.get("Alias")
        self._RckName = params.get("RckName")
        self._PosCode = params.get("PosCode")
        self._SwitchName = params.get("SwitchName")
        self._DeliverTime = params.get("DeliverTime")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePriceInfo(AbstractModel):
    """服务器价格信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机ID
        :type InstanceId: str
        :param _DeviceClassCode: 设备型号
        :type DeviceClassCode: str
        :param _IsElastic: 是否是弹性机型，1：是，0：否
        :type IsElastic: int
        :param _CpmPayMode: 付费模式ID, 1:预付费; 2:后付费; 3:预付费转后付费中
        :type CpmPayMode: int
        :param _CpuDescription: Cpu信息描述
        :type CpuDescription: str
        :param _MemDescription: 内存信息描述
        :type MemDescription: str
        :param _DiskDescription: 硬盘信息描述
        :type DiskDescription: str
        :param _NicDescription: 网卡信息描述
        :type NicDescription: str
        :param _GpuDescription: Gpu信息描述
        :type GpuDescription: str
        :param _RaidDescription: Raid信息描述
        :type RaidDescription: str
        :param _Price: 客户的单价
        :type Price: int
        :param _NormalPrice: 刊例单价
        :type NormalPrice: int
        :param _TotalCost: 原价
        :type TotalCost: int
        :param _RealTotalCost: 折扣价
        :type RealTotalCost: int
        :param _TimeSpan: 计费时长
        :type TimeSpan: int
        :param _TimeUnit: 计费时长单位, M:按月计费; D:按天计费
        :type TimeUnit: str
        :param _GoodsCount: 商品数量
        :type GoodsCount: int
        """
        self._InstanceId = None
        self._DeviceClassCode = None
        self._IsElastic = None
        self._CpmPayMode = None
        self._CpuDescription = None
        self._MemDescription = None
        self._DiskDescription = None
        self._NicDescription = None
        self._GpuDescription = None
        self._RaidDescription = None
        self._Price = None
        self._NormalPrice = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._GoodsCount = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceClassCode(self):
        return self._DeviceClassCode

    @DeviceClassCode.setter
    def DeviceClassCode(self, DeviceClassCode):
        self._DeviceClassCode = DeviceClassCode

    @property
    def IsElastic(self):
        return self._IsElastic

    @IsElastic.setter
    def IsElastic(self, IsElastic):
        self._IsElastic = IsElastic

    @property
    def CpmPayMode(self):
        return self._CpmPayMode

    @CpmPayMode.setter
    def CpmPayMode(self, CpmPayMode):
        self._CpmPayMode = CpmPayMode

    @property
    def CpuDescription(self):
        return self._CpuDescription

    @CpuDescription.setter
    def CpuDescription(self, CpuDescription):
        self._CpuDescription = CpuDescription

    @property
    def MemDescription(self):
        return self._MemDescription

    @MemDescription.setter
    def MemDescription(self, MemDescription):
        self._MemDescription = MemDescription

    @property
    def DiskDescription(self):
        return self._DiskDescription

    @DiskDescription.setter
    def DiskDescription(self, DiskDescription):
        self._DiskDescription = DiskDescription

    @property
    def NicDescription(self):
        return self._NicDescription

    @NicDescription.setter
    def NicDescription(self, NicDescription):
        self._NicDescription = NicDescription

    @property
    def GpuDescription(self):
        return self._GpuDescription

    @GpuDescription.setter
    def GpuDescription(self, GpuDescription):
        self._GpuDescription = GpuDescription

    @property
    def RaidDescription(self):
        return self._RaidDescription

    @RaidDescription.setter
    def RaidDescription(self, RaidDescription):
        self._RaidDescription = RaidDescription

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def NormalPrice(self):
        return self._NormalPrice

    @NormalPrice.setter
    def NormalPrice(self, NormalPrice):
        self._NormalPrice = NormalPrice

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def GoodsCount(self):
        return self._GoodsCount

    @GoodsCount.setter
    def GoodsCount(self, GoodsCount):
        self._GoodsCount = GoodsCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceClassCode = params.get("DeviceClassCode")
        self._IsElastic = params.get("IsElastic")
        self._CpmPayMode = params.get("CpmPayMode")
        self._CpuDescription = params.get("CpuDescription")
        self._MemDescription = params.get("MemDescription")
        self._DiskDescription = params.get("DiskDescription")
        self._NicDescription = params.get("NicDescription")
        self._GpuDescription = params.get("GpuDescription")
        self._RaidDescription = params.get("RaidDescription")
        self._Price = params.get("Price")
        self._NormalPrice = params.get("NormalPrice")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._GoodsCount = params.get("GoodsCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskInfo(AbstractModel):
    """自定义机型磁盘的描述

    """

    def __init__(self):
        r"""
        :param _DiskTypeId: 磁盘ID
        :type DiskTypeId: int
        :param _Size: 磁盘的容量，单位为G
        :type Size: int
        :param _DiskDescription: 磁盘信息描述
        :type DiskDescription: str
        """
        self._DiskTypeId = None
        self._Size = None
        self._DiskDescription = None

    @property
    def DiskTypeId(self):
        return self._DiskTypeId

    @DiskTypeId.setter
    def DiskTypeId(self, DiskTypeId):
        self._DiskTypeId = DiskTypeId

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def DiskDescription(self):
        return self._DiskDescription

    @DiskDescription.setter
    def DiskDescription(self, DiskDescription):
        self._DiskDescription = DiskDescription


    def _deserialize(self, params):
        self._DiskTypeId = params.get("DiskTypeId")
        self._Size = params.get("Size")
        self._DiskDescription = params.get("DiskDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedTaskInfo(AbstractModel):
    """运行失败的自定义脚本信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 运行脚本的设备ID
        :type InstanceId: str
        :param _ErrorMsg: 失败原因
        :type ErrorMsg: str
        """
        self._InstanceId = None
        self._ErrorMsg = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostedDeviceOutBandInfo(AbstractModel):
    """托管设备带外信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机ID
        :type InstanceId: str
        :param _OutBandIp: 带外IP
        :type OutBandIp: str
        :param _VpnIp: VPN的IP
        :type VpnIp: str
        :param _VpnPort: VPN的端口
        :type VpnPort: int
        """
        self._InstanceId = None
        self._OutBandIp = None
        self._VpnIp = None
        self._VpnPort = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OutBandIp(self):
        return self._OutBandIp

    @OutBandIp.setter
    def OutBandIp(self, OutBandIp):
        self._OutBandIp = OutBandIp

    @property
    def VpnIp(self):
        return self._VpnIp

    @VpnIp.setter
    def VpnIp(self, VpnIp):
        self._VpnIp = VpnIp

    @property
    def VpnPort(self):
        return self._VpnPort

    @VpnPort.setter
    def VpnPort(self, VpnPort):
        self._VpnPort = VpnPort


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OutBandIp = params.get("OutBandIp")
        self._VpnIp = params.get("VpnIp")
        self._VpnPort = params.get("VpnPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomImageAttributeRequest(AbstractModel):
    """ModifyCustomImageAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _ImageName: 设置新的镜像名
        :type ImageName: str
        :param _ImageDescription: 设置新的镜像描述
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
        


class ModifyCustomImageAttributeResponse(AbstractModel):
    """ModifyCustomImageAttribute返回参数结构体

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


class ModifyDeviceAliasesRequest(AbstractModel):
    """ModifyDeviceAliases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceAliases: 需要改名的设备与别名列表
        :type DeviceAliases: list of DeviceAlias
        """
        self._DeviceAliases = None

    @property
    def DeviceAliases(self):
        return self._DeviceAliases

    @DeviceAliases.setter
    def DeviceAliases(self, DeviceAliases):
        self._DeviceAliases = DeviceAliases


    def _deserialize(self, params):
        if params.get("DeviceAliases") is not None:
            self._DeviceAliases = []
            for item in params.get("DeviceAliases"):
                obj = DeviceAlias()
                obj._deserialize(item)
                self._DeviceAliases.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceAliasesResponse(AbstractModel):
    """ModifyDeviceAliases返回参数结构体

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


class ModifyDeviceAutoRenewFlagRequest(AbstractModel):
    """ModifyDeviceAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoRenewFlag: 自动续费标志位。0: 不自动续费; 1: 自动续费
        :type AutoRenewFlag: int
        :param _InstanceIds: 需要修改的设备ID列表
        :type InstanceIds: list of str
        """
        self._AutoRenewFlag = None
        self._InstanceIds = None

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceAutoRenewFlagResponse(AbstractModel):
    """ModifyDeviceAutoRenewFlag返回参数结构体

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


class ModifyLanIpRequest(AbstractModel):
    """ModifyLanIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机ID
        :type InstanceId: str
        :param _VpcId: 指定新VPC
        :type VpcId: str
        :param _SubnetId: 指定新子网
        :type SubnetId: str
        :param _LanIp: 指定新内网IP
        :type LanIp: str
        :param _RebootDevice: 是否需要重启机器，取值 1(需要) 0(不需要)，默认取值0
        :type RebootDevice: int
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._LanIp = None
        self._RebootDevice = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def RebootDevice(self):
        return self._RebootDevice

    @RebootDevice.setter
    def RebootDevice(self, RebootDevice):
        self._RebootDevice = RebootDevice


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._LanIp = params.get("LanIp")
        self._RebootDevice = params.get("RebootDevice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLanIpResponse(AbstractModel):
    """ModifyLanIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
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


class ModifyPayModePre2PostRequest(AbstractModel):
    """ModifyPayModePre2Post请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要修改的设备ID列表
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
        


class ModifyPayModePre2PostResponse(AbstractModel):
    """ModifyPayModePre2Post返回参数结构体

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


class ModifyPsaRegulationRequest(AbstractModel):
    """ModifyPsaRegulation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PsaId: 预授权规则ID
        :type PsaId: str
        :param _PsaName: 预授权规则别名
        :type PsaName: str
        :param _RepairLimit: 维修中的实例上限
        :type RepairLimit: int
        :param _PsaDescription: 预授权规则备注
        :type PsaDescription: str
        :param _TaskTypeIds: 预授权规则关联故障类型ID列表
        :type TaskTypeIds: list of int non-negative
        """
        self._PsaId = None
        self._PsaName = None
        self._RepairLimit = None
        self._PsaDescription = None
        self._TaskTypeIds = None

    @property
    def PsaId(self):
        return self._PsaId

    @PsaId.setter
    def PsaId(self, PsaId):
        self._PsaId = PsaId

    @property
    def PsaName(self):
        return self._PsaName

    @PsaName.setter
    def PsaName(self, PsaName):
        self._PsaName = PsaName

    @property
    def RepairLimit(self):
        return self._RepairLimit

    @RepairLimit.setter
    def RepairLimit(self, RepairLimit):
        self._RepairLimit = RepairLimit

    @property
    def PsaDescription(self):
        return self._PsaDescription

    @PsaDescription.setter
    def PsaDescription(self, PsaDescription):
        self._PsaDescription = PsaDescription

    @property
    def TaskTypeIds(self):
        return self._TaskTypeIds

    @TaskTypeIds.setter
    def TaskTypeIds(self, TaskTypeIds):
        self._TaskTypeIds = TaskTypeIds


    def _deserialize(self, params):
        self._PsaId = params.get("PsaId")
        self._PsaName = params.get("PsaName")
        self._RepairLimit = params.get("RepairLimit")
        self._PsaDescription = params.get("PsaDescription")
        self._TaskTypeIds = params.get("TaskTypeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPsaRegulationResponse(AbstractModel):
    """ModifyPsaRegulation返回参数结构体

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


class ModifyUserCmdRequest(AbstractModel):
    """ModifyUserCmd请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdId: 待修改的脚本ID
        :type CmdId: str
        :param _Alias: 待修改的脚本名称
        :type Alias: str
        :param _OsType: 脚本适用的操作系统类型
        :type OsType: str
        :param _Content: 待修改的脚本内容，必须经过base64编码
        :type Content: str
        """
        self._CmdId = None
        self._Alias = None
        self._OsType = None
        self._Content = None

    @property
    def CmdId(self):
        return self._CmdId

    @CmdId.setter
    def CmdId(self, CmdId):
        self._CmdId = CmdId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._CmdId = params.get("CmdId")
        self._Alias = params.get("Alias")
        self._OsType = params.get("OsType")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserCmdResponse(AbstractModel):
    """ModifyUserCmd返回参数结构体

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


class OfflineDevicesRequest(AbstractModel):
    """OfflineDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要退还的物理机ID列表
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
        


class OfflineDevicesResponse(AbstractModel):
    """OfflineDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
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


class OsInfo(AbstractModel):
    """操作系统类型

    """

    def __init__(self):
        r"""
        :param _OsTypeId: 操作系统ID
        :type OsTypeId: int
        :param _OsName: 操作系统名称
        :type OsName: str
        :param _OsDescription: 操作系统名称描述
        :type OsDescription: str
        :param _OsEnglishDescription: 操作系统英文名称
        :type OsEnglishDescription: str
        :param _OsClass: 操作系统的分类，如CentOs Debian
        :type OsClass: str
        :param _ImageTag: 标识镜像分类。public:公共镜像; private: 专属镜像
        :type ImageTag: str
        :param _MaxPartitionSize: 操作系统，ext4文件下所支持的最大的磁盘大小。单位为T
        :type MaxPartitionSize: int
        :param _OsMinorVersion: 黑石版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OsMinorVersion: str
        :param _OsMinorClass: 黑石版本
注意：此字段可能返回 null，表示取不到有效值。
        :type OsMinorClass: str
        """
        self._OsTypeId = None
        self._OsName = None
        self._OsDescription = None
        self._OsEnglishDescription = None
        self._OsClass = None
        self._ImageTag = None
        self._MaxPartitionSize = None
        self._OsMinorVersion = None
        self._OsMinorClass = None

    @property
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def OsDescription(self):
        return self._OsDescription

    @OsDescription.setter
    def OsDescription(self, OsDescription):
        self._OsDescription = OsDescription

    @property
    def OsEnglishDescription(self):
        return self._OsEnglishDescription

    @OsEnglishDescription.setter
    def OsEnglishDescription(self, OsEnglishDescription):
        self._OsEnglishDescription = OsEnglishDescription

    @property
    def OsClass(self):
        return self._OsClass

    @OsClass.setter
    def OsClass(self, OsClass):
        self._OsClass = OsClass

    @property
    def ImageTag(self):
        return self._ImageTag

    @ImageTag.setter
    def ImageTag(self, ImageTag):
        self._ImageTag = ImageTag

    @property
    def MaxPartitionSize(self):
        return self._MaxPartitionSize

    @MaxPartitionSize.setter
    def MaxPartitionSize(self, MaxPartitionSize):
        self._MaxPartitionSize = MaxPartitionSize

    @property
    def OsMinorVersion(self):
        return self._OsMinorVersion

    @OsMinorVersion.setter
    def OsMinorVersion(self, OsMinorVersion):
        self._OsMinorVersion = OsMinorVersion

    @property
    def OsMinorClass(self):
        return self._OsMinorClass

    @OsMinorClass.setter
    def OsMinorClass(self, OsMinorClass):
        self._OsMinorClass = OsMinorClass


    def _deserialize(self, params):
        self._OsTypeId = params.get("OsTypeId")
        self._OsName = params.get("OsName")
        self._OsDescription = params.get("OsDescription")
        self._OsEnglishDescription = params.get("OsEnglishDescription")
        self._OsClass = params.get("OsClass")
        self._ImageTag = params.get("ImageTag")
        self._MaxPartitionSize = params.get("MaxPartitionSize")
        self._OsMinorVersion = params.get("OsMinorVersion")
        self._OsMinorClass = params.get("OsMinorClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionInfo(AbstractModel):
    """描述设备分区信息

    """

    def __init__(self):
        r"""
        :param _Name: 分区名称
        :type Name: str
        :param _Size: 分区大小
        :type Size: int
        """
        self._Name = None
        self._Size = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PsaRegulation(AbstractModel):
    """一条预授权规则

    """

    def __init__(self):
        r"""
        :param _PsaId: 规则ID
        :type PsaId: str
        :param _PsaName: 规则别名
        :type PsaName: str
        :param _TagCount: 关联标签数量
        :type TagCount: int
        :param _InstanceCount: 关联实例数量
        :type InstanceCount: int
        :param _RepairCount: 故障实例数量
        :type RepairCount: int
        :param _RepairLimit: 故障实例上限
        :type RepairLimit: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PsaDescription: 规则备注
        :type PsaDescription: str
        :param _Tags: 关联标签
        :type Tags: list of Tag
        :param _TaskTypeIds: 关联故障类型id
        :type TaskTypeIds: list of int non-negative
        """
        self._PsaId = None
        self._PsaName = None
        self._TagCount = None
        self._InstanceCount = None
        self._RepairCount = None
        self._RepairLimit = None
        self._CreateTime = None
        self._PsaDescription = None
        self._Tags = None
        self._TaskTypeIds = None

    @property
    def PsaId(self):
        return self._PsaId

    @PsaId.setter
    def PsaId(self, PsaId):
        self._PsaId = PsaId

    @property
    def PsaName(self):
        return self._PsaName

    @PsaName.setter
    def PsaName(self, PsaName):
        self._PsaName = PsaName

    @property
    def TagCount(self):
        return self._TagCount

    @TagCount.setter
    def TagCount(self, TagCount):
        self._TagCount = TagCount

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def RepairCount(self):
        return self._RepairCount

    @RepairCount.setter
    def RepairCount(self, RepairCount):
        self._RepairCount = RepairCount

    @property
    def RepairLimit(self):
        return self._RepairLimit

    @RepairLimit.setter
    def RepairLimit(self, RepairLimit):
        self._RepairLimit = RepairLimit

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PsaDescription(self):
        return self._PsaDescription

    @PsaDescription.setter
    def PsaDescription(self, PsaDescription):
        self._PsaDescription = PsaDescription

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TaskTypeIds(self):
        return self._TaskTypeIds

    @TaskTypeIds.setter
    def TaskTypeIds(self, TaskTypeIds):
        self._TaskTypeIds = TaskTypeIds


    def _deserialize(self, params):
        self._PsaId = params.get("PsaId")
        self._PsaName = params.get("PsaName")
        self._TagCount = params.get("TagCount")
        self._InstanceCount = params.get("InstanceCount")
        self._RepairCount = params.get("RepairCount")
        self._RepairLimit = params.get("RepairLimit")
        self._CreateTime = params.get("CreateTime")
        self._PsaDescription = params.get("PsaDescription")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TaskTypeIds = params.get("TaskTypeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootDevicesRequest(AbstractModel):
    """RebootDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要重启的设备ID列表
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
        


class RebootDevicesResponse(AbstractModel):
    """RebootDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
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


class RecoverDevicesRequest(AbstractModel):
    """RecoverDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要恢复的物理机ID列表
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
        


class RecoverDevicesResponse(AbstractModel):
    """RecoverDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
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


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域ID
        :type Region: str
        :param _RegionId: 地域整型ID
        :type RegionId: int
        :param _RegionDescription: 地域描述
        :type RegionDescription: str
        :param _ZoneInfoSet: 该地域下的可用区信息
        :type ZoneInfoSet: list of ZoneInfo
        """
        self._Region = None
        self._RegionId = None
        self._RegionDescription = None
        self._ZoneInfoSet = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionDescription(self):
        return self._RegionDescription

    @RegionDescription.setter
    def RegionDescription(self, RegionDescription):
        self._RegionDescription = RegionDescription

    @property
    def ZoneInfoSet(self):
        return self._ZoneInfoSet

    @ZoneInfoSet.setter
    def ZoneInfoSet(self, ZoneInfoSet):
        self._ZoneInfoSet = ZoneInfoSet


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionDescription = params.get("RegionDescription")
        if params.get("ZoneInfoSet") is not None:
            self._ZoneInfoSet = []
            for item in params.get("ZoneInfoSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadDeviceOsRequest(AbstractModel):
    """ReloadDeviceOs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 设备的唯一ID
        :type InstanceId: str
        :param _Password: 密码。 用户设置的linux root或Windows Administrator密码。密码校验规则: <li> Windows机器密码需12到16位，至少包括三项 `[a-z]`,`[A-Z]`,`[0-9]`和`[()`'`~!@#$%^&*-+=_`|`{}[]:;'<>,.?/]`的特殊符号, 密码不能包含Administrator(不区分大小写); <li> Linux机器密码需8到16位，至少包括两项`[a-z,A-Z]`,`[0-9]`和`[()`'`~!@#$%^&*-+=_`|`{}[]:;'<>,.?/]`的特殊符号
        :type Password: str
        :param _OsTypeId: 操作系统类型ID。通过接口[查询操作系统信息(DescribeOsInfo)](https://cloud.tencent.com/document/api/386/32902)获取操作系统信息
        :type OsTypeId: int
        :param _RaidId: RAID类型ID。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)获取RAID信息
        :type RaidId: int
        :param _IsZoning: 是否格式化数据盘。0: 不格式化（默认值）；1：格式化
        :type IsZoning: int
        :param _SysRootSpace: 系统盘根分区大小，默认是10G。系统盘的大小参考接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/32910)
        :type SysRootSpace: int
        :param _SysSwaporuefiSpace: 系统盘swap分区或/boot/efi分区的大小。若是uefi启动的机器，分区为/boot/efi ,且此值是默认是2G。普通机器为swap分区，可以不指定此分区。机型是否是uefi启动，参考接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/32911)
        :type SysSwaporuefiSpace: int
        :param _SysUsrlocalSpace: /usr/local分区大小
        :type SysUsrlocalSpace: int
        :param _VpcId: 重装到新的私有网络的ID。如果改变VPC子网，则要求与SubnetId同时传参，否则可不填
        :type VpcId: str
        :param _SubnetId: 重装到新的子网的ID。如果改变VPC子网，则要求与VpcId同时传参，否则可不填
        :type SubnetId: str
        :param _LanIp: 重装指定IP地址
        :type LanIp: str
        :param _HyperThreading: 指定是否开启超线程。 0：关闭超线程；1：开启超线程（默认值）
        :type HyperThreading: int
        :param _ImageId: 自定义镜像ID。传此字段则用自定义镜像重装
        :type ImageId: str
        :param _FileSystem: 指定数据盘的文件系统格式，当前支持 EXT4和XFS选项， 默认为EXT4。 参数适用于数据盘和Linux， 且在IsZoning为1时生效
        :type FileSystem: str
        :param _NeedSecurityAgent: 是否安装安全Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedSecurityAgent: int
        :param _NeedMonitorAgent: 是否安装监控Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedMonitorAgent: int
        :param _NeedEMRAgent: 是否安装EMR Agent，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRAgent: int
        :param _NeedEMRSoftware: 是否安装EMR软件包，取值：1(安装) 0(不安装)，默认取值0
        :type NeedEMRSoftware: int
        :param _ReserveSgConfig: 是否保留安全组配置，取值：1(保留) 0(不保留)，默认取值0
        :type ReserveSgConfig: int
        :param _SysDataSpace: /data分区大小，可不填。除root、swap、usr/local的剩余空间会自动分配到data分区
        :type SysDataSpace: int
        """
        self._InstanceId = None
        self._Password = None
        self._OsTypeId = None
        self._RaidId = None
        self._IsZoning = None
        self._SysRootSpace = None
        self._SysSwaporuefiSpace = None
        self._SysUsrlocalSpace = None
        self._VpcId = None
        self._SubnetId = None
        self._LanIp = None
        self._HyperThreading = None
        self._ImageId = None
        self._FileSystem = None
        self._NeedSecurityAgent = None
        self._NeedMonitorAgent = None
        self._NeedEMRAgent = None
        self._NeedEMRSoftware = None
        self._ReserveSgConfig = None
        self._SysDataSpace = None

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
    def OsTypeId(self):
        return self._OsTypeId

    @OsTypeId.setter
    def OsTypeId(self, OsTypeId):
        self._OsTypeId = OsTypeId

    @property
    def RaidId(self):
        return self._RaidId

    @RaidId.setter
    def RaidId(self, RaidId):
        self._RaidId = RaidId

    @property
    def IsZoning(self):
        return self._IsZoning

    @IsZoning.setter
    def IsZoning(self, IsZoning):
        self._IsZoning = IsZoning

    @property
    def SysRootSpace(self):
        return self._SysRootSpace

    @SysRootSpace.setter
    def SysRootSpace(self, SysRootSpace):
        self._SysRootSpace = SysRootSpace

    @property
    def SysSwaporuefiSpace(self):
        return self._SysSwaporuefiSpace

    @SysSwaporuefiSpace.setter
    def SysSwaporuefiSpace(self, SysSwaporuefiSpace):
        self._SysSwaporuefiSpace = SysSwaporuefiSpace

    @property
    def SysUsrlocalSpace(self):
        return self._SysUsrlocalSpace

    @SysUsrlocalSpace.setter
    def SysUsrlocalSpace(self, SysUsrlocalSpace):
        self._SysUsrlocalSpace = SysUsrlocalSpace

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
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def HyperThreading(self):
        return self._HyperThreading

    @HyperThreading.setter
    def HyperThreading(self, HyperThreading):
        self._HyperThreading = HyperThreading

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def NeedSecurityAgent(self):
        return self._NeedSecurityAgent

    @NeedSecurityAgent.setter
    def NeedSecurityAgent(self, NeedSecurityAgent):
        self._NeedSecurityAgent = NeedSecurityAgent

    @property
    def NeedMonitorAgent(self):
        return self._NeedMonitorAgent

    @NeedMonitorAgent.setter
    def NeedMonitorAgent(self, NeedMonitorAgent):
        self._NeedMonitorAgent = NeedMonitorAgent

    @property
    def NeedEMRAgent(self):
        return self._NeedEMRAgent

    @NeedEMRAgent.setter
    def NeedEMRAgent(self, NeedEMRAgent):
        self._NeedEMRAgent = NeedEMRAgent

    @property
    def NeedEMRSoftware(self):
        return self._NeedEMRSoftware

    @NeedEMRSoftware.setter
    def NeedEMRSoftware(self, NeedEMRSoftware):
        self._NeedEMRSoftware = NeedEMRSoftware

    @property
    def ReserveSgConfig(self):
        return self._ReserveSgConfig

    @ReserveSgConfig.setter
    def ReserveSgConfig(self, ReserveSgConfig):
        self._ReserveSgConfig = ReserveSgConfig

    @property
    def SysDataSpace(self):
        return self._SysDataSpace

    @SysDataSpace.setter
    def SysDataSpace(self, SysDataSpace):
        self._SysDataSpace = SysDataSpace


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._OsTypeId = params.get("OsTypeId")
        self._RaidId = params.get("RaidId")
        self._IsZoning = params.get("IsZoning")
        self._SysRootSpace = params.get("SysRootSpace")
        self._SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self._SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._LanIp = params.get("LanIp")
        self._HyperThreading = params.get("HyperThreading")
        self._ImageId = params.get("ImageId")
        self._FileSystem = params.get("FileSystem")
        self._NeedSecurityAgent = params.get("NeedSecurityAgent")
        self._NeedMonitorAgent = params.get("NeedMonitorAgent")
        self._NeedEMRAgent = params.get("NeedEMRAgent")
        self._NeedEMRSoftware = params.get("NeedEMRSoftware")
        self._ReserveSgConfig = params.get("ReserveSgConfig")
        self._SysDataSpace = params.get("SysDataSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadDeviceOsResponse(AbstractModel):
    """ReloadDeviceOs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
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


class RepairTaskControlRequest(AbstractModel):
    """RepairTaskControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 维修任务ID
        :type TaskId: str
        :param _Operate: 操作
        :type Operate: str
        :param _OperateRemark: 需要重新维修操作的备注信息，可提供返场维修原因，以便驻场快速针对问题定位解决。
        :type OperateRemark: str
        """
        self._TaskId = None
        self._Operate = None
        self._OperateRemark = None

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
    def OperateRemark(self):
        return self._OperateRemark

    @OperateRemark.setter
    def OperateRemark(self, OperateRemark):
        self._OperateRemark = OperateRemark


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Operate = params.get("Operate")
        self._OperateRemark = params.get("OperateRemark")
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
        :param _TaskId: 出参TaskId是黑石异步任务ID，不同于入参TaskId字段。
此字段可作为DescriptionOperationResult查询异步任务状态接口的入参，查询异步任务执行结果。
        :type TaskId: int
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


class ResetDevicePasswordRequest(AbstractModel):
    """ResetDevicePassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要重置密码的服务器ID列表
        :type InstanceIds: list of str
        :param _Password: 新密码
        :type Password: str
        """
        self._InstanceIds = None
        self._Password = None

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


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDevicePasswordResponse(AbstractModel):
    """ResetDevicePassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
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


class ReturnDevicesRequest(AbstractModel):
    """ReturnDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要退还的物理机ID列表
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
        


class ReturnDevicesResponse(AbstractModel):
    """ReturnDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
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


class RunUserCmdRequest(AbstractModel):
    """RunUserCmd请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CmdId: 自定义脚本ID
        :type CmdId: str
        :param _UserName: 执行脚本机器的用户名
        :type UserName: str
        :param _Password: 执行脚本机器的用户名的密码
        :type Password: str
        :param _InstanceIds: 执行脚本的服务器实例
        :type InstanceIds: list of str
        :param _CmdParam: 执行脚本的参数，必须经过base64编码
        :type CmdParam: str
        """
        self._CmdId = None
        self._UserName = None
        self._Password = None
        self._InstanceIds = None
        self._CmdParam = None

    @property
    def CmdId(self):
        return self._CmdId

    @CmdId.setter
    def CmdId(self, CmdId):
        self._CmdId = CmdId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def CmdParam(self):
        return self._CmdParam

    @CmdParam.setter
    def CmdParam(self, CmdParam):
        self._CmdParam = CmdParam


    def _deserialize(self, params):
        self._CmdId = params.get("CmdId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._InstanceIds = params.get("InstanceIds")
        self._CmdParam = params.get("CmdParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunUserCmdResponse(AbstractModel):
    """RunUserCmd返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessTaskInfoSet: 运行成功的任务信息列表
        :type SuccessTaskInfoSet: list of SuccessTaskInfo
        :param _FailedTaskInfoSet: 运行失败的任务信息列表
        :type FailedTaskInfoSet: list of FailedTaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessTaskInfoSet = None
        self._FailedTaskInfoSet = None
        self._RequestId = None

    @property
    def SuccessTaskInfoSet(self):
        return self._SuccessTaskInfoSet

    @SuccessTaskInfoSet.setter
    def SuccessTaskInfoSet(self, SuccessTaskInfoSet):
        self._SuccessTaskInfoSet = SuccessTaskInfoSet

    @property
    def FailedTaskInfoSet(self):
        return self._FailedTaskInfoSet

    @FailedTaskInfoSet.setter
    def FailedTaskInfoSet(self, FailedTaskInfoSet):
        self._FailedTaskInfoSet = FailedTaskInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SuccessTaskInfoSet") is not None:
            self._SuccessTaskInfoSet = []
            for item in params.get("SuccessTaskInfoSet"):
                obj = SuccessTaskInfo()
                obj._deserialize(item)
                self._SuccessTaskInfoSet.append(obj)
        if params.get("FailedTaskInfoSet") is not None:
            self._FailedTaskInfoSet = []
            for item in params.get("FailedTaskInfoSet"):
                obj = FailedTaskInfo()
                obj._deserialize(item)
                self._FailedTaskInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class SetOutBandVpnAuthPasswordRequest(AbstractModel):
    """SetOutBandVpnAuthPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: 设置的Vpn认证密码
        :type Password: str
        :param _Operate: 操作字段，取值为：Create（创建）或Update（修改）
        :type Operate: str
        """
        self._Password = None
        self._Operate = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOutBandVpnAuthPasswordResponse(AbstractModel):
    """SetOutBandVpnAuthPassword返回参数结构体

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


class ShutdownDevicesRequest(AbstractModel):
    """ShutdownDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要关闭的设备ID列表
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
        


class ShutdownDevicesResponse(AbstractModel):
    """ShutdownDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
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


class StartDevicesRequest(AbstractModel):
    """StartDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 需要开机的设备ID列表
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
        


class StartDevicesResponse(AbstractModel):
    """StartDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
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


class SubtaskStatus(AbstractModel):
    """各实例对应的异步任务执行结果

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _TaskStatus: 实例ID对应任务的状态，取值如下：<br>
1：成功<br>
2：失败<br>
3：部分成功，部分失败<br>
4：未完成<br>
5：部分成功，部分未完成<br>
6：部分未完成，部分失败<br>
7：部分未完成，部分失败，部分成功
        :type TaskStatus: int
        """
        self._InstanceId = None
        self._TaskStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessTaskInfo(AbstractModel):
    """成功运行的自定义脚本信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 运行脚本的设备ID
        :type InstanceId: str
        :param _TaskId: 黑石异步任务ID
        :type TaskId: int
        :param _CmdTaskId: 黑石自定义脚本运行任务ID
        :type CmdTaskId: str
        """
        self._InstanceId = None
        self._TaskId = None
        self._CmdTaskId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CmdTaskId(self):
        return self._CmdTaskId

    @CmdTaskId.setter
    def CmdTaskId(self, CmdTaskId):
        self._CmdTaskId = CmdTaskId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TaskId = params.get("TaskId")
        self._CmdTaskId = params.get("CmdTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键与值

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValues: 标签键对应的值
        :type TagValues: list of str
        """
        self._TagKey = None
        self._TagValues = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """维护平台维修任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _InstanceId: 主机id
        :type InstanceId: str
        :param _Alias: 主机别名
        :type Alias: str
        :param _TaskTypeId: 故障类型id
        :type TaskTypeId: int
        :param _TaskStatus: 任务状态id
        :type TaskStatus: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AuthTime: 授权时间
        :type AuthTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _TaskDetail: 任务详情
        :type TaskDetail: str
        :param _DeviceStatus: 设备状态
        :type DeviceStatus: int
        :param _OperateStatus: 设备操作状态
        :type OperateStatus: int
        :param _Zone: 可用区
        :type Zone: str
        :param _Region: 地域
        :type Region: str
        :param _VpcId: 所属网络
        :type VpcId: str
        :param _SubnetId: 所在子网
        :type SubnetId: str
        :param _SubnetName: 子网名
        :type SubnetName: str
        :param _VpcName: VPC名
        :type VpcName: str
        :param _VpcCidrBlock: VpcCidrBlock
        :type VpcCidrBlock: str
        :param _SubnetCidrBlock: SubnetCidrBlock
        :type SubnetCidrBlock: str
        :param _WanIp: 公网ip
        :type WanIp: str
        :param _LanIp: 内网IP
        :type LanIp: str
        :param _MgtIp: 管理IP
        :type MgtIp: str
        :param _TaskTypeName: 故障类中文名
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        :param _TaskSubType: 故障类型，取值：unconfirmed (不明确故障)；redundancy (有冗余故障)；nonredundancy (无冗余故障)
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSubType: str
        """
        self._TaskId = None
        self._InstanceId = None
        self._Alias = None
        self._TaskTypeId = None
        self._TaskStatus = None
        self._CreateTime = None
        self._AuthTime = None
        self._EndTime = None
        self._TaskDetail = None
        self._DeviceStatus = None
        self._OperateStatus = None
        self._Zone = None
        self._Region = None
        self._VpcId = None
        self._SubnetId = None
        self._SubnetName = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._SubnetCidrBlock = None
        self._WanIp = None
        self._LanIp = None
        self._MgtIp = None
        self._TaskTypeName = None
        self._TaskSubType = None

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
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

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
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetCidrBlock(self):
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock

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
    def MgtIp(self):
        return self._MgtIp

    @MgtIp.setter
    def MgtIp(self, MgtIp):
        self._MgtIp = MgtIp

    @property
    def TaskTypeName(self):
        return self._TaskTypeName

    @TaskTypeName.setter
    def TaskTypeName(self, TaskTypeName):
        self._TaskTypeName = TaskTypeName

    @property
    def TaskSubType(self):
        return self._TaskSubType

    @TaskSubType.setter
    def TaskSubType(self, TaskSubType):
        self._TaskSubType = TaskSubType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        self._TaskTypeId = params.get("TaskTypeId")
        self._TaskStatus = params.get("TaskStatus")
        self._CreateTime = params.get("CreateTime")
        self._AuthTime = params.get("AuthTime")
        self._EndTime = params.get("EndTime")
        self._TaskDetail = params.get("TaskDetail")
        self._DeviceStatus = params.get("DeviceStatus")
        self._OperateStatus = params.get("OperateStatus")
        self._Zone = params.get("Zone")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        self._WanIp = params.get("WanIp")
        self._LanIp = params.get("LanIp")
        self._MgtIp = params.get("MgtIp")
        self._TaskTypeName = params.get("TaskTypeName")
        self._TaskSubType = params.get("TaskSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOperationLog(AbstractModel):
    """维修任务操作日志

    """

    def __init__(self):
        r"""
        :param _TaskStep: 操作步骤
        :type TaskStep: str
        :param _Operator: 操作人
        :type Operator: str
        :param _OperationDetail: 操作描述
        :type OperationDetail: str
        :param _OperationTime: 操作时间
        :type OperationTime: str
        """
        self._TaskStep = None
        self._Operator = None
        self._OperationDetail = None
        self._OperationTime = None

    @property
    def TaskStep(self):
        return self._TaskStep

    @TaskStep.setter
    def TaskStep(self, TaskStep):
        self._TaskStep = TaskStep

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def OperationDetail(self):
        return self._OperationDetail

    @OperationDetail.setter
    def OperationDetail(self, OperationDetail):
        self._OperationDetail = OperationDetail

    @property
    def OperationTime(self):
        return self._OperationTime

    @OperationTime.setter
    def OperationTime(self, OperationTime):
        self._OperationTime = OperationTime


    def _deserialize(self, params):
        self._TaskStep = params.get("TaskStep")
        self._Operator = params.get("Operator")
        self._OperationDetail = params.get("OperationDetail")
        self._OperationTime = params.get("OperationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskType(AbstractModel):
    """故障id对应故障名列表

    """

    def __init__(self):
        r"""
        :param _TypeId: 故障类ID
        :type TypeId: int
        :param _TypeName: 故障类中文名
        :type TypeName: str
        :param _TaskSubType: 故障类型父类
        :type TaskSubType: str
        """
        self._TypeId = None
        self._TypeName = None
        self._TaskSubType = None

    @property
    def TypeId(self):
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def TaskSubType(self):
        return self._TaskSubType

    @TaskSubType.setter
    def TaskSubType(self, TaskSubType):
        self._TaskSubType = TaskSubType


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        self._TypeName = params.get("TypeName")
        self._TaskSubType = params.get("TaskSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindPsaTagRequest(AbstractModel):
    """UnbindPsaTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PsaId: 预授权规则ID
        :type PsaId: str
        :param _TagKey: 需要解绑的标签key
        :type TagKey: str
        :param _TagValue: 需要解绑的标签value
        :type TagValue: str
        """
        self._PsaId = None
        self._TagKey = None
        self._TagValue = None

    @property
    def PsaId(self):
        return self._PsaId

    @PsaId.setter
    def PsaId(self, PsaId):
        self._PsaId = PsaId

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._PsaId = params.get("PsaId")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindPsaTagResponse(AbstractModel):
    """UnbindPsaTag返回参数结构体

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


class UserCmd(AbstractModel):
    """脚本信息

    """

    def __init__(self):
        r"""
        :param _Alias: 用户自定义脚本名
        :type Alias: str
        :param _AppId: AppId
        :type AppId: int
        :param _AutoId: 脚本自增ID
        :type AutoId: int
        :param _CmdId: 脚本ID
        :type CmdId: str
        :param _Content: 脚本内容
        :type Content: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _OsType: 命令适用的操作系统类型
        :type OsType: str
        """
        self._Alias = None
        self._AppId = None
        self._AutoId = None
        self._CmdId = None
        self._Content = None
        self._CreateTime = None
        self._ModifyTime = None
        self._OsType = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AutoId(self):
        return self._AutoId

    @AutoId.setter
    def AutoId(self, AutoId):
        self._AutoId = AutoId

    @property
    def CmdId(self):
        return self._CmdId

    @CmdId.setter
    def CmdId(self, CmdId):
        self._CmdId = CmdId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._AppId = params.get("AppId")
        self._AutoId = params.get("AutoId")
        self._CmdId = params.get("CmdId")
        self._Content = params.get("Content")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._OsType = params.get("OsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserCmdTask(AbstractModel):
    """自定义脚本任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Status: 任务状态ID，取值: -1(进行中) 0(结束)
        :type Status: int
        :param _Alias: 脚本名称
        :type Alias: str
        :param _CmdId: 脚本ID
        :type CmdId: str
        :param _InstanceCount: 运行实例数量
        :type InstanceCount: int
        :param _SuccessCount: 运行成功数量
        :type SuccessCount: int
        :param _FailureCount: 运行失败数量
        :type FailureCount: int
        :param _RunBeginTime: 执行开始时间
        :type RunBeginTime: str
        :param _RunEndTime: 执行结束时间
        :type RunEndTime: str
        """
        self._TaskId = None
        self._Status = None
        self._Alias = None
        self._CmdId = None
        self._InstanceCount = None
        self._SuccessCount = None
        self._FailureCount = None
        self._RunBeginTime = None
        self._RunEndTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CmdId(self):
        return self._CmdId

    @CmdId.setter
    def CmdId(self, CmdId):
        self._CmdId = CmdId

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailureCount(self):
        return self._FailureCount

    @FailureCount.setter
    def FailureCount(self, FailureCount):
        self._FailureCount = FailureCount

    @property
    def RunBeginTime(self):
        return self._RunBeginTime

    @RunBeginTime.setter
    def RunBeginTime(self, RunBeginTime):
        self._RunBeginTime = RunBeginTime

    @property
    def RunEndTime(self):
        return self._RunEndTime

    @RunEndTime.setter
    def RunEndTime(self, RunEndTime):
        self._RunEndTime = RunEndTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._Alias = params.get("Alias")
        self._CmdId = params.get("CmdId")
        self._InstanceCount = params.get("InstanceCount")
        self._SuccessCount = params.get("SuccessCount")
        self._FailureCount = params.get("FailureCount")
        self._RunBeginTime = params.get("RunBeginTime")
        self._RunEndTime = params.get("RunEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserCmdTaskInfo(AbstractModel):
    """自定义脚本任务详细信息

    """

    def __init__(self):
        r"""
        :param _AutoId: 自动编号，可忽略
        :type AutoId: int
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RunBeginTime: 任务开始时间
        :type RunBeginTime: str
        :param _RunEndTime: 任务结束时间
        :type RunEndTime: str
        :param _Status: 任务状态ID，取值为 -1：进行中；0：成功；>0：失败错误码
        :type Status: int
        :param _InstanceName: 设备别名
        :type InstanceName: str
        :param _InstanceId: 设备ID
        :type InstanceId: str
        :param _VpcName: 私有网络名
        :type VpcName: str
        :param _VpcId: 私有网络整型ID
        :type VpcId: str
        :param _VpcCidrBlock: 私有网络Cidr
        :type VpcCidrBlock: str
        :param _SubnetName: 子网名
        :type SubnetName: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _SubnetCidrBlock: 子网Cidr
        :type SubnetCidrBlock: str
        :param _LanIp: 内网IP
        :type LanIp: str
        :param _CmdContent: 脚本内容，base64编码后的值
        :type CmdContent: str
        :param _CmdParam: 脚本参数，base64编码后的值
        :type CmdParam: str
        :param _CmdResult: 脚本执行结果，base64编码后的值
        :type CmdResult: str
        :param _AppId: 用户AppId
        :type AppId: int
        :param _LastShellExit: 用户执行脚本结束退出的返回值，没有返回值为-1
        :type LastShellExit: int
        """
        self._AutoId = None
        self._TaskId = None
        self._RunBeginTime = None
        self._RunEndTime = None
        self._Status = None
        self._InstanceName = None
        self._InstanceId = None
        self._VpcName = None
        self._VpcId = None
        self._VpcCidrBlock = None
        self._SubnetName = None
        self._SubnetId = None
        self._SubnetCidrBlock = None
        self._LanIp = None
        self._CmdContent = None
        self._CmdParam = None
        self._CmdResult = None
        self._AppId = None
        self._LastShellExit = None

    @property
    def AutoId(self):
        return self._AutoId

    @AutoId.setter
    def AutoId(self, AutoId):
        self._AutoId = AutoId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RunBeginTime(self):
        return self._RunBeginTime

    @RunBeginTime.setter
    def RunBeginTime(self, RunBeginTime):
        self._RunBeginTime = RunBeginTime

    @property
    def RunEndTime(self):
        return self._RunEndTime

    @RunEndTime.setter
    def RunEndTime(self, RunEndTime):
        self._RunEndTime = RunEndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetCidrBlock(self):
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock

    @property
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def CmdContent(self):
        return self._CmdContent

    @CmdContent.setter
    def CmdContent(self, CmdContent):
        self._CmdContent = CmdContent

    @property
    def CmdParam(self):
        return self._CmdParam

    @CmdParam.setter
    def CmdParam(self, CmdParam):
        self._CmdParam = CmdParam

    @property
    def CmdResult(self):
        return self._CmdResult

    @CmdResult.setter
    def CmdResult(self, CmdResult):
        self._CmdResult = CmdResult

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def LastShellExit(self):
        return self._LastShellExit

    @LastShellExit.setter
    def LastShellExit(self, LastShellExit):
        self._LastShellExit = LastShellExit


    def _deserialize(self, params):
        self._AutoId = params.get("AutoId")
        self._TaskId = params.get("TaskId")
        self._RunBeginTime = params.get("RunBeginTime")
        self._RunEndTime = params.get("RunEndTime")
        self._Status = params.get("Status")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._VpcName = params.get("VpcName")
        self._VpcId = params.get("VpcId")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetName = params.get("SubnetName")
        self._SubnetId = params.get("SubnetId")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        self._LanIp = params.get("LanIp")
        self._CmdContent = params.get("CmdContent")
        self._CmdParam = params.get("CmdParam")
        self._CmdResult = params.get("CmdResult")
        self._AppId = params.get("AppId")
        self._LastShellExit = params.get("LastShellExit")
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
        :param _Zone: 可用区ID
        :type Zone: str
        :param _ZoneId: 可用区整型ID
        :type ZoneId: int
        :param _ZoneDescription: 可用区描述
        :type ZoneDescription: str
        """
        self._Zone = None
        self._ZoneId = None
        self._ZoneDescription = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneDescription(self):
        return self._ZoneDescription

    @ZoneDescription.setter
    def ZoneDescription(self, ZoneDescription):
        self._ZoneDescription = ZoneDescription


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneDescription = params.get("ZoneDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        