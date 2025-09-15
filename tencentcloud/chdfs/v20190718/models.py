# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""权限组

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param _AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param _Description: 权限组描述
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._AccessGroupId = None
        self._AccessGroupName = None
        self._Description = None
        self._CreateTime = None

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def AccessGroupName(self):
        r"""权限组名称
        :rtype: str
        """
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def Description(self):
        r"""权限组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        self._AccessGroupName = params.get("AccessGroupName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRule(AbstractModel):
    r"""权限规则

    """

    def __init__(self):
        r"""
        :param _AccessRuleId: 权限规则ID
        :type AccessRuleId: int
        :param _Address: 权限规则地址（网段或IP）
        :type Address: str
        :param _AccessMode: 权限规则访问模式（1：只读；2：读写）
        :type AccessMode: int
        :param _Priority: 优先级（取值范围1~100，值越小优先级越高）
        :type Priority: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._AccessRuleId = None
        self._Address = None
        self._AccessMode = None
        self._Priority = None
        self._CreateTime = None

    @property
    def AccessRuleId(self):
        r"""权限规则ID
        :rtype: int
        """
        return self._AccessRuleId

    @AccessRuleId.setter
    def AccessRuleId(self, AccessRuleId):
        self._AccessRuleId = AccessRuleId

    @property
    def Address(self):
        r"""权限规则地址（网段或IP）
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AccessMode(self):
        r"""权限规则访问模式（1：只读；2：读写）
        :rtype: int
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def Priority(self):
        r"""优先级（取值范围1~100，值越小优先级越高）
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._AccessRuleId = params.get("AccessRuleId")
        self._Address = params.get("Address")
        self._AccessMode = params.get("AccessMode")
        self._Priority = params.get("Priority")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessGroupRequest(AbstractModel):
    r"""CreateAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param _Description: 权限组描述
        :type Description: str
        """
        self._AccessGroupName = None
        self._Description = None

    @property
    def AccessGroupName(self):
        r"""权限组名称
        :rtype: str
        """
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def Description(self):
        r"""权限组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccessGroupName = params.get("AccessGroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessGroupResponse(AbstractModel):
    r"""CreateAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroup: 权限组
        :type AccessGroup: :class:`tencentcloud.chdfs.v20190718.models.AccessGroup`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessGroup = None
        self._RequestId = None

    @property
    def AccessGroup(self):
        r"""权限组
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.AccessGroup`
        """
        return self._AccessGroup

    @AccessGroup.setter
    def AccessGroup(self, AccessGroup):
        self._AccessGroup = AccessGroup

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self._AccessGroup = AccessGroup()
            self._AccessGroup._deserialize(params.get("AccessGroup"))
        self._RequestId = params.get("RequestId")


class CreateAccessRulesRequest(AbstractModel):
    r"""CreateAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRules: 多个权限规则，上限为10
        :type AccessRules: list of AccessRule
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self._AccessRules = None
        self._AccessGroupId = None

    @property
    def AccessRules(self):
        r"""多个权限规则，上限为10
        :rtype: list of AccessRule
        """
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self._AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self._AccessRules.append(obj)
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessRulesResponse(AbstractModel):
    r"""CreateAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateFileSystemRequest(AbstractModel):
    r"""CreateFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param _CapacityQuota: 文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍
        :type CapacityQuota: int
        :param _Description: 文件系统描述
        :type Description: str
        """
        self._FileSystemName = None
        self._CapacityQuota = None
        self._Description = None

    @property
    def FileSystemName(self):
        r"""文件系统名称
        :rtype: str
        """
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def CapacityQuota(self):
        r"""文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍
        :rtype: int
        """
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def Description(self):
        r"""文件系统描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._FileSystemName = params.get("FileSystemName")
        self._CapacityQuota = params.get("CapacityQuota")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileSystemResponse(AbstractModel):
    r"""CreateFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystem: 文件系统
        :type FileSystem: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystem = None
        self._RequestId = None

    @property
    def FileSystem(self):
        r"""文件系统
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        """
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self._FileSystem = FileSystem()
            self._FileSystem._deserialize(params.get("FileSystem"))
        self._RequestId = params.get("RequestId")


class CreateLifeCycleRulesRequest(AbstractModel):
    r"""CreateLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _LifeCycleRules: 多个生命周期规则，上限为10
        :type LifeCycleRules: list of LifeCycleRule
        """
        self._FileSystemId = None
        self._LifeCycleRules = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleRules(self):
        r"""多个生命周期规则，上限为10
        :rtype: list of LifeCycleRule
        """
        return self._LifeCycleRules

    @LifeCycleRules.setter
    def LifeCycleRules(self, LifeCycleRules):
        self._LifeCycleRules = LifeCycleRules


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("LifeCycleRules") is not None:
            self._LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self._LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifeCycleRulesResponse(AbstractModel):
    r"""CreateLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateMountPointRequest(AbstractModel):
    r"""CreateMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointName: 挂载点名称
        :type MountPointName: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param _VpcId: VPC网络ID
        :type VpcId: str
        :param _MountPointStatus: 挂载点状态（1：打开；2：关闭）
        :type MountPointStatus: int
        :param _VpcType: VPC网络类型（1：CVM；2：黑石1.0；3：黑石2.0）
        :type VpcType: int
        """
        self._MountPointName = None
        self._FileSystemId = None
        self._AccessGroupId = None
        self._VpcId = None
        self._MountPointStatus = None
        self._VpcType = None

    @property
    def MountPointName(self):
        r"""挂载点名称
        :rtype: str
        """
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def VpcId(self):
        r"""VPC网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def MountPointStatus(self):
        r"""挂载点状态（1：打开；2：关闭）
        :rtype: int
        """
        return self._MountPointStatus

    @MountPointStatus.setter
    def MountPointStatus(self, MountPointStatus):
        self._MountPointStatus = MountPointStatus

    @property
    def VpcType(self):
        r"""VPC网络类型（1：CVM；2：黑石1.0；3：黑石2.0）
        :rtype: int
        """
        return self._VpcType

    @VpcType.setter
    def VpcType(self, VpcType):
        self._VpcType = VpcType


    def _deserialize(self, params):
        self._MountPointName = params.get("MountPointName")
        self._FileSystemId = params.get("FileSystemId")
        self._AccessGroupId = params.get("AccessGroupId")
        self._VpcId = params.get("VpcId")
        self._MountPointStatus = params.get("MountPointStatus")
        self._VpcType = params.get("VpcType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMountPointResponse(AbstractModel):
    r"""CreateMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoint: 挂载点
        :type MountPoint: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountPoint = None
        self._RequestId = None

    @property
    def MountPoint(self):
        r"""挂载点
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        """
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self._MountPoint = MountPoint()
            self._MountPoint._deserialize(params.get("MountPoint"))
        self._RequestId = params.get("RequestId")


class CreateRestoreTasksRequest(AbstractModel):
    r"""CreateRestoreTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _RestoreTasks: 多个回热任务，上限为10
        :type RestoreTasks: list of RestoreTask
        """
        self._FileSystemId = None
        self._RestoreTasks = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def RestoreTasks(self):
        r"""多个回热任务，上限为10
        :rtype: list of RestoreTask
        """
        return self._RestoreTasks

    @RestoreTasks.setter
    def RestoreTasks(self, RestoreTasks):
        self._RestoreTasks = RestoreTasks


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("RestoreTasks") is not None:
            self._RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self._RestoreTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRestoreTasksResponse(AbstractModel):
    r"""CreateRestoreTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAccessGroupRequest(AbstractModel):
    r"""DeleteAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self._AccessGroupId = None

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessGroupResponse(AbstractModel):
    r"""DeleteAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAccessRulesRequest(AbstractModel):
    r"""DeleteAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRuleIds: 多个权限规则ID，上限为10
        :type AccessRuleIds: list of int non-negative
        """
        self._AccessRuleIds = None

    @property
    def AccessRuleIds(self):
        r"""多个权限规则ID，上限为10
        :rtype: list of int non-negative
        """
        return self._AccessRuleIds

    @AccessRuleIds.setter
    def AccessRuleIds(self, AccessRuleIds):
        self._AccessRuleIds = AccessRuleIds


    def _deserialize(self, params):
        self._AccessRuleIds = params.get("AccessRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessRulesResponse(AbstractModel):
    r"""DeleteAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteFileSystemRequest(AbstractModel):
    r"""DeleteFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileSystemResponse(AbstractModel):
    r"""DeleteFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLifeCycleRulesRequest(AbstractModel):
    r"""DeleteLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifeCycleRuleIds: 多个生命周期规则ID，上限为10
        :type LifeCycleRuleIds: list of int non-negative
        """
        self._LifeCycleRuleIds = None

    @property
    def LifeCycleRuleIds(self):
        r"""多个生命周期规则ID，上限为10
        :rtype: list of int non-negative
        """
        return self._LifeCycleRuleIds

    @LifeCycleRuleIds.setter
    def LifeCycleRuleIds(self, LifeCycleRuleIds):
        self._LifeCycleRuleIds = LifeCycleRuleIds


    def _deserialize(self, params):
        self._LifeCycleRuleIds = params.get("LifeCycleRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLifeCycleRulesResponse(AbstractModel):
    r"""DeleteLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteMountPointRequest(AbstractModel):
    r"""DeleteMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        """
        self._MountPointId = None

    @property
    def MountPointId(self):
        r"""挂载点ID
        :rtype: str
        """
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountPointResponse(AbstractModel):
    r"""DeleteMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccessGroupsRequest(AbstractModel):
    r"""DescribeAccessGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，Name可选“AccessGroupId“和“AccessGroupName”，Values上限为10
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为所有
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        r"""过滤条件，Name可选“AccessGroupId“和“AccessGroupName”，Values上限为10
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为所有
        :rtype: int
        """
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
        


class DescribeAccessGroupsResponse(AbstractModel):
    r"""DescribeAccessGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroups: 权限组列表
        :type AccessGroups: list of AccessGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessGroups = None
        self._RequestId = None

    @property
    def AccessGroups(self):
        r"""权限组列表
        :rtype: list of AccessGroup
        """
        return self._AccessGroups

    @AccessGroups.setter
    def AccessGroups(self, AccessGroups):
        self._AccessGroups = AccessGroups

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessGroups") is not None:
            self._AccessGroups = []
            for item in params.get("AccessGroups"):
                obj = AccessGroup()
                obj._deserialize(item)
                self._AccessGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccessRulesRequest(AbstractModel):
    r"""DescribeAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为所有
        :type Limit: int
        """
        self._AccessGroupId = None
        self._Offset = None
        self._Limit = None

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为所有
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessRulesResponse(AbstractModel):
    r"""DescribeAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRules: 权限规则列表
        :type AccessRules: list of AccessRule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessRules = None
        self._RequestId = None

    @property
    def AccessRules(self):
        r"""权限规则列表
        :rtype: list of AccessRule
        """
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self._AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self._AccessRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileSystemRequest(AbstractModel):
    r"""DescribeFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileSystemResponse(AbstractModel):
    r"""DescribeFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystem: 文件系统
        :type FileSystem: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        :param _FileSystemCapacityUsed: 文件系统已使用容量（已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystemCapacityUsed: int
        :param _CapacityUsed: 已使用容量（byte），包括标准和归档存储
注意：此字段可能返回 null，表示取不到有效值。
        :type CapacityUsed: int
        :param _ArchiveCapacityUsed: 已使用归档存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchiveCapacityUsed: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystem = None
        self._FileSystemCapacityUsed = None
        self._CapacityUsed = None
        self._ArchiveCapacityUsed = None
        self._RequestId = None

    @property
    def FileSystem(self):
        r"""文件系统
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        """
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def FileSystemCapacityUsed(self):
        r"""文件系统已使用容量（已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSystemCapacityUsed

    @FileSystemCapacityUsed.setter
    def FileSystemCapacityUsed(self, FileSystemCapacityUsed):
        self._FileSystemCapacityUsed = FileSystemCapacityUsed

    @property
    def CapacityUsed(self):
        r"""已使用容量（byte），包括标准和归档存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CapacityUsed

    @CapacityUsed.setter
    def CapacityUsed(self, CapacityUsed):
        self._CapacityUsed = CapacityUsed

    @property
    def ArchiveCapacityUsed(self):
        r"""已使用归档存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ArchiveCapacityUsed

    @ArchiveCapacityUsed.setter
    def ArchiveCapacityUsed(self, ArchiveCapacityUsed):
        self._ArchiveCapacityUsed = ArchiveCapacityUsed

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self._FileSystem = FileSystem()
            self._FileSystem._deserialize(params.get("FileSystem"))
        self._FileSystemCapacityUsed = params.get("FileSystemCapacityUsed")
        self._CapacityUsed = params.get("CapacityUsed")
        self._ArchiveCapacityUsed = params.get("ArchiveCapacityUsed")
        self._RequestId = params.get("RequestId")


class DescribeFileSystemsRequest(AbstractModel):
    r"""DescribeFileSystems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为所有
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为所有
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileSystemsResponse(AbstractModel):
    r"""DescribeFileSystems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystems: 文件系统列表
        :type FileSystems: list of FileSystem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystems = None
        self._RequestId = None

    @property
    def FileSystems(self):
        r"""文件系统列表
        :rtype: list of FileSystem
        """
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self._FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystem()
                obj._deserialize(item)
                self._FileSystems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLifeCycleRulesRequest(AbstractModel):
    r"""DescribeLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLifeCycleRulesResponse(AbstractModel):
    r"""DescribeLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LifeCycleRules: 生命周期规则列表
        :type LifeCycleRules: list of LifeCycleRule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LifeCycleRules = None
        self._RequestId = None

    @property
    def LifeCycleRules(self):
        r"""生命周期规则列表
        :rtype: list of LifeCycleRule
        """
        return self._LifeCycleRules

    @LifeCycleRules.setter
    def LifeCycleRules(self, LifeCycleRules):
        self._LifeCycleRules = LifeCycleRules

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self._LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self._LifeCycleRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMountPointRequest(AbstractModel):
    r"""DescribeMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        """
        self._MountPointId = None

    @property
    def MountPointId(self):
        r"""挂载点ID
        :rtype: str
        """
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointResponse(AbstractModel):
    r"""DescribeMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoint: 挂载点
        :type MountPoint: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountPoint = None
        self._RequestId = None

    @property
    def MountPoint(self):
        r"""挂载点
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        """
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self._MountPoint = MountPoint()
            self._MountPoint._deserialize(params.get("MountPoint"))
        self._RequestId = params.get("RequestId")


class DescribeMountPointsRequest(AbstractModel):
    r"""DescribeMountPoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
注意：若根据AccessGroupId查看挂载点列表，则无需设置FileSystemId
        :type FileSystemId: str
        :param _AccessGroupId: 权限组ID
注意：若根据FileSystemId查看挂载点列表，则无需设置AccessGroupId
        :type AccessGroupId: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为所有
        :type Limit: int
        """
        self._FileSystemId = None
        self._AccessGroupId = None
        self._Offset = None
        self._Limit = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
注意：若根据AccessGroupId查看挂载点列表，则无需设置FileSystemId
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def AccessGroupId(self):
        r"""权限组ID
注意：若根据FileSystemId查看挂载点列表，则无需设置AccessGroupId
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为所有
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._AccessGroupId = params.get("AccessGroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointsResponse(AbstractModel):
    r"""DescribeMountPoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoints: 挂载点列表
        :type MountPoints: list of MountPoint
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountPoints = None
        self._RequestId = None

    @property
    def MountPoints(self):
        r"""挂载点列表
        :rtype: list of MountPoint
        """
        return self._MountPoints

    @MountPoints.setter
    def MountPoints(self, MountPoints):
        self._MountPoints = MountPoints

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountPoints") is not None:
            self._MountPoints = []
            for item in params.get("MountPoints"):
                obj = MountPoint()
                obj._deserialize(item)
                self._MountPoints.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    r"""DescribeResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    r"""DescribeResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tags: 资源标签列表
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tags = None
        self._RequestId = None

    @property
    def Tags(self):
        r"""资源标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRestoreTasksRequest(AbstractModel):
    r"""DescribeRestoreTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTasksResponse(AbstractModel):
    r"""DescribeRestoreTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RestoreTasks: 回热任务列表
        :type RestoreTasks: list of RestoreTask
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RestoreTasks = None
        self._RequestId = None

    @property
    def RestoreTasks(self):
        r"""回热任务列表
        :rtype: list of RestoreTask
        """
        return self._RestoreTasks

    @RestoreTasks.setter
    def RestoreTasks(self, RestoreTasks):
        self._RestoreTasks = RestoreTasks

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RestoreTasks") is not None:
            self._RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self._RestoreTasks.append(obj)
        self._RequestId = params.get("RequestId")


class FileSystem(AbstractModel):
    r"""文件系统

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: int
        :param _FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param _Description: 文件系统描述
        :type Description: str
        :param _Region: 地域
        :type Region: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _BlockSize: 文件系统块大小（byte）
        :type BlockSize: int
        :param _CapacityQuota: 文件系统容量（byte）
        :type CapacityQuota: int
        :param _Status: 文件系统状态（1：创建中；2：创建成功；3：创建失败）
        :type Status: int
        """
        self._AppId = None
        self._FileSystemName = None
        self._Description = None
        self._Region = None
        self._FileSystemId = None
        self._CreateTime = None
        self._BlockSize = None
        self._CapacityQuota = None
        self._Status = None

    @property
    def AppId(self):
        r"""appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FileSystemName(self):
        r"""文件系统名称
        :rtype: str
        """
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def Description(self):
        r"""文件系统描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BlockSize(self):
        r"""文件系统块大小（byte）
        :rtype: int
        """
        return self._BlockSize

    @BlockSize.setter
    def BlockSize(self, BlockSize):
        self._BlockSize = BlockSize

    @property
    def CapacityQuota(self):
        r"""文件系统容量（byte）
        :rtype: int
        """
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def Status(self):
        r"""文件系统状态（1：创建中；2：创建成功；3：创建失败）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._FileSystemName = params.get("FileSystemName")
        self._Description = params.get("Description")
        self._Region = params.get("Region")
        self._FileSystemId = params.get("FileSystemId")
        self._CreateTime = params.get("CreateTime")
        self._BlockSize = params.get("BlockSize")
        self._CapacityQuota = params.get("CapacityQuota")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段
        :type Name: str
        :param _Values: 过滤值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤字段
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤值
        :rtype: list of str
        """
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
        


class LifeCycleRule(AbstractModel):
    r"""生命周期规则

    """

    def __init__(self):
        r"""
        :param _LifeCycleRuleId: 生命周期规则ID
        :type LifeCycleRuleId: int
        :param _LifeCycleRuleName: 生命周期规则名称
        :type LifeCycleRuleName: str
        :param _Path: 生命周期规则路径（目录或文件）
        :type Path: str
        :param _Transitions: 生命周期规则转换列表
        :type Transitions: list of Transition
        :param _Status: 生命周期规则状态（1：打开；2：关闭）
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._LifeCycleRuleId = None
        self._LifeCycleRuleName = None
        self._Path = None
        self._Transitions = None
        self._Status = None
        self._CreateTime = None

    @property
    def LifeCycleRuleId(self):
        r"""生命周期规则ID
        :rtype: int
        """
        return self._LifeCycleRuleId

    @LifeCycleRuleId.setter
    def LifeCycleRuleId(self, LifeCycleRuleId):
        self._LifeCycleRuleId = LifeCycleRuleId

    @property
    def LifeCycleRuleName(self):
        r"""生命周期规则名称
        :rtype: str
        """
        return self._LifeCycleRuleName

    @LifeCycleRuleName.setter
    def LifeCycleRuleName(self, LifeCycleRuleName):
        self._LifeCycleRuleName = LifeCycleRuleName

    @property
    def Path(self):
        r"""生命周期规则路径（目录或文件）
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Transitions(self):
        r"""生命周期规则转换列表
        :rtype: list of Transition
        """
        return self._Transitions

    @Transitions.setter
    def Transitions(self, Transitions):
        self._Transitions = Transitions

    @property
    def Status(self):
        r"""生命周期规则状态（1：打开；2：关闭）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._LifeCycleRuleId = params.get("LifeCycleRuleId")
        self._LifeCycleRuleName = params.get("LifeCycleRuleName")
        self._Path = params.get("Path")
        if params.get("Transitions") is not None:
            self._Transitions = []
            for item in params.get("Transitions"):
                obj = Transition()
                obj._deserialize(item)
                self._Transitions.append(obj)
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupRequest(AbstractModel):
    r"""ModifyAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param _AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param _Description: 权限组描述
        :type Description: str
        """
        self._AccessGroupId = None
        self._AccessGroupName = None
        self._Description = None

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def AccessGroupName(self):
        r"""权限组名称
        :rtype: str
        """
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def Description(self):
        r"""权限组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        self._AccessGroupName = params.get("AccessGroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupResponse(AbstractModel):
    r"""ModifyAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAccessRulesRequest(AbstractModel):
    r"""ModifyAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRules: 多个权限规则，上限为10
        :type AccessRules: list of AccessRule
        """
        self._AccessRules = None

    @property
    def AccessRules(self):
        r"""多个权限规则，上限为10
        :rtype: list of AccessRule
        """
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self._AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self._AccessRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessRulesResponse(AbstractModel):
    r"""ModifyAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyFileSystemRequest(AbstractModel):
    r"""ModifyFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param _Description: 文件系统描述
        :type Description: str
        :param _CapacityQuota: 文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍
注意：修改的文件系统容量不能小于当前使用量
        :type CapacityQuota: int
        """
        self._FileSystemId = None
        self._FileSystemName = None
        self._Description = None
        self._CapacityQuota = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FileSystemName(self):
        r"""文件系统名称
        :rtype: str
        """
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def Description(self):
        r"""文件系统描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CapacityQuota(self):
        r"""文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍
注意：修改的文件系统容量不能小于当前使用量
        :rtype: int
        """
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FileSystemName = params.get("FileSystemName")
        self._Description = params.get("Description")
        self._CapacityQuota = params.get("CapacityQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemResponse(AbstractModel):
    r"""ModifyFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLifeCycleRulesRequest(AbstractModel):
    r"""ModifyLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifeCycleRules: 多个生命周期规则，上限为10
        :type LifeCycleRules: list of LifeCycleRule
        """
        self._LifeCycleRules = None

    @property
    def LifeCycleRules(self):
        r"""多个生命周期规则，上限为10
        :rtype: list of LifeCycleRule
        """
        return self._LifeCycleRules

    @LifeCycleRules.setter
    def LifeCycleRules(self, LifeCycleRules):
        self._LifeCycleRules = LifeCycleRules


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self._LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self._LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLifeCycleRulesResponse(AbstractModel):
    r"""ModifyLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMountPointRequest(AbstractModel):
    r"""ModifyMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        :param _MountPointName: 挂载点名称
        :type MountPointName: str
        :param _MountPointStatus: 挂载点状态
        :type MountPointStatus: int
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self._MountPointId = None
        self._MountPointName = None
        self._MountPointStatus = None
        self._AccessGroupId = None

    @property
    def MountPointId(self):
        r"""挂载点ID
        :rtype: str
        """
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def MountPointName(self):
        r"""挂载点名称
        :rtype: str
        """
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def MountPointStatus(self):
        r"""挂载点状态
        :rtype: int
        """
        return self._MountPointStatus

    @MountPointStatus.setter
    def MountPointStatus(self, MountPointStatus):
        self._MountPointStatus = MountPointStatus

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._MountPointName = params.get("MountPointName")
        self._MountPointStatus = params.get("MountPointStatus")
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMountPointResponse(AbstractModel):
    r"""ModifyMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    r"""ModifyResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _Tags: 多个资源标签，可以为空数组
        :type Tags: list of Tag
        """
        self._FileSystemId = None
        self._Tags = None

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Tags(self):
        r"""多个资源标签，可以为空数组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
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
        


class ModifyResourceTagsResponse(AbstractModel):
    r"""ModifyResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MountPoint(AbstractModel):
    r"""挂载点

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        :param _MountPointName: 挂载点名称
        :type MountPointName: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param _VpcId: VPC网络ID
        :type VpcId: str
        :param _Status: 挂载点状态（1：打开；2：关闭）
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _VpcType: VPC网络类型
        :type VpcType: int
        """
        self._MountPointId = None
        self._MountPointName = None
        self._FileSystemId = None
        self._AccessGroupId = None
        self._VpcId = None
        self._Status = None
        self._CreateTime = None
        self._VpcType = None

    @property
    def MountPointId(self):
        r"""挂载点ID
        :rtype: str
        """
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def MountPointName(self):
        r"""挂载点名称
        :rtype: str
        """
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def FileSystemId(self):
        r"""文件系统ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def AccessGroupId(self):
        r"""权限组ID
        :rtype: str
        """
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def VpcId(self):
        r"""VPC网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Status(self):
        r"""挂载点状态（1：打开；2：关闭）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpcType(self):
        r"""VPC网络类型
        :rtype: int
        """
        return self._VpcType

    @VpcType.setter
    def VpcType(self, VpcType):
        self._VpcType = VpcType


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._MountPointName = params.get("MountPointName")
        self._FileSystemId = params.get("FileSystemId")
        self._AccessGroupId = params.get("AccessGroupId")
        self._VpcId = params.get("VpcId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._VpcType = params.get("VpcType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreTask(AbstractModel):
    r"""回热任务

    """

    def __init__(self):
        r"""
        :param _RestoreTaskId: 回热任务ID
        :type RestoreTaskId: int
        :param _FilePath: 回热任务文件路径
        :type FilePath: str
        :param _Type: 回热任务类型（1：标准；2：极速；3：批量）
        :type Type: int
        :param _Days: 指定恢复出的临时副本的有效时长（单位天）
        :type Days: int
        :param _Status: 回热任务状态（1：绑定文件中；2：绑定文件完成；3：文件回热中；4：文件回热完成）
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._RestoreTaskId = None
        self._FilePath = None
        self._Type = None
        self._Days = None
        self._Status = None
        self._CreateTime = None

    @property
    def RestoreTaskId(self):
        r"""回热任务ID
        :rtype: int
        """
        return self._RestoreTaskId

    @RestoreTaskId.setter
    def RestoreTaskId(self, RestoreTaskId):
        self._RestoreTaskId = RestoreTaskId

    @property
    def FilePath(self):
        r"""回热任务文件路径
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Type(self):
        r"""回热任务类型（1：标准；2：极速；3：批量）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Days(self):
        r"""指定恢复出的临时副本的有效时长（单位天）
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Status(self):
        r"""回热任务状态（1：绑定文件中；2：绑定文件完成；3：文件回热中；4：文件回热完成）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._RestoreTaskId = params.get("RestoreTaskId")
        self._FilePath = params.get("FilePath")
        self._Type = params.get("Type")
        self._Days = params.get("Days")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""资源标签。

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
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
        :rtype: str
        """
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
        


class Transition(AbstractModel):
    r"""生命周期规则转换属性

    """

    def __init__(self):
        r"""
        :param _Days: 触发时间（单位天）
        :type Days: int
        :param _Type: 转换类型（1：归档；2：删除）
        :type Type: int
        """
        self._Days = None
        self._Type = None

    @property
    def Days(self):
        r"""触发时间（单位天）
        :rtype: int
        """
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Type(self):
        r"""转换类型（1：归档；2：删除）
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Days = params.get("Days")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        