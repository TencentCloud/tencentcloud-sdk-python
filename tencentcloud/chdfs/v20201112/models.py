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
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param _AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param _Description: 权限组描述
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _VpcType: VPC网络类型（1：CVM；2：黑石1.0）
        :type VpcType: int
        :param _VpcId: VPC网络ID
        :type VpcId: str
        """
        self._AccessGroupId = None
        self._AccessGroupName = None
        self._Description = None
        self._CreateTime = None
        self._VpcType = None
        self._VpcId = None

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def AccessGroupName(self):
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpcType(self):
        return self._VpcType

    @VpcType.setter
    def VpcType(self, VpcType):
        self._VpcType = VpcType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        self._AccessGroupName = params.get("AccessGroupName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._VpcType = params.get("VpcType")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRule(AbstractModel):
    """权限规则

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
        return self._AccessRuleId

    @AccessRuleId.setter
    def AccessRuleId(self, AccessRuleId):
        self._AccessRuleId = AccessRuleId

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def CreateTime(self):
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
        


class AssociateAccessGroupsRequest(AbstractModel):
    """AssociateAccessGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        :param _AccessGroupIds: 权限组ID列表
        :type AccessGroupIds: list of str
        """
        self._MountPointId = None
        self._AccessGroupIds = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def AccessGroupIds(self):
        return self._AccessGroupIds

    @AccessGroupIds.setter
    def AccessGroupIds(self, AccessGroupIds):
        self._AccessGroupIds = AccessGroupIds


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAccessGroupsResponse(AbstractModel):
    """AssociateAccessGroups返回参数结构体

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


class CreateAccessGroupRequest(AbstractModel):
    """CreateAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupName: 权限组名称
        :type AccessGroupName: str
        :param _VpcType: VPC网络类型（1：CVM；2：黑石1.0）
        :type VpcType: int
        :param _VpcId: VPC网络ID
        :type VpcId: str
        :param _Description: 权限组描述，默认为空字符串
        :type Description: str
        """
        self._AccessGroupName = None
        self._VpcType = None
        self._VpcId = None
        self._Description = None

    @property
    def AccessGroupName(self):
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def VpcType(self):
        return self._VpcType

    @VpcType.setter
    def VpcType(self, VpcType):
        self._VpcType = VpcType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccessGroupName = params.get("AccessGroupName")
        self._VpcType = params.get("VpcType")
        self._VpcId = params.get("VpcId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessGroupResponse(AbstractModel):
    """CreateAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroup: 权限组
        :type AccessGroup: :class:`tencentcloud.chdfs.v20201112.models.AccessGroup`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessGroup = None
        self._RequestId = None

    @property
    def AccessGroup(self):
        return self._AccessGroup

    @AccessGroup.setter
    def AccessGroup(self, AccessGroup):
        self._AccessGroup = AccessGroup

    @property
    def RequestId(self):
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
    """CreateAccessRules请求参数结构体

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
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def AccessGroupId(self):
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
    """CreateAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRules: 权限规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessRules: list of AccessRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessRules = None
        self._RequestId = None

    @property
    def AccessRules(self):
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def RequestId(self):
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


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param _CapacityQuota: 文件系统容量（byte），下限为1GB，上限为1PB，且必须是1GB的整数倍
        :type CapacityQuota: int
        :param _PosixAcl: 是否校验POSIX ACL
        :type PosixAcl: bool
        :param _Description: 文件系统描述，默认为空字符串
        :type Description: str
        :param _SuperUsers: 超级用户名列表，默认为空数组
        :type SuperUsers: list of str
        :param _RootInodeUser: 根目录Inode用户名，默认为hadoop
        :type RootInodeUser: str
        :param _RootInodeGroup: 根目录Inode组名，默认为supergroup
        :type RootInodeGroup: str
        :param _EnableRanger: 是否打开Ranger地址校验
        :type EnableRanger: bool
        :param _RangerServiceAddresses: Ranger地址列表，默认为空数组
        :type RangerServiceAddresses: list of str
        :param _Tags: 多个资源标签，可以为空数组
        :type Tags: list of Tag
        """
        self._FileSystemName = None
        self._CapacityQuota = None
        self._PosixAcl = None
        self._Description = None
        self._SuperUsers = None
        self._RootInodeUser = None
        self._RootInodeGroup = None
        self._EnableRanger = None
        self._RangerServiceAddresses = None
        self._Tags = None

    @property
    def FileSystemName(self):
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def CapacityQuota(self):
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def PosixAcl(self):
        return self._PosixAcl

    @PosixAcl.setter
    def PosixAcl(self, PosixAcl):
        self._PosixAcl = PosixAcl

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SuperUsers(self):
        return self._SuperUsers

    @SuperUsers.setter
    def SuperUsers(self, SuperUsers):
        self._SuperUsers = SuperUsers

    @property
    def RootInodeUser(self):
        return self._RootInodeUser

    @RootInodeUser.setter
    def RootInodeUser(self, RootInodeUser):
        self._RootInodeUser = RootInodeUser

    @property
    def RootInodeGroup(self):
        return self._RootInodeGroup

    @RootInodeGroup.setter
    def RootInodeGroup(self, RootInodeGroup):
        self._RootInodeGroup = RootInodeGroup

    @property
    def EnableRanger(self):
        return self._EnableRanger

    @EnableRanger.setter
    def EnableRanger(self, EnableRanger):
        self._EnableRanger = EnableRanger

    @property
    def RangerServiceAddresses(self):
        return self._RangerServiceAddresses

    @RangerServiceAddresses.setter
    def RangerServiceAddresses(self, RangerServiceAddresses):
        self._RangerServiceAddresses = RangerServiceAddresses

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._FileSystemName = params.get("FileSystemName")
        self._CapacityQuota = params.get("CapacityQuota")
        self._PosixAcl = params.get("PosixAcl")
        self._Description = params.get("Description")
        self._SuperUsers = params.get("SuperUsers")
        self._RootInodeUser = params.get("RootInodeUser")
        self._RootInodeGroup = params.get("RootInodeGroup")
        self._EnableRanger = params.get("EnableRanger")
        self._RangerServiceAddresses = params.get("RangerServiceAddresses")
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
        


class CreateFileSystemResponse(AbstractModel):
    """CreateFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystem: 文件系统
        :type FileSystem: :class:`tencentcloud.chdfs.v20201112.models.FileSystem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystem = None
        self._RequestId = None

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def RequestId(self):
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
    """CreateLifeCycleRules请求参数结构体

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
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleRules(self):
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
    """CreateLifeCycleRules返回参数结构体

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


class CreateMountPointRequest(AbstractModel):
    """CreateMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointName: 挂载点名称
        :type MountPointName: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _MountPointStatus: 挂载点状态（1：打开；2：关闭）
        :type MountPointStatus: int
        """
        self._MountPointName = None
        self._FileSystemId = None
        self._MountPointStatus = None

    @property
    def MountPointName(self):
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def MountPointStatus(self):
        return self._MountPointStatus

    @MountPointStatus.setter
    def MountPointStatus(self, MountPointStatus):
        self._MountPointStatus = MountPointStatus


    def _deserialize(self, params):
        self._MountPointName = params.get("MountPointName")
        self._FileSystemId = params.get("FileSystemId")
        self._MountPointStatus = params.get("MountPointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMountPointResponse(AbstractModel):
    """CreateMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoint: 挂载点
        :type MountPoint: :class:`tencentcloud.chdfs.v20201112.models.MountPoint`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountPoint = None
        self._RequestId = None

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def RequestId(self):
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
    """CreateRestoreTasks请求参数结构体

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
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def RestoreTasks(self):
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
    """CreateRestoreTasks返回参数结构体

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


class DeleteAccessGroupRequest(AbstractModel):
    """DeleteAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self._AccessGroupId = None

    @property
    def AccessGroupId(self):
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
    """DeleteAccessGroup返回参数结构体

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


class DeleteAccessRulesRequest(AbstractModel):
    """DeleteAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRuleIds: 多个权限规则ID，上限为10
        :type AccessRuleIds: list of int non-negative
        """
        self._AccessRuleIds = None

    @property
    def AccessRuleIds(self):
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
    """DeleteAccessRules返回参数结构体

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


class DeleteFileSystemRequest(AbstractModel):
    """DeleteFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
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
    """DeleteFileSystem返回参数结构体

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


class DeleteLifeCycleRulesRequest(AbstractModel):
    """DeleteLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifeCycleRuleIds: 多个生命周期规则ID，上限为10
        :type LifeCycleRuleIds: list of int non-negative
        """
        self._LifeCycleRuleIds = None

    @property
    def LifeCycleRuleIds(self):
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
    """DeleteLifeCycleRules返回参数结构体

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


class DeleteMountPointRequest(AbstractModel):
    """DeleteMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        """
        self._MountPointId = None

    @property
    def MountPointId(self):
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
    """DeleteMountPoint返回参数结构体

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


class DescribeAccessGroupRequest(AbstractModel):
    """DescribeAccessGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self._AccessGroupId = None

    @property
    def AccessGroupId(self):
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
        


class DescribeAccessGroupResponse(AbstractModel):
    """DescribeAccessGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroup: 权限组
        :type AccessGroup: :class:`tencentcloud.chdfs.v20201112.models.AccessGroup`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessGroup = None
        self._RequestId = None

    @property
    def AccessGroup(self):
        return self._AccessGroup

    @AccessGroup.setter
    def AccessGroup(self, AccessGroup):
        self._AccessGroup = AccessGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self._AccessGroup = AccessGroup()
            self._AccessGroup._deserialize(params.get("AccessGroup"))
        self._RequestId = params.get("RequestId")


class DescribeAccessGroupsRequest(AbstractModel):
    """DescribeAccessGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC网络ID
备注：入参只能指定VpcId和OwnerUin的其中一个
        :type VpcId: str
        :param _OwnerUin: 资源所属者Uin
        :type OwnerUin: int
        """
        self._VpcId = None
        self._OwnerUin = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessGroupsResponse(AbstractModel):
    """DescribeAccessGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroups: 权限组列表
        :type AccessGroups: list of AccessGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessGroups = None
        self._RequestId = None

    @property
    def AccessGroups(self):
        return self._AccessGroups

    @AccessGroups.setter
    def AccessGroups(self, AccessGroups):
        self._AccessGroups = AccessGroups

    @property
    def RequestId(self):
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
    """DescribeAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        """
        self._AccessGroupId = None

    @property
    def AccessGroupId(self):
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
        


class DescribeAccessRulesResponse(AbstractModel):
    """DescribeAccessRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRules: 权限规则列表
        :type AccessRules: list of AccessRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessRules = None
        self._RequestId = None

    @property
    def AccessRules(self):
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def RequestId(self):
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
    """DescribeFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
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
    """DescribeFileSystem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystem: 文件系统
        :type FileSystem: :class:`tencentcloud.chdfs.v20201112.models.FileSystem`
        :param _CapacityUsed: 文件系统已使用容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type CapacityUsed: int
        :param _ArchiveCapacityUsed: 已使用COS归档存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchiveCapacityUsed: int
        :param _StandardCapacityUsed: 已使用COS标准存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardCapacityUsed: int
        :param _DegradeCapacityUsed: 已使用COS低频存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type DegradeCapacityUsed: int
        :param _DeepArchiveCapacityUsed: 已使用COS深度归档存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type DeepArchiveCapacityUsed: int
        :param _IntelligentCapacityUsed: 已使用COS智能分层存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type IntelligentCapacityUsed: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystem = None
        self._CapacityUsed = None
        self._ArchiveCapacityUsed = None
        self._StandardCapacityUsed = None
        self._DegradeCapacityUsed = None
        self._DeepArchiveCapacityUsed = None
        self._IntelligentCapacityUsed = None
        self._RequestId = None

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def CapacityUsed(self):
        return self._CapacityUsed

    @CapacityUsed.setter
    def CapacityUsed(self, CapacityUsed):
        self._CapacityUsed = CapacityUsed

    @property
    def ArchiveCapacityUsed(self):
        return self._ArchiveCapacityUsed

    @ArchiveCapacityUsed.setter
    def ArchiveCapacityUsed(self, ArchiveCapacityUsed):
        self._ArchiveCapacityUsed = ArchiveCapacityUsed

    @property
    def StandardCapacityUsed(self):
        return self._StandardCapacityUsed

    @StandardCapacityUsed.setter
    def StandardCapacityUsed(self, StandardCapacityUsed):
        self._StandardCapacityUsed = StandardCapacityUsed

    @property
    def DegradeCapacityUsed(self):
        return self._DegradeCapacityUsed

    @DegradeCapacityUsed.setter
    def DegradeCapacityUsed(self, DegradeCapacityUsed):
        self._DegradeCapacityUsed = DegradeCapacityUsed

    @property
    def DeepArchiveCapacityUsed(self):
        return self._DeepArchiveCapacityUsed

    @DeepArchiveCapacityUsed.setter
    def DeepArchiveCapacityUsed(self, DeepArchiveCapacityUsed):
        self._DeepArchiveCapacityUsed = DeepArchiveCapacityUsed

    @property
    def IntelligentCapacityUsed(self):
        return self._IntelligentCapacityUsed

    @IntelligentCapacityUsed.setter
    def IntelligentCapacityUsed(self, IntelligentCapacityUsed):
        self._IntelligentCapacityUsed = IntelligentCapacityUsed

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self._FileSystem = FileSystem()
            self._FileSystem._deserialize(params.get("FileSystem"))
        self._CapacityUsed = params.get("CapacityUsed")
        self._ArchiveCapacityUsed = params.get("ArchiveCapacityUsed")
        self._StandardCapacityUsed = params.get("StandardCapacityUsed")
        self._DegradeCapacityUsed = params.get("DegradeCapacityUsed")
        self._DeepArchiveCapacityUsed = params.get("DeepArchiveCapacityUsed")
        self._IntelligentCapacityUsed = params.get("IntelligentCapacityUsed")
        self._RequestId = params.get("RequestId")


class DescribeFileSystemsRequest(AbstractModel):
    """DescribeFileSystems请求参数结构体

    """


class DescribeFileSystemsResponse(AbstractModel):
    """DescribeFileSystems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystems: 文件系统列表
        :type FileSystems: list of FileSystem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSystems = None
        self._RequestId = None

    @property
    def FileSystems(self):
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

    @property
    def RequestId(self):
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
    """DescribeLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
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
    """DescribeLifeCycleRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LifeCycleRules: 生命周期规则列表
        :type LifeCycleRules: list of LifeCycleRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LifeCycleRules = None
        self._RequestId = None

    @property
    def LifeCycleRules(self):
        return self._LifeCycleRules

    @LifeCycleRules.setter
    def LifeCycleRules(self, LifeCycleRules):
        self._LifeCycleRules = LifeCycleRules

    @property
    def RequestId(self):
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
    """DescribeMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        """
        self._MountPointId = None

    @property
    def MountPointId(self):
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
    """DescribeMountPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoint: 挂载点
        :type MountPoint: :class:`tencentcloud.chdfs.v20201112.models.MountPoint`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountPoint = None
        self._RequestId = None

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def RequestId(self):
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
    """DescribeMountPoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
备注：入参只能指定AccessGroupId、FileSystemId和OwnerUin的其中一个
        :type FileSystemId: str
        :param _AccessGroupId: 权限组ID
        :type AccessGroupId: str
        :param _OwnerUin: 资源所属者Uin
        :type OwnerUin: int
        """
        self._FileSystemId = None
        self._AccessGroupId = None
        self._OwnerUin = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._AccessGroupId = params.get("AccessGroupId")
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointsResponse(AbstractModel):
    """DescribeMountPoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPoints: 挂载点列表
        :type MountPoints: list of MountPoint
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MountPoints = None
        self._RequestId = None

    @property
    def MountPoints(self):
        return self._MountPoints

    @MountPoints.setter
    def MountPoints(self, MountPoints):
        self._MountPoints = MountPoints

    @property
    def RequestId(self):
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
    """DescribeResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
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
    """DescribeResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tags: 资源标签列表
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tags = None
        self._RequestId = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
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
    """DescribeRestoreTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
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
    """DescribeRestoreTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RestoreTasks: 回热任务列表
        :type RestoreTasks: list of RestoreTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RestoreTasks = None
        self._RequestId = None

    @property
    def RestoreTasks(self):
        return self._RestoreTasks

    @RestoreTasks.setter
    def RestoreTasks(self, RestoreTasks):
        self._RestoreTasks = RestoreTasks

    @property
    def RequestId(self):
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


class DisassociateAccessGroupsRequest(AbstractModel):
    """DisassociateAccessGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        :param _AccessGroupIds: 权限组ID列表
        :type AccessGroupIds: list of str
        """
        self._MountPointId = None
        self._AccessGroupIds = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def AccessGroupIds(self):
        return self._AccessGroupIds

    @AccessGroupIds.setter
    def AccessGroupIds(self, AccessGroupIds):
        self._AccessGroupIds = AccessGroupIds


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateAccessGroupsResponse(AbstractModel):
    """DisassociateAccessGroups返回参数结构体

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


class FileSystem(AbstractModel):
    """文件系统

    """

    def __init__(self):
        r"""
        :param _AppId: 资源所属用户AppId
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
        :param _SuperUsers: 超级用户名列表
        :type SuperUsers: list of str
        :param _PosixAcl: POSIX权限控制
        :type PosixAcl: bool
        :param _EnableRanger: 是否打开Ranger地址校验
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableRanger: bool
        :param _RangerServiceAddresses: Ranger地址列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RangerServiceAddresses: list of str
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
        self._SuperUsers = None
        self._PosixAcl = None
        self._EnableRanger = None
        self._RangerServiceAddresses = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FileSystemName(self):
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BlockSize(self):
        return self._BlockSize

    @BlockSize.setter
    def BlockSize(self, BlockSize):
        self._BlockSize = BlockSize

    @property
    def CapacityQuota(self):
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuperUsers(self):
        return self._SuperUsers

    @SuperUsers.setter
    def SuperUsers(self, SuperUsers):
        self._SuperUsers = SuperUsers

    @property
    def PosixAcl(self):
        return self._PosixAcl

    @PosixAcl.setter
    def PosixAcl(self, PosixAcl):
        self._PosixAcl = PosixAcl

    @property
    def EnableRanger(self):
        return self._EnableRanger

    @EnableRanger.setter
    def EnableRanger(self, EnableRanger):
        self._EnableRanger = EnableRanger

    @property
    def RangerServiceAddresses(self):
        return self._RangerServiceAddresses

    @RangerServiceAddresses.setter
    def RangerServiceAddresses(self, RangerServiceAddresses):
        self._RangerServiceAddresses = RangerServiceAddresses


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
        self._SuperUsers = params.get("SuperUsers")
        self._PosixAcl = params.get("PosixAcl")
        self._EnableRanger = params.get("EnableRanger")
        self._RangerServiceAddresses = params.get("RangerServiceAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycleRule(AbstractModel):
    """生命周期规则

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
        :param _Summary: 生命周期规则当前路径具体存储量
        :type Summary: :class:`tencentcloud.chdfs.v20201112.models.Summary`
        :param _LastSummaryTime: Summary更新时间
        :type LastSummaryTime: str
        """
        self._LifeCycleRuleId = None
        self._LifeCycleRuleName = None
        self._Path = None
        self._Transitions = None
        self._Status = None
        self._CreateTime = None
        self._Summary = None
        self._LastSummaryTime = None

    @property
    def LifeCycleRuleId(self):
        return self._LifeCycleRuleId

    @LifeCycleRuleId.setter
    def LifeCycleRuleId(self, LifeCycleRuleId):
        self._LifeCycleRuleId = LifeCycleRuleId

    @property
    def LifeCycleRuleName(self):
        return self._LifeCycleRuleName

    @LifeCycleRuleName.setter
    def LifeCycleRuleName(self, LifeCycleRuleName):
        self._LifeCycleRuleName = LifeCycleRuleName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Transitions(self):
        return self._Transitions

    @Transitions.setter
    def Transitions(self, Transitions):
        self._Transitions = Transitions

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def LastSummaryTime(self):
        return self._LastSummaryTime

    @LastSummaryTime.setter
    def LastSummaryTime(self, LastSummaryTime):
        self._LastSummaryTime = LastSummaryTime


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
        if params.get("Summary") is not None:
            self._Summary = Summary()
            self._Summary._deserialize(params.get("Summary"))
        self._LastSummaryTime = params.get("LastSummaryTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupRequest(AbstractModel):
    """ModifyAccessGroup请求参数结构体

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
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def AccessGroupName(self):
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def Description(self):
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
    """ModifyAccessGroup返回参数结构体

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


class ModifyAccessRulesRequest(AbstractModel):
    """ModifyAccessRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRules: 多个权限规则，上限为10
        :type AccessRules: list of AccessRule
        """
        self._AccessRules = None

    @property
    def AccessRules(self):
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
    """ModifyAccessRules返回参数结构体

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


class ModifyFileSystemRequest(AbstractModel):
    """ModifyFileSystem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _FileSystemName: 文件系统名称
        :type FileSystemName: str
        :param _Description: 文件系统描述
        :type Description: str
        :param _CapacityQuota: 文件系统容量（byte），下限为1GB，上限为1PB，且必须是1GB的整数倍
注意：修改的文件系统容量不能小于当前使用量
        :type CapacityQuota: int
        :param _SuperUsers: 超级用户名列表，可以为空数组
        :type SuperUsers: list of str
        :param _PosixAcl: 是否校验POSIX ACL
        :type PosixAcl: bool
        :param _EnableRanger: 是否打开Ranger地址校验
        :type EnableRanger: bool
        :param _RangerServiceAddresses: Ranger地址列表，可以为空数组
        :type RangerServiceAddresses: list of str
        """
        self._FileSystemId = None
        self._FileSystemName = None
        self._Description = None
        self._CapacityQuota = None
        self._SuperUsers = None
        self._PosixAcl = None
        self._EnableRanger = None
        self._RangerServiceAddresses = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FileSystemName(self):
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CapacityQuota(self):
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def SuperUsers(self):
        return self._SuperUsers

    @SuperUsers.setter
    def SuperUsers(self, SuperUsers):
        self._SuperUsers = SuperUsers

    @property
    def PosixAcl(self):
        return self._PosixAcl

    @PosixAcl.setter
    def PosixAcl(self, PosixAcl):
        self._PosixAcl = PosixAcl

    @property
    def EnableRanger(self):
        return self._EnableRanger

    @EnableRanger.setter
    def EnableRanger(self, EnableRanger):
        self._EnableRanger = EnableRanger

    @property
    def RangerServiceAddresses(self):
        return self._RangerServiceAddresses

    @RangerServiceAddresses.setter
    def RangerServiceAddresses(self, RangerServiceAddresses):
        self._RangerServiceAddresses = RangerServiceAddresses


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FileSystemName = params.get("FileSystemName")
        self._Description = params.get("Description")
        self._CapacityQuota = params.get("CapacityQuota")
        self._SuperUsers = params.get("SuperUsers")
        self._PosixAcl = params.get("PosixAcl")
        self._EnableRanger = params.get("EnableRanger")
        self._RangerServiceAddresses = params.get("RangerServiceAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemResponse(AbstractModel):
    """ModifyFileSystem返回参数结构体

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


class ModifyLifeCycleRulesRequest(AbstractModel):
    """ModifyLifeCycleRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifeCycleRules: 多个生命周期规则，上限为10
        :type LifeCycleRules: list of LifeCycleRule
        """
        self._LifeCycleRules = None

    @property
    def LifeCycleRules(self):
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
    """ModifyLifeCycleRules返回参数结构体

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


class ModifyMountPointRequest(AbstractModel):
    """ModifyMountPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        :param _MountPointName: 挂载点名称
        :type MountPointName: str
        :param _MountPointStatus: 挂载点状态
        :type MountPointStatus: int
        """
        self._MountPointId = None
        self._MountPointName = None
        self._MountPointStatus = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def MountPointName(self):
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def MountPointStatus(self):
        return self._MountPointStatus

    @MountPointStatus.setter
    def MountPointStatus(self, MountPointStatus):
        self._MountPointStatus = MountPointStatus


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._MountPointName = params.get("MountPointName")
        self._MountPointStatus = params.get("MountPointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMountPointResponse(AbstractModel):
    """ModifyMountPoint返回参数结构体

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


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags请求参数结构体

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
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Tags(self):
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
    """ModifyResourceTags返回参数结构体

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


class MountPoint(AbstractModel):
    """挂载点

    """

    def __init__(self):
        r"""
        :param _MountPointId: 挂载点ID
        :type MountPointId: str
        :param _MountPointName: 挂载点名称
        :type MountPointName: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _Status: 挂载点状态（1：打开；2：关闭）
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AccessGroupIds: 绑定的权限组ID列表
        :type AccessGroupIds: list of str
        """
        self._MountPointId = None
        self._MountPointName = None
        self._FileSystemId = None
        self._Status = None
        self._CreateTime = None
        self._AccessGroupIds = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def MountPointName(self):
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AccessGroupIds(self):
        return self._AccessGroupIds

    @AccessGroupIds.setter
    def AccessGroupIds(self, AccessGroupIds):
        self._AccessGroupIds = AccessGroupIds


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._MountPointName = params.get("MountPointName")
        self._FileSystemId = params.get("FileSystemId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreTask(AbstractModel):
    """回热任务

    """

    def __init__(self):
        r"""
        :param _RestoreTaskId: 回热任务ID
        :type RestoreTaskId: int
        :param _FilePath: 回热任务文件路径
        :type FilePath: str
        :param _Type: 回热任务类型（1：标准；2：极速；3：批量，暂时仅支持极速）
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
        return self._RestoreTaskId

    @RestoreTaskId.setter
    def RestoreTaskId(self, RestoreTaskId):
        self._RestoreTaskId = RestoreTaskId

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
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
        


class Summary(AbstractModel):
    """生命周期规则当前路径具体存储量信息

    """

    def __init__(self):
        r"""
        :param _CapacityUsed: 已使用容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type CapacityUsed: int
        :param _StandardCapacityUsed: 已使用COS标准存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardCapacityUsed: int
        :param _DegradeCapacityUsed: 已使用COS低频存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type DegradeCapacityUsed: int
        :param _ArchiveCapacityUsed: 已使用COS归档存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchiveCapacityUsed: int
        :param _DeepArchiveCapacityUsed: 已使用COS深度归档存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type DeepArchiveCapacityUsed: int
        :param _IntelligentCapacityUsed: 已使用COS智能分层存储容量（byte）
注意：此字段可能返回 null，表示取不到有效值。
        :type IntelligentCapacityUsed: int
        """
        self._CapacityUsed = None
        self._StandardCapacityUsed = None
        self._DegradeCapacityUsed = None
        self._ArchiveCapacityUsed = None
        self._DeepArchiveCapacityUsed = None
        self._IntelligentCapacityUsed = None

    @property
    def CapacityUsed(self):
        return self._CapacityUsed

    @CapacityUsed.setter
    def CapacityUsed(self, CapacityUsed):
        self._CapacityUsed = CapacityUsed

    @property
    def StandardCapacityUsed(self):
        return self._StandardCapacityUsed

    @StandardCapacityUsed.setter
    def StandardCapacityUsed(self, StandardCapacityUsed):
        self._StandardCapacityUsed = StandardCapacityUsed

    @property
    def DegradeCapacityUsed(self):
        return self._DegradeCapacityUsed

    @DegradeCapacityUsed.setter
    def DegradeCapacityUsed(self, DegradeCapacityUsed):
        self._DegradeCapacityUsed = DegradeCapacityUsed

    @property
    def ArchiveCapacityUsed(self):
        return self._ArchiveCapacityUsed

    @ArchiveCapacityUsed.setter
    def ArchiveCapacityUsed(self, ArchiveCapacityUsed):
        self._ArchiveCapacityUsed = ArchiveCapacityUsed

    @property
    def DeepArchiveCapacityUsed(self):
        return self._DeepArchiveCapacityUsed

    @DeepArchiveCapacityUsed.setter
    def DeepArchiveCapacityUsed(self, DeepArchiveCapacityUsed):
        self._DeepArchiveCapacityUsed = DeepArchiveCapacityUsed

    @property
    def IntelligentCapacityUsed(self):
        return self._IntelligentCapacityUsed

    @IntelligentCapacityUsed.setter
    def IntelligentCapacityUsed(self, IntelligentCapacityUsed):
        self._IntelligentCapacityUsed = IntelligentCapacityUsed


    def _deserialize(self, params):
        self._CapacityUsed = params.get("CapacityUsed")
        self._StandardCapacityUsed = params.get("StandardCapacityUsed")
        self._DegradeCapacityUsed = params.get("DegradeCapacityUsed")
        self._ArchiveCapacityUsed = params.get("ArchiveCapacityUsed")
        self._DeepArchiveCapacityUsed = params.get("DeepArchiveCapacityUsed")
        self._IntelligentCapacityUsed = params.get("IntelligentCapacityUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """资源标签。

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
        


class Transition(AbstractModel):
    """生命周期规则转换属性

    """

    def __init__(self):
        r"""
        :param _Days: 触发时间（单位天）
        :type Days: int
        :param _Type: 转换类型（1：归档；2：删除；3：低频；4：深度归档；5：智能分层）
        :type Type: int
        """
        self._Days = None
        self._Type = None

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Type(self):
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
        