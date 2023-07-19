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


class ClientToken(AbstractModel):
    """查询Client Token

    """

    def __init__(self):
        r"""
        :param _NodeIp: 节点 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeIp: str
        :param _LocalDirectory: 挂载点
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDirectory: str
        :param _GooseFSDirectory: 可以访问的 GooseFS 目录
注意：此字段可能返回 null，表示取不到有效值。
        :type GooseFSDirectory: str
        :param _Token: token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        """
        self._NodeIp = None
        self._LocalDirectory = None
        self._GooseFSDirectory = None
        self._Token = None

    @property
    def NodeIp(self):
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def LocalDirectory(self):
        return self._LocalDirectory

    @LocalDirectory.setter
    def LocalDirectory(self, LocalDirectory):
        self._LocalDirectory = LocalDirectory

    @property
    def GooseFSDirectory(self):
        return self._GooseFSDirectory

    @GooseFSDirectory.setter
    def GooseFSDirectory(self, GooseFSDirectory):
        self._GooseFSDirectory = GooseFSDirectory

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._NodeIp = params.get("NodeIp")
        self._LocalDirectory = params.get("LocalDirectory")
        self._GooseFSDirectory = params.get("GooseFSDirectory")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterRole(AbstractModel):
    """ClusterRole

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RoleName: 角色名
        :type RoleName: str
        :param _Description: 描述
        :type Description: str
        :param _DirectoryList: 目录列表
        :type DirectoryList: list of str
        """
        self._ClusterId = None
        self._RoleName = None
        self._Description = None
        self._DirectoryList = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DirectoryList(self):
        return self._DirectoryList

    @DirectoryList.setter
    def DirectoryList(self, DirectoryList):
        self._DirectoryList = DirectoryList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RoleName = params.get("RoleName")
        self._Description = params.get("Description")
        self._DirectoryList = params.get("DirectoryList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataRepositoryTaskRequest(AbstractModel):
    """CreateDataRepositoryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskType: 数据流通任务类型, FS_TO_COS(文件系统到COS Bucket),或者COS_TO_FS(COS Bucket到文件系统)
        :type TaskType: str
        :param _Bucket: COS存储桶名
        :type Bucket: str
        :param _FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param _TaskPath: 对于FS_TO_COS, TaskPath是Bucket映射目录的相对路径, 对于COS_TO_FS是COS上的路径。如果置为空, 则表示全部数据
        :type TaskPath: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _RepositoryType: 数据流通方式 MSP_AFM 手动加载  RAW_AFM 按需加载
        :type RepositoryType: str
        :param _TextLocation: 文件列表下载地址，以http开头
        :type TextLocation: str
        """
        self._TaskType = None
        self._Bucket = None
        self._FileSystemId = None
        self._TaskPath = None
        self._TaskName = None
        self._RepositoryType = None
        self._TextLocation = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def TaskPath(self):
        return self._TaskPath

    @TaskPath.setter
    def TaskPath(self, TaskPath):
        self._TaskPath = TaskPath

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def RepositoryType(self):
        return self._RepositoryType

    @RepositoryType.setter
    def RepositoryType(self, RepositoryType):
        self._RepositoryType = RepositoryType

    @property
    def TextLocation(self):
        return self._TextLocation

    @TextLocation.setter
    def TextLocation(self, TextLocation):
        self._TextLocation = TextLocation


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._Bucket = params.get("Bucket")
        self._FileSystemId = params.get("FileSystemId")
        self._TaskPath = params.get("TaskPath")
        self._TaskName = params.get("TaskName")
        self._RepositoryType = params.get("RepositoryType")
        self._TextLocation = params.get("TextLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataRepositoryTaskResponse(AbstractModel):
    """CreateDataRepositoryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeClusterClientTokenRequest(AbstractModel):
    """DescribeClusterClientToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterClientTokenResponse(AbstractModel):
    """DescribeClusterClientToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientTokens: 客户端凭证
        :type ClientTokens: list of ClientToken
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientTokens = None
        self._RequestId = None

    @property
    def ClientTokens(self):
        return self._ClientTokens

    @ClientTokens.setter
    def ClientTokens(self, ClientTokens):
        self._ClientTokens = ClientTokens

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClientTokens") is not None:
            self._ClientTokens = []
            for item in params.get("ClientTokens"):
                obj = ClientToken()
                obj._deserialize(item)
                self._ClientTokens.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterRoleTokenRequest(AbstractModel):
    """DescribeClusterRoleToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RoleName: 角色名
        :type RoleName: str
        """
        self._ClusterId = None
        self._RoleName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterRoleTokenResponse(AbstractModel):
    """DescribeClusterRoleToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleTokens: 角色凭证
        :type RoleTokens: list of RoleToken
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleTokens = None
        self._RequestId = None

    @property
    def RoleTokens(self):
        return self._RoleTokens

    @RoleTokens.setter
    def RoleTokens(self, RoleTokens):
        self._RoleTokens = RoleTokens

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RoleTokens") is not None:
            self._RoleTokens = []
            for item in params.get("RoleTokens"):
                obj = RoleToken()
                obj._deserialize(item)
                self._RoleTokens.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterRolesRequest(AbstractModel):
    """DescribeClusterRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RoleName: 角色名
        :type RoleName: str
        """
        self._ClusterId = None
        self._RoleName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterRolesResponse(AbstractModel):
    """DescribeClusterRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterRoles: 集群角色
        :type ClusterRoles: list of ClusterRole
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterRoles = None
        self._RequestId = None

    @property
    def ClusterRoles(self):
        return self._ClusterRoles

    @ClusterRoles.setter
    def ClusterRoles(self, ClusterRoles):
        self._ClusterRoles = ClusterRoles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterRoles") is not None:
            self._ClusterRoles = []
            for item in params.get("ClusterRoles"):
                obj = ClusterRole()
                obj._deserialize(item)
                self._ClusterRoles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataRepositoryTaskStatusRequest(AbstractModel):
    """DescribeDataRepositoryTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: task id
        :type TaskId: str
        :param _FileSystemId: file system id
        :type FileSystemId: str
        """
        self._TaskId = None
        self._FileSystemId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataRepositoryTaskStatusResponse(AbstractModel):
    """DescribeDataRepositoryTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _Status: 任务状态 0(初始化中), 1(运行中), 2(已完成), 3(任务失败)
        :type Status: int
        :param _FinishedFileNumber: 已完成的文件数量
        :type FinishedFileNumber: int
        :param _FinishedCapacity: 已完成的数据量
        :type FinishedCapacity: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._FinishedFileNumber = None
        self._FinishedCapacity = None
        self._RequestId = None

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
    def FinishedFileNumber(self):
        return self._FinishedFileNumber

    @FinishedFileNumber.setter
    def FinishedFileNumber(self, FinishedFileNumber):
        self._FinishedFileNumber = FinishedFileNumber

    @property
    def FinishedCapacity(self):
        return self._FinishedCapacity

    @FinishedCapacity.setter
    def FinishedCapacity(self, FinishedCapacity):
        self._FinishedCapacity = FinishedCapacity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._FinishedFileNumber = params.get("FinishedFileNumber")
        self._FinishedCapacity = params.get("FinishedCapacity")
        self._RequestId = params.get("RequestId")


class RoleToken(AbstractModel):
    """角色凭证

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名
        :type RoleName: str
        :param _Token: 用于goosefs client/sdk等
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        """
        self._RoleName = None
        self._Token = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        