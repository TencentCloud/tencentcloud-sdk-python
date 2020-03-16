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


class AvailableProtoStatus(AbstractModel):
    """版本控制-协议详情

    """

    def __init__(self):
        """
        :param SaleStatus: 售卖状态。可选值有 sale_out 售罄、saling可售、no_saling不可销售
        :type SaleStatus: str
        :param Protocol: 协议类型。可选值有 NFS、CIFS
        :type Protocol: str
        """
        self.SaleStatus = None
        self.Protocol = None


    def _deserialize(self, params):
        self.SaleStatus = params.get("SaleStatus")
        self.Protocol = params.get("Protocol")


class AvailableRegion(AbstractModel):
    """版本控制-区域数组

    """

    def __init__(self):
        """
        :param Region: 区域名称，如“ap-beijing”
        :type Region: str
        :param RegionName: 区域名称，如“bj”
        :type RegionName: str
        :param RegionStatus: 区域可用情况，当区域内至少有一个可用区处于可售状态时，取值为AVAILABLE，否则为UNAVAILABLE
        :type RegionStatus: str
        :param Zones: 可用区数组
        :type Zones: list of AvailableZone
        :param RegionCnName: 区域中文名称，如“广州”
        :type RegionCnName: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionStatus = None
        self.Zones = None
        self.RegionCnName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionStatus = params.get("RegionStatus")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = AvailableZone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RegionCnName = params.get("RegionCnName")


class AvailableType(AbstractModel):
    """版本控制-类型数组

    """

    def __init__(self):
        """
        :param Protocols: 协议与售卖详情
        :type Protocols: list of AvailableProtoStatus
        :param Type: 存储类型。可选值有 SD 标准型存储、HP性能型存储
        :type Type: str
        """
        self.Protocols = None
        self.Type = None


    def _deserialize(self, params):
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = AvailableProtoStatus()
                obj._deserialize(item)
                self.Protocols.append(obj)
        self.Type = params.get("Type")


class AvailableZone(AbstractModel):
    """版本控制-可用区数组

    """

    def __init__(self):
        """
        :param Zone: 可用区名称
        :type Zone: str
        :param ZoneId: 可用区ID
        :type ZoneId: int
        :param ZoneCnName: 可用区中文名称
        :type ZoneCnName: str
        :param Types: Type数组
        :type Types: list of AvailableType
        :param ZoneName: 可用区中英文名称
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneCnName = None
        self.Types = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneCnName = params.get("ZoneCnName")
        if params.get("Types") is not None:
            self.Types = []
            for item in params.get("Types"):
                obj = AvailableType()
                obj._deserialize(item)
                self.Types.append(obj)
        self.ZoneName = params.get("ZoneName")


class CreateCfsFileSystemRequest(AbstractModel):
    """CreateCfsFileSystem请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区名称，例如ap-beijing-1，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的地域与可用区列表
        :type Zone: str
        :param NetInterface: 网络类型，值为 VPC，BASIC；其中 VPC 为私有网络，BASIC 为基础网络
        :type NetInterface: str
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param Protocol: 文件系统协议类型， 值为 NFS、CIFS; 若留空则默认为 NFS协议
        :type Protocol: str
        :param StorageType: 文件系统存储类型，值为 SD ；其中 SD 为标准型存储， HP为性能存储。
        :type StorageType: str
        :param VpcId: 私有网络（VPC） ID，若网络类型选择的是VPC，该字段为必填。
        :type VpcId: str
        :param SubnetId: 子网 ID，若网络类型选择的是VPC，该字段为必填。
        :type SubnetId: str
        :param MountIP: 指定IP地址，仅VPC网络支持；若不填写、将在该子网下随机分配 IP
        :type MountIP: str
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        :param ResourceTags: 文件系统标签
        :type ResourceTags: list of TagInfo
        """
        self.Zone = None
        self.NetInterface = None
        self.PGroupId = None
        self.Protocol = None
        self.StorageType = None
        self.VpcId = None
        self.SubnetId = None
        self.MountIP = None
        self.FsName = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NetInterface = params.get("NetInterface")
        self.PGroupId = params.get("PGroupId")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.MountIP = params.get("MountIP")
        self.FsName = params.get("FsName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)


class CreateCfsFileSystemResponse(AbstractModel):
    """CreateCfsFileSystem返回参数结构体

    """

    def __init__(self):
        """
        :param CreationTime: 文件系统创建时间
        :type CreationTime: str
        :param CreationToken: 用户自定义文件系统名称
        :type CreationToken: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param LifeCycleState: 文件系统状态
        :type LifeCycleState: str
        :param SizeByte: 文件系统已使用容量大小
        :type SizeByte: int
        :param ZoneId: 可用区 ID
        :type ZoneId: int
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        :param Encrypted: 文件系统是否加密
        :type Encrypted: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.ZoneId = None
        self.FsName = None
        self.Encrypted = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.ZoneId = params.get("ZoneId")
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.RequestId = params.get("RequestId")


class CreateCfsPGroupRequest(AbstractModel):
    """CreateCfsPGroup请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :type Name: str
        :param DescInfo: 权限组描述信息，1-255个字符
        :type DescInfo: str
        """
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")


class CreateCfsPGroupResponse(AbstractModel):
    """CreateCfsPGroup返回参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param Name: 权限组名字
        :type Name: str
        :param DescInfo: 权限组描述信息
        :type DescInfo: str
        :param BindCfsNum: 已经与该权限组绑定的文件系统个数
        :type BindCfsNum: int
        :param CDate: 权限组创建时间
        :type CDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.BindCfsNum = None
        self.CDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.BindCfsNum = params.get("BindCfsNum")
        self.CDate = params.get("CDate")
        self.RequestId = params.get("RequestId")


class CreateCfsRuleRequest(AbstractModel):
    """CreateCfsRule请求参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :type Priority: int
        :param RWPermission: 读写权限, 值为 RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param UserPermission: 用户权限，值为 all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。不填默认为root_squash。
        :type UserPermission: str
        """
        self.PGroupId = None
        self.AuthClientIp = None
        self.Priority = None
        self.RWPermission = None
        self.UserPermission = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.Priority = params.get("Priority")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")


class CreateCfsRuleResponse(AbstractModel):
    """CreateCfsRule返回参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则 ID
        :type RuleId: str
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param AuthClientIp: 客户端 IP
        :type AuthClientIp: str
        :param RWPermission: 读写权限
        :type RWPermission: str
        :param UserPermission: 用户权限
        :type UserPermission: str
        :param Priority: 优先级
        :type Priority: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class DeleteCfsFileSystemRequest(AbstractModel):
    """DeleteCfsFileSystem请求参数结构体

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系统 ID。说明，进行删除文件系统操作前需要先调用 DeleteMountTarget 接口删除该文件系统的挂载点，否则会删除失败。
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")


class DeleteCfsFileSystemResponse(AbstractModel):
    """DeleteCfsFileSystem返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCfsPGroupRequest(AbstractModel):
    """DeleteCfsPGroup请求参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")


class DeleteCfsPGroupResponse(AbstractModel):
    """DeleteCfsPGroup返回参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param AppId: 用户 ID
        :type AppId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.AppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AppId = params.get("AppId")
        self.RequestId = params.get("RequestId")


class DeleteCfsRuleRequest(AbstractModel):
    """DeleteCfsRule请求参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RuleId: 规则 ID
        :type RuleId: str
        """
        self.PGroupId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")


class DeleteCfsRuleResponse(AbstractModel):
    """DeleteCfsRule返回参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则 ID
        :type RuleId: str
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.RequestId = params.get("RequestId")


class DeleteMountTargetRequest(AbstractModel):
    """DeleteMountTarget请求参数结构体

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param MountTargetId: 挂载点 ID
        :type MountTargetId: str
        """
        self.FileSystemId = None
        self.MountTargetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")


class DeleteMountTargetResponse(AbstractModel):
    """DeleteMountTarget返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAvailableZoneInfoRequest(AbstractModel):
    """DescribeAvailableZoneInfo请求参数结构体

    """


class DescribeAvailableZoneInfoResponse(AbstractModel):
    """DescribeAvailableZoneInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RegionZones: 各可用区的资源售卖情况以及支持的存储类型、存储协议等信息
        :type RegionZones: list of AvailableRegion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionZones = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionZones") is not None:
            self.RegionZones = []
            for item in params.get("RegionZones"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self.RegionZones.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsFileSystemsRequest(AbstractModel):
    """DescribeCfsFileSystems请求参数结构体

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param VpcId: 私有网络（VPC） ID
        :type VpcId: str
        :param SubnetId: 子网 ID
        :type SubnetId: str
        """
        self.FileSystemId = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DescribeCfsFileSystemsResponse(AbstractModel):
    """DescribeCfsFileSystems返回参数结构体

    """

    def __init__(self):
        """
        :param FileSystems: 文件系统信息
        :type FileSystems: list of FileSystemInfo
        :param TotalCount: 文件系统总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileSystems = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemInfo()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCfsPGroupsRequest(AbstractModel):
    """DescribeCfsPGroups请求参数结构体

    """


class DescribeCfsPGroupsResponse(AbstractModel):
    """DescribeCfsPGroups返回参数结构体

    """

    def __init__(self):
        """
        :param PGroupList: 权限组信息列表
        :type PGroupList: list of PGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PGroupList") is not None:
            self.PGroupList = []
            for item in params.get("PGroupList"):
                obj = PGroupInfo()
                obj._deserialize(item)
                self.PGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsRulesRequest(AbstractModel):
    """DescribeCfsRules请求参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")


class DescribeCfsRulesResponse(AbstractModel):
    """DescribeCfsRules返回参数结构体

    """

    def __init__(self):
        """
        :param RuleList: 权限组规则列表
        :type RuleList: list of PGroupRuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = PGroupRuleInfo()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsServiceStatusRequest(AbstractModel):
    """DescribeCfsServiceStatus请求参数结构体

    """


class DescribeCfsServiceStatusResponse(AbstractModel):
    """DescribeCfsServiceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param CfsServiceStatus: 该用户当前 CFS 服务的状态，none 为未开通，creating 为开通中，created 为已开通
        :type CfsServiceStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class DescribeMountTargetsRequest(AbstractModel):
    """DescribeMountTargets请求参数结构体

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")


class DescribeMountTargetsResponse(AbstractModel):
    """DescribeMountTargets返回参数结构体

    """

    def __init__(self):
        """
        :param MountTargets: 挂载点详情
        :type MountTargets: list of MountInfo
        :param NumberOfMountTargets: 挂载点数量
        :type NumberOfMountTargets: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MountTargets = None
        self.NumberOfMountTargets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountTargets") is not None:
            self.MountTargets = []
            for item in params.get("MountTargets"):
                obj = MountInfo()
                obj._deserialize(item)
                self.MountTargets.append(obj)
        self.NumberOfMountTargets = params.get("NumberOfMountTargets")
        self.RequestId = params.get("RequestId")


class FileSystemInfo(AbstractModel):
    """文件系统基本信息

    """

    def __init__(self):
        """
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param CreationToken: 用户自定义名称
        :type CreationToken: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param LifeCycleState: 文件系统状态
        :type LifeCycleState: str
        :param SizeByte: 文件系统已使用容量
        :type SizeByte: int
        :param SizeLimit: 文件系统最大空间限制
        :type SizeLimit: int
        :param ZoneId: 区域 ID
        :type ZoneId: int
        :param Zone: 区域名称
        :type Zone: str
        :param Protocol: 文件系统协议类型
        :type Protocol: str
        :param StorageType: 文件系统存储类型
        :type StorageType: str
        :param StorageResourcePkg: 文件系统绑定的预付费存储包（暂未支持）
        :type StorageResourcePkg: str
        :param BandwidthResourcePkg: 文件系统绑定的预付费带宽包（暂未支持）
        :type BandwidthResourcePkg: str
        :param PGroup: 文件系统绑定权限组信息
        :type PGroup: :class:`tencentcloud.cfs.v20190719.models.PGroup`
        :param FsName: 用户自定义名称
        :type FsName: str
        :param Encrypted: 文件系统是否加密
        :type Encrypted: bool
        :param KmsKeyId: 加密所使用的密钥，可以为密钥的 ID 或者 ARN
        :type KmsKeyId: str
        :param AppId: 应用ID
        :type AppId: int
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.SizeLimit = None
        self.ZoneId = None
        self.Zone = None
        self.Protocol = None
        self.StorageType = None
        self.StorageResourcePkg = None
        self.BandwidthResourcePkg = None
        self.PGroup = None
        self.FsName = None
        self.Encrypted = None
        self.KmsKeyId = None
        self.AppId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.SizeLimit = params.get("SizeLimit")
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.StorageResourcePkg = params.get("StorageResourcePkg")
        self.BandwidthResourcePkg = params.get("BandwidthResourcePkg")
        if params.get("PGroup") is not None:
            self.PGroup = PGroup()
            self.PGroup._deserialize(params.get("PGroup"))
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.KmsKeyId = params.get("KmsKeyId")
        self.AppId = params.get("AppId")


class MountInfo(AbstractModel):
    """挂载点信息

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param MountTargetId: 挂载点 ID
        :type MountTargetId: str
        :param IpAddress: 挂载点 IP
        :type IpAddress: str
        :param FSID: 挂载根目录
        :type FSID: str
        :param LifeCycleState: 挂载点状态
        :type LifeCycleState: str
        :param NetworkInterface: 网络类型
        :type NetworkInterface: str
        :param VpcId: 私有网络 ID
        :type VpcId: str
        :param VpcName: 私有网络名称
        :type VpcName: str
        :param SubnetId: 子网 Id
        :type SubnetId: str
        :param SubnetName: 子网名称
        :type SubnetName: str
        """
        self.FileSystemId = None
        self.MountTargetId = None
        self.IpAddress = None
        self.FSID = None
        self.LifeCycleState = None
        self.NetworkInterface = None
        self.VpcId = None
        self.VpcName = None
        self.SubnetId = None
        self.SubnetName = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")
        self.IpAddress = params.get("IpAddress")
        self.FSID = params.get("FSID")
        self.LifeCycleState = params.get("LifeCycleState")
        self.NetworkInterface = params.get("NetworkInterface")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")


class PGroup(AbstractModel):
    """文件系统绑定权限组信息

    """

    def __init__(self):
        """
        :param PGroupId: 权限组ID
        :type PGroupId: str
        :param Name: 权限组名称
        :type Name: str
        """
        self.PGroupId = None
        self.Name = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")


class PGroupInfo(AbstractModel):
    """权限组数组

    """

    def __init__(self):
        """
        :param PGroupId: 权限组ID
        :type PGroupId: str
        :param Name: 权限组名称
        :type Name: str
        :param DescInfo: 描述信息
        :type DescInfo: str
        :param CDate: 创建时间
        :type CDate: str
        :param BindCfsNum: 关联文件系统个数
        :type BindCfsNum: int
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.CDate = None
        self.BindCfsNum = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.CDate = params.get("CDate")
        self.BindCfsNum = params.get("BindCfsNum")


class PGroupRuleInfo(AbstractModel):
    """权限组规则列表

    """

    def __init__(self):
        """
        :param RuleId: 规则ID
        :type RuleId: str
        :param AuthClientIp: 允许访问的客户端IP
        :type AuthClientIp: str
        :param RWPermission: 读写权限, ro为只读，rw为读写
        :type RWPermission: str
        :param UserPermission: 用户权限。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。
        :type UserPermission: str
        :param Priority: 规则优先级，1-100。 其中 1 为最高，100为最低
        :type Priority: int
        """
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")


class SignUpCfsServiceRequest(AbstractModel):
    """SignUpCfsService请求参数结构体

    """


class SignUpCfsServiceResponse(AbstractModel):
    """SignUpCfsService返回参数结构体

    """

    def __init__(self):
        """
        :param CfsServiceStatus: 该用户当前 CFS 服务的状态，none 是未开通，creating 是开通中，created 是已开通
        :type CfsServiceStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """Tag信息单元

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class UpdateCfsFileSystemNameRequest(AbstractModel):
    """UpdateCfsFileSystemName请求参数结构体

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        """
        self.FileSystemId = None
        self.FsName = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")


class UpdateCfsFileSystemNameResponse(AbstractModel):
    """UpdateCfsFileSystemName返回参数结构体

    """

    def __init__(self):
        """
        :param CreationToken: 用户自定义文件系统名称
        :type CreationToken: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param FsName: 用户自定义文件系统名称
        :type FsName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CreationToken = None
        self.FileSystemId = None
        self.FsName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemPGroupRequest(AbstractModel):
    """UpdateCfsFileSystemPGroup请求参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        """
        self.PGroupId = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")


class UpdateCfsFileSystemPGroupResponse(AbstractModel):
    """UpdateCfsFileSystemPGroup返回参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param FileSystemId: 文件系统 ID
        :type FileSystemId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.FileSystemId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemSizeLimitRequest(AbstractModel):
    """UpdateCfsFileSystemSizeLimit请求参数结构体

    """

    def __init__(self):
        """
        :param FsLimit: 文件系统容量限制大小，输入范围0-1073741824, 单位为GB；其中输入值为0时，表示不限制文件系统容量。
        :type FsLimit: int
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self.FsLimit = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FsLimit = params.get("FsLimit")
        self.FileSystemId = params.get("FileSystemId")


class UpdateCfsFileSystemSizeLimitResponse(AbstractModel):
    """UpdateCfsFileSystemSizeLimit返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateCfsPGroupRequest(AbstractModel):
    """UpdateCfsPGroup请求参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param Name: 权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线
        :type Name: str
        :param DescInfo: 权限组描述信息，1-255个字符
        :type DescInfo: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")


class UpdateCfsPGroupResponse(AbstractModel):
    """UpdateCfsPGroup返回参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组ID
        :type PGroupId: str
        :param Name: 权限组名称
        :type Name: str
        :param DescInfo: 描述信息
        :type DescInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.RequestId = params.get("RequestId")


class UpdateCfsRuleRequest(AbstractModel):
    """UpdateCfsRule请求参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RuleId: 规则 ID
        :type RuleId: str
        :param AuthClientIp: 可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。
        :type AuthClientIp: str
        :param RWPermission: 读写权限, 值为RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读
        :type RWPermission: str
        :param UserPermission: 用户权限，值为all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。不填默认为root_squash。
        :type UserPermission: str
        :param Priority: 规则优先级，参数范围1-100。 其中 1 为最高，100为最低
        :type Priority: int
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")


class UpdateCfsRuleResponse(AbstractModel):
    """UpdateCfsRule返回参数结构体

    """

    def __init__(self):
        """
        :param PGroupId: 权限组 ID
        :type PGroupId: str
        :param RuleId: 规则 ID
        :type RuleId: str
        :param AuthClientIp: 允许访问的客户端 IP 或者 IP 段
        :type AuthClientIp: str
        :param RWPermission: 读写权限
        :type RWPermission: str
        :param UserPermission: 用户权限
        :type UserPermission: str
        :param Priority: 优先级
        :type Priority: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")