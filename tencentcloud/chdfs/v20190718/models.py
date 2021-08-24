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


class AccessGroup(AbstractModel):
    """权限组

    """

    def __init__(self):
        r"""
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param Description: 权限组描述
        :type Description: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.AccessGroupId = None
        self.AccessGroupName = None
        self.Description = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRule(AbstractModel):
    """权限规则

    """

    def __init__(self):
        r"""
        :param AccessRuleId: 权限规则ID
        :type AccessRuleId: int
        :param Address: 权限规则地址（网段或IP）
        :type Address: str
        :param AccessMode: 权限规则访问模式（1：只读；2：读写）
        :type AccessMode: int
        :param Priority: 优先级（取值范围1~100，值越小优先级越高）
        :type Priority: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.AccessRuleId = None
        self.Address = None
        self.AccessMode = None
        self.Priority = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessRuleId = params.get("AccessRuleId")
        self.Address = params.get("Address")
        self.AccessMode = params.get("AccessMode")
        self.Priority = params.get("Priority")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessGroupRequest(AbstractModel):
    """CreateAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param Description: 权限组描述
        :type Description: str
        """
        self.AccessGroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessGroupResponse(AbstractModel):
    """CreateAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccessGroup: 权限组
        :type AccessGroup: :class:`tencentcloud.chdfs.v20190718.models.AccessGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self.AccessGroup = AccessGroup()
            self.AccessGroup._deserialize(params.get("AccessGroup"))
        self.RequestId = params.get("RequestId")


class CreateAccessRulesRequest(AbstractModel):
    """CreateAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessRules: 多个权限规则，上限为10
        :type AccessRules: list of AccessRule
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self.AccessRules = None
        self.AccessGroupId = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        self.AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessRulesResponse(AbstractModel):
    """CreateAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param CapacityQuota: 文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍
        :type CapacityQuota: int
        :param Description: 文件系统描述
        :type Description: str
        """
        self.FileSystemName = None
        self.CapacityQuota = None
        self.Description = None


    def _deserialize(self, params):
        self.FileSystemName = params.get("FileSystemName")
        self.CapacityQuota = params.get("CapacityQuota")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileSystemResponse(AbstractModel):
    """CreateFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystem: 文件系统
        :type FileSystem: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileSystem = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self.FileSystem = FileSystem()
            self.FileSystem._deserialize(params.get("FileSystem"))
        self.RequestId = params.get("RequestId")


class CreateLifeCycleRulesRequest(AbstractModel):
    """CreateLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param LifeCycleRules: 多个生命周期规则，上限为10
        :type LifeCycleRules: list of LifeCycleRule
        """
        self.FileSystemId = None
        self.LifeCycleRules = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        if params.get("LifeCycleRules") is not None:
            self.LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self.LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifeCycleRulesResponse(AbstractModel):
    """CreateLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMountPointRequest(AbstractModel):
    """CreateMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param MountPointName: 挂载点名称
        :type MountPointName: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param VpcId: VPC网络ID
        :type VpcId: str
        :param MountPointStatus: 挂载点状态（1：打开；2：关闭）
        :type MountPointStatus: int
        :param VpcType: VPC网络类型（1：CVM；2：黑石1.0；3：黑石2.0）
        :type VpcType: int
        """
        self.MountPointName = None
        self.FileSystemId = None
        self.AccessGroupId = None
        self.VpcId = None
        self.MountPointStatus = None
        self.VpcType = None


    def _deserialize(self, params):
        self.MountPointName = params.get("MountPointName")
        self.FileSystemId = params.get("FileSystemId")
        self.AccessGroupId = params.get("AccessGroupId")
        self.VpcId = params.get("VpcId")
        self.MountPointStatus = params.get("MountPointStatus")
        self.VpcType = params.get("VpcType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMountPointResponse(AbstractModel):
    """CreateMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param MountPoint: 挂载点
        :type MountPoint: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MountPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self.MountPoint = MountPoint()
            self.MountPoint._deserialize(params.get("MountPoint"))
        self.RequestId = params.get("RequestId")


class CreateRestoreTasksRequest(AbstractModel):
    """CreateRestoreTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param RestoreTasks: 多个回热任务，上限为10
        :type RestoreTasks: list of RestoreTask
        """
        self.FileSystemId = None
        self.RestoreTasks = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        if params.get("RestoreTasks") is not None:
            self.RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self.RestoreTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRestoreTasksResponse(AbstractModel):
    """CreateRestoreTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAccessGroupRequest(AbstractModel):
    """DeleteAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self.AccessGroupId = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessGroupResponse(AbstractModel):
    """DeleteAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAccessRulesRequest(AbstractModel):
    """DeleteAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessRuleIds: 多个权限规则ID，上限为10
        :type AccessRuleIds: list of int non-negative
        """
        self.AccessRuleIds = None


    def _deserialize(self, params):
        self.AccessRuleIds = params.get("AccessRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessRulesResponse(AbstractModel):
    """DeleteAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFileSystemRequest(AbstractModel):
    """DeleteFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileSystemResponse(AbstractModel):
    """DeleteFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLifeCycleRulesRequest(AbstractModel):
    """DeleteLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param LifeCycleRuleIds: 多个生命周期规则ID，上限为10
        :type LifeCycleRuleIds: list of int non-negative
        """
        self.LifeCycleRuleIds = None


    def _deserialize(self, params):
        self.LifeCycleRuleIds = params.get("LifeCycleRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLifeCycleRulesResponse(AbstractModel):
    """DeleteLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMountPointRequest(AbstractModel):
    """DeleteMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param MountPointId: 挂载点ID
        :type MountPointId: str
        """
        self.MountPointId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountPointResponse(AbstractModel):
    """DeleteMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessGroupsRequest(AbstractModel):
    """DescribeAccessGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件，Name可选“AccessGroupId“和“AccessGroupName”，Values上限为10
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为所有
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
        


class DescribeAccessGroupsResponse(AbstractModel):
    """DescribeAccessGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccessGroups: 权限组列表
        :type AccessGroups: list of AccessGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessGroups") is not None:
            self.AccessGroups = []
            for item in params.get("AccessGroups"):
                obj = AccessGroup()
                obj._deserialize(item)
                self.AccessGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessRulesRequest(AbstractModel):
    """DescribeAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为所有
        :type Limit: int
        """
        self.AccessGroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessRulesResponse(AbstractModel):
    """DescribeAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccessRules: 权限规则列表
        :type AccessRules: list of AccessRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessRules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFileSystemRequest(AbstractModel):
    """DescribeFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileSystemResponse(AbstractModel):
    """DescribeFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystem: 文件系统
        :type FileSystem: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        :param FileSystemCapacityUsed: 文件系统已使用容量（已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemCapacityUsed: int
        :param CapacityUsed: 已使用容量（byte），包括标准和归档存储
注意：此字段可能返回 null，表示取不到有效值。
        :type CapacityUsed: int
        :param ArchiveCapacityUsed: 已使用归档存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchiveCapacityUsed: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileSystem = None
        self.FileSystemCapacityUsed = None
        self.CapacityUsed = None
        self.ArchiveCapacityUsed = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self.FileSystem = FileSystem()
            self.FileSystem._deserialize(params.get("FileSystem"))
        self.FileSystemCapacityUsed = params.get("FileSystemCapacityUsed")
        self.CapacityUsed = params.get("CapacityUsed")
        self.ArchiveCapacityUsed = params.get("ArchiveCapacityUsed")
        self.RequestId = params.get("RequestId")


class DescribeFileSystemsRequest(AbstractModel):
    """DescribeFileSystems请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为所有
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileSystemsResponse(AbstractModel):
    """DescribeFileSystems返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystems: 文件系统列表
        :type FileSystems: list of FileSystem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileSystems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystem()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLifeCycleRulesRequest(AbstractModel):
    """DescribeLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLifeCycleRulesResponse(AbstractModel):
    """DescribeLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param LifeCycleRules: 生命周期规则列表
        :type LifeCycleRules: list of LifeCycleRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LifeCycleRules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self.LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self.LifeCycleRules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMountPointRequest(AbstractModel):
    """DescribeMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param MountPointId: 挂载点ID
        :type MountPointId: str
        """
        self.MountPointId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointResponse(AbstractModel):
    """DescribeMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param MountPoint: 挂载点
        :type MountPoint: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MountPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self.MountPoint = MountPoint()
            self.MountPoint._deserialize(params.get("MountPoint"))
        self.RequestId = params.get("RequestId")


class DescribeMountPointsRequest(AbstractModel):
    """DescribeMountPoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
注意：若根据AccessGroupId查看挂载点列表，则无需设置FileSystemId
        :type FileSystemId: str
        :param AccessGroupId: 权限组ID
注意：若根据FileSystemId查看挂载点列表，则无需设置AccessGroupId
        :type AccessGroupId: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为所有
        :type Limit: int
        """
        self.FileSystemId = None
        self.AccessGroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.AccessGroupId = params.get("AccessGroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointsResponse(AbstractModel):
    """DescribeMountPoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param MountPoints: 挂载点列表
        :type MountPoints: list of MountPoint
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MountPoints = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoints") is not None:
            self.MountPoints = []
            for item in params.get("MountPoints"):
                obj = MountPoint()
                obj._deserialize(item)
                self.MountPoints.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tags: 资源标签列表
        :type Tags: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRestoreTasksRequest(AbstractModel):
    """DescribeRestoreTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTasksResponse(AbstractModel):
    """DescribeRestoreTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RestoreTasks: 回热任务列表
        :type RestoreTasks: list of RestoreTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RestoreTasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RestoreTasks") is not None:
            self.RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self.RestoreTasks.append(obj)
        self.RequestId = params.get("RequestId")


class FileSystem(AbstractModel):
    """文件系统

    """

    def __init__(self):
        r"""
        :param AppId: appid
        :type AppId: int
        :param FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param Description: 文件系统描述
        :type Description: str
        :param Region: 地域
        :type Region: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param BlockSize: 文件系统块大小（byte）
        :type BlockSize: int
        :param CapacityQuota: 文件系统容量（byte）
        :type CapacityQuota: int
        :param Status: 文件系统状态（1：创建中；2：创建成功；3：创建失败）
        :type Status: int
        """
        self.AppId = None
        self.FileSystemName = None
        self.Description = None
        self.Region = None
        self.FileSystemId = None
        self.CreateTime = None
        self.BlockSize = None
        self.CapacityQuota = None
        self.Status = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.FileSystemName = params.get("FileSystemName")
        self.Description = params.get("Description")
        self.Region = params.get("Region")
        self.FileSystemId = params.get("FileSystemId")
        self.CreateTime = params.get("CreateTime")
        self.BlockSize = params.get("BlockSize")
        self.CapacityQuota = params.get("CapacityQuota")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段
        :type Name: str
        :param Values: 过滤值
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
        


class LifeCycleRule(AbstractModel):
    """生命周期规则

    """

    def __init__(self):
        r"""
        :param LifeCycleRuleId: 生命周期规则ID
        :type LifeCycleRuleId: int
        :param LifeCycleRuleName: 生命周期规则名称
        :type LifeCycleRuleName: str
        :param Path: 生命周期规则路径（目录或文件）
        :type Path: str
        :param Transitions: 生命周期规则转换列表
        :type Transitions: list of Transition
        :param Status: 生命周期规则状态（1：打开；2：关闭）
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.LifeCycleRuleId = None
        self.LifeCycleRuleName = None
        self.Path = None
        self.Transitions = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.LifeCycleRuleId = params.get("LifeCycleRuleId")
        self.LifeCycleRuleName = params.get("LifeCycleRuleName")
        self.Path = params.get("Path")
        if params.get("Transitions") is not None:
            self.Transitions = []
            for item in params.get("Transitions"):
                obj = Transition()
                obj._deserialize(item)
                self.Transitions.append(obj)
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupRequest(AbstractModel):
    """ModifyAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param Description: 权限组描述
        :type Description: str
        """
        self.AccessGroupId = None
        self.AccessGroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupResponse(AbstractModel):
    """ModifyAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccessRulesRequest(AbstractModel):
    """ModifyAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessRules: 多个权限规则，上限为10
        :type AccessRules: list of AccessRule
        """
        self.AccessRules = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessRulesResponse(AbstractModel):
    """ModifyAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFileSystemRequest(AbstractModel):
    """ModifyFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param Description: 文件系统描述
        :type Description: str
        :param CapacityQuota: 文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍
注意：修改的文件系统容量不能小于当前使用量
        :type CapacityQuota: int
        """
        self.FileSystemId = None
        self.FileSystemName = None
        self.Description = None
        self.CapacityQuota = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.FileSystemName = params.get("FileSystemName")
        self.Description = params.get("Description")
        self.CapacityQuota = params.get("CapacityQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemResponse(AbstractModel):
    """ModifyFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLifeCycleRulesRequest(AbstractModel):
    """ModifyLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param LifeCycleRules: 多个生命周期规则，上限为10
        :type LifeCycleRules: list of LifeCycleRule
        """
        self.LifeCycleRules = None


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self.LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self.LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLifeCycleRulesResponse(AbstractModel):
    """ModifyLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMountPointRequest(AbstractModel):
    """ModifyMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param MountPointId: 挂载点ID
        :type MountPointId: str
        :param MountPointName: 挂载点名称
        :type MountPointName: str
        :param MountPointStatus: 挂载点状态
        :type MountPointStatus: int
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self.MountPointId = None
        self.MountPointName = None
        self.MountPointStatus = None
        self.AccessGroupId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.MountPointName = params.get("MountPointName")
        self.MountPointStatus = params.get("MountPointStatus")
        self.AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMountPointResponse(AbstractModel):
    """ModifyMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param Tags: 多个资源标签，可以为空数组
        :type Tags: list of Tag
        """
        self.FileSystemId = None
        self.Tags = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
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
        


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MountPoint(AbstractModel):
    """挂载点

    """

    def __init__(self):
        r"""
        :param MountPointId: 挂载点ID
        :type MountPointId: str
        :param MountPointName: 挂载点名称
        :type MountPointName: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param VpcId: VPC网络ID
        :type VpcId: str
        :param Status: 挂载点状态（1：打开；2：关闭）
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param VpcType: VPC网络类型
        :type VpcType: int
        """
        self.MountPointId = None
        self.MountPointName = None
        self.FileSystemId = None
        self.AccessGroupId = None
        self.VpcId = None
        self.Status = None
        self.CreateTime = None
        self.VpcType = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.MountPointName = params.get("MountPointName")
        self.FileSystemId = params.get("FileSystemId")
        self.AccessGroupId = params.get("AccessGroupId")
        self.VpcId = params.get("VpcId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.VpcType = params.get("VpcType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreTask(AbstractModel):
    """回热任务

    """

    def __init__(self):
        r"""
        :param RestoreTaskId: 回热任务ID
        :type RestoreTaskId: int
        :param FilePath: 回热任务文件路径
        :type FilePath: str
        :param Type: 回热任务类型（1：标准；2：极速；3：批量）
        :type Type: int
        :param Days: 指定恢复出的临时副本的有效时长（单位天）
        :type Days: int
        :param Status: 回热任务状态（1：绑定文件中；2：绑定文件完成；3：文件回热中；4：文件回热完成）
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.RestoreTaskId = None
        self.FilePath = None
        self.Type = None
        self.Days = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.RestoreTaskId = params.get("RestoreTaskId")
        self.FilePath = params.get("FilePath")
        self.Type = params.get("Type")
        self.Days = params.get("Days")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """资源标签。

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
        


class Transition(AbstractModel):
    """生命周期规则转换属性

    """

    def __init__(self):
        r"""
        :param Days: 触发时间（单位天）
        :type Days: int
        :param Type: 转换类型（1：归档；2：删除）
        :type Type: int
        """
        self.Days = None
        self.Type = None


    def _deserialize(self, params):
        self.Days = params.get("Days")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        